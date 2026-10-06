**What happens in the run:**
- The stack stands until 0.49 s.
- The ball then hits block1 hard enough to knock it clean out from under the stack. Block1 flies about 0.9 m forward.
- Block2 falls onto its side.
- Block3 to block5 drop straight down about 16 cm.
- They land still stacked upright on top of the fallen block2.

The stack collapses downward rather than toppling. The hit is too violent: it pulls the base out instead of pushing it.

**The fix:**
- Go back to a gentler, pushing impact, near the speed that only shoved the stack in the second run.
- Keep the slippery block-to-block contacts, so block1 slides out from under block2 rather than dragging it along.
- Make the blocks thinner along the push, so a shorter slide leaves block2 hanging off block1's back edge.
- Block2 should then tip back and take the column over with it.

```json
{"what_happens": "The stack stands until 0.49 s. The ball then hits block1 hard enough to knock it out from under the stack, sending it about 0.9 m forward. Block2 falls on its side, and block3 to block5 drop straight down and stay stacked upright on it.", "works": false, "problem": "The hit is so violent that it knocks the bottom block out, so the upper blocks drop straight down and stay stacked instead of toppling."}
```

```world
world  stack toppled by a push at the bottom

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.0002

block
  is a      box 6 by 16 by 12 cm, 400 g
  colour    wood
  friction  0.25
  moves     freely
  stacked   5 high
  stands    on floor, 1.5 m along

pusher
  is a      sphere 5 cm radius, 3 kg
  colour    grey
  rolls
  bounce    dead
  friction  0.8, spinning 0.001, rolling 0.0002
  moves     freely
  rests     on floor, 20 cm along
  launched  1.6 m/s along
  spins     32 rad/s about y

expect
  pusher touches block1
  block5 touches floor
```

---
thinking (summarized):

This time block1 got knocked out cleanly, but block2 toppled onto its side while blocks 3-5 just dropped and stayed stacked upright on it instead of toppling. I need a sustained push rather than a sharp impact since a hard hit yanks the base out while a moderate one drags the whole stack together, likely due to the 0.7 block-to-block friction pulling blocks 2 and 3 along with it. I should aim for a moderate hit that tilts the base strongly forward without dragging the top blocks.

