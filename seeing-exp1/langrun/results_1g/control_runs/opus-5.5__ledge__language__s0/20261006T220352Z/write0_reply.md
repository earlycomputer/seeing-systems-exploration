The table top spans x = −0.6 m to 0.6 m with its top at 75 cm, so its far edge is at x = 0.6 m. The bucket is centred 60 cm beyond that edge, at x = 1.2 m.

The ball starts 30 cm from the edge and rolls at 1.55 m/s. It is given a matching spin (v/r ≈ 51.7 rad/s) so it rolls from the start instead of skidding, and rolling friction is kept small so it doesn't slow down.

Dropping 73 cm to the bucket floor takes about 0.386 s. In that time it travels about 0.598 m beyond the edge, which lands it at the bucket's centre. When it passes over the near wall, its bottom is about 10 cm above the 25 cm wall top.

```world
world  ball off a table into a bucket

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

table
  is a      table
  surface   120 by 60 cm
  height    75 cm
  friction  0.8, spinning 0.001, rolling 0.0001
  colour    wood

-- the table's far edge is at 0.6 m along; the bucket's centre is 60 cm beyond it
bucket
  is an     open box
  length    40 cm
  width     40 cm
  walls     25 cm
  colour    grey
  stands    on floor, 1.2 m along

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  friction  0.8, spinning 0.001, rolling 0.0001
  colour    orange
  moves     freely
  rests     on table.top, 30 cm along
  launched  1.55 m/s along
  spins     51.7 rad/s about y

expect
  ball touches table
  ball comes to rest in bucket
```

---
thinking (summarized):

I'm sketching out a physical scene: a table with a ball that rolls off the edge and falls into a bucket positioned 60 cm beyond the table, working out dimensions like the table surface size and thickness to set up the layout.

The trickier part is figuring out how to position the bucket relative to the table's edge, since the world description seems to only support defining positions by named reference points like centers rather than edges directly — so I'm thinking about how to express "60 cm beyond the table edge" using the centers of both objects.

I'm computing the ball's fall time and required velocity: with a 3 cm radius ball needing to clear a 25 cm bucket wall and land near the base center, I get roughly 0.32 s to reach rim height and 0.39 s to reach the base, giving a target speed around 1.55 m/s and a horizontal clearance of about 0.5 m past the bucket's near edge.

The ball hits the far wall but at low speed and height so it won't escape, and the vertical drop gives it a modest downward velocity that typical contact damping handles fine. At the edge, the ball's horizontal speed is fast enough that it leaves the table cleanly rather than pivoting on the lip, and I'm now checking how rolling friction on the table surface would gradually decelerate it beforehand.

Rolling friction on the table could slow the ball noticeably over a one-meter path, so I'm planning to keep rolling friction very low or position the launch close to the edge to avoid that energy loss, and I need to make sure the table and ball friction values I set don't compound through MuJoCo's default contact combination.

I also want the ball to roll rather than slide from the start, so instead of giving it pure linear velocity, I should add matching angular velocity about the y-axis (ω = v/r) so the contact point has zero relative slip — otherwise sliding friction would decelerate it to 5/7 of its initial speed before true rolling. With v = 1.55 and r = 0.03, that gives ω ≈ 51.7 rad/s, and I'll place the ball near the far end of the table, roughly 30 cm from the edge, to set up the launch.

I'm checking that rolling friction (μr ≈ 0.0001) gives negligible deceleration over the short 0.2 s travel time, so the ball's speed stays essentially constant. For positioning, I need to reference the ball resting on the table's top surface at that 30 cm mark, accounting for the table height plus the box thickness so the ball's center sits correctly at table-top height plus its radius.

Now I'm working out the drop: ball center starts at 0.78 m and needs to land with its center at 0.05 m above the floor (accounting for the base thickness), giving a fall distance of 0.73 m and a fall time of about 0.386 s. Setting the horizontal distance from the table edge to the target landing spot of 1.2 m, I solve for the launch speed, landing on roughly 1.55 m/s with a spin of about 51.7 rad/s, which lands very close to the target at 1.198 m. I'm also checking the bucket's dimensions and wall height to make sure the ball clears the near wall as it passes over on its way to landing inside.

Time to write up the final scene configuration now.

