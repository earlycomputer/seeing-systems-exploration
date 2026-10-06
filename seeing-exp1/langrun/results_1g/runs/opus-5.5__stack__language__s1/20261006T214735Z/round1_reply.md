**What happened:** The stack stood still until the ball reached it at 1.09 s. By then the ball had slowed to about 1.1 m/s, partly from turning its slide into a roll and partly from rolling friction. Its contact was dead, so it slumped against `block1` and stopped. It nudged `block1` only 4 cm and the whole stack shuffled 2 cm forward. The stack settled upright and never toppled, and `block5` never reached the floor.

**The fix:** Give the bottom block a sharp kick, not a slow shove. `block1` should shoot forward about 7 cm while the four blocks above lag behind. The stack's centre of mass then sits beyond `block1`'s back edge, and the stack tips over backward.

- **Ball:** lighter (600 g), with a lively bounce so it delivers a quick blow and rebounds.
- **Launch:** 3 m/s, already spinning at the matching rolling rate, so it arrives at about 2.7 m/s.
- **Timing:** it starts farther back, so the stack still stands for most of a second.
- **Block friction:** raised to 0.8, so `block1` pulls hard on the bottom of `block2` as it leaves and helps tip the stack.

```json
{"what_happens": "The stack stands until the ball reaches it at 1.09 s, but the ball has slowed to about 1.1 m/s and hits with a dead contact. It shoves block1 only 4 cm and the stack shifts 2 cm, then everything settles upright; block5 never reaches the floor.", "works": false, "problem": "The push is too weak and too slow to unsettle the stack, so it never topples."}
```

```world
world  toppling stack

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

block
  is a      cube 10 cm, 250 g
  friction  0.8
  colour    wood
  moves     freely
  stacked   5 high
  stands    on floor, 2.5 m along

-- the pusher: a ball already rolling, which strikes the bottom block sharply and rebounds
ball
  is a      sphere 4 cm radius, 600 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.01, rolling 0.002
  colour    orange
  moves     freely
  rests     on floor, 0 m along
  launched  3 m/s along
  spins     75 rad/s about y

expect
  ball touches block1
  block5 touches floor
```

---
thinking (summarized):

The ball only slowed to 1.13 m/s by the time it arrived and merely shoved the block 4 cm without toppling it, so I need a stronger impact. I'm considering whether a faster or heavier ball would work better, and thinking through the momentum transfer if the collision is effectively inelastic, with friction acting under the combined mass afterward.

Maybe a better approach is to kick the bottom block out quickly so the upper blocks lag due to inertia and land off-center, creating a tilt — I'm estimating the fall distance during the brief kick-out window and weighing it against the friction drag coupling the blocks together.

Running the numbers, friction between block1 and block2 only accelerates the stack a few mm during the kick, so the stack basically just drops flat onto the floor like the classic tablecloth trick rather than toppling. To actually get toppling, I think the push needs to be gentler so the whole stack shifts together but tips backward from inertia lag between bottom and top — though with identical friction values between all the stacked blocks, it's tricky to predict exactly how much offset causes a topple.

If block1 shifts 6cm forward, its new span no longer sits under the stack's center of mass, which stays near x=2.00 — so the stack tips backward off the edge and topples. That suggests the target slide distance is somewhere in the 6-9cm range, where the upper stack lags enough to lose support, and I'm working out the deceleration from floor and interblock friction to estimate what impact velocity achieves that.

Running the numbers, block1 needs around 3.2 m/s to slide roughly 8cm before friction stops it, while the friction drag transmitted to the upper stack only pushes it a few millimeters forward in that same short window — not enough to keep it centered over block1's new position. That mismatch is what causes the toppling, and since block1 sliding forward applies a forward pull at the stack's base, it actually creates a backward-tipping torque, which works in my favor since the stack would then fall onto the ball sitting behind it.

Rather than relying on a dead collision where ball and block stick together and the ball's momentum just drags block1 forward with little deceleration, I think the better setup is a lighter, fast, lively ball — say 1 kg bouncing in at roughly 4 m/s — so the impulse is sharp and the ball rebounds cleanly instead of pushing block1 along indefinitely.

I'm reconsidering whether high inter-block friction would make the stack act rigidly, but calculating the torque from a base-level push shows the floor friction largely cancels out the toppling moment. A low push height just isn't generating enough torque to tip the stack forward.

So I'm leaning toward the backward-toppling mechanism from the overhang instead, where a sharp impact displaces the bottom block several centimeters and leaves the upper block to land with rotation induced by friction. I'm tuning the ball mass and speed around 1 kg at roughly 2.5 m/s, and checking how starting distance affects timing—wanting the stack to stand undisturbed for about a second before impact rather than toppling almost immediately, while also accounting for the speed loss as rolling motion converts from sliding.

Now I'm working out the spin needed for the ball to roll without slipping when it hits—setting the angular velocity about the y-axis equal to v/r so the contact point has zero velocity relative to the ground, which means giving the ball initial spin matching its translational speed divided by its radius.

I'll place the ball farther back, around 2.5 m from the stack, giving it a ~0.85 s travel time before impact at roughly 2.7 m/s, which seems like a good arrival speed. Now I need to tune the ball's mass so the impact transfers enough momentum to send block1 off at around 3-4 m/s.

Trying an 0.8 kg ball with an elastic collision gives about 4.1 m/s, but factoring in a more realistic restitution of around 0.7 brings it down to roughly 3.5 m/s, which seems like the right range. From there, block1's sliding distance under friction works out to only about 0.1 m, though I realize the friction on block2 will change as the normal force shifts once block1 starts separating.

Switching to the 0.6 kg ball instead, the restitution-adjusted velocity comes out to about 3.2 m/s, giving a slide distance near 0.072–0.08 m, which feels more consistent once I bump the block-block friction up to 0.8 to increase tipping torque, and the floor friction to 0.8 as well — the numbers check out with an acceleration around 71 m/s².

I'm also considering how the ball rebounds and whether the stack eventually settles back down onto it, likely with the lowest block reaching the floor, and I need to confirm the sign convention for the ball's spin, settling on positive 75 rad/s about the y-axis.

