```world
world  pendulum sends four balls into a box

floor
  size      5 m
  friction  0.8, spinning 0.01, rolling 0.01

rail
  is a      box 110 by 16 by 10 cm
  on        floor, 40 cm along
  friction  0.002, spinning 0.00001, rolling 0.00001
  colour    grey

left guide
  is a      box 110 by 2 by 10 cm
  on        rail, at rail's left side
  friction  0.002, spinning 0.00001, rolling 0.00001
  colour    grey

right guide
  is a      box 110 by 2 by 10 cm
  on        rail, at rail's right side
  friction  0.002, spinning 0.00001, rolling 0.00001
  colour    grey

pivot
  is a      point
  at        0 m along, 0 m to the left, 1.14 m up

support post
  is a      box 6 by 6 by 120 cm
  on        floor, 25 cm right of pivot
  colour    dark grey

support beam
  is a      box 6 by 30 by 4 cm
  level with pivot, 12 cm right of pivot
  colour    dark grey

-- A 1 m pendulum starting at 60 degrees has a release height
-- of 1 m × (1 − cos 60 degrees) = 0.5 m above its lowest point.
pendulum
  is a           sphere 4 cm radius, 200 g
  1 m below pivot
  turns on       pendulum hinge, about y, at pivot
  swings         from -80° to 60°
  starts turned  60°
  damping        0 N·m·s/rad
  bounce         lively
  friction       0.002, spinning 0.00001, rolling 0.00001
  colour         orange

pendulum rod
  is a         rod 6 mm thick, from pivot to pendulum's top
  weighs       0.1 g
  attached to  pendulum
  touches nothing
  colour       grey

-- Equal balls, with centres spaced 0.15 m apart.
ball1
  is a      sphere 4 cm radius, 200 g
  moves     freely
  rolls
  bounce    lively
  friction  0.002, spinning 0.00001, rolling 0.00001
  on        rail, 8 cm beyond pivot
  colour    white

ball2
  is a      sphere 4 cm radius, 200 g
  moves     freely
  rolls
  bounce    lively
  friction  0.002, spinning 0.00001, rolling 0.00001
  on        rail, 15 cm beyond ball1
  colour    white

ball3
  is a      sphere 4 cm radius, 200 g
  moves     freely
  rolls
  bounce    lively
  friction  0.002, spinning 0.00001, rolling 0.00001
  on        rail, 15 cm beyond ball2
  colour    white

ball4
  is a      sphere 4 cm radius, 200 g
  moves     freely
  rolls
  bounce    lively
  friction  0.002, spinning 0.00001, rolling 0.00001
  on        rail, 15 cm beyond ball3
  colour    orange

-- The rail ends at the low entrance wall; the ball drops inside.
box
  is an             open box
  length            60 cm
  width             30 cm
  walls             40 cm
  wall thickness    2 cm
  base thickness    2 cm
  near wall height  2 cm
  on                floor, 1.25 m along
  bounce            dead
  friction          0.9, spinning 0.02, rolling 0.02
  colour            wood

expect
  pendulum touches ball1
  ball1 touches ball2
  ball2 touches ball3
  ball3 touches ball4
  ball4 comes to rest in box
```

---
thinking (summarized):

**Evaluating simulation settings**

I’m examining how the dead box floor affects the sliding and rolling of objects. It seems that as the box is adjusted, the transition from sliding to rolling happens quickly when the conditions are set. I’m considering how to handle the bounce settings to optimize the ball's liveliness during this process. I need to make sure the restitution settings are combined well to control the bounce height and achieve the desired realism in the simulation.

**Evaluating rail geometry and support details**

I'm considering whether the right rail should be spaced flush. The placement of the guide rail on the left means I've calculated the inner edge correctly, leaving a gap I find acceptable. I'm also checking if the pendulum shaft intersects appropriately and ensuring no contact with the bob. There's some extra detail on the guides and whether to add a support post. I'll have to assess if support is really necessary for this setup.

**Defining blocks and components**

I'm realizing I haven't properly tested my tools or claimed any results. I should focus on defining the key components first, like the rail and the pivot. Maybe I can just provide a single block definition along with an optional comment that explains the height. It's essential to keep things straightforward and ensure everything is clear for anyone reviewing it. Let's streamline this process to make it easier to follow!