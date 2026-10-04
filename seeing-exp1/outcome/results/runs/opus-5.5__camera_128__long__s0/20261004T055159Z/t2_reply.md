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
    <key name="shot" qvel="3.45 0 8.46 0 0 0"/>
    <!-- Changed shot qvel from (3.5952, 0, 10.416) to (3.45, 0, 8.46).
         Why: the old launch peaked near 5.6 m and was still about 2.5 m above the 3.05 m rim
         when it reached x = 4, so it sailed over the backboard and landed far past the hoop (long).
         How the new values were chosen: they target a flight of about 1.2 s that peaks near 3.6 m
         and comes down through the rim center at about 45 degrees.
         - With no drag, the target is vx = 3.33, vz = 8.25 m/s.
         - The air model (density 1.2, blunt coef 0.25) gives drag of about 0.011*v^2 m/s^2 and
           buoyancy of about 1.4 percent of g.
         - Integrating along the arc, that costs about 0.15 m of range and 0.24 m of height,
           so vx and vz were raised to make up for it.
         Expected result: at rim height the ball center is about 4.0 m out and descending.
         The ball can be off center by about 0.11 m and still clear the rim tube.
         It also clears the front rim on the way in, then falls through and lands below the hoop.
         Caveat: this is a hand estimate of the drag, not a run of the simulation. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to work out a launch velocity that carries the ball through the hoop, factoring in drag from MuJoCo's fluid model, starting near the ground and arcing up to the target around (4, 3.05) on a descending path—aiming for roughly a 55° launch angle.

Estimating the drag coefficient works out to about 0.0108 per v², with buoyancy effects reducing effective gravity slightly to about 9.675 m/s². I'm now setting up the no-drag projectile equations for horizontal and vertical motion to solve for a flight time and velocity that land the ball at the hoop, planning to correct afterward for drag's small effect.

Testing T=1.0s gives too shallow a descent angle (25°), but T=1.2s produces a clean 45° entry angle with velocities around 3.33 m/s horizontal and 8.25 m/s vertical, reaching an apex height near 3.6 meters - this looks like a solid baseline trajectory. Now I need to account for how drag will reduce the speed throughout the flight, roughly from 8.9 m/s initially down to about 3.3 m/s at apex and back up to 4.7 m/s near the hoop.

I'm setting up a perturbative numerical integration, computing drag decelerations in both x and z directions at small time steps (0.2s intervals) based on the speed-squared drag law, to estimate how much the trajectory deviates from the no-drag case.

Finishing Simpson's rule, I get Δx(T) ≈ -0.1525 m. Now computing the analogous integral for Δz using the same weighted products and Simpson coefficients, summing to roughly -3 before the final scaling.

So with drag included at t=1.2, I estimate x≈3.848, z≈2.814, which means I need to boost the initial vx and vz to compensate. Using rough sensitivities (∂x/∂vx≈1.2, ∂z/∂vz≈1.2), I adjust vx to about 3.47 and vz to about 8.46, then plan to recheck where the trajectory crosses the hoop height to confirm x lands near 4.0 at the rim.

Given the rim's inner radius and ball size, I calculate the ball must stay within about 0.109 m of the hoop's axis to avoid clipping the rim, so with the backboard close on the far side I should aim slightly short, targeting x≈3.98 rather than dead center. Rechecking with the updated vx=3.47, vz=8.46 and accounting for slightly higher drag at the increased speed, I expect the deviations to shrink to roughly Δx≈-0.16 and Δz≈-0.25 from the no-drag case.

Testing the trajectory at t=1.2s and correcting for drag gives x≈4.00 and z≈3.05, close to descending through the hoop, with negligible timing correction since vz is still around -3.4 there — so trimming vx down to 3.45 should land x closer to 3.98. I also need to confirm the ball clears the front rim on its way up, checking its height around x≈3.6-3.76 near the front rim location.

Checking clearance distances, I confirm the ball center stays far enough from both the front rim tube and the back rim tube (around 0.17-0.24 units away, both exceeding the 0.127 ball radius), so the trajectory should pass cleanly through the hoop without hitting either rim.

The ball's continued fall after passing through lands under the hoop without colliding with the bracket, since the bracket sits at x 4.24-4.38 and z 3.03-3.05, above the ball's actual descending path.

