The ball rests on the floor with its centre 12 cm up. It is launched at 2.865 m/s along and 8.947 m/s up, with no air drag. Its centre then peaks at about 4.2 m and comes down through the rim centre (3.05 m up, 4 m along) about 1.4 s after launch, falling at roughly 59° below horizontal. At that angle the ball's path clears the near and far rim by about 7 cm, worked out by hand rather than from a run. It should also pass under the bracket and backboard before hitting the pole.

```world
world  basketball shot from the floor

floor
  size      12 m
  friction  0.8, spinning 0.005, rolling 0.002

-- regulation size 7 ball: 24 cm across, about 620 g, a hollow shell
ball
  is a      sphere 12 cm radius, 620 g
  is        hollow, lively
  rolls
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on floor
  -- apex of the centre at about 4.2 m, centre crosses 3.05 m at 4 m along after about 1.40 s
  launched  2.865 m/s along, 8.947 m/s up

hoop
  is a        hoop
  rim height  3.05 m
  its rim 4 m beyond ball

expect
  ball drops through hoop
```

---
thinking (summarized):

I'm working out the physical specs of a regulation basketball—about 24 cm diameter, 620 g—and setting up the launch geometry: ball resting on the floor at 4 m horizontal distance from a hoop at 3.05 m height, needing to find a trajectory that threads through the rim center while accounting for air resistance.

I decide to keep the physics purely ballistic, ignoring drag for simplicity, and work through the projectile equations to find an apex height and vertical velocity that gets the ball descending through the rim at the right point.

Solving the timing, I get a total flight of about 1.4 seconds, a horizontal velocity near 2.87 m/s, and a descent angle at the rim around 59°, which should give good clearance through the hoop opening. I'm now double-checking that the trajectory doesn't clip the backboard, since it sits just beyond the rim in the x-direction.

Checking the bracket clearance too — ball top is below 2.9 so it clears the backboard bottom fine, and tracing the geometry near the bracket at x≈4.24 shows the ball's top edge stays just under the bracket's bottom height, so it clears that too, though margins are tight.

Now looking at the ring collision: I need to find where the ball's center crosses the ring plane and compare the ball's horizontal offset there against the inner rim radius, accounting for the sphere's actual cross-sectional width at that height rather than its full diameter.

Checking the far rim point too — same margin, so clearance holds in both directions. The rim's position only needs fixing along the direction axis since it's centered by default. Now I'm setting up the ball itself: a hollow 12cm sphere weighing 620g, resting on the floor at x=0.

Launch velocity components (2.865 m/s along, 8.947 m/s up) should carry the ball past the rim cleanly before any bounce dynamics matter, and the floor size needs to be large enough that the ball's eventual landing point near x~5m still lands within bounds.

