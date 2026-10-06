```world
world  door swings shut and stays shut

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

frame
  is a      box 8 by 8 by 214 cm
  stands    on floor, 12 cm to the right
  colour    dark grey

door
  is a           box 4 by 90 by 200 cm, 12 kg
  raised         2 cm, 8 cm outside frame's left side
  colour         wood
  turns on       hinge, about z, at its right side
  swings         from 0° to 100°
  starts turned  75°
  -- Preload holds the door against its shut stop.
  spring         40 N·m/rad toward −5°
  damping        18 N·m·s/rad

expect
  door reaches its lower stop
```