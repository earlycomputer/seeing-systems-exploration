The ball is a 24 cm, 600 g hollow, lively sphere resting on the floor. It is launched at 2.865 m/s along and 8.947 m/s up. Without air drag, that peaks at about 4.2 m and its centre passes the rim plane 4 m away, descending at about 59°.

**Clearances, worked by hand on the drag-free path (not yet confirmed in a run):**
- **Front of the rim:** over the front edge of the rim's opening, the ball's bottom is about 22 cm above the rim top.
- **Ring:** where it crosses the ring, the path passes about 19.6 cm from both the front and back tube, against the 12.4 cm needed.
- **Bracket:** it misses the bracket by about 7 cm.

**After it scores:** the ball hits the hoop's pole at about 0.85 m high and bounces back. I didn't trace where it ends up. It is not expected to come to rest, but that isn't checked.

```world
world  basketball shot from the floor

floor
  size      10 m
  friction  0.8, spinning 0.005, rolling 0.002

ball
  is a      sphere 24 cm across, 600 g
  rolls
  is        hollow, lively
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on floor, 1 m along
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

I'm working out the physical setup: a regulation size-7 basketball (about 24 cm diameter, 600 g) starting at rest on the floor with its center 12 cm up, needing to travel 4 m horizontally and rise to a rim centered at 3.05 m.

Checking clearance through the hoop, the rim's inner radius gives roughly 10.5 cm of margin around the ball, so the trajectory needs to be steep enough on the way down to avoid the rim or backboard — I'm noting the backboard sits about 15 cm beyond the rim's far edge and extends well above it, so the ball's path from the near side should clear it easily. I'm deciding to ignore air drag for a clean ballistic calculation, and now I'm setting up the parabolic trajectory equations to find the right launch angle and speed so the ball descends through the rim center at the correct steepness.

Picking an apex height around 4.2 m, I'm computing the vertical velocity needed to rise from the starting height to that apex, then working out the fall time from the apex down to rim height to get the full flight timing.

From there I'm computing horizontal velocity, the resulting descent angle at the rim (around 59°, nice and steep), and double-checking clearance at the front edge of the rim to confirm the ball's bottom stays above the rim top as it passes through.

Checking the back rim similarly gives the same clearance by symmetry, so curvature effects are negligible. Now I'm tracking the ball after it passes through the rim, falling from z=3.05 to the floor at z=0.12 while still moving forward at vx=2.865, solving for the fall time to see where it lands relative to the pole base.

Actually recalculating, the ball's landing point at x≈5.226 would put it right into the pole itself, which spans roughly 5.1 to 5.3 — so I need to check if the ball strikes the pole before reaching the floor, checking the height at which x=4.98 (ball edge touching pole) and finding it hits around 0.85m up.

I should also check the support bracket/arm geometry near the rim: it sits slightly beyond and below the rim plane, so I need to verify whether the ball's trajectory just after passing through the hoop clears the bracket's height and position, computing the ball's top edge versus the bracket's bottom edge at the relevant x position.

Then I consider whether the ball could strike the pole at a lower point and bounce back into the hoop area from underneath, tracking the reflected velocity components after that collision.

I decide this is unlikely to add up to a clean drop-through, so I keep the hoop and pole geometry fixed as-is and move to setting up the ball's starting position—placing it on the floor a meter along, with the rim positioned some distance beyond it to establish the horizontal offset I need.

I'm sizing the floor generously to accommodate the hoop assembly and pole base, then turning to the ball's physical properties—its diameter, mass, hollow construction, friction, and liveliness—before recomputing the precise launch velocities along and upward to ensure it clears the rim correctly.

