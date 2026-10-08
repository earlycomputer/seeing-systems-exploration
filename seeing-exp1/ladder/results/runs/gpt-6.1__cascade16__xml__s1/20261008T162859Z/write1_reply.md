```xml
<mujoco model="passive_chain_candidate">
  <compiler angle="degree" autolimits="true" inertiafromgeom="auto"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="100" tolerance="1e-10"/>
  <size njmax="4000" nconmax="1000"/>
  <visual>
    <global azimuth="125" elevation="-18"/>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
  </visual>

  <!-- All initial generalized velocities are zero. -->
  <!-- solref damping ratio 0.69 approximates e=0.05 for a linearized impact. -->
  <!-- MuJoCo does not provide an exact, velocity-independent restitution attribute. -->
  <!-- Every contact geom explicitly specifies sliding friction 0.70. -->

  <worldbody>
    <light name="main_light" pos="3 -3 7" dir="0 0 -1" directional="true"/>
    <camera name="overview" pos="3.5 -8 4.5" xyaxes="1 0 0 0 0.45 0.893"/>
    <geom name="floor" type="plane" pos="0 0 0" size="12 4 0.1" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.24 0.27 0.30 1"/>

    <!-- Ramp top endpoints: (0,0,0.492020) and (0.939693,0,0.15). -->
    <body name="ramp1" pos="0.463006 0 0.302216" quat="0.984807753 0 0.173648178 0">
      <geom name="ramp1_surface" type="box" size="0.50 0.15 0.02" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.55 0.58 0.62 1"/>
    </body>
    <body name="ball1" pos="0.054689 0 0.525325">
      <freejoint name="ball1_free"/>
      <geom name="ball1_sphere" type="sphere" size="0.05" mass="0.20" condim="6" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.90 0.18 0.12 1"/>
    </body>

    <body name="domino1" pos="1.079693 0 0.12">
      <freejoint name="domino1_free"/>
      <geom name="domino1_box" type="box" size="0.04 0.02 0.12" mass="0.25" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.92 0.76 0.22 1"/>
    </body>
    <body name="domino2" pos="1.259693 0 0.12">
      <freejoint name="domino2_free"/>
      <geom name="domino2_box" type="box" size="0.04 0.02 0.12" mass="0.25" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.92 0.76 0.22 1"/>
    </body>

    <!-- Positive flap rotation moves the hanging panel toward +x. -->
    <body name="flap1" pos="1.439693 0 0.55">
      <joint name="flap1_hinge" type="hinge" axis="0 -1 0" range="0 65" damping="0.04" armature="0.0001" solreflimit="0.004 1" solimplimit="0.99 0.999 0.0001"/>
      <geom name="flap1_panel" type="box" pos="0 0 -0.20" size="0.02 0.10 0.20" mass="0.30" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.20 0.65 0.85 1"/>
    </body>
    <body name="cart1" pos="1.679693 0 0.50">
      <joint name="cart1_slide" type="slide" axis="1 0 0" range="0 0.75" damping="0.20" solreflimit="0.004 1"/>
      <geom name="cart1_chassis" type="box" size="0.11 0.09 0.05" mass="0.50" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.25 0.75 0.35 1"/>
    </body>

    <!-- Cart1's front reaches ball2 after 0.45 m of slide travel. -->
    <body name="ramp2" pos="2.698013 0 0.302216" quat="0.984807753 0 0.173648178 0">
      <geom name="ramp2_surface" type="box" size="0.50 0.15 0.02" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.55 0.58 0.62 1"/>
    </body>
    <body name="ball2" pos="2.289696 0 0.525325">
      <freejoint name="ball2_free"/>
      <geom name="ball2_sphere" type="sphere" size="0.05" mass="0.20" condim="6" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.95 0.40 0.12 1"/>
    </body>

    <!-- The lever starts inclined so the two falling stages remain above z=0. -->
    <!-- Positive rotation lowers its left side and initially raises its right side. -->
    <body name="lever1" pos="3.462020 0 0.459808" quat="0.866025404 0 -0.5 0">
      <joint name="lever1_hinge" type="hinge" axis="0 -1 0" range="0 45" damping="0.04" armature="0.0001" solreflimit="0.004 1" solimplimit="0.99 0.999 0.0001"/>
      <geom name="lever1_beam" type="box" size="0.30 0.05 0.02" mass="0.50" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.55 0.30 0.80 1"/>
    </body>
    <body name="ball3" pos="3.536399 0 0.728635">
      <freejoint name="ball3_free"/>
      <geom name="ball3_sphere" type="sphere" size="0.05" mass="0.20" condim="6" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.85 0.22 0.62 1"/>
    </body>

    <!-- The right guide starts at z=0.76, above the lever's initial highest corner. -->
    <body name="ball3_guide" pos="3.536399 0 1.03">
      <geom name="ball3_guide_left" type="box" pos="-0.066 0 0" size="0.008 0.074 0.35" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.60 0.70 0.80 0.35"/>
      <geom name="ball3_guide_right" type="box" pos="0.066 0 0.04" size="0.008 0.074 0.31" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.60 0.70 0.80 0.35"/>
      <geom name="ball3_guide_front" type="box" pos="0 -0.066 0" size="0.058 0.008 0.35" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.60 0.70 0.80 0.35"/>
      <geom name="ball3_guide_back" type="box" pos="0 0.066 0" size="0.058 0.008 0.35" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.60 0.70 0.80 0.35"/>
    </body>

    <!-- Capsule polygon with a 0.16 m inscribed clear diameter. -->
    <!-- Shifted 0.020 m toward +x to clear the inclined lever at reset. -->
    <body name="ring1" pos="3.556399 0 0.378635">
      <geom name="ring1_segment01" type="capsule" fromto="0.091763 0 0 0.084779 0.035115 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring1_segment02" type="capsule" fromto="0.084779 0.035115 0 0.064887 0.064887 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring1_segment03" type="capsule" fromto="0.064887 0.064887 0 0.035115 0.084779 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring1_segment04" type="capsule" fromto="0.035115 0.084779 0 0 0.091763 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring1_segment05" type="capsule" fromto="0 0.091763 0 -0.035115 0.084779 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring1_segment06" type="capsule" fromto="-0.035115 0.084779 0 -0.064887 0.064887 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring1_segment07" type="capsule" fromto="-0.064887 0.064887 0 -0.084779 0.035115 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring1_segment08" type="capsule" fromto="-0.084779 0.035115 0 -0.091763 0 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring1_segment09" type="capsule" fromto="-0.091763 0 0 -0.084779 -0.035115 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring1_segment10" type="capsule" fromto="-0.084779 -0.035115 0 -0.064887 -0.064887 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring1_segment11" type="capsule" fromto="-0.064887 -0.064887 0 -0.035115 -0.084779 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring1_segment12" type="capsule" fromto="-0.035115 -0.084779 0 0 -0.091763 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring1_segment13" type="capsule" fromto="0 -0.091763 0 0.035115 -0.084779 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring1_segment14" type="capsule" fromto="0.035115 -0.084779 0 0.064887 -0.064887 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring1_segment15" type="capsule" fromto="0.064887 -0.064887 0 0.084779 -0.035115 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring1_segment16" type="capsule" fromto="0.084779 -0.035115 0 0.091763 0 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
    </body>

    <!-- Offset bob makes the vertical ball impact produce a swinging impulse. -->
    <!-- The rigid rod and bob together have mass 0.35 kg. -->
    <body name="pendulum1" pos="3.596399 0 0.555345">
      <joint name="pendulum1_hinge" type="hinge" axis="0 -1 0" range="0 40" damping="0.04" armature="0.0001" solreflimit="0.004 1" solimplimit="0.99 0.999 0.0001"/>
      <geom name="pendulum1_rod" type="capsule" fromto="0 0 0 0 0 -0.50" size="0.008" mass="0.33" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.65 0.68 0.72 1"/>
      <geom name="pendulum1_bob" type="sphere" pos="0 0 -0.50" size="0.045" mass="0.02" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.20 0.50 0.85 1"/>
    </body>
    <body name="domino3" pos="3.980000 0 0.12">
      <freejoint name="domino3_free"/>
      <geom name="domino3_box" type="box" size="0.04 0.02 0.12" mass="0.25" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.92 0.76 0.22 1"/>
    </body>

    <!-- Upright, bottom-hinged door stores gravitational potential energy. -->
    <!-- Its explicit inertia represents a top-weighted 0.45 kg panel. -->
    <body name="door1" pos="4.160000 0 0.02">
      <inertial pos="0 0 0.35" mass="0.45" diaginertia="0.009 0.009 0.004"/>
      <joint name="door1_hinge" type="hinge" axis="0 1 0" range="0 70" damping="0.04" armature="0.0001" solreflimit="0.004 1" solimplimit="0.99 0.999 0.0001"/>
      <geom name="door1_panel" type="box" pos="0 0 0.21" size="0.02 0.16 0.21" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.70 0.35 0.18 1"/>
    </body>
    <body name="block1" pos="4.440000 0 0.06">
      <freejoint name="block1_free"/>
      <geom name="block1_cube" type="box" size="0.06 0.06 0.06" mass="0.35" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.75 0.40 0.70 1"/>
    </body>

    <!-- The chassis is 0.22 x 0.18 x 0.10 m; attachments share its 0.50 kg total mass. -->
    <!-- The slide supports the cart 1 mm above the floor. -->
    <body name="cart2" pos="4.960000 0 0.051">
      <joint name="cart2_slide" type="slide" axis="1 0 0" range="0 0.75" damping="0.20" solreflimit="0.004 1"/>
      <geom name="cart2_chassis" type="box" size="0.11 0.09 0.05" mass="0.485" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.25 0.75 0.35 1"/>
      <geom name="cart2_striker_post" type="box" pos="-0.04 0 0.25" size="0.012 0.025 0.225" mass="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.30 0.65 0.35 1"/>
      <geom name="cart2_striker_head" type="box" pos="0.035 0 0.484" size="0.075 0.03 0.02" mass="0.005" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.30 0.65 0.35 1"/>
    </body>

    <!-- Cart2's striker reaches ball4 after 0.42 m of travel. -->
    <body name="ramp3" pos="5.948316 0 0.302216" quat="0.984807753 0 0.173648178 0">
      <geom name="ramp3_surface" type="box" size="0.50 0.15 0.02" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.55 0.58 0.62 1"/>
    </body>
    <body name="ball4" pos="5.540000 0 0.525325">
      <freejoint name="ball4_free"/>
      <geom name="ball4_sphere" type="sphere" size="0.05" mass="0.20" condim="6" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.15 0.70 0.85 1"/>
    </body>

    <!-- Horizontal flap swings clockwise viewed from above. -->
    <!-- A low trigger arm bridges ramp-exit height to shelf height. -->
    <!-- Main panel and trigger attachments together have mass 0.28 kg. -->
    <body name="flap2" pos="6.525003 -0.20 0.84">
      <joint name="flap2_hinge" type="hinge" axis="0 0 -1" range="0 60" damping="0.04" armature="0.0001" solreflimit="0.004 1" solimplimit="0.99 0.999 0.0001"/>
      <geom name="flap2_panel" type="box" pos="0 0.19 0" size="0.09 0.19 0.02" mass="0.27" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.20 0.65 0.85 1"/>
      <geom name="flap2_trigger_post" type="capsule" fromto="0 0 -0.66 0 0 0" size="0.008" mass="0.005" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.30 0.55 0.70 1"/>
      <geom name="flap2_trigger_arm" type="capsule" fromto="0 0 -0.66 0 0.20 -0.66" size="0.01" mass="0.005" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.30 0.55 0.70 1"/>
    </body>

    <body name="shelf1" pos="6.570003 0 0.78">
      <geom name="shelf1_platform" type="box" size="0.15 0.125 0.02" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.60 0.45 0.30 1"/>
    </body>
    <body name="ball5" pos="6.715003 0 0.85">
      <freejoint name="ball5_free"/>
      <geom name="ball5_sphere" type="sphere" size="0.05" mass="0.20" condim="6" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.30 0.85 0.45 1"/>
    </body>

    <body name="ring2" pos="6.850003 -0.08 0.55">
      <geom name="ring2_segment01" type="capsule" fromto="0.091763 0 0 0.084779 0.035115 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring2_segment02" type="capsule" fromto="0.084779 0.035115 0 0.064887 0.064887 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring2_segment03" type="capsule" fromto="0.064887 0.064887 0 0.035115 0.084779 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring2_segment04" type="capsule" fromto="0.035115 0.084779 0 0 0.091763 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring2_segment05" type="capsule" fromto="0 0.091763 0 -0.035115 0.084779 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring2_segment06" type="capsule" fromto="-0.035115 0.084779 0 -0.064887 0.064887 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring2_segment07" type="capsule" fromto="-0.064887 0.064887 0 -0.084779 0.035115 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring2_segment08" type="capsule" fromto="-0.084779 0.035115 0 -0.091763 0 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring2_segment09" type="capsule" fromto="-0.091763 0 0 -0.084779 -0.035115 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring2_segment10" type="capsule" fromto="-0.084779 -0.035115 0 -0.064887 -0.064887 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring2_segment11" type="capsule" fromto="-0.064887 -0.064887 0 -0.035115 -0.084779 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring2_segment12" type="capsule" fromto="-0.035115 -0.084779 0 0 -0.091763 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring2_segment13" type="capsule" fromto="0 -0.091763 0 0.035115 -0.084779 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring2_segment14" type="capsule" fromto="0.035115 -0.084779 0 0.064887 -0.064887 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring2_segment15" type="capsule" fromto="0.064887 -0.064887 0 0.084779 -0.035115 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
      <geom name="ring2_segment16" type="capsule" fromto="0.084779 -0.035115 0 0.091763 0 0" size="0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.90 0.65 0.15 1"/>
    </body>

    <!-- Inner footprint 0.32 x 0.32 m; wall height 0.20 m; thickness 0.02 m. -->
    <!-- Bottom top is z=0.15, giving a resting ball center at z=0.20. -->
    <body name="bin1" pos="6.850003 -0.08 0.14">
      <geom name="bin1_bottom" type="box" size="0.18 0.18 0.01" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.30 0.45 0.65 1"/>
      <geom name="bin1_wall_left" type="box" pos="-0.17 0 0.11" size="0.01 0.18 0.10" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.30 0.45 0.65 1"/>
      <geom name="bin1_wall_right" type="box" pos="0.17 0 0.11" size="0.01 0.18 0.10" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.30 0.45 0.65 1"/>
      <geom name="bin1_wall_front" type="box" pos="0 -0.17 0.11" size="0.16 0.01 0.10" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.30 0.45 0.65 1"/>
      <geom name="bin1_wall_back" type="box" pos="0 0.17 0.11" size="0.16 0.01 0.10" friction="0.70 0.005 0.0001" solref="0.008 0.69" solimp="0.95 0.99 0.001" rgba="0.30 0.45 0.65 1"/>
      <geom name="bin1_leg01" type="cylinder" pos="-0.14 -0.14 -0.075" size="0.018 0.065" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.25 0.30 0.35 1"/>
      <geom name="bin1_leg02" type="cylinder" pos="-0.14 0.14 -0.075" size="0.018 0.065" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.25 0.30 0.35 1"/>
      <geom name="bin1_leg03" type="cylinder" pos="0.14 -0.14 -0.075" size="0.018 0.065" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.25 0.30 0.35 1"/>
      <geom name="bin1_leg04" type="cylinder" pos="0.14 0.14 -0.075" size="0.018 0.065" friction="0.70 0.005 0.0001" solref="0.008 0.69" rgba="0.25 0.30 0.35 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start"/>
  </keyframe>
</mujoco>
```