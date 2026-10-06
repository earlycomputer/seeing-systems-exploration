The ball is launched from the floor 4 m in front of the rim. Its arc peaks about 1 m above the rim, so it comes down through the 3.05 m rim at roughly 55° and clears the rim tube by about 6 cm on each side. It does not touch the bracket or the backboard on the way down. After passing through, it will likely glance off the hoop's pole before landing.

The launch speeds come from simple projectile motion under gravity alone (no air drag):

- **Speeds:** the ball's centre starts at 0.12 m and peaks at 4.0 m, which needs 8.73 m/s up.
- **Timing:** it reaches the rim 1.33 s after launch, so it needs 3.01 m/s along to cover the 4 m.

```world
world  free throw from the floor

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

ball
  is a      sphere 24 cm across, 620 g
  is        hollow, lively
  rolls
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on floor, 0 m along, 0 m to the left
  launched  3.01 m/s along, 8.73 m/s up

hoop
  is a        hoop
  rim height  3.05 m
  its rim 4 m beyond ball, 0 m to the left

expect
  ball drops through hoop
```

---
thinking (summarized):

I'm working out the physical setup: a regulation basketball, roughly 24 cm diameter and 0.62 kg, starting on the floor with its center at about 0.12 m height, needing to arc through a hoop 4 m away at 3.05 m, descending as it passes through.

I'm computing a trajectory with an apex around 4 m, giving vertical and horizontal velocities so the ball reaches x=4 at the right time with a steep descent angle near 55° through the rim center — then checking clearance against the rim's inner diameter and the backboard/bracket geometry to make sure nothing obstructs the shot.

Checking clearance confirms the ball top stays below the bracket, so now I'm computing the actual distance from the ball's center to the far rim point along the trajectory, since what matters is clearance from the ring tube itself rather than just vertical position—tracking how that distance changes as the ball passes through.

I'll skip air resistance to keep it simple. Checking the backboard position relative to the rim, I confirm the ball's trajectory clears the backboard's bottom edge comfortably as it passes through on its way down.

But then I realize the ball keeps falling after the hoop and could actually strike the support pole positioned 120 cm beyond the rim—working out the fall time and landing x-position shows the ball's path intersects the pole's width, which is a problem I need to account for even though the shot otherwise drops through cleanly.

Position it right on the floor, fine as is. The ball itself should be a 24cm sphere weighing 620g, hollow and lively with some bounce, colored orange, with floor friction affecting its roll.

