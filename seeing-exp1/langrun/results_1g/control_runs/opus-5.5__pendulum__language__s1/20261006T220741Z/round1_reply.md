## What happened in the run

The pendulum was released from 45°. Its rod touched the part's stand arm for the entire run, and that contact dragged on the swing. The bob reached the bottom far slower than a free swing would.

- **The strike:** the bob hit the ball at 0.38 s. The ball left at only about 0.47 m/s.
- **The approach:** the ball rolled along the floor and slowed to about 0.32 m/s by the time it reached the cup's 1 cm near lip at 2.42 s.
- **The lip:** it could not climb the lip. It bounced back and rolled slowly away.
- **The end:** the ball came to rest on the floor at x ≈ 0.76–0.84 m, outside the cup. The pendulum kept swinging feebly at about ±10°.

## Changes

1. **Pendulum rebuilt by hand.** I removed the library pendulum and built my own: a bob named `pendulum` on a hinge, with a rod attached. Its support beam and post sit clear of the rod and touch nothing, so the swing is no longer dragged.
2. **Starting angle 40°.** I scaled the strike from what the last run showed. A free swing from 40° should send the ball off at roughly 1.2 m/s.
3. **Lower lip.** The near wall is now 8 mm high, so the ball climbs it more easily. It still stands 3 mm above the cup's base to help hold the ball in.
4. **Longer cup with stronger braking.** The cup is now 40 cm long, still centred 1 m from the ball's start, and its rolling friction is doubled to 0.06. This should stop the ball inside.

This version has not been run yet; the speeds above are estimates.

```world
world  pendulum strikes ball into cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.001

pivot
  is a  point
  at    55 cm up, 0 m along

pendulum
  is a           sphere 4 cm radius, 500 g
  colour         grey
  50 cm below pivot, 0 m along
  turns on       pendulum hinge, about y, at pivot
  starts turned  40°

pendulum rod
  is a         rod 1 cm thick, from pivot to pendulum's top
  weighs       50 g
  colour       grey
  attached to  pendulum

support beam
  is a    box 6 by 30 by 4 cm
  touches nothing
  colour  wood
  4 cm above pivot, 15 cm to the right, 0 m along

support post
  is a    post 6 cm square, from floor to support beam's top
  touches nothing
  colour  wood
  centred on support beam's right side

ball
  is a      sphere 4 cm radius, 100 g
  rolls
  friction  0.8, spinning 0.005, rolling 0.001
  colour    orange
  moves     freely
  rests     on floor, 9.5 cm beyond pivot

cup
  is an             open box
  length            40 cm
  width             30 cm
  walls             10 cm
  wall thickness    2 cm
  base thickness    5 mm
  near wall height  8 mm
  friction          1.0, spinning 0.02, rolling 0.06
  bounce            dead
  colour            wood
  its base 1 m beyond ball

expect
  ball touches pendulum
  ball comes to rest in cup
```

```json
{"what_happens": "The pendulum's rod rubbed against the library stand arm throughout, so the bob swung slowly and hit the ball at only about 0.56 m/s. The ball rolled off at 0.47 m/s and slowed to about 0.32 m/s at the cup. It bounced back off the 1 cm near lip and came to rest on the floor at x ≈ 0.76–0.84 m, outside the cup.", "works": false, "problem": "The rod rubbing on the stand arm robbed the swing, so the ball was too slow to climb the cup's near lip and stopped on the floor short of the cup."}
```

---
thinking (summarized):

The ball only reached 0.47 m/s and bounced off the near wall, ending at 0.76 on the floor—this fails. I'm also noticing the pendulum rod stays in contact with the stand arm throughout the swing, creating friction drag that's damping the motion dramatically, dropping the pendulum from 45° to just -11° instead of swinging freely.

I should avoid the stand arm friction issue altogether—rather than modifying the existing part, I could define my own pendulum setup directly: a bob sphere named `pendulum` that turns on a hinge, with a rod attached, built so the stand doesn't physically contact the rod during the swing (raising the arm or adding clearance around the pivot).

Working out positions: pivot at 55cm height, pendulum bob 50cm below it turning on a hinge about y at 45° start, arm rod connecting pivot to bob, and a separate support beam placed with a few cm of clearance above the pivot so it never touches the swinging rod.

I'm also figuring out the support post dimensions and placement so it reaches from floor to beam without colliding with anything, keeping these fixed supports touching nothing for safety.

Now I'm recalculating the pendulum physics: bob speed at bottom without friction loss is about 1.70 m/s, but the ball previously only reached 0.47 m/s with losses, decelerating from 0.47 to 0.32 m/s over 1.75s (a deceleration around 0.086 m/s²). Since that failed to climb the lip at 0.32 m/s, I need a launch speed closer to 0.8 m/s to have enough margin after the predicted velocity loss over the remaining distance.

I'm now tweaking the lip geometry — lowering the near-wall height to around 7-8mm (just 2-3mm above the base) to make climbing easier while still requiring enough speed to avoid the ball stalling out. Since transfer efficiency from pendulum to ball strike is uncertain, the safest fix is bumping the starting swing angle up to 60° to get more bob speed.

I'm recalculating ball dynamics using the actual measured floor deceleration rather than my predicted one, since the real decel was about half what I estimated — this changes how far the ball travels before stopping, suggesting I need to increase cup rolling friction and lengthen the cup to around 40cm to keep the ball from hitting the far wall dead.

Now I'm considering whether a 45° angle works without pendulum friction, checking ball speeds at different launch angles — at 50° the ball reaches about 1.87 m/s, and factoring in elastic collision and rolling conversion, the max speed could hit around 2.2 m/s, though I'm unsure how MuJoCo's restitution settings will actually behave here.

Working back from the pendulum's observed swing angle after impact, I estimate the bob's post-collision speed around 0.43 m/s, which through momentum conservation suggests the bob struck the ball at roughly 0.56 m/s — far below the ideal 1.70 m/s, indicating significant friction losses during the swing, with the ball only picking up about 84% of the bob's speed.

Now I'm checking a frictionless 45° case where the ball would hit about 1.43 m/s, losing some speed climbing over the 8mm lip to enter the cup near 1.15 m/s. Scaling the rolling friction from measured deceleration suggests the ball travels roughly 25cm before stopping at this friction level, well short of the ~34cm needed to cross the cup — so I'm considering either increasing rolling resistance to around 0.06 to get it closer to 13cm, or instead reducing the launch angle to 35° to adjust the entry speed.

Testing 35° gives ball speed ~1.12 m/s and entry around 1.06, after-lip speed 0.85 — a decent middle ground. Then trying 40° instead: ball speed comes out to 1.27 m/s, entry 1.21 — this seems like a good choice. I'll settle on 40° launch angle, cup rolling resistance of 0.06, cup length 40cm, near wall thickness 8mm, base thickness 5mm. I also need to check whether this rolling resistance causes issues during the lip-climbing pivot, but the speed margin should cover it. Now I'm setting up positions: pendulum hanging 50cm below its pivot, ball resting on the floor 9.5cm beyond the pivot, with the expectation that the ball should just touch the pendulum.

