## What happened in the run

The pendulum swung freely this time; its swing matches an undamped 50 cm pendulum, and it touched nothing but the ball.

- **The strike:** the bob reached about 1.5 m/s, yet the ball rolled off at only 0.43 m/s.
- **After the strike:** the bob kept about a quarter of its speed and swung on at about ±10° for the rest of the run.
- **The cup:** the ball reached the 8 mm near lip at 2.50 s, moving at about 0.29 m/s. It could not climb it.
- **The end:** the ball stopped at x ≈ 0.86 m and then crept back to 0.80 m, outside the cup.

The first run showed the same speed ratio, about 0.28. So the stand arm contact was never the cause. The cause is how little momentum the strike passes on.

## Why the strike is so weak

Working back from the speeds before and after the strike, the swinging body acts as if it weighs only about 50 g. That is roughly the rod's mass, about half the ball's, not the 500 g I gave the bob. My guess is that the bob's mass in its `is a` line is not being applied to the hinged body. I have not confirmed this.

## Changes

1. **Mass on both pieces.** The bob's mass now goes on its own `weighs 1 kg` line, and the rod weighs 500 g. Whichever way the masses are combined, the swinging body should now clearly outweigh the 100 g ball.
2. **Starting angle 48°.** If both masses take effect, the ball should leave at about 1.35 m/s. If only the rod's does, about 0.9 m/s. Either way it should reach the lip fast enough to climb it.
3. **Cup unchanged.** Its high rolling friction should stop even the faster ball well before the far wall.

This version has not been run yet, and the mass explanation is a guess.

```world
world  pendulum strikes ball into cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.001

pivot
  is a  point
  at    55 cm up, 0 m along

pendulum
  is a           sphere 4 cm radius
  weighs         1 kg
  colour         grey
  50 cm below pivot, 0 m along
  turns on       pendulum hinge, about y, at pivot
  starts turned  48°

pendulum rod
  is a         rod 1 cm thick, from pivot to pendulum's top
  weighs       500 g
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
{"what_happens": "The pendulum swings freely from 40° and hits the ball at 0.38 s with the bob moving about 1.5 m/s. The ball rolls off at only 0.43 m/s and slows to about 0.29 m/s by the cup. It fails to climb the 8 mm near lip and stops on the floor at x ≈ 0.80–0.86 m, outside the cup.", "works": false, "problem": "The strike passes on too little momentum, as if the swinging body were lighter than the ball, so the ball is too slow to climb into the cup."}
```

---
thinking (summarized):

I realize the swing matches the pendulum's natural motion exactly, not friction — checking the angular velocity at 18.8° against the ideal energy conservation formula confirms it lines up almost perfectly at ω≈2.66-2.67 rad/s, so I'm now working out the bob's speed at the bottom using the maximum angular velocity.

Something's off though: the predicted bottom speed is around 1.51 m/s but the ball only ends up at 0.43 m/s, and checking momentum conservation with the post-strike amplitude of ~10° doesn't balance out — I'm getting inconsistent ball velocities depending on which values I plug in. I'm now second-guessing the period estimate from the oscillation data and wondering if the energy loss comes from the contact model's softness parameters rather than true inelastic collision, since momentum should still be conserved regardless.

I'm trying long contact duration explanations — floor friction on the ball seems too small to absorb the missing momentum. Maybe the sphere or pendulum mass assumptions are off, or the post-strike amplitude of ±10° doesn't actually match the energy I calculated, so I need to recheck those numbers.

By 0.5s the pendulum is nearly stopped at -8.7°, so whatever energy transferred barely moved it despite the ball ending at 0.43 m/s. I can't pin down exactly why the numbers land there, but empirically the ball seems to come out around 0.43-0.47 m/s depending on the drop angle, so I'll just treat that as the observed behavior rather than fully deriving it.

Working the momentum conservation backward with an unknown pendulum mass, I get roughly 0.054 kg for the effective bob mass — suggesting the actual swinging mass is closer to 50 g rather than 500 g, maybe from a rod or small sphere component rather than the heavier body.

I should test whether both masses are actually being ignored and defaulting to a standard density calculation instead, giving equal masses rather than the specified 500 g and 100 g. The safest fix is to explicitly set the bob's mass using an unambiguous weight specification.

Maybe a ramp replacing the lip could work—ball rolls up onto the base, kept low-friction on the ramp itself but high friction at the base to stop it before it rolls back out. But that risks the ball rebounding back down the ramp if it's still moving too fast, so I should just ensure sufficient incoming speed and rely on strong base friction to catch it instead of overcomplicating the geometry.

I'm trying a bigger bob (5 cm radius, denser, plus explicit heavier mass) and a heavier ball, but I'm unsure whether the engine actually respects the given mass overrides versus defaulting to density. I'm working through the equal-mass hypothesis, estimating effective mass at the bob by combining the sphere's mass with a fraction of the rod's mass based on moment of inertia.

I'm computing the post-collision common velocity if effective masses honor that combined estimate, but the predicted bob swing doesn't match the measured 0.39 amplitude well, so I'm considering whether gravity deceleration during the brief contact or sphere-bob friction could explain the gap. Testing the alternative where the stated masses (500g/100g) are used directly gives a common velocity way higher than what's measured, so that assumption seems wrong too.

So I'm now trying a different approach: deriving masses from density given a bob radius of 8 cm (~2.14 kg) and a ball radius of 4 cm (~268 g), roughly preserving an 8:1 ratio, and checking if explicit weights near 2 kg and 270 g are consistent. With that, I'm recomputing an elastic-ish collision with restitution between 0 and 0.3, then applying rolling friction's 5/7 factor to the ball's post-collision speed.

Working through the inelastic case where the ball keeps moving at roughly 0.89 of the bob's incoming speed before rolling resistance brings it down near 0.64 of that speed, I pick an entry speed of about 1.8 m/s for the bob to land the ball's final speed around 1.15 m/s, fitting the target range. With the bob radius now at 8 cm, I need to redo the geometry so the bob's center clears the ledge height, meaning the drop point sits around 9 cm up, with the ball's 4 cm radius contact point positioned above that.

The contact angle between ball and bob matters now — at these radii it comes out around 24° above horizontal, pushing the ball down into the floor and bleeding energy, so I want to shrink that mismatch. Bumping the ball to 6 cm radius and adjusting the bob to 7 cm with a slightly lower drop point fixes the contact angle, but then the mass ratio suffers — ball at 905 g against a 1.44 kg bob isn't ideal, so I'm considering either specifying explicit masses or swapping the bob for a box shape, though a weighted sphere with the right radius might be the simplest fix despite the uncertainty.

With this configuration density ratio stays unfavorable, so maybe the issue isn't mass at all but contact duration — if the timeconst is 0.02s and contact lasts 0.06s, the ball could be getting pinned rather than cleanly struck. I should look more carefully at the ball's initial setup for clues.

/7 v0 regardless of timing, so that's not a hidden loss beyond that factor. I'm trying to reconcile the empirical ball/bob speed ratio of 0.285 against earlier drag estimates that suggested something closer to 0.84, which seems contradictory unless run 1 had much lower friction than I assumed. Checking run 1's data at 0.25s against the idealized trajectory from 45° to see if the discrepancy can be explained.

I'm finding run 1 also matches the ideal case — friction wasn't actually an issue there. Both runs show a consistent bob-to-initial ratio around 0.26 and ball ratio around 0.28, so I'm checking whether momentum conservation holds between the bob's initial and final speeds plus the ball's contribution.

Working out M/m from these numbers gives about 0.54, which is suspiciously close to the rod's 50g mass over a 100g ball — suggesting the "bob" mass used in the simulation might actually just be the rod's weight, not the full pendulum assembly, as if attached objects collapsed into one body during motion.

I'm trying different fixes: boosting the rod's weight significantly, or scrapping the rod altogether and letting the bob hang directly from the pivot. If the rod carries most of the mass distributed along its length, the effective mass at the bob ends up around a third of a kilogram, giving a roughly 3:1 ratio against the ball rather than the much larger ratio if the bob's own mass is properly counted.

I'm now working through the momentum equation using the observed mass ratio of 0.54 between pendulum and ball, plugging in the recorded velocities to solve for the ball's rebound speed and back out the coefficient of restitution.

Testing different ratio scenarios against a target rolling speed of 1.1 m/s, I'm checking which release angle (somewhere between 38° and 58°) gets me close, then verifying the ball still clears the lip given the deceleration from friction.

For the rolling resistance estimate, I'm extrapolating from a measured deceleration value to figure out how far the ball travels inside the cup before stopping -- roughly 14 cm of rolling distance, well within the 36 cm cup diameter, which checks out fine.

Looking back at run 2, I remember the ball hit the lip at 8mm and rebounded then stopped, meaning I need a minimum speed around 0.4+ to clear it, and our target speeds of 0.85+ satisfy that comfortably. For the ball and bob objects, I'll keep consistent descriptions -- sphere, 4cm radius, appropriate mass -- while varying phrasing slightly between "is a sphere" and "weighs" to avoid repetition, and I'll set the starting rotation to 48 degrees.

