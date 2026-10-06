The ball starts 30 cm from the table's far edge. It is launched at 1.55 m/s with the matching spin, so it rolls rather than skids. From a 78 cm centre height, that speed carries it about 60 cm beyond the edge as it reaches the bucket's base. The bucket has a dead, grippy surface so the ball should settle there.

```world
world  ball rolls off a table into a bucket

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

-- table top spans x from -60 cm to +60 cm, so its far edge is at x = 60 cm; top surface at 75 cm
table
  is a      table
  surface   120 by 60 cm
  height    75 cm
  friction  0.8, spinning 0.0001, rolling 0.0001
  colour    wood

-- bucket centre 60 cm beyond the table's far edge (120 cm beyond the table's centre)
bucket
  is an     open box
  length    30 cm
  width     30 cm
  walls     25 cm
  friction  1.0, spinning 0.01, rolling 0.01
  bounce    dead
  colour    grey
  stands    on floor, 120 cm beyond table.top

-- rolls at 1.55 m/s with matching spin (v / r = 51.7 rad/s about +y, so no skidding);
-- falls 73 cm (centre from 78 cm to 5 cm) in 0.386 s, travelling 60 cm past the edge
ball
  is a      sphere 3 cm radius, 50 g
  rolls
  friction  0.8, spinning 0.0001, rolling 0.0001
  colour    orange
  moves     freely
  rests     on table.top, 30 cm beyond table.top
  launched  1.55 m/s along
  spins     51.7 rad/s about y

expect
  ball touches table
  ball touches bucket
  ball comes to rest in bucket
```

---
thinking (summarized):

I'm thinking through how to model a table object physically—its dimensions, height, and surface, and how its position should default relative to the origin if not otherwise specified.

I'm then positioning the bucket 60 cm beyond the table's far edge, around 1.2 m from center, and working out the bucket's dimensions as an open box roughly 25 cm tall and 30 cm square. I'm calculating the ball's trajectory—its launch height off the table surface, its fall to the bucket, and where its center needs to land to clear the near wall and settle near the bucket's base.

Solving for v gives about 1.56 m/s, and checking clearance at the near wall and rim confirms the trajectory clears both obstacles with a few centimeters to spare. But I still need to account for rolling friction decelerating the ball across the table before launch, so I'm estimating that deceleration using MuJoCo's rolling friction coefficient.

I should probably reduce the rolling friction coefficient for the ball and table to keep things simple, or just start the ball near the edge. I also need to give the ball initial spin matching rolling-without-slipping (ω = v/r about the appropriate axis), otherwise it'll slide and lose speed to a smaller fraction of its initial velocity before true rolling takes over.

MuJoCo combines friction by max, so both table and ball geoms need low rolling friction set; the floor's slightly higher rolling friction barely matters since deceleration from 0.0001 friction over 30 cm is negligible. I also need to use condim 6 for proper rolling contact, and work out the ball's placement — centre height at table top plus radius, positioned safely on "table.top" at x=0.3 along the surface.

For the bucket, I'm figuring placement at 1.2 m along the floor, open box with 30 cm length and width and 25 cm walls. I'm debating whether to explicitly position the table or leave its default placement, checking that the table's far edge lines up correctly if centred at the origin.

A more robust approach is to position the bucket relative to the table, like "1.2 m beyond table.top," and similarly place the ball at 30 cm beyond that reference so the geometry holds regardless of exact table position. Then I'm working out the ball's trajectory landing near x≈1.2 for a bounce off the bucket's base, aiming for the bucket to absorb the impact while the ball itself bounces.

Thinking through the physics, with a vertical impact speed around 3.8 m/s and horizontal speed near 1.55 m/s, the ball will rattle within the bucket walls before settling given MuJoCo's default soft contacts. I want to tune rolling friction so the bucket has higher rolling friction than the table, ensuring the ball settles inside the bucket by around 6 seconds rather than rolling back and forth indefinitely.

Checking the edge timing, the ball reaches the table edge at about 0.19s given its horizontal speed, and I'm verifying the spin rate (~51.7 rad/s about the y-axis) matches a no-slip launch condition so the ball doesn't skid awkwardly on the table before falling off.

