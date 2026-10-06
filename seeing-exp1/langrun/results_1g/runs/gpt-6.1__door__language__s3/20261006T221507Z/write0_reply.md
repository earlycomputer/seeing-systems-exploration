```world
world  self closing door

floor
  size      4 m
  friction  0.8, spinning 0.005, rolling 0.002

hinge jamb
  is a      box 8 by 8 by 214 cm
  stands    on floor, 54 cm to the right
  colour    grey

door
  is a           box 4 by 90 by 200 cm, 12 kg
  raised         2 cm
  colour         wood
  bounce         dead
  turns on       hinge, about z, at its right side
  swings         from 0° to 100°
  spring         45 N·m/rad toward 0°
  damping        16 N·m·s/rad
  starts turned  75°

expect
  door reaches its lower stop
```