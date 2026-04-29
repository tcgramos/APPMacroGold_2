from datetime import UTC, datetime
import random

from app.engine.scoring import SignalState, compute_gold_score, confidence_from_score
from app.schemas.market import AlertMessage, GoldMacroScore


class SignalEngine:
    def evaluate_macro(self) -> GoldMacroScore:
        state = SignalState(
            xau_dir=random.choice([-1, 1]),
            dxy_dir=random.choice([-1, 1]),
            us10y_dir=random.choice([-1, 1]),
            silver_dir=random.choice([-1, 1]),
            copper_dir=random.choice([-1, 1]),
            platinum_dir=random.choice([-1, 1]),
            bcom_dir=random.choice([-1, 1]),
            fed_dir=random.choice([-1, 1]),
        )
        score, drivers = compute_gold_score(state)
        direction = 'BULLISH' if state.xau_dir > 0 else 'BEARISH'
        return GoldMacroScore(
            direction=direction,
            score=score,
            confidence=confidence_from_score(score),
            drivers=drivers,
        )

    def evaluate_alert(self, macro: GoldMacroScore) -> AlertMessage:
        if macro.score >= 70:
            title = 'FORÇA CONFIRMADA NO OURO'
            kind = 'trend_confirmation'
            description = f'Movimento alinhado ao cenário macro ({macro.direction}).'
        else:
            title = 'POSSÍVEL EXAUSTÃO / REVERSÃO NO OURO'
            kind = 'reversal_risk'
            description = 'Divergências macro detectadas entre ouro e ativos correlatos.'

        return AlertMessage(
            kind=kind,
            title=title,
            description=description,
            confidence=macro.confidence,
            score=macro.score,
            created_at=datetime.now(UTC),
        )
