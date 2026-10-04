**Expected behaviour of the corrected scene**

- **Before the push:** for about 0.5 s the five-block column stands still on the floor. The sphere rolls toward it at 4 m/s, and with condim 3 there is no rolling resistance.
- **The impact:** the sphere hits block1 at its mid-height. The soft, mostly inelastic contact sends block1 off at roughly 3.5 m/s. The heavy sphere stays behind it and keeps driving it.
- **Block1 pulled out:** friction can accelerate the upper four blocks at no more than about 5.9 m/s². Block1 therefore slips the 0.1 m that leaves block2's centre unsupported in about 0.03 s, and is fully clear in about 0.06 s. Meanwhile that same friction has started rotating the upper stack backward.
- **The column falls:** block2 loses its rear support first and starts dropping tail-first. The sphere follows block1 into the space under the stack and strikes block2's low side while it is still falling. That knocks the base of the column forward out from under the blocks above.
- **Afterwards:** the column comes apart and the blocks tumble onto the floor and scatter. The sphere and block1 carry on along +x.

```json
{"what_happens": "The five-block column stands untouched for about 0.5 s. The rolling 4 kg sphere then slams into block1 at ~4 m/s and drives it out from under the stack faster than friction can carry the upper blocks along. Block2 loses support and drops tail-first, the sphere follows through and knocks the falling base forward, and the column topples and the blocks scatter across the floor.", "works": true, "problem": ""}
```

---
thinking (summarized):

I'm rechecking the scene geometry: pusher at -2.2, gap of 2.0 m to the block face, rolling at 4 m/s with no slip means impact occurs around 0.5 s. Since the contact is soft and inelastic-ish, the pusher and block1 end up moving together at roughly 3.5 m/s, and I'm now considering how the pusher's 40 rad/s spin affects the contact point velocity at block1's face.

Friction between the spinning ball and block1 could push upward on the ball even though the normal force is horizontal, and the ball continues to lose spin while also experiencing floor friction as it keeps rolling forward. Looking at the stack, block1 slides out from under block2 with floor friction decelerating it, and I estimate the relative slip needed to clear block2's support happens in about 0.03-0.06 s, during which block2 barely moves (~0.35 m/s) before dropping about 0.2 m -- essentially a tablecloth-pull scenario where the stack might stay standing if block1 clears quickly enough. I'm now working through whether block2 pivots about block1's rear edge as its front support disappears.

I realize the ball itself might slide into the space right under where the stack is falling, since block1 clears out of the way just as block2 is dropping. Timing-wise, the ball crosses under the stack's footprint while block2 has only fallen a small amount, so there's a real chance the ball ends up supporting or colliding with block2 mid-fall rather than the stack landing cleanly on the floor.

Checking that block1 and ball stay roughly in contact as both decelerate under floor friction, continuing at similar speeds around 3 m/s. No blow-ups expected from the soft contact penetration at that impact speed, and the initial stacking settle should be stable until the push—overall this setup should work fine.

