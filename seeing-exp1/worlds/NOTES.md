# Notes

## Parking lot

- **A person in the loop.** 1c's rounds are the agent alone. The tool Jono described has a person looking at
  the same readback and editing the same text; experiment 5 (edits survive) is the nearest test of that.
- **A brief that needs breaking, bending or liquid.** MuJoCo 3.14 has cloth-like deformables but no fracture
  or fluids, so no 1c brief asks for them.
- **Tests as the brief's other half.** Writing each test made the briefs sharper (what does "stays shut"
  mean? within 2° for the last second). A tool could ask the person to confirm a test before building.

## Building it

- The hand-written catapult works only for a spring between about 2.5 and 3.5 N·m/rad: at 2 it falls
  short, at 4 it overshoots and rolls away. Like the free throw in 1b, a working world is a narrow target.
- A gentle push slides the whole stack along the floor without toppling it, and the stack test fails it:
  "topples" needs the push to tip the stack, not move it.
- The basketball in Opus's 1b scene keeps rolling after it lands, so its run never comes to rest and the
  residue spreads over all 6 s.

## What the 40 worlds showed (2026-10-04)

- **The first write usually works.** 28 of 40 worlds passed as first written; the shot and the cup 16 of 16.
  A one-sentence brief to a working world is mostly not the hard part with these briefs.
- **The picture's two fixes were both absences.** A door whose residue had no swinging copies, and a stack
  that stayed up. Text cannot report that something did not happen; a picture of the run can.
- **The degrees trap is real and sticky.** Opus wrote hinge ranges in radians in 3 of 4 doors. With the
  picture it caught it once from the missing swing and once called the shut door right.
- **Text only means no second look.** Asked to check again with no readback, models almost always said the
  world works (6 of 6 final failures claimed working) and tried a fix once in 6.
- **"3 m away" was ambiguous.** Models placed the bucket from the catapult, the test measures from the ball.
  Next time, write the measurement into the brief or confirm it with the person, as the parking lot says.
- **Catapults keep rolling.** Three catapult worlds failed "ball at rest at the end": the ball lands in or
  near the bucket and is still moving after 6 s.
- **Cost came in at a quarter of the estimate** because most worlds stopped after one round: $8.30, about
  $0.34 a world for Opus and $0.08 for GPT-6.1 Sol.

## Found while building the viewer (2026-10-04)

- **Every door picture covered only the first 0.6 s.** `draw.active_until` decides when a run has come to rest
  from the speed of each moving body's origin. A door's origin is on its hinge, so it never counts as moving,
  and the residue falls back to 0 to 0.6 s. All 5 door pictures were drawn that way (`round*_view.json`); every
  other brief's ran 1.2 to 6.0 s. The tests never read the picture, so no verdict changes. But a door picture
  could not show the door shutting and staying shut, and Opus said so ("the picture only covers the first
  0.6 s"). 1c is left as it ran; 1d fixes it before its first run, since a pendulum turns about its origin too.
- **The viewer re-checks every verdict.** `viewer.py` runs each of the 47 saved files again through
  `tests.judge` and stops if any check comes out different. All 47 matched.
- **Watching the worlds run shows what the tests leave out.** All four of GPT-6.1 Sol's shots go through and then
  roll on, ending 8 to 11 m past the hoop at 6 s; Opus's end 0.2 to 2.2 m past it. "Drops through a hoop" allows
  both. A failing catapult ball can be seen still rolling at 6 s, in or beside the bucket.

