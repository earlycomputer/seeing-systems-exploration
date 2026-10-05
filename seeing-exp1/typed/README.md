# Typed worlds: a first sketch

A world described as typed parts that say *how* it is built (a hinge, a spring, a pusher), compiled to MuJoCo
XML, with Elm-style problems before anything runs and a readback of what happened in the parts' own names.
Asked for by Jono on 2026-10-05 ("describe how instead of what"; "I continue to be inspired by Elm"). No model
calls and no spend: this is the vocabulary, checked against the seven 1d briefs.

## Run it

```bash
cd seeing-exp1 && source .venv/bin/activate
python -m typed.demo          # compiles the seven briefs, judges each with 1d's tests, writes demo_output.md
```

## Where things are

```
units.py      quantities with units in the type: m(), cm(), deg(), rad(), kg(), g(), mps(), rps(), Nm_per_rad()...
parts.py      the parts: Floor, Ball, Hoop, Ramp, OpenBox, Door, Catapult, Stack, Pusher, DominoRow, Pendulum
compiler.py   checks types, then meaning, then overlaps; all problems at once; XML only when there are none
replay.py     runs a compiled world; at(t) and events() say what happened in the parts' names
briefs.py     the seven 1d briefs written as parts
demo.py       the evidence: demo_output.md
```

## What it showed

- **All seven briefs fit.** Each compiles to MuJoCo and passes its own 1d test, unchanged (`demo_output.md`).
  The seven take 5 to 10 lines each (50 in all) against 229 lines of hand-written XML; the shot is 6 against 63.
- **The hinge trap can't be written.** `range=(deg(0), 2.1)` stops with ANGLE WITHOUT A UNIT. Written with the
  wrong unit, `deg(2.1)`, it stops with STARTS OUTSIDE ITS OWN RANGE. Written as meant, `rad(2.1)`, the door
  swings shut and passes. 1d's door break was fixed by no model in 16 tries.
- **Contact failures still need the run.** The cup moved away, the slow pusher and the weak spring all compile
  cleanly. Types can't know a spring of 2.0 N·m/rad is too weak; the readback says "Ball comes to rest 0.13 m
  short of Bucket", in words, from the run.
- **One break can't be said at all.** `Ball` has no spin field, so 1d's backspin break is not expressible. That
  is a vocabulary decision: it removes a mistake and a capability together.
- **The checker found a flaw in a hand-written fixture.** 1d's pendulum stand overlapped its rod by 10 mm at the
  start. The hinge pins the rod, so no result changed, but nobody had noticed. The typed stand clears the rod.

## Decisions made without a human

- **Python dataclasses, not a new language.** The program is Python and MuJoCo's bindings are Python. Frozen
  dataclasses give values that can't change, type hints the compiler reads, and `dataclasses.replace` for edits.
- **Every number has a unit, except dimensionless ones.** Friction coefficients are plain floats; the catapult's
  armature (kg·m²) is a plain float for now.
- **Angles reach MuJoCo in radians only.** The compiler writes `<compiler angle="radian"/>` in every file.
- **Parts own the names the tests need.** A world written from parts can't miss `ball`, `hinge` or `catapult_*`.
- **The keyframe is generated.** 1d's dominoes keyframe was 60 hand-typed velocities; parts now say
  `first_tip=rps(4)` and the compiler writes the keyframe in MuJoCo's joint order.
- **Each part reproduces its fixture.** Sizes, masses and offsets were copied from the hand-written worlds, so
  "passes its 1d test" compares like with like. The ball on the ramp sits 1 mm lower than the fixture's.
