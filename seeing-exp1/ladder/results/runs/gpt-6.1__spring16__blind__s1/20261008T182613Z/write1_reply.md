```xml
<mujoco model="five_ball_mechanical_cascade">
  <compiler angle="degree" autolimits="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="100" tolerance="1e-10" cone="elliptic"/>
  <size njmax="3000" nconmax="1000"/>

  <!--
    Unvalidated mechanical layout.
    All bodies start with zero velocity.
    Sliding contact friction is 0.68.
    Contact damping ratio 0.69 approximates restitution 0.05.
    Small rolling resistance helps the balls settle.
    Auxiliary passive catchers guide ball2 and ball4 through their rings.
    A constant 2.25 N, sub-static-friction motor assists block1 after impact.
    Cart1 uses a compression-only axial tendon spring, initially compressed 0.20 m.
  -->

  <worldbody>
    <light name="overhead_light" pos="1 0 6" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="12 12 0.1" friction="0.68 0.001 0.0005" solref="0.006 0.69" solimp="0.95 0.99 0.001" rgba="0.24 0.27 0.30 1"/>

    <!-- Cart1 touches ball1 at slide displacement 0.50 m. -->
    <body name="cart1" pos="-0.06 0 0.542020">
      <inertial pos="0 0 0" mass="0.50" diaginertia="0.001766667 0.002433333 0.003366667"/>
      <joint name="cart1_slide" type="slide" axis="1 0 0" damping="0.20" range="0 0.56" solreflimit="0.004 1"/>
      <geom name="cart1_chassis" type="box" size="0.11 0.09 0.05" mass="0" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.80 0.20 0.12 1"/>
    </body>

    <body name="ball1" pos="0.60 0 0.542020">
      <freejoint name="ball1_free"/>
      <geom name="ball1_sphere" type="sphere" size="0.05" mass="0.20" condim="6" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.96 0.67 0.12 1"/>
    </body>

    <!-- Ramp1 top endpoints: (0.65, 0, 0.492020), (1.589693, 0, 0.15). -->
    <body name="ramp1" pos="1.114716 0 0.306915">
      <geom name="ramp1_incline" type="box" quat="0.984807753 0 0.173648178 0" size="0.50 0.15 0.015" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.40 0.58 0.68 1"/>
      <geom name="ramp1_start_perch" type="box" pos="-0.594716 0 0.165105" size="0.13 0.15 0.02" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.40 0.58 0.68 1"/>
    </body>

    <!-- Horizontal rigid pendulum, clockwise about its downward vertical axis. -->
    <body name="pendulum1" pos="1.739693 -0.50 0.18">
      <joint name="pendulum1_hinge" type="hinge" axis="0 0 -1" damping="0.04" range="0 85" solreflimit="0.004 1"/>
      <geom name="pendulum1_rod" type="capsule" fromto="0 0 0 0 0.50 0" size="0.009" mass="0.035" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.75 0.76 0.79 1"/>
      <geom name="pendulum1_bob" type="sphere" pos="0 0.50 0" size="0.05" mass="0.315" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.70 0.24 0.65 1"/>
    </body>

    <!-- Tilted hinge provides a gravity-assisted clockwise door swing. -->
    <body name="door1" pos="2.131086 -0.536978 0.32">
      <inertial pos="0 0.38 0" mass="0.45" diaginertia="0.0040 0.00384 0.00030"/>
      <joint name="door1_hinge" type="hinge" axis="0 0.4 -0.916515139" damping="0.04" range="0 70" solreflimit="0.003 1"/>
      <geom name="door1_panel" type="box" pos="0 0.21 0" size="0.02 0.21 0.16" mass="0" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.25 0.65 0.37 1"/>
    </body>

    <body name="block1" pos="2.46916 -0.38833 0.06" quat="0.827380 0 0 -0.561642">
      <freejoint name="block1_free"/>
      <geom name="block1_cube" type="box" size="0.06 0.06 0.06" mass="0.35" friction="0.68 0.001 0.0005" solref="0.006 0.69" solimp="0.95 0.99 0.001" rgba="0.88 0.49 0.15 1"/>
    </body>

    <!-- Thin dimension follows the block's nominal travel direction. -->
    <body name="domino1" pos="2.61681 -0.76008 0.12" quat="0.827380 0 0 -0.561642">
      <freejoint name="domino1_free"/>
      <geom name="domino1_tile" type="box" size="0.02 0.04 0.12" mass="0.25" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.91 0.89 0.75 1"/>
    </body>

    <!-- Initially steeply inclined lever with a level launch pad. -->
    <body name="lever1" pos="2.70249 -0.97580 0.475442" quat="0.633825 -0.361023 -0.531842 -0.430253">
      <inertial pos="0 0 0" mass="0.50" diaginertia="0.000483333 0.015066667 0.015416667"/>
      <joint name="lever1_hinge" type="hinge" axis="0 -1 0" damping="0.04" range="0 45" solreflimit="0.003 1"/>
      <geom name="lever1_beam" type="box" size="0.30 0.05 0.02" mass="0" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.20 0.55 0.78 1"/>
      <geom name="lever1_launch_pad" type="box" pos="0.309848 0 0.001736" quat="0.766044443 0 0.642787610 0" size="0.06 0.05 0.01" mass="0" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.18 0.45 0.67 1"/>
    </body>

    <body name="ball2" pos="2.72172 -1.02422 0.840884">
      <freejoint name="ball2_free"/>
      <geom name="ball2_sphere" type="sphere" size="0.05" mass="0.20" contype="3" conaffinity="3" condim="6" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.98 0.77 0.16 1"/>
    </body>

    <!-- Collision bit 2 selects ball2's passive catcher and ring. -->
    <body name="ball2_catcher" pos="2.815 -0.718 0.515884">
      <geom name="ball2_catcher_positive_x" type="box" pos="0.32 0 0.25" quat="0.923879533 0 -0.382683432 0" size="0.353553391 0.57 0.008" contype="2" conaffinity="2" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.45 0.64 0.72 0.35"/>
      <geom name="ball2_catcher_negative_x" type="box" pos="-0.32 0 0.25" quat="0.923879533 0 0.382683432 0" size="0.353553391 0.57 0.008" contype="2" conaffinity="2" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.45 0.64 0.72 0.35"/>
      <geom name="ball2_catcher_positive_y" type="box" pos="0 0.32 0.25" quat="0.923879533 0.382683432 0 0" size="0.57 0.353553391 0.008" contype="2" conaffinity="2" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.45 0.64 0.72 0.35"/>
      <geom name="ball2_catcher_negative_y" type="box" pos="0 -0.32 0.25" quat="0.923879533 -0.382683432 0 0" size="0.57 0.353553391 0.008" contype="2" conaffinity="2" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.45 0.64 0.72 0.35"/>
    </body>

    <!-- Octagonal capsule ring: minimum clear diameter approximately 0.160 m. -->
    <body name="ring1" pos="2.815 -0.718 0.520884">
      <geom name="ring1_segment0" type="capsule" fromto="0.0952505 0 0 0.0673522 0.0673522 0" size="0.008" contype="2" conaffinity="2" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.95 0.79 0.21 1"/>
      <geom name="ring1_segment1" type="capsule" fromto="0.0673522 0.0673522 0 0 0.0952505 0" size="0.008" contype="2" conaffinity="2" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.95 0.79 0.21 1"/>
      <geom name="ring1_segment2" type="capsule" fromto="0 0.0952505 0 -0.0673522 0.0673522 0" size="0.008" contype="2" conaffinity="2" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.95 0.79 0.21 1"/>
      <geom name="ring1_segment3" type="capsule" fromto="-0.0673522 0.0673522 0 -0.0952505 0 0" size="0.008" contype="2" conaffinity="2" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.95 0.79 0.21 1"/>
      <geom name="ring1_segment4" type="capsule" fromto="-0.0952505 0 0 -0.0673522 -0.0673522 0" size="0.008" contype="2" conaffinity="2" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.95 0.79 0.21 1"/>
      <geom name="ring1_segment5" type="capsule" fromto="-0.0673522 -0.0673522 0 0 -0.0952505 0" size="0.008" contype="2" conaffinity="2" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.95 0.79 0.21 1"/>
      <geom name="ring1_segment6" type="capsule" fromto="0 -0.0952505 0 0.0673522 -0.0673522 0" size="0.008" contype="2" conaffinity="2" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.95 0.79 0.21 1"/>
      <geom name="ring1_segment7" type="capsule" fromto="0.0673522 -0.0673522 0 0.0952505 0 0" size="0.008" contype="2" conaffinity="2" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.95 0.79 0.21 1"/>
    </body>

    <!-- Tilted chassis converts downward impact into positive-y slide motion. -->
    <body name="cart2" pos="2.815 -0.668 0.184281">
      <inertial pos="0 0 0" mass="0.50" diaginertia="0.002433333 0.001766667 0.003366667"/>
      <joint name="cart2_slide" type="slide" axis="0 1 0" damping="0.20" range="0 0.44" solreflimit="0.004 1"/>
      <geom name="cart2_chassis" type="box" quat="0.965925826 0.258819045 0 0" size="0.09 0.11 0.05" mass="0" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.82 0.26 0.16 1"/>
      <geom name="cart2_striker" type="capsule" fromto="0 0.10 0 0 0.10 0.27" size="0.012" mass="0" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.75 0.77 0.80 1"/>
    </body>

    <body name="domino2_platform" pos="2.815 -0.136 0.165">
      <geom name="domino2_platform_top" type="box" size="0.08 0.065 0.165" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.31 0.35 0.39 1"/>
    </body>

    <body name="domino2" pos="2.815 -0.136 0.45">
      <freejoint name="domino2_free"/>
      <geom name="domino2_tile" type="box" size="0.04 0.02 0.12" mass="0.25" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.91 0.89 0.75 1"/>
    </body>

    <body name="ball3" pos="2.815 0.044 0.542020">
      <freejoint name="ball3_free"/>
      <geom name="ball3_sphere" type="sphere" size="0.05" mass="0.20" condim="6" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.96 0.65 0.13 1"/>
    </body>

    <!-- Ramp2 top endpoints: (2.815, 0.094, 0.492020), (2.815, 1.033693, 0.15). -->
    <body name="ramp2" pos="2.815 0.558716 0.306915">
      <geom name="ramp2_incline" type="box" quat="0.984807753 -0.173648178 0 0" size="0.15 0.50 0.015" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.40 0.58 0.68 1"/>
      <geom name="ramp2_start_perch" type="box" pos="0 -0.509716 0.165105" size="0.15 0.045 0.02" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.40 0.58 0.68 1"/>
    </body>

    <!-- Upright flap is gravity-neutral at reset and tips forward after impact. -->
    <body name="flap1" pos="2.815 1.153693 0.18">
      <inertial pos="0 0 0.19" mass="0.28" diaginertia="0.003406667 0.004126667 0.000793333"/>
      <joint name="flap1_hinge" type="hinge" axis="-1 0 0" damping="0.04" range="0 60" solreflimit="0.003 1"/>
      <geom name="flap1_panel" type="box" pos="0 0 0.19" size="0.09 0.02 0.19" mass="0" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.24 0.68 0.43 1"/>
      <geom name="flap1_striker" type="capsule" fromto="0 0 0.35 0 0 0.60" size="0.015" mass="0" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.75 0.77 0.80 1"/>
    </body>

    <!-- Inverted rigid pendulum; gravity assists once displaced by flap1. -->
    <body name="pendulum2" pos="2.815 1.700308 0.43">
      <joint name="pendulum2_hinge" type="hinge" axis="-1 0 0" damping="0.04" range="0 38" solreflimit="0.003 1"/>
      <geom name="pendulum2_rod" type="capsule" fromto="0 0 0 0 0 0.50" size="0.012" mass="0.04" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.75 0.76 0.79 1"/>
      <geom name="pendulum2_bob" type="sphere" pos="0 0 0.50" size="0.05" mass="0.31" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.70 0.24 0.65 1"/>
    </body>

    <!-- Shelf top is at z = 0.85 m. -->
    <body name="shelf1" pos="2.815 1.963137 0.83">
      <geom name="shelf1_board" type="box" size="0.15 0.125 0.02" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.55 0.40 0.27 1"/>
    </body>

    <body name="ball4" pos="2.815 2.073137 0.90">
      <freejoint name="ball4_free"/>
      <geom name="ball4_sphere" type="sphere" size="0.05" mass="0.20" contype="5" conaffinity="5" condim="6" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.96 0.68 0.14 1"/>
    </body>

    <!-- Collision bit 4 selects ball4's passive catcher and ring. -->
    <body name="ball4_catcher" pos="2.815 2.20 0.63">
      <geom name="ball4_catcher_positive_x" type="box" pos="0.16 0 0.09" quat="0.923879533 0 -0.382683432 0" size="0.127279221 0.25 0.008" contype="4" conaffinity="4" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.45 0.64 0.72 0.35"/>
      <geom name="ball4_catcher_negative_x" type="box" pos="-0.16 0 0.09" quat="0.923879533 0 0.382683432 0" size="0.127279221 0.25 0.008" contype="4" conaffinity="4" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.45 0.64 0.72 0.35"/>
      <geom name="ball4_catcher_positive_y" type="box" pos="0 0.16 0.09" quat="0.923879533 0.382683432 0 0" size="0.25 0.127279221 0.008" contype="4" conaffinity="4" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.45 0.64 0.72 0.35"/>
      <geom name="ball4_catcher_negative_y" type="box" pos="0 -0.16 0.09" quat="0.923879533 -0.382683432 0 0" size="0.25 0.127279221 0.008" contype="4" conaffinity="4" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.45 0.64 0.72 0.35"/>
    </body>

    <body name="ring2" pos="2.815 2.20 0.60">
      <geom name="ring2_segment0" type="capsule" fromto="0.0952505 0 0 0.0673522 0.0673522 0" size="0.008" contype="4" conaffinity="4" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.95 0.79 0.21 1"/>
      <geom name="ring2_segment1" type="capsule" fromto="0.0673522 0.0673522 0 0 0.0952505 0" size="0.008" contype="4" conaffinity="4" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.95 0.79 0.21 1"/>
      <geom name="ring2_segment2" type="capsule" fromto="0 0.0952505 0 -0.0673522 0.0673522 0" size="0.008" contype="4" conaffinity="4" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.95 0.79 0.21 1"/>
      <geom name="ring2_segment3" type="capsule" fromto="-0.0673522 0.0673522 0 -0.0952505 0 0" size="0.008" contype="4" conaffinity="4" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.95 0.79 0.21 1"/>
      <geom name="ring2_segment4" type="capsule" fromto="-0.0952505 0 0 -0.0673522 -0.0673522 0" size="0.008" contype="4" conaffinity="4" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.95 0.79 0.21 1"/>
      <geom name="ring2_segment5" type="capsule" fromto="-0.0673522 -0.0673522 0 0 -0.0952505 0" size="0.008" contype="4" conaffinity="4" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.95 0.79 0.21 1"/>
      <geom name="ring2_segment6" type="capsule" fromto="0 -0.0952505 0 0.0673522 -0.0673522 0" size="0.008" contype="4" conaffinity="4" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.95 0.79 0.21 1"/>
      <geom name="ring2_segment7" type="capsule" fromto="0.0673522 -0.0673522 0 0.0952505 0 0" size="0.008" contype="4" conaffinity="4" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.95 0.79 0.21 1"/>
    </body>

    <!-- Left contact center is z = 0.35, 0.25 m below ring2. -->
    <body name="seesaw1" pos="2.815 2.525 0.28">
      <inertial pos="0 0 0" mass="0.55" diaginertia="0.019437917 0.000531667 0.019822917"/>
      <joint name="seesaw1_hinge" type="hinge" axis="1 0 0" damping="0.04" range="0 42" solreflimit="0.003 1"/>
      <geom name="seesaw1_beam" type="box" size="0.05 0.325 0.02" mass="0" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.20 0.55 0.78 1"/>
      <geom name="seesaw1_left_pad" type="box" pos="0 -0.325 0.01" size="0.05 0.06 0.01" mass="0" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.18 0.45 0.67 1"/>
      <geom name="seesaw1_right_pad" type="box" pos="0 0.325 0.01" size="0.05 0.06 0.01" mass="0" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.18 0.45 0.67 1"/>
    </body>

    <body name="ball5" pos="2.815 2.85 0.35">
      <freejoint name="ball5_free"/>
      <geom name="ball5_sphere" type="sphere" size="0.05" mass="0.20" condim="6" friction="0.68 0.001 0.0005" solref="0.006 0.69" rgba="0.98 0.78 0.16 1"/>
    </body>
  </worldbody>

  <tendon>
    <fixed name="cart1_compression_spring" stiffness="18" damping="0" springlength="0.20 10">
      <joint joint="cart1_slide" coef="1"/>
    </fixed>
  </tendon>

  <actuator>
    <motor name="block1_substatic_assist" joint="block1_free" gear="0.369116 -0.929383 0 0 0 0" ctrllimited="true" ctrlrange="0 2.30"/>
  </actuator>

  <keyframe>
    <key name="start" ctrl="2.25"/>
  </keyframe>
</mujoco>
```