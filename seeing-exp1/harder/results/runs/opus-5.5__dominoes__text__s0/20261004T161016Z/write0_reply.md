The first domino starts tilted 15° and balanced on its leading bottom edge, so gravity tips it into the row. The dominoes are 1 × 5 × 10 cm and spaced 5 cm apart (half their height). They lean on each other at roughly 25° or more, and the last one falls flat.

```xml
<mujoco model="domino_chain">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0.25 -0.5 1.0" dir="0 0.5 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="2 2 0.1" pos="0 0 0" rgba="0.8 0.8 0.8 1" friction="1 0.005 0.0001"/>

    <body name="domino1" pos="0.013111 0 0.049590" quat="0.991445 0 0.130526 0">
      <freejoint name="domino1_free"/>
      <geom name="domino1_geom" type="box" size="0.005 0.025 0.05" density="1000" friction="0.4 0.005 0.0001" rgba="0.9 0.2 0.2 1"/>
    </body>
    <body name="domino2" pos="0.05 0 0.05">
      <freejoint name="domino2_free"/>
      <geom name="domino2_geom" type="box" size="0.005 0.025 0.05" density="1000" friction="0.4 0.005 0.0001" rgba="0.2 0.2 0.9 1"/>
    </body>
    <body name="domino3" pos="0.10 0 0.05">
      <freejoint name="domino3_free"/>
      <geom name="domino3_geom" type="box" size="0.005 0.025 0.05" density="1000" friction="0.4 0.005 0.0001" rgba="0.2 0.2 0.9 1"/>
    </body>
    <body name="domino4" pos="0.15 0 0.05">
      <freejoint name="domino4_free"/>
      <geom name="domino4_geom" type="box" size="0.005 0.025 0.05" density="1000" friction="0.4 0.005 0.0001" rgba="0.2 0.2 0.9 1"/>
    </body>
    <body name="domino5" pos="0.20 0 0.05">
      <freejoint name="domino5_free"/>
      <geom name="domino5_geom" type="box" size="0.005 0.025 0.05" density="1000" friction="0.4 0.005 0.0001" rgba="0.2 0.2 0.9 1"/>
    </body>
    <body name="domino6" pos="0.25 0 0.05">
      <freejoint name="domino6_free"/>
      <geom name="domino6_geom" type="box" size="0.005 0.025 0.05" density="1000" friction="0.4 0.005 0.0001" rgba="0.2 0.2 0.9 1"/>
    </body>
    <body name="domino7" pos="0.30 0 0.05">
      <freejoint name="domino7_free"/>
      <geom name="domino7_geom" type="box" size="0.005 0.025 0.05" density="1000" friction="0.4 0.005 0.0001" rgba="0.2 0.2 0.9 1"/>
    </body>
    <body name="domino8" pos="0.35 0 0.05">
      <freejoint name="domino8_free"/>
      <geom name="domino8_geom" type="box" size="0.005 0.025 0.05" density="1000" friction="0.4 0.005 0.0001" rgba="0.2 0.2 0.9 1"/>
    </body>
    <body name="domino9" pos="0.40 0 0.05">
      <freejoint name="domino9_free"/>
      <geom name="domino9_geom" type="box" size="0.005 0.025 0.05" density="1000" friction="0.4 0.005 0.0001" rgba="0.2 0.2 0.9 1"/>
    </body>
    <body name="domino10" pos="0.45 0 0.05">
      <freejoint name="domino10_free"/>
      <geom name="domino10_geom" type="box" size="0.005 0.025 0.05" density="1000" friction="0.4 0.005 0.0001" rgba="0.2 0.9 0.2 1"/>
    </body>
  </worldbody>
</mujoco>
```

I checked the starting setup by hand: the first domino is placed so its leading bottom edge touches the floor and it doesn't overlap the second. Once it touches domino2, it leans with enough force to push domino2 over. I haven't run the 6 s simulation, so whether every domino ends at least 15° from upright is predicted, not measured.

---
thinking (summarized):

I'm sketching out the domino dimensions and spacing—about 0.01 x 0.05 x 0.1 meters each, spaced roughly half the height apart so they'll topple in sequence. I'm planning to give the first domino an initial push via angular velocity to kick off the chain reaction.

For getting it moving, I think tilting the domino slightly at the start (around 15 degrees about its hinge edge) is simpler than computing an exact angular velocity, since gravity will naturally take over once it's past the tipping point. I'm working out the pivot geometry—where the bottom corner lands after rotation—to make sure the tilt is physically consistent with resting on the floor.

Checking the numbers: with a 15° tilt, the computed body position puts the top corner around x=0.031, while the next domino's near face sits at x=0.045, so there's no overlap and the tilt looks safe.

I'm computing the quaternion for a 15° rotation about the y-axis, giving roughly (0.9914, 0, 0.1305, 0). I decide no explicit keyframe is needed — gravity alone will topple the first domino from this tilt, so I'll just set the initial body orientations directly, treating the chain reaction as the natural end state.

For spacing, I estimate the resting angle where one fallen domino leans on the next (with 0.05 spacing and 0.1 height) comes out around 25-30°, comfortably above the 15° starting tilt, so the chain should propagate properly with friction values like 0.6 for floor and 0.3 between dominoes. I also start working out the mass from the default density and box dimensions.

I'm checking whether the toppling motion actually delivers enough contact force to knock over the next domino, computing where the falling top edge lands relative to the next domino's position as it rotates from its pivot.

Domino2 starts upright, so it needs enough torque to start tipping over its own base edge rather than just being nudged. I'm comparing the pushing torque from domino1's lean against the resisting gravitational torque of domino2, factoring in the contact height where the push is applied near the top.

The lever arm from domino1's torque gives up to ~0.17mg of pushing force available against a ~0.054mg threshold, so the chain reaction should proceed through the quasi-static push without needing extra velocity. I'll keep the initial tilt at 15° rather than increasing it, since the margin looks sufficient without adding explicit angular velocity in the keyframe.

I'm finalizing the domino positions along x with 0.05 spacing, and setting friction explicitly—floor friction at 1 and domino-domino friction at 0.4—so pivoting against the floor stays reliable while domino-to-domino contact stays low enough to avoid jamming.

I'll skip the keyframe since specifying qpos for all 70 entries isn't necessary; the chain of leaning dominoes with tilt angles exceeding 23° should hold up fine as-is.

