**What happened.** The first two hand-offs work. `ball1` strikes `ball2` at 0.21 s and `ball2` strikes `ball3` at 0.72 s.

Each collision passes on only about half the speed:
- `ball2` leaves at 1.04 m/s.
- `ball2` loses speed fast while skidding.
- `ball3` gets only 0.33 m/s.

Floor rolling friction (about 0.3 m/s²) then stops `ball3` at x = 1.77 m. That is 19 cm short of the cup's near wall, so it never touches or enters the cup.

**Fixes.**
- Put the balls 30 cm apart, so less speed is lost between collisions.
- Put the cup closer.
- Halve the rolling friction on the floor and balls.
- Launch `ball1` faster, with matching spin.
- Lower the cup's entry step to 3 mm.

```json
{"what_happens": "ball1 rolls into ball2 and ball2 into ball3, but each collision passes on only about half the speed; ball3 leaves at 0.33 m/s, is slowed by rolling friction and stops at x = 1.77 m, 19 cm short of the cup, without touching it.", "works": false, "problem": "Collision losses and rolling friction over the long gaps leave ball3 too slow to reach the cup, which is too far away."}
```

```world
world  three balls into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.001

ball1
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.001
  colour    orange
  moves     freely
  on floor, 0.5 m along
  launched  3.5 m/s along
  spins     87.5 rad/s about y

ball2
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.001
  colour    white
  moves     freely
  on floor, 0.8 m along

ball3
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.001
  colour    grey
  moves     freely
  on floor, 1.1 m along

cup
  is an             open box
  length            30 cm
  width             20 cm
  walls             10 cm
  wall thickness    1 cm
  base thickness    3 mm
  near wall height  3 mm
  friction          1, spinning 0.01, rolling 0.02
  bounce            dead
  colour            wood
  on floor, 1.65 m along

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 touches cup
  ball3 comes to rest in cup
```

---
thinking (summarized):

These collisions are clearly very lossy — ball1 at 2 m/s transfers only 1.04 to ball2 while bouncing back at 0.38, then ball2's speed decays quickly before handing off just 0.33 to ball3. The deceleration rate of ball3, about 0.32 m/s², lines up with my earlier estimate.

Given this lossy energy transfer, I should shrink the gaps between balls to roughly 0.3 m each, lower rolling friction, and raise launch speed to compensate. Estimating forward from a 3 m/s launch with tighter spacing, ball3 should arrive at the cup around 0.4–0.45 m/s, which should be enough to climb the small step.

Checking the numbers: ball1 would travel about 0.63 m, not quite reaching the cup, while ball3 slows to roughly 0.28 m/s—likely still enough to climb a small 5mm step edge, though I should double check the impact energy condition. To be safe, I could thin the step to 3mm or just boost the initial launch speed to around 4 m/s.

With a 3.5 m/s launch and 87.5 rad/s spin, rolling resistance 0.001, and 30cm gaps, ball3 starting near 1.1 should slow to about 0.5 m/s and land around 1.37—roughly a 0.37m gap from the cup. Ball1 retaining more energy could travel 0.86 m, landing near 1.58, which risks colliding with ball2's resting position—so I'll need to adjust spacing further.

