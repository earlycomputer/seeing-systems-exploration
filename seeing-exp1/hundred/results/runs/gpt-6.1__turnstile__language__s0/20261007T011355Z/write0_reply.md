The latch is a loose shelf constrained by fixed sliding guides. This gravity-driven design has not been run in MuJoCo here.

```world
world  ramp rotor latch release

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

-- The ramp is 2 m long; its midpoint is 1 m up from its foot.

ramp foot
  is a  point
  at    0 m along, 40 cm to the right, 60 cm up

ramp high end
  is a  point
  at    1.6 m behind ramp foot, 40 cm to the right, 1.2 m above ramp foot

ramp
  is a      plank from ramp high end to ramp foot, 26 cm wide, 4 cm thick
  friction  0.6, spinning 0.001, rolling 0.001
  colour    wood

ball1 runway
  is a      box 90 by 28 by 4 cm
  raised    56 cm, 25 cm along, 40 cm to the right
  friction  0.6, spinning 0.001, rolling 0.001
  colour    wood

ball1
  is a      sphere 8 cm radius, 800 g
  moves     freely
  rolls
  bounce    dead
  friction  0.6, spinning 0.001, rolling 0.001
  colour    orange
  on ramp, 1 m from the top

rotor pivot
  is a  point
  at    35 cm along, 68 cm up

-- The lower arm receives ball1; the opposite arm sweeps toward ball2.

rotor
  is a      box 6 by 110 by 12 cm, 250 g
  at        35 cm along, 68 cm up
  turns on  rotor hinge, about z, at rotor pivot
  swings    from 0° to 80°
  damping   0.01 N·m·s/rad
  armature  0.003 kg·m²
  bounce    dead
  friction  0.2
  colour    grey

ball2 runway
  is a      box 180 by 34 by 4 cm
  raised    56 cm, 35 cm behind ramp foot, 40 cm to the left
  friction  0.03, spinning 0.001, rolling 0.001
  colour    wood

ball2
  is a      sphere 8 cm radius, 400 g
  moves     freely
  rolls
  bounce    dead
  friction  0.3, spinning 0.001, rolling 0.001
  colour    white
  on ball2 runway, 11.1 cm behind rotor

-- Two runners support the shelf without obstructing the payload's drop.

latch lower runner
  is a      box 180 by 8 by 4 cm
  raised    56 cm, 35 cm behind ramp foot, 16 cm to the right
  friction  0.01
  colour    grey

latch lower guide
  is a      box 120 by 2 by 16 cm
  raised    58 cm, 65 cm behind ramp foot, 21.4 cm to the right
  friction  0.01
  colour    grey

latch upper guide
  is a      box 120 by 2 by 16 cm
  raised    58 cm, 65 cm behind ramp foot, 57.4 cm to the left
  friction  0.01
  colour    grey

latch lower keeper
  is a      box 120 by 3 by 2 cm
  raised    72.4 cm, 65 cm behind ramp foot, 18.5 cm to the right
  friction  0.01
  colour    grey

latch upper keeper
  is a      box 120 by 3 by 2 cm
  raised    72.4 cm, 65 cm behind ramp foot, 54.5 cm to the left
  friction  0.01
  colour    grey

latch stop
  is a      box 12 by 76 by 12 cm
  raised    60 cm, 1.31 m behind ramp foot, 18 cm to the left
  bounce    dead
  friction  0.01
  colour    dark grey

latch
  is a      box 40 by 76 by 12 cm, 120 g
  moves     freely
  bounce    dead
  friction  0.01, spinning 0.001, rolling 0.001
  colour    orange
  raised    60 cm, 28 cm behind ramp foot, 18 cm to the left

block
  is a      cube 14 cm, 250 g
  moves     freely
  bounce    dead
  friction  0.01
  colour    wood
  on latch, 4 cm behind latch, 5 cm to the left

ring
  is a    ring 46 cm across, 8 mm thick
  at      39 cm up, centred over block
  colour  orange

box
  is an           open box
  length          64 cm
  width           64 cm
  walls           24 cm
  wall thickness  2 cm
  base thickness  2 cm
  bounce          dead
  friction        0.8, spinning 0.01, rolling 0.004
  colour          wood
  on floor, centred over ring

expect
  ball1 touches ramp
  ball1 touches rotor
  rotor touches ball2
  ball2 touches latch
  block drops through ring
  block comes to rest in box
```

---
thinking (summarized):

**Planning rotor interaction platform**

I'm looking to design a rotor interaction platform, aiming for a surface elevation of about 0.65. I want to choose a high point around -1.6 along one axis and 1.8 up; this positions it at about 2m. The ramp deck will need to be around 4 cm thick, with the top surface measuring roughly 0.616 or 0.625. It looks like the horizontal platform should align with the top at about 0.62.

**Evaluating latch and support requirements**

I'm considering that Ball2 has a speed of about 1 to 2 m/s, and the latch mass is 0.1 with a friction of around 0.03, which seems enough for sliding at 0.6. I need a rail platform that supports the latch while also ensuring the block can drop when the opening is accessed. There’s a lot to think about in balancing these elements effectively!

**Interpreting dimensions**

I’m trying to make sense of some measurements. It seems like I have dimensions for different objects, like a latch with its center at 0.66 height and some details on a block, which is a 0.14 cube with its center at 0.79. Additionally, there's a ring with specifics like a center at z=0.39, a diameter of 0.46, and a thickness of 0.008. I'm piecing it all together!

**Measuring ramp details**

I'm considering the ramp's measurement specifics. The ramp's length is 2 meters, and I note that it's indeed 1 meter up from the foot of the ramp to the midpoint. That's a nice detail to keep straight! Both the top and the foot are aligned, which is great. So, the ramp's total length is 2 meters with the ball positioned 1 meter up from the bottom. Everything seems to check out!