Positions can't refer to the stack's copies by name, so the ball is now placed relative to `block`. The offset fixes only the along direction, so the result is the same.

```world
world  toppling stack

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

block
  is a      box 8 by 8 by 16 cm, 300 g
  friction  0.6, spinning 0.005, rolling 0.002
  colour    wood
  moves     freely
  stacked   5 high
  stands    on floor, 1 m along

ball
  is a      sphere 6 cm radius, 2 kg
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.002
  colour    orange
  moves     freely
  rests     on floor, 1.2 m behind block
  launched  1.2 m/s along
  spins     20 rad/s about y

expect
  ball touches block1
```

The `expect` line still names `block1`. If the checker rejects copy names there too, it will need changing to `block`. Everything else is unchanged and still unrun. The ball should hit the bottom block about 0.9 s in, but the stack might drop rather than visibly topple.

---
thinking (summarized):

Copies can't be referenced by name in positions, so I should use "block" to mean the original, and since the offset is only along one direction, I can just phrase it as "on floor, 1.2 m behind block."

