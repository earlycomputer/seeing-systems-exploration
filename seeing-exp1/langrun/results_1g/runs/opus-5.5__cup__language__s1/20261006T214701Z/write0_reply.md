The ball starts near the top of a sloping ramp and rolls down it. It rolls off the low end and drops into a wide open box (the cup) just past the foot. Its dead bounce lets it settle inside before the 6 s run ends.

By my estimate it leaves the ramp at about 1.5 m/s and lands about 22 cm past the foot, near the middle of the cup. That estimate assumes the deck's surface follows the high-end and low-end points. If the run shows otherwise, the cup's position along x is what needs adjusting.

```world
world  ball rolls down a ramp into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ramp
  is a       ramp
  high end   0 m along, 40 cm up
  low end    60 cm along, 20 cm up
  width      30 cm
  thickness  4 cm
  friction   0.9, spinning 0.005, rolling 0.002
  colour     wood

cup
  is a            open box
  length          40 cm
  width           34 cm
  walls           12 cm
  wall thickness  2 cm
  base thickness  2 cm
  friction        0.9, spinning 0.01, rolling 0.01
  bounce          dead
  colour          grey
  its base 85 cm along

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.9, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on ramp.deck, 8 cm from the top

expect
  ball touches ramp
  ball comes to rest in cup
```

---
thinking (summarized):

I'm thinking through the physical setup: a ramp feeding a ball onto the floor and into a cup, and considering whether the cup's near wall needs to be low enough—maybe matching the base thickness—for the ball to roll in without needing to clear a tall edge.

Instead, it might be more reliable to have the ball leave the end of the ramp in the air and fall directly into the cup, treating it as a projectile landing in a wide-enough container rather than something rolling over a step. I'm working out rough dimensions—ramp height, cup width and wall height, and how to phrase the position syntax for "high end" and "low end" with along/across/up offsets—then I'll need to check the trajectory math to confirm the ball actually lands inside the cup given its rolling speed off the ramp.

Solving for fall time gives t≈0.18s, so the ball travels about 32 cm horizontally after leaving the ramp, landing near x≈112 cm. I'll size the cup to span roughly 92–132 cm to catch it, and checking the trajectory at the near wall (height 15 cm) confirms the ball still clears it comfortably at that point.

With dead-bounce physics and moderate rolling friction, the ball should oscillate and settle inside the cup within the time limit, assuming walls are tall enough. But that speed feels a bit high, so I'm reconsidering a gentler ramp instead—starting at 40 cm, ending at 20 cm over a 60 cm run, giving a shallower 18.4° slope and a lower exit velocity (~1.56 m/s), which should land more gently.

Working through the drop time and landing position, the ball lands around 82 cm, which fits neatly inside a 40 cm cup centered at 85 cm (spanning 65 to 105 cm), with no overlap against the ramp's base near 60 cm. I'm checking that wall heights at the near edge of the cup still clear the ball's trajectory comfortably.

Now figuring out placement syntax for the open box: I'll phrase it as "its base 85 cm along" to position it correctly, following the established pattern for referencing specific faces of a part. For the ball, I'm specifying its position as "on ramp, 8 cm from the top," referring to the ramp's deck surface.

I'll set the ball's rolling friction low (around 0.002) so it naturally settles after moving, make its bounce behavior dead so it doesn't bounce off the ramp, and configure the cup's friction so the ball comes to rest inside it rather than sliding out.

