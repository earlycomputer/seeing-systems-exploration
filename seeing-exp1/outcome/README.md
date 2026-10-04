# Experiment 1b: see the outcome

Can a model correct what it made happen, when the error shows only in the outcome and not in any line of
text? Opus 5.5 writes a shot as a MuJoCo keyframe. The harness misses it on purpose by a one-line edit to
that keyframe, MuJoCo flies it, and the model has to say where the ball went and correct the shot, from one
of six readbacks. Design: the 2026-10-04 entries in the
[design journal](https://claude.ai/artifact/88e7a541-1b9c-49d6-85f3-d7ee56581363). Branch:
`exp1b-see-the-outcome`.

## Run it

```bash
cd seeing-exp1                     # the venv and keys are experiment 1's; see ../README.md
source .venv/bin/activate
python -m outcome.author --model opus-5.5      # step 1: Opus adds the shot; base shot and misses settled
python -m outcome.run --model opus-5.5 --condition camera_64 --miss short --seed 0   # one cell
python -m outcome.matrix --plan                # what would run, rough cost
python -m outcome.matrix --first               # the first real runs: seed 0 of eight cells per model
python -m outcome.matrix                       # all 144 cells, 4 at a time, skips done cells
python -m outcome.report                       # results/results.md and results/failures.md
```

Every step takes `--model dry-run` (always right) or `--model dry-run-echo` (always says it goes in and
changes nothing), which make no calls and write to `.dryrun/outcome/` (gitignored).

## Where things are

```
settings.py   every constant that changes a result
shot.py       air, the keyframe, flying the shot, made or missed and which way, the deliberate misses
draw.py       residue in experiment 1's camera and in the drafting view; the flight as numbers
author.py     step 1; budget.py the spend cap; run.py one cell; matrix.py; report.py; viewer.py (viewer.html)
prompts/      every prompt, as sent
scene/        brief.txt, aired.xml, shot_authored.xml + .json (Opus's reply), base.xml + base.json
results/      runs/<cell>/<timestamp>/ (every prompt, reply, raw response, image, measurement), spend.jsonl,
              results.md and failures.md (generated), summary.md (written after reading)
NOTES.md      parking lot and observations;  STATUS.md  where it stands
```

## The base shot

Opus 5.5 wrote `qvel="3.21 0 9.3 0 0 0"` on its first attempt ($0.18): 9.84 m/s at 71 degrees, no spin,
from a hand integration of the drag equations in its reasoning. MuJoCo flies it through the rim 1.4 cm from
the center, apex 4.11 m. It is a clean make as written, so the harness did not tune it: `base.xml` is
Opus's file.

## Decisions made without a human

Each is logged here so it shows its origin; the ones that change the design are also in the journal.

- **Air is realistic, not MuJoCo's default.** The design fixed air at 1.2 kg/m³. MuJoCo's default fluid
  model treats the ball as its inertia box and gives about twice a real basketball's drag (2.7 N at
  10 m/s against about 1.3 N for Cd 0.5), so the harness adds air as two one-line edits: `density="1.2"` on
  `<option>`, and `fluidshape="ellipsoid" fluidcoef="0.25 0.25 1.5 1.0 1.0"` on the ball's geom, which is
  MuJoCo's ellipsoid model with its blunt drag halved to match Cd 0.5. With MuJoCo's added-mass term the
  default Magnus coefficient already gives a realistic backspin lift (0.86 N at 10 m/s, 20 rad/s). A model
  that knows real basketball physics should get close, but not exact.
- **Made** means the ball's center passes down through the rim's plane within the rim's opening (0.224 m
  from its center, measured from the rim geoms), in the real flight with every contact, before landing.
- **Which way it missed** is read from a ghost flight in which only the ball and floor collide: where its
  path crosses the rim's plane on the way down, along and across the line from the ball to the hoop. The
  larger of the two decides short, long, left or right; a path that never reaches rim height is short.
  A shot made off the backboard counts as made, but cannot be the base: the base must be a clean make, its
  own path through the opening.
- **Landing** is the first contact while the ball's center is below 0.5 m after it leaves the floor: the
  floor, or the hoop support's base plate, which one shot hit first.
- **Deliberate misses on this base:** short is launch speed −8% (path 0.86 m short of the rim center),
  left is the aim turned 5° toward +y (0.35 m left), and long is +12%, because +8% banks in off the
  backboard: its path would cross 0.80 m long, but the board drops it through the rim. The design allowed
  that step up. At +12% the path crosses 1.20 m long and the ball goes over the board.
- **Residue**: a copy of the ball every 0.1 s from launch, plus the landing itself; ink from 30% (oldest)
  to 100% (landing). The copies are the ball's own dots at its real pose, so they turn with any spin.
- **Drafting view**: side elevation (looking along +y) over plan (looking down), one scale of 65.6 px/m at
  512 px so x lines up between them; x −0.7 to 7.1 m, side z −0.2 to 5.35 m, plan y −1.0 to 1.25 m, a gray
  rule between. The ranges were set after the misses were settled and before any model run, so every
  deliberate miss's whole flight fits. Experiment 1's camera is unchanged, so the long miss's apex runs off
  the top of its frame.
- **Numbers**: the ball's center every 0.05 s to the millimetre, with the landing as the last row.
- **Turns.** Turn 2 asks for a change to the `shot` key's qvel only. A correction counts only if nothing
  else in the file changed and the ball still starts where it rests. XML comments do not count as changes,
  wherever they sit: the prompt asks for one, and Opus put its comment just after `</keyframe>`. The
  first batch ran with a check that counted it; `python -m outcome.rescore` re-judged those runs from
  their saved files and kept the old verdicts under `superseded` in each run.json. If the turn-2 file cannot run, turn 3
  sends MuJoCo's error instead of a readback. If turn 3 gives no file, the turn-2 correction stands.
- **Seeds** set the dot sampling, so each seed is a slightly different picture and an independent sample.
  For text only and numbers, seeds are plain repeats.
- **Models and settings** as experiment 1: Opus 5.5 and GPT-6.1 Sol, effort high, no refusal fallbacks.
- **Spend**: 1b has its own ledger, `results/spend.jsonl`. The cap check adds experiment 1's, so the two
  stay under $100 together.
