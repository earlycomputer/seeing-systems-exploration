In the run, `ball1` rolls into `ball2` at 0.15 s and `ball2` rolls into `ball3` at 0.33 s. Each collision loses about half the speed, so `ball3` sets off at only 0.36 m/s. By the time it reaches the cup's 5 mm lip (1.09 s) it is down to about 0.31 m/s. That is too slow to climb the lip: it bounces back and stops on the floor just outside the cup at x = 0.76 m. `ball1` and `ball2` stop behind it. The chain of hits works, but `ball3` never gets into the cup.

To fix it, `ball1` is launched much faster (4 m/s, still already rolling), so `ball3` should reach the lip at about 0.9 m/s. The lip and base are lowered to 3 mm. The cup is lengthened to 50 cm so its high rolling friction stops the ball well inside.

```json
{"what_happens": "ball1 rolls into ball2 (0.15 s), and ball2 rolls into ball3 (0.33 s), but each hit loses about half the speed. ball3 reaches the cup's 5 mm near-wall lip at about 0.31 m/s, bounces back off it, and comes to rest on the floor just outside the cup at x = 0.76 m. ball1 and ball2 stop behind it.", "works": false, "problem": "ball3 arrives too slowly to climb the cup's lip, bounces off it and stops outside the cup."}
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
  rests     on floor
  launched  4 m/s along
  spins     100 rad/s about y

ball2
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.001
  colour    white
  moves     freely
  rests     on floor, 30 cm beyond ball1

ball3
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.001
  colour    grey
  moves     freely
  rests     on floor, 20 cm beyond ball2

-- a shallow cup whose near wall is a flush 3 mm lip, so a fast-rolling ball can enter;
-- its high rolling friction stops the ball inside
cup
  is an             open box
  length            50 cm
  width             30 cm
  walls             12 cm
  wall thickness    2 cm
  base thickness    3 mm
  near wall height  3 mm
  friction          1.0, spinning 0.01, rolling 0.01
  bounce            dead
  colour            wood
  on floor, its base 54 cm beyond ball3

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

---
thinking (summarized):

That attempt failed too—ball3 only reached 0.36 m/s off the lip, far too slow, and the collision speeds dropped sharply across the board (ball1 from 1.5 down to 0.38 or even 0.15, ball2 to 0.65). The collisions are too lossy even with the bounciness settings, so I need to rethink how energy transfers between the balls.

The real issue is the cup's lip: a 5mm step at the near wall, and climbing it needs around 0.37 m/s or more. A ramp or plank to smooth the transition seems messy since any plank thickness just creates its own step problem at the low end. The simpler fix is boosting the launch speed substantially — maybe 3.5 m/s instead of 1.5 — since that should scale ball3's post-collision speed up to roughly 0.85 m/s, enough to clear the lip.

Thinning the base and lip to 3mm each should also help reduce the step height. I'm also puzzled by the large energy losses between collisions — each ball seems to lose about half its speed to the next, which feels too lossy for near-elastic contact; could be related to ball1 hopping vertically on impact rather than transferring momentum cleanly.

I'll bump the launch speed to 4 m/s with 100 rad/s spin, but that raises a concern: ball3 might not have enough room to stop before hitting the far wall of the cup. Checking the geometry, the clearance is tight, so I should extend the cup length to 50 cm to give it more room, while keeping the follow-up balls' speeds low enough to settle safely inside.

