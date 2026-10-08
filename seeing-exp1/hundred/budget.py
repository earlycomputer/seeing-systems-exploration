"""Spend for 1h: its own ceiling, and every experiment together under the program cap (config.py)."""

from config import SPEND_CAP_USD
from history import budget as budget_1e_1g
from loop.models import BudgetExceeded, spent_usd
from hundred.settings import CEILING_1H_USD, JUDGE_CEILING_USD, JUDGE_LEDGER, SPEND_LEDGER
from ladder.settings import SPEND_LEDGER as LEDGER_1J, SPEND_LEDGER_1K as LEDGER_1K

# Jono chose "Pilot first" on 2026-10-06 22:19: 5 briefs, 60 worlds, "about $20". Opus cost about $0.85 a world, so the
# run stopped at the program cap after 25 worlds; Jono then chose "Finish it" (2026-10-07 00:04), about $40 in all.
# Opus's reads cost $0.15 each, so finishing every read takes the pilot to about $46; the quiz runs on GPT-6.1 only to
# stay near the "about $40" Jono approved.
PILOT_CEILING_USD = 47.0


def spent() -> dict:
    return budget_1e_1g.spent() | {"exp1h": spent_usd(SPEND_LEDGER), "exp1h_judge": spent_usd(JUDGE_LEDGER),
                                    "exp1j": spent_usd(LEDGER_1J), "exp1k": spent_usd(LEDGER_1K)}


def check(pilot: bool = True) -> None:
    s = spent()
    total = sum(s.values())
    if total >= SPEND_CAP_USD:
        raise BudgetExceeded(f"spent ${total:.2f} across all experiments, the ${SPEND_CAP_USD:.0f} program cap; "
                             "raising it needs Jono")
    ceiling = PILOT_CEILING_USD if pilot else CEILING_1H_USD
    if s["exp1h"] >= ceiling:
        raise BudgetExceeded(f"1h has spent ${s['exp1h']:.2f}, its ${ceiling:.0f} ceiling; going on needs Jono")


def check_judge() -> None:
    s = spent()
    total = sum(s.values())
    if total >= SPEND_CAP_USD:
        raise BudgetExceeded(f"spent ${total:.2f} across all experiments, the ${SPEND_CAP_USD:.0f} program cap; "
                             "raising it needs Jono")
    if s["exp1h_judge"] >= JUDGE_CEILING_USD:
        raise BudgetExceeded(f"the judge has spent ${s['exp1h_judge']:.2f}, its ${JUDGE_CEILING_USD:.0f} ceiling")
