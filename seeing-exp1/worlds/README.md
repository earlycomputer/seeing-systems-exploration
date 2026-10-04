# Experiment 1c: five worlds

Can an agent turn a one-line brief into a physical world that does what the brief says, and get there by
seeing and fixing it? A model writes a MuJoCo world from one sentence, MuJoCo runs it, and the model gets up
to three rounds to see and fix it: with a picture of the run, or with no readback at all. A test of each
brief, written before any run and never shown to the models, decides whether the world works. Proposed in
[Prototyping physical worlds](https://claude.ai/artifact/HX5KYtusMnqGxtS2xxzfVV); approved by Jono on
2026-10-04 to run after experiment 1b. Branch: `exp1c-five-worlds`.

## Run it

```bash
cd seeing-exp1 && source .venv/bin/activate          # experiment 1's venv and keys
python -m worlds.run --model opus-5.5 --brief catapult --arm picture --seed 0   # one world
python -m worlds.matrix --plan                       # what would run, rough cost
python -m worlds.matrix --first                      # seed 0, picture arm, every brief, both models
python -m worlds.matrix                              # all 40 worlds, 4 at a time, skips done worlds
python -m worlds.report                              # results/results.md
```

`--model dry-run` writes the hand-written world for each brief and says it works; `--model dry-run-echo`
writes an empty floor. Neither makes calls; both write to `.dryrun/worlds/` (gitignored).

## Where things are

```
settings.py   the five briefs, the names each needs, the arms, the readback, every constant
tests.py      load, run 6 s, and test a world against its brief from MuJoCo state
fixtures/     a hand-written world per brief that passes its own test; never sent to a model
draw.py       the picture readback for any world: residue of whatever moves, framed to fit the run
prompts/      every prompt, as sent
run.py        one world;  matrix.py  every world;  report.py  the generated tables;  budget.py  the cap
results/      runs/<world>/<timestamp>/ (every prompt, reply, file, image, test result), spend.jsonl
```

## The five briefs and their tests

| Brief | It works when MuJoCo shows |
|---|---|
| a regulation basketball is launched from the floor and drops through a hoop at 3.05 m, 4 m away | rim at 3.05 m and 4 m away (5%), ball radius 0.12 m (5%), launched from the floor, and the ball's center passes down through the rim's opening |
| a ball rolls down a ramp and comes to rest in a cup | the ball starts above the cup's rim and outside it, touches the ramp, and ends at rest inside the cup's footprint below its rim |
| a door swings shut and stays shut | the door starts open (20° or more) and within its hinge's range, stays within 2° of shut for the last second, and is still at the end |
| a stack of five blocks stands until the bottom block is pushed, then topples | the blocks start stacked, nothing moves for at least 0.2 s until the bottom block does, and the top block ends at least two block-heights lower |
| a catapult throws a ball into a bucket 3 m away | the ball starts at rest touching the catapult, the bucket is 2.5 to 3.5 m away, the ball is in the air at least 0.2 s, and it ends at rest inside the bucket |

## Decisions made without a human

- **Tests before runs.** Each brief's test is a MuJoCo measurement of its words, written and checked on
  hand-written worlds before any model run, and never shown to a model. The model gets only the brief and
  the names the test needs (`ball`, `cup`, `hinge`, `block1`..`block5`, the `rim`, `ramp` and `catapult`
  prefixes). Names fix what to measure, not what to build.
- **Each test was checked both ways.** Every fixture passes its own test and fails the other four (for
  missing names). Failing variants fail: a door with no spring, a door that starts outside its hinge's
  range, a stack pushed gently enough that it slides instead of toppling, a catapult spring too weak or too
  strong, and a ball given a launch velocity instead of being thrown.
- **A loophole closed before any run.** MuJoCo reads joint ranges in degrees. My first door fixture set
  the range in radians, so the door started far outside its own limit, and the limit snapped it shut. The
  door test now requires the door to start within its hinge's range.
- **The world runs itself.** MuJoCo resets to a `start` keyframe if there is one and runs 6 s. Nothing acts
  from outside: motion comes from the scene (keyframe velocities, springs, gravity, motors whose control the
  keyframe sets).
- **The loop.** One write, with up to two more tries if MuJoCo cannot load the file or a name is missing.
  Then up to three see-and-fix rounds. Each round the model says whether the world works and, if not, sends
  a corrected file. The loop stops when the model is satisfied or the rounds run out. A round whose file
  will not load sends MuJoCo's error next instead of a readback.
- **Two arms.** Picture: the run drawn as residue. Text: no readback, a request to check again. The text arm
  measures what thinking it through achieves without seeing anything.
- **Picture readback.** Experiment 1b's dot renderer, generalised. Whatever moves is drawn 24 times, evenly
  spaced in time from the start to when everything has come to rest (or 6 s), older copies lighter, so
  spacing still shows speed. The view is framed from the run itself so nothing is cut off. 128 px, the
  larger of 1b's sizes, because these worlds have more parts than one ball and a hoop. The view (drafting or
  camera) is set in `settings.VIEW` from 1b's results before any run.
- **Measures.** Loads; works as first written; works in the end; the round it first worked; whether the
  model's last claim was right; rounds used; minutes and dollars per world.
- **Size.** 5 briefs × 2 arms × 2 seeds × 2 models = 40 worlds. Seeds set the dot sampling for the picture
  arm and are plain repeats for text. Rough estimate $33, from 1b's cost per call.
- **Spend.** 1c has its own ledger; the cap check adds experiments 1 and 1b, so all three stay under $100.
