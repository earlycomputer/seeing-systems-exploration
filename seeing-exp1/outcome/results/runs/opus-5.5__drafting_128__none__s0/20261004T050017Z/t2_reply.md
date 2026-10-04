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
    <key name="shot" qvel="3.6 0 8.75 0 0 0"/>
  </keyframe>
  <!-- Changed the shot key's qvel from "3.21 0 9.3 0 0 0" to "3.6 0 8.75 0 0 0".
       Old launch: too much vertical speed for its horizontal speed. The ball was still ~4.1 m high
       at x = 4 m, sailed ~1 m over the rim and struck the backboard face (a long miss).
       New launch: aimed at the rim centre (4, 0, 3.05) at t ~ 1.2 s, arriving on the way down.
       Drag compensation: I integrated the flight by hand, assuming the ellipsoid model's quadratic
       blunt drag F = 0.25 * rho * pi r^2 |v| v (about 0.022 |v| v per unit mass). That drag
       costs ~0.3 m of reach and ~0.45 m of height by the rim, so the launch speed was raised to
       make up for it.
       Predicted crossing: centre at x ~ 4.00, z ~ 3.05, moving (3.15, -3.5) m/s, i.e. ~48 deg
       downward.
       Clearances: ~0.23 m from the front rim tube and ~0.18 m from the back rim tube, versus
       0.127 m needed (ball radius 0.1194 + tube radius 0.008).
       Caveat: if MuJoCo's blunt-drag term includes an extra factor of 1/2, drag is half what I
       assumed and the ball would arrive ~0.2 m higher, so the result should be checked in
       simulation. -->
</mujoco>
```

---
thinking (summarized):

I need to find the launch velocity so the ball passes through the rim center at (4,0,3.05) while falling. Picking a launch angle around 55°, I'm setting up the no-drag trajectory equation with horizontal distance 4 and vertical drop to solve for the required speed.

Testing this gives a velocity where the ball is still rising at the rim, which won't work — I need it descending. Working through different flight times, I find that around t=1.2s produces a nice ~46° descent angle through the hoop with vx≈3.33 and vz≈-3.44, which gives good clearance. Now I need to account for drag effects on top of this ideal trajectory.

Since drag is nonzero for a sphere, I need to numerically simulate the trajectory with drag included rather than use clean projectile equations. I'm setting up a step-by-step integration with a drag coefficient around 0.0217, tracking velocity and position at small time increments to see how much the deceleration shifts the landing point from the no-drag estimate.

Continuing the drag integral for the z-displacement, I'm sampling the deceleration term at several time points and weighting by remaining time to approximate the total vertical correction from drag.

Applying Simpson's rule across these samples, the drag-induced displacement comes out to roughly -0.47 m, meaning the projectile lands lower than a drag-free trajectory would predict, and also arrives later since drag reduces speed throughout the flight. I'll need to compensate by bumping up the initial horizontal velocity proportionally to account for this delay.

Given the clearance tolerance of about ±0.1 m, and knowing overshoot can bank off the backboard while undershoot hits the front rim, I want to be careful about which direction to bias my correction. My estimates have enough uncertainty that I should just re-run the numerical integration with revised guesses for vx and vz to check the landing point more precisely.

Finishing the Heun step gives vx≈3.531, vz≈7.610 at t=0.1, with position x≈0.357, z≈0.937. Then I recompute the speed and drag acceleration at this new point to prepare for the next step, getting ax≈-0.643, az≈-11.20.

Using these predicted accelerations to advance again, I get vx≈3.471, vz≈6.508, updating position to x≈0.707, z≈1.643 at t=0.2. I'm recalculating the drag terms once more for the following step.

Continuing the position update: x=1.3909, z=2.732 at t=0.4, with drag deceleration computed similarly (ax≈-0.406, az≈-10.34), then moving to t=0.4 predictions with vx=3.334, vz=3.359 and smaller drag terms as velocity decreases.

Stepping forward through t=0.5 and t=0.6, I'm tracking position growing to x≈2.06, z≈3.41, with vx settling near 3.3 and vz dropping to about 2.36 as gravity and drag continue reducing vertical speed.

Continuing the drag-adjusted trajectory integration at t=0.7, computing speed-dependent acceleration and predicting velocities for the next step at t=0.8, with vx settling around 3.255.

Continuing the numerical integration at t=0.9, computing drag-adjusted velocities and positions, finding vx≈3.209, vz≈-1.583, with speed and acceleration terms feeding into the next step.

Continuing the step-by-step integration at t=1.1, updating velocity and position using the drag-adjusted accelerations, then projecting forward to estimate the next acceleration values at t=1.2.

At t=1.2 I get x≈3.997, z≈3.050 — remarkably close to the rim target, with a descent angle around 48°, which looks like a clean shot. I'm checking whether the ball clears the front rim by interpolating its position near x=3.77 (the rim's inner edge) to estimate its height there and compare against the rim's geometry.

Checking clearance against both front and back rim tubes confirms safe margins throughout the ball's path — distances stay above the rim tube radius threshold at every point I sample, so the trajectory passes cleanly through the hoop.

I'm second-guessing the exact MuJoCo blunt drag formula — whether it includes a ½ coefficient or not. I recall the docs specifying f_D = -C_D,blunt · ρ · A_proj · ||v|| · v without the ½ factor, and I'll proceed with that, though I should flag the uncertainty since using ½ instead would shift the ball's landing position noticeably (roughly +0.15 in x, +0.23 in z), possibly causing it to clip the back rim instead.

Checking the initial floor contact, the ball starts resting at z=0.1194, which touches the ground correctly, so that part looks fine.

