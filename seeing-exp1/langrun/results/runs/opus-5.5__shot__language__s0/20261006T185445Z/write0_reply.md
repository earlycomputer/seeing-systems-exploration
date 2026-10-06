The ball is a 24 cm, 620 g hollow sphere resting on the floor. It is launched at 3.01 m/s along and 8.73 m/s up, so it peaks near 4.0 m and comes down through the rim centre, 4 m away at 3.05 m, at about 55°. There is no air drag. Worked through by hand, the ball's bottom clears the front of the rim by about 18 cm, and the ball misses the back of the rim and the backboard on the way down.

```world
world  basketball shot

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
  rests     on floor
  launched  3.01 m/s along, 8.73 m/s up

hoop
  is a        hoop
  rim height  3.05 m
  its rim 4 m beyond ball

expect
  ball drops through hoop
```

---
thinking (summarized):

I'm working out the physical setup: a regulation basketball about 24 cm across and 0.62 kg, launched from a height of 0.12 m, with the rim at 3.05 m and 4 m away horizontally, leaving roughly 21.7 cm of clearance through the hoop.

I'll skip air drag to keep things simple, and instead solve for a trajectory where the ball peaks around 4 m high before descending steeply into the rim center at a ~55° entry angle, giving vx≈3.0 m/s and a total flight time near 1.33 s. I still need to check the ball clears the front lip of the rim as it comes down.

Checking position at x=3.77 m, the ball's bottom sits at 3.232 m, safely above the rim height, and as it passes through the hoop plane at x=4 it stays clear of the back rim with about 0.11 m to spare before contact.

I'm now checking whether the ball clears the rim tube as it descends past x=4.1, verifying the distance from the ball center to the back rim's circular cross-section stays above the combined radius at multiple sample points along the trajectory.

Next I'm working out the backboard geometry—its bracket offset, the board's extent above and below the rim—to figure out at what point the ball's trajectory would reach the backboard's front face.

Then I'm checking where the ball lands after falling from its apex, finding it comes down around x=5.35 m, but the support pole is located near 5.1–5.3 m, so the ball's path intersects the pole at about 1.1 m height—meaning it would strike the pole after going through the hoop.

I'm working out placement: setting the ball at the origin resting on the floor, the hoop rim about 4 m along with its standard height of 3.05 m, and the pole base near 5.2–6.2 m, with the floor sized around 12 m to keep everything contained safely.

The ball itself is a 24 cm hollow sphere weighing 620 g, lively and able to roll with friction, moving freely once launched at roughly 3.01 m/s forward and 8.73 m/s upward — close enough that the small rounding differences shouldn't matter for the shot to pass through the hoop.

