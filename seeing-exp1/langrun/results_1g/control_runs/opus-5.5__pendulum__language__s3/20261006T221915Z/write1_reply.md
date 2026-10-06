Both errors came from writing `touches  nothing` with two spaces, which split it into a key and a value. It is a single flag line, written `touches nothing`, and it is now fixed on the stand arm and the stand post. Nothing else changed, and the world is still unsimulated.

```world
world  pendulum strikes ball into cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.0002

pivot
  is a  point
  at    55 cm up

pendulum
  is a           sphere 3 cm radius, 300 g
  bounce         lively
  colour         grey
  50 cm below pivot
  turns on       pendulum hinge, about y, at pivot
  starts turned  45°

pendulum rod
  is a         rod 1 cm thick, from pivot to pendulum's top
  weighs       20 g
  colour       wood
  attached to  pendulum

stand arm
  is a     box 4 by 20 by 4 cm
  touches nothing
  colour   dark grey
  level with pivot, 12 cm left of pivot

stand post
  is a     post 4 cm square, from floor to stand arm's top
  touches nothing
  colour   dark grey
  centred on stand arm's left side

ball
  is a      sphere 4 cm radius, 100 g
  rolls
  friction  0.8, spinning 0.005, rolling 0.0002
  colour    orange
  moves     freely
  rests     on floor, 7.2 cm beyond pivot

cup
  is an             open box
  length            24 cm
  width             24 cm
  walls             8 cm
  wall thickness    1 cm
  base thickness    5 mm
  near wall height  1.5 cm
  friction          0.8, spinning 0.005, rolling 0.002
  bounce            dead
  colour            wood
  its base 1 m beyond ball

expect
  ball touches pendulum
  ball comes to rest in cup
```

---
thinking (summarized):

I see the bug now—"touches nothing" with a double space is getting incorrectly split into key/value pairs instead of being treated as a single flag line. I need to fix the spacing in both spots.

