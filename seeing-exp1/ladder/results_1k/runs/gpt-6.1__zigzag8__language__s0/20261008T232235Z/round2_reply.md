```world
world  impact released gravity chain

-- All moving bodies start from rest.
-- No launches or initial spins are used.
-- Numeric restitution and slide-joint damping are unavailable
-- in the supplied language.
-- Spring assists are held by physical impact-release latches.
-- This revision has not been simulated.

floor
  size      6 m
  friction  0.72, spinning 0.005, rolling 0.002

ring1
  is a      ring 16 cm across, 8 mm thick
  at        30 cm behind floor, 57 cm up
  friction  0.72
  bounce    dead
  colour    orange

ball1
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  centred over ring1, 30 cm above ring1
  friction  0.72, spinning 0.005, rolling 0.002
  bounce    dead

lever pivot
  is a      point
  at        30 cm up

lever1
  is a           box 60 by 10 by 4 cm, 0.50 kg
  at             lever pivot
  turns on       lever hinge, about y, at lever pivot
  swings         from -45° to 0°
  starts turned  0°
  spring         40 N·m/rad toward -45°
  damping        0.04 N·m·s/rad
  armature       0.05 kg·m²
  friction       0.72
  bounce         dead
  colour         wood

-- The latch's rear stems are moved forward to clear ramp1.leg.
-- Opening the latch moves its narrow support sideways,
-- out from under the lever.

lever latch pivot
  is a      point
  at        55 cm behind lever pivot, 3 cm to the left, 48 cm up

lever latch elbow
  is a      point
  at        55 cm behind lever pivot, 5 cm to the left, 26.5 cm up

lever latch foot
  is a      point
  at        29.5 cm behind lever pivot, 5 cm to the left, 27.5 cm up

lever latch trigger anchor
  is a      point
  at        55 cm behind lever pivot, 31.5 cm up

lever latch button centre
  is a      point
  at        31 cm behind lever pivot, 31.5 cm up

lever latch stem
  is a           rod 10 mm thick, from lever latch pivot to lever latch elbow
  weighs         30 g
  turns on       lever latch hinge, about x, at lever latch pivot
  swings         from 0° to 90°
  starts turned  0°
  spring         0.5 N·m/rad toward 0°
  damping        0.04 N·m·s/rad
  friction       0.72
  bounce         dead

lever latch support arm
  is a         rod 6 mm thick, from lever latch elbow to lever latch foot
  weighs       10 g
  attached to  lever latch stem
  friction     0.72
  bounce       dead

lever latch support
  is a         box 20 by 2 by 10 mm, 5 g
  at           29.5 cm behind lever pivot, 5 cm to the left, 27.5 cm up
  attached to  lever latch stem
  friction     0.72
  bounce       dead

lever latch trigger stem
  is a         rod 6 mm thick, from lever latch pivot to lever latch trigger anchor
  weighs       10 g
  attached to  lever latch stem
  friction     0.72
  bounce       dead

lever latch trigger arm
  is a         rod 6 mm thick, from lever latch trigger anchor to lever latch button centre
  weighs       5 g
  attached to  lever latch stem
  friction     0.72
  bounce       dead

lever latch button
  is a         box 20 by 20 by 10 mm, 5 g
  at           31 cm behind lever pivot, 31.5 cm up
  attached to  lever latch stem
  friction     0.72
  bounce       dead

-- Split rails leave a clear central opening for ball1
-- and for the lever's rising end.

left slide rail
  is a      box 100 by 2.5 by 2 cm
  at        20 cm behind lever pivot, 7.5 cm to the left, 49 cm up
  friction  0.72
  bounce    dead

right slide rail
  is a      box 100 by 2.5 by 2 cm
  at        20 cm behind lever pivot, 7.5 cm to the right, 49 cm up
  friction  0.72
  bounce    dead

left slide guide
  is a      box 100 by 2 by 8 cm
  at        20 cm behind lever pivot, 11 cm to the left, 54 cm up
  friction  0.72
  bounce    dead

right slide guide
  is a      box 100 by 2 by 8 cm
  at        20 cm behind lever pivot, 11 cm to the right, 54 cm up
  friction  0.72
  bounce    dead

left upper guide
  is a      box 67 by 2.5 by 2 cm
  at        9.5 cm behind lever pivot, 7.5 cm to the left, 61.2 cm up
  friction  0.72
  bounce    dead

right upper guide
  is a      box 67 by 2.5 by 2 cm
  at        9.5 cm behind lever pivot, 7.5 cm to the right, 61.2 cm up
  friction  0.72
  bounce    dead

cart1
  is a      box 22 by 18 by 10 cm, 0.50 kg
  moves     freely
  at        11 cm beyond lever pivot, 55 cm up
  friction  0.72
  bounce    dead

domino pedestal
  is a      box 12 by 12 by 2 cm
  at        46 cm behind lever pivot, 49 cm up
  friction  0.72
  bounce    dead

-- Cart-to-domino face clearance is 42 cm.
domino1
  is a      box 8 by 4 by 24 cm, 0.25 kg
  moves     freely
  on        domino pedestal, 46 cm behind lever pivot
  friction  0.72
  bounce    dead

ramp high end
  is a      point
  at        62.2899 cm behind lever pivot, 49.2020 cm up

ramp low end
  is a      point
  at        156.2592 cm behind lever pivot, 15 cm up

ramp1
  is a       ramp
  high end   ramp high end
  low end    ramp low end
  width      30 cm
  thickness  4 cm
  friction   0.72, spinning 0.005, rolling 0.002
  bounce     dead
  colour     wood

ball2 retaining curb
  is a      box 1.2 by 10 by 3.4 cm
  at        68.2 cm behind lever pivot, 50.6 cm up
  friction  0.72
  bounce    dead

-- Ball2 and domino1 have an 18 cm horizontal centre spacing.
ball2
  is a      sphere 10 cm across, 0.20 kg
  moves     freely
  rolls
  at        64 cm behind lever pivot, 55.779 cm up
  friction  0.72, spinning 0.005, rolling 0.002
  bounce    dead

-- The incoming panel face is 10 cm beyond the ramp endpoint.
door1
  is a           box 4 by 32 by 42 cm, 0.45 kg
  at             168.2592 cm behind lever pivot, 23 cm up
  turns on       door hinge, about z, at its left side
  swings         from -70° to 0°
  starts turned  0°
  spring         5 N·m/rad toward -70°
  damping        0.04 N·m·s/rad
  friction       0.72
  bounce         dead
  colour         wood

-- A second latch holds the door's spring.
-- Its rear support just touches the panel.
-- Its thin release plate just touches the incoming face.

door latch pivot
  is a      point
  at        18 cm beyond door1, 10 cm to the right, 46 cm up

door latch rear top
  is a      point
  at        2.5 cm behind door1, 16 cm to the right, 46 cm up

door latch rear foot
  is a      point
  at        2.5 cm behind door1, 16 cm to the right, 20 cm up

door latch trigger top
  is a      point
  at        2.005 cm beyond door1, 8 cm to the left, 46 cm up

door latch trigger bottom
  is a      point
  at        2.005 cm beyond door1, 8 cm to the left, 20 cm up

door latch release centre
  is a      point
  at        2.005 cm beyond door1, 20 cm up

door latch arm
  is a           rod 6 mm thick, from door latch pivot to door latch rear top
  weighs         20 g
  turns on       door latch hinge, about z, at door latch pivot
  swings         from 0° to 90°
  starts turned  0°
  spring         0.5 N·m/rad toward 0°
  damping        0.04 N·m·s/rad
  friction       0.72
  bounce         dead

door latch rear column
  is a         rod 6 mm thick, from door latch rear top to door latch rear foot
  weighs       5 g
  attached to  door latch arm
  friction     0.72
  bounce       dead

door latch support
  is a         box 10 by 2 by 60 mm, 5 g
  at           2.5 cm behind door1, 16 cm to the right, 20 cm up
  attached to  door latch arm
  friction     0.72
  bounce       dead

door latch trigger beam
  is a         rod 6 mm thick, from door latch pivot to door latch trigger top
  weighs       5 g
  attached to  door latch arm
  friction     0.72
  bounce       dead

door latch trigger column
  is a         rod 0.05 mm thick, from door latch trigger top to door latch trigger bottom
  weighs       0.01 g
  attached to  door latch arm
  friction     0.72
  bounce       dead

door latch trigger link
  is a         rod 0.05 mm thick, from door latch trigger bottom to door latch release centre
  weighs       0.01 g
  attached to  door latch arm
  friction     0.72
  bounce       dead

door latch release plate
  is a         box 0.1 by 20 by 60 mm, 3 g
  at           2.005 cm beyond door1, 20 cm up
  attached to  door latch arm
  friction     0.72
  bounce       dead

pendulum pivot
  is a      point
  at        199.3 cm behind lever pivot, 6.2 cm to the left, 68 cm up

pendulum1
  is a           box 3 by 3 by 50 cm, 0.35 kg
  at             25 cm below pendulum pivot, 199.3 cm behind lever pivot, 6.2 cm to the left
  turns on       pendulum hinge, about y, at pendulum pivot
  swings         from 0° to 38°
  starts turned  0°
  damping        0.04 N·m·s/rad
  friction       0.72
  bounce         dead
  colour         wood

block pedestal
  is a      box 30 by 30 by 2 cm
  at        237.2651 cm behind lever pivot, 6.2 cm to the left, 22.52 cm up
  friction  0.72
  bounce    dead

block1
  is a      cube 12 cm, 0.35 kg
  moves     freely
  on        block pedestal, 237.2651 cm behind lever pivot, 6.2 cm to the left
  friction  0.72
  bounce    dead

expect
  ball1 drops through ring1
  ball1 touches lever1
  lever1 touches cart1
  lever1 reaches its lower stop
  cart1 touches domino1
  domino1 touches ball2
  ball2 touches ramp1
  ball2 touches door1
  door1 touches pendulum1
  door1 reaches its lower stop
  pendulum1 touches block1
```