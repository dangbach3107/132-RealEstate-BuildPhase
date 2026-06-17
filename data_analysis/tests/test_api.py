from pathlib import Path

from fastapi.testclient import TestClient

from app import chatbot as chatbot_module
from app.main import DB_PATH, app, config
from app.schemas import ChatRequest


def test_health_endpoint():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_projects_endpoint():
    client = TestClient(app)
    response = client.get("/projects")
    assert response.status_code == 200
    assert any(project["slug"] == "vinhomes-ocean-park" for project in response.json())


def test_price_snapshots_endpoint():
    client = TestClient(app)
    response = client.get("/price-snapshots", params={"project": "vinhomes-smart-city", "property_type": "apartment"})
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_chat_asks_for_missing_fields():
    client = TestClient(app)
    response = client.post("/chat", json={"message": "định giá căn 2PN"})
    assert response.status_code == 200
    body = response.json()
    assert body["intent"] == "valuation"
    assert "project" in body["missing_fields"]
    assert "area_m2" in body["missing_fields"]
    suggestions = body["data"]["retrieval_suggestions"]
    assert suggestions["nearest_projects"]
    assert suggestions["hint_text"]
    assert "\n" in body["answer"]
    assert body["answer"].startswith("- ")


def test_chat_suggests_nearest_info_when_area_missing():
    client = TestClient(app)
    response = client.post("/chat", json={"message": "định giá căn hộ Vinhomes Smart City 2PN"})
    assert response.status_code == 200
    body = response.json()
    assert body["intent"] == "valuation"
    assert body["missing_fields"] == ["area_m2"]
    suggestions = body["data"]["retrieval_suggestions"]
    assert suggestions["area_hint"]["sample_size"] > 0
    assert "Vinhomes Smart City" in suggestions["hint_text"]
    assert "diện tích" in body["answer"].lower()
    assert "\n" in body["answer"]
    assert body["answer"].startswith("- ")


def test_chat_greets_without_calling_valuation():
    client = TestClient(app)
    response = client.post("/chat", json={"message": "hello"})
    assert response.status_code == 200
    body = response.json()
    assert body["intent"] == "greeting"
    assert body["missing_fields"] == []
    assert body["extracted"] == {}
    assert body["answer"]
    assert body["answer"].startswith("- ")
    assert body["valuation"] is None


def test_chat_help_intent_direct():
    response = chatbot_module.handle_chat(
        ChatRequest(message="bạn có thể làm gì"),
        config(),
        DB_PATH,
    )

    assert response.intent == "help"
    assert response.missing_fields == []
    assert response.valuation is None
    assert response.answer.startswith("- ")


def test_chat_valuation_from_vietnamese_text():
    client = TestClient(app)
    response = client.post(
        "/chat",
        json={"message": "Định giá bán căn hộ Vinhomes Smart City 54.2m2 2PN full nội thất"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["intent"] == "valuation"
    assert body["valuation"]["sample_size"] > 0
    assert body["extracted"]["project"] == "vinhomes-smart-city"


def test_chat_valuation_routes_answer_through_llm_prompt(monkeypatch):
    calls = {}

    def fake_generate_answer(intent, message, context, fallback_key=None):
        calls["intent"] = intent
        calls["message"] = message
        calls["context"] = context
        calls["fallback_key"] = fallback_key
        return "- Đây là câu trả lời tự nhiên do LLM sinh từ ví dụ."

    monkeypatch.setattr(chatbot_module, "generate_answer", fake_generate_answer)

    response = chatbot_module.handle_chat(
        ChatRequest(message="Định giá bán căn hộ Vinhomes Smart City 54.2m2 2PN full nội thất"),
        config(),
        DB_PATH,
    )

    assert response.answer == "- Đây là câu trả lời tự nhiên do LLM sinh từ ví dụ."
    assert calls["intent"] == "valuation"
    assert calls["fallback_key"] == "valuation"
    assert "example_answer" in calls["context"]
    assert "Ước tính giá bán hợp lý:" in calls["context"]["example_answer"]
    assert response.valuation is not None
    assert calls["context"]["sample_size"] == response.valuation["sample_size"]


def test_chat_trend_intent_direct():
    response = chatbot_module.handle_chat(
        ChatRequest(message="xu hướng thị trường Vinhomes Smart City căn hộ"),
        config(),
        DB_PATH,
    )

    assert response.intent == "trend"
    assert response.data is not None
    assert response.data["project"] == "Vinhomes Smart City"
    assert "windows" in response.data
    assert response.answer.startswith("- ")


def test_chat_snapshot_intent_direct():
    response = chatbot_module.handle_chat(
        ChatRequest(message="bảng giá tham khảo Vinhomes Smart City căn hộ"),
        config(),
        DB_PATH,
    )

    assert response.intent == "snapshot"
    assert response.data is not None
    assert "reference_price_snapshots" in response.data
    assert response.answer.startswith("- ")


def test_chat_rent_valuation_uses_structured_answer_format():
    client = TestClient(app)
    response = client.post(
        "/chat",
        json={"message": "Tôi có căn Vinhomes Smart City 54m², 2 phòng ngủ. Cho thuê được bao nhiêu?"},
    )
    assert response.status_code == 200
    body = response.json()
    answer = body["answer"]
    assert body["intent"] == "valuation"
    assert body["extracted"]["purpose"] == "rent"
    assert answer.startswith("- Ước tính giá thuê hợp lý:")
    assert "Giá trung vị thị trường hiện tại:" in answer
    assert "Độ tin cậy:" in answer
    assert "Phân tích:" in answer
    assert "Các yếu tố có thể làm thay đổi giá:" in answer
    assert "Để định giá chính xác hơn, vui lòng cung cấp:" in answer
