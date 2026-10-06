The hinge name `pendulum hinge` became `pendulum_hinge`, which seems to clash with a joint name the compiler derives for the thing named `pendulum`. This is my best guess at the cause. I've renamed the hinge to `swing`, and nothing else changes.

```parts
part low cup
  needs  length
  needs  width
  needs  walls
  needs  lip height
  needs  wall thickness, else 1 cm
  needs  base thickness, else 2 mm

  base
    is a  box length by width by base thickness
    on    floor
  near wall
    is a  box wall thickness by width by lip height
    on    floor, centred on base's near end
  far wall
    is a    box wall thickness by width by walls
    on      floor, centred on base's far end
    bounce  dead
  left wall
    is a    box length by wall thickness by walls
    on      floor, centred on base's left side
    bounce  dead
  right wall
    is a    box length by wall thickness by walls
    on      floor, centred on base's right side
    bounce  dead
```

```world
world  pendulum knocks a ball into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.001

ball
  is a      sphere 5 cm radius, 100 g
  rolls
  friction  0.8, spinning 0.005, rolling 0.001
  colour    orange
  moves     freely
  rests     on floor, 1 m along

pivot
  is a  point
  at    9.5 cm behind ball, 56 cm up

-- the bob: hangs 50 cm below the pivot, centre 6 cm up, 5.5 mm short of the ball
pendulum
  is a           sphere 4 cm radius, 400 g
  colour         grey
  50 cm below pivot, 9.5 cm behind ball
  turns on       swing, about y, at pivot
  starts turned  45°

pendulum rod
  is a         rod 1 cm thick, from pivot to pendulum's top
  weighs       20 g
  colour       dark grey
  attached to  pendulum

stand beam
  is a    box 4 by 16 by 4 cm
  colour  wood
  at      9.5 cm behind ball, 12 cm to the left, level with pivot

stand post
  is a    box 4 by 4 by 58 cm
  colour  wood
  stands  on floor, 9.5 cm behind ball, 22 cm to the left

cup
  is a         low cup
  length       20 cm
  width        20 cm
  walls        10 cm
  lip height   1.5 cm
  its base 1 m beyond ball

expect
  ball touches pendulum
  ball comes to rest in cup
```

---
thinking (summarized):

I'm wondering if the duplicate joint name comes from the compiler auto-naming both the pendulum's hinge and the attached rod's connection the same way, since things moving together get merged into one body but something about the naming logic might be causing a collision.

To avoid guessing further, I'll just rename the hinge to something distinct like "swing" to sidestep any possible auto-naming convention clash.

