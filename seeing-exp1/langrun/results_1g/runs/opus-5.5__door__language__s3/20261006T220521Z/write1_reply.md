The jamb's `post ... to 2.15 m up` failed because a post's top must be a named point, not a bare height. I've made the jamb a plain box standing on the floor instead.

```world
world  a door swings shut and stays shut

floor
  friction  0.8, spinning 0.005, rolling 0.002

-- a jamb beside the hinge side, for looks only
jamb
  is a      box 8 by 8 by 215 cm
  on floor, 1 m along, 46 cm to the right
  touches nothing
  colour    grey

door
  is a           box 4 by 80 by 200 cm, 20 kg
  raised         1 cm, 1 m along
  colour         wood
  turns on       hinge, about z, at its right side
  swings         from 0° to 110°
  spring         20 N·m/rad toward −5°
  damping        12 N·m·s/rad
  starts turned  80°

expect
  door reaches its lower stop
```

---
thinking (summarized):

I'm working out the jamb geometry instead — modeling it as an 8x8x215 cm box placed on the floor, positioned 1 m along and 46 cm to the right, then checking how it aligns with the door's extent from -42 to -50 cm.

