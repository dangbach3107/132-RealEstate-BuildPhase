from __future__ import annotations

import os
from pathlib import Path
import sys

import uvicorn

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from app.env import load_app_env  # noqa: E402


def _int_env(name: str, default: int) -> int:
    try:
        return int(os.getenv(name, str(default)))
    except ValueError:
        return default

if __name__ == "__main__":
    load_app_env()
    uvicorn.run(
        "app.main:app",
        host=os.getenv("VALUATION_HOST", "127.0.0.1"),
        port=_int_env("VALUATION_PORT", 8000),
        reload=True,
        app_dir=str(ROOT),
    )
