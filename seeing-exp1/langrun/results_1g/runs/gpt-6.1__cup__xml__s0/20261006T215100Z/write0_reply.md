```xml
<mujoco model="ball_ramp_cup">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" cone="elliptic" iterations="80"/>

  <visual>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.7 0.7 0.7"/>
    <global azimuth="135" elevation="-25"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="-1 -2 4" dir="0.2 0.3 -1"/>
    <camera name="overview" pos="2.8 -4 2.7" xyaxes="0.8 0.6 0 -0.3 0.4 0.866"/>

    <geom name="floor" type="plane" size="4 4 0.1" pos="0 0 0" rgba="0.82 0.84 0.87 1" friction="1 0.005 0.01" condim="6"/>

    <body name="ramp">
      <geom name="ramp_surface" type="box" pos="-0.760307 0 0.761351" euler="0 14.931417 0" size="0.776209 0.20 0.04" rgba="0.50 0.32 0.17 1" friction="0.8 0.002 0.001" condim="6" solref="0.008 1" solimp="0.95 0.99 0.001"/>
      <geom name="ramp_rail_left" type="box" pos="-0.744847 0.207 0.819325" euler="0 14.931417 0" size="0.776209 0.018 0.06" rgba="0.38 0.23 0.12 1" friction="0.8 0.002 0.001" condim="6"/>
      <geom name="ramp_rail_right" type="box" pos="-0.744847 -0.207 0.819325" euler="0 14.931417 0" size="0.776209 0.018 0.06" rgba="0.38 0.23 0.12 1" friction="0.8 0.002 0.001" condim="6"/>
      <geom name="ramp_support_high" type="box" pos="-1.30 0 0.432" size="0.07 0.16 0.432" rgba="0.38 0.23 0.12 1"/>
      <geom name="ramp_support_low" type="box" pos="-0.25 0 0.292" size="0.07 0.16 0.292" rgba="0.38 0.23 0.12 1"/>
    </body>

    <body name="cup" pos="0.60 0 0">
      <geom name="cup_base" type="cylinder" pos="0 0 0.03" size="0.56 0.03" rgba="0.12 0.38 0.65 1" friction="1.2 0.01 0.025" condim="6" solref="0.008 1" solimp="0.95 0.99 0.001"/>
      <geom name="cup_wall_00" type="box" pos="0.53 0 0.25" euler="0 0 0" size="0.03 0.11 0.20" rgba="0.16 0.46 0.74 1" friction="1.2 0.01 0.025" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_01" type="box" pos="0.489656 0.202817 0.25" euler="0 0 22.5" size="0.03 0.11 0.20" rgba="0.16 0.46 0.74 1" friction="1.2 0.01 0.025" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_02" type="box" pos="0.374767 0.374767 0.25" euler="0 0 45" size="0.03 0.11 0.20" rgba="0.16 0.46 0.74 1" friction="1.2 0.01 0.025" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_03" type="box" pos="0.202817 0.489656 0.25" euler="0 0 67.5" size="0.03 0.11 0.20" rgba="0.16 0.46 0.74 1" friction="1.2 0.01 0.025" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_04" type="box" pos="0 0.53 0.25" euler="0 0 90" size="0.03 0.11 0.20" rgba="0.16 0.46 0.74 1" friction="1.2 0.01 0.025" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_05" type="box" pos="-0.202817 0.489656 0.25" euler="0 0 112.5" size="0.03 0.11 0.20" rgba="0.16 0.46 0.74 1" friction="1.2 0.01 0.025" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_06" type="box" pos="-0.374767 0.374767 0.25" euler="0 0 135" size="0.03 0.11 0.20" rgba="0.16 0.46 0.74 1" friction="1.2 0.01 0.025" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_07" type="box" pos="-0.489656 0.202817 0.25" euler="0 0 157.5" size="0.03 0.11 0.20" rgba="0.16 0.46 0.74 1" friction="1.2 0.01 0.025" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_08" type="box" pos="-0.53 0 0.25" euler="0 0 180" size="0.03 0.11 0.20" rgba="0.16 0.46 0.74 1" friction="1.2 0.01 0.025" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_09" type="box" pos="-0.489656 -0.202817 0.25" euler="0 0 202.5" size="0.03 0.11 0.20" rgba="0.16 0.46 0.74 1" friction="1.2 0.01 0.025" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_10" type="box" pos="-0.374767 -0.374767 0.25" euler="0 0 225" size="0.03 0.11 0.20" rgba="0.16 0.46 0.74 1" friction="1.2 0.01 0.025" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_11" type="box" pos="-0.202817 -0.489656 0.25" euler="0 0 247.5" size="0.03 0.11 0.20" rgba="0.16 0.46 0.74 1" friction="1.2 0.01 0.025" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_12" type="box" pos="0 -0.53 0.25" euler="0 0 270" size="0.03 0.11 0.20" rgba="0.16 0.46 0.74 1" friction="1.2 0.01 0.025" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_13" type="box" pos="0.202817 -0.489656 0.25" euler="0 0 292.5" size="0.03 0.11 0.20" rgba="0.16 0.46 0.74 1" friction="1.2 0.01 0.025" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_14" type="box" pos="0.374767 -0.374767 0.25" euler="0 0 315" size="0.03 0.11 0.20" rgba="0.16 0.46 0.74 1" friction="1.2 0.01 0.025" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_15" type="box" pos="0.489656 -0.202817 0.25" euler="0 0 337.5" size="0.03 0.11 0.20" rgba="0.16 0.46 0.74 1" friction="1.2 0.01 0.025" condim="6" solref="0.008 1"/>
    </body>

    <body name="ball" pos="-1.35 0 1.0283">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.065" mass="0.12" rgba="1 0.65 0.08 1" friction="0.8 0.002 0.001" condim="6" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-1.35 0 1.0283 1 0 0 0" qvel="0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
ball touches ramp
ball comes to rest in cup
```