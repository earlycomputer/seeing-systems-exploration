```xml
<mujoco model="spring_assisted_chain">
  <compiler angle="degree" autolimits="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" cone="elliptic" solver="Newton" iterations="100" tolerance="1e-10"/>

  <visual>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.65 0.65 0.65" specular="0.15 0.15 0.15"/>
    <map znear="0.01" zfar="30"/>
  </visual>

  <!-- Passive, spring-assisted implementation; the full cascade is not simulation-verified. -->
  <!-- MuJoCo has compliant contacts rather than a direct restitution coefficient. -->
  <!-- solref damping ratio 0.7156 approximates restitution 0.04. -->
  <!-- All initial velocities are zero. Springs supply energy only after mechanical triggering. -->

  <worldbody>
    <light name="scene_light" pos="-1.5 -3 7" dir="0 0.3 -1" diffuse="0.8 0.8 0.8"/>
    <camera name="overview" pos="-1.8 -6 3.8" xyaxes="1 0 0 0 0.48 0.877268"/>
    <geom name="floor" type="plane" pos="0 0 0" size="10 5 0.1" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.24 0.27 0.30 1"/>

    <!-- Ball1 starts 0.30 m above ring1. Its initial lever-contact center is 0.25 m below ring1. -->
    <body name="ball1" pos="-0.285 -0.025 1.022020">
      <freejoint name="ball1_free"/>
      <geom name="ball1_sphere" type="sphere" size="0.05" mass="0.20" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.95 0.25 0.18 1"/>
    </body>

    <!-- Capsule centerlines form a polygon with an approximately 0.16 m clear diameter. -->
    <body name="ring1" pos="-0.285 -0.025 0.722020">
      <geom name="ring1_segment00" type="capsule" fromto="0.0917632 0 0 0.0847781 0.0351163 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring1_segment01" type="capsule" fromto="0.0847781 0.0351163 0 0.0648864 0.0648864 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring1_segment02" type="capsule" fromto="0.0648864 0.0648864 0 0.0351163 0.0847781 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring1_segment03" type="capsule" fromto="0.0351163 0.0847781 0 0 0.0917632 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring1_segment04" type="capsule" fromto="0 0.0917632 0 -0.0351163 0.0847781 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring1_segment05" type="capsule" fromto="-0.0351163 0.0847781 0 -0.0648864 0.0648864 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring1_segment06" type="capsule" fromto="-0.0648864 0.0648864 0 -0.0847781 0.0351163 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring1_segment07" type="capsule" fromto="-0.0847781 0.0351163 0 -0.0917632 0 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring1_segment08" type="capsule" fromto="-0.0917632 0 0 -0.0847781 -0.0351163 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring1_segment09" type="capsule" fromto="-0.0847781 -0.0351163 0 -0.0648864 -0.0648864 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring1_segment10" type="capsule" fromto="-0.0648864 -0.0648864 0 -0.0351163 -0.0847781 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring1_segment11" type="capsule" fromto="-0.0351163 -0.0847781 0 0 -0.0917632 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring1_segment12" type="capsule" fromto="0 -0.0917632 0 0.0351163 -0.0847781 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring1_segment13" type="capsule" fromto="0.0351163 -0.0847781 0 0.0648864 -0.0648864 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring1_segment14" type="capsule" fromto="0.0648864 -0.0648864 0 0.0847781 -0.0351163 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring1_segment15" type="capsule" fromto="0.0847781 -0.0351163 0 0.0917632 0 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
    </body>

    <body name="lever1" pos="0 0 0.402020">
      <joint name="lever1_hinge" type="hinge" axis="0 -1 0" damping="0.04" limited="true" range="0 45" solreflimit="0.004 1" solimplimit="0.99 0.999 0.0001"/>
      <geom name="lever1_beam" type="box" size="0.30 0.05 0.02" mass="0.50" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.20 0.55 0.85 1"/>
      <site name="lever1_spring_tip" pos="-0.25 -0.08 0" size="0.006" rgba="1 0.55 0.1 1"/>
    </body>

    <!-- Cart1's horizontal bearing supplies support without a rubbing track. -->
    <!-- Its leading face reaches domino1 after 0.42 m of travel. -->
    <body name="cart1" pos="0.37 0.125 0.542020">
      <joint name="cart1_slide" type="slide" axis="-1 0 0" damping="0.20" limited="true" range="0 0.46" solreflimit="0.004 1" solimplimit="0.99 0.999 0.0001"/>
      <geom name="cart1_box" type="box" size="0.11 0.09 0.05" mass="0.50" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.25 0.72 0.42 1"/>
    </body>

    <body name="domino1_plinth" pos="-0.20 0.125 0.246010">
      <geom name="domino1_plinth_box" type="box" size="0.08 0.04 0.246010" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.43 0.46 0.49 1"/>
    </body>

    <body name="domino1" pos="-0.20 0.125 0.612020">
      <freejoint name="domino1_free"/>
      <geom name="domino1_box" type="box" size="0.04 0.02 0.12" mass="0.25" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.88 0.83 0.68 1"/>
    </body>

    <!-- A level entry pad holds ball2 until domino1 strikes it. -->
    <!-- Initial surface gap from domino1 to ball2 is 0.18 m. -->
    <body name="ball2" pos="-0.47 0.125 0.542020">
      <freejoint name="ball2_free"/>
      <geom name="ball2_sphere" type="sphere" size="0.05" mass="0.20" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.95 0.40 0.15 1"/>
    </body>

    <!-- Ramp's sloping top is 1.00 m long and 0.30 m wide at 20 degrees. -->
    <!-- Low endpoint is approximately (-1.459693, 0.125, 0.15). -->
    <body name="ramp1" pos="-0.989846 0.125 0.321010">
      <geom name="ramp1_slope" type="box" pos="0.006840 0 -0.018794" quat="0.984807753 0 -0.173648178 0" size="0.50 0.15 0.02" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.48 0.55 0.63 1"/>
      <geom name="ramp1_entry_pad" type="box" pos="0.529846 0 0.161010" size="0.06 0.15 0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.48 0.55 0.63 1"/>
      <geom name="ramp1_rail_north" type="box" pos="-0.011971 0.158 0.032889" quat="0.984807753 0 -0.173648178 0" size="0.50 0.008 0.035" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.30 0.36 0.43 1"/>
      <geom name="ramp1_rail_south" type="box" pos="-0.011971 -0.158 0.032889" quat="0.984807753 0 -0.173648178 0" size="0.50 0.008 0.035" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.30 0.36 0.43 1"/>
    </body>

    <!-- Door's incoming face is 0.10 m beyond the low ramp endpoint. -->
    <!-- Door dimensions: 0.42 across y, 0.32 vertically, 0.04 thick. -->
    <body name="door1" pos="-1.579693 0.125 0.33">
      <joint name="door1_hinge" type="hinge" axis="0 1 0" damping="0.04" limited="true" range="0 70" solreflimit="0.004 1" solimplimit="0.99 0.999 0.0001"/>
      <geom name="door1_panel" type="box" size="0.02 0.21 0.16" mass="0.45" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.50 0.32 0.72 1"/>
      <site name="door1_spring_tip" pos="0 0.25 -0.14" size="0.006" rgba="1 0.55 0.1 1"/>
    </body>

    <body name="pendulum1" pos="-1.747 0.125 0.515">
      <joint name="pendulum1_hinge" type="hinge" axis="0 1 0" damping="0.04" limited="true" range="0 38" solreflimit="0.004 1" solimplimit="0.99 0.999 0.0001"/>
      <geom name="pendulum1_rod" type="capsule" fromto="0 0 -0.018 0 0 -0.482" size="0.018" mass="0.35" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.78 0.53 0.22 1"/>
      <site name="pendulum1_spring_tip" pos="0 0.055 -0.45" size="0.006" rgba="1 0.55 0.1 1"/>
    </body>

    <!-- A lightweight carriage prevents tumbling while allowing vertical settling onto the floor. -->
    <body name="block1_carriage" pos="-2.083 0.125 0.06">
      <inertial pos="0 0 0" mass="0.001" diaginertia="0.000001 0.000001 0.000001"/>
      <joint name="block1_carriage_slide" type="slide" axis="-1 0 0" damping="0.20"/>
      <joint name="block1_carriage_settle" type="slide" axis="0 0 1" damping="0.20" limited="true" range="-0.003 0.003"/>
    </body>

    <body name="block1" pos="-2.083 0.125 0.06">
      <freejoint name="block1_free"/>
      <geom name="block1_cube" type="box" size="0.06 0.06 0.06" mass="0.35" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.72 0.38 0.25 1"/>
    </body>

    <!-- Block1's leading face reaches cart2 after 0.35 m. -->
    <!-- Cart2 has a massless striker mast for the elevated seesaw. -->
    <!-- Its primary box is 0.22 by 0.18 by 0.10 m and its total mass is 0.50 kg. -->
    <body name="cart2" pos="-2.603 0.125 0.051">
      <joint name="cart2_slide" type="slide" axis="-1 0 0" damping="0.20" limited="true" range="0 0.47" solreflimit="0.004 1" solimplimit="0.99 0.999 0.0001"/>
      <geom name="cart2_box" type="box" size="0.11 0.09 0.05" mass="0.50" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.25 0.72 0.42 1"/>
      <geom name="cart2_striker_mast" type="box" pos="-0.12 0 0.57" size="0.01 0.025 0.57" mass="0" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.30 0.44 0.38 1"/>
      <geom name="cart2_striker_head" type="sphere" pos="-0.12 0 1.135" size="0.01" mass="0" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.30 0.44 0.38 1"/>
    </body>

    <!-- Seesaw's working left end is toward +x; its ball-carrying right end is toward -x. -->
    <!-- Cart2 reaches the left-end flange after 0.42 m of travel. -->
    <body name="seesaw1" pos="-3.478 0.125 1.20">
      <joint name="seesaw1_hinge" type="hinge" axis="0 1 0" damping="0.04" limited="true" range="0 42" solreflimit="0.004 1" solimplimit="0.99 0.999 0.0001"/>
      <geom name="seesaw1_beam" type="box" size="0.325 0.05 0.02" mass="0.55" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.20 0.55 0.85 1"/>
      <geom name="seesaw1_trigger_flange" type="box" pos="0.315 0 -0.065" size="0.01 0.05 0.045" mass="0" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.17 0.43 0.68 1"/>
      <site name="seesaw1_spring_tip" pos="0.28 0.08 0" size="0.006" rgba="1 0.55 0.1 1"/>
    </body>

    <body name="ball3" pos="-3.798 0.125 1.27">
      <freejoint name="ball3_free"/>
      <geom name="ball3_sphere" type="sphere" size="0.05" mass="0.20" contype="2" conaffinity="1" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.95 0.25 0.18 1"/>
    </body>

    <!-- These guides collide only with ball3, not with the seesaw. -->
    <!-- They constrain lateral launch motion and terminate above domino2. -->
    <body name="ball3_vertical_guide" pos="-3.798 0.125 3.36">
      <geom name="ball3_vertical_guide_east" type="box" pos="0.056 0 0" size="0.003 0.06 2.60" contype="4" conaffinity="2" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.60 0.78 0.85 0.18"/>
      <geom name="ball3_vertical_guide_west" type="box" pos="-0.056 0 0" size="0.003 0.06 2.60" contype="4" conaffinity="2" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.60 0.78 0.85 0.18"/>
      <geom name="ball3_vertical_guide_north" type="box" pos="0 0.056 0" size="0.06 0.003 2.60" contype="4" conaffinity="2" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.60 0.78 0.85 0.18"/>
      <geom name="ball3_vertical_guide_south" type="box" pos="0 -0.056 0" size="0.06 0.003 2.60" contype="4" conaffinity="2" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.60 0.78 0.85 0.18"/>
    </body>

    <!-- Ring2 is centered 0.32 m below ball3's initial center. -->
    <body name="ring2" pos="-3.798 0.125 0.95">
      <geom name="ring2_segment00" type="capsule" fromto="0.0917632 0 0 0.0847781 0.0351163 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring2_segment01" type="capsule" fromto="0.0847781 0.0351163 0 0.0648864 0.0648864 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring2_segment02" type="capsule" fromto="0.0648864 0.0648864 0 0.0351163 0.0847781 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring2_segment03" type="capsule" fromto="0.0351163 0.0847781 0 0 0.0917632 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring2_segment04" type="capsule" fromto="0 0.0917632 0 -0.0351163 0.0847781 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring2_segment05" type="capsule" fromto="-0.0351163 0.0847781 0 -0.0648864 0.0648864 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring2_segment06" type="capsule" fromto="-0.0648864 0.0648864 0 -0.0847781 0.0351163 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring2_segment07" type="capsule" fromto="-0.0847781 0.0351163 0 -0.0917632 0 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring2_segment08" type="capsule" fromto="-0.0917632 0 0 -0.0847781 -0.0351163 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring2_segment09" type="capsule" fromto="-0.0847781 -0.0351163 0 -0.0648864 -0.0648864 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring2_segment10" type="capsule" fromto="-0.0648864 -0.0648864 0 -0.0351163 -0.0847781 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring2_segment11" type="capsule" fromto="-0.0351163 -0.0847781 0 0 -0.0917632 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring2_segment12" type="capsule" fromto="0 -0.0917632 0 0.0351163 -0.0847781 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring2_segment13" type="capsule" fromto="0.0351163 -0.0847781 0 0.0648864 -0.0648864 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring2_segment14" type="capsule" fromto="0.0648864 -0.0648864 0 0.0847781 -0.0351163 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
      <geom name="ring2_segment15" type="capsule" fromto="0.0847781 -0.0351163 0 0.0917632 0 0" size="0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.85 0.72 0.22 1"/>
    </body>

    <body name="domino2_plinth" pos="-3.766 0.125 0.21">
      <geom name="domino2_plinth_box" type="box" size="0.06 0.04 0.21" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.43 0.46 0.49 1"/>
    </body>

    <!-- Domino2 top is at z=0.66: descending ball contact center is z=0.71. -->
    <!-- Thus ball3 descends another 0.24 m after ring2 before contact. -->
    <!-- Ball3 strikes toward the domino's -x edge to initiate toppling. -->
    <body name="domino2" pos="-3.766 0.125 0.54">
      <freejoint name="domino2_free"/>
      <geom name="domino2_box" type="box" size="0.04 0.02 0.12" mass="0.25" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.88 0.83 0.68 1"/>
    </body>

    <!-- Initial surface gap between domino2 and flap1 is 0.18 m. -->
    <!-- Flap dimensions: 0.38 vertically, 0.18 across y, 0.04 thick. -->
    <body name="flap1" pos="-4.006 0.125 0.76">
      <joint name="flap1_hinge" type="hinge" axis="0 1 0" damping="0.04" limited="true" range="0 60" solreflimit="0.004 1" solimplimit="0.99 0.999 0.0001"/>
      <geom name="flap1_panel" type="box" size="0.02 0.09 0.19" mass="0.28" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.50 0.32 0.72 1"/>
      <site name="flap1_spring_tip" pos="0 -0.12 -0.16" size="0.006" rgba="1 0.55 0.1 1"/>
    </body>

    <!-- Shelf is offset sideways so it does not obstruct domino2. -->
    <!-- Shelf top is 0.55 m above the cup's inner bottom. -->
    <body name="shelf1" pos="-4.075 0.30 0.55">
      <geom name="shelf1_box" type="box" size="0.15 0.125 0.02" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.48 0.55 0.63 1"/>
    </body>

    <body name="ball4" pos="-4.195 0.205 0.62">
      <freejoint name="ball4_free"/>
      <geom name="ball4_sphere" type="sphere" size="0.05" mass="0.20" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.95 0.25 0.18 1"/>
    </body>

    <!-- Separate catch chute dissipates horizontal motion before the final drop. -->
    <!-- Its upper incoming side is open toward +x. -->
    <body name="catch_chute" pos="-4.42 0.205 0">
      <geom name="catch_chute_west" type="box" pos="-0.155 0 0.66" size="0.005 0.15 0.44" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.55 0.72 0.78 0.28"/>
      <geom name="catch_chute_north" type="box" pos="0 0.155 0.66" size="0.16 0.005 0.44" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.55 0.72 0.78 0.28"/>
      <geom name="catch_chute_south" type="box" pos="0 -0.155 0.66" size="0.16 0.005 0.44" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.55 0.72 0.78 0.28"/>
      <geom name="catch_chute_east_lower" type="box" pos="0.155 0 0.31" size="0.005 0.15 0.09" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.55 0.72 0.78 0.28"/>
    </body>

    <!-- Cup has a 0.30 by 0.30 m inner footprint. -->
    <!-- Its walls are 0.20 m high above the inner bottom and 0.02 m thick. -->
    <body name="cup1" pos="-4.42 0.205 0">
      <geom name="cup1_bottom" type="box" pos="0 0 0.01" size="0.17 0.17 0.01" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.20 0.58 0.66 1"/>
      <geom name="cup1_wall_west" type="box" pos="-0.16 0 0.12" size="0.01 0.17 0.10" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.20 0.58 0.66 1"/>
      <geom name="cup1_wall_east" type="box" pos="0.16 0 0.12" size="0.01 0.17 0.10" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.20 0.58 0.66 1"/>
      <geom name="cup1_wall_north" type="box" pos="0 0.16 0.12" size="0.15 0.01 0.10" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.20 0.58 0.66 1"/>
      <geom name="cup1_wall_south" type="box" pos="0 -0.16 0.12" size="0.15 0.01 0.10" friction="0.72 0.005 0.0001" condim="6" solref="0.004 0.7156" rgba="0.20 0.58 0.66 1"/>
    </body>

    <!-- Fixed spring anchors lie opposite the moving attachments across each hinge. -->
    <!-- At initial alignment, spring forces produce zero hinge torque. -->
    <body name="spring_frame" pos="0 0 0">
      <site name="lever1_spring_anchor" pos="0.25 -0.08 0.402020" size="0.008" rgba="1 0.55 0.1 1"/>
      <site name="door1_spring_anchor" pos="-1.579693 0.375 0.47" size="0.008" rgba="1 0.55 0.1 1"/>
      <site name="pendulum1_spring_anchor" pos="-1.747 0.18 0.965" size="0.008" rgba="1 0.55 0.1 1"/>
      <site name="seesaw1_spring_anchor" pos="-3.758 0.205 1.20" size="0.008" rgba="1 0.55 0.1 1"/>
      <site name="flap1_spring_anchor" pos="-4.006 0.005 0.92" size="0.008" rgba="1 0.55 0.1 1"/>
    </body>
  </worldbody>

  <tendon>
    <spatial name="lever1_overcenter_spring" stiffness="250" damping="0" springlength="0.10" width="0.002" rgba="1 0.55 0.1 1">
      <site site="lever1_spring_anchor"/>
      <site site="lever1_spring_tip"/>
    </spatial>
    <spatial name="door1_overcenter_spring" stiffness="500" damping="0" springlength="0.08" width="0.002" rgba="1 0.55 0.1 1">
      <site site="door1_spring_anchor"/>
      <site site="door1_spring_tip"/>
    </spatial>
    <spatial name="pendulum1_overcenter_spring" stiffness="1600" damping="0" springlength="0.50" width="0.002" rgba="1 0.55 0.1 1">
      <site site="pendulum1_spring_anchor"/>
      <site site="pendulum1_spring_tip"/>
    </spatial>
    <spatial name="seesaw1_overcenter_spring" stiffness="450" damping="0" springlength="0.06" width="0.002" rgba="1 0.55 0.1 1">
      <site site="seesaw1_spring_anchor"/>
      <site site="seesaw1_spring_tip"/>
    </spatial>
    <spatial name="flap1_overcenter_spring" stiffness="40" damping="0" springlength="0.08" width="0.002" rgba="1 0.55 0.1 1">
      <site site="flap1_spring_anchor"/>
      <site site="flap1_spring_tip"/>
    </spatial>
  </tendon>

  <equality>
    <weld name="block1_linear_guide" body1="block1" body2="block1_carriage" solref="0.004 1" solimp="0.99 0.999 0.0001"/>
  </equality>

  <!-- Omitted key qpos uses the model's initial pose; omitted qvel is identically zero. -->
  <keyframe>
    <key name="start" time="0"/>
  </keyframe>
</mujoco>
```