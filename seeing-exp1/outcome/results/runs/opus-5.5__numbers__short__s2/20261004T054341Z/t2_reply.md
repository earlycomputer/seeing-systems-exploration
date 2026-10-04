The new launch velocity was chosen with a drag model fitted to the simulated track, not re-simulated in MuJoCo, so it still needs a run to confirm. I fitted quadratic drag (k ≈ 0.02 /m) to the original trajectory. The fit reproduces its early positions and its average horizontal speed after the apex to within about 0.005 m/s.

**Predicted trajectory for qvel = (3.36, 0, 9.0)**
- The apex rises to about 3.90 m.
- On the way down the ball should cross rim height (3.05 m) at x ≈ 4.00. That is the rim center, entering at about 50° below horizontal.

**Clearances**
- The ball's center line should pass about 0.18 m from the front and back rim tubes. Clearing a tube takes 0.127 m.
- It should also clear the bracket and the bottom edge of the backboard.
- The tolerance on the crossing point is roughly ±0.07 m along x.

After it drops through, the ball will probably hit the support pole on the way down. That happens after it has passed through the hoop.

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
    <key name="shot" qvel="3.36 0 9.0 0 0 0"/>
    <!-- Changed shot qvel from (2.9532, 0, 8.556) to (3.36, 0, 9.0).
         The old launch fell short: the ball came down through rim height (3.05 m) at x ~3.14 m,
         0.86 m before the rim center, and passed under the hoop.
         Using quadratic air drag fitted to that simulated track (k ~0.02 /m), the new velocity
         should peak near z ~3.90 m and cross rim height on the descent at x ~4.00, the rim center,
         at about 50 deg below horizontal. That leaves ~0.18 m between the ball's center line and
         the front/back rim (0.127 m needed) and clears the bracket and the backboard's bottom edge.
         Predicted from the fitted model, not yet re-simulated. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm recalculating the velocity needed to account for drag, since the current shot falls short by 0.86 m at rim height. Comparing the drag-affected trajectory to the no-drag case shows a meaningful velocity loss over time, so I need to factor in how much the fluid resistance is slowing the shot down.

Working through a quadratic drag model, I'm estimating the deceleration coefficient by looking at how the x-position increments shrink slightly over successive time steps, which should let me back out the drag constant k from the data.

Estimating k again with the early high-velocity data gives a similar range of 0.03-0.04, so I'm now checking this against the physical drag formula MuJoCo uses, computing the projected area from the body's radius to see if the coefficient matches a plausible blunt-drag model.

Since the apex occurs earlier (t≈0.825 vs 0.872 without drag) and at a lower height (3.54 vs 3.85), I'm trying to back out k by fitting the ascent equation with an average speed estimate, since the simple area-based calculation alone doesn't fully explain the discrepancy -- there may be additional viscous or slender-body drag contributions.

Finishing that integral gives 707.6/25.67 ≈ 27.6, so k ≈ 0.56/27.6 ≈ 0.0203 — roughly k ≈ 0.02. Now I'm sanity-checking against horizontal drag: with v averaging around 6, k·v·vx gives an average ax near -0.34, producing a predicted x-loss of about 0.47 over the flight, but I need to compare that to the actual observed loss of 4.93 - 4.498.

Now I'm setting up a new shot design: rim center at (4, 3.05), ball starting at (0, 0.119), needing a descending trajectory through the rim with enough angle to clear the front rim tube at x ≈ 3.763, z = 3.05, accounting for ball radius versus inner rim radius for proper clearance.

I'll first estimate a drag-free solution with a steep descent angle around 45°, picking trial velocities like vx0 ≈ 3.6 and vz0 ≈ 8.6, then solving the vertical equation for time of flight to hit z = 3.05, before correcting for the k ≈ 0.02 drag coefficient.

I'm deciding to numerically integrate with k=0.02 using a Heun-type scheme at dt=0.1, but first I want a shortcut: estimate drag loss by comparing against the drag-free descending crossing time of z=3.05, computing t≈1.276 and x≈3.768 as a baseline reference.

Comparing that against the actual drag-affected crossing (t≈1.144, x≈3.146) gives a scale factor of roughly 0.835 for x, suggesting similar scaling could apply to nearby trajectories. I'm now setting up to test a candidate shot with vx=3.4, vz=9.0, integrating acceleration from drag using v=sqrt(vx²+vz²) with ax=-k·v·vx and az=-9.81-k·v·vz, starting by validating k against the original trajectory's first step where v≈9.051.

I'm computing predictor and corrector values for velocity and acceleration at each step, averaging them to update position and velocity — continuing the numerical integration...

But comparing to the actual data, the model's predicted z drop doesn't match the real trajectory, suggesting an extra loss mechanism like floor contact friction or initial impact that isn't captured by drag alone. I'm cross-checking vx values at small time intervals against the actual data to see where the discrepancy originates.

I'll just treat it as a positional offset rather than a velocity change, since later velocities line up fine with the model — not worth chasing further. Moving on to check the drag coefficient k across the rest of the flight: for step 2 (0.1→0.2), velocity comes out to about 7.985 m/s, so I'm computing the corresponding acceleration to see if it's consistent.

That confirms k≈0.02 holds well, matching both position checks within error. Now I'll move to designing the new shot, trying candidate velocities vx=3.4, vz=9.0 and integrating forward to see where it crosses the rim height at the target distance.

Let me try a faster initial velocity for the new shot and numerically step through the trajectory with drag, computing acceleration from speed-dependent drag terms at each small time increment to track position and velocity evolution toward the crossing point.

Continuing the predictor-corrector step for drag and gravity, I compute new velocity estimate giving ax=-0.5706, az=-11.1542, then predict forward velocities and recompute drag forces at the new point, averaging to get ax=-0.5317, az=-10.9888 for this substep.

Using these averaged accelerations I update position to x2=0.6682, z2=1.6939, then move to the next integration stage S2 with vx=3.2857, vz=6.7666, recomputing speed and drag-adjusted accelerations (ax=-0.4943, az=-10.828) to begin another prediction step.

z3 = 2.3171. Continuing to step S3 at t=0.3 with vx=3.2398, vz=5.6975, I compute drag-adjusted accelerations ax=-0.4247, az=-10.5568, then predict forward velocities vx=3.1973, vz=4.6418 and recompute accelerations for the next averaging step.

Averaging accelerations gives ax=-0.39255, az=-10.445, yielding vx4=3.2005, vz4=4.653, then updating position to x4=1.3165, z4=2.8346 at t=0.4. Now I'm starting the S4 step, computing speed and drag acceleration for vx=3.2005, vz=4.653, getting ax=-0.3615 so far.

z5 finalizes to 3.2487. Continuing the Euler integration into step 5 (t=0.5), I compute acceleration from velocity components, then predict the next step's velocity and begin recalculating acceleration for that prediction.

Computing drag-adjusted accelerations for the predictor step at t=0.6, then averaging to get vx7 and vz7, and starting the position update for x7.

Computing the averaged acceleration gives ax=-0.20705, az=-9.8868, yielding vx8=3.0946, vz8=0.6331, with updated position x8=2.5734, z8=3.8860. I continue into step S8 at t=0.8, recalculating velocity magnitude for the next predictor stage.

Updating position: x9 = 2.8819, z9 = 3.9002, continuing the integration at t=0.9 with vx=3.0753, vz=-0.3488 and recomputing drag acceleration there to predict the next step.

Continuing the integration step, at t=1.0 I get vx≈3.0556, vz≈-1.3243 with v≈3.330, giving ax≈-0.2035 and az≈-9.7218. Projecting forward with these accelerations, the predicted velocities become vx≈3.0353, vz≈-2.2965, so I'm recomputing v, ax, and az again for the next correction step.

Continuing the predictor-corrector integration, I get az=-9.6357, then predict vx12≈3.0108, vz12≈-3.2558, giving acceleration averages ax=-0.2489, az=-9.57845, updating vx12=3.0090, vz12=-3.2500, and starting the x12 position update with x12≈3.4930+0.30215.

Now computing z12=3.6357-0.27711=3.3586, then moving to the next step at t=1.2: recomputing velocity magnitude v≈4.429 and accelerations ax=-0.2665, az=-9.5221, then predicting vx=2.9824, vz=-4.2022 with v≈5.153 for the next acceleration estimate.

I average the accelerations to get vx13=2.9803, vz13=-4.1950, giving x13=4.0947 and z13=2.9864. Since z drops from 3.3586 to 2.9864 across this interval, I'm now checking where it crosses z=3.05, which requires a drop of 0.3086 from the starting height.

Solving the quadratic for time τ gives roughly 0.0845s, landing x at approximately 4.0485 at the crossing point, and I'm now applying small offsets (-0.006 in x, -0.017 in z) to adjust for the shifted crossing timing.

I'm checking clearance against the back rim tube — at a descent angle near 50°, I need the ball's path to stay at least the tube radius away from the rim point at roughly (4.2366, 3.05), so this is really a geometric tolerance check on whether the shot clears the rim cleanly.

Continuing the trajectory, z drops to about 2.74 by the time it reaches the backboard's bottom edge height of 2.9, giving a clearance distance of about 0.2 against the corner—just enough since the ball radius is 0.119. So it looks like the ball barely clears the backboard's bottom edge.

I'm also checking the mounting bracket box near the hoop (roughly x 4.24–4.381, z 3.028–3.052), computing the perpendicular distance from the ball's path to its nearest corner to make sure the ball doesn't clip it either.

With margins fairly tight (around 0.03), I think aiming for a crossing point near x_cross ≈ 3.97-3.98 would give better clearance on both sides. Now I want to verify the ball also clears the front rim on its way down—checking the ball's height as it passes x=3.763 given its trajectory slope.

I'm adjusting vx slightly downward by about 0.04 to shift the crossing point by roughly 0.05, landing at vx0=3.36, vz0=9.0 with expected crossing near x≈3.978. I should also sanity-check this k-model against the original's later-stage data since I've only validated it against early ascent and apex timing so far.

Looking at the original trajectory's velocity decay near the end of flight, I'm comparing drag-free versus actual dx values at different time points — like dx between 1.60-1.65s giving vx≈2.46 versus earlier intervals giving vx≈2.88 — to see how much drag grows as speed increases near impact when vz is large (~-7.5).

The data between close time points is too noisy for reliable derivatives, so I'm switching to longer baselines (comparing dx over 0.2s spans instead of 0.05s) to get a cleaner estimate of dvx and thus the drag acceleration, checking it against the predicted ax = -0.02·v·vx model at the corresponding average speed.

I'm integrating the drag deceleration numerically across time steps, computing velocity magnitude and the resulting ax at each interval, then tracking vx as it slowly decreases from the apex value toward the later measurement point to see if it's consistent with the model.

Using Simpson's rule on these intervals gives an average vx of about 2.5985, matching the observed data average of 2.594 very closely — the drag model checks out well. I also sanity-check the vertical descent against a drag-free free-fall estimate (3.338 m drop vs 3.244 observed), which seems plausible once drag is accounted for.

Now I'm testing a slight sensitivity adjustment: lowering initial vx from 3.4 to 3.36 and rescaling the average velocity gives roughly 3.114, producing a crossing position near x=4.000, close to target.

Crossing time itself barely shifts since vz is unaffected, so with the offsets applied I get about 3.980 — close enough. I'm puzzled about the early discrepancy though: in the original trajectory, x drops by 0.006 and z by 0.017 within the first 0.05s, which seems odd for a ball just contacting the floor, since contact forces should push rather than pull it down. I'm wondering if this stems from drag modeling instead, where the expected z at t=0.05 would be roughly 0.119 plus 8.556 times 0.05.

Checking the arithmetic, that gives 0.5326 versus the actual 0.516, which doesn't quite match — so I'm testing whether the sample was actually taken at 0.048s instead of 0.05s (maybe an off-by-one step issue). Dividing out x and z differences by their respective velocities both give 0.048, which confirms that timing shift. Applying that corrected timing to t=0.10 gives x=0.2928 versus 0.287, a diff of 0.0058, consistent with the same step offset.

The small discrepancies likely come from my Heun integration error rather than real trajectory offset, so x_cross ≈ 4.00 with vx=3.36 seems like a solid estimate, maybe nudging slightly short given typical bias. Checking rim tolerance, the path through (4.0, 3.05) with direction (0.64, -0.77) gives a perpendicular distance to the front rim of 0.182, comfortably clearing the 0.127 margin by about 0.055.

Checking back rim, bracket, and backboard corners confirms all margins hold with the aim at center (vx=3.36, vz=9.0), giving roughly ±0.07 m of lateral clearance. The apex comes out to 3.90 m against a 3.05 m rim height, yielding about a 49° entry angle, which looks good.

Tracing the ball after it passes through the hoop, I'm checking whether it eventually lands on the support base or pole — working out the fall time from the crossing point (4.0, 3.05) with vz=-3.65, vx=2.98 gives t≈0.485s and a landing x of about 5.41, which seems to clear the front of the pole.

Actually checking more carefully, the pole face sits at x=5.1, so the ball's center reaches x≈4.98 at t≈0.335s, putting it at z≈1.30 — meaning it strikes the pole after already passing through the hoop. Since the shot already counted as going through the rim, this is fine; I just need to verify the ball's ascent path doesn't clip the rim from below before that.

