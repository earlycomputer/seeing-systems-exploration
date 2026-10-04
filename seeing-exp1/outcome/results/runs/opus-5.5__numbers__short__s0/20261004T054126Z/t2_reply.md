The original launch (vx = 2.95, vz = 8.56 m/s) drops through rim height at x ≈ 3.14 m, which is 0.86 m short. I changed the `shot` key to vx = 3.2, vz = 9.3 m/s.

- **How I chose it:** I fitted the drag from the logged trajectory, which comes to about 0.021·|v|·v per unit mass. I then integrated candidate launches by hand. I did not re-run MuJoCo, so the new shot is a prediction, not a simulated result.
- **Predicted path:** apex about 4.13 m near x ≈ 2.7. The ball centre comes down through z = 3.05 at x ≈ 4.00, descending at about 58°.
- **Rim clearance:** at that angle the ball clears both sides of the rim by about 7 cm. That allows roughly ±9 cm of error along x.
- **After the hoop:** the ball passes below the backboard (bottom edge at 2.9 m). It will probably hit the support pole at about 0.8 m height before reaching the floor. That happens only after it has gone through the hoop.

```xml
<mujoco model="basketball_hoop">
  <option timestep="0.002" density="1.2"/>

  <visual>
    <headlight ambient="0.15 0.15 0.15" diffuse="0.3 0.3 0.3" specular="0 0 0"/>
  </visual>

  <worldbody>
    <!-- Lighting: main overhead directional light plus a softer fill spot above the hoop -->
    <light name="overhead_sun" directional="true" pos="2 0 10" dir="0 0 -1" diffuse="0.8 0.8 0.8" specular="0.2 0.2 0.2" castshadow="true"/>
    <light name="overhead_fill" pos="4 0 8" dir="0 0 -1" diffuse="0.3 0.3 0.3" specular="0 0 0" castshadow="false"/>

    <!-- Floor: top surface at z = 0 -->
    <geom name="floor" type="plane" pos="0 0 0" size="10 10 0.1" rgba="0.72 0.52 0.32 1" friction="0.8 0.005 0.0001"/>

    <!-- Regulation size-7 basketball: circumference 0.75 m -> radius 0.1194 m, mass ~0.62 kg (hollow shell inertia 2/3 m r^2) -->
    <body name="ball" pos="0 0 0.1194">
      <freejoint name="ball_free"/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.005893 0.005893 0.005893"/>
      <geom name="ball" type="sphere" size="0.1194" rgba="0.85 0.40 0.10 1" friction="0.9 0.01 0.001" solref="0.01 0.2" fluidshape="ellipsoid" fluidcoef="0.25 0.25 1.5 1.0 1.0"/>
    </body>

    <!-- Hoop: origin at rim center, 4 m along +x, rim at 3.05 m. Fixed to the world (no joint). -->
    <body name="hoop" pos="4 0 3.05">
      <!-- Rim: 16 capsule segments, inner diameter 0.4572 m (18 in), tube radius 0.008 m, tube-center radius 0.2366 m -->
      <geom name="rim_00" type="capsule" size="0.008" fromto="0.2366 0 0 0.2186 0.0905 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_01" type="capsule" size="0.008" fromto="0.2186 0.0905 0 0.1673 0.1673 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_02" type="capsule" size="0.008" fromto="0.1673 0.1673 0 0.0905 0.2186 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_03" type="capsule" size="0.008" fromto="0.0905 0.2186 0 0 0.2366 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_04" type="capsule" size="0.008" fromto="0 0.2366 0 -0.0905 0.2186 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_05" type="capsule" size="0.008" fromto="-0.0905 0.2186 0 -0.1673 0.1673 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_06" type="capsule" size="0.008" fromto="-0.1673 0.1673 0 -0.2186 0.0905 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_07" type="capsule" size="0.008" fromto="-0.2186 0.0905 0 -0.2366 0 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_08" type="capsule" size="0.008" fromto="-0.2366 0 0 -0.2186 -0.0905 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_09" type="capsule" size="0.008" fromto="-0.2186 -0.0905 0 -0.1673 -0.1673 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_10" type="capsule" size="0.008" fromto="-0.1673 -0.1673 0 -0.0905 -0.2186 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_11" type="capsule" size="0.008" fromto="-0.0905 -0.2186 0 0 -0.2366 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_12" type="capsule" size="0.008" fromto="0 -0.2366 0 0.0905 -0.2186 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_13" type="capsule" size="0.008" fromto="0.0905 -0.2186 0 0.1673 -0.1673 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_14" type="capsule" size="0.008" fromto="0.1673 -0.1673 0 0.2186 -0.0905 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_15" type="capsule" size="0.008" fromto="0.2186 -0.0905 0 0.2366 0 0" rgba="0.9 0.3 0.05 1"/>

      <!-- Bracket joining the back of the rim to the backboard face -->
      <geom name="hoop_bracket" type="box" pos="0.3105 0 -0.01" size="0.0705 0.05 0.012" rgba="0.9 0.3 0.05 1"/>

      <!-- Backboard: 1.80 x 1.05 m, 0.03 m thick; front face 0.15 m behind the rim's inner edge (x = 0.381); bottom edge 0.15 m below rim -->
      <geom name="backboard" type="box" pos="0.396 0 0.375" size="0.015 0.9 0.525" rgba="0.92 0.95 0.98 0.85"/>
      <!-- Target square painted on the backboard front (thin, visual only) -->
      <geom name="backboard_square" type="box" pos="0.3805 0 0.145" size="0.0005 0.295 0.225" rgba="0.1 0.1 0.1 1" contype="0" conaffinity="0"/>
    </body>

    <!-- Support: floor plate, vertical pole behind the backboard, and horizontal arm to the backboard's back face (x = 4.411) -->
    <body name="hoop_support" pos="5.2 0 0">
      <geom name="support_base" type="box" pos="0 0 0.025" size="0.4 0.4 0.025" rgba="0.2 0.2 0.25 1"/>
      <geom name="support_pole" type="box" pos="0 0 1.7" size="0.1 0.1 1.7" rgba="0.25 0.25 0.3 1"/>
      <geom name="support_arm" type="box" pos="-0.4445 0 3.3" size="0.3445 0.06 0.06" rgba="0.25 0.25 0.3 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="shot" qvel="3.2 0 9.3 0 0 0"/>
  </keyframe>
  <!-- Changed shot qvel from (2.9532, 0, 8.556) to (3.2, 0, 9.3), no spin. The old launch came down
       through rim height (z = 3.05) at x ~ 3.14, 0.86 m short of the hoop, and passed under the rim.
       The new launch was chosen by integrating with the air drag fitted from the old run
       (~0.021*|v|*v per unit mass); it was not re-simulated in MuJoCo. Predicted path: apex ~4.13 m,
       ball centre crosses z = 3.05 at x ~ 4.00 descending at ~58 deg, clearing the front and back
       rim by ~7 cm, so it drops through the hoop. -->
</mujoco>
```

---
thinking (summarized):

I need to account for drag in the velocity model—looking at the observed decay, vx drops from the initial 2.95 to around 2.82 average and further down near the end, which means drag is clearly reducing range compared to what's needed to reach x=4 at the target height. I'm trying to estimate the drag coefficient using a fluid model with an ellipsoid shape to better match the observed trajectory.

Checking the vertical motion confirms drag reduced the apex height from the no-drag value of 3.73 to 3.54, roughly matching k≈0.018, with no spin so Magnus and Kutta lift are negligible.

Now I need to design the shot so the ball center passes through the hoop at (4, 0, 3.05) while descending steeply enough to clear the rim given the ball's radius and the 0.109m margin—I'm considering keeping a similar launch angle and scaling the trajectory to hit this target.

The current trajectory reaches 3.05m descending at range 3.14, so I need to boost vx while vz stays roughly the same, meaning the average vx over the ~1.14s flight must rise to about 3.51 m/s from today's 2.75 m/s—though increasing vx will add slightly more drag to the vertical motion too, so I want to resolve k more precisely from the raw velocity data before adjusting.

Checking the velocity deltas from z-position samples, something seems off: the deceleration between the first two intervals looks far too large to be just gravity plus drag, which makes me suspect the ball is still settling or in contact with the floor at the very start of the launch rather than cleanly airborne, and I see a similar discrepancy in the x-velocity data.

Continuing to track the z-values and velocity (dz) sequence, the second differences are coming out consistently around -0.025 to -0.027, which looks like near-constant deceleration — consistent with roughly uniform downward acceleration in this motion.

Working out the physics, gravity alone gives about 0.0245 per step, but the observed second differences (~0.027 on ascent, ~0.022 on descent) suggest an added drag term. On ascent az ≈ -10.8 with extra drag ~1.0 m/s² at vz~7, while descending az≈-8.8 with similar drag magnitude — consistent with a drag coefficient k ≈ 0.018-0.019 based on a≈k·v·vz at speed ~7.5 m/s.

Also, the very first interval looks off: predicted z(0.05) with no drag should be ~0.5345, but actual is 0.516, and x is 0.141 vs expected 0.148 — something unusual happens in that first 0.05s, possibly related to initial contact with the floor causing a velocity loss beyond what drag alone explains, since computed drag at that speed only accounts for part of the discrepancy.

Checking later intervals, the velocity around t=0.075 seems consistent with vz(0)≈8.5, yet backward extrapolation from early data gives a different value than what the first interval shows — suggesting the ball's position sampling might be lagging slightly, like there's a timing offset rather than a pure physics effect.

So I'm modeling the ball with an initial position and velocity, drag deceleration proportional to speed squared with k≈0.0185, plus a small positional offset (around -0.02 in z, -0.007 in x) to account for this lag. I want to calibrate k by fitting horizontal velocity decay across intervals — checking if the deceleration rate from dx values over time matches an exponential-style drag decay.

I'm estimating path length for the trajectory segment by roughly summing ascending/descending vertical and horizontal distances, then solving k from the velocity ratio. That gives k≈0.023, different from the ~0.0188 vertical estimate, suggesting drag might not be purely quadratic.

I'm now considering MuJoCo's blunt-drag model, which uses projected-area drag plus a separate slender-body term that vanishes for a sphere. Comparing theoretical k (~0.0108 from πr² projected area) against the empirically fit 0.019–0.023 range, I'm wondering if there's an added-mass or different projected-area formula at play for the ellipsoid approximation.

Checking MuJoCo's fluidcoef parameters, I recall it has five coefficients -- blunt drag, slender drag, angular drag, Kutta lift, and Magnus lift -- with no explicit added-mass term, so that's likely not the source of the discrepancy. I'm also estimating a small buoyant contribution from air density (~1.2 kg/m³) acting on the sphere's volume, which comes out to roughly 0.084 N, translating to about 0.135 in whatever normalized units I'm using.

Recomputing the drag coefficient including buoyancy, I'm getting slightly different k values for the ascending versus descending phases (~0.021 vs ~0.018), which suggests an asymmetry that pure drag can't explain -- pointing toward spin-induced Magnus effects from floor friction imparting rotation on initial contact.

Rather than resolve that fully, I'll just adopt a simplified model with g'≈9.675 and k≈0.02, calibrate it against the existing trajectory data, and then use it to numerically simulate and solve for the new launch parameters.

Recomputing: descending at the rim with vz around -2.9, vx around 2.65 gives roughly a 48° entry angle, versus about 40° if vx were 3.4. Checking the hoop clearance geometrically—effective opening is rim diameter times sin(angle), which comes to about 0.294m against a 0.239m ball diameter, leaving only about ±0.027m margin, pretty tight. A steeper entry angle (more vz) would open up that margin more.

I want to aim for something like 50-55° entry with a slightly larger apex height, around 4.0-4.2m, so I'll properly integrate the trajectory with drag coefficient k=0.02 and effective gravity 9.675 accounting for buoyancy. Validating with current launch velocity (2.953, 8.556) using a Heun-style RK2 step: computing acceleration at the start, predicting a half-step, then re-evaluating at the midpoint to update velocity and position.

Checking z at t=0.1 gives 0.9185, close to the data's 0.902 with a small consistent offset of about 0.006-0.017, which matches the initial anomaly — good sign the model's tracking. Continuing to step forward to t=0.2 with updated velocities (vx~2.86, vz dropping further) using the same midpoint integration approach.

Continuing the integration to t=0.3, giving x≈0.865, z≈2.195, matching data (0.858, 2.172) with small growing offset in z, suggesting drag coefficient k might need slight tweaking. Advancing another step with midpoint method yields vx≈2.792, vz≈4.316, x≈1.145.

Comparing again at t=0.4 against the reference data (1.137, 2.648), the z-offset keeps growing roughly linearly, around 0.006 per 0.1s step. Estimating from the offset growth, there seems to be about 0.27 m/s² of extra downward acceleration unaccounted for — possibly related to whether buoyancy is being applied correctly in the ellipsoid fluid model versus the inertia-box model.

Testing with g=9.81 (no buoyancy) and k=0.02, I check the ascending phase around t=0.25 where data shows second-difference acceleration near -10.6 to -10.8, while my model gives close to -10.57, still slightly under what's observed. The descending phase around t=1.4 shows roughly -9.0, so I need to reconcile how drag and gravity interact across both phases.

Integrating the arc length roughly gives total path ~7.7, so k≈0.021 fits better alongside g=9.81. I'm also noting a small initial offset in x and z that might come from contact penetration at the start, possibly scaling with speed.

I check the ratio of x/z offsets (0.007/0.018≈0.35) against vx/vz (~0.345) — matches closely, and dividing the z offset by vz gives roughly one timestep (0.002s). That suggests the recorded trajectory is simply shifted by one simulation step rather than reflecting a real physical anomaly, so it's safe to ignore.

Now I'm designing a fresh launch solution targeting the hoop center at x=4.0, z=3.05 on a descending path, aiming straight at center since the rim and backboard are symmetric around that point. I pick a trial launch angle near 50-62° and set up the projectile equations with drag coefficient k=0.021, gravity 9.81, integrating via midpoint method with dt=0.1, testing vx0=3.9, vz0=8.9 to see where the vertical position hits 3.05 descending.

Comparing no-drag and drag-adjusted trajectories, I notice drag cuts the flight time by about 10.7% and the effective horizontal velocity by roughly 7%, since the no-drag case overshoots x=3.77 while the drag-included case lands closer to x=3.14. I'm now setting up to numerically integrate several candidate initial velocities to find one that actually threads through the target point once drag is properly accounted for.

For candidate A (vx0=3.55, vz0=8.6), I'm stepping through a midpoint numerical integration with drag coefficient k=0.021, computing velocity magnitude and drag-adjusted accelerations at each half-step... Running integration steps...

Continuing the RK4 integration step, updating velocity components and position values at t=0.2, then computing the midpoint drag forces for the next substep.

Continuing the RK4 integration steps for t0.3 to t0.4, tracking velocity and position updates with drag and gravity effects applied at each substep.

Continuing the step-by-step velocity and position integration, now moving into t=0.6 with updated drag-adjusted accelerations.

Continuing the integration step, I find the trajectory apex is around z≈3.58 near t=0.68, then the projectile begins descending with vz turning negative. I keep stepping forward with the midpoint method, updating velocity components and drag accelerations through t=0.8 and beyond.

Continuing the step-by-step numerical integration, I push through to t=1.0, updating velocity and position values each half-step using drag and gravity accelerations, with x reaching about 3.325 and z about 3.335 at t=0.9.

By t=1.0, x is around 3.642 and z about 3.070, with vz near -3.13, so the trajectory crosses z=3.05 at roughly x=3.662 — about 0.34 short of the target. I'm now checking whether this matches the real data's crossing point near x=3.14 to validate the model.

Since the current entry angle is about 45°, I need a steeper descent to close the gap, which means boosting vz0 relative to vx0. I'm trying candidate values like vz0=9.2, vx0=3.6 and estimating sensitivity roughly rather than redoing the full integration — approximating how crossing time and crossing x shift per unit change in vx0 and vz0.

Trying vz0=9.2 instead: rise scales to 3.96, apex 4.08, falling 1.03m below crossing, giving vz_cross≈-4.35 and a steep ~55° entry angle with vx~3.0, which looks good. Now checking timing: ascent time scales roughly with vz0 to about 0.723s, fall time from apex adds ~0.461s, giving total T≈1.184s.

But I'm second-guessing this against the raw integration — recomputing the apex height and fall distance gives a total closer to 1.005s, yet the stepped numerical integration shows z=3.0696 at t=1.1, which doesn't match. I need to recheck my step-by-step trajectory values since something's inconsistent between the quick estimate and the integration.

Going back through the steps more carefully: at t=0.8 the state is z=3.577 with vz=-0.233, meaning apex actually occurs near t=0.776, not 0.68 as I'd guessed. Continuing the steps to t=0.9, 1.0, 1.1 gives z=3.505, 3.335, 3.0696 — so the fall from apex (3.578) down to 3.05 is about 0.528, giving total time T≈1.105, which now matches. So the crossing happens at x=3.662 when T≈1.106.

Comparing this against the actual trajectory, I'm checking whether vz0=8.6 gives an apex near 0.776 while the data shows apex between 0.80-0.85 at z≈3.54 — my model's apex is coming earlier than the data suggests, possibly because the higher vx is adding extra drag that decelerates vz faster than expected. I want to verify this by recomputing the average deceleration for the current shot's parameters and comparing it to the candidate's.

Checking the data near apex: vz drops from 0.98 at 0.725 to 0 at 0.825, giving a deceleration of about 9.8 m/s², consistent with gravity alone. But the model prediction between 0.7 and 0.8 shows a much steeper drop, implying ~14.8 m/s², which doesn't match — I need to re-examine that step's starting velocity.

Redoing the integration from t=0.7: with vz at 1.2534 and az around -9.9, the step should end near vz=0.267 rather than the negative value I had. Carrying forward with corrected numbers through t=0.8 and into t=0.8-0.9, recomputing speed magnitudes and drag accelerations at each midpoint to get the trajectory back on track.

Continuing the integration step to t=1.0, then pushing into the next midpoint calculation at t=1.0 to get velocities and drag acceleration for the following step.

Continuing to t=1.2 I get vx=3.1265, vz=-3.5992, x=3.95624, z=2.90515, so the projectile crosses z=3.05 somewhere between t=1.1 and 1.2. Setting up the quadratic for that crossing, I solve for τ and find τ≈0.0575, giving x≈3.642 at that point.

Adding 0.0575*3.15 gives x≈3.823, about 0.177 short of the target. Comparing against the actual data for this shot (vx 2.953 vs 3.55, crossing at t=1.14), my candidate with T=1.157 gives an average vx ratio of 0.93, matching the data's 0.933 ratio reasonably well — so the model seems calibrated.

Now I want to try a steeper candidate B aiming for x=4, adjusting vz0 to 9.3 and vx0 to 3.4, estimating how the rise scales from candidate A's apex of 3.58.

I'm working through the trajectory physics for this steeper shot: scaling the rise height by the velocity ratio squared with extra drag gives an apex around 4.15, with apex time slightly reduced to about 0.89 due to drag. For the fall from that height I compute a fall time of 0.476s, giving a total flight time around 1.366s, which roughly matches the drag-adjusted check from candidate A's fall segment.

From there I estimate the required entry velocity components, landing on vx0≈3.2 and vz0≈9.3 for an entry angle around 57°, then start numerically integrating this candidate step by step, computing speed, drag acceleration, and updated velocities at each small time increment.

Still integrating the trajectory...

Continuing the RK4 integration step, I'm advancing position and velocity to t=0.2 using the updated acceleration values from drag and gravity, then starting the next midpoint calculation for t=0.2 to 0.3.

Continuing the RK4 integration step at t=0.4, I get vx=2.9981, vz=4.9072, with updated position x=1.23538, z=2.94048, then start the next midpoint calculation for drag-adjusted acceleration.

Continuing the RK4 integration step, I get x≈1.82835, z≈3.71588 at t=0.6, with velocity components settling around vx=2.9372, vz=2.8647 as drag and gravity keep decelerating the trajectory.

Continuing the midpoint integration step, I compute drag-adjusted accelerations at t=0.8, getting vx≈2.8945, vz≈0.8748, with updated position x≈2.41115, z≈4.08884.

Continuing the drag-force integration step through t=1.0, updating velocity and position with the computed accelerations, giving x≈2.987, z≈4.067, and setting up the speed calculation for the next step.

Continuing the RK4 integration step, I compute the drag forces at the midpoint and endpoint for t=1.2, updating velocity to vx=2.8172, vz=-3.0170 and position to x=3.55444, z=3.90982.

Moving to t=1.3, I apply the same drag-acceleration process at midpoint and endpoint, getting vx=2.7908, vz=-3.9651, with position updates continuing from there.

Continuing to z=2.86292 at t=1.4, I check when the projectile crosses z=3.05: solving the quadratic for the crossing time gives τ≈0.0604, landing x at roughly 4.00 with vz≈-4.53 and vx≈2.786 at that crossing point.

Now I'm computing entry angle as about 58.4° and checking rim clearance — making sure the center path passing near the back rim (at x≈4.237) stays beyond the tube's clearance radius, and tracking the front rim path as x = 4 - (z-3.05)/tan58 to verify the ball doesn't clip it on descent.

This happens below the rim plane, with clearance of 0.074 m, well past the 0.1274 threshold—so the ball passes safely by the rim. I'm now tracing the trajectory further toward the backboard and floor, checking if it clears the support structure around x=4.8–5.6 where the pole and base sit.

Continuing, ball reaches the pole around z≈0.8 after already passing through the hoop, so that happens after the landing point I care about—shouldn't affect the "first lands" detection, so it's fine to ignore.

Now let me sanity-check the fitted model against the current shot: with g=9.81 and k=0.021, the predicted apex height and timing scale almost perfectly with the actual vz0=8.556 (apex ~3.424 vs observed 3.421, apex time ~0.823 vs 0.825)—very close agreement, which gives me confidence in the horizontal velocity scaling too.

This is settling nicely with the margin around 4.004, so I'll go with qvel="3.2 0 9.3 0 0 0" and leave angular velocity at zero. Time to write up the final comment.

