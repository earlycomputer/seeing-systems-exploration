"""Constants for experiment 1c, five worlds. Anything that changes a result lives here, so it is logged by commit.

Each brief is one line a person might type. Its conventions fix only the names MuJoCo needs to measure the
world, never what the model builds. The pass test for each brief (worlds/tests.py) is written before any
model run and is never shown to the models.
"""

from config import ROOT

WORLDS_DIR = ROOT / "worlds"
RESULTS_DIR = WORLDS_DIR / "results"
RUNS_DIR = RESULTS_DIR / "runs"
SPEND_LEDGER = RESULTS_DIR / "spend.jsonl"  # 1c's own; the cap check adds experiments 1 and 1b
DRYRUN_DIR = ROOT / ".dryrun" / "worlds"
FIXTURES_DIR = WORLDS_DIR / "fixtures"  # hand-written worlds that prove each test can pass; never sent to a model

SIM_SECONDS = 6.0  # every world runs this long from its start
START_KEY = "start"  # optional keyframe the harness resets to before running

BRIEFS = {
    "shot": {
        "brief": "a regulation basketball is launched from the floor and drops through a hoop at 3.05 m, 4 m away",
        "names": "The ball is a body named `ball` with a `<freejoint/>` and one sphere geom named `ball`. The hoop "
                 "is a body named `hoop` whose origin is the center of the rim; every rim geom is named with the "
                 "prefix `rim`.",
    },
    "cup": {
        "brief": "a ball rolls down a ramp and comes to rest in a cup",
        "names": "The ball is a body named `ball` with a `<freejoint/>` and one sphere geom named `ball`. Every geom "
                 "of the ramp is named with the prefix `ramp`. The cup is a body named `cup`; all its geoms belong "
                 "to it.",
    },
    "door": {
        "brief": "a door swings shut and stays shut",
        "names": "The door is a body named `door` on a hinge joint named `hinge`. The door is shut when `hinge` is "
                 "at 0.",
    },
    "stack": {
        "brief": "a stack of five blocks stands until the bottom block is pushed, then topples",
        "names": "The blocks are bodies named `block1` (bottom) to `block5` (top), each with a `<freejoint/>` and "
                 "one box geom. Whatever does the pushing is part of the scene.",
    },
    "catapult": {
        "brief": "a catapult throws a ball into a bucket 3 m away",
        "names": "The ball is a body named `ball` with a `<freejoint/>` and one sphere geom named `ball`; it starts "
                 "at rest in the catapult. Every geom of the catapult is named with the prefix `catapult`. The "
                 "bucket is a body named `bucket`; all its geoms belong to it.",
    },
}

ARMS = ("picture", "text")  # see-and-fix with a picture of the run, or with no readback at all
MAX_ROUNDS = 3  # see-and-fix rounds after the first write
MAX_LOAD_RETRIES = 2  # a file MuJoCo cannot load, or that lacks a required name, goes back with the error
MODELS = ("opus-5.5", "gpt-6.1")
SEEDS = (0, 1)

# Picture readback: residue of everything that moves, auto-framed so the whole run fits, at 128 px.
# VIEW is "drafting" or "camera"; set from 1b's results before any 1c run (journal, decision log).
VIEW = "drafting"
RES = 128
RESIDUE_COPIES = 16  # copies of each moving body across the active part of the run, older lighter
REST_SPEED = 0.05  # m/s: a body slower than this is at rest
