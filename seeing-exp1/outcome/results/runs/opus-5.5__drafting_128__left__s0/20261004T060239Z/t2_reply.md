The original launch carried the ball about 0.5 m past the rim and 0.4 m to its left. I set the sideways velocity to zero and lowered the forward and upward speeds so the ball comes down at the rim centre (x = 4 m). I worked this out by hand with an approximate air-drag model, not by running MuJoCo, so it should be checked in the simulator.

- **Forward speed:** 3.20 → 3.16 m/s.
- **Upward speed:** 9.3 → 9.0 m/s.
- **Path:** the apex is about 4.03 m. With drag, the ball comes back down through rim height at t ≈ 1.33 s and x ≈ 4.0 m. It descends at roughly 58°. At that angle the ball's centre stays about 0.20 m from both the front and back of the rim, more than the 0.127 m needed to clear the rim tube.
- **Main uncertainty:** whether my drag model matches the simulator's. Ignoring drag entirely, the same launch would land long, at x ≈ 4.46 m. The earlier picture showed the original shot coming down near x ≈ 4.5 m, which is closer to my drag estimate (4.55 m) than to the no-drag value (4.79 m). That agreement supports the correction, but it is not proof.

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
    <key name="shot" qvel="3.16 0 9.0 0 0 0"/>
    <!-- Changed qvel from "3.19778 0.27977 9.3 0 0 0" to "3.16 0 9.0 0 0 0".
         Why: the old shot came down about 0.5 m past the rim centre (long, into the backboard)
         and about 0.4 m to the shooter's left (+y).
         - vy 0.28 -> 0: removes the leftward drift so the ball stays on the y = 0 line through the rim.
         - vz 9.3 -> 9.0 and vx 3.20 -> 3.16: lower, slightly shorter arc. Apex about 4.0 m. Hand
           integration of the sphere's quadratic air drag (blunt coefficient 0.25, rho 1.2, about 4-5%
           horizontal loss) puts the ball back at rim height (3.05 m) at t about 1.33 s, x about 4.0 m.
         - Descent is about 58 degrees, so the ball centre stays about 0.20 m from the front and back rim
           (clearance needed 0.127 m) and does not reach the backboard at x = 4.381.
         Not checked in simulation; if MuJoCo's drag is weaker than assumed, the shot will land long. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to pick an initial velocity so the ball arcs into the hoop center at (4,0,3.05) while descending, factoring in a roughly 5% drag effect. I'll go with a higher arc, setting vz around 9.3 for an apex near 4.5 without drag, giving a descent time of about 1.5 seconds, then adjust vx upward slightly from the no-drag estimate of 2.672 to compensate for drag shortening the horizontal distance.

Thinking through MuJoCo's fluid drag model for a sphere: since the projected area equals the max cross-section for a sphere, the slender-body term vanishes and only the blunt drag term matters, scaling with the squared velocity. I'm also considering whether added mass or other fluid effects apply here, since MuJoCo's ellipsoid model includes several force components beyond simple drag that could affect the trajectory.

Computing the terminal velocity and drag coefficient, I get a moderate value suggesting significant but not extreme air resistance over the flight. Given the uncertainty in my earlier rough estimate, I should run a proper numerical integration of the trajectory with speed-dependent drag rather than relying on linear approximations, using small time steps to track how the horizontal distance evolves.

Continuing the drag-affected trajectory integration, I'm stepping through each 0.1s interval, recalculating speed, drag deceleration, and updating velocity and position—by t=0.3 the projectile has traveled about 0.83m horizontally and climbed to roughly 2.34m in height, with speed gradually dropping toward 6.4 m/s.

Continuing the step-by-step integration, drag keeps shrinking velocity's effect as speed drops toward around 2.78 m/s by t=0.8, with position creeping to roughly x=2.17, z=4.0.

By t=1.0s the projectile is near its peak, x≈2.70, z≈3.97, now descending as vz turns negative and drag force diminishes further; continuing to t=1.1s, x reaches about 2.96 with vz at -2.1 m/s.

Tracking further: by t=1.3s position is roughly x=3.49, z=3.19, with speed climbing past 4.8 m/s as the drop accelerates under gravity minus a shrinking drag correction.

Continuing the step-by-step integration, I find the trajectory crosses z=3.05 around t≈1.33s at x≈3.57, short of the target x=4. I'm now considering whether scaling the initial horizontal velocity up (so vx≈3.14) would get x closer to 4 at that crossing point, while noting drag complicates a simple linear scaling since it grows with speed.

Working through the loss fraction (~4.2%) from drag, I settle on vx≈3.16 as a reasonable fit, giving x≈4.0 at the crossing. I'm also checking the geometry of clearing the rim front edge, estimating the ball's descent angle (~58° from horizontal) and comparing that to the rim's inner radius and the ball's own radius to see if it can pass through without catching the rim.

Checking clearance at both the front and back rim points along the trajectory, the perpendicular distance from each rim point to the ball's path comes out around 0.201m, comfortably above the 0.127m minimum margin needed — so the shot should clear cleanly, settling on vx=3.16, vz=9.0 for the initial velocity.

Confirming the drag formula does use the ½ρ factor, consistent with standard documentation. Rechecking with slightly higher vx means more drag on vz too, so the crossing happens a touch earlier, around t≈1.32 — landing somewhere near x≈3.16.

