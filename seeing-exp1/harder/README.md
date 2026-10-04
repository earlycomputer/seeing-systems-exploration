# Experiment 1d: harder worlds

When a world fails in a way only running it reveals, does seeing the run let a model fix it, where thinking it
over does not? In 1c the 6 failing worlds were whatever the models wrote, and the picture fixed 2. 1d breaks
worlds on purpose so every failure is known in advance, and adds two briefs built around things that don't
happen. Design: the journal's 2026-10-04 entry "Experiment 1d started"
([design journal](https://claude.ai/artifact/88e7a541-1b9c-49d6-85f3-d7ee56581363)). Approved by Jono on
2026-10-04, up to $25. Branch: `exp1d-harder-worlds`.

## Run it

```bash
cd seeing-exp1 && source .venv/bin/activate          # experiment 1's venv and keys
python -m harder.selftest                            # tests checked both ways, the residue fix; no calls
python -m harder.breaks                              # (re)write harder/broken/ from 1c's fixtures
python -m harder.run --model opus-5.5 --brief door --arm picture --seed 0   # one world
python -m harder.matrix --plan                       # what would run, rough cost
python -m harder.matrix --first                      # seed 0 of every brief and arm, both models (28 worlds)
python -m harder.matrix                              # all 112 worlds, 4 at a time, skips done worlds
python -m harder.report                              # results/results.md
python -m harder.viewer                              # results/viewer.html
```

`--model dry-run` fixes each broken world with 1c's hand-written file and writes each new brief's fixture;
`--model dry-run-echo` changes nothing. Neither makes calls; both write to `.dryrun/harder/` (gitignored).

## Where things are

```
settings.py   the seven briefs, the five breaks, the arms, every constant
tests.py      1c's five tests (unchanged) plus dominoes and pendulum
breaks.py     writes broken/<brief>.xml from 1c's fixtures and settings.BREAKS
selftest.py   every test checked both ways, every break checked to fail, the residue fix checked
rescore.py    re-judges every saved file with the current tests, keeping old verdicts under `superseded`
fixtures/     hand-written dominoes and pendulum worlds that pass their tests; never sent to a model
broken/       the five broken worlds, exactly as sent
run.py        one world;  matrix.py  every world;  report.py  the tables;  budget.py  the cap and 1d's ceiling
viewer.py     results/viewer.html: every world running in 3D (1c's viewer, merged from exp1c-viewer)
prompts/      every prompt, as sent (1c's, plus given.md for a broken world)
results/      runs/<world>/<timestamp>/ in 1c's layout (every file as XML, world.json), spend.jsonl
```

## The briefs

| Brief | Kind | It works when MuJoCo shows |
|---|---|---|
| a regulation basketball is launched from the floor and drops through a hoop at 3.05 m, 4 m away | broken | as 1c |
| a ball rolls down a ramp and comes to rest in a cup | broken | as 1c |
| a door swings shut and stays shut | broken | as 1c |
| a stack of five blocks stands until the bottom block is pushed, then topples | broken | as 1c |
| a catapult throws a ball into a bucket whose centre is 3 m from where the ball starts | broken | as 1c |
| ten dominoes stand in a row; the first is tipped over and knocks down the rest, and every domino ends tilted at least 15 degrees from upright | new | all ten start upright on the floor; only the first is set moving; they start falling in order; every one ends tilted at least 15° |
| a pendulum swings down and strikes a ball resting on the floor, which rolls into a cup whose centre is 1 m from where the ball starts | new | the ball starts at rest on the floor; the cup's centre is 0.9 to 1.1 m from it; the pendulum touches the ball before it moves; the ball ends at rest in the cup |

## The breaks

| World | One-line edit to 1c's hand-written file | What running shows |
|---|---|---|
| shot | launch `qvel` gains backspin `0 -30 0` | the ball comes down 0.58 m short of the rim |
| cup | the cup moves from x = 2.05 to 2.65 m | the ball lands and stops short of it |
| door | `range="0 120"` becomes `range="0 2.1"` | MuJoCo reads degrees, so the limit snaps the open door shut at once: no swing |
| stack | the pusher's speed 3.0 becomes 1.5 m/s | the stack is shoved but does not topple |
| catapult | the spring's stiffness 3.0 becomes 2.0 | the ball falls short of the bucket |

## Decisions made without a human

- **The residue fix (before any run).** 1c's `draw.active_until` judged rest from each body's origin, so a
  door or pendulum turning about its origin never counted as moving, and every 1c door picture stopped at
  0.6 s (found by the parent session's viewer). It now adds each body's turning rate times its reach. Fixed
  in `worlds/draw.py`, which 1d shares; 1c's saved pictures and verdicts are unchanged. `selftest.py` checks
  the door and pendulum residue runs past their last turn.
- **The catapult's measurement.** Jono approved "3 m from the catapult (or whatever single measurement you
  choose)". The brief says "whose centre is 3 m from where the ball starts", the one point 1c's test already
  measures, so the test and the fixture carry over unchanged.
- **The breaks.** Each is one edit, chosen so the file still looks plausible and only running it shows the
  failure; each was tried at a few sizes and the first clear failure taken. Backspin made the shot fall short,
  not long as the design guessed. `selftest.py` checks each break trips the check it is meant to.
- **How a broken world is presented.** As "a scene written for this brief", to check, never as known to be
  broken, so text only must find the problem unaided. Its first round comes with the file; after the model
  edits it, prompts say "your scene", as in 1c.
- **New tests.** Dominoes: upright means the box's longest side within 10° of vertical; falling in order
  means each starts to tilt (2°) after the one before. Pendulum: struck means a pendulum geom touches the
  ball before the ball has moved 1 cm. Each test fails its own variants in `selftest.py` (a gap in the row,
  a second domino set moving, a pendulum released too low, the cup too far, a launched ball).
- **Size, spend and the first runs.** 7 briefs × 2 arms × 4 seeds × 2 models = 112. The first runs are seed 0
  of every brief and arm (28). If their rate projects 1d over $25, it stops for Jono; `budget.py` also refuses
  any call once 1d has spent $25.
- **A test flaw the first runs found, fixed and rescored.** The dominoes test required all ten dominoes to
  start upright. Three of the first four dominoes worlds started the first domino leaning 15 to 20 degrees,
  a fair reading of "the first is tipped over", and were failed for it. The test now requires only the other
  nine to start upright (`selftest.py` checks that a leaning first domino passes and a leaning second one fails).
  `python -m harder.rescore` re-judged every saved file: 3 worlds changed from fail to pass. Each world.json
  keeps its old verdicts under `superseded`. The tests never reach the models or steer the loop, so the
  re-judged verdicts are exactly what the fixed test would have given live.
- **A second test flaw, found after the full run.** The pendulum test took the cup's centre from the box
  around all its geoms. The naming convention puts every cup geom in the cup body, so a cup with an entry ramp
  measured from the ramp's end: four cups placed exactly 1 m away measured 0.82 to 0.88 m. The centre is now
  the cup body's origin when that lies within the cup's footprint, otherwise the footprint's middle
  (`selftest.py` checks a ramped cup and an offset cup). Rescored: 3 worlds changed from fail to pass.
- **The viewer.** 1c's viewer (parent session, `exp1c-viewer`) was merged into this branch, as the plan
  said, and `viewer.py` adapts it: 1d's tests, the broken file shown as given, each world's break named.
