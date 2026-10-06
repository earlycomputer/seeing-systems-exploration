The first domino starts tilted beyond its balance point, so gravity initiates the chain reaction without motors or external forces.

```xml
<mujoco model="ten_domino_chain">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="100"/>

  <visual>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="overhead_light" pos="0.54 -0.8 2" dir="0 0.3 -1"/>
    <geom name="floor" type="plane" size="2 2 0.1" friction="1 0.005 0.0001" solref="0.008 1" rgba="0.25 0.28 0.32 1"/>

    <body name="domino1" pos="0 0 0.148124112" euler="0 15 0">
      <freejoint name="domino1_joint"/>
      <geom name="domino1_geom" type="box" size="0.0125 0.06 0.15" mass="0.15" friction="1 0.005 0.0001" solref="0.008 1" rgba="0.9 0.25 0.15 1"/>
    </body>

    <body name="domino2" pos="0.12 0 0.15">
      <freejoint name="domino2_joint"/>
      <geom name="domino2_geom" type="box" size="0.0125 0.06 0.15" mass="0.15" friction="1 0.005 0.0001" solref="0.008 1" rgba="0.95 0.6 0.15 1"/>
    </body>

    <body name="domino3" pos="0.24 0 0.15">
      <freejoint name="domino3_joint"/>
      <geom name="domino3_geom" type="box" size="0.0125 0.06 0.15" mass="0.15" friction="1 0.005 0.0001" solref="0.008 1" rgba="0.95 0.75 0.2 1"/>
    </body>

    <body name="domino4" pos="0.36 0 0.15">
      <freejoint name="domino4_joint"/>
      <geom name="domino4_geom" type="box" size="0.0125 0.06 0.15" mass="0.15" friction="1 0.005 0.0001" solref="0.008 1" rgba="0.55 0.75 0.25 1"/>
    </body>

    <body name="domino5" pos="0.48 0 0.15">
      <freejoint name="domino5_joint"/>
      <geom name="domino5_geom" type="box" size="0.0125 0.06 0.15" mass="0.15" friction="1 0.005 0.0001" solref="0.008 1" rgba="0.2 0.7 0.4 1"/>
    </body>

    <body name="domino6" pos="0.60 0 0.15">
      <freejoint name="domino6_joint"/>
      <geom name="domino6_geom" type="box" size="0.0125 0.06 0.15" mass="0.15" friction="1 0.005 0.0001" solref="0.008 1" rgba="0.2 0.7 0.7 1"/>
    </body>

    <body name="domino7" pos="0.72 0 0.15">
      <freejoint name="domino7_joint"/>
      <geom name="domino7_geom" type="box" size="0.0125 0.06 0.15" mass="0.15" friction="1 0.005 0.0001" solref="0.008 1" rgba="0.2 0.5 0.85 1"/>
    </body>

    <body name="domino8" pos="0.84 0 0.15">
      <freejoint name="domino8_joint"/>
      <geom name="domino8_geom" type="box" size="0.0125 0.06 0.15" mass="0.15" friction="1 0.005 0.0001" solref="0.008 1" rgba="0.35 0.35 0.8 1"/>
    </body>

    <body name="domino9" pos="0.96 0 0.15">
      <freejoint name="domino9_joint"/>
      <geom name="domino9_geom" type="box" size="0.0125 0.06 0.15" mass="0.15" friction="1 0.005 0.0001" solref="0.008 1" rgba="0.6 0.3 0.75 1"/>
    </body>

    <body name="domino10" pos="1.08 0 0.15">
      <freejoint name="domino10_joint"/>
      <geom name="domino10_geom" type="box" size="0.0125 0.06 0.15" mass="0.15" friction="1 0.005 0.0001" solref="0.008 1" rgba="0.8 0.3 0.55 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Considering geometry and naming conventions**

I'm thinking about how to approach the relationship between density and mass and deciding to focus on geometry and mass inertia. I'm imagining a thin box with dimensions of .0125 by .06 by .15, where .15 is the height. I'll also need to consider the angle for the Euler calculation and the floor plane size. The camera positions need to be set up thoughtfully, ensuring every body and geom has a name, but keeping in mind the special rules about the world body.