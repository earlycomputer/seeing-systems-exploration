```xml
<mujoco model="ball_paddle_slider_drop">
  <compiler angle="radian" autolimits="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" iterations="80"/>
  <size njmax="1500" nconmax="300"/>
  <visual>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.75 0.75 0.75" specular="0.15 0.15 0.15"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="0 -2 5" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <camera name="overview" pos="4 -6 3.8" xyaxes="0.857 0.514 0 -0.220 0.366 0.904"/>

    <geom name="floor" type="plane" size="8 5 0.1" friction="1.0 0.02 0.08" condim="6" priority="1" solref="0.012 1" rgba="0.24 0.27 0.30 1"/>

    <!-- The ball's starting contact point is one metre uphill from the ramp's lower end. -->
    <body name="ramp" pos="-0.593292 0 1.681763" quat="0.987688341 0 0.156434465 0">
      <geom name="ramp_surface" type="box" pos="0 0 -0.06" size="0.75 0.23 0.06" friction="0.7 0.005 0.0002" condim="6" priority="2" solref="0.01 1" rgba="0.50 0.55 0.60 1"/>
      <geom name="ramp_rail_left" type="box" pos="0 0.25 0.075" size="0.75 0.022 0.075" friction="0.4 0.005 0.0002" condim="6" priority="2" rgba="0.34 0.39 0.44 1"/>
      <geom name="ramp_rail_right" type="box" pos="0 -0.25 0.075" size="0.75 0.022 0.075" friction="0.4 0.005 0.0002" condim="6" priority="2" rgba="0.34 0.39 0.44 1"/>
    </body>

    <body name="ball" pos="-0.793975 0 1.873144">
      <freejoint name="ball_free"/>
      <geom name="ball_geom" type="sphere" size="0.12" mass="3" friction="0.7 0.015 0.06" condim="6" solref="0.01 1" rgba="0.95 0.30 0.12 1"/>
    </body>

    <body name="paddle_support" pos="0.24 -0.5 0.75">
      <geom name="paddle_support_post" type="cylinder" size="0.045 0.75" contype="0" conaffinity="0" rgba="0.30 0.33 0.37 1"/>
      <geom name="paddle_support_base" type="box" pos="0 0 -0.70" size="0.14 0.14 0.05" contype="0" conaffinity="0" rgba="0.30 0.33 0.37 1"/>
    </body>

    <body name="paddle" pos="0.24 -0.5 1.60">
      <joint name="paddle_hinge" type="hinge" axis="0 0 1" range="-1.42 0.02" damping="0.06" frictionloss="0.01" armature="0.002"/>
      <geom name="paddle_blade" type="box" pos="0 0.525 0" size="0.035 0.525 0.135" mass="0.8" friction="0.3 0.005 0.001" condim="6" priority="1" solref="0.008 1" rgba="0.95 0.72 0.16 1"/>
    </body>

    <body name="slider_guide" pos="0.82 -0.05 1.43">
      <geom name="slider_guide_left" type="box" pos="0 0.22 0" size="0.52 0.025 0.025" contype="0" conaffinity="0" rgba="0.30 0.35 0.40 1"/>
      <geom name="slider_guide_right" type="box" pos="0 -0.22 0" size="0.52 0.025 0.025" contype="0" conaffinity="0" rgba="0.30 0.35 0.40 1"/>
    </body>

    <body name="slider" pos="0.50 -0.05 1.58">
      <joint name="slider_slide" type="slide" axis="1 0 0" range="0 0.65" damping="1.2" frictionloss="0.015" armature="0.01"/>
      <geom name="slider_striker" type="box" size="0.10 0.15 0.10" mass="0.30" friction="0.25 0.005 0.001" condim="6" solref="0.008 1" rgba="0.20 0.65 0.90 1"/>
    </body>

    <body name="ledge" pos="0.85 -0.05 0">
      <geom name="ledge_platform" type="box" pos="0 0 1.405" size="0.22 0.24 0.045" friction="0.18 0.005 0.001" condim="6" priority="1" solref="0.01 1" rgba="0.57 0.45 0.32 1"/>
      <geom name="ledge_pedestal" type="box" pos="0 0 0.68" size="0.11 0.13 0.68" friction="0.6 0.01 0.02" rgba="0.42 0.34 0.27 1"/>
    </body>

    <body name="block" pos="0.93 -0.05 1.55">
      <freejoint name="block_free"/>
      <geom name="block_geom" type="box" size="0.10 0.10 0.10" mass="0.18" friction="0.6 0.02 0.02" condim="6" solref="0.008 1" rgba="0.65 0.25 0.82 1"/>
    </body>

    <!-- A horizontal hoop assembled entirely from primitive capsules. -->
    <body name="hoop" pos="1.60 -0.05 0.90">
      <geom name="hoop_ring_01" type="capsule" fromto="0.720000 0 0 0.665193 0.275532 0" size="0.027" rgba="0.15 0.80 0.45 1"/>
      <geom name="hoop_ring_02" type="capsule" fromto="0.665193 0.275532 0 0.509117 0.509117 0" size="0.027" rgba="0.15 0.80 0.45 1"/>
      <geom name="hoop_ring_03" type="capsule" fromto="0.509117 0.509117 0 0.275532 0.665193 0" size="0.027" rgba="0.15 0.80 0.45 1"/>
      <geom name="hoop_ring_04" type="capsule" fromto="0.275532 0.665193 0 0 0.720000 0" size="0.027" rgba="0.15 0.80 0.45 1"/>
      <geom name="hoop_ring_05" type="capsule" fromto="0 0.720000 0 -0.275532 0.665193 0" size="0.027" rgba="0.15 0.80 0.45 1"/>
      <geom name="hoop_ring_06" type="capsule" fromto="-0.275532 0.665193 0 -0.509117 0.509117 0" size="0.027" rgba="0.15 0.80 0.45 1"/>
      <geom name="hoop_ring_07" type="capsule" fromto="-0.509117 0.509117 0 -0.665193 0.275532 0" size="0.027" rgba="0.15 0.80 0.45 1"/>
      <geom name="hoop_ring_08" type="capsule" fromto="-0.665193 0.275532 0 -0.720000 0 0" size="0.027" rgba="0.15 0.80 0.45 1"/>
      <geom name="hoop_ring_09" type="capsule" fromto="-0.720000 0 0 -0.665193 -0.275532 0" size="0.027" rgba="0.15 0.80 0.45 1"/>
      <geom name="hoop_ring_10" type="capsule" fromto="-0.665193 -0.275532 0 -0.509117 -0.509117 0" size="0.027" rgba="0.15 0.80 0.45 1"/>
      <geom name="hoop_ring_11" type="capsule" fromto="-0.509117 -0.509117 0 -0.275532 -0.665193 0" size="0.027" rgba="0.15 0.80 0.45 1"/>
      <geom name="hoop_ring_12" type="capsule" fromto="-0.275532 -0.665193 0 0 -0.720000 0" size="0.027" rgba="0.15 0.80 0.45 1"/>
      <geom name="hoop_ring_13" type="capsule" fromto="0 -0.720000 0 0.275532 -0.665193 0" size="0.027" rgba="0.15 0.80 0.45 1"/>
      <geom name="hoop_ring_14" type="capsule" fromto="0.275532 -0.665193 0 0.509117 -0.509117 0" size="0.027" rgba="0.15 0.80 0.45 1"/>
      <geom name="hoop_ring_15" type="capsule" fromto="0.509117 -0.509117 0 0.665193 -0.275532 0" size="0.027" rgba="0.15 0.80 0.45 1"/>
      <geom name="hoop_ring_16" type="capsule" fromto="0.665193 -0.275532 0 0.720000 0 0" size="0.027" rgba="0.15 0.80 0.45 1"/>
      <geom name="hoop_support_left" type="capsule" fromto="0 0.72 -0.82 0 0.72 0" size="0.022" rgba="0.12 0.48 0.30 1"/>
      <geom name="hoop_support_right" type="capsule" fromto="0 -0.72 -0.82 0 -0.72 0" size="0.022" rgba="0.12 0.48 0.30 1"/>
    </body>

    <body name="box" pos="1.65 -0.05 0">
      <geom name="box_bottom" type="box" pos="0 0 0.04" size="1.10 0.85 0.04" friction="1.2 0.03 0.08" condim="6" priority="1" solref="0.008 1" rgba="0.24 0.43 0.65 1"/>
      <geom name="box_wall_low_x" type="box" pos="-1.10 0 0.30" size="0.04 0.85 0.22" friction="0.9 0.02 0.04" condim="6" priority="1" solref="0.008 1" rgba="0.30 0.50 0.73 1"/>
      <geom name="box_wall_high_x" type="box" pos="1.10 0 0.30" size="0.04 0.85 0.22" friction="0.9 0.02 0.04" condim="6" priority="1" solref="0.008 1" rgba="0.30 0.50 0.73 1"/>
      <geom name="box_wall_low_y" type="box" pos="0 -0.85 0.30" size="1.14 0.04 0.22" friction="0.9 0.02 0.04" condim="6" priority="1" solref="0.008 1" rgba="0.30 0.50 0.73 1"/>
      <geom name="box_wall_high_y" type="box" pos="0 0.85 0.30" size="1.14 0.04 0.22" friction="0.9 0.02 0.04" condim="6" priority="1" solref="0.008 1" rgba="0.30 0.50 0.73 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-0.793975 0 1.873144 1 0 0 0 0 0 0.93 -0.05 1.55 1 0 0 0"/>
  </keyframe>
</mujoco>
```