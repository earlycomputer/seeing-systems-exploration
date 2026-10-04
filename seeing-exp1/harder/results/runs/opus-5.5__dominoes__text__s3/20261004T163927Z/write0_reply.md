Ten dominoes stand in a row along +x, 6 cm apart. The keyframe gives `domino1` a forward spin about its front bottom edge, so it tips over and starts the chain. I haven't simulated this, but the geometry should meet the 15° requirement. Dominoes leaning on their neighbour come to rest at roughly asin(0.045/0.1) ≈ 27° from upright. The last one should fall flat.

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
      <freejoint name="j1"/>
      <geom name="domino1_geom" type="box" size="0.0075 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.9 0.2 0.2 1"/>
    </body>
    <body name="domino2" pos="0.06 0 0.05">
      <freejoint name="j2"/>
      <geom name="domino2_geom" type="box" size="0.0075 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino3" pos="0.12 0 0.05">
      <freejoint name="j3"/>
      <geom name="domino3_geom" type="box" size="0.0075 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino4" pos="0.18 0 0.05">
      <freejoint name="j4"/>
      <geom name="domino4_geom" type="box" size="0.0075 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino5" pos="0.24 0 0.05">
      <freejoint name="j5"/>
      <geom name="domino5_geom" type="box" size="0.0075 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino6" pos="0.30 0 0.05">
      <freejoint name="j6"/>
      <geom name="domino6_geom" type="box" size="0.0075 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino7" pos="0.36 0 0.05">
      <freejoint name="j7"/>
      <geom name="domino7_geom" type="box" size="0.0075 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino8" pos="0.42 0 0.05">
      <freejoint name="j8"/>
      <geom name="domino8_geom" type="box" size="0.0075 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino9" pos="0.48 0 0.05">
      <freejoint name="j9"/>
      <geom name="domino9_geom" type="box" size="0.0075 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="domino10" pos="0.54 0 0.05">
      <freejoint name="j10"/>
      <geom name="domino10_geom" type="box" size="0.0075 0.025 0.05" density="1000" friction="0.5 0.005 0.0001" rgba="0.2 0.9 0.3 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0 0 0.05 1 0 0 0 0.06 0 0.05 1 0 0 0 0.12 0 0.05 1 0 0 0 0.18 0 0.05 1 0 0 0 0.24 0 0.05 1 0 0 0 0.30 0 0.05 1 0 0 0 0.36 0 0.05 1 0 0 0 0.42 0 0.05 1 0 0 0 0.48 0 0.05 1 0 0 0 0.54 0 0.05 1 0 0 0" qvel="0.2 0 0 0 4 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out domino dimensions and spacing for a chain reaction setup, settling on roughly 0.1 tall, 0.05 wide, 0.015 thick blocks spaced about 0.06 apart, with the first domino given an initial tip to start the cascade.

Rather than hand-tilting the first domino, I'm computing an angular velocity (ω≈5 rad/s about the y-axis) plus a matching linear velocity for its center of mass, treating the fall as a rotation about the bottom edge so the physics looks natural from the start. The last domino in the line should end up falling flat (90°), while the middle ones just need to lean enough to topple their neighbors given the spacing-to-height ratio.

With a gap of 0.045 between dominoes and a height of 0.1, the leaning angle works out to roughly 27° via arcsin, comfortably above the 15° threshold needed for the chain reaction to propagate. I'll keep friction and condim at defaults and compute mass from the density and box volume, coming out to about 0.075 kg per domino—now I just need to set up the keyframe's absolute qpos values for each domino's position and orientation.

Spacing dominoes 0.06 apart along x, I'm writing out the full qpos line with each domino's position and upright quaternion, then setting qvel with an initial velocity and angular spin on the first domino and zeros elsewhere. I'm checking whether that spin of 5 rad/s gives enough kinetic energy to tip the domino past its critical angle, estimating the moment of inertia about the edge and comparing it to the height the center of mass must rise to tip over.

The energy margin is huge (0.0055 m rise needed vs much more available), so I dial back the velocity to something more modest like vx=0.2 with ω=4 to avoid an unrealistic flying motion. I'll also set a reasonable timestep, add lighting and a floor plane, run for 6 seconds, and make sure each model element stays on its own line.

