The ball is a size-7 basketball (23.8 cm across, 620 g) resting on the floor, with the rim centre 4 m ahead of it. I left out air drag, so the flight follows plain projectile motion.

**The launch** is 3.01 m/s along and 8.73 m/s up.
- The ball's centre peaks at about 4.0 m, roughly 2.7 m along.
- It reaches rim height (3.05 m) 4 m out, about 1.33 s after launch.
- It is coming down at about 55° when it gets there.

**Clearance**, from hand calculation:
- The ball's surface stays about 6 cm or more clear of the front and back of the rim tube.
- It passes about 4 cm under the rim bracket and about 14 cm under the bottom edge of the backboard.

**After the hoop**, the ball keeps moving forward. It should hit the hoop's pole at about 1.1 m height and bounce around. That happens after it has already passed through the rim.

```world
world  basketball shot from the floor

floor
  size      12 m
  friction  0.8, spinning 0.005, rolling 0.002

ball
  is a      sphere 23.8 cm across, 620 g
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

I'm working out the regulation basketball dimensions—about 24 cm diameter, 620 g mass—and setting up the launch geometry from a floor-level start to a rim 3.05 m high and 4 m away horizontally.

I'm checking clearance against the rim's inner diameter (~45.7 cm) and the backboard/bracket positions, making sure the ball's trajectory through the hoop doesn't clip the backboard or its support. I'll keep the physics deterministic without air drag to simplify the simulation.

Working out the parabolic path: starting the ball's center at floor height (0.119 m), choosing an apex of 4.0 m, and computing vertical/horizontal velocities so the ball descends through the rim plane at a steep ~55° angle—now I'm verifying whether this path actually clears the rim without contact.

Continuing the fall after passing through the hoop, the ball lands roughly 1.35 m beyond the rim, putting it right around the pole structure positioned 1.1 to 1.3 m beyond the rim — so I need to check whether the ball actually collides with that pole.

Working through the trajectory, the ball hits the pole area at about 1.1 m height, but since this occurs after it's already passed through the hoop, the shot still technically counts as going through. I should also verify it clears the backboard and support arm, checking the backboard's position 38 to 41 cm beyond the rim with its bottom edge 15 cm below rim height.

I'm checking the bracket more carefully — it's positioned about 31 cm beyond the rim and just 1 cm below rim height, 2.4 cm tall. Running the numbers, the ball's top surface at that point reaches about 2.99 m while the bracket bottom sits around 3.028 m, giving roughly a 4 cm clearance margin, which is tight but seems to pass.

Now I'm checking whether the ball actually brushes the far rim itself as it crosses the hoop plane, setting up the distance between the ball's surface and the far rim tube using the trajectory equations to see if they ever get close enough to touch.

Checking the front rim distance similarly, I scan several s values and find the minimum distance there is about 0.18, still safely above the 0.124 threshold. Good, that confirms this edge also clears.

Now I'm working out positions: the ball rests on the floor, with the hoop's rim placed 4 meters beyond it along one axis, and I'll set the floor size to roughly 12 meters to comfortably fit both, placing the ball near the origin and the rim at the 4 meter mark with the pole rising to about 5.6 meters.

I'm recalculating the launch velocity using a more precise ball radius of 11.9 cm, giving roughly 3.01 m/s horizontal and 8.73 m/s vertical speed, and planning the ball as a hollow basketball-like shell with lively bounce and friction so it drops cleanly through the hoop. Time to write the file.

