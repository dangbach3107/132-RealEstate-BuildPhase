from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import os

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.chatbot import handle_chat
from app.config import load_config
from app.crawler import crawl_once
from app.database import DEFAULT_DB_PATH
from app.env import load_app_env
from app.normalization import infer_project_slug
from app.schemas import (
    ChatRequest,
    ChatResponse,
    CrawlResponse,
    MarketTrendResponse,
    PriceSnapshotReference,
    PropertyInput,
    ValuationResponse,
    VerifiedTransactionInput,
)
from app.storage import get_store, init_storage
from app.valuation import estimate_property, market_trends, price_snapshot_references


load_app_env()
CONFIG_PATH = Path(os.getenv("VALUATION_CONFIG_PATH", "config/projects.yaml"))
DB_PATH = Path(os.getenv("VALUATION_DB_PATH", str(DEFAULT_DB_PATH)))
DEFAULT_CORS_ORIGINS = "http://localhost:5173,http://127.0.0.1:5173,https://solanai.us,https://www.solanai.us"
CORS_ORIGINS = [
    origin.strip()
    for origin in os.getenv("VALUATION_CORS_ORIGINS", DEFAULT_CORS_ORIGINS).split(",")
    if origin.strip()
]

app = FastAPI(title="Vinhomes Hanoi Valuation API", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup() -> None:
    init_storage(DB_PATH)


def config():
    return load_config(CONFIG_PATH)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/projects")
def projects() -> list[dict[str, str | list[str] | None]]:
    cfg = config()
    return [
        {
            "slug": project.slug,
            "name": project.name,
            "aliases": list(project.aliases),
            "district_hint": project.district_hint,
        }
        for project in cfg.projects
    ]


@app.post("/ingest/crawl", response_model=CrawlResponse)
def ingest_crawl(limit: int | None = None, source: str | None = None):
    try:
        return crawl_once(config(), DB_PATH, limit=limit, source_filter=source)
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/valuation", response_model=ValuationResponse)
def valuation(payload: PropertyInput):
    try:
        return estimate_property(payload, config(), DB_PATH)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.get("/market-trends", response_model=MarketTrendResponse)
def trends(project: str, purpose: str = "sale", property_type: str | None = None, bedrooms: int | None = None):
    try:
        return market_trends(config(), project, purpose, property_type, bedrooms, DB_PATH)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.get("/price-snapshots", response_model=list[PriceSnapshotReference])
def price_snapshots(project: str, purpose: str = "sale", property_type: str | None = None, limit: int = 12):
    try:
        return price_snapshot_references(config(), project, purpose, property_type, limit=limit, db_path=DB_PATH)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=500, detail=str(exc)) from exc


@app.post("/verified-transactions")
def verified_transaction(payload: VerifiedTransactionInput) -> dict[str, int | str]:
    cfg = config()
    project_slug = infer_project_slug(cfg, payload.project, default=payload.project)
    project = cfg.project_by_slug.get(project_slug or "")
    if not project:
        raise HTTPException(status_code=422, detail="Không nhận diện được project trong config.")
    if payload.purpose == "sale" and not payload.transaction_price_vnd:
        raise HTTPException(status_code=422, detail="Giao dịch bán cần transaction_price_vnd.")
    if payload.purpose == "rent" and not payload.rent_monthly_vnd:
        raise HTTPException(status_code=422, detail="Giao dịch thuê cần rent_monthly_vnd.")

    record = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "project_slug": project.slug,
        "project_name": project.name,
        "property_type": payload.property_type,
        "purpose": payload.purpose,
        "transaction_price_vnd": payload.transaction_price_vnd,
        "rent_monthly_vnd": payload.rent_monthly_vnd,
        "area_m2": payload.area_m2,
        "bedrooms": payload.bedrooms,
        "subdivision": payload.subdivision,
        "transaction_date": payload.transaction_date,
        "confidence_score": payload.confidence_score,
        "evidence_note": payload.evidence_note,
        "source": payload.source,
    }
    inserted_id = get_store(DB_PATH).insert_verified_transaction(record)
    return {"status": "created", "id": inserted_id}


@app.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest):
    return handle_chat(payload, config(), DB_PATH)
