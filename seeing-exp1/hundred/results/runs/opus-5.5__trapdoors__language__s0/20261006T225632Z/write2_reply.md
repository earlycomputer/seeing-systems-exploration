Both hoops now place their rim with absolute offsets instead of `at <point>`. Hoop1's rim is at 0 cm along, 0 cm left; hoop2's is at 13 cm along, 45 cm left. Their heights still come from `rim height`.

```world
world  two trapdoor relay

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

hoop1 spot
  is a  point
  at    0 cm along, 0 cm to the left, 245 cm up

hoop1
  is a        hoop
  rim height  245 cm
  its rim 0 cm along, 0 cm to the left

ball1
  is a      sphere 6 cm radius, 1 kg
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  at        0 cm along, 0 cm to the left, 80 cm above hoop1 spot

flap1 pivot
  is a  point
  at    30 cm along, 20 cm to the left, 194 cm up

flap1
  is a      box 80 by 70 by 2 cm, 150 g
  colour    wood
  friction  0.5
  its far end at flap1 pivot, level with flap1 pivot, 20 cm to the left
  turns on  flap1 hinge, about y, at flap1 pivot
  swings    from -45° to 0°
  spring    0.4 N·m/rad toward 330°
  damping   0.02 N·m·s/rad

block
  is a      cube 8 cm, 200 g
  colour    grey
  friction  0.5
  moves     freely
  on flap1, 72 cm behind flap1 pivot, 45 cm to the left

hoop2
  is a        hoop
  rim height  45 cm
  its rim 13 cm along, 45 cm to the left

flap2 pivot
  is a  point
  at    28 cm along, 45 cm to the left, 104 cm up

flap2
  is a      box 80 by 20 by 2 cm, 150 g
  colour    wood
  friction  0.5
  its far end at flap2 pivot, level with flap2 pivot, 45 cm to the left
  turns on  flap2 hinge, about y, at flap2 pivot
  swings    from -45° to 0°
  spring    0.18 N·m/rad toward 330°
  damping   0.02 N·m·s/rad

ball2
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.01
  colour    white
  moves     freely
  on flap2, 15 cm behind flap2 pivot, 45 cm to the left

cup
  is a      open box
  length    30 cm
  width     30 cm
  walls     12 cm
  colour    wood
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.01
  on floor, 13 cm along, 45 cm to the left

expect
  ball1 drops through hoop1
  ball1 touches flap1
  flap1 reaches its lower stop
  block touches flap2
  flap2 reaches its lower stop
  ball2 drops through hoop2
  ball2 comes to rest in cup
```

---
thinking (summarized):

That positioning syntax isn't valid — "at hoop1 spot" doesn't work as a clause after "its rim." I need to find the correct way to express relative offsets between the two hoops' rim positions.

