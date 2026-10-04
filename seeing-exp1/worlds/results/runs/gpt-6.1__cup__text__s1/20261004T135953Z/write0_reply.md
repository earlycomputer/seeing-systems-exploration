```xml
<mujoco model="ball_rolls_into_cup">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" cone="elliptic" iterations="80"/>

  <visual>
    <global azimuth="135" elevation="-25"/>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.65 0.65 0.65" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="-0.4 -1.5 3" dir="0.1 0.3 -1" directional="true"/>
    <camera name="overview" pos="1.4 -2.7 1.8" xyaxes="0.8619 0.5071 0 -0.226 0.384 0.895"/>

    <geom name="floor" type="plane" size="4 4 0.1" rgba="0.82 0.84 0.86 1" friction="0.9 0.005 0.005" condim="6"/>

    <!-- The ramp slopes downward toward +x. Its lower end overhangs the cup. -->
    <body name="ramp" pos="-0.503179 0 0.409898" quat="0.994521895 0 0.104528463 0">
      <geom name="ramp_surface" type="box" size="0.55 0.18 0.025" rgba="0.56 0.38 0.22 1" friction="0.9 0.005 0.0003" condim="6" solref="0.01 1"/>
      <geom name="ramp_rail_left" type="box" pos="0 0.192 0.05" size="0.55 0.012 0.05" rgba="0.42 0.27 0.15 1" friction="0.9 0.005 0.0003" condim="6"/>
      <geom name="ramp_rail_right" type="box" pos="0 -0.192 0.05" size="0.55 0.012 0.05" rgba="0.42 0.27 0.15 1" friction="0.9 0.005 0.0003" condim="6"/>
    </body>

    <geom name="ramp_support_upper" type="box" pos="-0.95 0 0.237" size="0.045 0.14 0.237" rgba="0.42 0.27 0.15 1"/>
    <geom name="ramp_support_lower" type="box" pos="-0.20 0 0.16" size="0.045 0.14 0.16" rgba="0.42 0.27 0.15 1"/>

    <!-- A solid bottom and overlapping wall segments make an open, hollow cup. -->
    <body name="cup" pos="0.25 0 0">
      <geom name="cup_bottom" type="cylinder" pos="0 0 0.0175" size="0.36 0.0175" rgba="0.16 0.38 0.68 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_00" type="box" pos="0.33 0 0.1475" euler="0 0 0" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_01" type="box" pos="0.318755 0.085410 0.1475" euler="0 0 15" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_02" type="box" pos="0.285788 0.165 0.1475" euler="0 0 30" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_03" type="box" pos="0.233345 0.233345 0.1475" euler="0 0 45" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_04" type="box" pos="0.165 0.285788 0.1475" euler="0 0 60" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_05" type="box" pos="0.085410 0.318755 0.1475" euler="0 0 75" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_06" type="box" pos="0 0.33 0.1475" euler="0 0 90" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_07" type="box" pos="-0.085410 0.318755 0.1475" euler="0 0 105" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_08" type="box" pos="-0.165 0.285788 0.1475" euler="0 0 120" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_09" type="box" pos="-0.233345 0.233345 0.1475" euler="0 0 135" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_10" type="box" pos="-0.285788 0.165 0.1475" euler="0 0 150" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_11" type="box" pos="-0.318755 0.085410 0.1475" euler="0 0 165" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_12" type="box" pos="-0.33 0 0.1475" euler="0 0 180" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_13" type="box" pos="-0.318755 -0.085410 0.1475" euler="0 0 195" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_14" type="box" pos="-0.285788 -0.165 0.1475" euler="0 0 210" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_15" type="box" pos="-0.233345 -0.233345 0.1475" euler="0 0 225" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_16" type="box" pos="-0.165 -0.285788 0.1475" euler="0 0 240" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_17" type="box" pos="-0.085410 -0.318755 0.1475" euler="0 0 255" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_18" type="box" pos="0 -0.33 0.1475" euler="0 0 270" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_19" type="box" pos="0.085410 -0.318755 0.1475" euler="0 0 285" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_20" type="box" pos="0.165 -0.285788 0.1475" euler="0 0 300" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_21" type="box" pos="0.233345 -0.233345 0.1475" euler="0 0 315" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_22" type="box" pos="0.285788 -0.165 0.1475" euler="0 0 330" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
      <geom name="cup_wall_23" type="box" pos="0.318755 -0.085410 0.1475" euler="0 0 345" size="0.02 0.046 0.1125" rgba="0.20 0.45 0.75 1" friction="1 0.01 0.005" condim="6" solref="0.01 1"/>
    </body>

    <!-- Gravity starts the ball; low ramp rolling resistance permits rolling. -->
    <body name="ball" pos="-0.927544 0 0.577797">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.05" mass="0.1" rgba="0.95 0.24 0.08 1" friction="0.9 0.005 0.0003" condim="6" solref="0.01 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-0.927544 0 0.577797 1 0 0 0" qvel="0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Evaluating ball ramp mechanics**

I’m working through the cup and ramp setup, focusing on the ball's launch and trajectory. The ball's edges, height, and cup dimensions need careful consideration to ensure it doesn't collide with the lip. The exit needs to be gentle, with proper velocity, and the ramp should end correctly inside the cup's center. I’m calculating necessary adjustments for the ramp length and angle, ensuring the ball lands effectively without issues.

**Designing ramp and cup mechanics**

I’m setting up a ramp with a length of 0.90 and a 12-degree slope, ensuring the top aligns at a specific height. The ball's rolling speed, based on a drop height, should be around 1.51, contributing to cumulative movement. I'm considering the cup dimensions for a good landing, while ensuring the ball rolls rather than slides down the ramp. Choosing an appropriate friction coefficient is crucial for the solid ball on a gentle slope.

**Considering XML options**

I’m thinking about how to provide XML header options, which could include timesteps, gravity, solver iterations, and integrator settings like implicit fast. There's also the option for keyframes — starting with unnecessary body positioning to account for gravity causing roll. I could include the keyframe name to set the start position automatically. And it seems valid to have keyframes default to zero for position and velocity unless specified otherwise. It’s a bit complex, but I’m working through it!