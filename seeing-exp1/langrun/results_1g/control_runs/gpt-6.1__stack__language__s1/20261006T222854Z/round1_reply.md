The stack stands until the pusher hits `block1` at 0.83 s. The bottom block shifts about 12 cm, and the upper blocks rock slightly, but they settle back into an upright stack. **The world does not meet the brief: the stack never topples.**

This revision uses a heavier, faster pusher to displace the bottom block farther and remove support from the blocks above it.

```world
world  five blocks toppled by a rolling pusher

floor
  size      12 m
  friction  0.45, spinning 0.005, rolling 0.001

block
  is a      cube 20 cm, 500 g
  colour    wood
  friction  0.45, spinning 0.005, rolling 0.001
  bounce    dead
  moves     freely
  stacked   5 high
  stands    on floor, 1.8 m along

pusher
  is a      sphere 8 cm radius, 10 kg
  colour    orange
  friction  0.45, spinning 0.005, rolling 0.001
  bounce    dead
  rolls
  moves     freely
  rests     on floor, 0 m along
  launched  3 m/s along
  spins     37.5 rad/s about y

expect
  pusher touches block1
```

```json
{
  "what_happens": "The pusher hits the bottom block at 0.83 s and shifts it about 12 cm. The upper blocks rock slightly, then settle back into an upright five-block stack.",
  "works": false,
  "problem": "The push does not displace the bottom block enough to topple the stack."
}
```

---
thinking (summarized):

**Evaluating friction parameters**

I'm thinking about the friction of cubes, specifically comparing a .45 floor to the original versions that lower resistance. However, if the tower interfriction is at .45, it seems to make the upper part accelerate less safely. I’m wondering about the mechanics when a block cube is on a .45 floor: it seems a brief push on the bottom could cause the top to slip or topple, but it’s hard to conceptualize how that would work coherently.