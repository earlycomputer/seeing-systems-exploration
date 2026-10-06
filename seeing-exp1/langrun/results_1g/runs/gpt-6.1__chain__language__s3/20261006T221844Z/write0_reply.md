```world
world  three balls roll into a cup

floor
  size      4 m
  friction  0.6, spinning 0.005, rolling 0.003

ball1
  is a      sphere 6 cm radius, 200 g
  rolls
  bounce    lively
  friction  0.6, spinning 0.005, rolling 0.003
  colour    orange
  moves     freely
  sits      on floor, 0 cm along, 0 cm to the left
  launched  1.8 m/s along
  spins     30 rad/s about y

ball2
  is a      sphere 6 cm radius, 200 g
  rolls
  bounce    lively
  friction  0.6, spinning 0.005, rolling 0.003
  colour    white
  moves     freely
  sits      on floor, 24 cm beyond ball1, 0 cm to the left

ball3
  is a      sphere 6 cm radius, 200 g
  rolls
  bounce    lively
  friction  0.6, spinning 0.005, rolling 0.003
  colour    orange
  moves     freely
  sits      on floor, 24 cm beyond ball2, 0 cm to the left

cup
  is an            open box
  length           48 cm
  width            30 cm
  walls            18 cm
  wall thickness   1 cm
  base thickness   4 mm
  near wall height  4 mm
  bounce           dead
  friction         1.2, spinning 0.02, rolling 0.015
  colour           wood
  sits             on floor, 48 cm beyond ball3, 0 cm to the left

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

---
thinking (summarized):

**Analyzing ball dynamics**

I'm considering how lively contact affects ball transfer. At a velocity of 1.8, ball three should roll about 0.92 before entering a low lip, with a gap around .2. If the cup is close enough, other balls will likely follow within about 6 seconds. To ensure proper stopping, larger masses descending could help with ball one carrying inertia to prevent back rolling. I'll need to tune the floor friction accordingly.

**Considering cup design**

I’m thinking about designing a cup with a low rim, possibly around .004 inches, which might be considered a shallow entrance. My main concern is ensuring that expectations align with the notion that the "ball3" comes to rest in the cup. I need to ensure it detects the center and is bounded, plus the z-axis? I wonder how the standard base parser will handle this design choice. I'll have to explore these aspects further!