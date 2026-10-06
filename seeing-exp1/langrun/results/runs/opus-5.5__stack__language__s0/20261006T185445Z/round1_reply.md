**What happens:** The stack stands, but the push is too weak to topple it. The ball starts at 2 m/s and loses speed to sliding and rolling drag. It reaches `block1` at 1.29 s moving only about 0.7 m/s. It nudges the whole stack about 1 cm along, and the ball and blocks then sit still for the rest of the run. Nothing topples.

**Fix:** Send the ball much faster, already rolling (spin matched to its speed, so it doesn't lose speed to sliding), with less rolling drag. It then hits `block1` hard and knocks it out quickly. Raise the friction between the blocks so `block1` drags hard on `block2` as it shoots out. That should tip the upper column backward, so the stack topples rather than dropping flat.

```json
{"what_happens": "The stack stands while the ball rolls toward it, but the ball arrives at only about 0.7 m/s after losing speed to sliding and rolling drag; it nudges the whole stack about 1 cm along and everything comes to rest with the stack still standing.", "works": false, "problem": "The ball reaches block1 far too slowly to knock it out, so the stack is only shoved 1 cm and never topples."}
```

```world
world  stack of five knocked from below

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.001

block
  is a      cube 10 cm, 200 g
  friction  0.9, spinning 0.005, rolling 0.001
  colour    wood
  moves     freely
  stacked   5 high
  stands    on floor, 2 m along

-- the pusher: a heavy ball already rolling at the bottom block, hitting it below its centre
ball
  is a      sphere 4 cm radius, 1 kg
  rolls
  bounce    dead
  friction  0.8, spinning 0.005, rolling 0.001
  colour    orange
  moves     freely
  rests     on floor, 0.5 m along
  launched  4 m/s along
  spins     100 rad/s about y

expect
  ball touches block1
  block5 touches floor
```

---
thinking (summarized):

The ball lost too much speed to rolling friction and barely nudged the stack 1 cm, so that attempt failed. I need a harder hit—maybe starting the ball faster and closer, or switching to a pendulum setup with a heavy bob instead.

Trying 5 m/s from 1 m away: after rolling-friction decay it's still hitting around 3.4 m/s, which should transfer enough force to shoot block1 out while dragging the stack above via friction, possibly tilting it before it drops.

I'm weighing whether that drop topples the stack onto the still-rolling ball (likely collapse) or whether the stack just settles flat and stays standing, with the ball continuing on into block2 at reduced speed after the first impact.

Checking the timing shows the ball may actually pass under block2 before the stack even lands, which is risky for the setup. I'm now considering an alternative: a slow-moving pusher that drags block1 out gradually via friction with block2, tipping the stack only if the inertial torque from the drag exceeds gravity's restoring torque.

Trying a different approach with a heavier pusher box driving block1 at moderate speed still leads to the same outcome: block1 slides out in a fraction of a second and the stack drops. It seems the tall stack dropping with any angular kick will likely topple, especially since friction between block2 and block1 as block1 exits pulls block2's base forward too.

That gives angular acceleration around 124 rad/s², so over 0.05 seconds the stack picks up roughly 6 rad/s — plenty to topple, confirming even a rough estimate works. I also check that the ball's height clears block1 without clipping block2, which it does given the gap. Now I'm settling on launch parameters: a 1 kg ball starting 1.2 m out, moving at 4 m/s with slight rolling friction, and matching spin to rolling velocity so it doesn't slip early.

Working out the cross product confirms spin should be +100 rad/s about the y-axis for a 4 m/s roll with the ball's radius, which keeps contact velocity at zero. By the time it reaches the target at roughly 0.2-0.37 seconds depending on starting distance, it's still moving near 3.9 m/s, which is plenty. I'll set block friction to 0.9 and finalize the start position around 0.5 m along the track.

