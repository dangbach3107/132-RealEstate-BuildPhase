from __future__ import annotations

import os
import re
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml
from pydantic import ValidationError

from app.config import AppConfig
from app.env import PROJECT_ROOT, load_app_env
from app.llm import generate_answer
from app.normalization import infer_project_slug, infer_property_type, normalize_furniture, normalize_view, parse_area, parse_bedrooms
from app.retrieval import missing_info_retrieval
from app.schemas import ChatRequest, ChatResponse, PropertyInput, ValuationResponse
from app.text import compact_spaces, text_key
from app.valuation import estimate_property, market_trends, price_snapshot_references


def handle_chat(payload: ChatRequest, config: AppConfig, db_path: str | Path) -> ChatResponse:
    message = compact_spaces(payload.message)
    intent = _detect_intent(message)
    parsed = _parse_property_fields(message, config)
    if payload.property:
        parsed = {**payload.property.model_dump(exclude_none=True), **{key: value for key, value in parsed.items() if value is not None}}

    if intent == "greeting":
        return _handle_simple_intent("greeting", message, config)
    if intent == "thanks":
        return _handle_simple_intent("thanks", message, config)
    if intent == "help":
        return _handle_simple_intent("help", message, config)
    if intent == "trend":
        return _handle_trend(message, parsed, config, db_path)
    if intent == "snapshot":
        return _handle_snapshot(message, parsed, config, db_path)
    return _handle_valuation(message, parsed, config, db_path)


def _handle_simple_intent(intent: str, message: str, config: AppConfig) -> ChatResponse:
    context = {
        "market": config.raw.get("market", {}),
        "projects": [{"slug": project.slug, "name": project.name} for project in config.projects],
    }
    return ChatResponse(
        answer=generate_answer(intent, message, context),
        missing_fields=[],
        intent=intent,
        extracted={},
    )


def _handle_valuation(message: str, fields: dict[str, Any], config: AppConfig, db_path: str | Path) -> ChatResponse:
    missing = _missing_for_valuation(fields)
    if missing:
        context = _missing_context(missing, fields, message, config, db_path)
        return ChatResponse(
            answer=generate_answer(
                "valuation_missing",
                message,
                context,
                fallback_key="valuation_missing",
            ),
            missing_fields=missing,
            data={"retrieval_suggestions": context.get("retrieval_suggestions")},
            intent="valuation",
            extracted=fields,
        )
    try:
        prop = PropertyInput(**fields)
        result = estimate_property(prop, config, db_path)
    except (ValidationError, ValueError) as exc:
        return ChatResponse(
            answer=generate_answer("error", message, {"error": str(exc), "fields": fields}, fallback_key="error"),
            missing_fields=[],
            intent="valuation",
            extracted=fields,
        )

    refs = result.reference_price_snapshots
    answer_example = _format_valuation_answer(result, prop)
    answer = generate_answer(
        "valuation",
        message,
        _valuation_answer_context(result, prop, answer_example),
        fallback_key="valuation",
    )
    return ChatResponse(
        answer=answer,
        missing_fields=[],
        valuation=result.model_dump(),
        data={"reference_price_snapshots": [item.model_dump() for item in refs]},
        intent="valuation",
        extracted=fields,
    )


def _handle_trend(message: str, fields: dict[str, Any], config: AppConfig, db_path: str | Path) -> ChatResponse:
    missing = _missing_project(fields)
    if missing:
        context = _missing_context(missing, fields, message, config, db_path)
        return ChatResponse(
            answer=generate_answer("trend_missing", message, context, fallback_key="trend_missing"),
            missing_fields=missing,
            data={"retrieval_suggestions": context.get("retrieval_suggestions")},
            intent="trend",
            extracted=fields,
        )
    try:
        data = market_trends(
            config,
            fields["project"],
            fields.get("purpose", "sale"),
            fields.get("property_type"),
            fields.get("bedrooms"),
            db_path,
        )
    except ValueError as exc:
        return ChatResponse(
            answer=generate_answer("error", message, {"error": str(exc), "fields": fields}, fallback_key="error"),
            missing_fields=[],
            intent="trend",
            extracted=fields,
        )

    windows = data.get("windows", {})
    primary = windows.get("1m") or windows.get("3m") or {}
    refs = data.get("reference_price_snapshots") or []
    answer = generate_answer(
        "trend",
        message,
        {
            "project": data.get("project"),
            "property_type": data.get("property_type"),
            "property_type_label": _property_type_label(data.get("property_type") or "all"),
            "purpose": data.get("purpose"),
            "purpose_label": _purpose_label(data.get("purpose")),
            "bedrooms": data.get("bedrooms"),
            "windows": windows,
            "primary_median": primary.get("median"),
            "primary_median_text": _format_vnd(primary.get("median")) if primary.get("median") else "chưa đủ dữ liệu",
            "primary_sample_size": primary.get("sample_size", 0),
            "snapshot_reference_count": len(refs),
            "snapshot_count_text": _snapshot_count_text(len(refs)),
            "caveat": data.get("caveat"),
        },
    )
    return ChatResponse(answer=answer, intent="trend", extracted=fields, data=data)


def _handle_snapshot(message: str, fields: dict[str, Any], config: AppConfig, db_path: str | Path) -> ChatResponse:
    missing = _missing_project(fields)
    if missing:
        context = _missing_context(missing, fields, message, config, db_path)
        return ChatResponse(
            answer=generate_answer(
                "snapshot_missing",
                message,
                context,
                fallback_key="snapshot_missing",
            ),
            missing_fields=missing,
            data={"retrieval_suggestions": context.get("retrieval_suggestions")},
            intent="snapshot",
            extracted=fields,
        )
    refs = price_snapshot_references(
        config,
        fields["project"],
        fields.get("purpose", "sale"),
        fields.get("property_type"),
        db_path=db_path,
    )
    if not refs:
        return ChatResponse(
            answer=generate_answer("no_snapshot", message, {"fields": fields}, fallback_key="no_snapshot"),
            intent="snapshot",
            extracted=fields,
            data={"reference_price_snapshots": []},
    )
    first = refs[0]
    range_text = _snapshot_range_text(first.model_dump())
    answer = generate_answer(
        "snapshot",
        message,
        {
            "project": first.project,
            "property_type": first.property_type,
            "property_type_label": _property_type_label(first.property_type),
            "purpose": first.purpose,
            "purpose_label": _purpose_label(first.purpose),
            "reference_count": len(refs),
            "first_label": first.label or first.property_type,
            "first_reference": first.model_dump(),
            "range_text": range_text,
        },
    )
    return ChatResponse(
        answer=answer,
        intent="snapshot",
        extracted=fields,
        data={"reference_price_snapshots": [item.model_dump() for item in refs]},
    )


def _detect_intent(message: str) -> str:
    key = text_key(message)
    rules = _intent_rules()
    if _is_greeting_only(key, rules):
        return "greeting"
    if _is_thanks_only(key, rules):
        return "thanks"
    if any(term in key for term in rules.get("help_terms", [])):
        return "help"
    if any(term in key for term in rules.get("trend_terms", [])):
        return "trend"
    if any(term in key for term in rules.get("snapshot_terms", [])):
        return "snapshot"
    return "valuation"


@lru_cache(maxsize=1)
def _intent_rules() -> dict[str, list[str]]:
    load_app_env()
    path = Path(os.getenv("VALUATION_INTENT_RULES_PATH") or PROJECT_ROOT / "prompts" / "intent_rules.yaml")
    data = yaml.safe_load(path.read_text(encoding="utf-8")) if path.exists() else {}
    return {str(key): [str(item) for item in value] for key, value in (data or {}).items() if isinstance(value, list)}


def _is_greeting_only(key: str, rules: dict[str, list[str]]) -> bool:
    normalized = compact_spaces(re.sub(r"[^a-z0-9 ]+", " ", key)).strip()
    if not normalized:
        return True
    if normalized in set(rules.get("greeting_phrases", [])):
        return True
    tokens = normalized.split()
    domain_terms = set(rules.get("domain_terms", []))
    greeting_starts = set(rules.get("greeting_starts", []))
    return len(tokens) <= 3 and tokens[0] in greeting_starts and not any(
        token in domain_terms for token in tokens[1:]
    )


def _is_thanks_only(key: str, rules: dict[str, list[str]]) -> bool:
    normalized = compact_spaces(re.sub(r"[^a-z0-9 ]+", " ", key)).strip()
    return normalized in set(rules.get("thanks_phrases", []))


def _parse_property_fields(message: str, config: AppConfig) -> dict[str, Any]:
    project_slug = infer_project_slug(config, message, default=None)
    project = config.project_by_slug.get(project_slug or "")
    area = _parse_area_from_message(message)
    fields: dict[str, Any] = {
        "purpose": _parse_purpose(message),
        "project": project.slug if project else None,
        "property_type": _parse_property_type(message),
        "area_m2": area,
        "bedrooms": parse_bedrooms(message),
        "bathrooms": _parse_bathrooms(message),
        "subdivision": _parse_subdivision(message),
        "tower": _parse_tower(message),
        "view": normalize_view(message),
        "furniture": normalize_furniture(message),
    }
    return {key: value for key, value in fields.items() if value is not None}


def _parse_purpose(message: str) -> str:
    key = text_key(message)
    if any(term in key for term in ("thue", "cho thue", "rent")):
        return "rent"
    return "sale"


def _parse_property_type(message: str) -> str:
    prop_type = infer_property_type(message, default="other")
    return "apartment" if prop_type == "other" else prop_type


def _parse_area_from_message(message: str) -> float | None:
    for match in re.finditer(r"(\d+(?:[,.]\d+)?)\s*(?:m2|m²|mét|met)\b", message, re.IGNORECASE):
        prefix = message[max(0, match.start() - 18) : match.start()].lower()
        if "triệu" in prefix or "trieu" in text_key(prefix):
            continue
        area = parse_area(match.group(1))
        if area:
            return area
    return None


def _parse_bathrooms(message: str) -> int | None:
    match = re.search(r"(\d+)\s*(?:wc|vs|ve sinh|vệ sinh)", message, re.IGNORECASE)
    return int(match.group(1)) if match else None


def _parse_subdivision(message: str) -> str | None:
    candidates = [
        "Sapphire",
        "Ruby",
        "Zenpark",
        "Pavilion",
        "Masteri",
        "Miami",
        "Sakura",
        "San Hô",
        "Sao Biển",
        "Ngọc Trai",
        "Vịnh Xanh",
        "Hải Âu",
        "Ánh Dương",
        "Thời Đại",
        "Phố Biển",
    ]
    key = text_key(message)
    for candidate in candidates:
        if text_key(candidate) in key:
            return candidate
    return None


def _parse_tower(message: str) -> str | None:
    match = re.search(r"\b([A-Z]{1,3}\d{1,3}(?:\.\d{1,3})?|S\d{1,3}|GS\d|R\d{1,2}|T\d{1,2})\b", message, re.IGNORECASE)
    return match.group(1).upper() if match else None


def _missing_for_valuation(fields: dict[str, Any]) -> list[str]:
    missing = _missing_project(fields)
    if not fields.get("area_m2"):
        missing.append("area_m2")
    return missing


def _missing_project(fields: dict[str, Any]) -> list[str]:
    return [] if fields.get("project") else ["project"]


def _missing_context(
    missing: list[str],
    fields: dict[str, Any],
    message: str,
    config: AppConfig,
    db_path: str | Path,
) -> dict[str, Any]:
    labels = {
        "project": "dự án/khu đô thị",
        "area_m2": "diện tích m2",
    }
    retrieval = missing_info_retrieval(message, fields, missing, config, db_path)
    return {
        "missing_fields": missing,
        "missing_labels": ", ".join(labels.get(item, item) for item in missing),
        "extracted": fields,
        "retrieval_suggestions": retrieval,
        "retrieval_hint_text": retrieval.get("hint_text") or "",
    }


def _snapshot_range_text(item: dict[str, Any]) -> str:
    if item.get("price_min_vnd") and item.get("price_max_vnd"):
        return f"{_format_vnd(item['price_min_vnd'])} - {_format_vnd(item['price_max_vnd'])}"
    if item.get("price_per_m2_min_vnd") and item.get("price_per_m2_max_vnd"):
        return f"{_format_vnd(item['price_per_m2_min_vnd'])}/m2 - {_format_vnd(item['price_per_m2_max_vnd'])}/m2"
    return "chưa có khoảng giá rõ"


def _format_valuation_answer(result: ValuationResponse, prop: PropertyInput) -> str:
    purpose_label = "giá thuê" if result.purpose == "rent" else "giá bán"
    monthly_suffix = "/tháng" if result.purpose == "rent" else ""
    lines = [
        f"Ước tính {purpose_label} hợp lý: {_format_market_money_range(result.p10_total_vnd, result.p90_total_vnd, result.purpose)}{monthly_suffix}.",
        f"Giá trung vị thị trường hiện tại: {_format_market_money(result.p50_total_vnd, result.purpose)}{monthly_suffix}.",
        f"Độ tin cậy: {_confidence_percent(result)}%.",
        "",
        "Phân tích:",
    ]
    lines.extend(f"- {line}" for line in _valuation_analysis_lines(result, prop))
    lines.extend(
        [
            "",
            "Các yếu tố có thể làm thay đổi giá:",
        ]
    )
    lines.extend(_valuation_adjustment_lines(result, prop))
    missing_optional = _missing_optional_detail_lines(prop)
    if missing_optional:
        lines.extend(["", "Để định giá chính xác hơn, vui lòng cung cấp:"])
        lines.extend(f"- {line}" for line in missing_optional)
    return "\n".join(lines)


def _valuation_answer_context(result: ValuationResponse, prop: PropertyInput, answer_example: str) -> dict[str, Any]:
    monthly_suffix = "/tháng" if result.purpose == "rent" else ""
    missing_optional = _missing_optional_detail_lines(prop)
    return {
        "purpose": result.purpose,
        "purpose_label": _purpose_label(result.purpose),
        "project": result.project,
        "property": prop.model_dump(),
        "property_type": result.property_type,
        "property_type_label": _property_type_label(result.property_type),
        "area_m2": prop.area_m2,
        "area_text": _format_area(prop.area_m2),
        "bedrooms": prop.bedrooms,
        "bedrooms_text": f" {prop.bedrooms}PN" if prop.bedrooms is not None else "",
        "p10_total_vnd": result.p10_total_vnd,
        "p50_total_vnd": result.p50_total_vnd,
        "p90_total_vnd": result.p90_total_vnd,
        "p10_total_text": f"{_format_market_money(result.p10_total_vnd, result.purpose)}{monthly_suffix}",
        "p50_total_text": f"{_format_market_money(result.p50_total_vnd, result.purpose)}{monthly_suffix}",
        "p90_total_text": f"{_format_market_money(result.p90_total_vnd, result.purpose)}{monthly_suffix}",
        "range_total_text": f"{_format_market_money_range(result.p10_total_vnd, result.p90_total_vnd, result.purpose)}{monthly_suffix}",
        "price_per_m2_text": _valuation_price_per_m2_text(result),
        "sample_size": result.sample_size,
        "confidence": result.confidence,
        "confidence_percent": _confidence_percent(result),
        "data_freshness": result.data_freshness,
        "estimate_basis": result.estimate_basis,
        "caveat": result.caveat,
        "top_factors": result.top_factors,
        "top_factor_text": _valuation_top_factor_text(result),
        "analysis_lines": _valuation_analysis_lines(result, prop),
        "adjustment_lines": _valuation_adjustment_lines(result, prop),
        "missing_optional_details": missing_optional,
        "missing_optional_text": ", ".join(missing_optional),
        "verified_comparable_count": _verified_comparable_count(result),
        "comparable_range_text": _comparable_range_text(result) or "",
        "reference_snapshot_count": len(result.reference_price_snapshots),
        "answer_example": answer_example,
        "example_answer": answer_example,
    }


def _valuation_analysis_lines(result: ValuationResponse, prop: PropertyInput) -> list[str]:
    area_text = _format_area(prop.area_m2)
    bedroom_text = f"{prop.bedrooms}PN " if prop.bedrooms is not None else ""
    lines = [
        f"Diện tích {area_text} thuộc nhóm {bedroom_text}{_property_type_label(result.property_type)} tại {result.project}.",
    ]
    proxy_note = _proxy_scope_note(result)
    if proxy_note:
        lines.append(proxy_note)
    comp_range = _comparable_range_text(result)
    if comp_range:
        lines.append(comp_range)
    verified_count = _verified_comparable_count(result)
    if verified_count:
        lines.append(f"Có {verified_count} giao dịch verified trong nhóm so sánh, được ưu tiên trọng số cao hơn listing thường.")
    else:
        lines.append("Dataset hiện chưa có giao dịch chốt verified phù hợp; kết quả đang dựa trên giá rao công khai đã lọc nhiễu.")
    if result.sample_size:
        lines.append(f"Mẫu tính toán gồm {result.sample_size} listing/giao dịch sau lọc nhiễu.")
    return lines


def _valuation_adjustment_lines(result: ValuationResponse, prop: PropertyInput) -> list[str]:
    if result.purpose == "rent":
        positive = [
            "+ Full nội thất: mức trung vị sẽ sát nhóm giá tốt hơn nếu căn đúng full nội thất; dữ liệu hiện tại chưa đủ căn trống/cơ bản để tách riêng premium.",
            "+ View hồ/công viên/nội khu: có thể kéo giá thuê lên nếu view thật sự thoáng; cần view/hướng cụ thể để lượng hóa.",
            "+ Tòa/phân khu tốt và tầng đẹp: có thể tăng giá khi gần tiện ích, sảnh/thang thuận tiện, tầng không quá thấp hoặc quá cao.",
        ]
        negative = [
            "- Nội thất cơ bản hoặc căn trống: thường thấp hơn nhóm full nội thất trong mẫu so sánh.",
            "- View bí/đối diện tòa khác, tầng bất tiện hoặc xa tiện ích: thường làm giá thuê giảm.",
        ]
    else:
        positive = [
            "+ Full nội thất/hoàn thiện đẹp: có thể hỗ trợ giá bán nếu người mua vào ở ngay.",
            "+ View hồ/công viên/nội khu và tầng đẹp: thường giúp thanh khoản và mức chào bán tốt hơn.",
            "+ Tòa/phân khu có tiện ích, pháp lý và vận hành tốt: có thể kéo giá lên so với mặt bằng chung.",
        ]
        negative = [
            "- Nội thất xuống cấp hoặc cần sửa chữa: thường làm người mua chiết khấu khi đàm phán.",
            "- View bí, tầng kém thuận tiện hoặc xa tiện ích: thường làm giá bán thấp hơn nhóm đẹp.",
        ]
    if prop.furniture == "full":
        positive[0] = "+ Full nội thất: đã được đưa vào so khớp khi dữ liệu listing có thông tin nội thất."
    elif prop.furniture in {"basic", "empty"}:
        negative[0] = "- Nội thất cơ bản/trống: đã được đưa vào so khớp; nên so với nhóm full nội thất cần chiết khấu thêm."
    if prop.view:
        positive[1] = f"+ View {prop.view}: đã được đưa vào so khớp khi listing có thông tin view tương ứng."
    return positive + negative


def _missing_optional_detail_lines(prop: PropertyInput) -> list[str]:
    missing = []
    if not prop.subdivision and not prop.tower:
        missing.append("Tòa/phân khu")
    if prop.floor_number is None:
        missing.append("Tầng")
    if not prop.furniture:
        missing.append("Tình trạng nội thất")
    if not prop.view:
        missing.append("Hướng ban công/view")
    return missing


def _proxy_scope_note(result: ValuationResponse) -> str | None:
    comps = result.comparable_listings
    if not comps:
        return None
    same_project = sum(1 for item in comps if item.project == result.project)
    if same_project >= max(1, len(comps) // 2):
        return None
    return (
        f"Mẫu cùng dự án hiện chưa đủ mạnh; hệ thống đang dùng thêm nhóm {_property_type_label(result.property_type)} "
        "tương tự trong rổ Vinhomes Hà Nội làm proxy."
    )


def _comparable_range_text(result: ValuationResponse) -> str | None:
    values = []
    for item in result.comparable_listings:
        value = item.rent_monthly_vnd if result.purpose == "rent" else item.price_total_vnd
        if value:
            values.append(float(value))
    if not values:
        return None
    verb = "chào thuê" if result.purpose == "rent" else "chào bán"
    suffix = "/tháng" if result.purpose == "rent" else ""
    return (
        f"Các căn tương tự trong top mẫu so sánh đang được {verb} từ "
        f"{_format_market_money_range(min(values), max(values), result.purpose)}{suffix}."
    )


def _verified_comparable_count(result: ValuationResponse) -> int:
    # ComparableListing intentionally hides storage internals; verified rows currently have no public source_url.
    return sum(1 for item in result.comparable_listings if not item.source_url)


def _confidence_percent(result: ValuationResponse) -> int:
    score = {"low": 52, "medium": 68, "high": 78}.get(result.confidence, 60)
    if result.sample_size >= 100:
        score += 6
    elif result.sample_size >= 50:
        score += 4
    elif result.sample_size < 15:
        score -= 5
    if result.p50_total_vnd:
        spread_ratio = (result.p90_total_vnd - result.p10_total_vnd) / max(result.p50_total_vnd, 1)
        if spread_ratio < 0.25:
            score += 4
        elif spread_ratio > 0.8:
            score -= 4
    return max(40, min(88, int(round(score))))


def _format_area(value: float | int | None) -> str:
    if value is None:
        return ""
    number = float(value)
    return f"{number:.0f}m²" if number.is_integer() else f"{number:.1f}m²"


def _format_market_money(value: float | int | None, purpose: str) -> str:
    if value is None:
        return "N/A"
    value = float(value)
    if purpose == "rent":
        return f"{_trim_decimal(value / 1_000_000)} triệu"
    if value >= 1_000_000_000:
        return f"{_trim_decimal(value / 1_000_000_000, digits=2)} tỷ"
    if value >= 1_000_000:
        return f"{_trim_decimal(value / 1_000_000)} triệu"
    return f"{value:,.0f} VND"


def _format_market_money_range(low: float | int | None, high: float | int | None, purpose: str) -> str:
    if low is None or high is None:
        return f"{_format_market_money(low, purpose)} - {_format_market_money(high, purpose)}"
    low_value = float(low)
    high_value = float(high)
    if purpose == "rent":
        return f"{_trim_decimal(low_value / 1_000_000)} - {_trim_decimal(high_value / 1_000_000)} triệu"
    if low_value >= 1_000_000_000 and high_value >= 1_000_000_000:
        return f"{_trim_decimal(low_value / 1_000_000_000, digits=2)} - {_trim_decimal(high_value / 1_000_000_000, digits=2)} tỷ"
    if low_value >= 1_000_000 and high_value >= 1_000_000:
        return f"{_trim_decimal(low_value / 1_000_000)} - {_trim_decimal(high_value / 1_000_000)} triệu"
    return f"{low_value:,.0f} - {high_value:,.0f} VND"


def _valuation_price_per_m2_text(result: ValuationResponse) -> str:
    if not result.p50_price_per_m2_vnd:
        return ""
    suffix = "/tháng" if result.purpose == "rent" else ""
    return f"Giá trung vị theo m2 khoảng {_format_market_money(result.p50_price_per_m2_vnd, result.purpose)}/m2{suffix}."


def _valuation_top_factor_text(result: ValuationResponse) -> str:
    factors = [factor for factor in result.top_factors if factor]
    if not factors:
        return ""
    return "Yếu tố ảnh hưởng chính: " + "; ".join(factors[:3]) + "."


def _trim_decimal(value: float, digits: int = 1) -> str:
    text = f"{value:.{digits}f}"
    return text.rstrip("0").rstrip(".")


def _format_vnd(value: float | int | None) -> str:
    if value is None:
        return "N/A"
    value = float(value)
    if value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.2f} tỷ VND"
    if value >= 1_000_000:
        return f"{value / 1_000_000:.1f} triệu VND"
    return f"{value:,.0f} VND"


def _price_per_m2_text(value: float | int | None) -> str:
    return f"Đơn giá P50 khoảng {_format_vnd(value)}/m2. " if value else ""


def _top_factor_text(factors: list[str]) -> str:
    return f"Yếu tố chính: {factors[0]}" if factors else ""


def _snapshot_count_text(count: int) -> str:
    return f"Có thêm {count} snapshot bảng giá để đối chiếu." if count else ""


def _purpose_label(value: str | None) -> str:
    return {"sale": "bán", "rent": "thuê"}.get(value or "", value or "")


def _property_type_label(value: str | None) -> str:
    return {
        "apartment": "căn hộ",
        "villa": "biệt thự",
        "townhouse": "liền kề",
        "shophouse": "shophouse",
        "house": "nhà phố",
        "other": "BĐS",
        "all": "tất cả loại hình",
    }.get(value or "", value or "")
