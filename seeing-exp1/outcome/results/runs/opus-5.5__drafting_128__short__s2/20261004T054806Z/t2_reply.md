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
    <key name="shot" qvel="3.5 0 8.8 0 0 0"/>
    <!-- Changed qvel from (2.9532, 0, 8.556) to (3.5, 0, 8.8). The old values were a no-drag
         solution that reached rim height at x ~ 3.77 m even in vacuum. With the scene's air drag
         it actually fell to rim height near x ~ 3.3 m, so the shot landed short.
         The new velocity was integrated by hand, not run in MuJoCo, using:
           - blunt drag k = 0.25 * 1.2 * A / m ~ 0.0217 per m
           - buoyancy-reduced g ~ 9.675 m/s^2
         Predicted flight: apex ~ 3.76 m near x ~ 2.95 m; the ball centre comes down through
         z = 3.05 m at x ~ 4.02 m, entering at about 47 degrees.
         The ball fits through the rim if its centre is within ~0.11 m of x = 4 m (3.89 to 4.11 m),
         and the ball clears the front rim on the way in. The landing point depends strongly on
         drag (in vacuum this velocity would land long), so check the next render. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to account for drag since the apex heights differ noticeably (3.5 vs 3.85), suggesting meaningful air resistance. I'm working out the drag force using the ball's mass, cross-sectional area, and MuJoCo's ellipsoid fluid drag model with air density 1.2.

Running the numbers, a drag coefficient fit gives roughly 18% deceleration at 9 m/s, and comparing observed rim crossing (~3.2-3.5) versus the no-drag estimate (~3.77) tells me I need to aim for greater horizontal reach to compensate. I'm trying different drag coefficient values against the observed apex height to pin down a reasonable k value before finalizing the aim adjustment.

Checking the MuJoCo blunt drag formula without the ½ factor gives k≈0.0217 using the sphere's cross-sectional area and density. Since there's no spin, Kutta lift and Magnus effects should vanish by symmetry, though I should still check whether the ellipsoid model's added mass terms contribute.

Buoyancy from the fluid density reduces effective gravity by about 1.4%, giving g_eff≈9.675. Plugging k and g_eff into the apex height formula yields roughly 3.5 units above launch, which lines up reasonably well with my earlier visual estimate of 3.5, accounting for the extra horizontal speed.

Now I want to design the trajectory to hit the target near (4, 3.05) with a steep descent, so I'm manually stepping through the equations of motion with drag, trying launch velocities like vx=3.5, vz=8.8, and tracking position and speed over small time increments to see where it lands.

Continuing the numerical integration, updating position and velocity through the 0.6-0.7 interval with drag deceleration still being applied.

Continuing the step integration, I get x=2.639, z=3.755, with velocity dropping to vx=3.166, vz=.526 as drag and gravity keep decelerating the vertical component toward zero.

Continuing the drag coefficient calculation, I get velocity magnitude ~3.175 with updated acceleration components, then moving to the midpoint velocities for the next integration step.

Continuing the numerical integration, I'm tracking position and velocity through successive small time steps, watching the height drop toward 3.05 as drag and gravity shape the descent.

That puts the crossing at roughly x≈4.02, right near the center of the 3.89–4.11 window, with a steep entry angle around 47 degrees — good for clearance. Checking the ball against both rim edges confirms it clears the front at z≈3.3 and stays within the back rim's inner boundary, though I want to sanity-check how sensitive this result is to the drag coefficient by comparing against a zero-drag trajectory.

The picture estimate of apex and landing roughly matches the drag-model predictions, so I'll settle on 3.5 and 8.8 as the values to use.

