The ball is a regulation size 7 basketball (23.9 cm across, 620 g). It is set on the floor with the hoop's rim centred 4 m ahead at 3.05 m. I solved the launch so the ball's centre passes the rim centre while coming down at about 50°: 3.19 m/s along and 8.49 m/s up. It reaches the rim about 1.25 s after launch, at the top of an arc about 3.8 m high. The ball's centre clears both the near and far edges of the rim by about 17.5 cm, against the 12.3 cm needed for the ball and the rim tube. After passing through, it drops under the bracket and backboard.

```world
world  basketball shot from the floor

floor
  size      12 m
  friction  0.8, spinning 0.005, rolling 0.002

ball
  is a      sphere 23.9 cm across, 620 g
  rolls
  is        hollow, lively
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on floor
  launched  3.19 m/s along, 8.49 m/s up

hoop
  is a        hoop
  rim height  3.05 m
  its rim 4 m beyond ball

expect
  ball drops through hoop
```

---
thinking (summarized):

I'm working out the physical setup: a regulation size-7 basketball (about 11.9 cm radius, 620 g) starting at floor level, needing to travel 4 m horizontally and rise to a rim height of 3.05 m, factoring in the rim's 45.72 cm diameter for clearance.

I want the trajectory to drop steeply through the hoop, so the ball's center needs to climb roughly 2.93 m from its resting position to the rim's center height before descending into it.

Checking clearance, the rim's inner opening is only about 0.46 m wide while the ball is 0.24 m across, so a shallow entry angle would clip the rim—I calculate I need at least a 31° descent angle, and I'm targeting something steeper like 50° for a clean swish. Working through the kinematics with horizontal distance of 4 m and vertical rise of 2.93 m, I'm solving for the flight time and launch velocity that satisfy both the entry angle requirement and the position constraints.

Solving numerically, I get a flight time around 1.25 seconds, with horizontal velocity about 3.19 m/s and vertical velocity about 8.49 m/s, putting the peak trajectory height at roughly 3.79 m. Now I'm double-checking the shot doesn't clip the backboard, which sits mounted behind the rim—working out exactly where the ball's horizontal position falls relative to the backboard's near and far edges at the moment it passes through the rim center.

Tracking the ball a bit further, I'm computing where it crosses the backboard's vertical plane and how much it has dropped by then, then comparing the ball's top edge to the backboard's bottom edge height to see whether it actually clears underneath.

I'm checking clearance against the far rim as the ball descends through the hoop — using the trajectory angle to find perpendicular distance from the rim tube's edge, confirming it's safely larger than the ball radius plus tube radius at both the near and far side.

Then I'm checking the bracket mounted past the rim: computing the ball's drop in height as it travels that extra 12-24 cm horizontally, and comparing the ball's top edge to the bracket's bottom surface to see if there's enough clearance underneath it.

After the ball lands and rolls toward the pole base, it doesn't really matter for this check. I'm also reconsidering whether the ring measurement is outer vs center diameter, and whether the 16-segment discretization changes the effective interior radius slightly, but these are minor factors. The 5cm margin at 50° entry angle seems adequate, though I could bump it to 52° for extra safety.

I'm also checking whether MuJoCo's contact solver might introduce a tiny impulse at the start since the ball begins exactly touching the floor with upward velocity — likely negligible, but I should use the correct radius value, around 11.95 cm for a basketball with 23.9 cm diameter.

Recomputing the trajectory more precisely: with vx around 3.19 m/s and vz around 8.49 m/s, the ball reaches z ≈ 3.05 m at x = 4 m, which checks out consistently across both calculation passes.

I should verify the ball doesn't clip the rim near its peak — the peak occurs around x=2.76 m, well before the hoop, so it's already descending when it reaches the rim area at x≈3.77-4 m. I also need to confirm clearance under the backboard: tracking forward to x≈4.262 m, the center height drops to about 2.705 m while the backboard bottom sits near 2.90 m, so the ball's top edge at 2.825 m stays under it — looks like it clears.

I also check the distance from the backboard corner at (4.381, 2.90) to the ball center, finding it exceeds the ball's radius, confirming the ball passes underneath cleanly. There's also a support pole at x 5.1–5.3 which the ball will eventually strike and bounce off during the 6-second simulation. I should make sure the hoop object is properly named with its rim component, give the ball proper physical properties (hollow, orange, lively bounce, rolling), and then write out the full world definition.

