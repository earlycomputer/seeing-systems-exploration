**What happened:** The pendulum, released from 45°, struck the ball at 0.37 s. The collision lost most of the energy, so the ball only rolled at about 0.58 m/s. When it reached the cup at 1.81 s, it bumped against the 1.5 cm near lip and couldn't climb it. It bounced back at about 0.28 m/s, rolled all the way back to its start, and stopped at x ≈ 0.12 m. It never entered the cup.

**Changes:**
- **More speed:** the pendulum now starts at 80° instead of 45°. That drops the bob about 41 cm instead of 15, which should send the ball off at roughly 1 m/s.
- **Easier lip:** the near wall is now 1 cm high and the base 2 mm thick. Getting in needs only about 0.46 m/s. The inside lip stays 8 mm above the base, so it still holds the ball in.
- **Settling in the cup:** the cup's rolling friction is raised to 0.01, so the ball slows inside the cup instead of rebounding out.

The floor's low rolling friction still lets the ball carry its speed across the 1 m.

```world
world  pendulum strikes ball into cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.0002

pivot
  is a  point
  at    55 cm up

pendulum
  is a           sphere 3 cm radius, 300 g
  bounce         lively
  colour         grey
  50 cm below pivot
  turns on       pendulum hinge, about y, at pivot
  starts turned  80°

pendulum rod
  is a         rod 1 cm thick, from pivot to pendulum's top
  weighs       20 g
  colour       wood
  attached to  pendulum

stand arm
  is a     box 4 by 20 by 4 cm
  touches nothing
  colour   dark grey
  level with pivot, 12 cm left of pivot

stand post
  is a     post 4 cm square, from floor to stand arm's top
  touches nothing
  colour   dark grey
  centred on stand arm's left side

ball
  is a      sphere 4 cm radius, 100 g
  rolls
  friction  0.8, spinning 0.005, rolling 0.0002
  colour    orange
  moves     freely
  rests     on floor, 7.2 cm beyond pivot

cup
  is an             open box
  length            24 cm
  width             24 cm
  walls             8 cm
  wall thickness    1 cm
  base thickness    2 mm
  near wall height  1 cm
  friction          0.8, spinning 0.01, rolling 0.01
  bounce            dead
  colour            wood
  its base 1 m beyond ball

expect
  ball touches pendulum
  ball comes to rest in cup
```

```json
{"what_happens": "The pendulum, released from 45°, strikes the ball at 0.37 s, but the collision is lossy and the ball rolls at only about 0.58 m/s. It reaches the cup at 1.81 s, cannot climb the 1.5 cm near lip and bounces off it, then rolls back to near its start and stops at x ≈ 0.12 m, outside the cup.", "works": false, "problem": "The ball rolls too slowly to climb the cup's 1.5 cm near lip, so it bounces back and comes to rest near its start instead of in the cup."}
```

---
thinking (summarized):

The ball only reached 0.59 m/s after the collision, losing a lot of energy from the inelastic contact, and bounced off the near wall whose 1.5 cm lip was too high to clear at that speed. The pendulum also lost significant energy, swinging back to just -7.7° post-collision, implying the bob's speed dropped from 1.69 m/s to roughly 0.29 m/s — the collision is far too inelastic to transfer enough momentum to the ball.

To fix this I should increase the swing angle to 90°, use a heavier bob, and lower the lip height. A 90° swing gives the bob a speed of about 3.13 m/s versus 1.69 m/s, a 1.85x increase, which should push the ball to roughly 1.1 m/s — more than enough to clear a 1 cm lip (minimum required is around 0.46 m/s by my energy calculation), though I need to be careful not to overshoot and have the ball slam into the far wall and rebound unpredictably.

One option is to make the base thinner (2 mm) so the near lip is effectively 8 mm tall from inside, while also increasing rolling friction inside the cup (say to 0.01) to help decelerate the ball before it reaches the far wall.

Checking the numbers: with decel around 1.75 m/s², a ball entering at 0.9 m/s across roughly 15 cm would drop to about 0.6 m/s by the far wall, and after a near-dead rebound (~0.2 m/s) it should stop within about a centimeter — that works. I need to confirm this rolling friction only applies to ball-cup contacts and not ball-floor (which stays at 0.0002), and that condim 6 is needed for rolling friction torques to engage. I'm now working out the pendulum release angle needed to give the ball its target speed of about 1 m/s, computing the height drop at 70° and the corresponding velocity.

Testing 80° instead gives a drop height of 0.413 m and swing speed of 2.85 m/s, which after the energy transfer factor lands close to 1.0 m/s for the ball — that's the sweet spot, so I'll keep the bob mass as is. Tracing the ball's path after it clears the lip: losing energy to the small rise leaves it around 0.73 m/s, then rolling friction over about 13 cm inside the cup brings it down further, landing it near the far wall with only a small residual speed, likely settling there with minimal rebound. I'm now sizing the cup's interior dimensions and near wall thickness.

Setting the start rotation to 80 degrees so the rod clears the bob near pivot height. For friction, I'm setting the near wall at 1 cm height, base at 2 mm thickness, and cup rolling friction at 0.01, which will dominate over the sphere's own 0.0002 rolling friction since MuJoCo takes the max when combining.

