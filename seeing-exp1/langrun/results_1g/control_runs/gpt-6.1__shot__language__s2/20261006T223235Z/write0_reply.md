```world
world  regulation basketball shot

floor
  size      12 m
  friction  0.8, spinning 0.005, rolling 0.002

ball
  is a      sphere 12 cm radius, 620 g
  is        hollow, lively
  colour    orange
  rolls
  friction  0.8, spinning 0.01, rolling 0.004
  moves     freely
  rests     on floor, 0 m along, 0 m to the left
  launched  2.5 m/s along, 9.68 m/s up

hoop
  is a        hoop
  rim height  3.05 m
  rim size    45.72 cm
  tube        8 mm
  its rim 4 m beyond ball

expect
  ball drops through hoop
```