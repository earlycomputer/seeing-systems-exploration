Ten 1×5×10 cm boxes stand 6 cm apart along +x. The keyframe gives `domino1` a forward spin of 3 rad/s about y. Its linear velocity is matched so the bottom edge starts at rest, which pivots it into the chain. I haven't run this scene. On paper the fallen dominoes should end leaning on each other at steep angles, and the last one should lie roughly flat, so every tilt should be well past 15°.

```xml
<mujoco model="domino_chain">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0.3 -0.5 1.5" dir="0 0.3 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="2 2 0.1" rgba="0.8 0.8 0.8 1" friction="0.8 0.005 0.0001"/>
    <body name="domino1" pos="0.00 0 0.05">
      <freejoint/>
      <geom name="domino1_geom" type="box" size="0.005 0.025 0.05" rgba="0.9 0.2 0.2 1" friction="0.5 0.005 0.0001"/>
    </body>
    <body name="domino2" pos="0.06 0 0.05">
      <freejoint/>
      <geom name="domino2_geom" type="box" size="0.005 0.025 0.05" rgba="0.2 0.4 0.9 1" friction="0.5 0.005 0.0001"/>
    </body>
    <body name="domino3" pos="0.12 0 0.05">
      <freejoint/>
      <geom name="domino3_geom" type="box" size="0.005 0.025 0.05" rgba="0.2 0.4 0.9 1" friction="0.5 0.005 0.0001"/>
    </body>
    <body name="domino4" pos="0.18 0 0.05">
      <freejoint/>
      <geom name="domino4_geom" type="box" size="0.005 0.025 0.05" rgba="0.2 0.4 0.9 1" friction="0.5 0.005 0.0001"/>
    </body>
    <body name="domino5" pos="0.24 0 0.05">
      <freejoint/>
      <geom name="domino5_geom" type="box" size="0.005 0.025 0.05" rgba="0.2 0.4 0.9 1" friction="0.5 0.005 0.0001"/>
    </body>
    <body name="domino6" pos="0.30 0 0.05">
      <freejoint/>
      <geom name="domino6_geom" type="box" size="0.005 0.025 0.05" rgba="0.2 0.4 0.9 1" friction="0.5 0.005 0.0001"/>
    </body>
    <body name="domino7" pos="0.36 0 0.05">
      <freejoint/>
      <geom name="domino7_geom" type="box" size="0.005 0.025 0.05" rgba="0.2 0.4 0.9 1" friction="0.5 0.005 0.0001"/>
    </body>
    <body name="domino8" pos="0.42 0 0.05">
      <freejoint/>
      <geom name="domino8_geom" type="box" size="0.005 0.025 0.05" rgba="0.2 0.4 0.9 1" friction="0.5 0.005 0.0001"/>
    </body>
    <body name="domino9" pos="0.48 0 0.05">
      <freejoint/>
      <geom name="domino9_geom" type="box" size="0.005 0.025 0.05" rgba="0.2 0.4 0.9 1" friction="0.5 0.005 0.0001"/>
    </body>
    <body name="domino10" pos="0.54 0 0.05">
      <freejoint/>
      <geom name="domino10_geom" type="box" size="0.005 0.025 0.05" rgba="0.2 0.9 0.3 1" friction="0.5 0.005 0.0001"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0.00 0 0.05 1 0 0 0  0.06 0 0.05 1 0 0 0  0.12 0 0.05 1 0 0 0  0.18 0 0.05 1 0 0 0  0.24 0 0.05 1 0 0 0  0.30 0 0.05 1 0 0 0  0.36 0 0.05 1 0 0 0  0.42 0 0.05 1 0 0 0  0.48 0 0.05 1 0 0 0  0.54 0 0.05 1 0 0 0" qvel="0.15 0 0 0 3 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm sketching out the domino chain setup, sizing each box and spacing them close enough to topple sequentially, with the first domino given an initial angular velocity to kick off the fall toward the next ones.

For the keyframe, I need to figure out whether MuJoCo requires a full qpos vector for all ten freejoints or whether omitted fields default to qpos0, since each domino needs its own position and orientation defined.

Then I'm considering whether to give the first domino an initial tilt or angular velocity instead, computing how the linear velocity of the center of mass must be set so the bottom edge stays pinned when the domino rotates about its pivot point.

I'm checking whether 3 rad/s gives enough energy to tip the domino over, estimating the potential energy barrier from raising the center of mass over the pivot edge versus the rotational kinetic energy available.

Kinetic energy comes out around 0.015 J/kg, comfortably exceeding the 0.00245 J/kg barrier, so the tip should succeed. I'm also double-checking domino spacing (0.06 m, less than their 0.1 m height) ensures contact, verifying mass from default density gives about 0.05 kg per domino, and confirming default contact stiffness, timestep, and friction settings should let the chain reaction propagate normally.

With about 10 dominoes falling at roughly 0.1-0.2 s each, the last one should topple flat onto the ground fine. Now I'm writing out the scene file: quaternion poses for each domino, a floor plane, and a light source.

