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
  is a           box 4 by 90 by 200 cm, 12 kg
  raised         2 cm
  8 cm outside frame's left side
  colour         wood
  bounce         dead
  turns on       hinge, about z, at its right side
  swings         from 0° to 100°
  spring         40 N·m/rad toward −5°
  damping        20 N·m·s/rad
  starts turned  75°

expect
  door reaches its lower stop
```

---
thinking (summarized):

**Processing floor frame dimensions**

I’m working on framing that measures 8 by 214 cm, with a floor of 12 cm. It should be centered with some margins, and I need to ensure the door hinge is correctly positioned. I’m considering using a simple hinge post and panel that meets the brief. I have to double-check everything, especially since I can’t use any tools right now. The door should reach a lower stop without issue.