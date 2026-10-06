```world
world  five blocks toppled by a rolling pusher

floor
  size      6 m
  friction  0.7, spinning 0.005, rolling 0.001

block
  is a      cube 20 cm, 500 g
  friction  0.65, spinning 0.005, rolling 0.002
  bounce    dead
  colour    wood
  moves     freely
  stacked   5 high
  stands    on floor

pusher
  is a      sphere 8 cm radius, 4 kg
  rolls
  friction  0.6, spinning 0.005, rolling 0.001
  bounce    dead
  colour    orange
  moves     freely
  rests     on floor, 1.2 m behind block
  launched  2.5 m/s along
  spins     31.25 rad/s about y

expect
  pusher touches block1
  block5 touches floor
```