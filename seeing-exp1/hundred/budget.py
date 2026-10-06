"""Spend for 1h: its own ceiling, and every experiment together under the program cap (config.py)."""

from config import SPEND_CAP_USD
from history import budget as budget_1e_1g
from loop.models import BudgetExceeded, spent_usd
from hundred.settings import CEILING_1H_USD, SPEND_LEDGER

# Jono chose "Pilot first" on 2026-10-06 22:19: 5 briefs, 60 worlds, "about $20". The pilot stops here.
PILOT_CEILING_USD = 25.0


def spent() -> dict:
    return budget_1e_1g.spent() | {"exp1h": spent_usd(SPEND_LEDGER)}


def check(pilot: bool = True) -> None:
    s = spent()
    total = sum(s.values())
    if total >= SPEND_CAP_USD:
        raise BudgetExceeded(f"spent ${total:.2f} across all experiments, the ${SPEND_CAP_USD:.0f} program cap; "
                             "raising it needs Jono")
    ceiling = PILOT_CEILING_USD if pilot else CEILING_1H_USD
    if s["exp1h"] >= ceiling:
        raise BudgetExceeded(f"1h has spent ${s['exp1h']:.2f}, its ${ceiling:.0f} ceiling; going on needs Jono")
