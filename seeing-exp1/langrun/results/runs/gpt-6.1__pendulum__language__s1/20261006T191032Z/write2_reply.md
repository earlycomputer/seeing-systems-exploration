```world
world  pendulum rolls a ball into a cup

floor
  size      4 m
  friction  0.6, spinning 0.001, rolling 0.0005

ball
  is a      sphere 3 cm radius, 80 g
  moves     freely
  rolls
  bounce    dead
  friction  0.6, spinning 0.001, rolling 0.0005
  rests     on floor, 0 m along
  colour    orange

pivot
  is a  point
  at    6 cm behind ball, 63 cm up

pendulum tip
  is a  point
  at    6 cm behind ball, 3 cm up

pendulum
  is a           rod 6 cm thick, from pivot to pendulum tip
  weighs         350 g
  turns on       swing axis, about y, at pivot
  swings         from -70° to 70°
  starts turned  35°
  damping        0.005 N·m·s/rad
  bounce         dead
  colour         grey

cup
  is an             open box
  length            24 cm
  width             20 cm
  walls             9 cm
  wall thickness    5 mm
  base thickness    2 mm
  near wall height  2 mm
  sits              on floor, 1 m beyond ball

expect
  ball touches pendulum
  ball comes to rest in cup
```

---
thinking (summarized):

**Exploring pendulum design**

I’m considering the idea of avoiding an attached rod and making a primitive pendulum with a hinged bob instead. Duplicating this could lead to interesting designs. I think using a long rod with a weighted capsule makes sense. The rod can be 6 cm thick, and the mass could be set at 250g. The pendulum tip is positioned behind the ball, measuring 6cm and 3cm high, allowing for a unique gravity-driven mechanism.