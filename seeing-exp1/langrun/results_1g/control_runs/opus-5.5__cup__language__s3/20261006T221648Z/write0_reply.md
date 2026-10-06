The ball starts at rest near the high end of a gentle ramp, about 10° steep, and gravity rolls it down. It leaves the low end about 14 cm above the floor, clears the cup's low near wall, and drops into the cup. The cup has a tall far wall and a dead bounce. Its high rolling friction should bring the ball to rest inside it well within the 6 s.

I haven't run this. The numbers come from rough hand estimates:
- The ball leaves the ramp at about 1.5 m/s.
- It should land around 1.4 m along, inside the cup.
- Rolling friction in the cup should stop it within about a second.

```world
world  ball rolls down a ramp into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ramp
  is a        ramp
  high end    20 cm along, 30 cm up
  low end     1.2 m along, 12 cm up
  width       20 cm
  thickness   4 cm
  friction    0.8, spinning 0.002, rolling 0.0005
  colour      wood

cup
  is an             open box
  length            40 cm
  width             30 cm
  walls             15 cm
  near wall height  8 cm
  friction          1.0, spinning 0.02, rolling 0.01
  bounce            dead
  colour            grey
  its base 1.45 m along

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.002, rolling 0.0005
  colour    orange
  moves     freely
  rests     on ramp, 10 cm from the top

expect
  ball touches ramp
  ball comes to rest in cup
```

---
thinking (summarized):

I need to work out the ramp's geometry — a high end and low end for the slope, with a box at the foot to catch the ball. I'm trying to figure out how to specify the high and low points, maybe using position coordinates like height and horizontal distance, so the ball placed near the top rolls down into the cup.

For the cup placement, I'm thinking the near wall should be short enough for the ball to roll over given its speed, while the far wall stays tall to stop it, so the ball settles inside after bouncing a bit.

Let me recalculate: with the ramp dropping 38 cm over a meter at about 21°, I'm computing the ball's exit speed using the rolling sphere energy equation, giving roughly v ≈ 2.3 m/s at the bottom.

That's too fast, so I'm trying a gentler slope instead - high end at 30 cm, low end at 12 cm - and recomputing exit speed at about 1.45 m/s, then estimating fall time from the ramp's exit height down to the cup's base, and the resulting horizontal travel distance of around 21 cm, checking that against the cup's 40 cm length to see if the ball lands inside.

Now I'm worried about whether the ball will settle to rest within the time limit after bouncing between the walls, since a dead bounce with low rolling friction could mean it rolls back and forth for a while. I'm considering tuning the cup's friction parameters, like adding rolling friction, to help the ball lose energy faster and come to rest sooner.

That's small compared to gravity's component along the slope, so it's fine. For ball placement, I'll use "on ramp, 10 cm from the top" matching the doc's convention, letting gravity roll it down the 10.2° slope with friction 0.8. For the cup, I need to position it on the floor by its base.

I'm checking the vertical clearances: ramp foot around 12 cm up, deck top near 14 cm, matching ball height, with the near wall sitting 8 cm below the ball's path so it clears over, landing near x=1.2 before the far wall at 1.45. I'm leaving the across-position unspecified since it should default to centered, and double-checking that ramp width (20 cm) versus cup width (30 cm) won't cause the ball to miss.

Now I'm pinning down exact coordinates: ramp high end around 20 cm along and 30 cm up, foot at 1.2 m along and 12 cm up, cup base at 1.45 m along. For the ball starting 10 cm from the ramp top, I'm estimating the drop distance along the ~1 m ramp length and computing the resulting velocity at the bottom, getting roughly 1.5 m/s.

I should also set the ball's bounce to dead on contact, per the spec, so it settles properly rather than bouncing around.

