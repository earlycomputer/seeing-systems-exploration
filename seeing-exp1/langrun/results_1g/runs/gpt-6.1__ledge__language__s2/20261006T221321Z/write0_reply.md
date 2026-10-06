```world
world  rolling ball into a bucket

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

table
  is a      table
  surface   120 by 80 cm
  height    80 cm
  legs      6 cm
  friction  0.8, spinning 0, rolling 0
  colour    wood
  on floor, 0 m along, 0 m to the left

-- The table's far edge is at 60 cm along.
-- The bucket's centre is another 60 cm beyond that edge.
bucket
  is an           open box
  length          40 cm
  width           40 cm
  walls           20 cm
  wall thickness  2 cm
  base thickness  2 cm
  friction        0.8, spinning 0.01, rolling 0.01
  bounce          dead
  colour          grey
  on floor, 1.2 m along, 0 m to the left

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  friction  0.8, spinning 0, rolling 0
  bounce    dead
  colour    orange
  moves     freely
  on table.top, 0 m along, 0 m to the left
  launched  1.5 m/s along
  spins     50 rad/s about y

expect
  ball touches table
  ball touches bucket
  ball comes to rest in bucket
```

---
thinking (summarized):

**Analyzing rolling friction and torque**

I'm working through the topic of rolling friction, torque, and how they relate in various scenarios. The equations start to take shape; for example, the acceleration derived from friction coefficients like mu_r leads to specific values. 

There are different friction values for table surfaces with rolling and sliding cases, aiming for an effortless roll. I also think about the bucket's role in moderating the ball's impact and how its design affects interactions with walls. I'm focused on ensuring stability and understanding the physics at play.

**Determining bucket placement**

I'm figuring out how to position the bucket, specifically placing it 60 cm beyond the far end of the table. I need to clarify if this placement affects the stability or support of the bucket since there's an offset clause involved. I'll look for examples that only reference being beyond the rim. It’s about ensuring the setup is sound and functional for whatever activity is taking place, so stability is key here in my calculations.

**Clarifying table position**

I need to avoid introducing complexities, so I'll use simple language like "on floor, 60 cm beyond the table's far end" to stay clear. The position function should understand it well with scalar offsets, like using x1.2 m. The table's dimensions are 120 by 80 cm, and its height is 80 cm while standing on the floor. Therefore, I want to ensure it’s clearly positioned at the bottom, which could be at x0 according to the default settings.

**Setting positions and parameters**

I need to define the ball's position with appropriate syntax, using “on table.top, 0 m along, 0 m to the left” to set it on top center. However, I realize that direction duplication may cause confusion, so I'll keep it simple with a fixed position. The table's height is 0.8 m, and for the ball's position, if it's 30 cm behind the table, it should have an initial x of -0.3, resulting in a 90 cm roll. I'll also consider rolling and spinning friction, with parameters like friction at 0.7 and rolling at 0.01 for stability.