The ball starts near the top of a gently sloping ramp. The ramp ends just above the low near wall of an open cup, so the ball rolls down, drops in, and its dead bounce and rolling friction bring it to rest inside.

```world
world  ball rolls down a ramp into a cup

floor
  friction  0.8, spinning 0.005, rolling 0.002

ramp
  is a       ramp
  high end   0 m along, 30 cm up
  low end    1 m along, 14 cm up
  width      20 cm
  thickness  4 cm
  friction   0.8, spinning 0.005, rolling 0.002
  colour     wood

cup
  is an             open box
  length            50 cm
  width             30 cm
  walls             12 cm
  near wall height  10 cm
  friction          0.8, spinning 0.005, rolling 0.003
  bounce            dead
  colour            white
  on floor, 1.27 m along

ball
  is a      sphere 3 cm radius, 50 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.005, rolling 0.002
  colour    orange
  moves     freely
  rests     on ramp.deck, 10 cm from the top

expect
  ball touches ramp
  ball comes to rest in cup
```

---
thinking (summarized):

I'm sketching out a world with a ramp, a ball, and a cup at the bottom, thinking through how to define the ramp's geometry—its high end, low end, and width—so the ball can roll down and settle into the cup.

For the deck, I'm treating it as a centreline going from top to foot with a fixed thickness, and placing the ball resting on the ramp's deck a set distance from the top for clarity. For the cup, I'm defining it as an open box with its pieces placed on the floor.

Now I'm working out the geometry so the ball rolls off the ramp and lands inside the cup rather than hitting a wall and bouncing out. The plan is to set the ramp's foot height to roughly match the cup's near wall top, so the ball naturally falls into the cup's interior after leaving the deck, using the cup's length and wall height to position the ramp's endpoint precisely at the cup's near edge.

I need the ball to eventually settle within 6 seconds, so I want enough rolling friction to damp it out, but too much rolling friction coefficient relative to radius could actually prevent it from rolling down the 14.6° slope in the first place—checking tan(slope)≈0.26 against μ_roll/r suggests I need to pick a smaller rolling friction value so gravity still overcomes resistance while still damping the ball over time.

A 16 cm drop gives the ball roughly 1.5 m/s with a ramp angle near 9°, well above the friction threshold so it keeps rolling. Now I'm checking clearances — deck thickness and cup wall height near the foot of the ramp — to make sure nothing intersects where the ramp meets the cup.

I'm placing the cup centered about 1.27 m along with its near wall spanning 1.01 to 1.03 m, leaving about a 1 cm gap past the deck's end, and accounting for the slight corner extension from the ramp's slope rotation. Lowering the near wall to 10 cm (versus 12 cm elsewhere) should give the ball enough clearance to land inside cleanly, since the ball's center sits around 19 cm at the foot.

For the ramp itself I'll skip giving it an explicit position since its pieces are defined by the high and low ends absolutely, similar to how the bucket uses "on table." The ball is a 3 cm radius sphere, 50 g, with rolling/spinning friction values and placed "on ramp.deck, 10 cm from the top," defaulting its across position to 0.

The cup gets friction 0.8 with spinning 0.005 and rolling 0.003, bounce dead, and floor friction set to 0.8 too. The expected behavior is that the ball rolls down the ramp and comes to rest in the cup, starting purely from gravity with no launch needed.

