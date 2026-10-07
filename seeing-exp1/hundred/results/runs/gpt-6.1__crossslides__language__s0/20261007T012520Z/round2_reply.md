```world
world  gravity driven crossed slides

floor
  size  6 m
  friction  0.8, spinning 0.005, rolling 0.03

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
  at  1.2 m along, 65 cm up
  colour  orange

slide origin
  is a  point
  at  0 m along, 0 m to the left, 1.1 m up

ball tray
  is an  open box
  length  2 m
  width  60 cm
  walls  50 cm
  wall thickness  2 cm
  base thickness  3 cm
  on  floor, 1.85 m behind slide origin
  friction  0.8, spinning 0.005, rolling 0.03
  bounce  dead

slide bed
  is a  box 195 by 240 by 8 cm
  at  12.5 cm along, 1.06 m up
  friction  0.005
  bounce  dead
  colour  grey

-- The first carriage is captured along x.
-- Its long rear section stays between the guides throughout its stroke.

first left rail
  is a  box 124 by 3 by 8 cm
  at  22 cm behind slide origin, 12 cm to the left, 1.12 m up
  friction  0.005
  bounce  dead

first right rail
  is a  box 124 by 3 by 8 cm
  at  22 cm behind slide origin, 12 cm to the right, 1.12 m up
  friction  0.005
  bounce  dead

first left keeper
  is a  box 124 by 3 by 2 cm
  at  22 cm behind slide origin, 9 cm to the left, 1.151 m up
  friction  0.005
  bounce  dead

first right keeper
  is a  box 124 by 3 by 2 cm
  at  22 cm behind slide origin, 9 cm to the right, 1.151 m up
  friction  0.005
  bounce  dead

first rear stop
  is a  box 4 by 24 by 8 cm
  at  76 cm behind slide origin, 1.12 m up
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

-- The second carriage is captured along y.
-- Its guides are behind the cam, outside the first carriage's path.

second near rail
  is a  box 3 by 80 by 8 cm
  at  55 cm along, 70 cm to the right, 1.12 m up
  friction  0.005
  bounce  dead

second far rail
  is a  box 3 by 80 by 8 cm
  at  73 cm along, 70 cm to the right, 1.12 m up
  friction  0.005
  bounce  dead

second near keeper
  is a  box 3 by 80 by 2 cm
  at  57.5 cm along, 70 cm to the right, 1.151 m up
  friction  0.005
  bounce  dead

second far keeper
  is a  box 3 by 80 by 2 cm
  at  70.5 cm along, 70 cm to the right, 1.151 m up
  friction  0.005
  bounce  dead

-- The elevated stop catches the raised runner lug after 22 cm of travel.
-- The cam and its flat connecting link pass underneath it.

second end stop
  is a  box 10 by 4 by 8 cm
  at  64 cm along, 1 cm to the right, 1.20 m up
  bounce  dead

cam near end
  is a  point
  at  48 cm along, 16 cm to the left, 1.12 m up

cam far end
  is a  point
  at  80 cm along, 16 cm to the right, 1.12 m up

slider2
  is a  rod 4 cm thick, from cam near end to cam far end
  weighs  80 g
  moves  freely
  friction  0.005
  bounce  dead
  colour  orange

second runner
  is a  box 14 by 80 by 4 cm, 80 g
  at  64 cm along, 65 cm to the right, 1.12 m up
  attached to  slider2
  friction  0.005
  bounce  dead

runner link
  is a  box 8 by 32 by 4 cm, 25 g
  at  64 cm along, 13 cm to the right, 1.12 m up
  attached to  slider2
  friction  0.005
  bounce  dead

second stop lug
  is a  box 10 by 4 by 10 cm, 20 g
  at  64 cm along, 27 cm to the right, 1.19 m up
  attached to  slider2
  friction  0.005
  bounce  dead

support connecting bar
  is a  box 39 by 4 by 4 cm, 25 g
  at  66.5 cm along, 16 cm to the left, 1.12 m up
  attached to  slider2
  friction  0.005
  bounce  dead

support bracket
  is a  box 6 by 16 by 4 cm, 20 g
  at  85 cm along, 10 cm to the left, 1.12 m up
  attached to  slider2
  friction  0.005
  bounce  dead

withdrawable support
  is a  box 60 by 20 by 4 cm, 60 g
  at  1.10 m along, 1.12 m up
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

-- The vertical fall to first contact with the inclined slide is 0.400 m.

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
  ball comes to rest in ball tray
```