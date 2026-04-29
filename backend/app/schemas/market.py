from datetime import datetime
from pydantic import BaseModel


class TickerSnapshot(BaseModel):
    symbol: str
    price: float
    change_daily: float
    change_pct_daily: float
    timestamp: datetime


class GoldMacroScore(BaseModel):
    direction: str
    score: int
    confidence: str
    drivers: dict[str, int]


class AlertMessage(BaseModel):
    kind: str
    title: str
    description: str
    confidence: str
    score: int
    created_at: datetime
