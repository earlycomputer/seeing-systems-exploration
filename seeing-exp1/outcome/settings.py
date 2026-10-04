"""Constants for experiment 1b. Anything that changes a result lives here, so it is logged by commit.

Experiment 1's config.py still holds what both share (timestep, render size, seeds, the $100 cap).
"""

from config import ROOT

OUTCOME_DIR = ROOT / "outcome"
SCENE_DIR = OUTCOME_DIR / "scene"
RESULTS_DIR = OUTCOME_DIR / "results"
RUNS_DIR = RESULTS_DIR / "runs"
SPEND_LEDGER = RESULTS_DIR / "spend.jsonl"  # 1b's own; the cap check adds experiment 1's ledger too
DRYRUN_DIR = ROOT / ".dryrun" / "outcome"

SOURCE_SCENE = ROOT / "scene" / "authored.xml"  # experiment 1's scene, exactly as Opus wrote it
AIRED_SCENE = SCENE_DIR / "aired.xml"  # the same scene with air added by the harness
SHOT_SCENE = SCENE_DIR / "shot_authored.xml"  # Opus's shot keyframe added, as Opus wrote it
BASE_SCENE = SCENE_DIR / "base.xml"  # the made shot every cell starts from
BASE_RECORD = SCENE_DIR / "base.json"  # how the base was reached, and the deliberate misses as measured

# Air (design entry 2026-10-04). Density on <option>, and MuJoCo's ellipsoid fluid model on the ball with
# its blunt drag halved from the default 0.5 to 0.25, which gives a real basketball's drag (Cd about 0.5:
# 1.34 N at 10 m/s). MuJoCo's default inertia-box model, and the ellipsoid default, both give about twice
# that. The other coefficients stay at MuJoCo's defaults; with the added-mass term MuJoCo includes, the
# default Magnus coefficient gives a realistic lift for backspin (0.86 N at 10 m/s and 20 rad/s).
AIR_DENSITY = 1.2  # kg/m^3
BALL_FLUID = {"fluidshape": "ellipsoid", "fluidcoef": "0.25 0.25 1.5 1.0 1.0"}

SHOT_KEY = "shot"  # the keyframe Opus writes; every deliberate miss edits only its line
MAX_FLIGHT_S = 4.0  # stop simulating at first landing, or here

# Deliberate misses (design entry): one-line edits to the keyframe's qvel. If MuJoCo shows a miss is not
# clear-cut on the base shot, the larger step is used instead, and base.json records which.
MISSES = {
    "short": {"kind": "speed", "steps": (-0.08, -0.12)},  # launch speed scaled by 1 + step
    "long": {"kind": "speed", "steps": (0.08, 0.12)},
    "left": {"kind": "aim", "steps": (5.0, 8.0)},  # degrees, turned toward +y (the shooter's left)
    "none": {"kind": "none", "steps": (0.0,)},
}

# Readbacks (design entry, six conditions). The scene text is always included: the model edits it.
CONDITIONS = ("text", "numbers", "camera_128", "camera_64", "drafting_128", "drafting_64")
RESIDUE_EVERY_S = 0.1  # a copy of the ball every 0.1 s from launch to first landing
RESIDUE_OLDEST_WEIGHT = 0.3  # the oldest copy's ink, as a fraction of the newest's darkness
NUMBERS_EVERY_S = 0.05

# Drafting view: side elevation over plan, one shared scale, stacked in one square image. Ranges fixed
# before any model run so every deliberate miss's whole flight fits, at the steps base.json settled:
# x -0.12 to 6.22 m (long), y up to 1.21 m (left), z up to 5.13 m (long); the backboard spans y +-0.9 m.
# 7.8 m across 512 px is 65.6 px/m.
DRAFT_X = (-0.7, 7.1)  # m, both views
DRAFT_SIDE_Z = (-0.2, 5.35)  # m, side view (looking along +y)
DRAFT_PLAN_Y = (-1.0, 1.25)  # m, plan view (looking down), +y up the page
DRAFT_RULE_GRAY = 0.5  # one-pixel rule between the two views at 512 px

MODELS = ("opus-5.5", "gpt-6.1")
SEEDS = (0, 1, 2)
