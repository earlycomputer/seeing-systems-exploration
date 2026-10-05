# Typed worlds: a first sketch

A world described as typed parts that say *how* it is built (a hinge, a spring, a pusher), compiled to MuJoCo
XML, with Elm-style problems before anything runs and a readback of what happened in the parts' own names.
Asked for by Jono on 2026-10-05 ("describe how instead of what"; "I continue to be inspired by Elm"). No model
calls and no spend: this is the vocabulary, checked against the seven 1d briefs.

## Run it

```bash
cd seeing-exp1 && source .venv/bin/activate
python -m typed.demo          # compiles the seven briefs, judges each with 1d's tests, writes demo_output.md
python -m typed.lang_demo     # the seven in the world language, built from library.world; writes lang_output.md
```

## Where things are

```
units.py      quantities with units in the type: m(), cm(), deg(), rad(), kg(), g(), mps(), rps(), Nm_per_rad()...
parts.py      the parts: Floor, Ball, Hoop, Ramp, OpenBox, Door, Catapult, Stack, Pusher, DominoRow, Pendulum
compiler.py   checks types, then meaning, then overlaps; all problems at once; XML only when there are none
replay.py     runs a compiled world; at(t) and events() say what happened in the parts' names
briefs.py     the seven 1d briefs written as parts
demo.py       the evidence for the Python layer: demo_output.md
lang.py       the world language: primitives, relations, parts from library.world, bodies, expect
library.world the parts library, written in the language itself: open box, ramp, door, catapult, pendulum,
              hoop, table, raised bucket
worlds/       the seven briefs as .world files, plus raised.world (a new part in use)
lang_demo.py  the evidence for the language: lang_output.md
```

## The world language

Jono asked on 2026-10-05 what a language for worlds would look like if it dropped programming's brackets and
read well to people and machines alike, then asked to decompose the parts using it ("Sacrificing more lines for
way more understanding is exactly the kind of tradeoff we can start moving towards"). The first form (commit
abd792b) parsed into the Python parts above. This form has no parts in Python at all: every part is written in
`library.world`, in the same language as the worlds, down to primitives.

```
part catapult                                   catapult
  needs  pivot height                             is a          catapult
  needs  arm length                               pivot height  40 cm
  ...                                             arm length    1 m
  stand                                           ...
    is a  box 16 by 24 by pivot height − 6 cm
    on    floor                                 ball
  arm                                             is a   sphere 6 cm radius, 150 g
    is a      box arm length by 6 by 4 cm, ...    moves  freely
    its far end at pivot, level with pivot        sits   in catapult
    turns on  catapult hinge, about y, at pivot
    swings    swings                            expect
  scoop base                                      ball comes to rest in bucket
    is a         box 16 by 16 by 1 cm, 20 g
    on           arm, at arm's near end
    attached to  arm
```

- **All seven briefs, rebuilt on the library, pass their 1d tests**, and all 11 `expect` lines hold
  (`lang_output.md`). The geometry is the same as the Python parts' to the millimetre. The one difference is
  that the catapult's ball now starts touching the scoop instead of 0.5 mm into it.
- **Eight primitives, eight parts.** Primitives are box, cube, sphere, rod, plank, post, ring and point. The
  library holds open box, ramp, door, catapult, pendulum and hoop, plus table and raised bucket, in 182 lines.
  The seven worlds take 128 lines without `expect`, against 86 in the first form and 229 of hand-written XML.
- **One rule for `sits in`.** `sits in X` puts a thing on top of X's base, centred over it, by reading X's
  pieces for one called `base` (or ending in ` base`). The same line seats a ball in the catapult's scoop, a
  bucket, or a bucket on a table. No part knows how to seat anything; the Python `seat()` methods are gone.
- **Positions are relations, one direction at a time.** `on`, `in`, `under`, `raised`, `40 cm up`, `2 m along`,
  `1 m beyond X` (also behind, above, below, left of, right of), `at X's near end` (flush inside), `8 cm outside
  X's left side` (flush outside), `centred on X's far end`, `level with X`, `its far end at X`, and `its rim 4 m
  beyond ball` for one piece of a part. `on` a sloping plank rests on its face, `12 cm from the top`. A
  direction set twice is a problem, TWO PLACES FOR ONE DIRECTION.
- **Bodies come last.** A piece `moves freely`, `turns on <joint>, about <axis>, at <point>`, or is `attached
  to` another. Pieces that move together become one MuJoCo body, named after the part when it has one; the
  rest are fixed. `stacked 5 high` and `repeated 10 times, 10 cm apart along` make block1 to block5 and domino1
  to domino10.
- **New parts need no Python.** `table` is a box and four posts. `raised bucket` is a table and an open box
  with one relation between them (`on table`). The 1d catapult, unchanged, throws into it (`raised.world`).
- **Problems point at the line that caused them.** A bad value passed into a part is reported at the world
  line where it was written, not inside the library: `from 0° to 2.1` stops with ANGLE WITHOUT A UNIT at the
  door's `swings` line. A slip inside the library is reported at its library line. New problems include `sphere
  6 cm` (SAY WHAT IT MEASURES: radius or across), NOTHING TO SIT IN, a need left out, and a misspelt need
  ("did you mean `pivot height`?").
- **Building is cheap.** Parsing and compiling a world takes about 6 ms; running it for 6 s of simulated time
  takes about 500 ms. More lines cost nothing that matters.

Decisions taken alone:

- **Directions.** Along is x, so beyond and ahead of are +x, and a thing's near end faces back along x. To the
  left is y, and up is z.
- **Naming.** A geom is named by its path (`catapult_scoop_base`). One convention entry, `hoop_rim_` to
  `rim_`, keeps the 1d tests' own name for the rim; it is in Python, outside the language.
- **Needs.**
  - Needs are written into a part by name: whole words, longest first, one pass.
  - A need may not share a name with a piece (NAME USED TWICE).
  - `else` gives a default, and `else nothing` drops the line.
- **Spheres.** A sphere must say `radius` or `across`.
- **Open boxes.** An open box's walls are centred on its base's edges, as in the 1d fixtures. The cup with a
  low near wall is the same part with `near wall height 2.5 cm`.

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
