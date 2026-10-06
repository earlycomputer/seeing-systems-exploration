Ten 2 × 5 × 10 cm dominoes stand 7 cm apart, a spacing of 0.7 times their height. The `start` keyframe gives domino1 a spin about +y, plus the matching velocity of its centre, so it pivots on its front bottom edge and falls toward domino2. The dominoes resting against their neighbours should settle around 30° from upright, and the last one should fall flat on the floor. I haven't run this, so the 15° condition still needs checking in simulation.

```xml
<mujoco model="domino_chain">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="0.3 -0.5 1.5" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" size="2 2 0.1" rgba="0.8 0.8 0.8 1" friction="0.8 0.005 0.0001"/>
    <body name="domino1" pos="0 0 0.05">
      <freejoint/>
      <geom name="domino1_geom" type="box" size="0.01 0.025 0.05" density="650" friction="0.6 0.005 0.0001" rgba="0.9 0.2 0.2 1"/>
    </body>
    <body name="domino2" pos="0.07 0 0.05">
      <freejoint/>
      <geom name="domino2_geom" type="box" size="0.01 0.025 0.05" density="650" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino3" pos="0.14 0 0.05">
      <freejoint/>
      <geom name="domino3_geom" type="box" size="0.01 0.025 0.05" density="650" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino4" pos="0.21 0 0.05">
      <freejoint/>
      <geom name="domino4_geom" type="box" size="0.01 0.025 0.05" density="650" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino5" pos="0.28 0 0.05">
      <freejoint/>
      <geom name="domino5_geom" type="box" size="0.01 0.025 0.05" density="650" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino6" pos="0.35 0 0.05">
      <freejoint/>
      <geom name="domino6_geom" type="box" size="0.01 0.025 0.05" density="650" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino7" pos="0.42 0 0.05">
      <freejoint/>
      <geom name="domino7_geom" type="box" size="0.01 0.025 0.05" density="650" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino8" pos="0.49 0 0.05">
      <freejoint/>
      <geom name="domino8_geom" type="box" size="0.01 0.025 0.05" density="650" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino9" pos="0.56 0 0.05">
      <freejoint/>
      <geom name="domino9_geom" type="box" size="0.01 0.025 0.05" density="650" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino10" pos="0.63 0 0.05">
      <freejoint/>
      <geom name="domino10_geom" type="box" size="0.01 0.025 0.05" density="650" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0 0 0.05 1 0 0 0  0.07 0 0.05 1 0 0 0  0.14 0 0.05 1 0 0 0  0.21 0 0.05 1 0 0 0  0.28 0 0.05 1 0 0 0  0.35 0 0.05 1 0 0 0  0.42 0 0.05 1 0 0 0  0.49 0 0.05 1 0 0 0  0.56 0 0.05 1 0 0 0  0.63 0 0.05 1 0 0 0" qvel="0.15 0 0.03 0 3 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm sketching out a domino chain design with ten standard-sized dominoes (roughly 1cm x 2.5cm x 5cm), spacing them about 3cm apart so the first domino can tip into the next in sequence.

For the first domino, I'll give it an initial angular velocity around the y-axis (about 6 rad/s) plus a small linear velocity component, so it topples forward and pivots realistically onto the floor and into the second domino. As the chain propagates, each domino should lean against the next, with the final domino expected to fall to roughly 90°, comfortably exceeding the 15° threshold requirement.

For spacing and sizing, I'm working out that a gap-to-height ratio around 0.7 (e.g., spacing 0.035 with height 0.05) gives each domino a resting lean angle of roughly 30°, which is safely above the minimum and still allows the chain to propagate. I'm also checking that default density and friction values yield reasonable masses for these small dominoes, though I may bump dimensions up slightly (2cm x 5cm x 10cm) for better simulation stability given the small timestep.

Now I'm working through the keyframe setup: positioning each domino at half-height so it rests on the floor, spacing them by 0.07 along x, and computing the initial velocity for the first domino so it topples correctly — using angular velocity about the pivot edge and converting that into the linear velocity of the center of mass via the cross product of ω and the offset vector from pivot to center.

Confirmed the top point moves in +x as rotation increases, matching the fall direction. Now I'm setting up the scene file — identity quaternions in the keyframe, floor friction around 0.6, proper naming for all bodies and geoms, and checking timing so the ten dominoes finish falling within the 6-second simulation window. Writing qpos values...

