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
