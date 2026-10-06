The ball starts resting on the floor and is launched at 3.18 m/s along and 8.50 m/s up, with no air drag. It peaks near 3.8 m and comes down through the rim centre at 3.05 m, 4 m away, about 1.26 s after launch. It is falling steeply there (about 50°), so the 24 cm ball fits through the 45.72 cm rim with room to spare.

```world
world  basketball shot from the floor

floor
  size      12 m
  friction  0.8, spinning 0.005, rolling 0.002

ball
  is a      sphere 24 cm across, 620 g
  is        hollow, lively
  rolls
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on floor, 0 m along
  launched  3.18 m/s along, 8.50 m/s up

hoop
  is a        hoop
  rim height  3.05 m
  its rim 4 m beyond ball

expect
  ball drops through hoop
```

---
thinking (summarized):

I'm working out the physical specs of a regulation basketball and hoop, then setting up the launch trajectory needed for the ball to arc from the floor through the rim 4 meters away at a height of 3.05 meters.

I pick an apex height around 3.8 m, calculate the vertical and horizontal velocities needed to reach it and descend steeply into the rim at the right angle, then trace what happens to the ball's path afterward as it continues past the rim toward the floor and backboard area.

Checking the backboard clearance, the ball barely squeezes under its bottom edge by a couple centimeters at that point in the trajectory, so now I need to check whether it also clears the support pole positioned further out.

Then there's the rim tube itself—the actual clear opening shrinks because the ball is descending at an angle rather than passing straight down, so the effective opening along the direction of travel is reduced by the sine of the descent angle, cutting the 44 cm diameter down to around 33 cm.

I'll skip air resistance to keep things simple and aim the trajectory so the ball's center passes through the rim's center. Setting the ball's starting height at its radius above the floor and the hoop four meters ahead with rim height 3.05 m, I work out a launch velocity around 3.18 m/s horizontal and 8.5 m/s vertical, then solve for the time at which the ball reaches the rim height to verify the trajectory.

