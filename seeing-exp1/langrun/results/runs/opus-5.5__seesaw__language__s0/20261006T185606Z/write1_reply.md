The checker didn't read the minus sign in `−20°`. To avoid a negative angle, I mirrored the setup instead: the ball now sits on the near end and the weight drops onto the far end. The hinge range becomes 0° to 20°. The ball's weight holds the seesaw level at 0°, and the impact drives it to 20°. The expectation now names the upper stop. As before, I haven't run this, and nothing in it checks the ball's 50 cm rise.

```world
world  seesaw throw

floor
  friction  0.8, spinning 0.005, rolling 0.002

pivot
  is a  point
  at    1 m along, 30 cm up

stand top
  is a  point
  at    1 m along, 24 cm up

stand
  is a    post 6 cm square, from floor to stand top
  colour  grey

seesaw
  is a      box 120 by 10 by 3 cm, 300 g
  at        1 m along, level with pivot
  turns on  seesaw hinge, about y, at pivot
  swings    from 0° to 20°
  colour    wood

ball
  is a      sphere 4 cm radius, 100 g
  friction  0.8, spinning 0.01, rolling 0.004
  moves     freely
  colour    orange
  rests     on seesaw, 50 cm behind pivot

weight
  is a      sphere 6 cm radius, 1 kg
  bounce    dead
  moves     freely
  colour    dark grey
  at        50 cm beyond pivot, 2 m up

expect
  weight touches seesaw
  seesaw reaches its upper stop
```

---
thinking (summarized):

Since the negative sign didn't parse, I should avoid negatives entirely by reorienting the setup: range 0° to 20°, with the weight on the far end and ball on the near end, so it naturally rests at 0° and tips positive toward 20° when the weight dominates.

So with the ball 50 cm behind the pivot and weight 50 cm beyond it, the seesaw now reaches its upper stop at 20° instead of a lower stop — I need to update the expected outcome accordingly to "reaches its upper stop."

