Here is the complete world. All heights in `up` clauses are centre heights. The table, cart and weight run along y = 0. The ball, seesaw lip and cup sit 32 cm to the right, so the backward throw clears the table. The seesaw starts at its upper stop (6°, ball end down) and is driven to its lower stop at −45°.

I have not run it. Two risks remain:
- I assumed positive hinge angles about y swing the bob back (−x) and lower the ball end of the seesaw.
- I estimated the ball's launch speed at about 2.55 m/s by hand. The cup only catches it between roughly 2.2 and 2.9 m/s.

```world
world  pendulum cart weight seesaw ball cup

floor
  size      6 m
  friction  0.5

-- the pendulum: bob centre released 0.6 m above its lowest point (length 1 m, cos 66.42° = 0.4)
pendulum pivot
  is a  point
  at    50 cm along, 171 cm up

pendulum
  is a           sphere 4 cm radius, 1 kg
  colour         grey
  at             50 cm along, 71 cm up
  turns on       pendulum hinge, about y, at pendulum pivot
  starts turned  66.42°

pendulum rod
  is a         rod 1 cm thick, from pendulum pivot to pendulum's top
  weighs       50 g
  attached to  pendulum
  touches nothing
  colour       dark grey

-- the table the cart slides along
track
  is a      box 70 by 30 by 65 cm
  friction  0.1
  colour    wood
  on floor, 65 cm along

cart
  is a      box 16 by 14 by 12 cm, 500 g
  friction  0.1
  colour    orange
  moves     freely
  on track, 63 cm along

-- a low ledge at the table's far edge: the cart stops on it, the weight slides off it
ledge
  is a      box 6 by 14 by 4 cm
  friction  0.1
  colour    grey
  on track, 97 cm along

weight
  is a      cube 10 cm, 1 kg
  friction  0.1
  colour    dark grey
  moves     freely
  on ledge, 96 cm along

-- the seesaw: pivot 42 cm up, starts at its upper stop (ball end down)
seesaw pivot
  is a  point
  at    153 cm along, 16 cm to the right, 42 cm up

seesaw stand top
  is a  point
  at    153 cm along, 16 cm to the right, 32 cm up

seesaw stand
  is a    post 6 cm square, from floor to seesaw stand top
  colour  grey

seesaw
  is a           box 100 by 48 by 2 cm, 850 g
  friction       0.6
  colour         wood
  level with seesaw pivot, 153 cm along, 16 cm to the right
  turns on       seesaw hinge, about y, at seesaw pivot
  swings         from −45° to 6°
  starts turned  6°

seesaw lip
  is a         box 2 by 14 by 4 cm, 30 g
  colour       wood
  on seesaw, at seesaw's far end, 32 cm to the right
  attached to  seesaw

-- the ball rests against the lip on the tilted seesaw (position worked out for the 6° start)
ball
  is a      sphere 3 cm radius, 50 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    white
  moves     freely
  at        198 cm along, 32 cm to the right, 41.5 cm up

-- the cup beside the table, where the backward throw lands
cup
  is an     open box
  length    56 cm
  width     26 cm
  walls     15 cm
  friction  0.8, spinning 0.01, rolling 0.004
  bounce    dead
  colour    glass
  on floor, 72 cm along, 32 cm to the right

expect
  pendulum touches cart
  cart touches weight
  weight touches seesaw
  seesaw reaches its lower stop
  ball comes to rest in cup
```

---
thinking (summarized):

Now I'll flesh out the world based on the design I've settled on.

