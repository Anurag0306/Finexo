from datetime import datetime, timezone
from typing import List

from fastapi import FastAPI
from pydantic import BaseModel


class MarketPrice(BaseModel):
    symbol: str
    price: float
    change_pct: float


class Indicator(BaseModel):
    name: str
    value: float
    unit: str
    updated_at: str


app = FastAPI(title="MacroMind API", version="0.1.0")


@app.get("/health")
def health() -> dict:
    return {
        "status": "ok",
        "service": "macromind-api",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/api/prices", response_model=List[MarketPrice])
def get_prices() -> List[MarketPrice]:
    # Mock values for local testing/demo.
    return [
        MarketPrice(symbol="NIFTY50", price=22480.35, change_pct=0.64),
        MarketPrice(symbol="SPX", price=5792.88, change_pct=-0.12),
        MarketPrice(symbol="BTCUSD", price=68120.50, change_pct=1.42),
        MarketPrice(symbol="USDINR", price=83.12, change_pct=0.08),
    ]


@app.get("/api/indicators", response_model=List[Indicator])
def get_indicators() -> List[Indicator]:
    now = datetime.now(timezone.utc).isoformat()
    return [
        Indicator(name="US CPI YoY", value=3.2, unit="%", updated_at=now),
        Indicator(name="US GDP QoQ", value=2.4, unit="%", updated_at=now),
        Indicator(name="India Repo Rate", value=6.5, unit="%", updated_at=now),
    ]
