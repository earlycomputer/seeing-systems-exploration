The row runs along +x with 6 cm spacing. The `start` keyframe gives domino1 a rigid-body rotation of 4 rad/s about its front bottom edge, so it tips forward into domino2. I haven't run this file. In the expected outcome, each domino ends leaning on its neighbour at roughly 30° or more, and the last one lies flat on the floor.

```xml
<mujoco model="domino_row">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="0.3 -0.5 1.5" dir="0 0.3 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="2 2 0.1" rgba="0.8 0.8 0.75 1" friction="0.8 0.005 0.0001"/>
    <body name="domino1" pos="0.00 0 0.05">
      <freejoint name="j1"/>
      <geom name="g1" type="box" size="0.01 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.9 0.2 0.2 1"/>
    </body>
    <body name="domino2" pos="0.06 0 0.05">
      <freejoint name="j2"/>
      <geom name="g2" type="box" size="0.01 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.2 0.3 0.9 1"/>
    </body>
    <body name="domino3" pos="0.12 0 0.05">
      <freejoint name="j3"/>
      <geom name="g3" type="box" size="0.01 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.2 0.3 0.9 1"/>
    </body>
    <body name="domino4" pos="0.18 0 0.05">
      <freejoint name="j4"/>
      <geom name="g4" type="box" size="0.01 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.2 0.3 0.9 1"/>
    </body>
    <body name="domino5" pos="0.24 0 0.05">
      <freejoint name="j5"/>
      <geom name="g5" type="box" size="0.01 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.2 0.3 0.9 1"/>
    </body>
    <body name="domino6" pos="0.30 0 0.05">
      <freejoint name="j6"/>
      <geom name="g6" type="box" size="0.01 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.2 0.3 0.9 1"/>
    </body>
    <body name="domino7" pos="0.36 0 0.05">
      <freejoint name="j7"/>
      <geom name="g7" type="box" size="0.01 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.2 0.3 0.9 1"/>
    </body>
    <body name="domino8" pos="0.42 0 0.05">
      <freejoint name="j8"/>
      <geom name="g8" type="box" size="0.01 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.2 0.3 0.9 1"/>
    </body>
    <body name="domino9" pos="0.48 0 0.05">
      <freejoint name="j9"/>
      <geom name="g9" type="box" size="0.01 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.2 0.3 0.9 1"/>
    </body>
    <body name="domino10" pos="0.54 0 0.05">
      <freejoint name="j10"/>
      <geom name="g10" type="box" size="0.01 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.2 0.9 0.3 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0.00 0 0.05 1 0 0 0  0.06 0 0.05 1 0 0 0  0.12 0 0.05 1 0 0 0  0.18 0 0.05 1 0 0 0  0.24 0 0.05 1 0 0 0  0.30 0 0.05 1 0 0 0  0.36 0 0.05 1 0 0 0  0.42 0 0.05 1 0 0 0  0.48 0 0.05 1 0 0 0  0.54 0 0.05 1 0 0 0" qvel="0.2 0 0.04 0 4 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm sizing the dominoes at roughly 8mm by 24mm by 48mm and spacing them about 3cm apart along a row, then planning to give the first domino an initial angular velocity about the y-axis so it tips forward into the chain. I'm setting up each domino's free joint with position, quaternion orientation, and velocity state.

For the first domino's push, I'm computing the combination of linear and angular velocity so the rotation pivots around its bottom edge rather than the center—solving for vx so that v plus the cross product of angular velocity and the offset to the base cancels out horizontal motion at the contact point. The rest should fall naturally via default friction, with the last domino ending flat and the middle ones resting tilted against each other.

I'm also weighing whether to scale up the domino dimensions (to roughly 2x5x10cm) with wider spacing for better numerical stability, and estimating the cascade timing across ten dominoes to make sure everything settles within the simulation window.

Checking whether the initial angular velocity gives enough energy to tip the first domino past its pivot edge, given the small height difference it needs to climb.

Writing keyframe qpos/qvel values...

