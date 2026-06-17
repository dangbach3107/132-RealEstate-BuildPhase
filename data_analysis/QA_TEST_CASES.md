# QA Test Cases - HomeValue AI Chatbot

File này là bộ test case để team QA/PM chạy trước demo hoặc trước khi merge thay đổi lớn vào chatbot/API.

Quy ước:
- `Pass`: kết quả đúng như expected.
- `Fail`: sai intent, sai số liệu, lỗi API, trả lời khó hiểu hoặc bịa dữ liệu.
- `Blocked`: không chạy được do thiếu env/data/server.
- Với test liên quan LLM, cần kiểm tra ý nghĩa câu trả lời thay vì so exact text, vì wording có thể thay đổi.

## 01. Chatbot Intent & Routing

| ID | Mục tiêu | Input | Điều kiện | Expected | Trạng thái | Owner | Bug/Link | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| CHAT-001 | Chào hỏi không gọi valuation | `hello` | API/chatbot chạy được | `intent = greeting`, `missing_fields = []`, `valuation = null`, câu trả lời chào tự nhiên | Chưa chạy | QA |  | Automated: `test_chat_greets_without_calling_valuation` |
| CHAT-002 | Hỏi help/hướng dẫn | `bạn có thể làm gì` | API/chatbot chạy được | `intent = help`, trả lời các khả năng chính: định giá, trend, snapshot/bảng giá | Chưa chạy | QA |  | Automated added |
| CHAT-003 | Cảm ơn | `cảm ơn` | API/chatbot chạy được | `intent = thanks`, không chạy valuation, trả lời ngắn gọn | Chưa chạy | QA |  |  |
| CHAT-004 | Hỏi trend | `xu hướng thị trường Vinhomes Smart City căn hộ` | Có market data | `intent = trend`, có `data.windows`, answer có median hoặc nói chưa đủ dữ liệu | Chưa chạy | QA |  | Automated added |
| CHAT-005 | Hỏi bảng giá/snapshot | `bảng giá tham khảo Vinhomes Smart City căn hộ` | Có snapshot data hoặc fallback no_snapshot | `intent = snapshot`, không chạy valuation, trả về snapshot refs nếu có | Chưa chạy | QA |  | Automated added |

## 02. Missing Information

| ID | Mục tiêu | Input | Điều kiện | Expected | Trạng thái | Owner | Bug/Link | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| MISS-001 | Thiếu project và diện tích | `định giá căn 2PN` | Có retrieval data | `intent = valuation`, `missing_fields` gồm `project`, `area_m2`, answer hỏi bổ sung đúng thông tin | Chưa chạy | QA |  | Automated: `test_chat_asks_for_missing_fields` |
| MISS-002 | Thiếu diện tích nhưng có project | `định giá căn hộ Vinhomes Smart City 2PN` | Có retrieval data | `missing_fields = ["area_m2"]`, có gợi ý diện tích từ dữ liệu gần nhất | Chưa chạy | QA |  | Automated: `test_chat_suggests_nearest_info_when_area_missing` |
| MISS-003 | Thiếu project khi hỏi trend | `xu hướng giá căn hộ 2PN` | Có retrieval data | `intent = trend`, hỏi thêm dự án/khu đô thị | Chưa chạy | QA |  |  |
| MISS-004 | Thiếu project khi hỏi snapshot | `bảng giá căn hộ tham khảo` | Có retrieval data | `intent = snapshot`, hỏi thêm dự án/khu đô thị | Chưa chạy | QA |  |  |

## 03. Valuation - Sale

| ID | Mục tiêu | Input | Điều kiện | Expected | Trạng thái | Owner | Bug/Link | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| SALE-001 | Định giá bán căn hộ đủ dữ liệu | `Định giá bán căn hộ Vinhomes Smart City 54.2m2 2PN full nội thất` | Có listing data | `intent = valuation`, có `valuation.sample_size > 0`, `extracted.project = vinhomes-smart-city`, answer có P50/khoảng giá/độ tin cậy | Chưa chạy | QA |  | Automated: `test_chat_valuation_from_vietnamese_text` |
| SALE-002 | Kiểm tra LLM không trả hardcode trực tiếp | Cùng SALE-001 | LLM enabled hoặc monkeypatch test | Luồng gọi `generate_answer("valuation")`, context có `example_answer`; answer cuối do LLM/fallback sinh | Chưa chạy | QA |  | Automated: `test_chat_valuation_routes_answer_through_llm_prompt` |
| SALE-003 | Căn có view/nội thất | `Định giá bán Vinhomes Smart City 60m2 2PN view hồ full nội thất` | Có listing data | Answer có nhắc yếu tố view/nội thất nếu parse được; không bịa giao dịch chốt | Chưa chạy | QA |  |  |
| SALE-004 | Dự án không nhận diện được | `Định giá căn hộ dự án ABC 60m2 2PN` | Config không có project ABC | Bot hỏi lại project hoặc báo chưa nhận diện; không tự map bừa sang Vinhomes | Chưa chạy | QA |  |  |

## 04. Valuation - Rent

| ID | Mục tiêu | Input | Điều kiện | Expected | Trạng thái | Owner | Bug/Link | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| RENT-001 | Định giá thuê đủ dữ liệu | `Tôi có căn Vinhomes Smart City 54m², 2 phòng ngủ. Cho thuê được bao nhiêu?` | Có rent/listing data | `intent = valuation`, `extracted.purpose = rent`, answer có giá thuê/tháng, P50, độ tin cậy, phân tích | Chưa chạy | QA |  | Automated: `test_chat_rent_valuation_uses_structured_answer_format` |
| RENT-002 | Thuê nhưng thiếu diện tích | `Cho thuê căn Vinhomes Smart City 2PN được bao nhiêu?` | Có retrieval data | Bot hỏi thêm diện tích, không định giá bừa | Chưa chạy | QA |  |  |
| RENT-003 | Thuê có nội thất/view | `Cho thuê Vinhomes Smart City 55m2 2PN full nội thất view nội khu` | Có rent/listing data | Answer có nhắc yếu tố nội thất/view nếu parse được; không nói chắc giá chốt | Chưa chạy | QA |  |  |

## 05. Trend & Snapshot

| ID | Mục tiêu | Input | Điều kiện | Expected | Trạng thái | Owner | Bug/Link | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| TREND-001 | Trend theo project | `xu hướng thị trường Vinhomes Smart City căn hộ` | Có market data | Có `data.windows`, answer nêu median/mẫu hoặc caveat chưa đủ dữ liệu | Chưa chạy | QA |  | Automated added |
| TREND-002 | Trend thuê | `trend giá thuê Vinhomes Smart City căn hộ 2PN` | Có rent data | `purpose = rent`, answer nói giá thuê, không nói giá bán | Chưa chạy | QA |  |  |
| SNAP-001 | Snapshot/bảng giá | `bảng giá tham khảo Vinhomes Smart City căn hộ` | Có snapshot data | `intent = snapshot`, trả số lượng snapshot hoặc no_snapshot rõ ràng | Chưa chạy | QA |  | Automated added |
| SNAP-002 | Snapshot thiếu project | `bảng giá căn hộ tham khảo` | Có retrieval data | Bot hỏi thêm project | Chưa chạy | QA |  |  |

## 06. LLM Answer Quality

| ID | Mục tiêu | Input | Điều kiện | Expected | Trạng thái | Owner | Bug/Link | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| LLM-001 | Câu trả lời tự nhiên, không máy móc | SALE-001 chạy 3 lần | `VALUATION_LLM_ENABLED=1`, có API key/model | Wording có thể khác nhau, vẫn giữ P50/P10-P90/sample/confidence đúng context | Chưa chạy | QA/Backend |  | Không so exact text. |
| LLM-002 | Không bịa số liệu | SALE-001 | LLM enabled | Không xuất hiện dự án, giao dịch chốt, nguồn dữ liệu không có trong context | Chưa chạy | QA/Backend |  | Check guardrail. |
| LLM-003 | Fallback khi tắt LLM | SALE-001 | `VALUATION_LLM_ENABLED=0` | API vẫn trả answer hợp lệ, có bullet, không crash | Chưa chạy | Backend |  | Automated đang dùng LLM disabled trong tests. |
| LLM-004 | Output format | Các case chat chính | API/chatbot chạy được | Mỗi dòng bắt đầu bằng `- `, không markdown bold, không nhắc API/prompt/system message | Chưa chạy | QA |  |  |

## 07. API Smoke

| ID | Mục tiêu | Endpoint/Input | Điều kiện | Expected | Trạng thái | Owner | Bug/Link | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| API-001 | Health check | `GET /health` | Server chạy | HTTP 200, `status = ok` | Chưa chạy | QA |  | Automated: `test_health_endpoint` |
| API-002 | Projects list | `GET /projects` | Config loaded | HTTP 200, có `vinhomes-ocean-park` | Chưa chạy | QA |  | Automated: `test_projects_endpoint` |
| API-003 | Price snapshots | `GET /price-snapshots?project=vinhomes-smart-city&property_type=apartment` | DB loaded | HTTP 200, response là list | Chưa chạy | QA |  | Automated: `test_price_snapshots_endpoint` |

## 08. Regression Checklist Trước Demo

| ID | Việc cần check | Expected | Trạng thái | Owner | Ghi chú |
|---|---|---|---|---|---|
| REG-001 | Chạy automated tests chính | Test pass hoặc ghi rõ test bị blocked do env | Chưa chạy | Backend | `python -m pytest tests/test_api.py::test_chat_valuation_routes_answer_through_llm_prompt -vv` |
| REG-002 | Chạy 5 câu hỏi demo chính | Greeting, missing info, sale valuation, rent valuation, trend/snapshot đều ổn | Chưa chạy | QA/PM | Ghi lại answer nếu cần. |
| REG-003 | Kiểm tra `.env` production | Có `OPENAI_API_KEY`, `MODEL`, storage config đúng | Chưa chạy | Backend | Không commit secret. |
| REG-004 | Kiểm tra dữ liệu | DB/Mongo có listing/snapshot cần thiết | Chưa chạy | Data | Nếu thiếu data thì demo có thể no data. |
| REG-005 | Kiểm tra PM worksheet | Owner/deadline/link demo đã điền | Chưa chạy | PM | Tránh sheet chỉ là template. |
