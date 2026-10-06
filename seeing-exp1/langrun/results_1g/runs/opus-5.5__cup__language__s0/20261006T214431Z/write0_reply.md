The ball rolls from rest down a gentle ramp. It leaves the low end just above the cup's near wall and drops into the cup. The cup's dead walls and grippy base settle it there.

Two things I haven't checked against a run:
- **Ramp heights:** I'm assuming the ramp's end points mark the deck's centre line, not its top surface.
- **Cup placement:** I'm assuming `its base 1.2 m along` moves the whole cup.

Rough numbers:
- **Speed off the ramp:** about 1.2 m/s.
- **Landing:** about 20 cm past the ramp's end, inside the cup's 30 cm length.
- **Clearance:** the ball's bottom should pass a few cm above the 12 cm near wall.

```world
world  ball rolls down a ramp into a cup

floor
  friction  0.8, spinning 0.005, rolling 0.002

ramp
  is a       ramp
  high end   25 cm up
  low end    1 m along, 14 cm up
  width      20 cm
  thickness  4 cm
  friction   0.9, spinning 0.005, rolling 0.002
  colour     wood

cup
  is a            open box
  length          30 cm
  width           30 cm
  walls           12 cm
  wall thickness  2 cm
  base thickness  2 cm
  friction        1.0, spinning 0.02, rolling 0.02
  bounce          dead
  colour          grey
  its base 1.2 m along

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.9, spinning 0.01, rolling 0.01
  colour    orange
  moves     freely
  rests     on ramp.deck, 10 cm from the top

expect
  ball touches ramp
  ball touches cup
  ball comes to rest in cup
```

---
thinking (summarized):

I'm reconsidering the geometry: instead of rolling into a cup with walls, it makes more sense to position the ramp's low end above the cup so the ball falls off into it, and I'm working out how to define that ramp's high and low end positions.

Thinking through placing the ball "on ramp.deck" a specific distance from the top, and whether the cup should just be an open box the ball drops into after flying off the end of the ramp rather than trying to roll directly in over a wall.

Let me work out actual numbers: ramp high end at 40 cm up, low end around 14 cm up over a 1 m span, giving roughly a 15° slope. Computing rolling speed with the solid-sphere moment of inertia from a 26 cm drop gives about 1.9 m/s at the bottom — fast enough that the ball will launch off the end rather than just roll off. I'm checking that the ball clears the cup's near wall height before dropping toward the middle of the cup and hitting the far wall, so friction and the bounce eventually bring it to rest inside.

I need to place the cup part using its base position, maybe at 1.3 m along, then work out wall placement so the near wall of the cup aligns with where the ball exits the ramp at x≈1.0 m. Checking the geometry, the ball's center height as it leaves the deck is roughly 0.17-0.19 m, while the cup wall is only 12 cm tall, so I need to verify whether the ball clears the wall or catches it after traveling that short horizontal gap.

Tracking the trajectory, the ball clears the near wall with only about a 0.8 cm drop over 0.04 s, then continues falling until it lands near the cup floor around x≈1.2 m, which is within the cup's 1.05-1.55 m span. It then strikes the far wall around 1.2 m/s, but since the wall is 12 cm tall and the ball center sits at only 5 cm, it stays contained; after that it's a dead bounce and the ball rolls back and forth, with rolling friction eventually damping it to rest, though I need to check the friction coefficients MuJoCo uses for this to estimate how long that settling takes.

Now I'm working out the leg and deck placement at x=0, with the ball starting 10 cm from the top. For the cup, I'll just specify its base 1.2 m along. For the ramp, I'll set the high end 25 cm up at the origin and the low end 1 m along at 14 cm up, then place the ball on the ramp deck 10 cm from the top, relying on gravity and ramp-contact behavior for the rest.

