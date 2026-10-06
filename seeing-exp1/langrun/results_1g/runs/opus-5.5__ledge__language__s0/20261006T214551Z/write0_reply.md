The ball starts 20 cm from the table's far edge. It is launched at 1.6 m/s with matching backspin-free rolling spin (ω = v/r ≈ 53 rad/s about y), so it rolls cleanly rather than skidding.

**Layout**
- The table top is 75 cm high and spans x = −40…40 cm, so its edge is at x = 40 cm.
- The bucket is a 50 cm open box centred at x = 1 m, which is 60 cm beyond the edge. Its walls are 20 cm high.

**Expected flight** (worked by hand, not from a run)
- After leaving the edge, the ball's centre falls about 73 cm to the bucket base. That takes about 0.39 s, so it should land about 60 cm out, near the bucket's centre.
- It should clear the near wall (35 cm out) with room to spare and land well short of the far wall (85 cm out).

**Settling**
- The bucket has dead contacts and high rolling friction, so the ball should settle quickly.

```world
world  ball rolls off a table into a bucket

floor
  friction  0.8, spinning 0.005, rolling 0.002

table
  is a      table
  surface   80 by 60 cm
  height    75 cm
  friction  0.8, spinning 0.001, rolling 0.0005
  colour    wood

-- the table's far edge is at 40 cm along; the bucket's centre is 60 cm beyond it
bucket
  is an     open box
  length    50 cm
  width     50 cm
  walls     20 cm
  friction  0.9, spinning 0.01, rolling 0.01
  bounce    dead
  colour    grey
  on floor, 1 m along

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.005, rolling 0.001
  colour    orange
  moves     freely
  on table, 20 cm along
  launched  1.6 m/s along
  spins     53 rad/s about y

expect
  ball touches table
  ball touches bucket
  ball comes to rest in bucket
```

---
thinking (summarized):

I'm working out the projectile physics: the ball leaves the table edge at height h+r with launch speed v, falls to the bucket, and needs to land with its center accounting for the bucket base thickness and radius so it lands centered 60 cm beyond the edge.

With a 75 cm table, 3 cm ball radius, and a 40x40 bucket with 20 cm walls positioned 40–80 cm from the edge, I'm checking the trajectory clears the near wall and stays inside the far wall — computing drop times and required launch speeds for both constraints, finding v≈1.55 m/s hits the bucket center with good margin while clearing the walls safely. I still need to account for rolling friction slowing the ball as it travels across the table before launch.

To get realistic rolling rather than sliding, I should give the ball spin consistent with rolling motion (ω_y = v/r) rather than pure linear velocity, since a sliding sphere converts to rolling and loses speed in the process. Starting the ball 20 cm from the table edge with the correct angular velocity about the y-axis should produce a clean roll-off.

For the edge transition, I check that v²/r exceeds g so the ball leaves the table surface immediately rather than curving around it, which checks out at this speed. For the bounce in the bucket, I want dead bounces on the ball and walls so it doesn't escape, but I'm thinking through whether rolling friction is enough to make it settle within six seconds of bouncing back and forth in the narrow box, and whether I need to increase that friction value.

I decide to widen the bucket to 50 cm so there's more clearance from the near wall and plenty before the far wall. Then for placement, since parts position themselves relative to the origin by default, I just leave the table at the origin so the top surface spans -40 to 40 cm, putting the table edge at x = 40 cm.

Now for the bucket itself — an open box 50 cm long, 50 cm wide, with 20 cm walls — I need to figure out how to anchor its position at roughly x = 100 cm. I'm unsure whether "on floor, 1 m along" works the same way for a part as it does for whole objects like the raised bucket example, but I'll try writing it that way and see if it parses correctly.

The table legs sit near the top's edges and shouldn't interfere with the ball's trajectory since it falls past x = 40 cm, clear of the leg positions. Now for the ball itself, a small sphere around 3 cm radius — I need to figure out how "on table" positioning works for placing it at a specific point along the table's length.

I'm also calculating rolling friction deceleration: using a = (5/7)·μ·g/r, I get about 0.47 m/s², which over a 0.2 m roll reduces velocity squared from 2.56 to roughly 2.37, bringing speed down to about 1.54 m/s — though I still need to confirm which friction coefficient MuJoCo actually applies in contact.

Taking the ball's launch speed of 1.6 m/s and spin of 53 rad/s, I estimate it lands about 0.61 m from the table edge, assuming it leaves the surface right as its center passes the edge corner. For the bucket, I want a dead bounce with higher rolling friction so the ball settles rather than keeps circling, so I'm setting rolling friction to 0.01 there.

I'm also noting the key expectations: the ball should touch the table, then touch and settle in the bucket. For colors, I'll make the ball orange, the table wood-toned, and the bucket grey.

