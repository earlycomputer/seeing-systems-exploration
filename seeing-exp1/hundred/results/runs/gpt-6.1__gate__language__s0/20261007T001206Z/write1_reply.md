```world
world  ramp paddle slider drop

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ramp top
  is a  point
  at    1.2 m behind floor, 1.7 m up

ramp foot
  is a  point
  at    0 m along, 80 cm up

ramp
  is a      plank from ramp top to ramp foot, 36 cm wide, 4 cm thick
  friction  0.6, spinning 0.001, rolling 0.0005
  bounce    dead
  colour    wood

-- The ramp is 1.5 m long: the ball starts 1 m up from its foot.
ball
  is a      sphere 9 cm radius, 900 g
  moves     freely
  rolls
  friction  0.6, spinning 0.001, rolling 0.0005
  bounce    dead
  colour    orange
  rests     on ramp, 50 cm from the top

-- The paddle's bottom is 86 cm high, clear of the 84 cm ledge top.
paddle
  is a           box 6 by 75 by 14 cm, 250 g
  at             10 cm along, 22.5 cm to the right, 93 cm up
  turns on       paddle hinge, about z, at its right side
  swings         from -38° to 0°
  starts turned  0°
  damping        0.03 N·m·s/rad
  friction       0.3
  bounce         dead
  colour         wood

ledge
  is a      box 70 by 30 by 6 cm
  at        22 cm along, 38 cm to the right, 81 cm up
  friction  0.25
  bounce    dead
  colour    grey

slider
  is a      box 28 by 12 by 10 cm, 450 g
  moves     freely
  rests     on ledge, 30 cm along, 38 cm to the right
  friction  0.25
  bounce    dead
  colour    dark grey

-- These guides constrain the loose striker to slide horizontally.
left slider guide
  is a      box 18 by 1.6 by 12 cm
  at        51 cm along, 30.9 cm to the right, 90 cm up
  friction  0.15
  bounce    dead
  colour    grey

right slider guide
  is a      box 18 by 1.6 by 12 cm
  at        51 cm along, 45.1 cm to the right, 90 cm up
  friction  0.15
  bounce    dead
  colour    grey

slider keeper
  is a      box 18 by 16 by 2 cm
  at        51 cm along, 38 cm to the right, 95.4 cm up
  friction  0.15
  bounce    dead
  colour    grey

-- The shoulder catches the guide ends after 21 cm of travel.
slider shoulder
  is a         box 2 by 22 by 10 cm, 20 g
  attached to  slider
  at           20 cm along, 38 cm to the right, 89 cm up
  friction     0.15
  bounce       dead
  colour       dark grey

block
  is a      cube 10 cm, 120 g
  moves     freely
  rests     on ledge, 53 cm along, 38 cm to the right
  friction  0.45, spinning 0.01, rolling 0.002
  bounce    dead
  colour    white

hoop
  is a    ring 120 cm across, 8 mm thick
  at      93 cm along, 38 cm to the right, 48 cm up
  bounce  dead
  colour  orange

box
  is an           open box
  length          160 cm
  width           140 cm
  walls           28 cm
  wall thickness  3 cm
  base thickness  4 cm
  at              93 cm along, 38 cm to the right
  friction        0.9, spinning 0.02, rolling 0.01
  bounce          dead
  colour          wood

expect
  ball touches ramp
  ball touches paddle
  paddle touches slider
  slider touches block
  block drops through hoop
  block comes to rest in box
```