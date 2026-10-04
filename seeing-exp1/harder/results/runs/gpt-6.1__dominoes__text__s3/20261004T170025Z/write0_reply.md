```xml
<mujoco model="ten_domino_chain">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="100"/>
  <size nconmax="200" njmax="1000"/>

  <worldbody>
    <light name="overhead" pos="0.35 -0.5 1.5" dir="0 0 -1"/>
    <camera name="overview" pos="0.35 -1.2 0.65" xyaxes="1 0 0 0 0.45 0.893"/>
    <geom name="floor" type="plane" pos="0 0 0" size="2 1 0.1" friction="0.9 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.25 0.28 0.32 1"/>

    <!-- The first domino begins tilted 20 degrees toward the others, beyond its tipping point. -->
    <body name="domino1" pos="0 0 0.098244514" quat="0.984807753 0 0.173648178 0">
      <freejoint name="domino1_free"/>
      <geom name="domino1_geom" type="box" size="0.0125 0.04 0.1" density="600" friction="0.9 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.9 0.25 0.15 1"/>
    </body>

    <body name="domino2" pos="0.075 0 0.1">
      <freejoint name="domino2_free"/>
      <geom name="domino2_geom" type="box" size="0.0125 0.04 0.1" density="600" friction="0.9 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.95 0.55 0.15 1"/>
    </body>

    <body name="domino3" pos="0.15 0 0.1">
      <freejoint name="domino3_free"/>
      <geom name="domino3_geom" type="box" size="0.0125 0.04 0.1" density="600" friction="0.9 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.95 0.75 0.2 1"/>
    </body>

    <body name="domino4" pos="0.225 0 0.1">
      <freejoint name="domino4_free"/>
      <geom name="domino4_geom" type="box" size="0.0125 0.04 0.1" density="600" friction="0.9 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.65 0.8 0.2 1"/>
    </body>

    <body name="domino5" pos="0.3 0 0.1">
      <freejoint name="domino5_free"/>
      <geom name="domino5_geom" type="box" size="0.0125 0.04 0.1" density="600" friction="0.9 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.25 0.75 0.35 1"/>
    </body>

    <body name="domino6" pos="0.375 0 0.1">
      <freejoint name="domino6_free"/>
      <geom name="domino6_geom" type="box" size="0.0125 0.04 0.1" density="600" friction="0.9 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.2 0.75 0.7 1"/>
    </body>

    <body name="domino7" pos="0.45 0 0.1">
      <freejoint name="domino7_free"/>
      <geom name="domino7_geom" type="box" size="0.0125 0.04 0.1" density="600" friction="0.9 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.2 0.55 0.9 1"/>
    </body>

    <body name="domino8" pos="0.525 0 0.1">
      <freejoint name="domino8_free"/>
      <geom name="domino8_geom" type="box" size="0.0125 0.04 0.1" density="600" friction="0.9 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.35 0.35 0.85 1"/>
    </body>

    <body name="domino9" pos="0.6 0 0.1">
      <freejoint name="domino9_free"/>
      <geom name="domino9_geom" type="box" size="0.0125 0.04 0.1" density="600" friction="0.9 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.65 0.3 0.8 1"/>
    </body>

    <body name="domino10" pos="0.675 0 0.1">
      <freejoint name="domino10_free"/>
      <geom name="domino10_geom" type="box" size="0.0125 0.04 0.1" density="600" friction="0.9 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.85 0.3 0.6 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Evaluating rotation dynamics**

I'm trying to understand a scenario regarding rotation centered on a body. At the start, with the lowest vertex positioned, I note some calculations. The body at x=0 translates, and it seems I've got a cosine and sine component for determining values, particularly for pivot adjustments. However, I'm sensing there's complexity in how these elements interact with each other. I need to clarify parts of the rotation and how they relate to the overall movement.

**Exploring simulation parameters**

I’m working through the details for resetting gravity in the MuJoCo simulation. It looks like it should inherit the initial position settings from qpos0, according to the documentation. I need to set time to 0.002, with gravity at -9.81. In terms of the solver, I’m using Newton’s method with an implicit fast integrator, and I need to configure it to allow for 100 iterations. Let’s see if everything aligns correctly!