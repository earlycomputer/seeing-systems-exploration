```xml
<mujoco model="ball_rolls_into_cup">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" cone="elliptic" iterations="80"/>
  <visual>
    <global azimuth="135" elevation="-25"/>
  </visual>
  <worldbody>
    <light name="overhead" pos="-0.5 -1.5 3" dir="0.1 0.3 -1"/>
    <camera name="overview" pos="-0.2 -3 1.9" xyaxes="1 0 0 0 0.45 0.893"/>
    <geom name="floor" type="plane" size="4 4 0.1" rgba="0.82 0.85 0.88 1" friction="0.9 0.02 0.015"/>

    <body name="ramp">
      <geom name="ramp_surface" type="box" pos="-0.757906 0 0.676283" euler="0 18.434949 0" size="0.632456 0.16 0.025" rgba="0.65 0.43 0.22 1" friction="0.9 0.005 0.006" condim="6" solref="0.012 1"/>
      <geom name="ramp_support_high" type="box" pos="-1.22 0 0.4" size="0.045 0.13 0.4" rgba="0.36 0.28 0.20 1"/>
      <geom name="ramp_support_low" type="box" pos="-0.5 0 0.275" size="0.045 0.13 0.275" rgba="0.36 0.28 0.20 1"/>
    </body>

    <body name="cup" pos="0.2 0 0">
      <geom name="cup_bottom" type="cylinder" pos="0 0 0.035" size="0.52 0.035" rgba="0.15 0.42 0.68 1" friction="0.9 0.02 0.02" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_00" type="box" pos="0.49 0 0.235" euler="0 0 0" size="0.03 0.103 0.185" rgba="0.18 0.48 0.75 1" friction="0.9 0.02 0.02" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_01" type="box" pos="0.452701 0.187515 0.235" euler="0 0 22.5" size="0.03 0.103 0.185" rgba="0.18 0.48 0.75 1" friction="0.9 0.02 0.02" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_02" type="box" pos="0.346482 0.346482 0.235" euler="0 0 45" size="0.03 0.103 0.185" rgba="0.18 0.48 0.75 1" friction="0.9 0.02 0.02" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_03" type="box" pos="0.187515 0.452701 0.235" euler="0 0 67.5" size="0.03 0.103 0.185" rgba="0.18 0.48 0.75 1" friction="0.9 0.02 0.02" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_04" type="box" pos="0 0.49 0.235" euler="0 0 90" size="0.03 0.103 0.185" rgba="0.18 0.48 0.75 1" friction="0.9 0.02 0.02" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_05" type="box" pos="-0.187515 0.452701 0.235" euler="0 0 112.5" size="0.03 0.103 0.185" rgba="0.18 0.48 0.75 1" friction="0.9 0.02 0.02" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_06" type="box" pos="-0.346482 0.346482 0.235" euler="0 0 135" size="0.03 0.103 0.185" rgba="0.18 0.48 0.75 1" friction="0.9 0.02 0.02" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_07" type="box" pos="-0.452701 0.187515 0.235" euler="0 0 157.5" size="0.03 0.103 0.185" rgba="0.18 0.48 0.75 1" friction="0.9 0.02 0.02" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_08" type="box" pos="-0.49 0 0.235" euler="0 0 180" size="0.03 0.103 0.185" rgba="0.18 0.48 0.75 1" friction="0.9 0.02 0.02" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_09" type="box" pos="-0.452701 -0.187515 0.235" euler="0 0 202.5" size="0.03 0.103 0.185" rgba="0.18 0.48 0.75 1" friction="0.9 0.02 0.02" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_10" type="box" pos="-0.346482 -0.346482 0.235" euler="0 0 225" size="0.03 0.103 0.185" rgba="0.18 0.48 0.75 1" friction="0.9 0.02 0.02" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_11" type="box" pos="-0.187515 -0.452701 0.235" euler="0 0 247.5" size="0.03 0.103 0.185" rgba="0.18 0.48 0.75 1" friction="0.9 0.02 0.02" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_12" type="box" pos="0 -0.49 0.235" euler="0 0 270" size="0.03 0.103 0.185" rgba="0.18 0.48 0.75 1" friction="0.9 0.02 0.02" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_13" type="box" pos="0.187515 -0.452701 0.235" euler="0 0 292.5" size="0.03 0.103 0.185" rgba="0.18 0.48 0.75 1" friction="0.9 0.02 0.02" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_14" type="box" pos="0.346482 -0.346482 0.235" euler="0 0 315" size="0.03 0.103 0.185" rgba="0.18 0.48 0.75 1" friction="0.9 0.02 0.02" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_15" type="box" pos="0.452701 -0.187515 0.235" euler="0 0 337.5" size="0.03 0.103 0.185" rgba="0.18 0.48 0.75 1" friction="0.9 0.02 0.02" condim="6" solref="0.01 1"/>
    </body>

    <body name="ball" pos="-1.2338 0 0.9255">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.06" mass="0.12" rgba="0.95 0.24 0.08 1" friction="0.9 0.005 0.006" condim="6" solref="0.01 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-1.2338 0 0.9255 1 0 0 0" qvel="0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
ball touches ramp
ball comes to rest in cup
```

---
thinking (summarized):

**Considering ramp support design**

I need to think about the ramp support for a floating structure. It looks like I’ll need to use primitive boxes under the ramp for support. I’m planning to position the box supports carefully, ensuring they align correctly with the ramp. For instance, I've noted their dimensions and placements. I want to organize them neatly without adding unnecessary clutter to the ramp body, so I might name these supports with a consistent prefix for clarity. Let's make sure everything fits well!

**Evaluating ramp aesthetics and supports**

I'm considering the ramp's aesthetics alongside its supports. I want to ensure that these vertical supports don’t obstruct anything, particularly since they're positioned below the ramp. The top height of the support should be just right, ideally around 0.8. I'm thinking through dimensions, making sure I'm calculating correctly to avoid issues where supports might protrude unintentionally. I also need to think about the ramp box's proper positioning, so it fits nicely without interference or friction complications. Let's keep refining this!