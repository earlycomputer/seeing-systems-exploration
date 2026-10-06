**What happens in the run:** Ball1 is launched at 1.4 m/s and hits ball2 at 0.16 s. The collision is lossy: ball1 hops, and ball2 leaves at only about 0.67 m/s. Ball2 hits ball3 at 0.50 s, and ball3 leaves at only about 0.43 m/s. The floor's rolling resistance then slows ball3 steadily. It reaches the cup's 8 mm front lip at 1.70 s barely moving, fails to climb it, and comes to rest at x ≈ 0.81–0.83 m, outside the cup. Ball1 and ball2 stop well short of the cup.

**Fix:** The chain passes on only about a third of the launch speed to ball3, so I'm launching ball1 at 2.8 m/s with a matching 70 rad/s spin. Ball3 should then reach the lip at about 0.9 m/s, well above the roughly 0.4 m/s needed to climb 8 mm. I'm keeping the floor's rolling resistance, so the slower ball1 and ball2 should still stop before the cup.

```json
{"what_happens": "ball1 rolls into ball2 and ball2 into ball3, but each collision loses much of the speed; ball3 leaves at only 0.43 m/s, slows on the floor, nudges the cup's front lip at 1.7 s and stops outside the cup at x≈0.81 m.", "works": false, "problem": "ball3 arrives too slowly to climb the cup's 8 mm lip and comes to rest outside the cup."}
```

```world
world  three balls and a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ball1
  is a      sphere 4 cm radius, 170 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    orange
  moves     freely
  rests     on floor
  launched  2.8 m/s along
  spins     70 rad/s about y

ball2
  is a      sphere 4 cm radius, 170 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    white
  moves     freely
  rests     on floor, 30 cm beyond ball1

ball3
  is a      sphere 4 cm radius, 170 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    grey
  moves     freely
  rests     on floor, 30 cm beyond ball2

-- an open box with a low front lip the rolling ball can climb;
-- high rolling resistance inside stops the ball before it reaches the far wall
cup
  is an             open box
  length            40 cm
  width             30 cm
  walls             10 cm
  base thickness    3 mm
  near wall height  8 mm
  friction          0.8, spinning 0.005, rolling 0.015
  bounce            dead
  colour            wood
  its base 1.06 m beyond ball1

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

---
thinking (summarized):

The run failed: ball3 stalled at the lip, decelerating much faster than predicted — about 0.24 m/s² based on the observed slowdown. The collision transfer was also off: ball1 dropped to 0.22 m/s and ball2 only picked up 0.67 m/s, far less than the ~1.4 m/s expected, suggesting significant energy loss.

Tracing the ratios, ball2/ball1 comes out to roughly 0.49 and ball3/ball2 to about 0.7, so ball3 ends up near 0.34 times v0 — way too slow to clear the lip with the friction involved. To fix this I'm considering raising v0 to around 3.5 m/s, lowering the lip height, or reducing floor rolling friction. I'm also puzzled by the vertical hop after collision — ball1 briefly left the floor, which points to some bounciness in the contact model that might need adjusting.

Testing with floor and ball rolling friction cut to 0.0005 and v0 at 2.5 m/s, ball3 reaches about 0.85 m/s while the followers trail at roughly 0.4 m/s, landing just near the lip threshold at the cup — so I'm weighing whether to keep friction low overall or instead bump floor friction back up for the followers while giving ball3 extra initial speed, since its gap to the lip is only 0.2 m.

With v0 raised to 2.8 and floor friction at 0.002, ball3 arrives at the lip around 0.9 m/s, comfortably clearing the 0.39 m/s threshold even with rebound loss. Checking the followers: ball1 trails at roughly 0.44 m/s and could travel far enough to bump into ball2, transferring some speed onward — so I'm tracing through how that chain collision plays out near ball2's resting position.

Inside the cup, ball3 decelerates quickly under the cup's drag coefficient and comes to rest well before the far wall, so the geometry works even with some margin for error. I'm settling on v0=2.8 m/s with spin 70 rad/s, and adjusting the cup's placement so ball3 starts only about 16 cm from the lip, which should keep everything within bounds.

