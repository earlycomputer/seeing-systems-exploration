**What happened in the run.** `ball1` hit `ball2` at 0.21 s and `ball2` hit `ball3` at 0.72 s, so both handoffs worked. Each collision lost about half the speed: 2 m/s became about 1 m/s for `ball2`, then 0.33 m/s for `ball3`. Rolling friction of 0.002 then slowed `ball3` at roughly 0.2 m/s². It stopped at x = 1.27 m, about 19 cm short of the cup's lip, and never touched the cup. The brief's last step, the third ball rolling into the cup, does not happen.

**Changes in the corrected world.**
- Rolling friction on the balls and floor is cut to 0.0003.
- The balls are spaced 25 cm apart instead of 50 cm.
- `ball1` is launched at 4 m/s with a matching rolling spin.
- The balls are slightly larger (5 cm radius).
- The cup sits closer, and its lip and base are lowered to 3 mm so `ball3` can roll over them.
- The cup keeps a high rolling friction so `ball3` stops inside it.

```json
{"what_happens": "ball1 rolls into ball2 at 0.21 s and ball2 into ball3 at 0.72 s, but each collision halves the speed and the strong rolling friction stops ball3 at x = 1.27 m, about 19 cm short of the cup, which it never touches.", "works": false, "problem": "ball3 is left too slow and the rolling friction too high for it to reach the cup, so it never rolls in."}
```

```world
world  three balls into a cup

floor
  size      6 m
  friction  0.8, spinning 0.002, rolling 0.0003

ball1
  is a      sphere 5 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.002, rolling 0.0003
  colour    orange
  moves     freely
  rests     on floor, 0 m along, 0 m to the left
  launched  4 m/s along
  spins     80 rad/s about y

ball2
  is a      sphere 5 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.002, rolling 0.0003
  colour    white
  moves     freely
  rests     on floor, 25 cm beyond ball1, 0 m to the left

ball3
  is a      sphere 5 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.002, rolling 0.0003
  colour    grey
  moves     freely
  rests     on floor, 25 cm beyond ball2, 0 m to the left

cup
  is an              open box
  length             30 cm
  width              30 cm
  walls              12 cm
  wall thickness     1 cm
  base thickness     3 mm
  near wall height   3 mm
  bounce             dead
  friction           0.9, spinning 0.02, rolling 0.02
  colour             wood
  on                 floor, 40 cm beyond ball3, 0 m to the left

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 touches cup
  ball3 comes to rest in cup
```

---
thinking (summarized):

I'm noticing the energy loss is severe across collisions—ball1 at 2 m/s drops to 1.04, then 0.33 m/s—and ball3's deceleration from there to zero seems too fast for a realistic rolling friction coefficient, suggesting MuJoCo's friction model is amplifying the effect more than expected.

I should cut rolling friction down to around 0.0002, shrink the spacing between balls to about 20 cm, move the cup closer, and boost launch speed to 3-4 m/s to compensate. With transfer fraction around 0.5 per hit, ball3 should still arrive with enough speed to climb the cup's lip—though I'm now weighing whether to lower the lip height or increase ball radius to 5 cm instead, since a bigger ball reduces the relative height of that 5mm climb.

