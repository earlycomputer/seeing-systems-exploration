## What happened in the run

The five blocks stand still for the first second. At 1.01 s the 2 kg ball, now slowed to about 1 m/s, hits `block1`. The bottom block is pinned by the 1.2 kg on top of it and by floor friction, so it slides only 3 cm. The dead contact stops the ball almost at once. The upper blocks wobble by 3°, then everything settles. The stack is still standing upright at 6 s, so it never topples.

## Corrected world

The push needs far more momentum, and it must keep shoving rather than tap and stop.

- **Pusher:** the ball becomes 10 kg, launched at 2.5 m/s with matching spin, from 2.5 m back, so it still arrives after about a second. It keeps driving `block1` forward after impact.
- **Blocks:** block friction rises to 1.0, so the shove drags the base out from under the tall, narrow column and tips it over.

```world
world  toppling stack

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

block
  is a      box 8 by 8 by 16 cm, 300 g
  friction  1.0, spinning 0.005, rolling 0.002
  colour    wood
  moves     freely
  stacked   5 high
  stands    on floor, 1 m along

ball
  is a      sphere 6 cm radius, 10 kg
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.002
  colour    orange
  moves     freely
  rests     on floor, 2.5 m behind block
  launched  2.5 m/s along
  spins     41.7 rad/s about y

expect
  ball touches block1
```

This is still unrun. A hard enough shove might pull the bottom block cleanly out from under the others, so the column drops 16 cm and stays upright instead of tipping.

```json
{"what_happens": "The stack stands untouched for the first second. At 1.01 s the 2 kg ball, rolling at about 1 m/s, hits block1, pushes it only 3 cm and stops dead. The upper blocks wobble about 3 degrees and settle. All five blocks are still stacked upright at 6 s.", "works": false, "problem": "The push from the light, slow, dead-bouncing ball is far too weak to move the loaded bottom block, so the stack never topples."}
```

---
thinking (summarized):

The stack didn't topple since the ball's impact only moved block1 by 3 cm, likely because friction absorbed most of the momentum. I need a much stronger push with more mass or speed, so I'm calculating the friction forces holding block1 in place—both from the floor and from block2 resting on top.

Working through the math, block1 decelerates at roughly 63 m/s² due to combined friction, meaning it would need an initial velocity around 3.5 m/s to slide 10 cm before stopping. A heavier, faster ball could transfer enough velocity to block1, but I'm also considering whether dragging block1 out would actually destabilize the stack through rotation rather than just horizontal displacement—since simply removing the base cleanly might just let the blocks drop straight down and remain standing. I'm now thinking about whether hitting the ball at a different height or point of contact on block1 could introduce enough tilt to topple the stack.

Working through the timing, the ball passes under block2 before it falls far enough to intersect, so that collision path doesn't work. Enlarging the ball doesn't help either since its contact point stays fixed at its center height, only touching block1. I should try a different approach—maybe a slower, sustained push instead of a quick impulse.

Thinking about a heavy sliding pusher box instead: sized shorter than block1 so it only contacts that one, launched fast enough to drag it forward while friction drags block2 along with it. But friction combination rules mean the floor's higher friction coefficient wins regardless of the pusher's surface, so a sliding box won't decelerate the way I want—maybe a rolling sphere pusher would avoid that friction penalty.

Switching to a heavy lead-like sphere (radius 6 cm, 10 kg) launched at 2 m/s with matching spin so it rolls without slipping and keeps shoving after impact. At that mass and speed it should kick block1 forward fast enough to slide it out from under block2 within a few hundredths of a second, with the ball catching up and continuing to push while block2 falls and the stack tips.

Now I'm checking the timing carefully: the ball passes under block2's footprint before block2 actually lands, so block2 might come down on top of the ball instead of past it — the geometry depends on exact heights and fall times, and it's borderline. I'm considering increasing inter-block friction to 1.0 to strengthen the drag-induced topple, and also thinking about using a larger 9 cm ball so it can strike both block1 and the lower portion of block2 after it drops, though the overlap in spans is still uncertain and needs more thought.

I'll settle on friction 1.0 between blocks and a heavy 10 kg ball at 2.5 m/s. To give the stack time to stand before impact, I'll position the ball further back, around 2.5 m behind, so it hits roughly 1 second in, with spin set around 41.7 rad/s for a radius of 6 cm rolling without slipping. I'll account for some speed loss from rolling friction as a minor detail.

