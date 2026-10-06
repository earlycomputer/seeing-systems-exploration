The ball starts on the table already rolling (its spin matches its speed), leaves the edge at 1.55 m/s, clears the near wall and lands in the bucket centred 60 cm beyond the edge. Heavy rolling friction on the bucket stops it there.

- **Layout.** The table top's edge is at x = 0.4 m and its top surface is at 0.75 m. The bucket is centred at x = 1.0 m, with its inner walls running from 0.81 to 1.19 m.
- **The fall.** The ball's centre drops about 0.73 m, which takes about 0.39 s. At 1.55 m/s it covers about 0.6 m in that time, so it lands near the bucket's centre.
- **Clearing the near wall.** By the time the ball has fallen to the near wall's top (20 cm), it is about 0.92 m along. The wall plus the ball's radius only reaches 0.84 m, so it passes over.
- **Not checked by a run.** These figures come from free-fall arithmetic only. Two things are assumed: that the table part's top sits centred at the origin, and that placing the bucket "1 m along" puts its base's centre at x = 1.0 m.

```world
world  roll off the table into a bucket

floor
  friction  0.8, spinning 0.005, rolling 0.002

table
  is a      table
  surface   80 by 60 cm
  height    75 cm
  friction  0.6, spinning 0.001, rolling 0.0001
  colour    wood
  on floor, 0 cm along, 0 cm to the left

bucket
  is an     open box
  length    40 cm
  width     40 cm
  walls     20 cm
  friction  0.8, spinning 0.01, rolling 0.01
  bounce    dead
  colour    grey
  on floor, 1 m along, 0 cm to the left

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.6, spinning 0.001, rolling 0.0001
  colour    orange
  moves     freely
  on table.top, 30 cm behind table.top, 0 cm to the left
  launched  1.55 m/s along
  spins     51.7 rad/s about y

expect
  ball touches table
  ball comes to rest in bucket
```

---
thinking (summarized):

I'm setting up the scene with a table, a ball rolling off its edge, and a bucket positioned 60 cm beyond the table to catch it, figuring out how to size the table surface appropriately.

Now I'm working out the physics: computing table height, ball radius, and fall trajectory to determine the launch velocity needed so the ball lands centered in the bucket, factoring in the drop height and horizontal distance from edge to bucket.

Then I check wall clearance—computing landing coordinates against near/far bucket wall positions to confirm the ball clears both. I also factor in rolling friction decelerating the ball on the table before it leaves the edge, estimating the small but non-negligible deceleration from rolling resistance.

For friction setup, I should set matching ball and table friction values—sliding 0.6, spinning 0.001, rolling 0.0001—so the contact uses consistent coefficients. For launch velocity, I need to decide whether to give the ball initial spin matching rolling motion (ω = v/r about the y-axis) so it rolls immediately without the slip-to-roll transition that would reduce its speed to 5/7 of the launch velocity.

Working through placement: starting the ball around x=-0.3 on a table ending near -0.4 gives roughly 0.7 m to travel before reaching the edge, taking about 0.45 s at 1.55 m/s. Checking the edge-tipping physics confirms v²/(gr) is well above 1, so the ball leaves the table edge cleanly rather than pivoting. Now I'm turning to the bucket geometry—a 40x40 open box with 25 cm walls—and figuring out how to position it correctly on the floor relative to the table.

The table's top is centered at the origin, so placing it "on floor" keeps that centering simple. For the ball sitting on the table, I can describe its offset like "30 cm behind table.top" to capture its position relative to the table surface.

Now I'm checking whether the ball's trajectory actually clears the bucket's near wall. With the bucket centered about 1.0 m from origin and the wall edge around 0.8 m, I need to verify the ball's horizontal position at wall-top height actually exceeds the wall's far edge plus the ball's radius — recalculating, it looks like the ball barely clears by less than 10 cm, so I should double check these numbers more carefully.

Lowering wall height to 20 cm gives better clearance, with the ball landing roughly 1.0 m from the edge inside the bucket, and the far wall around 1.2 m away. After landing, the ball will roll inside at about 1.55 m/s, bounce off the far wall, and continue oscillating — I need to figure out if it settles down within a reasonable time to count as "at rest" in the bucket.

