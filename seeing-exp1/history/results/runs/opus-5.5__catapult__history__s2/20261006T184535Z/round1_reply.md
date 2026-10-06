**What happens in the run**

- **Launch.** The sprung arm swings up from its 0° stop. It hits the 55° stop at about 188°/s and lets go of the ball at about 0.53 s, from roughly (−0.46, 1.22) m. The ball leaves at about 2.8 m/s and only about 22° above horizontal.
- **Flight.** It peaks at (−0.17, 1.28) m.
- **Landing.** It hits the floor at x ≈ 1.1 m at 1.14 s. It bounces into the outside of `bucket_near` and comes to rest on the floor at (1.47, 0, 0.06) m, short of the bucket.
- **Bucket position is also wrong.** The bucket centre is at x = 2.0, which is 2.92 m from the ball's start rather than 3 m.

**Fix**

- **Bucket.** Move the bucket to x = 2.08 so its centre is exactly 3 m from the ball's start. I also widened it to 0.9 m and lowered its walls to 0.3 m, which gives more room for error.
- **Spring.** Stiffen the catapult spring from 2.0 to 2.75 N·m/rad.
- **Energy estimate behind the new stiffness.** From the measured run, the arm's kinetic energy at the stop was about 1.4 J. Gravity took about 2.5 J and damping and losses about 0.2 J, out of about 4.1 J from the spring. With k = 2.75 the spring gives about 5.6 J. That should raise launch speed by about 1.45×, to about 4.1 m/s.
- **Predicted landing (not yet run).** At the observed launch angle, this lands near x ≈ 2.1. Speeds 7% lower or higher should still land inside, between about x ≈ 1.86 and 2.32. The inner walls are at 1.64 and 2.52. The ball should clear the near wall's top by a few centimetres even at the low end. The landing estimate assumes ball speed scales with arm speed and the launch angle stays near 22°, so it needs a run to confirm.

```xml
<mujoco model="catapult_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="8 8 0.1"/>
    <geom name="catapult_base" type="box" pos="0 0 0.170" size="0.08 0.12 0.170"/>
    <body name="catapult_arm" pos="0 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 55" stiffness="2.75" springref="150" damping="0.05" armature="0.01"/>
      <geom name="catapult_beam" type="box" pos="-0.500 0 0" size="0.500 0.03 0.02" mass="0.3"/>
      <geom name="catapult_cup_floor" type="box" pos="-0.920 0 0.025" size="0.08 0.08 0.005" mass="0.02"/>
      <geom name="catapult_cup_back" type="box" pos="-1.005 0 0.07" size="0.005 0.08 0.05" mass="0.01"/>
    </body>
    <body name="ball" pos="-0.920 0 0.4895">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.06" mass="0.15" condim="6" friction="0.8 0.01 0.004" solref="0.01 1"/>
    </body>
    <body name="bucket" pos="2.08 0 0">
      <geom name="bucket_base" type="box" pos="0 0 0.01" size="0.45 0.45 0.01"/>
      <geom name="bucket_near" type="box" pos="-0.45 0 0.15" size="0.01 0.45 0.15"/>
      <geom name="bucket_far" type="box" pos="0.45 0 0.15" size="0.01 0.45 0.15"/>
      <geom name="bucket_left" type="box" pos="0 0.45 0.15" size="0.45 0.01 0.15"/>
      <geom name="bucket_right" type="box" pos="0 -0.45 0.15" size="0.45 0.01 0.15"/>
    </body>
  </worldbody>
</mujoco>
```

```json
{"what_happens": "The sprung arm swings to its 55° stop and releases the ball at about 2.8 m/s and a shallow ~22° angle from about (-0.46, 1.22) m. The ball peaks at 1.28 m, lands on the floor at x≈1.1 m, bounces off the outside of the bucket's near wall and rests on the floor at x≈1.47 m, outside the bucket, which is also centred 2.92 m rather than 3 m from the ball's start.", "works": false, "problem": "The catapult throws too weakly, so the ball lands about 1 m short and never enters the bucket, and the bucket centre is 2.92 m rather than 3 m from the ball's start."}
```

---
thinking (summarized):

I'm noticing the ball falls short of the bucket with my current setup — it lands around x=1.2 and bounces away instead of landing in bucket_near. I need to reposition the bucket closer, around x=2.08, so the ball's roughly 3m horizontal travel actually lands it inside.

I'm tracing the ball's trajectory in detail: computing the release point, velocity, apex, and fall time to pin down where it touches the floor, while also checking it clears the near wall at x≈1.67 by enough height margin. It seems the launch speed needs to increase, so I'm working through the arm's rotation geometry at the release angle to figure out the resulting velocity direction.

I need a scale factor around 1.45 to hit the right range. Computing the actual release point: with the arm at 55°, I'm rotating the ball's offset from the pivot and finding it releases around (-0.454, 1.205) — though this doesn't quite match what I had before, so I should double-check the arm geometry.

Working through the physics now: release angle 35°, aiming for the ball to land around x≈2.08 at the bucket floor near z≈0.08. Using the projectile drop equation with horizontal distance D=2.53 and the known tangent/cosine values for 35°, I'm solving for the velocity needed to match that trajectory drop.

Solving gives v²≈16.15, so v≈4.02 m/s. Checking the trajectory at the near wall (x=1.67) shows the ball passes well above the 0.46 threshold, confirming it clears the wall before descending steeply into the bucket.

Now I'm noting a discrepancy in my release velocity figures: I'm getting vz dropping from 1.72 at t=0.50 to about 1.08 at t=0.53, which is more than gravity alone would account for—suggesting the arm's deceleration at the stop is affecting the ball's velocity right at release, so I need to be careful about which exact release moment and velocity to use.

I could instead rely on the catapult's dynamics by stopping the arm at a larger angle, like 45°, to get a steeper launch. Checking the numbers though, the actual release point gives a lower vz than a clean free-flight calculation would predict, meaning the arm's deceleration phase is bleeding off some of the ball's vertical velocity before it separates.

Comparing release state (around speed 3.0 m/s at 35.5°) to what's actually needed (speed closer to 4.0 m/s at similar angle), I need to scale the arm's angular velocity by roughly 1.33x, which means boosting the spring energy by about 1.78x — accounting for gravity's work during the swing.

Computing the spring's stored energy between the 150° and 95° positions gives about 4.1 J, while gravity does roughly 2.5 J of negative work lifting the arm, cup, and ball through the swing — leaving net kinetic energy available to accelerate the ball.

Cross-checking with the system's moment of inertia (beam, cup, ball, armature summing to about 0.263 kg·m²), I verify that this kinetic energy translates to a plausible angular velocity, confirming consistency with a damping-adjusted estimate. To hit the target angular velocity of 4.37 rad/s, I work backward to find the required spring stiffness scaling (around 2.55 vs the current 2.0), then consider how sensitive the ball's landing spot is to velocity errors given the bucket's width — roughly ±14% tolerance in range.

I also want to calibrate against the observed trajectory data rather than just theory, tracking the ball's position and velocity at successive timestamps (around t=0.55 to 1.14s) to back out an effective launch state and improve my estimate's accuracy.

I'm solving for the required launch speed at that 22° angle to hit the target, getting v≈4.12 (scaling factor ~1.45x). Checking clearance near the wall at that speed, the trajectory clears with some margin but it's tight enough that I need to verify at slightly different speeds too.

Rather than fiddling with launch timing, I'm considering whether adjusting the bucket geometry—like lowering wall height or widening the tub—might give more margin, though the bucket dimensions already seem reasonably generous. I'll move on to recalculating the energy scaling needed for the arm to reach this new speed factor.

Accounting for the ball's offset above the beam axis, the tangent direction elevation works out closer to 29.4°, which roughly matches the observed 22° once the stop impulse and overshoot are factored in. I'll settle on a spring stiffness of 2.8, widen the bucket slightly, and lower the walls for margin, then check landing sensitivity across the stroke range using the 22° launch angle and 1.22 height.

Solving the quadratic for different stroke values, I find the ball lands around x=1.86 for s=1.35, which clears the inner wall at 1.63 and the wall clearance check at x=1.62 confirms the trajectory passes just above the required 0.36 height. I'm now working through the same clearance calculation for s=1.55 with updated velocity and coefficients.

That gives D=2.775, so x=2.32, comfortably clearing the far inner face at 2.52. This narrows the valid stroke range to s∈[1.35,1.55], with a target around s=1.45, so now I'm setting up the energy balance between spring energy, kinetic energy needs, and observed losses to back out the required spring constant k.

Solving across the stroke range gives k roughly between 2.57 and 2.97, so k=2.75 sits comfortably in the middle — good since the ball speed scales linearly with arm speed.

I'm checking that the ball's landing dynamics make sense: with critically damped contact and a low wall height relative to ball radius, the ball should settle without bouncing over, and the bucket being a fixed body without a joint works fine. Now I'm finalizing the bucket and wall geometry parameters before writing the scene file.

