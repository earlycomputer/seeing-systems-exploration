"""The spend cap for experiment 1c counts experiments 1 and 1b too, so all three stay under $100 together."""

from config import SPEND_CAP_USD, SPEND_LEDGER as EXP1_LEDGER
from loop.models import BudgetExceeded, spent_usd
from outcome.settings import SPEND_LEDGER as EXP1B_LEDGER
from worlds.settings import SPEND_LEDGER


def spent() -> dict:
    return {"exp1": spent_usd(EXP1_LEDGER), "exp1b": spent_usd(EXP1B_LEDGER), "exp1c": spent_usd(SPEND_LEDGER)}


def check() -> None:
    s = spent()
    total = sum(s.values())
    if total >= SPEND_CAP_USD:
        raise BudgetExceeded(f"spent ${total:.2f} across experiments 1, 1b and 1c of the ${SPEND_CAP_USD:.0f} cap; "
                             "raising it needs a human first")
