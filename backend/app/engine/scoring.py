from dataclasses import dataclass


@dataclass(slots=True)
class SignalState:
    xau_dir: int
    dxy_dir: int
    us10y_dir: int
    silver_dir: int
    copper_dir: int
    platinum_dir: int
    bcom_dir: int
    fed_dir: int


def compute_gold_score(state: SignalState) -> tuple[int, dict[str, int]]:
    drivers = {
        'dxy_inverse': 20 if state.xau_dir * state.dxy_dir == -1 else 0,
        'us10y_inverse': 20 if state.xau_dir * state.us10y_dir == -1 else 0,
        'silver_direct': 15 if state.xau_dir * state.silver_dir == 1 else 0,
        'copper_direct': 10 if state.xau_dir * state.copper_dir == 1 else 0,
        'platinum_direct': 10 if state.xau_dir * state.platinum_dir == 1 else 0,
        'commodities_direct': 10 if state.xau_dir * state.bcom_dir == 1 else 0,
        'fed_expectation': 15 if state.xau_dir * state.fed_dir == -1 else 0,
    }
    score = sum(drivers.values())
    return score, drivers


def confidence_from_score(score: int) -> str:
    if score >= 85:
        return 'Muito Alto'
    if score >= 70:
        return 'Alto'
    if score >= 50:
        return 'Médio'
    return 'Baixo'
