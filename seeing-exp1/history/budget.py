"""Spend for experiments 1e (the run in words) and 1f (the language run).

Jono chose both on 2026-10-06 ("Both" on the decision card: "about $20 to $26 of the $34.35"). Together they stop at
JOINT_CEILING_USD, and every experiment together stays under the program's $100 cap. Going past either needs Jono.
"""

from config import ROOT, SPEND_CAP_USD
from loop.models import BudgetExceeded, spent_usd
from harder import budget as budget_1d

JOINT_CEILING_USD = 26.0
LEDGERS = {"exp1e": ROOT / "history" / "results" / "spend.jsonl", "exp1f": ROOT / "langrun" / "results" / "spend.jsonl"}


def spent() -> dict:
    return budget_1d.spent() | {k: spent_usd(p) for k, p in LEDGERS.items()}


def check() -> None:
    s = spent()
    total = sum(s.values())
    if total >= SPEND_CAP_USD:
        raise BudgetExceeded(f"spent ${total:.2f} across experiments 1 to 1f of the ${SPEND_CAP_USD:.0f} cap; "
                             "raising it needs a human first")
    joint = s["exp1e"] + s["exp1f"]
    if joint >= JOINT_CEILING_USD:
        raise BudgetExceeded(f"1e and 1f have spent ${joint:.2f}, the ${JOINT_CEILING_USD:.0f} Jono approved; going on needs Jono")
