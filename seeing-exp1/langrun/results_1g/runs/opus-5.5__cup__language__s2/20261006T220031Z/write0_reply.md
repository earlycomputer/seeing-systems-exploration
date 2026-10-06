The ball starts near the top of a fixed ramp and rolls down. It leaves the low end in a short arc and lands in an open box cup set just past the ramp's foot. The ball has dead bounces and some rolling friction, so it settles inside the cup well within the 6 s run.

Rough numbers I used to size the cup, not yet confirmed by a run:
- **Leaving the ramp:** the ball rolls down about 22 cm of height and leaves the ramp end at roughly 1.7 m/s along.
- **Clearing the near wall:** it passes the cup's 15 cm near wall with its centre about 26 cm up, so it clears comfortably.
- **Landing:** it falls about 25 cm and lands near 1.32 m along. That is inside the cup, which spans 1.1–1.5 m along.

```world
world  ball rolls down a ramp into a cup

floor
  friction  0.8, spinning 0.005, rolling 0.002

ramp top
  is a  point
  at    0 m along, 50 cm up

ramp foot
  is a  point
  at    1 m along, 25 cm up

ramp
  is a       ramp
  high end   ramp top
  low end    ramp foot
  width      20 cm
  thickness  4 cm
  friction   0.9, spinning 0.005, rolling 0.002
  colour     wood

cup
  is an      open box
  length     40 cm
  width      30 cm
  walls      15 cm
  friction   0.9, spinning 0.01, rolling 0.004
  bounce     dead
  colour     grey
  stands     on floor, 1.3 m along

ball
  is a      sphere 3 cm radius, 60 g
  rolls
  bounce    dead
  friction  0.9, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on ramp.deck, 10 cm from the top

expect
  ball touches ramp
  ball comes to rest in cup
```

---
thinking (summarized):

I'm thinking through the physical setup: maybe instead of a ball rolling over a wall into the cup, it's better to have the ramp end positioned directly above the cup so the ball simply drops off the edge into it, avoiding the issue of bouncing back out over a low wall due to momentum.

I'm working out the geometry — ramp height, ball radius, and projectile distance needed so the ball lands inside the cup rather than overshooting, and figuring out how to define the ramp's top and bottom points using coordinates like "along" and "up" measurements.

Working through the energy and velocity at the bottom of the slope using rotational dynamics, then tracking the ball's trajectory as it leaves the deck's edge and falls toward the cup, solving for fall time using the vertical velocity component and gravity.

Checking the horizontal travel confirms the ball clears the near wall of the cup with margin to spare, lands inside near the center, and likely settles after bouncing given low restitution — though with rolling friction so small, I'm considering whether it might roll back and forth before stopping.

After the dead bounce off the far wall, the ball keeps a bit of forward spin but rolling friction around 0.004 should decelerate it roughly 0.9 m/s², enough to settle within a couple seconds. That timing works, so I'll place the cup's near wall around 1.1 m with the ramp deck ending near 1.0 m.

For the cup, I'm sizing it as an open box 40 cm long, 30 cm wide, with 15 cm walls, positioned about 1.3 m along the floor — simplest to just state it stands on the floor at that distance, similar to how the raised bucket example handles placement. For the ball, I'll spec a 3 cm radius sphere with a mass around 50-60 g, and I'm double-checking the ramp's leg position at the top matches up with the deck geometry.

The plank should extend cleanly between the two reference points, and I'm expecting the overall sequence to work out as: ball touches ramp, rolls down, and settles in the cup, with friction at the cup doing the final resting.

