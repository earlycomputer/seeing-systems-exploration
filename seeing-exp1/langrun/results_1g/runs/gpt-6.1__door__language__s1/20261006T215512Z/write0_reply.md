```world
world  self-closing door

floor
  size      4 m
  friction  0.8, spinning 0.005, rolling 0.002

frame
  is a      box 8 by 8 by 214 cm
  stands    on floor, 12 cm to the right
  colour    grey

door
  is a      box 4 by 90 by 200 cm, 10 kg
  raised    2 cm
  8 cm outside frame's left side
  colour    wood
  turns on  hinge, about z, at its right side
  swings    from 0° to 100°
  -- The spring presses against the closed stop after closing.
  spring    60 N·m/rad toward -5°
  damping   22 N·m·s/rad
  starts turned  75°

expect
  door reaches its lower stop
```

---
thinking (summarized):

**Explaining spring preload**

I’m considering spring preload settings. I've got an 85-second stay time and a spring rate of 60 with a damping of 22. It's interesting that I don't need a latch, but preload seems to be adequate for indefinite stability at zero. I can explain more about how the spring preload presses against the closed lower stop, which is a crucial aspect in ensuring it functions properly.