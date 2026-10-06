"""Constants for experiment 1e, the run in words. Anything that changes a result lives here, so it is logged by commit.

1d's 40 broken worlds again, with a third readback beside 1d's picture and text: the run's history in words
(history/narrate.py), written from MuJoCo's state by a program that knows nothing of the brief. Everything else is
1d's: the same five broken files, briefs, naming conventions, prompts, three rounds, models, effort, seeds and
tests. 1d's picture and text worlds are the comparison and are not re-run.
"""

from config import ROOT

HISTORY_DIR = ROOT / "history"
RESULTS_DIR = HISTORY_DIR / "results"
RUNS_DIR = RESULTS_DIR / "runs"
SPEND_LEDGER = RESULTS_DIR / "spend.jsonl"
DRYRUN_DIR = ROOT / ".dryrun" / "history"
PROMPTS = HISTORY_DIR / "prompts"

BRIEFS = ("shot", "cup", "door", "stack", "catapult")  # 1d's broken worlds
ARM = "history"
