The first domino starts tilted toward the other nine. Gravity drives the chain reaction.

```xml
<mujoco model="ten_dominoes">
  <compiler angle="degree"/>
  <option timestep="0.002"/>

  <worldbody>
    <light name="overhead_light" pos="0.35 -0.5 2" dir="0 0 -1"/>
    <geom name="floor" type="plane" pos="0 0 0" size="1.5 1 0.1" friction="1 0.005 0.0001" rgba="0.25 0.28 0.32 1"/>

    <body name="domino1" pos="0 0 0.1168673562" quat="0.984807753 0 0.173648178 0">
      <freejoint name="domino1_free"/>
      <geom name="domino1_geom" type="box" size="0.012 0.05 0.12" mass="0.1" friction="0.6 0.005 0.0001" rgba="0.9 0.3 0.12 1"/>
    </body>

    <body name="domino2" pos="0.07 0 0.12">
      <freejoint name="domino2_free"/>
      <geom name="domino2_geom" type="box" size="0.012 0.05 0.12" mass="0.1" friction="0.6 0.005 0.0001" rgba="0.15 0.55 0.85 1"/>
    </body>

    <body name="domino3" pos="0.14 0 0.12">
      <freejoint name="domino3_free"/>
      <geom name="domino3_geom" type="box" size="0.012 0.05 0.12" mass="0.1" friction="0.6 0.005 0.0001" rgba="0.95 0.7 0.15 1"/>
    </body>

    <body name="domino4" pos="0.21 0 0.12">
      <freejoint name="domino4_free"/>
      <geom name="domino4_geom" type="box" size="0.012 0.05 0.12" mass="0.1" friction="0.6 0.005 0.0001" rgba="0.15 0.55 0.85 1"/>
    </body>

    <body name="domino5" pos="0.28 0 0.12">
      <freejoint name="domino5_free"/>
      <geom name="domino5_geom" type="box" size="0.012 0.05 0.12" mass="0.1" friction="0.6 0.005 0.0001" rgba="0.95 0.7 0.15 1"/>
    </body>

    <body name="domino6" pos="0.35 0 0.12">
      <freejoint name="domino6_free"/>
      <geom name="domino6_geom" type="box" size="0.012 0.05 0.12" mass="0.1" friction="0.6 0.005 0.0001" rgba="0.15 0.55 0.85 1"/>
    </body>

    <body name="domino7" pos="0.42 0 0.12">
      <freejoint name="domino7_free"/>
      <geom name="domino7_geom" type="box" size="0.012 0.05 0.12" mass="0.1" friction="0.6 0.005 0.0001" rgba="0.95 0.7 0.15 1"/>
    </body>

    <body name="domino8" pos="0.49 0 0.12">
      <freejoint name="domino8_free"/>
      <geom name="domino8_geom" type="box" size="0.012 0.05 0.12" mass="0.1" friction="0.6 0.005 0.0001" rgba="0.15 0.55 0.85 1"/>
    </body>

    <body name="domino9" pos="0.56 0 0.12">
      <freejoint name="domino9_free"/>
      <geom name="domino9_geom" type="box" size="0.012 0.05 0.12" mass="0.1" friction="0.6 0.005 0.0001" rgba="0.95 0.7 0.15 1"/>
    </body>

    <body name="domino10" pos="0.63 0 0.12">
      <freejoint name="domino10_free"/>
      <geom name="domino10_geom" type="box" size="0.012 0.05 0.12" mass="0.1" friction="0.6 0.005 0.0001" rgba="0.15 0.55 0.85 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start"/>
  </keyframe>
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
domino1 ends tilted at least 15 degrees from upright
domino2 ends tilted at least 15 degrees from upright
domino3 ends tilted at least 15 degrees from upright
domino4 ends tilted at least 15 degrees from upright
domino5 ends tilted at least 15 degrees from upright
domino6 ends tilted at least 15 degrees from upright
domino7 ends tilted at least 15 degrees from upright
domino8 ends tilted at least 15 degrees from upright
domino9 ends tilted at least 15 degrees from upright
domino10 ends tilted at least 15 degrees from upright
```

---
thinking (summarized):

**Considering domino dimensions**

I'm thinking about the dimensions of dominoes and whether the width of 0.1 and aspect ratio of 0.024 will work effectively. The end angles being greater than 15 degrees could create issues if they scatter. But maybe I’m overthinking it! I’ll aim for a minimal final XML to keep it straightforward. It’s interesting to juggle these calculations while keeping things simple. Let’s focus on getting it right without complicating it too much!