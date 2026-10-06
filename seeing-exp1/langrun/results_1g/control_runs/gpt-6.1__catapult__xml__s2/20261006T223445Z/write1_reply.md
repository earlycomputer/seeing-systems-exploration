```xml
<mujoco model="spring_catapult_into_bucket">
  <compiler angle="radian" autolimits="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="100"/>
  <size njmax="2000" nconmax="200"/>

  <visual>
    <global azimuth="135" elevation="-20"/>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="1.5 -2 5" dir="0 0 -1"/>
    <camera name="overview" pos="1.5 -6 3" xyaxes="1 0 0 0 0.4 0.916515"/>

    <geom name="floor" type="plane" pos="0 0 0" size="6 4 0.1" rgba="0.28 0.32 0.28 1" friction="1 0.03 0.02" condim="6" solref="0.015 1"/>

    <body name="catapult_base" pos="1 0 0">
      <geom name="catapult_base_plate" type="box" pos="0 0 0.05" size="0.35 0.32 0.05" rgba="0.32 0.19 0.09 1"/>
      <geom name="catapult_left_support" type="box" pos="0 -0.18 0.175" size="0.055 0.055 0.125" rgba="0.45 0.28 0.12 1"/>
      <geom name="catapult_right_support" type="box" pos="0 0.18 0.175" size="0.055 0.055 0.125" rgba="0.45 0.28 0.12 1"/>
      <geom name="catapult_axle" type="cylinder" pos="0 0 0.25" quat="0.707106781 0.707106781 0 0" size="0.04 0.25" rgba="0.25 0.27 0.3 1"/>

      <body name="catapult_arm" pos="0 0 0.25">
        <inertial pos="-0.45 0 0.03" mass="0.45" diaginertia="0.004 0.08 0.08"/>
        <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 0.785398163" stiffness="6.9" springref="1.25" damping="0.06" armature="0" solreflimit="0.004 1" solimplimit="0.999 0.999 0.001"/>
        <!-- The beam ends 10 mm clear of the axle's radial surface. -->
        <geom name="catapult_arm_beam" type="box" pos="-0.55 0 0" size="0.5 0.035 0.035" rgba="0.6 0.37 0.15 1" friction="0.02 0.001 0.0001" priority="1" condim="3"/>
        <geom name="catapult_cup_stem" type="box" pos="-1 0 0.065" size="0.04 0.04 0.065" rgba="0.4 0.25 0.12 1" friction="0.02 0.001 0.0001" priority="1" condim="3"/>
        <geom name="catapult_cup_floor" type="box" pos="-1 0 0.11" size="0.102 0.082 0.02" rgba="0.24 0.26 0.3 1" friction="0.02 0.001 0.0001" priority="1" condim="3" solref="0.004 1"/>
        <geom name="catapult_cup_outer_wall" type="box" pos="-1.081 0 0.21" size="0.02 0.082 0.08" rgba="0.24 0.26 0.3 1" friction="0.02 0.001 0.0001" priority="1" condim="3" solref="0.004 1"/>
        <geom name="catapult_cup_inner_wall" type="box" pos="-0.919 0 0.21" size="0.02 0.082 0.08" rgba="0.24 0.26 0.3 1" friction="0.02 0.001 0.0001" priority="1" condim="3" solref="0.004 1"/>
        <geom name="catapult_cup_left_wall" type="box" pos="-1 -0.082 0.21" size="0.102 0.014 0.08" rgba="0.24 0.26 0.3 1" friction="0.02 0.001 0.0001" priority="1" condim="3" solref="0.004 1"/>
        <geom name="catapult_cup_right_wall" type="box" pos="-1 0.082 0.21" size="0.102 0.014 0.08" rgba="0.24 0.26 0.3 1" friction="0.02 0.001 0.0001" priority="1" condim="3" solref="0.004 1"/>
      </body>
    </body>

    <!-- The bucket centre is exactly 3 m from the initial ball centre. -->
    <!-- A cylinder forms the bottom; twelve overlapping boxes form the open walls. -->
    <body name="bucket" pos="3 0 0.44">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 -0.4" size="0.865 0.04" rgba="0.12 0.34 0.58 1" friction="1 0.04 0.03" condim="6" solref="0.015 1"/>
      <geom name="bucket_wall_00" type="box" pos="0.8 0 0.04" size="0.035 0.22 0.4" euler="0 0 0" rgba="0.16 0.42 0.7 1" friction="1 0.04 0.03" condim="6" solref="0.015 1"/>
      <geom name="bucket_wall_01" type="box" pos="0.692820323 0.4 0.04" size="0.035 0.22 0.4" euler="0 0 0.523598776" rgba="0.16 0.42 0.7 1" friction="1 0.04 0.03" condim="6" solref="0.015 1"/>
      <geom name="bucket_wall_02" type="box" pos="0.4 0.692820323 0.04" size="0.035 0.22 0.4" euler="0 0 1.047197551" rgba="0.16 0.42 0.7 1" friction="1 0.04 0.03" condim="6" solref="0.015 1"/>
      <geom name="bucket_wall_03" type="box" pos="0 0.8 0.04" size="0.035 0.22 0.4" euler="0 0 1.570796327" rgba="0.16 0.42 0.7 1" friction="1 0.04 0.03" condim="6" solref="0.015 1"/>
      <geom name="bucket_wall_04" type="box" pos="-0.4 0.692820323 0.04" size="0.035 0.22 0.4" euler="0 0 2.094395102" rgba="0.16 0.42 0.7 1" friction="1 0.04 0.03" condim="6" solref="0.015 1"/>
      <geom name="bucket_wall_05" type="box" pos="-0.692820323 0.4 0.04" size="0.035 0.22 0.4" euler="0 0 2.617993878" rgba="0.16 0.42 0.7 1" friction="1 0.04 0.03" condim="6" solref="0.015 1"/>
      <geom name="bucket_wall_06" type="box" pos="-0.8 0 0.04" size="0.035 0.22 0.4" euler="0 0 3.141592654" rgba="0.16 0.42 0.7 1" friction="1 0.04 0.03" condim="6" solref="0.015 1"/>
      <geom name="bucket_wall_07" type="box" pos="-0.692820323 -0.4 0.04" size="0.035 0.22 0.4" euler="0 0 3.665191429" rgba="0.16 0.42 0.7 1" friction="1 0.04 0.03" condim="6" solref="0.015 1"/>
      <geom name="bucket_wall_08" type="box" pos="-0.4 -0.692820323 0.04" size="0.035 0.22 0.4" euler="0 0 4.188790205" rgba="0.16 0.42 0.7 1" friction="1 0.04 0.03" condim="6" solref="0.015 1"/>
      <geom name="bucket_wall_09" type="box" pos="0 -0.8 0.04" size="0.035 0.22 0.4" euler="0 0 4.71238898" rgba="0.16 0.42 0.7 1" friction="1 0.04 0.03" condim="6" solref="0.015 1"/>
      <geom name="bucket_wall_10" type="box" pos="0.4 -0.692820323 0.04" size="0.035 0.22 0.4" euler="0 0 5.235987756" rgba="0.16 0.42 0.7 1" friction="1 0.04 0.03" condim="6" solref="0.015 1"/>
      <geom name="bucket_wall_11" type="box" pos="0.692820323 -0.4 0.04" size="0.035 0.22 0.4" euler="0 0 5.759586532" rgba="0.16 0.42 0.7 1" friction="1 0.04 0.03" condim="6" solref="0.015 1"/>
    </body>

    <body name="ball" pos="0 0 0.44">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.06" mass="0.1" rgba="0.95 0.3 0.08 1" friction="1 0.04 0.03" condim="6" solref="0.008 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 0 0 0.44 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```