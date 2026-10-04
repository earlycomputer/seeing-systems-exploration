The first domino starts tilted 20° toward the others, allowing gravity to initiate the cascade.

```xml
<mujoco model="ten_domino_cascade">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" iterations="100"/>
  <size nconmax="300" njmax="1000"/>

  <visual>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="0.2 -0.3 1" dir="0 0.3 -1" directional="true"/>
    <camera name="overview" pos="0.2 -0.65 0.36" xyaxes="1 0 0 0 0.485 0.875"/>
    <geom name="floor" type="plane" pos="0 0 0" size="1 0.5 0.1" friction="0.8 0.005 0.0001" condim="3" solref="0.01 1" solimp="0.95 0.99 0.001" rgba="0.22 0.24 0.27 1"/>

    <body name="domino1" pos="0 0 0.059901758" quat="0.984807753 0 0.173648178 0">
      <freejoint name="domino1_joint"/>
      <geom name="domino1_geom" type="box" size="0.01 0.03 0.06" mass="0.08" friction="0.8 0.005 0.0001" condim="3" solref="0.01 1" solimp="0.95 0.99 0.001" rgba="0.9 0.25 0.12 1"/>
    </body>

    <body name="domino2" pos="0.045 0 0.0601">
      <freejoint name="domino2_joint"/>
      <geom name="domino2_geom" type="box" size="0.01 0.03 0.06" mass="0.08" friction="0.8 0.005 0.0001" condim="3" solref="0.01 1" solimp="0.95 0.99 0.001" rgba="0.95 0.55 0.15 1"/>
    </body>

    <body name="domino3" pos="0.090 0 0.0601">
      <freejoint name="domino3_joint"/>
      <geom name="domino3_geom" type="box" size="0.01 0.03 0.06" mass="0.08" friction="0.8 0.005 0.0001" condim="3" solref="0.01 1" solimp="0.95 0.99 0.001" rgba="0.95 0.72 0.18 1"/>
    </body>

    <body name="domino4" pos="0.135 0 0.0601">
      <freejoint name="domino4_joint"/>
      <geom name="domino4_geom" type="box" size="0.01 0.03 0.06" mass="0.08" friction="0.8 0.005 0.0001" condim="3" solref="0.01 1" solimp="0.95 0.99 0.001" rgba="0.55 0.75 0.25 1"/>
    </body>

    <body name="domino5" pos="0.180 0 0.0601">
      <freejoint name="domino5_joint"/>
      <geom name="domino5_geom" type="box" size="0.01 0.03 0.06" mass="0.08" friction="0.8 0.005 0.0001" condim="3" solref="0.01 1" solimp="0.95 0.99 0.001" rgba="0.2 0.7 0.4 1"/>
    </body>

    <body name="domino6" pos="0.225 0 0.0601">
      <freejoint name="domino6_joint"/>
      <geom name="domino6_geom" type="box" size="0.01 0.03 0.06" mass="0.08" friction="0.8 0.005 0.0001" condim="3" solref="0.01 1" solimp="0.95 0.99 0.001" rgba="0.15 0.65 0.65 1"/>
    </body>

    <body name="domino7" pos="0.270 0 0.0601">
      <freejoint name="domino7_joint"/>
      <geom name="domino7_geom" type="box" size="0.01 0.03 0.06" mass="0.08" friction="0.8 0.005 0.0001" condim="3" solref="0.01 1" solimp="0.95 0.99 0.001" rgba="0.2 0.5 0.85 1"/>
    </body>

    <body name="domino8" pos="0.315 0 0.0601">
      <freejoint name="domino8_joint"/>
      <geom name="domino8_geom" type="box" size="0.01 0.03 0.06" mass="0.08" friction="0.8 0.005 0.0001" condim="3" solref="0.01 1" solimp="0.95 0.99 0.001" rgba="0.35 0.35 0.85 1"/>
    </body>

    <body name="domino9" pos="0.360 0 0.0601">
      <freejoint name="domino9_joint"/>
      <geom name="domino9_geom" type="box" size="0.01 0.03 0.06" mass="0.08" friction="0.8 0.005 0.0001" condim="3" solref="0.01 1" solimp="0.95 0.99 0.001" rgba="0.6 0.3 0.8 1"/>
    </body>

    <body name="domino10" pos="0.405 0 0.0601">
      <freejoint name="domino10_joint"/>
      <geom name="domino10_geom" type="box" size="0.01 0.03 0.06" mass="0.08" friction="0.8 0.005 0.0001" condim="3" solref="0.01 1" solimp="0.95 0.99 0.001" rgba="0.8 0.3 0.6 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start"/>
  </keyframe>
</mujoco>
```