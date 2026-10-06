"""Constants every step shares. Anything that changes a result lives here, so it is logged by commit."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCENE_DIR = ROOT / "scene"
RESULTS_DIR = ROOT / "results"
RUNS_DIR = RESULTS_DIR / "runs"
SPEND_LEDGER = RESULTS_DIR / "spend.jsonl"
DRYRUN_DIR = ROOT / ".dryrun"  # dry-run output; gitignored and never read by make_results

BRIEF_FILE = SCENE_DIR / "brief.txt"
AUTHORED_SCENE = SCENE_DIR / "authored.xml"  # written by step 1 (scene/author.py); the matrix runs on this
FIXTURE_SCENE = SCENE_DIR / "fixture_handwritten.xml"  # hand-written, for development only

# Determinism (handoff, Environment).
TIMESTEP = 0.002

# What the brief asks for, as numbers. "Fixed" means within TOLERANCE of these after one correction turn.
TARGETS = {
    "hoop_height": 3.05,  # m, rim center z
    "ball_hoop_distance": 4.0,  # m, horizontal, ball center to rim center at t=0
    "ball_radius": 0.12,  # m, regulation size 7 is 0.119; the handoff uses 0.12
}
TOLERANCE = 0.05

RENDER_SIZE = 512
RESOLUTIONS = (128, 64, 32)
SEEDS = (0, 1, 2)

# Guardrail: spending past this needs a human first (handoff, Decisions). Raised from $100 on 2026-10-06: Jono said
# "Ok to increase budget, just keep me up to date" and chose the 1g rerun, "about $15, bringing the total to about
# $100" ($84.58 spent before it). Then "No need to stop at $18. Be thorough": 1g grew to four seeds and a control,
# stopping at $70 (history/budget.py).
SPEND_CAP_USD = 160.0
