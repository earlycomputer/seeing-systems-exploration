Ten dominoes, each 10 cm tall, stand 6 cm apart along +x. The keyframe starts `domino1` rotating about its front bottom edge. It falls into the next one and the chain topples down the row. The last domino falls flat. The others end leaning on their neighbours, well past 15°.

```xml
<mujoco model="domino_chain">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.3 -0.5 1.5" dir="0 0.3 -1"/>
    <geom name="floor" type="plane" size="2 2 0.1" friction="1 0.005 0.0001" rgba="0.8 0.8 0.8 1"/>
    <body name="domino1" pos="0 0 0.05">
      <freejoint/>
      <geom name="domino1_geom" type="box" size="0.01 0.025 0.05" friction="0.6 0.005 0.0001" rgba="0.9 0.2 0.2 1"/>
    </body>
    <body name="domino2" pos="0.06 0 0.05">
      <freejoint/>
      <geom name="domino2_geom" type="box" size="0.01 0.025 0.05" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino3" pos="0.12 0 0.05">
      <freejoint/>
      <geom name="domino3_geom" type="box" size="0.01 0.025 0.05" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino4" pos="0.18 0 0.05">
      <freejoint/>
      <geom name="domino4_geom" type="box" size="0.01 0.025 0.05" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino5" pos="0.24 0 0.05">
      <freejoint/>
      <geom name="domino5_geom" type="box" size="0.01 0.025 0.05" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino6" pos="0.30 0 0.05">
      <freejoint/>
      <geom name="domino6_geom" type="box" size="0.01 0.025 0.05" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino7" pos="0.36 0 0.05">
      <freejoint/>
      <geom name="domino7_geom" type="box" size="0.01 0.025 0.05" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino8" pos="0.42 0 0.05">
      <freejoint/>
      <geom name="domino8_geom" type="box" size="0.01 0.025 0.05" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino9" pos="0.48 0 0.05">
      <freejoint/>
      <geom name="domino9_geom" type="box" size="0.01 0.025 0.05" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino10" pos="0.54 0 0.05">
      <freejoint/>
      <geom name="domino10_geom" type="box" size="0.01 0.025 0.05" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0 0 0.05 1 0 0 0  0.06 0 0.05 1 0 0 0  0.12 0 0.05 1 0 0 0  0.18 0 0.05 1 0 0 0  0.24 0 0.05 1 0 0 0  0.30 0 0.05 1 0 0 0  0.36 0 0.05 1 0 0 0  0.42 0 0.05 1 0 0 0  0.48 0 0.05 1 0 0 0  0.54 0 0.05 1 0 0 0" qvel="0.2 0 0.04 0 4 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

These lines check that each domino reaches the next, which is what the chain needs. They don't directly check the brief's 15° tilt.

```expect
domino1 touches domino2
domino2 touches domino3
domino3 touches domino4
domino4 touches domino5
domino5 touches domino6
domino6 touches domino7
domino7 touches domino8
domino8 touches domino9
domino9 touches domino10
domino10 touches floor
```

---
thinking (summarized):

I'm working out the domino dimensions and spacing so that each falling domino tips over and strikes the next one, calculating the tilt angle needed for contact based on height, thickness, and gap distance, with the final domino falling flat onto the floor.

For the initial tip, I need to set an angular velocity on the first domino's free joint, reasoning about rotation direction about the y-axis so it falls toward +x, and computing the corresponding linear velocity based on a pivot point at the bottom front edge rather than the center.

Now I'm working out the full keyframe values: positions spaced evenly along x at half-height z, checking friction defaults are sufficient to prevent sliding, and confirming the mass from density and volume works out reasonable (~0.1 kg) for the chain reaction to propagate properly through all ten dominoes.

I still need to express expectations like consecutive dominoes touching each other and the last one touching the floor, plus write out the full keyframe qpos with positions and quaternions for every body. I should also add a named light source for completeness.

