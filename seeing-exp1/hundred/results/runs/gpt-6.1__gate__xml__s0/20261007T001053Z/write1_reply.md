```xml
<mujoco model="ball_paddle_slider_drop">
  <compiler angle="degree" inertiafromgeom="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" cone="elliptic" iterations="80"/>
  <size njmax="300" nconmax="150"/>

  <visual>
    <headlight ambient="0.45 0.45 0.45" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
    <map znear="0.01" zfar="20"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="1.4 -2 5" dir="0.1 0.3 -1"/>
    <camera name="overview" pos="4 -5 3.4" xyaxes="0.86 0.51 0 -0.23 0.39 0.89"/>

    <geom name="floor" type="plane" size="6 6 0.1" friction="0.8 0.01 0.025" condim="6" rgba="0.22 0.25 0.28 1"/>

    <!-- The ball starts one metre uphill along the ramp surface. -->
    <body name="ramp">
      <geom name="ramp_slope" type="box" pos="0.519774 -0.4 1.024066" quat="0.991444861 0 0.130526192 0" size="0.59 0.17 0.04" friction="0.7 0.005 0.0005" condim="6" rgba="0.42 0.48 0.56 1"/>
      <geom name="ramp_apron" type="box" pos="1.48 -0.4 0.89" size="0.40 0.17 0.02" friction="0.7 0.005 0.0005" condim="6" rgba="0.42 0.48 0.56 1"/>
      <geom name="ramp_support" type="box" pos="0.50 -0.4 0.43" size="0.38 0.13 0.43" rgba="0.30 0.35 0.41 1"/>
      <geom name="ramp_apron_support" type="box" pos="1.62 -0.4 0.435" size="0.08 0.13 0.435" rgba="0.30 0.35 0.41 1"/>
    </body>

    <body name="ball" pos="0.157368 -0.4 1.255752">
      <freejoint name="ball_free"/>
      <geom name="ball_sphere" type="sphere" size="0.09" mass="0.8" friction="0.7 0.005 0.0005" condim="6" solref="0.008 1" rgba="0.94 0.29 0.12 1"/>
    </body>

    <geom name="paddle_pedestal" type="cylinder" pos="1.25 0.70 0.42" size="0.065 0.42" rgba="0.28 0.31 0.36 1"/>

    <!-- The arm bottom is at z=0.92, clearing the apron top at z=0.91. -->
    <body name="paddle" pos="1.25 0.70 1.0">
      <joint name="paddle_hinge" type="hinge" axis="0 0 1" limited="true" range="0 70" damping="0.08" frictionloss="0.02" armature="0.002"/>
      <geom name="paddle_arm" type="box" pos="0 -0.65 0" size="0.035 0.65 0.08" mass="0.24" friction="0.25 0.005 0.0001" solref="0.008 1" rgba="0.96 0.67 0.12 1"/>
      <geom name="paddle_hub" type="cylinder" size="0.055 0.12" mass="0.025" rgba="0.72 0.46 0.08 1"/>
    </body>

    <geom name="slider_guide_base" type="box" pos="1.67 0 0.87" size="0.40 0.105 0.02" rgba="0.30 0.34 0.38 1"/>

    <body name="slider" pos="1.50 0 1.0">
      <joint name="slider_slide" type="slide" axis="1 0 0" limited="true" range="0 0.45" damping="0.8" frictionloss="0.04" armature="0.005" solreflimit="0.006 1"/>
      <geom name="slider_striker" type="box" size="0.18 0.075 0.055" mass="0.20" friction="0.25 0.005 0.0001" solref="0.008 1" rgba="0.12 0.57 0.84 1"/>
    </body>

    <body name="ledge">
      <geom name="ledge_top" type="box" pos="1.91 0 0.89" size="0.13 0.16 0.035" friction="0.18 0.005 0.0001" rgba="0.55 0.43 0.31 1"/>
      <geom name="ledge_leg_left" type="cylinder" pos="1.82 -0.12 0.4275" size="0.022 0.4275" rgba="0.40 0.31 0.23 1"/>
      <geom name="ledge_leg_right" type="cylinder" pos="1.82 0.12 0.4275" size="0.022 0.4275" rgba="0.40 0.31 0.23 1"/>
    </body>

    <body name="block" pos="1.955 0 1.0">
      <freejoint name="block_free"/>
      <geom name="block_payload" type="box" size="0.075 0.075 0.075" mass="0.075" friction="0.35 0.01 0.001" condim="6" solref="0.008 1" rgba="0.70 0.25 0.77 1"/>
    </body>

    <body name="hoop">
      <geom name="hoop_segment_01" type="capsule" fromto="2.960000 0.000000 0.60 2.917373 0.214303 0.60" size="0.022" rgba="0.20 0.83 0.49 1"/>
      <geom name="hoop_segment_02" type="capsule" fromto="2.917373 0.214303 0.60 2.795980 0.395980 0.60" size="0.022" rgba="0.20 0.83 0.49 1"/>
      <geom name="hoop_segment_03" type="capsule" fromto="2.795980 0.395980 0.60 2.614303 0.517373 0.60" size="0.022" rgba="0.20 0.83 0.49 1"/>
      <geom name="hoop_segment_04" type="capsule" fromto="2.614303 0.517373 0.60 2.400000 0.560000 0.60" size="0.022" rgba="0.20 0.83 0.49 1"/>
      <geom name="hoop_segment_05" type="capsule" fromto="2.400000 0.560000 0.60 2.185697 0.517373 0.60" size="0.022" rgba="0.20 0.83 0.49 1"/>
      <geom name="hoop_segment_06" type="capsule" fromto="2.185697 0.517373 0.60 2.004020 0.395980 0.60" size="0.022" rgba="0.20 0.83 0.49 1"/>
      <geom name="hoop_segment_07" type="capsule" fromto="2.004020 0.395980 0.60 1.882627 0.214303 0.60" size="0.022" rgba="0.20 0.83 0.49 1"/>
      <geom name="hoop_segment_08" type="capsule" fromto="1.882627 0.214303 0.60 1.840000 0.000000 0.60" size="0.022" rgba="0.20 0.83 0.49 1"/>
      <geom name="hoop_segment_09" type="capsule" fromto="1.840000 0.000000 0.60 1.882627 -0.214303 0.60" size="0.022" rgba="0.20 0.83 0.49 1"/>
      <geom name="hoop_segment_10" type="capsule" fromto="1.882627 -0.214303 0.60 2.004020 -0.395980 0.60" size="0.022" rgba="0.20 0.83 0.49 1"/>
      <geom name="hoop_segment_11" type="capsule" fromto="2.004020 -0.395980 0.60 2.185697 -0.517373 0.60" size="0.022" rgba="0.20 0.83 0.49 1"/>
      <geom name="hoop_segment_12" type="capsule" fromto="2.185697 -0.517373 0.60 2.400000 -0.560000 0.60" size="0.022" rgba="0.20 0.83 0.49 1"/>
      <geom name="hoop_segment_13" type="capsule" fromto="2.400000 -0.560000 0.60 2.614303 -0.517373 0.60" size="0.022" rgba="0.20 0.83 0.49 1"/>
      <geom name="hoop_segment_14" type="capsule" fromto="2.614303 -0.517373 0.60 2.795980 -0.395980 0.60" size="0.022" rgba="0.20 0.83 0.49 1"/>
      <geom name="hoop_segment_15" type="capsule" fromto="2.795980 -0.395980 0.60 2.917373 -0.214303 0.60" size="0.022" rgba="0.20 0.83 0.49 1"/>
      <geom name="hoop_segment_16" type="capsule" fromto="2.917373 -0.214303 0.60 2.960000 0.000000 0.60" size="0.022" rgba="0.20 0.83 0.49 1"/>
      <geom name="hoop_post_left" type="cylinder" pos="2.4 -0.63 0.30" size="0.018 0.30" rgba="0.15 0.48 0.32 1"/>
      <geom name="hoop_post_right" type="cylinder" pos="2.4 0.63 0.30" size="0.018 0.30" rgba="0.15 0.48 0.32 1"/>
      <geom name="hoop_bracket_left" type="capsule" fromto="2.4 -0.63 0.60 2.4 -0.56 0.60" size="0.018" rgba="0.15 0.48 0.32 1"/>
      <geom name="hoop_bracket_right" type="capsule" fromto="2.4 0.63 0.60 2.4 0.56 0.60" size="0.018" rgba="0.15 0.48 0.32 1"/>
    </body>

    <body name="box">
      <geom name="box_bottom" type="box" pos="2.4 0 0.035" size="0.80 0.75 0.035" friction="0.8 0.01 0.025" condim="6" solref="0.012 1" rgba="0.32 0.48 0.66 1"/>
      <geom name="box_wall_back" type="box" pos="1.62 0 0.20" size="0.025 0.75 0.13" friction="0.8 0.01 0.025" condim="6" rgba="0.36 0.53 0.72 1"/>
      <geom name="box_wall_front" type="box" pos="3.18 0 0.20" size="0.025 0.75 0.13" friction="0.8 0.01 0.025" condim="6" rgba="0.36 0.53 0.72 1"/>
      <geom name="box_wall_left" type="box" pos="2.4 -0.725 0.20" size="0.755 0.025 0.13" friction="0.8 0.01 0.025" condim="6" rgba="0.36 0.53 0.72 1"/>
      <geom name="box_wall_right" type="box" pos="2.4 0.725 0.20" size="0.755 0.025 0.13" friction="0.8 0.01 0.025" condim="6" rgba="0.36 0.53 0.72 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.157368 -0.4 1.255752 1 0 0 0 0 0 1.955 0 1.0 1 0 0 0" qvel="0 0 0 0 0 0 0 0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```