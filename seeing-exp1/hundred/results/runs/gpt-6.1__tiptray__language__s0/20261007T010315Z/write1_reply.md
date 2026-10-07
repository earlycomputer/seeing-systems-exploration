```world
world  falling weight and tipping tray

floor
  size      10 m
  friction  0.8, spinning 0.005, rolling 0.002

tray pivot
  is a  point
  at    1.3 m up, 0 m along, 0 m to the left

tray
  is a           box 90 by 50 by 1.8 cm, 650 g
  level with     tray pivot
  0 m along
  0 m to the left
  turns on       tray hinge, about y, at tray pivot
  swings         from -20° to 0°
  spring         4 N·m/rad toward 0°
  damping        3 N·m·s/rad
  armature       0.6 kg·m²
  starts turned  0°
  friction       0.6, spinning 0.001, rolling 0.0005
  bounce         dead
  colour         wood

tray ball left rail
  is a         box 90 by 1 by 8 cm, 20 g
  on           tray, 3 cm right of tray
  attached to  tray
  bounce       dead
  colour       wood

tray ball right rail
  is a         box 90 by 1 by 8 cm, 20 g
  on           tray, 21 cm right of tray
  attached to  tray
  bounce       dead
  colour       wood

weight pocket near wall
  is a         box 1 by 21 by 14 cm, 20 g
  on           tray, 40 cm behind tray, 13 cm left of tray
  attached to  tray
  bounce       dead
  colour       wood

weight pocket far wall
  is a         box 1 by 21 by 14 cm, 20 g
  on           tray, 16 cm behind tray, 13 cm left of tray
  attached to  tray
  bounce       dead
  colour       wood

weight pocket left wall
  is a         box 25 by 1 by 14 cm, 20 g
  on           tray, 28 cm behind tray, 23 cm left of tray
  attached to  tray
  bounce       dead
  colour       wood

weight pocket right wall
  is a         box 25 by 1 by 14 cm, 20 g
  on           tray, 28 cm behind tray, 3 cm left of tray
  attached to  tray
  bounce       dead
  colour       wood

-- The tray top is at 1.309 m. The weight's bottom starts
-- at 1.909 m, giving a clear vertical drop of 0.600 m.
weight
  is a      cube 8 cm, 2 kg
  moves     freely
  at        1.949 m up, 28 cm behind tray, 13 cm left of tray
  friction  0.8, spinning 0.01, rolling 0.002
  bounce    dead
  colour    dark grey

ball1
  is a      sphere 5.5 cm radius, 600 g
  moves     freely
  rolls
  on        tray, 14 cm beyond tray, 12 cm right of tray
  friction  0.6, spinning 0.001, rolling 0.0005
  bounce    dead
  colour    orange

ramp entrance
  is a  point
  at    1.135 m up, 46 cm behind tray, 12 cm right of tray

ramp exit
  is a  point
  at    65 cm up, 1.4 m behind tray, 12 cm right of tray

spill ramp
  is a      plank from ramp entrance to ramp exit, 24 cm wide, 2 cm thick
  friction  0.6, spinning 0.001, rolling 0.0005
  bounce    dead
  colour    wood

transfer deck
  is a      box 60 by 24 by 2 cm
  at        65 cm up, 1.7 m behind tray, 12 cm right of tray
  friction  0.3, spinning 0.001, rolling 0.0005
  bounce    dead
  colour    wood

ball2
  is a      sphere 6 cm radius, 400 g
  moves     freely
  rolls
  on        transfer deck, 4 cm beyond transfer deck
  friction  0.5, spinning 0.001, rolling 0.0005
  bounce    dead
  colour    white

block
  is a      cube 10 cm, 80 g
  moves     freely
  on        transfer deck, 23 cm behind transfer deck
  friction  0.25, spinning 0.005, rolling 0.002
  bounce    dead
  colour    wood

hoop
  is a    ring 1.6 m across, 1 cm thick
  at      45 cm up, 2.65 m behind tray, 12 cm right of tray
  bounce  dead
  colour  orange

bin
  is an           open box
  length          2.2 m
  width           1.9 m
  walls           38 cm
  wall thickness  3 cm
  base thickness  3 cm
  on              floor, 2.65 m behind tray, 12 cm right of tray
  friction        0.9, spinning 0.02, rolling 0.01
  bounce          dead
  colour          grey

expect
  weight touches tray
  tray reaches its lower stop
  ball1 touches spill ramp
  ball1 touches ball2
  ball2 touches block
  block drops through hoop
  block comes to rest in bin
```