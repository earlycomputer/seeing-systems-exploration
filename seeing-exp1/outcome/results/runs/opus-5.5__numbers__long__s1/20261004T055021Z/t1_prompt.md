You are checking a shot in a physics scene against the brief it was written from.

<brief>
a regulation basketball on a floor, a hoop at 3.05 m, 4 m away, lit from above; the ball is launched from where it rests and drops through the hoop
</brief>

The scene launches the ball with the keyframe named `shot`: MuJoCo resets to that keyframe and simulates
from there, with gravity and air, until the ball first lands. The scene text, as currently loaded:

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
    <key name="shot" qvel="3.5952 0 10.416 0 0 0"/>
  </keyframe>
</mujoco>
```


MuJoCo simulated the shot. Here is the ball's center every 0.05 s from launch to its first landing
(the last row is the landing):

| t (s) | x (m) | y (m) | z (m) |
|---|---|---|---|
| 0.00 | 0.000 | 0.000 | 0.119 |
| 0.05 | 0.172 | -0.000 | 0.605 |
| 0.10 | 0.348 | -0.000 | 1.081 |
| 0.15 | 0.523 | -0.000 | 1.527 |
| 0.20 | 0.696 | -0.000 | 1.945 |
| 0.25 | 0.868 | -0.000 | 2.334 |
| 0.30 | 1.038 | 0.000 | 2.696 |
| 0.35 | 1.206 | 0.000 | 3.030 |
| 0.40 | 1.373 | 0.000 | 3.337 |
| 0.45 | 1.539 | 0.000 | 3.617 |
| 0.50 | 1.704 | 0.000 | 3.871 |
| 0.55 | 1.868 | 0.000 | 4.099 |
| 0.60 | 2.031 | 0.000 | 4.301 |
| 0.65 | 2.193 | 0.000 | 4.477 |
| 0.70 | 2.354 | 0.000 | 4.628 |
| 0.75 | 2.514 | 0.000 | 4.754 |
| 0.80 | 2.674 | 0.000 | 4.855 |
| 0.85 | 2.833 | 0.000 | 4.931 |
| 0.90 | 2.992 | 0.000 | 4.982 |
| 0.95 | 3.150 | 0.000 | 5.009 |
| 1.00 | 3.307 | 0.000 | 5.011 |
| 1.05 | 3.464 | 0.000 | 4.989 |
| 1.10 | 3.620 | 0.000 | 4.942 |
| 1.15 | 3.776 | 0.000 | 4.871 |
| 1.20 | 3.931 | 0.000 | 4.775 |
| 1.25 | 4.086 | 0.000 | 4.656 |
| 1.30 | 4.240 | 0.000 | 4.513 |
| 1.35 | 4.393 | 0.000 | 4.345 |
| 1.40 | 4.545 | 0.000 | 4.155 |
| 1.45 | 4.697 | 0.000 | 3.940 |
| 1.50 | 4.847 | 0.000 | 3.703 |
| 1.55 | 4.993 | -0.000 | 3.460 |
| 1.60 | 5.038 | 0.000 | 3.527 |
| 1.65 | 5.075 | 0.000 | 3.584 |
| 1.70 | 5.112 | 0.000 | 3.615 |
| 1.75 | 5.150 | 0.000 | 3.622 |
| 1.80 | 5.187 | 0.000 | 3.603 |
| 1.85 | 5.224 | 0.000 | 3.561 |
| 1.90 | 5.264 | 0.000 | 3.515 |
| 1.95 | 5.316 | 0.000 | 3.521 |
| 2.00 | 5.368 | 0.000 | 3.503 |
| 2.05 | 5.420 | 0.000 | 3.460 |
| 2.10 | 5.471 | 0.000 | 3.392 |
| 2.15 | 5.522 | 0.000 | 3.300 |
| 2.20 | 5.573 | 0.000 | 3.183 |
| 2.25 | 5.623 | 0.000 | 3.042 |
| 2.30 | 5.673 | 0.000 | 2.877 |
| 2.35 | 5.721 | 0.000 | 2.688 |
| 2.40 | 5.769 | 0.000 | 2.475 |
| 2.45 | 5.817 | 0.000 | 2.239 |
| 2.50 | 5.863 | 0.000 | 1.979 |
| 2.55 | 5.908 | 0.000 | 1.696 |
| 2.60 | 5.952 | 0.000 | 1.391 |
| 2.65 | 5.994 | 0.000 | 1.063 |
| 2.70 | 6.036 | 0.000 | 0.713 |
| 2.75 | 6.076 | 0.000 | 0.341 |
| 2.78 | 6.099 | 0.000 | 0.107 |


Does the shot drop through the hoop? If not, which way does it miss: short (it falls before reaching the
hoop), long (it goes past the hoop), or left or right (as the shooter sees it, facing the hoop along +x,
so left is +y)? If it misses in more than one way, name the larger.

First say what you read in the numbers: where the ball goes and where it ends up. Then end your reply with a
```json block holding one object:

{"description": "<what you read in the numbers>", "goes_in": <true or false>, "miss": <"none", "short", "long", "left" or "right">, "evidence": <"numbers", "text", "both" or "none">}

`evidence` says where your answer came from.
