```world
world  door swings shut and stays shut

floor
  size      4 m
  friction  0.8, spinning 0.005, rolling 0.002

frame
  is a      box 8 by 8 by 214 cm
  stands    on floor, 12 cm to the right
  colour    dark grey

door
  is a           box 4 by 90 by 200 cm, 10 kg
  raised         2 cm
  8 cm outside frame's left side
  colour         wood
  turns on       hinge, about z, at its right side
  swings         from 0° to 110°
  spring         40 N·m/rad toward -5°
  damping        22 N·m·s/rad
  starts turned  85°

expect
  door reaches its lower stop
```

---
thinking (summarized):

**Defining hinge mechanics**

I’m considering whether to define the hinge axis z at the right side and include the starting angle. It seems clear that the angle range should be positive, specifically swinging from 0° to 110° actual. For the spring, I think a value of 40 N·m/rad toward -5° would work, and I’m wondering if I can use the unicode for minus. Typically, the positive spring reference is accepted, so I’ll keep it straightforward without extra commentary.