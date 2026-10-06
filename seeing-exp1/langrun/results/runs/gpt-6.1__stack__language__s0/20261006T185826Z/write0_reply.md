```world
world  five blocks topple after a push

floor
  size      8 m
  friction  0.35, spinning 0.005, rolling 0.002

block
  is a      cube 20 cm, 1 kg
  moves     freely
  stacked   5 high
  friction  0.65, spinning 0.005, rolling 0.002
  bounce    dead
  colour    wood
  stands    on floor, 1.6 m along

pusher
  is a      box 20 by 30 by 12 cm, 10 kg
  moves     freely
  friction  0.05, spinning 0.005, rolling 0.002
  bounce    dead
  colour    orange
  rests     on floor, 0 m along
  launched  4 m/s along

expect
  pusher touches block1
```

---
thinking (summarized):

**Evaluating block mechanics**

I'm thinking about how the contact includes the pushes and rotations of block1, with some concern about the bottom block's raising when near the end. There seems to be a standard robust set of topple parameters. I wonder if I should ensure it's standing for at least 0.5 seconds. If I choose a pusher gap of 1m and a speed of 3m/s, with floor friction at 0.15, I’ll need to consider how all that connects to the stopping distance.