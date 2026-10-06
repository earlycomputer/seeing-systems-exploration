```world
world  gravity powered seesaw

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

support
  is a    box 8 by 30 by 64 cm
  stands  on floor
  colour  grey

pivot
  is a  point
  at    70 cm up

seesaw
  is a           box 160 by 24 by 4 cm, 200 g
  level with pivot
  turns on       seesaw hinge, about y, at pivot
  swings         from -25° to 0°
  starts turned  0°
  damping        0.002 N·m·s/rad
  armature       0.001 kg·m²
  friction       0.6, spinning 0.005, rolling 0.002
  bounce         dead
  colour         wood

ball
  is a      sphere 5 cm radius, 100 g
  moves     freely
  rolls
  bounce    dead
  friction  0.6, spinning 0.005, rolling 0.002
  rests     on seesaw, 65 cm beyond pivot
  colour    orange

weight
  is a      sphere 8 cm radius, 1 kg
  moves     freely
  bounce    dead
  friction  0.6, spinning 0.005, rolling 0.002
  at        65 cm behind pivot, 3 m up
  colour    dark grey

expect
  weight touches seesaw
  ball touches seesaw
  seesaw reaches its lower stop
```