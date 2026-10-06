The first domino starts tilted beyond its balance point. Gravity tips it into the remaining nine, with close spacing to carry the chain reaction along the row.

```xml
<mujoco model="ten_domino_chain">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="100" cone="elliptic"/>
  <visual>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.65 0.65 0.65" specular="0.2 0.2 0.2"/>
  </visual>
  <worldbody>
    <light name="overhead_light" pos="0.3 -0.5 2" dir="0 0 -1" directional="true"/>
    <camera name="overview" pos="0.3 -1.3 0.8" xyaxes="1 0 0 0 0.447214 0.894427"/>
    <geom name="floor" type="plane" pos="0 0 0" size="2 1 0.1" friction="0.7 0.005 0.0001" condim="3" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.25 0.28 0.3 1"/>
    <body name="domino1" pos="0.020959319 0 0.119566116" quat="0.996194698 0 0.087155743 0">
      <freejoint name="domino1_free"/>
      <geom name="domino1_box" type="box" size="0.008 0.035 0.12" mass="0.1" friction="0.7 0.005 0.0001" condim="3" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.9 0.25 0.15 1"/>
    </body>
    <body name="domino2" pos="0.065 0 0.12">
      <freejoint name="domino2_free"/>
      <geom name="domino2_box" type="box" size="0.008 0.035 0.12" mass="0.1" friction="0.7 0.005 0.0001" condim="3" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.95 0.7 0.2 1"/>
    </body>
    <body name="domino3" pos="0.130 0 0.12">
      <freejoint name="domino3_free"/>
      <geom name="domino3_box" type="box" size="0.008 0.035 0.12" mass="0.1" friction="0.7 0.005 0.0001" condim="3" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.9 0.25 0.15 1"/>
    </body>
    <body name="domino4" pos="0.195 0 0.12">
      <freejoint name="domino4_free"/>
      <geom name="domino4_box" type="box" size="0.008 0.035 0.12" mass="0.1" friction="0.7 0.005 0.0001" condim="3" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.95 0.7 0.2 1"/>
    </body>
    <body name="domino5" pos="0.260 0 0.12">
      <freejoint name="domino5_free"/>
      <geom name="domino5_box" type="box" size="0.008 0.035 0.12" mass="0.1" friction="0.7 0.005 0.0001" condim="3" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.9 0.25 0.15 1"/>
    </body>
    <body name="domino6" pos="0.325 0 0.12">
      <freejoint name="domino6_free"/>
      <geom name="domino6_box" type="box" size="0.008 0.035 0.12" mass="0.1" friction="0.7 0.005 0.0001" condim="3" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.95 0.7 0.2 1"/>
    </body>
    <body name="domino7" pos="0.390 0 0.12">
      <freejoint name="domino7_free"/>
      <geom name="domino7_box" type="box" size="0.008 0.035 0.12" mass="0.1" friction="0.7 0.005 0.0001" condim="3" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.9 0.25 0.15 1"/>
    </body>
    <body name="domino8" pos="0.455 0 0.12">
      <freejoint name="domino8_free"/>
      <geom name="domino8_box" type="box" size="0.008 0.035 0.12" mass="0.1" friction="0.7 0.005 0.0001" condim="3" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.95 0.7 0.2 1"/>
    </body>
    <body name="domino9" pos="0.520 0 0.12">
      <freejoint name="domino9_free"/>
      <geom name="domino9_box" type="box" size="0.008 0.035 0.12" mass="0.1" friction="0.7 0.005 0.0001" condim="3" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.9 0.25 0.15 1"/>
    </body>
    <body name="domino10" pos="0.585 0 0.12">
      <freejoint name="domino10_free"/>
      <geom name="domino10_box" type="box" size="0.008 0.035 0.12" mass="0.1" friction="0.7 0.005 0.0001" condim="3" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.95 0.7 0.2 1"/>
    </body>
  </worldbody>
</mujoco>
```

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