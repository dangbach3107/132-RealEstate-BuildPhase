from __future__ import annotations

import json
import os
import random
import re
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from app.env import PROJECT_ROOT, load_app_env


TRUE_VALUES = {"1", "true", "yes", "on"}
DEFAULT_PROMPT_DIR = PROJECT_ROOT / "prompts"
RESPONSE_STYLE_HINTS = (
    {
        "name": "direct",
        "instruction": "Lead with the main number or conclusion, then add 1-2 short supporting points.",
    },
    {
        "name": "consultative",
        "instruction": "Sound like a human advisor: softer, conversational, with one brief judgment before the next step.",
    },
    {
        "name": "compact",
        "instruction": "Use short sentences, minimal lead-in, and avoid repeating stock openings such as 'Minh thay' or 'Voi can nay'.",
    },
    {
        "name": "analytical",
        "instruction": "Emphasize reasons behind the number: comparable sample, confidence, and main price drivers.",
    },
    {
        "name": "next_step",
        "instruction": "After the main answer, suggest one useful next detail if context is incomplete, without asking too much.",
    },
)


def llm_enabled() -> bool:
    load_app_env()
    flag = os.getenv("VALUATION_LLM_ENABLED")
    if flag is not None:
        return flag.strip().lower() in TRUE_VALUES
    return bool(os.getenv("OPENAI_API_KEY") and os.getenv("MODEL"))


def generate_answer(intent: str, message: str, context: dict[str, Any], fallback_key: str | None = None) -> str:
    fallback = _format_answer_lines(_fallback_answer(fallback_key or intent, context))
    if not llm_enabled():
        return fallback
    api_key = os.getenv("OPENAI_API_KEY")
    model = os.getenv("MODEL")
    if not api_key or not model:
        return fallback

    try:
        from openai import OpenAI
    except ImportError:
        return fallback

    try:
        client = OpenAI(api_key=api_key, timeout=_float_env("OPENAI_TIMEOUT_SECONDS", 8.0))
        system_prompt = _load_prompt("VALUATION_SYSTEM_PROMPT_PATH", "chatbot_system.md")
        prompt_context = _context_with_response_style(context)
        user_prompt = _load_prompt("VALUATION_USER_PROMPT_PATH", "chatbot_user.md").format(
            intent=intent,
            message=message,
            context_json=json.dumps(prompt_context, ensure_ascii=False, default=str, indent=2),
        )
        messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ]
        response = client.chat.completions.create(**_chat_completion_kwargs(model, messages))
    except Exception:  # noqa: BLE001
        return fallback

    text = response.choices[0].message.content if response.choices else None
    return _format_answer_lines(text) if text and text.strip() else fallback


def _context_with_response_style(context: dict[str, Any]) -> dict[str, Any]:
    if "response_style" in context:
        return dict(context)
    return {**context, "response_style": random.choice(RESPONSE_STYLE_HINTS)}


def _prompt_dir() -> Path:
    value = os.getenv("VALUATION_PROMPT_DIR")
    return Path(value) if value else DEFAULT_PROMPT_DIR


def _load_prompt(env_name: str, default_name: str) -> str:
    load_app_env()
    path = Path(os.getenv(env_name) or _prompt_dir() / default_name)
    return _read_text(str(path))


@lru_cache(maxsize=16)
def _read_text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def _fallback_answer(key: str, context: dict[str, Any]) -> str:
    template = _fallback_templates().get(key) or _fallback_templates().get("default") or ""
    safe_context = {name: _stringify(value) for name, value in context.items()}
    try:
        return template.format(**safe_context)
    except KeyError:
        return template


def _format_answer_lines(text: str | None) -> str:
    if not text:
        return ""
    normalized = str(text).replace("\r\n", "\n").replace("\r", "\n").strip()
    if not normalized:
        return ""
    if "\n" in normalized:
        lines = [re.sub(r"[ \t]+", " ", line).strip() for line in normalized.split("\n")]
        return _bulletize_lines(line for line in lines if line)

    decimal_safe = re.sub(r"(?<=\d)\.(?=\d)", "<decimal-dot>", re.sub(r"\s+", " ", normalized))
    parts = re.split(r"(?<=[.!?])\s+", decimal_safe)
    lines = [part.replace("<decimal-dot>", ".").strip() for part in parts if part.strip()]
    return _bulletize_lines(lines) if lines else normalized


def _bulletize_lines(lines: Any) -> str:
    formatted = []
    for line in lines:
        clean = str(line).strip()
        if not clean:
            continue
        clean = re.sub(r"^[-*•]\s+", "", clean)
        formatted.append(f"- {clean}")
    return "\n".join(formatted)


@lru_cache(maxsize=1)
def _fallback_templates() -> dict[str, str]:
    load_app_env()
    path = Path(os.getenv("VALUATION_FALLBACK_PROMPT_PATH") or _prompt_dir() / "fallback_answers.yaml")
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {str(key): str(value) for key, value in data.items()}


def _stringify(value: Any) -> str:
    if isinstance(value, list):
        return ", ".join(_stringify(item) for item in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, default=str)
    if value is None:
        return ""
    return str(value)


def _chat_completion_kwargs(model: str, messages: list[dict[str, str]]) -> dict[str, Any]:
    kwargs: dict[str, Any] = {
        "model": model,
        "messages": messages,
    }
    if _uses_max_completion_tokens(model):
        kwargs["max_completion_tokens"] = _int_env("OPENAI_MAX_TOKENS", 220)
    else:
        kwargs["max_tokens"] = _int_env("OPENAI_MAX_TOKENS", 220)
        kwargs["temperature"] = _float_env("OPENAI_TEMPERATURE", 0.55)
    return kwargs


def _uses_max_completion_tokens(model: str) -> bool:
    normalized = model.lower()
    return normalized.startswith(("gpt-5", "o1", "o3", "o4")) or "gpt-5" in normalized


def _float_env(name: str, default: float) -> float:
    value = os.getenv(name)
    if value is None:
        return default
    try:
        return float(value)
    except ValueError:
        return default


def _int_env(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None:
        return default
    try:
        return int(value)
    except ValueError:
        return default
