"""Constants for experiment 1h, the 100x measurement run. Anything that changes a result lives here, so it is logged by commit.

Jono, 2026-10-06: "I want to find 100x improvements in understanding, debugging, token cost, ease of expression,
shared understanding". 1h measures those five plus foresight and trust in one run (measure/README.md).

Twenty fresh briefs, harder than 1d's and written by a model that writes no worlds (briefs.py), each with a hidden
test in expectation forms that the authors never see. Three arms:

- `blind`: raw MJCF with no run information, as today's tools leave an agent: it writes the world and may check it
  against the brief, but is told nothing about the run.
- `xml`: raw MJCF with the language's two checks (langrun/lint.py) and the run's history in words each round (1g
  control's XML arm).
- `language`: the world language with its errors and the run in words (1g control's language arm).

No arm writes or hears expectations. 1g (2026-10-06) found that asking for them made first attempts worse (115
against 134 of 160 working as first written, p = 0.015) and checking them every round didn't help (149 against 156
in the end, p = 0.11): models argued with the checker, or never wrote down what the test checks. Every arm gets 1g
control's line on what "at rest" means.

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

# 1h's own ceiling past the pilot. Jono, 2026-10-07 01:02, on running the other 15 briefs with GPT-6.1 only (90 worlds
# plus reads, "about $12"): "go for it". The pilot spent $46.15, so 1h stops here.
# It cost more than estimated ($0.23 a world, not $0.13) and stopped at the program cap; Jono: "Continue on!" (2026-10-07).
CEILING_1H_USD = 72.0
