The first domino starts tilted 15° toward the others, with an initial tipping velocity. All remaining dominoes start upright.

```xml
<mujoco model="ten_domino_chain">
  <compiler angle="radian"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="100" cone="elliptic"/>

  <visual>
    <headlight ambient="0.4 0.4 0.4" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="0.3 -0.5 1.8" dir="0 0 -1"/>
    <camera name="overview" pos="0.3 -1.2 0.8" xyaxes="1 0 0 0 0.5 0.8660254"/>

    <geom name="floor" type="plane" pos="0 0 0" size="2 2 0.1" friction="0.8 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.25 0.28 0.32 1"/>

    <body name="domino1" pos="0 0 0.119016928" quat="0.9914448614 0 0.1305261922 0">
      <freejoint name="domino1_free"/>
      <geom name="domino1_geom" type="box" size="0.012 0.04 0.12" mass="0.12" friction="0.8 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.85 0.25 0.15 1"/>
    </body>

    <body name="domino2" pos="0.06 0 0.12">
      <freejoint name="domino2_free"/>
      <geom name="domino2_geom" type="box" size="0.012 0.04 0.12" mass="0.12" friction="0.8 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.9 0.65 0.2 1"/>
    </body>

    <body name="domino3" pos="0.12 0 0.12">
      <freejoint name="domino3_free"/>
      <geom name="domino3_geom" type="box" size="0.012 0.04 0.12" mass="0.12" friction="0.8 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.9 0.65 0.2 1"/>
    </body>

    <body name="domino4" pos="0.18 0 0.12">
      <freejoint name="domino4_free"/>
      <geom name="domino4_geom" type="box" size="0.012 0.04 0.12" mass="0.12" friction="0.8 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.9 0.65 0.2 1"/>
    </body>

    <body name="domino5" pos="0.24 0 0.12">
      <freejoint name="domino5_free"/>
      <geom name="domino5_geom" type="box" size="0.012 0.04 0.12" mass="0.12" friction="0.8 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.9 0.65 0.2 1"/>
    </body>

    <body name="domino6" pos="0.30 0 0.12">
      <freejoint name="domino6_free"/>
      <geom name="domino6_geom" type="box" size="0.012 0.04 0.12" mass="0.12" friction="0.8 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.9 0.65 0.2 1"/>
    </body>

    <body name="domino7" pos="0.36 0 0.12">
      <freejoint name="domino7_free"/>
      <geom name="domino7_geom" type="box" size="0.012 0.04 0.12" mass="0.12" friction="0.8 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.9 0.65 0.2 1"/>
    </body>

    <body name="domino8" pos="0.42 0 0.12">
      <freejoint name="domino8_free"/>
      <geom name="domino8_geom" type="box" size="0.012 0.04 0.12" mass="0.12" friction="0.8 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.9 0.65 0.2 1"/>
    </body>

    <body name="domino9" pos="0.48 0 0.12">
      <freejoint name="domino9_free"/>
      <geom name="domino9_geom" type="box" size="0.012 0.04 0.12" mass="0.12" friction="0.8 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.9 0.65 0.2 1"/>
    </body>

    <body name="domino10" pos="0.54 0 0.12">
      <freejoint name="domino10_free"/>
      <geom name="domino10_geom" type="box" size="0.012 0.04 0.12" mass="0.12" friction="0.8 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.25 0.55 0.85 1"/>
    </body>
  </worldbody>

  <keyframe>
    <!-- Positions default to the body poses above. Each velocity group has six entries. -->
    <key name="start" qvel="0.238034 0 -0.038934 0 2 0   0 0 0 0 0 0   0 0 0 0 0 0   0 0 0 0 0 0   0 0 0 0 0 0   0 0 0 0 0 0   0 0 0 0 0 0   0 0 0 0 0 0   0 0 0 0 0 0   0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Understanding MuJoCo Configurations**

I need to understand the default keyframe positions in the MuJoCo model, specifically setting all joints to their initial positions. To start, I intend to tilt the body’s first pose by 10° and set the initial rotation for keyframe velocity accordingly, while the rest will remain as zeros. It is crucial to ensure that the initial setup isn't intersecting the floor and that the physics feel logical when tilted appropriately. I'm also considering dimensions and mass requirements.

**Evaluating gravitational drive**

I'm calculating some factors here. Starting with a cosine calculation brings me to about .04159. Next, I'm looking at gravitational drive and considering a range from 25° to 28°. It seems like that should be sufficient. I wonder if I can lean about 10 degrees at the beginning. There’s an option to use a lean of just 15 without keyframe simulation, but kicking seems like a safer choice overall. Let's see how that plays out!