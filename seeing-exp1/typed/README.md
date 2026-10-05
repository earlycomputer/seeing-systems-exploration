# Typed worlds: a first sketch

A world described as typed parts that say *how* it is built (a hinge, a spring, a pusher), compiled to MuJoCo
XML, with Elm-style problems before anything runs and a readback of what happened in the parts' own names.
Asked for by Jono on 2026-10-05 ("describe how instead of what"; "I continue to be inspired by Elm"). No model
calls and no spend: this is the vocabulary, checked against the seven 1d briefs.

## Run it

```bash
cd seeing-exp1 && source .venv/bin/activate
python -m typed.demo          # compiles the seven briefs, judges each with 1d's tests, writes demo_output.md
python -m typed.lang_demo     # the same seven written in the world language, with expect; writes lang_output.md
```

## Where things are

```
units.py      quantities with units in the type: m(), cm(), deg(), rad(), kg(), g(), mps(), rps(), Nm_per_rad()...
parts.py      the parts: Floor, Ball, Hoop, Ramp, OpenBox, Door, Catapult, Stack, Pusher, DominoRow, Pendulum
compiler.py   checks types, then meaning, then overlaps; all problems at once; XML only when there are none
replay.py     runs a compiled world; at(t) and events() say what happened in the parts' names
briefs.py     the seven 1d briefs written as parts
demo.py       the evidence: demo_output.md
lang.py       the world language: plain indented lines, units in the numbers, positions as relations, expect
worlds/       the seven briefs as .world files
lang_demo.py  the evidence for the language: lang_output.md
```

## The world language

Jono asked on 2026-10-05 what a language for worlds would look like if it dropped programming's brackets and
read well to people and machines alike. `lang.py` parses it into the typed parts above, so every check carries
over. A part starts at the margin, its facts are indented under it, and each line is one key and its value:

```
pendulum
  hangs from         1.01 m up
  length             95 cm
  bob                sphere 5 cm, 1 kg
  starts swung back  63°

ball
  is a   sphere 5 cm, 200 g
  rests  on floor, 10 cm ahead of pendulum

expect
  pendulum.bob touches ball
  ball comes to rest in cup
```

- **All seven briefs, written in it, pass their 1d tests**, and all 11 `expect` lines hold against the replay
  (`lang_output.md`). The seven files use no brackets at all. They run 86 lines (7 to 19 each, without `expect`),
  against 50 for the Python briefs and 229 for the hand-written XML: one fact per line costs lines.
- **Units are part of the number.** `from 0° to 2.1` stops with ANGLE WITHOUT A UNIT at line 8, and `95 g` where
  a length goes stops with WRONG KIND OF QUANTITY.
- **Positions are relations, read top to bottom.** `1 m beyond ball` needs `ball` written above it; a misspelt
  name gets "did you mean ball?". A part with a problem reports once: parts that refer to it stay quiet.
- **`expect` speaks the replay's words.** With 1d's weak catapult spring the file still builds, and the line
  fails with the evidence: `✗ ball comes to rest in bucket: ball comes to rest at (1.47, 0.00) m, 0.13 m short
  of bucket`.

Decisions taken alone: a part's name picks its kind (`cup` and `bucket` are open boxes); `along` is x, `up` is z,
`to the left` is y; a rod is given by its thickness, not its radius; parts may refer only to parts above them, so
a world reads in one pass; positions default to x = y = 0. Angles are written `63°` or `1.1 rad`: the pendulum's
1.1 rad became 63°, and the world still passes.

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
