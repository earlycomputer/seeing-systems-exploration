A heavy ball rolls along the floor into the bottom block and knocks it out from under the stack. The blocks are taller than they are wide, so the four above lose their footing and topple. The stack stands untouched for about a second before the ball arrives.

```world
world  toppled stack

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

-- five tall blocks, block1 at the bottom, block5 on top
block
  is a      box 6 by 6 by 10 cm, 200 g
  friction  0.6
  colour    wood
  moves     freely
  stacked   5 high
  stands    on floor, 2 m along

-- the pusher: a heavy ball, launched along the floor at the bottom block
ball
  is a      sphere 4 cm radius, 1 kg
  rolls
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on floor, 0 m along
  launched  2.5 m/s along

expect
  ball touches block1
```

---
thinking (summarized):

I need a stack of five blocks that stays stable until something strikes the bottom block, like a tablecloth trick where the bottom gets yanked out and the stack above collapses or drops. I'm thinking of using a pendulum or sliding object in the scene that swings in to deliver that push after the stack has held still for a moment.

Working through the pendulum geometry, I realize positioning is ambiguous since I can't easily place the pivot relative to the stack, and the rotation direction depends on sign conventions I'm not fully certain about. A rolling ball launched toward the stack from a known distance feels like the more reliable and predictable approach, so I'll lean toward that instead.

For the ball, it'll slide briefly before friction induces rolling, reaching the stack after roughly half a second — maybe I place it farther away to extend the standing time. I'm weighing whether the impact should knock the bottom block out sideways while the top blocks drop and possibly stay partially stacked, versus wanting a clean topple where the whole stack falls over, which depends a lot on inter-block friction and how hard the ball strikes.

Thinking through the physics, a fast-sliding bottom block would drag on the block above via friction, rotating it backward relative to the impact direction, so if blocks are tall relative to their width (like 8-10 cm cubes stacked five high), the sudden shear should be more likely to make the whole thing tip over rather than just collapse straight down.

The impulse seems too small to really matter — the upper stack would just drop about 12 cm, and I'm unsure if that alone topples it. Maybe a slower, heavier push is more reliable: block1 slides a few centimeters while the stack above lags due to friction, then as block1 decelerates from floor friction the stack keeps moving and tips forward. Still uncertain, but this knock-out approach seems the most physically plausible path forward.

Estimating that a 4-block stack 40 cm tall would tip at around 8.5°, I'm treating the base impulse as acting like a push on a rod and computing the resulting angular velocity—roughly 2.4 rad/s—which over the fall time rotates the stack about 19°, enough that the blocks likely separate and topple rather than land cleanly.

The ball could also keep moving after hitting the first block and strike the second block as it falls, pushing it further—that seems acceptable to include. Now I'm settling on concrete object parameters: a 1 kg ball with 4 cm radius, and 200 g blocks sized 6×6×10 cm stacked five high, and I'm working out how to specify their positions and names (like "stacked 5 high" and whether "block" alone is a valid reference) so the scene description resolves unambiguously, probably by using absolute positions instead.

Aligning both objects at across 0 for simplicity, with block friction set to 0.6. Expecting the outcome to simply be "ball touches block1" without added complexity.

