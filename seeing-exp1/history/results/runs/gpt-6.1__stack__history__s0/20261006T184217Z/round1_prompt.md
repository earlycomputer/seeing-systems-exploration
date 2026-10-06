Here is a MuJoCo MJCF scene written for this brief:

<brief>
a stack of five blocks stands until the bottom block is pushed, then topples
</brief>

MuJoCo loads the file, resets to the keyframe named `start` if there is one, and simulates it for 6 s.
Nothing else acts on the scene: whatever moves is set moving by the scene itself, for example by a keyframe
velocity, a spring, gravity, or a motor whose control the keyframe sets.

It follows a few conventions so the other tools can find things. They fix names and axes, not what is built:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- The blocks are bodies named `block1` (bottom) to `block5` (top), each with a `<freejoint/>` and one box geom. Whatever does the pushing is part of the scene.
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures,
  `<default>` classes or `<include>`.
- Every body and geom has a name, and each element's attributes are on a single line.
- `<option timestep="0.002"/>`.

```xml
<mujoco model="stack_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="6 6 0.1" friction="0.6 0.005 0.0001"/>
    <body name="block1" pos="0 0 0.100">
      <freejoint/>
      <geom name="block1" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block2" pos="0 0 0.300">
      <freejoint/>
      <geom name="block2" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block3" pos="0 0 0.500">
      <freejoint/>
      <geom name="block3" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block4" pos="0 0 0.700">
      <freejoint/>
      <geom name="block4" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block5" pos="0 0 0.900">
      <freejoint/>
      <geom name="block5" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="pusher" pos="-1.2 0 0.1">
      <freejoint/>
      <geom name="pusher" type="sphere" size="0.1" mass="4.0" friction="0.3 0.005 0.0001"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0 0 0.100 1 0 0 0  0 0 0.300 1 0 0 0  0 0 0.500 1 0 0 0  0 0 0.700 1 0 0 0  0 0 0.900 1 0 0 0  -1.2 0 0.1 1 0 0 0" qvel="0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  1.5 0 0 0 0 0"/>
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
- block1: free body; its geoms: block1; starts at (0.00, 0.00, 0.10) m, at rest
- block2: free body; its geoms: block2; starts at (0.00, 0.00, 0.30) m, at rest
- block3: free body; its geoms: block3; starts at (0.00, 0.00, 0.50) m, at rest
- block4: free body; its geoms: block4; starts at (0.00, 0.00, 0.70) m, at rest
- block5: free body; its geoms: block5; starts at (0.00, 0.00, 0.90) m, at rest
- pusher: free body; its geoms: pusher; starts at (-1.20, 0.00, 0.10) m, moving 1.50 m/s (vx +1.50, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  block1 starts touching floor
 0.00 s  block1 starts touching block2
 0.00 s  block3 starts touching block4
 0.00 s  pusher starts touching floor
 0.00 s  block2 starts touching block3
 0.01 s  block5 starts moving
 0.01 s  block4 first touches block5
 0.92 s  block1 first touches pusher
 0.92 s  block1 starts moving
 0.92 s  block2 starts moving
 0.92 s  block3 starts moving
 0.92 s  block4 starts moving
 0.92 s  pusher leaves floor
 0.96 s  block1 leaves pusher
 0.97 s  pusher touches floor again
 1.02 s  block3 passes 0.21 m from pusher without touching it: nearest points (-0.07, 0.00, 0.40) m and (-0.12, 0.00, 0.20) m
 1.02 s  block4 passes 0.40 m from pusher without touching it: nearest points (-0.08, 0.00, 0.60) m and (-0.13, 0.00, 0.20) m
 1.02 s  block1 touches pusher again
 1.03 s  block2 passes 0.03 m from pusher without touching it: nearest points (-0.06, 0.00, 0.20) m and (-0.08, 0.00, 0.18) m
 1.07 s  block1 comes to rest at (0.06, 0.00, 0.10) m
 1.08 s  pusher comes to rest at (-0.14, 0.00, 0.10) m
 1.15 s  block1 leaves pusher
 1.66 s  block2 comes to rest at (0.05, 0.00, 0.30) m
 1.69 s  block3 comes to rest at (0.05, 0.00, 0.50) m
 1.70 s  block4 comes to rest at (0.05, 0.00, 0.70) m
 1.71 s  block5 comes to rest at (0.05, 0.00, 0.90) m

State every 0.25 s:
0.00 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3 | block5 at (0.00, 0.00, 0.90) m, at rest; touching nothing | pusher at (-1.20, 0.00, 0.10) m, moving 1.50 m/s (vx +1.50, vy +0.00, vz +0.00); touching floor
0.25 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4 | pusher at (-0.92, 0.00, 0.10) m, moving 1.07 m/s (vx +1.07, vy +0.00, vz -0.00); touching floor
0.50 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4 | pusher at (-0.65, 0.00, 0.10) m, moving 1.07 m/s (vx +1.07, vy +0.00, vz -0.00); touching floor
0.75 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4 | pusher at (-0.38, 0.00, 0.10) m, moving 1.07 m/s (vx +1.07, vy +0.00, vz +0.00); touching floor
1.00 s: block1 at (0.05, 0.00, 0.10) m, moving 0.37 m/s (vx +0.34, vy -0.00, vz -0.14); touching block2, floor | block2 at (0.03, 0.00, 0.30) m, moving 0.38 m/s (vx +0.38, vy -0.00, vz -0.05), turned 2° from how it started; touching block1, block3 | block3 at (0.02, 0.00, 0.50) m, moving 0.29 m/s (vx +0.28, vy +0.00, vz -0.05), turned 3° from how it started; touching block2, block4 | block4 at (0.01, 0.00, 0.70) m, moving 0.18 m/s (vx +0.17, vy +0.00, vz -0.05), turned 3° from how it started; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, moving 0.08 m/s (vx +0.05, vy +0.00, vz -0.07), turned 3° from how it started; touching block4 | pusher at (-0.16, 0.00, 0.10) m, moving 0.37 m/s (vx +0.37, vy +0.00, vz +0.01); touching floor
1.25 s: block1 at (0.06, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.05, 0.00, 0.30) m, at rest, turned 2° from how it started; touching block1, block3 | block3 at (0.06, 0.00, 0.50) m, moving 0.05 m/s (vx +0.05, vy +0.00, vz +0.01), turned 2° from how it started; touching block2, block4 | block4 at (0.06, 0.00, 0.70) m, moving 0.08 m/s (vx +0.08, vy +0.00, vz +0.01), turned 2° from how it started; touching block3, block5 | block5 at (0.07, 0.00, 0.90) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz +0.01), turned 2° from how it started; touching block4 | pusher at (-0.14, 0.00, 0.10) m, at rest; touching floor
1.50 s: block1 at (0.06, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.04, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.04, 0.00, 0.50) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.01); touching block2, block4 | block4 at (0.04, 0.00, 0.70) m, moving 0.09 m/s (vx -0.08, vy +0.00, vz +0.01); touching block3, block5 | block5 at (0.03, 0.00, 0.90) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.01); touching block4 | pusher at (-0.14, 0.00, 0.10) m, at rest; touching floor
1.75 s: block1 at (0.06, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.05, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.05, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.05, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.05, 0.00, 0.90) m, at rest; touching block4 | pusher at (-0.14, 0.00, 0.10) m, at rest; touching floor
(the same through 2.25 s)
2.50 s: block1 at (0.06, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.05, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.05, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.05, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.05, 0.00, 0.90) m, at rest; touching block4 | pusher at (-0.15, 0.00, 0.10) m, at rest; touching floor
(the same through 4.50 s)
4.75 s: block1 at (0.06, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.05, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.05, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.05, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.05, 0.00, 0.90) m, at rest; touching block4 | pusher at (-0.16, 0.00, 0.10) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (0.06, 0.00, 0.10) m, at rest; touching block2, floor
- block2 at (0.05, 0.00, 0.30) m, at rest; touching block1, block3
- block3 at (0.05, 0.00, 0.50) m, at rest; touching block2, block4
- block4 at (0.05, 0.00, 0.70) m, at rest; touching block3, block5
- block5 at (0.05, 0.00, 0.90) m, at rest; touching block4
- pusher at (-0.16, 0.00, 0.10) m, at rest; touching floor
</history>


Does the world do what the brief says? First describe what happens in the run. Then end your reply with a ```json block
holding one object:

{"what_happens": "<what happens in the run>", "works": <true or false>, "problem": "<one sentence, or empty>"}

If it does not work, also reply with the complete corrected file in one ```xml block, keeping the names the
brief needs. If it works, no file is needed.
