"""Constants for experiment 1j, the complexity ladder. Anything that changes a result lives here, so it is logged by commit.

Jono, 2026-10-07 23:44: "My hunch is that those numbers aren't linear and scale with complexity." 1h by chain length
hinted at it (a tie at 4 steps, the language ahead at 5 and 6), but 1h's chains were 4 to 6 steps. The ladder holds the
mechanisms fixed and varies only the length: each family is one 16-step chain, and its 2-, 4- and 8-step briefs are the
same chain cut short. Jono, 2026-10-08 06:15: "Run the complexity ladder experiment".

Everything 1h learned goes in from the start: the fixed hidden test (hundred/hidden.py: either hinge stop, 0.1 s order
slack, exact names), the settle check and the run in words with openings and stops by height (hundred/settle.py,
hundred/words.py), and the independent judge (hundred/judge.py) on every finished world. Arms as 1h (hundred/run.py).
"""

from config import ROOT

LADDER_DIR = ROOT / "ladder"
PROMPTS = LADDER_DIR / "prompts"
RESULTS_DIR = LADDER_DIR / "results"
RUNS_DIR = RESULTS_DIR / "runs"
JUDGE_DIR = RESULTS_DIR / "judge"
SPEND_LEDGER = RESULTS_DIR / "spend.jsonl"  # worlds, briefs and judge alike
BRIEFS_FILE = LADDER_DIR / "briefs.json"  # written once by briefs.py, committed before any world is run
DRYRUN_DIR = ROOT / ".dryrun" / "ladder"

LEVELS = (2, 4, 8, 16)  # causal steps in the chain; one hidden-test line per step
SECONDS = {2: 6.0, 4: 8.0, 8: 12.0, 16: 20.0}  # run length per level, told to the brief writer and the authors
N_FAMILIES = 4
ARMS = ("blind", "xml", "language")
MODEL = "gpt-6.1"
JUDGE = "gpt-6.1"
BRIEF_WRITER = "gpt-5.6"
SEEDS = (0, 1)

# 1j's own ceiling. Jono, 2026-10-08 06:15, on the coordinator's summary saying the ladder costs "about $30" and needs
# the cap raised "to about $250": "Run the complexity ladder experiment". $213.26 was spent before it.
# Raised to $68 the same day: a 16-step world costs about $1.30, not $0.30; Jono chose "Full ladder" (about $63).
# Raised to $78 with the cap to $295 (Jono, "Raise to $295"), for seed 1 and the judge.
CEILING_1J_USD = 78.0
