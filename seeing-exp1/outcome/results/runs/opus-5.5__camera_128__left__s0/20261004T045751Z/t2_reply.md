I changed the `shot` key's `qvel` to `3.45 0 8.55`, which should drop the ball through the hoop. I checked this with a hand integration of the flight including air drag; I did not run it in MuJoCo.

- **What was wrong:** The old launch carried the ball about 1 m above the rim at x = 4 m, so it hit the backboard. It also drifted about 0.35 m to +y (left), more than the rim's 0.229 m inner radius.
- **Drag estimate:** The ball's drag works out to roughly 0.0108·v² m/s², so it loses some speed but not much.
- **What the new launch does:** The y component is now zero, so there is no sideways drift. The ball peaks at about 3.65 m near x ≈ 2.8 m. It comes down through the rim plane (z = 3.05 m) at about x ≈ 4.0 m, about 1.2 s after launch, falling at about 45°. It clears the front rim, the back rim, the bracket and the backboard.

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
    <key name="shot" qvel="3.45 0 8.55 0 0 0"/>
    <!-- Changed qvel from "3.19778 0.27977 9.3 0 0 0" to "3.45 0 8.55 0 0 0".
         The old launch was about 1 m too high at x = 4 m and hit the backboard above the rim (long).
         It also drifted about 0.35 m to +y, more than the rim's 0.229 m inner radius (left).
         The new launch has no y component and a lower, slightly faster arc, with the blunt drag
         (about 0.0108*v^2 m/s^2) accounted for. By hand integration it peaks at about z = 3.65 m,
         passes the rim plane (z = 3.05 m) at x of about 4.0 m around t = 1.2 s, falling at about
         45 degrees, and clears the front rim, back rim, bracket and backboard. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out the launch velocity needed for the ball to reach the rim with a descending trajectory, accounting for both gravity and drag forces acting on the ball's motion through the air.

For the sphere, since projected area equals max area, the drag coefficient simplifies nicely, giving me a drag constant around 0.01084 per unit mass. Testing a no-drag trajectory with T=1.2s gives reasonable entry angles around 46°, so I'm bumping up the initial velocities slightly to compensate for drag and now stepping through a numerical integration to verify the trajectory lands correctly at the rim.

Continuing the midpoint Euler integration for step 3, updating velocities and position with drag deceleration, getting vx near 3.37-3.39 and vz dropping toward 6.0-6.5 as gravity and drag continue reducing vertical speed.

Continuing the numerical integration through steps 6 and 7, I'm tracking velocity and position decay with drag: by step 6 the projectile reaches roughly x=2.02, z=3.45, and step 7 shows the vertical velocity continuing to drop toward around 2.0 while drag coefficient and horizontal velocity keep shrinking slightly each step.

Continuing the integration through steps 10 and 11, the trajectory now reaches x≈3.656, z≈3.469 with vz turning more negative as the projectile descends, while vx continues its gradual drag-induced decay.

At step 12, I check whether this trajectory clears the rim near x=4, z≈3.05—landing roughly 0.11 m too high in z or about 0.1 m long when I solve for the exact target height, so it looks like this particular shot falls just short of threading the hoop given the rim's inner radius of 0.229 m.

I decide to reduce the initial vertical velocity slightly, estimating from the sensitivity of z to vz that dropping vz by about 0.1 (to roughly 8.55) should lower the landing height by the needed 0.11 m at x=4 without meaningfully disturbing the horizontal velocity.

Checking the trajectory against the front rim and backboard clearances, the ball's path stays comfortably clear of the front rim edge and passes with sufficient margin past the backboard's bottom and face, so the adjusted velocity seems sound.

Distance checks out clear of the bracket corner too. The ball resting on the floor at launch position looks fine, so I'll note that in a comment.

