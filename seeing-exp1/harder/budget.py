"""The spend cap for experiment 1d counts experiments 1, 1b and 1c too, so all four stay under $100 together.

1d also has its own ceiling: Jono approved up to $25 (journal, 2026-10-04). The matrix stops at it.
"""

from config import SPEND_CAP_USD, SPEND_LEDGER as EXP1_LEDGER
from loop.models import BudgetExceeded, spent_usd
from outcome.settings import SPEND_LEDGER as EXP1B_LEDGER
from worlds.settings import SPEND_LEDGER as EXP1C_LEDGER
from harder.settings import SPEND_LEDGER

EXP1D_CEILING_USD = 25.0


def spent() -> dict:
    return {"exp1": spent_usd(EXP1_LEDGER), "exp1b": spent_usd(EXP1B_LEDGER), "exp1c": spent_usd(EXP1C_LEDGER),
            "exp1d": spent_usd(SPEND_LEDGER)}


def check() -> None:
    s = spent()
    total = sum(s.values())
    if total >= SPEND_CAP_USD:
        raise BudgetExceeded(f"spent ${total:.2f} across experiments 1 to 1d of the ${SPEND_CAP_USD:.0f} cap; "
                             "raising it needs a human first")
    if s["exp1d"] >= EXP1D_CEILING_USD:
        raise BudgetExceeded(f"1d has spent ${s['exp1d']:.2f}, its approved ${EXP1D_CEILING_USD:.0f}; going on needs Jono")
