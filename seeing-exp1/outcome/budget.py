"""The spend cap for experiment 1b counts experiment 1's ledger too, so the two stay under $100 together."""

from config import SPEND_CAP_USD, SPEND_LEDGER as EXP1_LEDGER
from loop.models import BudgetExceeded, spent_usd
from outcome.settings import SPEND_LEDGER


def spent() -> dict:
    return {"exp1": spent_usd(EXP1_LEDGER), "exp1b": spent_usd(SPEND_LEDGER)}


def check() -> None:
    s = spent()
    total = s["exp1"] + s["exp1b"]
    if total >= SPEND_CAP_USD:
        raise BudgetExceeded(f"spent ${total:.2f} (experiment 1 ${s['exp1']:.2f}, 1b ${s['exp1b']:.2f}) of the "
                             f"${SPEND_CAP_USD:.0f} cap; raising it needs a human first")
