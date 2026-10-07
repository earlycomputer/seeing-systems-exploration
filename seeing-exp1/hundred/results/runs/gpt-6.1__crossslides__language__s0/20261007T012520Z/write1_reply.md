```world
world  falling ball and crossed slides

floor
  size  5 m
  friction  0.8, spinning 0.005, rolling 0.002

box
  is an  open box
  length  55 cm
  width  55 cm
  walls  25 cm
  wall thickness  2 cm
  base thickness  3 cm
  friction  0.8
  bounce  dead
  on  floor, 1.2 m along

hoop
  is a  ring 40 cm across, 8 mm thick
  at  1.2 m along, 70 cm up
  colour  orange

slide origin
  is a  point
  at  0 m along, 0 m to the left, 1.1 m up

slide bed
  is a  box 195 by 130 by 8 cm
  at  12.5 cm along, 30 cm to the left, 1.06 m up
  friction  0.005
  colour  grey

-- These rails capture the long carriage while leaving its nose exposed.

first left rail
  is a  box 124 by 3 by 8 cm
  at  22 cm behind slide origin, 12 cm to the left, 1.12 m up
  friction  0.005

first right rail
  is a  box 124 by 3 by 8 cm
  at  22 cm behind slide origin, 12 cm to the right, 1.12 m up
  friction  0.005

first left keeper
  is a  box 124 by 3 by 2 cm
  at  22 cm behind slide origin, 9 cm to the left, 1.151 m up
  friction  0.005

first right keeper
  is a  box 124 by 3 by 2 cm
  at  22 cm behind slide origin, 9 cm to the right, 1.151 m up
  friction  0.005

first end stop
  is a  box 4 by 24 by 8 cm
  at  1.09 m along, 1.12 m up
  bounce  dead

impact low end
  is a  point
  at  20 cm behind slide origin, 1.15 m up

impact high end
  is a  point
  at  20 cm beyond slide origin, 1.55 m up

slider1
  is a  plank from impact low end to impact high end, 12 cm wide, 4 cm thick
  weighs  120 g
  moves  freely
  friction  0.005
  bounce  dead
  colour  wood

first carriage
  is a  box 94 by 20 by 4 cm, 60 g
  at  23 cm behind slide origin, 1.12 m up
  attached to  slider1
  friction  0.005
  bounce  dead

-- The second carriage runs across on a separate captured track.
-- Its diagonal cam converts along motion into across motion.

second track
  is a  box 18 by 130 by 6 cm
  at  64 cm along, 90 cm to the left, 1.43 m up
  friction  0.005

second near rail
  is a  box 3 by 125 by 10 cm
  at  55 cm along, 92.5 cm to the left, 1.48 m up
  friction  0.005

second far rail
  is a  box 3 by 125 by 10 cm
  at  73 cm along, 92.5 cm to the left, 1.48 m up
  friction  0.005

second near keeper
  is a  box 3 by 125 by 2 cm
  at  57.5 cm along, 92.5 cm to the left, 1.531 m up
  friction  0.005

second far keeper
  is a  box 3 by 125 by 2 cm
  at  70.5 cm along, 92.5 cm to the left, 1.531 m up
  friction  0.005

second end stop
  is a  box 14 by 4 by 6 cm
  at  64 cm along, 1.37 m to the left, 1.49 m up
  bounce  dead

cam near end
  is a  point
  at  48 cm along, 16 cm to the left, 1.12 m up

cam far end
  is a  point
  at  80 cm along, 16 cm to the right, 1.12 m up

slider2
  is a  plank from cam near end to cam far end, 2.5 cm wide, 4 cm thick
  weighs  80 g
  moves  freely
  friction  0.005
  bounce  dead
  colour  orange

second runner
  is a  box 14 by 60 by 6 cm, 80 g
  at  64 cm along, 65 cm to the left, 1.49 m up
  attached to  slider2
  friction  0.005
  bounce  dead

-- The bridge passes above the rails and keepers, with 9 mm clearance.

cam upright
  is a  box 5 by 5 by 49 cm, 25 g
  at  50 cm along, 16 cm to the left, 1.345 m up
  attached to  slider2
  friction  0.005

cam bridge
  is a  box 19 by 5 by 4 cm, 20 g
  at  57 cm along, 50 cm to the left, 1.57 m up
  attached to  slider2
  friction  0.005

cam bridge link
  is a  box 5 by 39 by 4 cm, 20 g
  at  50 cm along, 33 cm to the left, 1.57 m up
  attached to  slider2
  friction  0.005

support upright
  is a  box 5 by 5 by 16 cm, 20 g
  at  65 cm along, 50 cm to the left, 1.57 m up
  attached to  slider2
  friction  0.005

support spine
  is a  box 6 by 64 by 4 cm, 25 g
  at  65 cm along, 27 cm to the left, 1.60 m up
  attached to  slider2
  friction  0.005

withdrawable support
  is a  box 65 by 20 by 3 cm, 60 g
  at  97.5 cm along, 1.635 m up
  attached to  slider2
  friction  0.001
  bounce  dead
  colour  wood

block
  is a  cube 12 cm, 300 g
  moves  freely
  on  withdrawable support, 1.2 m along, 0 m to the left
  friction  0.001
  bounce  dead
  colour  white

-- The ball falls 0.400 m before contacting the inclined slide.
-- Gravity supplies the only initial drive.

ball
  is a  sphere 6 cm radius, 2.5 kg
  moves  freely
  rolls
  at  0 m along, 0 m to the left, 1.86314 m up
  friction  0.005
  bounce  dead
  colour  orange

expect
  ball touches slider1
  slider1 touches slider2
  block drops through hoop
  block comes to rest in box
```