The table top is 75 cm high and 80 cm long, so its far edge is at x = 40 cm. The bucket stands on the floor centred 1 m along, which puts its centre 60 cm beyond that edge. The numbers below are hand calculations, not a run.

- **Launch speed.** The ball's centre leaves the edge at 78 cm. To land at the bucket's centre, 5 cm above the floor, it needs 1.55 m/s along. That gives a fall of about 0.39 s and a carry of about 60 cm.
- **Rolling start.** The ball starts spinning at 51.7 rad/s about y (1.55 m/s ÷ 3 cm). It therefore rolls without slipping from the start.
- **Little loss on the table.** The ball and the table both have very low rolling friction. The ball should reach the edge at almost full speed after 30 cm of rolling.
- **Clearing the near wall.** As it passes over the bucket's 20 cm near wall, the ball is still about 44 cm up.
- **Settling.** The bucket has a dead bounce and high rolling friction. That should bring the ball to rest inside it well within the 6 s run.

```world
world  ball rolls off a table into a bucket

floor
  friction  0.8, spinning 0.005, rolling 0.002

-- table top: 80 cm long, centred at x = 0, so its far edge is at x = 40 cm; top surface at 75 cm
table
  is a      table
  surface   80 by 50 cm
  height    75 cm
  friction  0.8, spinning 0.001, rolling 0.0001
  colour    wood

-- bucket centre at x = 1 m: 60 cm beyond the table's far edge
bucket
  is an     open box
  length    30 cm
  width     30 cm
  walls     20 cm
  friction  0.9, spinning 0.02, rolling 0.01
  bounce    dead
  colour    grey
  on floor, 1 m along

-- ball starts 30 cm before the edge, rolling at 1.55 m/s (spin = v / r = 1.55 / 0.03)
ball
  is a      sphere 3 cm radius, 50 g
  rolls
  friction  0.8, spinning 0.001, rolling 0.0001
  colour    orange
  moves     freely
  on table.top, 10 cm along
  launched  1.55 m/s along
  spins     51.7 rad/s about y

expect
  ball touches table
  ball comes to rest in bucket
```

---
thinking (summarized):

I'm working out the physics setup: a table of height 75 cm, a ball of radius 3 cm rolling off the edge, needing to land in a bucket whose center sits 60 cm beyond the table's edge, calculating the trajectory needed to clear the bucket's near wall.

I'm checking the launch speed around 1.6 m/s gets the ball past the near wall and landing near the bucket's center without hitting the far side, then considering how rolling friction will reduce the ball's speed after it leaves the table.

Checking the deceleration math, this rolling friction value would shave off too much speed over the distance, so I should lower the rolling friction coefficients for both ball and table to keep slowdown negligible, maybe 0.0001 each, and keep the start position around 30 cm from the edge. Now I need to figure out exactly when the ball leaves the table relative to its center crossing the edge.

I'm confirming that at the computed speed, the centripetal condition is easily satisfied, so the ball departs cleanly right at the edge without hugging the corner. Now I'm working out the table's dimensions, treating it as a box with surface width by depth and a 3 cm thickness, following the same sizing convention used for the earlier bucket example.

I'm placing the table at the origin for simplicity, with its top surface at 75 cm height, and planning to position the bucket further along at roughly 1 m so the pieces don't overlap. For the open box bucket, I'm now working through its individual wall and base pieces needed to assemble it on the floor at that position.

I'll reference the ball's position as "on table.top, 10 cm along" to be safe about which surface it means. Then I need to recompute the physics with the ball's 3 cm radius — working out the drop height, fall time, and required velocity so the ball clears the table edge and lands properly without hitting anything nearby.

Checking clearance near the far wall: at the relevant x position the ball's height stays above the wall's extent, so it should clear fine. After landing at the bucket's center it will carry residual horizontal velocity toward the far wall, bounce back, and I need to confirm it settles below the 5 cm/s threshold by 6 seconds given low rolling friction and the dead bounce absorbing energy, plus accounting for the ball's spin.

I'm tuning the bucket's rolling friction higher (around 0.8/0.01) so the rolling contact decelerates the ball quickly—roughly 2.3 m/s² deceleration—while keeping the ball and table's own rolling friction very low. Settling on velocity 1.55 m/s and spin ~51.7 rad/s for the 50 g ball, I expect it comes to rest in the bucket, though I should double check whether the open box's friction properties actually apply correctly to the contact.

I'll keep the ball with its default bounce but make the bucket bounce dead, and verify the contact solver mixing doesn't make things too lively. Wall heights at 20 cm and bucket inner width of 30 cm should comfortably fit the 3 cm radius ball centered at y=0.

