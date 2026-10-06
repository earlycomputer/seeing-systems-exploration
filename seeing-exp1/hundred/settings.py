"""Constants for experiment 1h, the 100x measurement run. Anything that changes a result lives here, so it is logged by commit.

Jono, 2026-10-06: "I want to find 100x improvements in understanding, debugging, token cost, ease of expression,
shared understanding". 1h measures those five plus foresight and trust in one run (measure/README.md).

Twenty fresh briefs, harder than 1d's and written by a model that writes no worlds (briefs.py), each with a hidden
test in expectation forms that the authors never see. Three arms:

- `blind`: raw MJCF with no run information, as today's tools leave an agent: it writes the world and may check it
  against the brief, but is told nothing about the run.
- `xml`: raw MJCF with the language's two checks (langrun/lint.py), the run's history in words each round, and its own
  expectations checked against the run (1g's checked XML arm).
- `language`: the world language with its errors, the run in words and its expectations checked (1g's checked
  language arm).

After each world, both models read only its final file and say which hidden-test statements will hold (read.py):
foresight and shared understanding. Then a quiz on the runs, answered from raw MuJoCo state or from the run in
words (quiz.py): understanding.
"""

from config import ROOT

HUNDRED_DIR = ROOT / "hundred"
PROMPTS = HUNDRED_DIR / "prompts"
RESULTS_DIR = HUNDRED_DIR / "results"
RUNS_DIR = RESULTS_DIR / "runs"
READS_DIR = RESULTS_DIR / "reads"
QUIZ_DIR = RESULTS_DIR / "quiz"
SPEND_LEDGER = RESULTS_DIR / "spend.jsonl"
DRYRUN_DIR = ROOT / ".dryrun" / "hundred"
BRIEFS_FILE = HUNDRED_DIR / "briefs.json"  # written once by briefs.py, committed before any world is run
DRY_BRIEFS_FILE = HUNDRED_DIR / "dry_briefs.json"  # 1f's held-out ledge and chain, for plumbing tests only

ARMS = ("blind", "xml", "language")
MODELS = ("opus-5.5", "gpt-6.1")
BRIEF_WRITER = "gpt-5.6"  # writes the briefs and their hidden tests; writes no worlds
SEEDS = (0, 1)
N_BRIEFS = 20
MAX_ROUNDS = 3
MAX_LOAD_RETRIES = 2
SIM_SECONDS = 6.0
REST = 0.05  # m/s; at rest, as every earlier experiment
QUIZ_WORLDS = 40  # final runs quizzed, chosen by seeded draw among worlds that built
QUIZ_SEED = 0
RAW_HZ = 10  # raw-state rows per second in the quiz's raw representation; contacts within each 0.1 s are all listed

# 1h's own ceiling. Not yet approved: the program cap in config.py (shared by every experiment) must also allow it.
CEILING_1H_USD = 90.0
