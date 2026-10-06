```world
world  rolling ball into a bucket

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

table
  is a      table
  surface   120 by 70 cm
  height    75 cm
  legs      6 cm
  friction  0.8, spinning 0.005, rolling 0.001
  colour    wood
  stands    on floor

edge
  is a      point
  centred on table.top's far end, level with table.top

bucket
  is an     open box
  length    40 cm
  width     40 cm
  walls     22 cm
  wall thickness  2 cm
  base thickness  2 cm
  friction  0.9, spinning 0.01, rolling 0.01
  bounce    dead
  colour    grey
  sits      on floor, 60 cm beyond edge

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  moves     freely
  friction  0.8, spinning 0.005, rolling 0.001
  bounce    dead
  colour    orange
  rests     on table.top, 30 cm behind table.top
  launched  1.6 m/s along
  spins     53.333 rad/s about y

expect
  ball touches table
  ball comes to rest in bucket
```

---
thinking (summarized):

**Analyzing rolling dynamics**

I'm thinking about the scenario where something lands, and there's a friction or bounce that affects how far it rolls. It sounds like it comes to rest after about 6 seconds, with a tiny movement of .004 in the bucket. I'm considering the table's roll, which is incredibly slight at .0001 or potentially .0. The ball has a maximum movement of .001, while the bucket can move up to .006. There’s a lot to unpack here!

**Ensuring table dimensions**

I need to make sure that the table's surface area of "120 by 70 cm" is accepted for the surface substitution, allowing for a 3 cm adjustment. I'm noting that the edge's point should be centered correctly and avoiding any unnecessary mention of the table's far end. I want to confirm that I'm referencing the right table top height. No need for extra details in this code—just keeping it straightforward!