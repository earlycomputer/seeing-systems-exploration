Ten 20 cm dominoes stand 12 cm apart along +x. The `start` keyframe gives `domino1` a forward angular velocity of 4 rad/s about its bottom front edge, and gravity carries the cascade down the row. Spacing that is 0.6 of the height should leave each domino leaning on the next, well past 15°, and the last one lying flat. I haven't run this, so the propagation and final tilts are predicted, not measured.

```xml
<mujoco model="domino_chain">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="0.5 -1 2" dir="0 0.5 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" friction="0.6 0.005 0.0001" rgba="0.8 0.8 0.8 1"/>
    <body name="domino1" pos="0 0 0.1">
      <freejoint name="j1"/>
      <geom name="d1" type="box" size="0.015 0.05 0.1" density="600" friction="0.6 0.005 0.0001" rgba="0.9 0.2 0.2 1"/>
    </body>
    <body name="domino2" pos="0.12 0 0.1">
      <freejoint name="j2"/>
      <geom name="d2" type="box" size="0.015 0.05 0.1" density="600" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino3" pos="0.24 0 0.1">
      <freejoint name="j3"/>
      <geom name="d3" type="box" size="0.015 0.05 0.1" density="600" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino4" pos="0.36 0 0.1">
      <freejoint name="j4"/>
      <geom name="d4" type="box" size="0.015 0.05 0.1" density="600" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino5" pos="0.48 0 0.1">
      <freejoint name="j5"/>
      <geom name="d5" type="box" size="0.015 0.05 0.1" density="600" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino6" pos="0.6 0 0.1">
      <freejoint name="j6"/>
      <geom name="d6" type="box" size="0.015 0.05 0.1" density="600" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino7" pos="0.72 0 0.1">
      <freejoint name="j7"/>
      <geom name="d7" type="box" size="0.015 0.05 0.1" density="600" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino8" pos="0.84 0 0.1">
      <freejoint name="j8"/>
      <geom name="d8" type="box" size="0.015 0.05 0.1" density="600" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino9" pos="0.96 0 0.1">
      <freejoint name="j9"/>
      <geom name="d9" type="box" size="0.015 0.05 0.1" density="600" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino10" pos="1.08 0 0.1">
      <freejoint name="j10"/>
      <geom name="d10" type="box" size="0.015 0.05 0.1" density="600" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0 0 0.1 1 0 0 0  0.12 0 0.1 1 0 0 0  0.24 0 0.1 1 0 0 0  0.36 0 0.1 1 0 0 0  0.48 0 0.1 1 0 0 0  0.6 0 0.1 1 0 0 0  0.72 0 0.1 1 0 0 0  0.84 0 0.1 1 0 0 0  0.96 0 0.1 1 0 0 0  1.08 0 0.1 1 0 0 0" qvel="0.4 0 0.06 0 4 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm designing the domino chain geometry with realistic proportions (roughly 48x24x8mm) spaced about 0.03 units apart along the x-axis, and planning to give the first domino an initial angular velocity about the y-axis so it tips forward into the rest.

Now I'm reconsidering scale for robustness — maybe larger dominoes (0.2 height, 0.03 thickness) with wider spacing would simulate more reliably, and I'm working out mass density, friction coefficients between floor and dominoes, and timestep settings. I also need to get the free-joint velocity convention right, since the angular velocity component is interpreted differently depending on whether it's in local or world frame.

Checking the chain reaction setup: spacing of 0.12 with 0.2 height gives a good ratio for propagation, so I'm laying out dominoes along x from 0 to 1.08 at z=0.1 with upright keyframe orientation. The fall sequence should complete within a few seconds, with each domino leaning against the next at a reasonable angle before the last one lands flat, so I'll move on to adding solver settings.

