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
    <key name="shot" qvel="3.19778 0.27977 9.3 0 0 0"/>
  </keyframe>
</mujoco>
```


MuJoCo simulated the shot. Here is the ball's center every 0.05 s from launch to its first landing
(the last row is the landing):

| t (s) | x (m) | y (m) | z (m) |
|---|---|---|---|
| 0.00 | 0.000 | 0.000 | 0.119 |
| 0.05 | 0.153 | 0.013 | 0.552 |
| 0.10 | 0.310 | 0.027 | 0.974 |
| 0.15 | 0.466 | 0.041 | 1.367 |
| 0.20 | 0.621 | 0.054 | 1.733 |
| 0.25 | 0.774 | 0.068 | 2.071 |
| 0.30 | 0.926 | 0.081 | 2.382 |
| 0.35 | 1.077 | 0.094 | 2.667 |
| 0.40 | 1.227 | 0.107 | 2.925 |
| 0.45 | 1.376 | 0.120 | 3.157 |
| 0.50 | 1.525 | 0.133 | 3.363 |
| 0.55 | 1.672 | 0.146 | 3.544 |
| 0.60 | 1.819 | 0.159 | 3.699 |
| 0.65 | 1.965 | 0.172 | 3.830 |
| 0.70 | 2.111 | 0.185 | 3.935 |
| 0.75 | 2.255 | 0.197 | 4.015 |
| 0.80 | 2.400 | 0.210 | 4.071 |
| 0.85 | 2.544 | 0.223 | 4.101 |
| 0.90 | 2.687 | 0.235 | 4.108 |
| 0.95 | 2.830 | 0.248 | 4.090 |
| 1.00 | 2.973 | 0.260 | 4.047 |
| 1.05 | 3.115 | 0.273 | 3.980 |
| 1.10 | 3.257 | 0.285 | 3.889 |
| 1.15 | 3.398 | 0.297 | 3.773 |
| 1.20 | 3.539 | 0.310 | 3.634 |
| 1.25 | 3.678 | 0.322 | 3.471 |
| 1.30 | 3.818 | 0.334 | 3.284 |
| 1.35 | 3.954 | 0.348 | 3.077 |
| 1.40 | 4.034 | 0.423 | 2.926 |
| 1.45 | 4.113 | 0.498 | 2.753 |
| 1.50 | 4.191 | 0.571 | 2.555 |
| 1.55 | 4.270 | 0.643 | 2.334 |
| 1.60 | 4.349 | 0.713 | 2.089 |
| 1.65 | 4.427 | 0.781 | 1.821 |
| 1.70 | 4.506 | 0.846 | 1.530 |
| 1.75 | 4.584 | 0.910 | 1.216 |
| 1.80 | 4.662 | 0.971 | 0.880 |
| 1.85 | 4.740 | 1.030 | 0.522 |
| 1.90 | 4.818 | 1.087 | 0.142 |
| 1.90 | 4.824 | 1.091 | 0.111 |


Does the shot drop through the hoop? If not, which way does it miss: short (it falls before reaching the
hoop), long (it goes past the hoop), or left or right (as the shooter sees it, facing the hoop along +x,
so left is +y)? If it misses in more than one way, name the larger.

First say what you read in the numbers: where the ball goes and where it ends up. Then end your reply with a
```json block holding one object:

{"description": "<what you read in the numbers>", "goes_in": <true or false>, "miss": <"none", "short", "long", "left" or "right">, "evidence": <"numbers", "text", "both" or "none">}

`evidence` says where your answer came from.
