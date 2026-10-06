```world
world  self closing door

floor
  size      4 m
  friction  0.8, spinning 0.005, rolling 0.002

frame
  is a      box 8 by 8 by 214 cm
  stands    on floor, 12 cm to the right
  colour    grey

door
  is a           box 4 by 90 by 200 cm, 10 kg
  raised         2 cm
  8 cm outside frame's left side
  colour         wood
  turns on       hinge, about z, at its right side
  swings         from 0° to 100°
  spring         60 N·m/rad toward −5°
  damping        25 N·m·s/rad
  starts turned  80°

expect
  door reaches its lower stop
```

---
thinking (summarized):

**Considering spring mechanics**

Okay, I'm thinking about providing a spring with parameters like a spring constant of 60, negative damping at 5, and a mass of 10. It seems I'm aiming for a near-critical velocity while looking for a smooth start given an initial setting of 80. I wonder if adding a shut-off mechanism would be beneficial for latching, even though it might not be necessary with the springs. Lots to consider here!