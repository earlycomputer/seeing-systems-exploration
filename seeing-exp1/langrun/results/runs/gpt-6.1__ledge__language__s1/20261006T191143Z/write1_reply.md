```world
world  rolling ball into a bucket

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

table
  is a     table
  surface  120 by 70 cm
  height   80 cm
  stands   on floor

table edge
  is a  point
  centred on table.top's far end

bucket
  is an           open box
  length          40 cm
  width           40 cm
  walls           30 cm
  wall thickness  2 cm
  base thickness  2 cm
  sits            on floor, 60 cm beyond table edge

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  moves     freely
  bounce    dead
  friction  0.8, spinning 0, rolling 0
  colour    orange
  rests     on table.top, 20 cm behind table
  launched  1.5 m/s along
  spins     50 rad/s about y

expect
  ball touches table
  ball comes to rest in bucket
```

---
thinking (summarized):

**Evaluating system flags**

I need to remove elements related to flags for color, bucket friction, and bounce that are unsupported. The error message indicates there’s an "on" position recognized without prefixes. It seems there were no issues previously on the lines, and the user has two entries, with the first one being unsupported, which might stop processing per block. I must ensure the bucket removes all material, and that the ball is set to a dead state to avoid conflicts. I'll also clarify positions using the "on floor" language.