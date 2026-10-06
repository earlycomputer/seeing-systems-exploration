```world
world  five blocks toppled by a rolling pusher

floor
  size      6 m
  friction  0.6, spinning 0.005, rolling 0.0002

block
  is a      cube 20 cm, 500 g
  moves     freely
  stacked   5 high
  friction  0.7, spinning 0.005, rolling 0.002
  bounce    dead
  colour    wood
  stands    on floor

pusher
  is a      sphere 8 cm radius, 6 kg
  moves     freely
  rolls
  friction  0.6, spinning 0.005, rolling 0.0002
  bounce    dead
  colour    orange
  rests     on floor, 1.2 m outside block's near end
  launched  2 m/s along
  spins     25 rad/s about y

expect
  pusher touches block1
```