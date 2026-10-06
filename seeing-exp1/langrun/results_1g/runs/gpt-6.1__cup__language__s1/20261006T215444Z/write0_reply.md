```world
world  ball rolls down into a cup

floor
  size      4 m
  friction  0.8, spinning 0.005, rolling 0.004

ramp start
  is a  point
  at    40 cm up, 0 m along

ramp finish
  is a  point
  at    15 cm up, 1 m along

ramp
  is a       ramp
  high end   ramp start
  low end    ramp finish
  width      30 cm
  thickness  3 cm
  friction   0.8, spinning 0.005, rolling 0.002
  bounce     dead
  colour     wood

cup
  is an             open box
  length            70 cm
  width             50 cm
  walls             30 cm
  near wall height  11 cm
  wall thickness    2 cm
  base thickness    2 cm
  friction          0.9, spinning 0.02, rolling 0.012
  bounce            dead
  colour            grey
  on                floor, 1.35 m along

ball
  is a      sphere 4 cm radius, 150 g
  moves     freely
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  on        ramp, 15 cm from the top

expect
  ball touches ramp
  ball comes to rest in cup
```

---
thinking (summarized):

**Calculating ball trajectory**

I'm considering a cup with a radius of .015 and a height of .04. It seems huge if we think about it! I'm estimating that a ball should reach the cup in under 6 seconds. I’m trying to figure out if the dimensions are appropriate for that. I want to confirm how quickly the ball will dissipate in that time frame. It’s interesting to analyze how all these numbers play together.

**Analyzing rolling contacts**

I need to create actual rolling contacts for the compiler, likely using condim6. Should I consider cup-shaped flag rolls? I want to ensure there’s enough friction for proper rolling contact, focusing on the dimensions. The geometry looks good for a cup shape—maybe I can design it as a square with specific wall and ramp measurements. I'll factor in ball speed and release angle to calculate bounce and wall interactions. It’s an interesting challenge!

**Calculating ball dynamics in the cup**

I'm considering the impact of baseline ball friction and how it affects the roll and travel time. Based on some calculations, I get specific values for travel distance, velocity, and cup rolling dynamics. The friction coefficients and different wall heights play a crucial role in determining where and how the ball will land. I need to ensure the cup dimensions and ramp setup facilitate the right flight path and stop effectively. The details are starting to come together nicely!

**Clarifying position inputs**

I'm trying to figure out the position details for parts within the model. It seems there are world points used correctly, but I need to clarify how the `at high end` value is parsed. I'm wondering if the defaults center is needed for the ramp piece model. It looks like the library doesn't require an initial position, as the exact points are already given. I’ll work through this to ensure everything is aligned properly!