"""Spend for experiments 1e (the run in words), 1f (the language run) and 1g (1f with expectations checked).

Jono chose both on 2026-10-06 ("Both" on the decision card: "about $20 to $26 of the $34.35"). Together they stop at
JOINT_CEILING_USD, and every experiment together stays under the program's cap (config.py). Going past either needs Jono.
"""

from config import ROOT, SPEND_CAP_USD
from loop.models import BudgetExceeded, spent_usd
from harder import budget as budget_1d

JOINT_CEILING_USD = 26.0
LEDGERS = {"exp1e": ROOT / "history" / "results" / "spend.jsonl", "exp1f": ROOT / "langrun" / "results" / "spend.jsonl",
           "exp1g": ROOT / "langrun" / "results_1g" / "spend.jsonl"}
# 1g, the rerun with expectations checked: Jono chose "Rerun" on 2026-10-06, "about $15, bringing the total to about
# $100". It stops here.
# Then Jono: "No need to stop at $18. Be thorough" (2026-10-06 21:59), so 1g grew to four seeds and a control
# (estimated about $55 in all) and stops at $70.
CEILING_1G_USD = 70.0


def spent() -> dict:
    return budget_1d.spent() | {k: spent_usd(p) for k, p in LEDGERS.items()}


def check() -> None:
    s = spent()
    total = sum(s.values())
    if total >= SPEND_CAP_USD:
        raise BudgetExceeded(f"spent ${total:.2f} across experiments 1 to 1f of the ${SPEND_CAP_USD:.0f} cap; "
                             "raising it needs a human first")
    if s["exp1g"] >= CEILING_1G_USD:
        raise BudgetExceeded(f"1g has spent ${s['exp1g']:.2f}, past the ${CEILING_1G_USD:.0f} ceiling; going on needs Jono")
    joint = s["exp1e"] + s["exp1f"]
    if joint >= JOINT_CEILING_USD:
        raise BudgetExceeded(f"1e and 1f have spent ${joint:.2f}, the ${JOINT_CEILING_USD:.0f} Jono approved; going on needs Jono")
