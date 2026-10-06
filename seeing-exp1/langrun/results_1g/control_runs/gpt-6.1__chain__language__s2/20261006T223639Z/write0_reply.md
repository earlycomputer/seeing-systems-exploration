```world
world  three balls roll into a cup

floor
  size      4 m
  friction  0.8, spinning 0.001, rolling 0.0002

ball1
  is a      sphere 5 cm radius, 200 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.001, rolling 0.0002
  colour    orange
  moves     freely
  sits      on floor, 0 m along, 0 m to the left
  launched  1.2 m/s along
  spins     24 rad/s about y

ball2
  is a      sphere 5 cm radius, 200 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.001, rolling 0.0002
  colour    white
  moves     freely
  sits      on floor, 30 cm beyond ball1, 0 m to the left

ball3
  is a      sphere 5 cm radius, 200 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.001, rolling 0.0002
  colour    grey
  moves     freely
  sits      on floor, 30 cm beyond ball2, 0 m to the left

cup
  is an             open box
  length            50 cm
  width             30 cm
  walls             18 cm
  wall thickness    2 mm
  base thickness    1 mm
  near wall height  1 mm
  friction          0.8, spinning 0.01, rolling 0.004
  bounce            dead
  colour            wood
  sits              on floor, 40 cm beyond ball3, 0 m to the left

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

---
thinking (summarized):

**Designing a cup geometry**

I'm trying to create a cup design that's easy to flush with a flat floor. The base should be about 0.5mm near the wall, and I need a thickness of 0.001m. The cup will have a width of 18cm, a length of 30cm, and a height of 1mm near the wall, tapering to 1mm at the base. I’ve planned for the cup's top to have a diameter starting at 0.75m and ending at 1.25m. There will be three stops for the ball, positioned at 0.9m.

**Considering cup alignment**

I'm trying to determine if the cup's base contact starts at 0.65 when it collides with the sphere at the edge, which is 0.05 ahead of the center at 0.70. The round step seems fine. I’m checking if the cup is above ball three. The cup is on the floor, 40cm beyond ball three, and I'm considering optional alignment centered at y0. I think having the cup on the floor resolves any potential issues with wall proximity.