The parser didn't accept a negative angle there, so the spring now pulls toward 0° exactly. With the stop also at 0°, the door settles shut and the spring has nothing left to push it back open.

```world
world  a door swings shut and stays shut

floor
  friction  0.8, spinning 0.005, rolling 0.002

frame
  is a    box 8 by 8 by 214 cm
  stands  on floor, 1 m along
  colour  grey

door
  is a           box 4 by 80 by 200 cm, 20 kg
  colour         wood
  raised         2 cm
  8 cm outside frame's left side
  turns on       hinge, about z, at its right side
  swings         from 0° to 90°
  spring         20 N·m/rad toward 0°
  damping        15 N·m·s/rad
  starts turned  80°

expect
  door reaches its lower stop
```

---
thinking (summarized):

I should avoid the unicode minus sign and negative angles altogether—simplest to just spring the door toward 0° so it rests shut at the stop.

