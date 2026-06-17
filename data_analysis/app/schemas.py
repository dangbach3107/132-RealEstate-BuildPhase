from __future__ import annotations

from typing import Any, Literal

from pydantic import BaseModel, Field


Purpose = Literal["sale", "rent"]
PropertyType = Literal["apartment", "villa", "townhouse", "shophouse", "house", "other"]


class PropertyInput(BaseModel):
    purpose: Purpose = "sale"
    project: str
    property_type: PropertyType = "apartment"
    area_m2: float = Field(..., gt=0)
    bedrooms: int | None = Field(default=None, ge=0)
    bathrooms: int | None = Field(default=None, ge=0)
    floor_number: int | None = None
    subdivision: str | None = None
    tower: str | None = None
    view: str | None = None
    furniture: str | None = None
    legal_status: str | None = None


class ComparableListing(BaseModel):
    title: str | None = None
    project: str
    property_type: str
    purpose: str
    price_total_vnd: float | None = None
    price_per_m2_vnd: float | None = None
    rent_monthly_vnd: float | None = None
    area_m2: float | None = None
    bedrooms: int | None = None
    subdivision: str | None = None
    view: str | None = None
    furniture: str | None = None
    observed_at: str | None = None
    source_url: str | None = None
    similarity_score: float


class PriceSnapshotReference(BaseModel):
    source: str
    source_url: str | None = None
    observed_at: str | None = None
    project: str
    property_type: str
    purpose: Purpose
    label: str | None = None
    subdivision: str | None = None
    area_min_m2: float | None = None
    area_max_m2: float | None = None
    price_min_vnd: float | None = None
    price_max_vnd: float | None = None
    price_per_m2_min_vnd: float | None = None
    price_per_m2_max_vnd: float | None = None
    basis: str


class ValuationResponse(BaseModel):
    purpose: Purpose
    project: str
    property_type: str
    currency: str = "VND"
    estimate_basis: str
    p10_total_vnd: float
    p50_total_vnd: float
    p90_total_vnd: float
    p10_price_per_m2_vnd: float | None = None
    p50_price_per_m2_vnd: float | None = None
    p90_price_per_m2_vnd: float | None = None
    sample_size: int
    confidence: Literal["low", "medium", "high"]
    data_freshness: str | None
    comparable_listings: list[ComparableListing]
    reference_price_snapshots: list[PriceSnapshotReference] = []
    top_factors: list[str]
    caveat: str


class MarketTrendResponse(BaseModel):
    project: str
    property_type: str | None
    purpose: Purpose
    bedrooms: int | None
    windows: dict[str, dict[str, float | int | None]]
    reference_price_snapshots: list[PriceSnapshotReference] = []
    caveat: str


class VerifiedTransactionInput(BaseModel):
    project: str
    property_type: PropertyType = "apartment"
    purpose: Purpose = "sale"
    transaction_price_vnd: float | None = Field(default=None, gt=0)
    rent_monthly_vnd: float | None = Field(default=None, gt=0)
    area_m2: float = Field(..., gt=0)
    bedrooms: int | None = Field(default=None, ge=0)
    subdivision: str | None = None
    transaction_date: str | None = Field(default=None, description="YYYY-MM-DD")
    confidence_score: float = Field(default=0.8, ge=0, le=1)
    evidence_note: str | None = None
    source: str = "manual"


class ChatRequest(BaseModel):
    message: str
    property: PropertyInput | None = None


class ChatResponse(BaseModel):
    answer: str
    missing_fields: list[str] = []
    valuation: dict[str, Any] | None = None
    data: dict[str, Any] | None = None
    intent: str | None = None
    extracted: dict[str, Any] | None = None


class CrawlResponse(BaseModel):
    fetched_at: str
    pages: list[dict[str, Any]]
    records_parsed: int
    price_snapshots_parsed: int = 0
    property_candidates_parsed: int = 0
    output_csv: str
    output_price_snapshots_csv: str | None = None
    output_property_candidates_csv: str | None = None
    db_path: str
    source_filter: str | None = None
