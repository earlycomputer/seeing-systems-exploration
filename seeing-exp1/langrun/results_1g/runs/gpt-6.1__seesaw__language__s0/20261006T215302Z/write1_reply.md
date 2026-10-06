```world
world  drop-powered seesaw

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

stand
  is a    box 6 by 16 by 60 cm
  stands  on floor
  colour  dark grey

pivot
  is a  point
  at    65 cm up

seesaw
  is a           box 160 by 20 by 3 cm, 400 g
  at             0 m along, 0 m to the left, 65 cm up
  turns on       seesaw hinge, about y, at pivot
  swings         from -30° to 0°
  starts turned  0°
  damping        0.005 N·m·s/rad
  armature       0.0001 kg·m²
  friction       0.7, spinning 0.005, rolling 0.002
  bounce         dead
  colour         wood

ball
  is a      sphere 4 cm radius, 100 g
  moves     freely
  rolls
  bounce    dead
  friction  0.7, spinning 0.005, rolling 0.002
  rests     on seesaw, 65 cm beyond seesaw
  colour    orange

weight
  is a      sphere 7 cm radius, 1 kg
  moves     freely
  rolls
  bounce    dead
  friction  0.7, spinning 0.005, rolling 0.002
  at        65 cm behind seesaw, 3 m up
  colour    black

expect
  weight touches seesaw
  ball touches seesaw
  seesaw reaches its lower stop
```