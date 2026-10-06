"""Constants for experiment 1f, the language run. Anything that changes a result lives here, so it is logged by commit.

Models write worlds from a one-line brief in one of two formats, and fix them over up to three rounds:

- `language`: the world language (typed/lang.py), with a reference (prompts/guide.md), the whole parts library and
  one example world. Problems come back as the language's Elm-style errors.
- `xml`: raw MJCF with 1d's authoring prompt and conventions, plus the two checks the language runs after parsing,
  in the same words (langrun/lint.py): a joint that starts outside its own range, and parts that start inside each
  other. MuJoCo's own load errors come back as in 1d.

Both arms then get the same readback each round: the run's history in words from 1e (history/narrate.py), on the
compiled MJCF. Ten briefs: 1d's seven, where the language's library already has parts for the hoop, ramp, door,
catapult, open box and pendulum, and three held-out briefs written after the language and its library, which
nobody tuned it on. 1d's tests and langrun/heldout.py judge every file; the model never sees them.
"""

from config import ROOT
from harder.settings import BRIEFS as BRIEFS_1D

LANGRUN_DIR = ROOT / "langrun"
RESULTS_DIR = LANGRUN_DIR / "results"
RUNS_DIR = RESULTS_DIR / "runs"
SPEND_LEDGER = RESULTS_DIR / "spend.jsonl"
DRYRUN_DIR = ROOT / ".dryrun" / "langrun"
PROMPTS = LANGRUN_DIR / "prompts"
FIXTURES = LANGRUN_DIR / "fixtures"

ARMS = ("language", "xml")
MODELS = ("opus-5.5", "gpt-6.1")
SEEDS = (0, 1)
MAX_ROUNDS = 3
MAX_LOAD_RETRIES = 2
SIM_SECONDS = 6.0

HELDOUT = {
    "seesaw": {
        "brief": "a 1 kg ball dropped onto one end of a seesaw throws a 100 g ball resting on the other end at least "
                 "50 cm above where it started",
        "names": "The seesaw is a body named `seesaw` on a hinge joint. The dropped ball is a body named `weight` with a "
                 "`<freejoint/>`. The thrown ball is a body named `ball` with a `<freejoint/>` and one sphere geom named "
                 "`ball`.",
    },
    "ledge": {
        "brief": "a ball rolls along a table, off its edge, and lands in a bucket on the floor whose centre is 60 cm "
                 "beyond the table's edge",
        "names": "The ball is a body named `ball` with a `<freejoint/>` and one sphere geom named `ball`. Every geom of the "
                 "table is named with the prefix `table`. The bucket is a body named `bucket`; all its geoms belong to it.",
    },
    "chain": {
        "brief": "three balls sit in a row on the floor; the first is rolled into the second, the second rolls into the "
                 "third, and the third rolls into a cup",
        "names": "The balls are bodies named `ball1` (the one set rolling), `ball2` and `ball3`, each with a "
                 "`<freejoint/>` and one sphere geom. The cup is a body named `cup`; all its geoms belong to it.",
    },
}

# The same names, said in the language's terms (a thing's name becomes its MuJoCo body; a part's pieces become geoms
# named <thing>_<piece>).
LANGUAGE_NAMES = {
    "shot": "Name the ball `ball` (a sphere that moves freely). Name the hoop `hoop`; its rim must be a ring piece named "
            "`rim`, as in the library's hoop part.",
    "cup": "Name the ball `ball` (a sphere that moves freely), the ramp `ramp` and the cup `cup`.",
    "door": "Name the door `door`; it turns on a hinge named `hinge`. The door is shut when the hinge is at 0°.",
    "stack": "The blocks are five boxes or cubes named `block1` (bottom) to `block5` (top), each moving freely "
             "(`stacked 5 high` on a thing named `block` does this). Whatever does the pushing is part of the world.",
    "catapult": "Name the ball `ball` (a sphere that moves freely); it starts at rest in the catapult. Name the catapult "
                "`catapult` and the bucket `bucket`.",
    "dominoes": "The dominoes are boxes named `domino1` (the first to fall) to `domino10`, each moving freely, each with "
                "its longest side as its height (`repeated 10 times, ... apart along` on a thing named `domino` does "
                "this).",
    "pendulum": "Name the pendulum `pendulum`; it turns on a hinge. Name the ball `ball` (a sphere that moves freely) and "
                "the cup `cup`.",
    "seesaw": "Name the seesaw `seesaw`; it turns on a hinge. Name the dropped ball `weight` and the thrown ball `ball`; "
              "both move freely, and `ball` is a sphere.",
    "ledge": "Name the ball `ball` (a sphere that moves freely), the table `table` and the bucket `bucket`.",
    "chain": "Name the balls `ball1` (the one set rolling), `ball2` and `ball3`, spheres that move freely, and the cup "
             "`cup`.",
}

BRIEFS = {k: {"brief": v["brief"], "names": v["names"], "kind": "library" if k in ("shot", "cup", "door", "catapult", "pendulum") else "primitives", "set": "1d"}
          for k, v in BRIEFS_1D.items()} | {k: dict(v, kind="primitives", set="held-out") for k, v in HELDOUT.items()}
