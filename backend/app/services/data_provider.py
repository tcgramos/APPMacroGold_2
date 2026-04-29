from datetime import UTC, datetime
import random

from app.schemas.market import TickerSnapshot


class MarketDataProvider:
    """Adapter placeholder for tvDatafeed / tradingview-ta integration."""

    async def get_snapshot(self, symbol: str) -> TickerSnapshot:
        base = {
            'XAUUSD': 2350,
            'DXY': 104,
            'US10Y': 4.2,
            'BCOM': 102,
            'XAGUSD': 29,
            'COPPER': 4.7,
            'XPTUSD': 1010,
            'FEDFUNDS': 5.25,
        }.get(symbol, 100)

        change = random.uniform(-1.2, 1.2)
        price = base + change
        return TickerSnapshot(
            symbol=symbol,
            price=round(price, 4),
            change_daily=round(change, 4),
            change_pct_daily=round((change / base) * 100, 4),
            timestamp=datetime.now(UTC),
        )
