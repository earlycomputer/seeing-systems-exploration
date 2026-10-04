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
