Here is a MuJoCo MJCF scene written for this brief:

<brief>
a regulation basketball is launched from the floor and drops through a hoop at 3.05 m, 4 m away
</brief>

MuJoCo loads the file, resets to the keyframe named `start` if there is one, and simulates it for 6 s.
Nothing else acts on the scene: whatever moves is set moving by the scene itself, for example by a keyframe
velocity, a spring, gravity, or a motor whose control the keyframe sets.

It follows a few conventions so the other tools can find things. They fix names and axes, not what is built:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- The ball is a body named `ball` with a `<freejoint/>` and one sphere geom named `ball`. The hoop is a body named `hoop` whose origin is the center of the rim; every rim geom is named with the prefix `rim`.
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures,
  `<default>` classes or `<include>`.
- Every body and geom has a name, and each element's attributes are on a single line.
- `<option timestep="0.002"/>`.

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
    <key name="start" qvel="3.21 0 9.3 0 -30 0"/>
  </keyframe>
</mujoco>
```

If you send a corrected file, keep these conventions.


MuJoCo ran the scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.12) m, moving 9.84 m/s (vx +3.21, vy +0.00, vz +9.30)

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  ball leaves floor
 0.93 s  ball is at the top of its flight, at (2.30, 0.00, 4.31) m
 1.47 s  ball passes 0.18 m from hoop (hoop.rim_07) without touching it: nearest points (3.59, 0.00, 2.98) m and (3.76, 0.00, 3.05) m
 1.89 s  ball touches floor again
 1.91 s  ball leaves floor
 2.12 s  ball is at the top of its flight, at (4.60, 0.00, 0.34) m
 2.33 s  ball first touches hoop_support.support_base
 2.35 s  ball leaves hoop_support.support_base
 2.36 s  ball touches floor again
 6.00 s  ball is still moving at the end, 0.53 m/s

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 0.12) m, moving 9.84 m/s (vx +3.21, vy +0.00, vz +9.30); touching floor
0.25 s: ball at (0.73, 0.00, 2.09) m, moving 7.15 m/s (vx +2.68, vy +0.00, vz +6.62); touching nothing
0.50 s: ball at (1.35, 0.00, 3.43) m, moving 4.74 m/s (vx +2.35, vy +0.00, vz +4.11); touching nothing
0.75 s: ball at (1.92, 0.00, 4.16) m, moving 2.76 m/s (vx +2.19, vy +0.00, vz +1.69); touching nothing
1.00 s: ball at (2.46, 0.00, 4.29) m, moving 2.25 m/s (vx +2.14, vy +0.00, vz -0.68); touching nothing
1.25 s: ball at (2.99, 0.00, 3.82) m, moving 3.73 m/s (vx +2.17, vy +0.00, vz -3.03); touching nothing
1.50 s: ball at (3.55, 0.00, 2.78) m, moving 5.76 m/s (vx +2.26, vy +0.00, vz -5.30); touching nothing
1.75 s: ball at (4.12, 0.00, 1.19) m, moving 7.81 m/s (vx +2.38, vy +0.00, vz -7.44); touching nothing
2.00 s: ball at (4.53, 0.00, 0.26) m, moving 1.34 m/s (vx +0.58, vy +0.00, vz +1.21); touching nothing
2.25 s: ball at (4.67, 0.00, 0.26) m, moving 1.38 m/s (vx +0.58, vy +0.00, vz -1.25); touching nothing
2.50 s: ball at (4.62, 0.00, 0.12) m, moving 0.59 m/s (vx -0.59, vy +0.00, vz +0.00); touching floor
2.75 s: ball at (4.47, 0.00, 0.12) m, moving 0.59 m/s (vx -0.59, vy +0.00, vz +0.00); touching floor
3.00 s: ball at (4.32, 0.00, 0.12) m, moving 0.58 m/s (vx -0.58, vy +0.00, vz +0.00); touching floor
3.25 s: ball at (4.18, 0.00, 0.12) m, moving 0.58 m/s (vx -0.58, vy +0.00, vz +0.00); touching floor
3.50 s: ball at (4.04, 0.00, 0.12) m, moving 0.57 m/s (vx -0.57, vy +0.00, vz +0.00); touching floor
3.75 s: ball at (3.89, 0.00, 0.12) m, moving 0.57 m/s (vx -0.57, vy +0.00, vz +0.00); touching floor
4.00 s: ball at (3.75, 0.00, 0.12) m, moving 0.56 m/s (vx -0.56, vy +0.00, vz +0.00); touching floor
4.25 s: ball at (3.61, 0.00, 0.12) m, moving 0.56 m/s (vx -0.56, vy +0.00, vz +0.00); touching floor
4.50 s: ball at (3.47, 0.00, 0.12) m, moving 0.56 m/s (vx -0.56, vy +0.00, vz +0.00); touching floor
4.75 s: ball at (3.33, 0.00, 0.12) m, moving 0.55 m/s (vx -0.55, vy +0.00, vz +0.00); touching floor
5.00 s: ball at (3.20, 0.00, 0.12) m, moving 0.55 m/s (vx -0.55, vy +0.00, vz +0.00); touching floor
5.25 s: ball at (3.06, 0.00, 0.12) m, moving 0.54 m/s (vx -0.54, vy +0.00, vz +0.00); touching floor
5.50 s: ball at (2.92, 0.00, 0.12) m, moving 0.54 m/s (vx -0.54, vy +0.00, vz +0.00); touching floor
5.75 s: ball at (2.79, 0.00, 0.12) m, moving 0.53 m/s (vx -0.53, vy +0.00, vz +0.00); touching floor
6.00 s: ball at (2.66, 0.00, 0.12) m, moving 0.53 m/s (vx -0.53, vy +0.00, vz +0.00); touching floor

At the end (6.00 s):
- ball at (2.66, 0.00, 0.12) m, moving 0.53 m/s (vx -0.53, vy +0.00, vz +0.00); touching floor
</history>


Does the world do what the brief says? First describe what happens in the run. Then end your reply with a ```json block
holding one object:

{"what_happens": "<what happens in the run>", "works": <true or false>, "problem": "<one sentence, or empty>"}

If it does not work, also reply with the complete corrected file in one ```xml block, keeping the names the
brief needs. If it works, no file is needed.
