```world
world  pendulum rolls a ball into a cup

floor
  size      4 m
  friction  0.6, spinning 0.001, rolling 0.0001

ball
  is a      sphere 5 cm radius, 150 g
  rolls
  moves     freely
  bounce    dead
  friction  0.6, spinning 0.001, rolling 0.0001
  colour    orange
  rests     on floor, 0 m along, 0 m to the left

pendulum
  is a               pendulum
  pivot height       65 cm
  length             60 cm
  bob size           8 cm across
  bob mass           500 g
  rod thickness      1 cm
  rod mass           30 g
  starts swung back  35°
  damping            0.01 N·m·s/rad
  bounce             dead
  colour             grey
  9 cm behind ball

-- A low entry lip lets the rolling ball enter the cup.
cup
  is an             open box
  length            36 cm
  width             24 cm
  walls             12 cm
  wall thickness    1 cm
  base thickness    3 mm
  near wall height  3 mm
  friction          0.8, spinning 0.01, rolling 0.015
  bounce            dead
  colour            wood
  sits              on floor, 1 m beyond ball

expect
  ball touches pendulum
  ball comes to rest in cup
```