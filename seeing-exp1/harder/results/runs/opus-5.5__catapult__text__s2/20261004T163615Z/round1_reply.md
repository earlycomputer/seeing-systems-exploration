## What happens in the submitted scene

**Release.** With no keyframe, the arm starts horizontal at q = 0. The spring torque there is k(θref − q) = 2.0 × 2.62 ≈ 5.2 N·m. The gravity torque from the beam, cup and ball is about 3.1 N·m, so the arm swings up as soon as the run starts. The ball sits in the cup and slides about 2 cm out against the cup back.

**Energy at the stop.** The arm stops at its 55° limit.
- Spring work over 0–55°: k(θref·Δ − Δ²/2) ≈ 2.0 × 2.05 ≈ 4.1 J.
- Lifting the arm and ball costs about 2.5 J, and damping about 0.1 J.
- That leaves about 1.5 J of kinetic energy on a hinge inertia of about 0.27 kg·m².
- So ω ≈ 3.4 rad/s, and the ball leaves at about 3.2 m/s.

**Flight.** The ball launches about 30° above horizontal, from around (x ≈ −0.47, z ≈ 1.22). It lands near x ≈ 1.3. The bucket's near wall is at x = 1.6, so the ball falls short on the floor.

**Placement.** The bucket is also in the wrong place. Its centre is at x = 2.0, which is 2.92 m from the ball's start at x = −0.92, not 3 m.

## Fix

**Move the bucket.** Put the bucket centre at x = 2.08, exactly 3 m from the ball's start.

**Strengthen the spring.** Aim for a landing at the bucket centre.
- The required launch speed is about 4.2 m/s, so ω ≈ 4.46 rad/s and KE ≈ 2.7 J.
- The spring must therefore supply about 2.7 + 2.5 + 0.1 ≈ 5.3 J.
- That means k ≈ 5.3 / 2.05 ≈ 2.55.

**Clearance.**
- At the near wall the ball is still around 0.85 m high, well above the 0.4 m rim.
- It drops below the rim well before the far wall.

**Margin.** I made the bucket a little wider (half-size 0.5 m), because the energy estimate is approximate. The ball's contact is critically damped, so once in the bucket it stays there.

```xml
<mujoco model="catapult_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="8 8 0.1"/>
    <geom name="catapult_base" type="box" pos="0 0 0.170" size="0.08 0.12 0.170"/>
    <body name="catapult_arm" pos="0 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 55" stiffness="2.55" springref="150" damping="0.05" armature="0.01"/>
      <geom name="catapult_beam" type="box" pos="-0.500 0 0" size="0.500 0.03 0.02" mass="0.3"/>
      <geom name="catapult_cup_floor" type="box" pos="-0.920 0 0.025" size="0.08 0.08 0.005" mass="0.02"/>
      <geom name="catapult_cup_back" type="box" pos="-1.005 0 0.07" size="0.005 0.08 0.05" mass="0.01"/>
    </body>
    <body name="ball" pos="-0.920 0 0.4895">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.06" mass="0.15" condim="6" friction="0.8 0.01 0.004" solref="0.01 1"/>
    </body>
    <body name="bucket" pos="2.08 0 0">
      <geom name="bucket_base" type="box" pos="0 0 0.01" size="0.5 0.5 0.01"/>
      <geom name="bucket_near" type="box" pos="-0.5 0 0.2" size="0.01 0.5 0.2"/>
      <geom name="bucket_far" type="box" pos="0.5 0 0.2" size="0.01 0.5 0.2"/>
      <geom name="bucket_left" type="box" pos="0 0.5 0.2" size="0.5 0.01 0.2"/>
      <geom name="bucket_right" type="box" pos="0 -0.5 0.2" size="0.5 0.01 0.2"/>
    </body>
  </worldbody>
</mujoco>
```

```json
{"what_happens": "The spring arm swings up from horizontal to its 55 degree stop, but only about 1.5 J of the 4.1 J spring work is left after lifting the arm and ball. The ball leaves at roughly 3.2 m/s and about 30 degrees elevation and lands near x = 1.3 m, short of the bucket's near wall at 1.6 m. The bucket centre is also 2.92 m from the ball's start instead of 3 m.", "works": false, "problem": "The spring (stiffness 2.0) is too weak to throw the ball over the bucket's near wall, so it lands short, and the bucket centre is 2.92 m rather than 3 m from the ball's start."}
```

---
thinking (summarized):

I'm checking the distance between the ball's starting position and the bucket center — it comes out to about 2.92 m rather than the stated 3 m, roughly 8 cm off, though still within the bucket's half-width tolerance. I'm noting this as a possible fixture discrepancy before moving on to check the dynamics.

Working through the catapult mechanics: the arm hinges about the y-axis with range 0–55°, spring reference 150°, and stiffness 2.0 N·m/rad, giving spring torque of about 5.24 N·m at rest versus combined gravity torque of roughly 3.1 N·m from the beam, cup, and ball — so the arm launches immediately from q=0 since the spring overpowers gravity. I'm now working out the energy delivered by the spring as it swings from 0° to 55°, integrating the torque expression over that range to get the total work done.

Spring work comes out to about 4.10 J, while gravity resists with about 2.54 J, leaving roughly 1.56 J net kinetic energy. Summing the rotational inertias of the beam, cup, ball, and armature gives about 0.262 kg·m², so solving for angular velocity from the net energy yields ω ≈ 3.45 rad/s at launch.

Damping is minor, so I estimate the ball's speed at the end of the arm (~0.92 m radius plus a bit of height) to be around 3.2 m/s. Since the velocity direction is perpendicular to the arm at the 55° release angle, this works out to roughly a 35° elevation angle aimed toward +x — the ball separates as the arm hits its stop and flies off at that speed and angle.

Breaking this into components (vx≈2.6, vz≈1.84) and solving the projectile fall from launch height (~1.15-1.2 m) down to the bucket rim height, I get a flight time of about 0.70 s, giving a landing x-position around 1.29 m — which falls short of the bucket's 1.6 to 2.4 m range, so this configuration misses.

Recomputing more carefully with the ball's offset from the hinge rotated through 55°, I'm getting a corrected landing position around 1.37 m, still falling short of the bucket near the wall at 1.6 m, and the shot also needs enough height to clear the 0.4 m bucket wall. Given the target is meant to be about 3 m out (x≈2.08), my estimate is clearly rough, so I should reconsider the spring energy assumptions.

The design seems off: the bucket sits roughly 2.92 m from the ball, so the current range is about 2.3 m short. I need to either reposition the bucket to x=2.08 or boost the spring force so the ball actually reaches that distance while still clearing the bucket's rim height of 0.4 m.

Working through the trajectory: at a 35° launch angle, dropping from z=1.205 to a landing height around 0.2 over a horizontal distance of about 2.535 m, I set up the projectile equation using tanα=0.7 and solve for the required launch velocity to hit that target.

Solving gives v²≈16.9, so v≈4.11 m/s, and converting to angular velocity ω≈4.45 gives a kinetic energy of about 2.6 J. I'm estimating the spring work needed to produce this, including energy lost to the drop in height and damping, getting a rough spring constant around k≈2.5, though I recognize these numbers are sensitive and my damping and release-point assumptions are still fairly approximate.

My estimates could easily be off by 10-20%, and since range scales roughly with v², even modest errors in kinetic energy translate into fairly large swings in the required spring constant k — maybe ±7-8%. That's uncomfortably tight, so I'm considering ways to make the system less sensitive, like resizing the bucket or adjusting how much gravity contributes to the overall energy balance, to give myself more margin for error.

Now I'm working through the moment of inertia piece by piece: the beam contributes about 0.1, the cup floor and back pieces add roughly 0.017 and 0.010, the ball adds about 0.128 plus a tiny rotational term, and the armature contributes 0.01 — summing these up to get the total inertia about the hinge.

Next I need the gravitational torque contributions from each component, computing height changes for the beam, both cup pieces, and the ball as the arm swings through its angle, so I can total the gravitational work done across the whole motion.

Then I'm checking whether the ball stays in contact with the cup floor or whether at high rotational speed it would instead be thrown outward against the back wall — looking at the geometry of the cup's inner surfaces versus the ball's radius to see how much clearance exists before contact would occur.

Working through the energy budget, I figure out what spring work is needed to reach a landing point at the bucket center, accounting for the kinetic energy at release, damping losses, and the ball's slightly adjusted moment of inertia from sliding outward — solving for the required spring constant to hit the target velocity and angular speed at launch.

Recomputing the geometry more carefully, I realize the velocity direction isn't perpendicular to the simple radius but to the effective radius including the offset, which shifts the launch elevation angle down to about 29.4° instead of 35°, changing the trig factors. I also recalculate the ball's launch position accounting for the offset at the slid-out radius, getting new x and z coordinates to check against the target landing x of 2.08.

Working through the projectile equations with the target displacement and drop, I solve for the required velocity squared, getting v²≈17.74 so v≈4.21, then derive the spin rate ω≈4.46 from the no-slip condition. Computing kinetic energy and total work needed gives a stiffness constant k≈2.57, and I'm now double-checking this against a near-wall position to verify the trajectory clears correctly at x=1.67.

Checking the far wall position shows the ball would land before reaching it, giving a comfortable landing margin of roughly ±0.33m within an acceptable range. I'm also noting some uncertainty sources — the joint's soft limit constraint could let the arm overshoot and bounce before release, meaning the ball might actually leave around 55-60° rather than exactly at the target angle, plus there's the ball's contact stiffness and friction parameters to factor in.

To make the bucket catch more forgiving, I could widen it to a half-size of 0.5 since the brief doesn't restrict bucket dimensions, and possibly stiffen the hinge's limit solref slightly. I'm also checking that the arm releases properly at t=0 from rest, and considering how the ball behaves on landing — with critical damping there should be minimal bounce, and the bucket's 0.4 wall height should be enough to contain it even with its incoming horizontal and vertical velocity components.

I'm also verifying geometry: the beam's resting position and the base box shouldn't intersect, since the base top sits below the beam's bottom edge, and as the beam swings upward near the hinge it clears the base corner without collision.

My main uncertainty is the energy budget. Checking with k=2 instead of 2.55: work done comes out to 4.10, minus losses of 2.48 and 0.1, giving kinetic energy of 1.52, angular velocity 3.36, and launch velocity 3.17 — which produces too short a landing range. So the original spring constant doesn't work regardless of other adjustments.

I should place the bucket at x=2.08 so the ball travels from its start at -0.92 to a total distance of 3.0. With a bucket half-size of 0.5, the near wall sits at 1.58, and checking the trajectory there confirms enough clearance since the ball is descending steeply by that point. This setup checks out, so I'll write up the final answer.

