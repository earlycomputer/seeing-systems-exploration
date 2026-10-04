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
    <key name="shot" qvel="3.21 0 9.3 0 0 0"/>
    <!-- Changed qvel from "3.19778 0.27977 9.3 0 0 0" to "3.21 0 9.3 0 0 0".
         Main fix: lateral velocity vy set to 0. The old 0.28 m/s carried the ball ~0.36 m to the +y (left)
         side by the time it reached the hoop, far outside the ~0.11 m clearance between ball (r 0.119)
         and rim (inner r 0.229).
         Re-integrating the flight with the scene's quadratic drag (blunt coef 0.25, rho 1.2, area 0.0448 m^2,
         mass 0.62 kg) shows drag is stronger than in my first estimate: with vz = 9.3 the ball peaks at
         ~4.12 m and descends through rim height (z = 3.05) at t ~ 1.36 s, at x ~ 1.25 * vx.
         So the original vx was already close, and the real miss was left rather than long.
         vx is nudged to 3.21 m/s, which puts the descending ball's centre at x ~ 4.0 m, y = 0 at rim height,
         entering steeply (about 60 deg below horizontal) through the centre of the hoop. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need vy=0 and need to pick vx, vz so the ball drops through the rim at x=4 while accounting for drag. Working from the drag-free estimate with vz=9.3 giving t≈1.497 and vx≈2.672, I'm adjusting vx slightly higher since drag shortens the horizontal distance by roughly 0.2-0.3 m over that range.

I'm uncertain about MuJoCo's exact blunt drag coefficient formula, whether there's a factor of ½ or not, which changes my estimate of the velocity loss anywhere from 5% to 10%. Given that uncertainty and the tolerance from the ball's radius (~0.11 m margin), I'll settle on a middle-ground vx around 2.82-2.87 to compensate.

Checking the default fluidcoef value of 0.5 against the standard sphere drag coefficient of 0.47 suggests MuJoCo's blunt drag formula omits the ½ factor, meaning the scene's 0.25 coefficient corresponds to a realistic effective Cd of 0.5 for a ball.

That gives me a per-mass drag constant k≈0.0217. Now I'm setting up numerical integration of the trajectory with ax=-k·v·vx and az=-g-k·v·vz, stepping through time starting from vx=3.0, vz=9.3 to check if a steep entry angle keeps drag sensitivity manageable.

This is getting tedious with manual iteration, so I'm switching to tracking position and velocity at each 0.1s step, computing drag-adjusted acceleration from current speed and updating x,z accordingly, continuing the Euler integration forward.

Continuing the numerical integration, I update position to roughly x=1.159, z=2.941 at t=0.4, recalculating drag and acceleration terms at each step as velocity decreases.

Continuing the drag integration: at t=0.6 position reaches x=1.715, z=3.715 with velocity dropping to v=3.963, and stepping forward to t=0.7 the velocity components settle near vx=2.729, vz=1.852 as deceleration continues.

Continuing the simulation through t0.9 and into t1.0, drag and gravity keep eroding vertical velocity while horizontal speed decays slowly, pushing position to roughly x=2.531, z=4.123 at t0.9 and projecting further downward motion into the next step.

Continuing the drag-adjusted numerical integration, stepping forward to t=1.2 with updated velocity and position values, then predicting t=1.3's motion.

Continuing the position update, I find the trajectory crosses z=3.05 around t≈1.356 with x≈3.741, which falls short of the target x=4.0 by about 0.26. I'm trying to compensate by scaling up vx to roughly 3.21, though I realize this will also increase drag effects on both components, so the relationship isn't perfectly linear.

Actually the original miss is leftward only, not long - my drag estimate was overcorrecting. I'll set vy to 0 since that offset was causing the leftward error, and keep vx around 3.2, close to the original 3.198, trusting that's within tolerance given my integration uncertainty.

