"""Spend for 1j: its own ceiling, and every experiment together under the program cap (config.py)."""

from config import SPEND_CAP_USD
from hundred import budget as budget_1h
from ladder.settings import CEILING_1J_USD, CEILING_1K_USD
from loop.models import BudgetExceeded


def spent() -> dict:
    return budget_1h.spent()  # includes exp1j


def check() -> None:
    s = spent()
    total = sum(s.values())
    if total >= SPEND_CAP_USD:
        raise BudgetExceeded(f"spent ${total:.2f} across all experiments, the ${SPEND_CAP_USD:.0f} program cap; "
                             "raising it needs Jono")
    if s["exp1j"] >= CEILING_1J_USD:
        raise BudgetExceeded(f"1j has spent ${s['exp1j']:.2f}, its ${CEILING_1J_USD:.0f} ceiling; going on needs Jono")


def check_1k() -> None:
    s = spent()
    total = sum(s.values())
    if total >= SPEND_CAP_USD:
        raise BudgetExceeded(f"spent ${total:.2f} across all experiments, the ${SPEND_CAP_USD:.0f} program cap; "
                             "raising it needs Jono")
    if s["exp1k"] >= CEILING_1K_USD:
        raise BudgetExceeded(f"1k has spent ${s['exp1k']:.2f}, its ${CEILING_1K_USD:.0f} ceiling; going on needs Jono")
