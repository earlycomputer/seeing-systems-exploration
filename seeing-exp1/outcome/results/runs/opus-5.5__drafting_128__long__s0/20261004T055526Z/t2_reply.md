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
    <key name="shot" qvel="3.7 0 8.61 0 0 0"/>
  </keyframe>
  <!-- Changed the shot key's qvel from "3.5952 0 10.416 0 0 0" to "3.7 0 8.61 0 0 0".
       Why: the old launch was far too steep and fast. Without drag the ball would still be at
       about z = 5.6 m when it reached x = 4 m, so it overflew the rim and came down at the
       backboard and support (a long miss).
       New launch: about 9.4 m/s at about 67 deg. I estimated air drag from the ball's ellipsoid
       fluid model, taking the drag force as about 0.25 * 1.2 * pi * 0.1194^2 * v^2, which is
       about 0.022 v^2 m/s^2 of deceleration. I treated it as an approximately linear drag with
       rate about 0.14 per second.
       With that estimate the ball reaches x = 4 m at about t = 1.17 s, at z of about 3.05 m.
       It is descending there at about -3.3 m/s vertical and about 3.1 m/s horizontal, which is
       an entry angle of about 45 deg into the rim.
       There is no y component, so there is no left/right error.
       Caveat: the exact MuJoCo drag prefactor was not verified. If the re-render shows the ball
       slightly short or long, scale vx and vz together by a few percent. -->
</mujoco>
```

---
thinking (summarized):

I'm working out the launch angle and velocity needed to hit the target point, ignoring drag for a first estimate—testing a 55° angle and solving for the required speed using projectile motion equations.

Then I'm factoring in air resistance using a simplified drag model based on the ellipsoid's cross-sectional area, estimating the velocity loss over the flight path, and compensating by boosting the initial speed roughly 3-4% to account for that decay, settling on a trial velocity with corresponding horizontal and vertical components.

Working through the drag-adjusted trajectory, I'm computing the time to reach the target horizontal distance and checking the resulting height, getting a value very close to the desired landing point of 3.05, which confirms the compensated speed is close to correct.

Let me try steeper launch angles to get a proper descending arc: at 60° the velocity still isn't steep enough, giving a shallow descent at the hoop. Trying 65° gives a required speed around 8.82 with vertical velocity component dropping sharply, which looks more like genuine descent into the hoop.

Checking 68° now gets me closer to a realistic entry angle near 45°, which feels right for a swish. Now I need to account for air drag, estimating a drag coefficient based on average speed and working out initial horizontal/vertical components that satisfy the flight time equation with that resistance included.

Speed drops from about 9.2 to 4.7 over the trajectory, averaging around 7, so the approximation holds reasonably well. I'm second-guessing the exact drag coefficient formula MuJoCo uses for ellipsoid blunt drag — whether it's 0.5 times density times area times velocity squared, or without the factor of a half.

Checking the rim clearance: inner radius 0.2286 minus ball radius 0.1194 gives about 0.109 m of horizontal room, though the 47° entry angle reduces the effective margin. Testing with doubled drag coefficient (k=0.0216, c=0.152), the horizontal distance comes up short by about 0.17 m, so I'm leaning toward a middle value around k=0.0108, with buoyancy being negligible at about 0.009 N.

I'm second-guessing the MuJoCo drag formula itself — recalling that the default fluidcoef sets blunt drag to 0.5, and here it's configured to 0.25 instead. For a sphere only the blunt term matters, and if the formula omits the usual 1/2 factor, an input of 0.25 is physically equivalent to a standard Cd of 0.5, meaning my original k might be off by a factor of two from using 0.5*0.25.

Recomputing with the corrected coefficient gives c ≈ 0.15, so I try vx0 = 3.75 and work through the exponential decay equations to find the time to reach the hoop, solving for vz0 that satisfies the vertical drop equation. This gives vz0 ≈ 8.65, and checking the velocity components at the hoop shows an entry angle near 45°, which is the target I wanted.

