from fastapi import APIRouter

from app.core.config import settings
from app.services.data_provider import MarketDataProvider
from app.services.signal_engine import SignalEngine

router = APIRouter()
provider = MarketDataProvider()
engine = SignalEngine()


@router.get('/health')
def health() -> dict[str, str]:
    return {'status': 'ok'}


@router.get('/snapshots')
async def snapshots() -> list[dict]:
    data = [await provider.get_snapshot(symbol) for symbol in settings.symbols]
    return [item.model_dump() for item in data]


@router.get('/macro-score')
def macro_score() -> dict:
    score = engine.evaluate_macro()
    return score.model_dump()


@router.get('/alerts/latest')
def latest_alert() -> dict:
    macro = engine.evaluate_macro()
    alert = engine.evaluate_alert(macro)
    return alert.model_dump()
