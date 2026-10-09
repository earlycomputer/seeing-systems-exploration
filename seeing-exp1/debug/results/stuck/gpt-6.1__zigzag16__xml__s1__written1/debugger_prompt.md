Write a MuJoCo MJCF scene for this brief:

<brief>
Use gravity 9.81 m/s2, contact friction 0.72, restitution 0.04, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, blocks are 0.12 m cubes and 0.35 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Ball1 starts 0.30 m above ring1 and drops vertically through it. Ball1 falls another 0.25 m and touches the left end of lever1, a 0.60 by 0.10 by 0.04 m, 0.50 kg center-hinged lever. Lever1 rotates clockwise through 45 degrees to its lower stop, and its rising right end knocks cart1 along a horizontal slide. Cart1 slides 0.42 m and touches domino1. Domino1 topples across a 0.18 m spacing and touches ball2 at the high end of ramp1. Ball2 rolls down ramp1, whose low end is 0.15 m above the floor, crosses a 0.10 m gap, and touches door1. Door1, a 0.42 by 0.32 by 0.04 m, 0.45 kg panel, swings clockwise through 70 degrees to its hard stop and strikes pendulum1. Pendulum1, a 0.50 m long, 0.35 kg rigid pendulum, swings clockwise through 38 degrees and touches block1. Block1 slides 0.35 m across the floor and touches cart2. Cart2 slides 0.42 m and touches the left end of seesaw1, a 0.65 by 0.10 by 0.04 m, 0.55 kg center-hinged beam carrying ball3 on its right end. Seesaw1 rotates clockwise through 42 degrees to its lower stop and launches ball3 vertically from its rising right end. Ball3 rises and then drops through ring2, centered 0.32 m below its initial center. Ball3 falls another 0.24 m and touches domino2. Domino2 topples across a 0.18 m gap and touches flap1, a 0.38 by 0.18 by 0.04 m, 0.28 kg hinged panel. Flap1 swings clockwise through 60 degrees to its hard stop and knocks ball4 from shelf1, a fixed 0.30 by 0.25 by 0.04 m shelf 0.55 m above cup1. Ball4 falls into cup1, whose inner footprint is 0.30 by 0.30 m with 0.20 m high and 0.02 m thick walls, and comes to rest there.
</brief>

MuJoCo will load the file, reset to the keyframe named `start` if there is one, and simulate it for
20 s. Nothing else acts on the scene: whatever moves must be set moving by the scene itself, for
example by a keyframe velocity, a spring, gravity, or a motor whose control the keyframe sets (controls keep
their keyframe values for the whole run).

A few conventions so the other tools can find things. They fix names and axes, not what you build:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- Name each thing's body exactly: `ball1` (starting falling ball: a body with a `<freejoint/>`); `ring1` (first horizontal ring: fixed in place; all its geoms belong to one body); `lever1` (cart striking lever: a body on a hinge joint); `cart1` (first slide cart: a body on a slide joint); `domino1` (first upright domino: a body with a `<freejoint/>`); `ball2` (ramp ball: a body with a `<freejoint/>`); `ramp1` (inclined ramp: fixed in place; all its geoms belong to one body); `door1` (pendulum striking door: a body on a hinge joint); `pendulum1` (block striking pendulum: a body on a hinge joint); `block1` (pendulum struck block: a body with a `<freejoint/>`); `cart2` (second slide cart: a body on a slide joint); `seesaw1` (ball launching seesaw: a body on a hinge joint); `ball3` (launched falling ball: a body with a `<freejoint/>`); `ring2` (second horizontal ring: fixed in place; all its geoms belong to one body); `domino2` (second upright domino: a body with a `<freejoint/>`); `flap1` (final striking flap: a body on a hinge joint); `ball4` (final catch ball: a body with a `<freejoint/>`); `shelf1` (ball support shelf: fixed in place; all its geoms belong to one body); `cup1` (final catch cup: fixed in place; all its geoms belong to one body). Its geoms may be named with the body's name as a prefix (`ball1_...`).
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures,
  `<default>` classes or `<include>`.
- Give every body and geom a name, and write each element's attributes on a single line.
- Set `<option timestep="0.002"/>`.

Reply with the complete file in one ```xml code block. A sentence or two before the block is fine.

A ball counts as at rest when it moves slower than 5 cm/s at the end.


You wrote this file:

```xml
<mujoco model="passive_chain_reaction">
  <compiler angle="radian" autolimits="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" iterations="100" tolerance="1e-10" o_friction="0.72 0.72 0.005 0.0001 0.0001" o_solref="0.01 0.7156" o_solimp="0.95 0.99 0.001">
    <flag override="enable"/>
  </option>
  <size njmax="3000" nconmax="800"/>
  <visual>
    <global azimuth="110" elevation="-25"/>
    <quality shadowsize="2048"/>
    <map znear="0.01" zfar="40"/>
  </visual>

  <worldbody>
    <light name="key_light" pos="-2 -3 6" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <light name="fill_light" pos="-3 3 4" dir="0 0 -1" diffuse="0.45 0.45 0.45"/>
    <camera name="overview" pos="-2.2 -7 3.6" xyaxes="1 0 0 0 0.38 0.925"/>
    <geom name="floor" type="plane" size="8 5 0.1" friction="0.72 0.005 0.0001" rgba="0.24 0.27 0.30 1"/>

    <!-- Passive springs are initially at dead centre. -->
    <site name="lever_spring_anchor" pos="-0.45 0 0.58" size="0.004" rgba="0.7 0.7 0.7 1"/>
    <site name="door_spring_anchor" pos="-1.609693 0.12 -0.29" size="0.004" rgba="0.7 0.7 0.7 1"/>
    <site name="pendulum_spring_anchor" pos="-1.99 0.12 1.03" size="0.004" rgba="0.7 0.7 0.7 1"/>
    <site name="seesaw_spring_anchor" pos="-3.270 0.12 1.15" size="0.004" rgba="0.7 0.7 0.7 1"/>

    <body name="ball1" pos="-0.26 -0.02 1.15">
      <freejoint name="ball1_free"/>
      <geom name="ball1_sphere" type="sphere" size="0.05" mass="0.20" rgba="0.95 0.25 0.15 1"/>
    </body>

    <!-- Circumscribed capsule polygons provide a 0.160 m clear diameter. -->
    <body name="ring1" pos="-0.26 -0.02 0.85">
      <geom name="ring1_01" type="capsule" fromto="0.089724 0 0 0.082894 0.034336 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring1_02" type="capsule" fromto="0.082894 0.034336 0 0.063444 0.063444 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring1_03" type="capsule" fromto="0.063444 0.063444 0 0.034336 0.082894 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring1_04" type="capsule" fromto="0.034336 0.082894 0 0 0.089724 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring1_05" type="capsule" fromto="0 0.089724 0 -0.034336 0.082894 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring1_06" type="capsule" fromto="-0.034336 0.082894 0 -0.063444 0.063444 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring1_07" type="capsule" fromto="-0.063444 0.063444 0 -0.082894 0.034336 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring1_08" type="capsule" fromto="-0.082894 0.034336 0 -0.089724 0 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring1_09" type="capsule" fromto="-0.089724 0 0 -0.082894 -0.034336 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring1_10" type="capsule" fromto="-0.082894 -0.034336 0 -0.063444 -0.063444 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring1_11" type="capsule" fromto="-0.063444 -0.063444 0 -0.034336 -0.082894 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring1_12" type="capsule" fromto="-0.034336 -0.082894 0 0 -0.089724 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring1_13" type="capsule" fromto="0 -0.089724 0 0.034336 -0.082894 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring1_14" type="capsule" fromto="0.034336 -0.082894 0 0.063444 -0.063444 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring1_15" type="capsule" fromto="0.063444 -0.063444 0 0.082894 -0.034336 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring1_16" type="capsule" fromto="0.082894 -0.034336 0 0.089724 0 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
    </body>

    <body name="lever1" pos="0 0 0.58">
      <inertial pos="0 0 0" mass="0.50" diaginertia="0.000483333 0.015066667 0.015416667"/>
      <joint name="lever1_hinge" type="hinge" axis="0 -1 0" damping="0.04" limited="true" range="0 0.785398163" solreflimit="0.004 1"/>
      <geom name="lever1_beam" type="box" size="0.30 0.05 0.02" mass="0" rgba="0.25 0.60 0.85 1"/>
      <geom name="lever1_kicker" type="capsule" fromto="0.30 -0.035 0 0.30 0.035 0" size="0.012" mass="0" rgba="0.20 0.45 0.65 1"/>
      <site name="lever_spring_tip" pos="0.28 0 0" size="0.004"/>
    </body>

    <!-- Post and split bearings are outside the moving beam's width. -->
    <body name="lever1_mount" pos="0 0 0.29">
      <geom name="lever1_mount_post" type="box" pos="0 0.10 0" size="0.025 0.025 0.29" rgba="0.40 0.42 0.45 1"/>
      <geom name="lever1_mount_bearing_a" type="cylinder" pos="0 -0.08 0.29" quat="0.707106781 0.707106781 0 0" size="0.018 0.020" rgba="0.65 0.65 0.68 1"/>
      <geom name="lever1_mount_bearing_b" type="cylinder" pos="0 0.08 0.29" quat="0.707106781 0.707106781 0 0" size="0.018 0.020" rgba="0.65 0.65 0.68 1"/>
    </body>

    <body name="cart1" pos="0.18 0.075 0.665">
      <joint name="cart1_slide" type="slide" axis="-1 0 0" damping="0.20" limited="true" range="0 0.42" solreflimit="0.006 1"/>
      <geom name="cart1_box" type="box" size="0.11 0.09 0.05" mass="0.50" rgba="0.20 0.75 0.35 1"/>
      <geom name="cart1_roller" type="sphere" pos="0.115 -0.075 -0.050" size="0.012" mass="0" rgba="0.15 0.35 0.20 1"/>
    </body>

    <!-- The slide joint supplies cart1's guide; intersecting decorative rails are omitted. -->

    <body name="domino1" pos="-0.37 0.12 0.612020143">
      <freejoint name="domino1_free"/>
      <geom name="domino1_box" type="box" size="0.02 0.04 0.12" mass="0.25" rgba="0.85 0.80 0.65 1"/>
    </body>

    <body name="domino1_support" pos="-0.37 0.12 0.472020143">
      <geom name="domino1_support_top" type="box" size="0.08 0.05 0.02" rgba="0.38 0.40 0.44 1"/>
      <geom name="domino1_support_leg" type="box" pos="0 0 -0.2260100715" size="0.025 0.025 0.2260100715" rgba="0.38 0.40 0.44 1"/>
    </body>

    <body name="ball2" pos="-0.55 0.12 0.542020143">
      <freejoint name="ball2_free"/>
      <geom name="ball2_sphere" type="sphere" size="0.05" mass="0.20" rgba="0.95 0.45 0.10 1"/>
    </body>

    <!-- This horizontal entry holds ball2 until domino1 pushes it onto the slope. -->
    <body name="ramp1_entry" pos="-0.535 0.12 0.482020143">
      <geom name="ramp1_entry_plate" type="box" size="0.045 0.10 0.01" rgba="0.45 0.50 0.58 1"/>
    </body>

    <body name="ramp1" pos="-1.016426169 0.12 0.311613145" quat="0.984807753 0 -0.173648178 0">
      <geom name="ramp1_surface" type="box" size="0.50 0.15 0.01" rgba="0.50 0.58 0.68 1"/>
      <geom name="ramp1_side_a" type="box" pos="0 -0.157 0.035" size="0.50 0.007 0.025" rgba="0.35 0.42 0.52 1"/>
      <geom name="ramp1_side_b" type="box" pos="0 0.157 0.035" size="0.50 0.007 0.025" rgba="0.35 0.42 0.52 1"/>
    </body>

    <body name="door1" pos="-1.609693 0.12 0.01">
      <joint name="door1_hinge" type="hinge" axis="0 -1 0" damping="0.04" limited="true" range="0 1.221730476" solreflimit="0.004 1"/>
      <geom name="door1_panel" type="box" pos="0 0 0.21" size="0.02 0.16 0.21" mass="0.45" rgba="0.70 0.35 0.20 1"/>
      <site name="door_spring_tip" pos="0 0 0.35" size="0.004"/>
    </body>

    <body name="door1_mount" pos="-1.609693 0.12 0.01">
      <geom name="door1_mount_bearing_a" type="cylinder" pos="0 -0.19 0" quat="0.707106781 0.707106781 0 0" size="0.008 0.025" rgba="0.55 0.55 0.58 1"/>
      <geom name="door1_mount_bearing_b" type="cylinder" pos="0 0.19 0" quat="0.707106781 0.707106781 0 0" size="0.008 0.025" rgba="0.55 0.55 0.58 1"/>
    </body>

    <body name="pendulum1" pos="-1.99 0.12 0.53">
      <joint name="pendulum1_hinge" type="hinge" axis="0 1 0" damping="0.04" limited="true" range="0 0.663225116" solreflimit="0.006 1"/>
      <geom name="pendulum1_rod" type="capsule" fromto="0 0 0 0 0 -0.50" size="0.012" mass="0.07" rgba="0.65 0.65 0.70 1"/>
      <geom name="pendulum1_bob" type="sphere" pos="0 0 -0.50" size="0.03" mass="0.28" rgba="0.45 0.25 0.75 1"/>
      <site name="pendulum_spring_tip" pos="0 0 -0.50" size="0.004"/>
    </body>

    <body name="pendulum1_mount" pos="-1.99 0.12 0.53">
      <geom name="pendulum1_mount_bearing_a" type="cylinder" pos="0 -0.045 0" quat="0.707106781 0.707106781 0 0" size="0.015 0.020" rgba="0.55 0.55 0.58 1"/>
      <geom name="pendulum1_mount_bearing_b" type="cylinder" pos="0 0.045 0" quat="0.707106781 0.707106781 0 0" size="0.015 0.020" rgba="0.55 0.55 0.58 1"/>
      <geom name="pendulum1_mount_post" type="box" pos="0 0.10 -0.265" size="0.018 0.018 0.265" rgba="0.40 0.42 0.45 1"/>
    </body>

    <body name="block1" pos="-2.383 0.12 0.06">
      <freejoint name="block1_free"/>
      <geom name="block1_box" type="box" size="0.06 0.06 0.06" mass="0.35" rgba="0.80 0.35 0.65 1"/>
    </body>

    <!-- Side guides terminate 20 mm before cart2's initial right face. -->
    <body name="block1_guide" pos="-2.66 0.12 0">
      <geom name="block1_guide_a" type="box" pos="0.157 -0.077 0.070" size="0.270 0.008 0.070" rgba="0.40 0.45 0.50 1"/>
      <geom name="block1_guide_b" type="box" pos="0.157 0.077 0.070" size="0.270 0.008 0.070" rgba="0.40 0.45 0.50 1"/>
      <geom name="block1_guide_roof" type="box" pos="-0.0565 0 0.132" size="0.2935 0.068 0.005" rgba="0.40 0.45 0.50 0.35"/>
    </body>

    <body name="cart2" pos="-2.903 0.12 0.06">
      <joint name="cart2_slide" type="slide" axis="-1 0 0" damping="0.20" limited="true" range="0 0.42" solreflimit="0.006 1"/>
      <geom name="cart2_box" type="box" size="0.11 0.09 0.05" mass="0.50" rgba="0.20 0.70 0.55 1"/>
    </body>

    <body name="cart2_rail" pos="-3.113 0.12 0.004">
      <geom name="cart2_rail_a" type="box" pos="0 -0.075 0" size="0.34 0.006 0.004" rgba="0.45 0.45 0.48 1"/>
      <geom name="cart2_rail_b" type="box" pos="0 0.075 0" size="0.34 0.006 0.004" rgba="0.45 0.45 0.48 1"/>
    </body>

    <!-- A low striker extension connects cart2 to the elevated seesaw. -->
    <body name="seesaw1" pos="-3.770 0.12 1.15">
      <inertial pos="0 0 0" mass="0.55" diaginertia="0.000531667 0.019437917 0.019822917"/>
      <joint name="seesaw1_hinge" type="hinge" axis="0 1 0" damping="0.04" limited="true" range="0 0.733038286" solreflimit="0.004 1"/>
      <geom name="seesaw1_beam" type="box" size="0.325 0.05 0.02" mass="0" rgba="0.25 0.55 0.90 1"/>
      <geom name="seesaw1_striker_extension" type="capsule" fromto="0.325 0 0 0.325 0 -1.08" size="0.012" mass="0" rgba="0.30 0.45 0.60 1"/>
      <site name="seesaw_spring_tip" pos="-0.30 0 0" size="0.004"/>
    </body>

    <body name="seesaw1_mount" pos="-3.770 0.12 0.575">
      <geom name="seesaw1_mount_post" type="box" pos="0 0.105 0" size="0.025 0.025 0.575" rgba="0.40 0.42 0.45 1"/>
      <geom name="seesaw1_mount_bearing_a" type="cylinder" pos="0 -0.075 0.575" quat="0.707106781 0.707106781 0 0" size="0.018 0.020" rgba="0.60 0.60 0.64 1"/>
      <geom name="seesaw1_mount_bearing_b" type="cylinder" pos="0 0.075 0.575" quat="0.707106781 0.707106781 0 0" size="0.018 0.020" rgba="0.60 0.60 0.64 1"/>
    </body>

    <body name="ball3" pos="-4.085 0.12 1.22">
      <freejoint name="ball3_free"/>
      <geom name="ball3_sphere" type="sphere" size="0.05" mass="0.20" rgba="0.95 0.75 0.15 1"/>
    </body>

    <!-- Beam-clearance window and tapered entrance in the launch guide. -->
    <body name="ball3_launch_guide" pos="-4.085 0.12 0">
      <geom name="ball3_launch_guide_y_a" type="box" pos="0 -0.063 1.60" size="0.12 0.008 0.90" rgba="0.55 0.65 0.75 0.30"/>
      <geom name="ball3_launch_guide_y_b" type="box" pos="0 0.063 1.60" size="0.12 0.008 0.90" rgba="0.55 0.65 0.75 0.30"/>
      <geom name="ball3_launch_guide_lower_a" type="box" pos="-0.063 0 0.9175" size="0.008 0.055 0.1975" rgba="0.55 0.65 0.75 0.30"/>
      <geom name="ball3_launch_guide_lower_b" type="box" pos="0.063 0 0.9175" size="0.008 0.055 0.1975" rgba="0.55 0.65 0.75 0.30"/>
      <geom name="ball3_launch_guide_taper_a" type="box" pos="-0.08 0 1.525" quat="0.996856 0 0.079244 0" size="0.006 0.055 0.12659" rgba="0.55 0.65 0.75 0.30"/>
      <geom name="ball3_launch_guide_taper_b" type="box" pos="0.08 0 1.525" quat="0.996856 0 -0.079244 0" size="0.006 0.055 0.12659" rgba="0.55 0.65 0.75 0.30"/>
      <geom name="ball3_launch_guide_upper_a" type="box" pos="-0.061 0 2.075" size="0.008 0.055 0.425" rgba="0.55 0.65 0.75 0.30"/>
      <geom name="ball3_launch_guide_upper_b" type="box" pos="0.061 0 2.075" size="0.008 0.055 0.425" rgba="0.55 0.65 0.75 0.30"/>
    </body>

    <body name="ring2" pos="-4.085 0.12 0.90">
      <geom name="ring2_01" type="capsule" fromto="0.089724 0 0 0.082894 0.034336 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring2_02" type="capsule" fromto="0.082894 0.034336 0 0.063444 0.063444 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring2_03" type="capsule" fromto="0.063444 0.063444 0 0.034336 0.082894 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring2_04" type="capsule" fromto="0.034336 0.082894 0 0 0.089724 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring2_05" type="capsule" fromto="0 0.089724 0 -0.034336 0.082894 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring2_06" type="capsule" fromto="-0.034336 0.082894 0 -0.063444 0.063444 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring2_07" type="capsule" fromto="-0.063444 0.063444 0 -0.082894 0.034336 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring2_08" type="capsule" fromto="-0.082894 0.034336 0 -0.089724 0 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring2_09" type="capsule" fromto="-0.089724 0 0 -0.082894 -0.034336 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring2_10" type="capsule" fromto="-0.082894 -0.034336 0 -0.063444 -0.063444 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring2_11" type="capsule" fromto="-0.063444 -0.063444 0 -0.034336 -0.082894 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring2_12" type="capsule" fromto="-0.034336 -0.082894 0 0 -0.089724 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring2_13" type="capsule" fromto="0 -0.089724 0 0.034336 -0.082894 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring2_14" type="capsule" fromto="0.034336 -0.082894 0 0.063444 -0.063444 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring2_15" type="capsule" fromto="0.063444 -0.063444 0 0.082894 -0.034336 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
      <geom name="ring2_16" type="capsule" fromto="0.082894 -0.034336 0 0.089724 0 0" size="0.008" rgba="0.95 0.75 0.15 1"/>
    </body>

    <body name="domino2" pos="-4.05 0.12 0.54">
      <freejoint name="domino2_free"/>
      <geom name="domino2_box" type="box" size="0.02 0.04 0.12" mass="0.25" rgba="0.85 0.80 0.65 1"/>
    </body>

    <body name="domino2_support" pos="-4.15 0.12 0.40">
      <geom name="domino2_support_top" type="box" size="0.25 0.10 0.02" rgba="0.38 0.40 0.44 1"/>
      <geom name="domino2_support_leg_a" type="box" pos="0.18 0 -0.19" size="0.025 0.025 0.19" rgba="0.38 0.40 0.44 1"/>
      <geom name="domino2_support_leg_b" type="box" pos="-0.18 0 -0.19" size="0.025 0.025 0.19" rgba="0.38 0.40 0.44 1"/>
    </body>

    <body name="flap1" pos="-4.27 0.12 0.42">
      <joint name="flap1_hinge" type="hinge" axis="0 -1 0" damping="0.04" limited="true" range="0 1.047197551" solreflimit="0.004 1"/>
      <geom name="flap1_panel" type="box" pos="0 0 0.19" size="0.02 0.09 0.19" mass="0.28" rgba="0.65 0.40 0.20 1"/>
    </body>

    <body name="flap1_mount" pos="-4.27 0.12 0.42">
      <geom name="flap1_mount_bearing_a" type="cylinder" pos="0 -0.11 0" quat="0.707106781 0.707106781 0 0" size="0.008 0.015" rgba="0.55 0.55 0.58 1"/>
      <geom name="flap1_mount_bearing_b" type="cylinder" pos="0 0.11 0" quat="0.707106781 0.707106781 0 0" size="0.008 0.015" rgba="0.55 0.55 0.58 1"/>
    </body>

    <body name="ball4" pos="-4.62 0.12 0.62">
      <freejoint name="ball4_free"/>
      <geom name="ball4_sphere" type="sphere" size="0.05" mass="0.20" rgba="0.90 0.20 0.30 1"/>
    </body>

    <body name="shelf1" pos="-4.52 0.12 0.55">
      <geom name="shelf1_plate" type="box" size="0.15 0.125 0.02" rgba="0.45 0.50 0.58 1"/>
    </body>

    <!-- Interior bottom is z=0.02; shelf top is 0.55 m above it. -->
    <body name="cup1" pos="-4.76 0.12 0">
      <geom name="cup1_bottom" type="box" pos="0 0 0.01" size="0.17 0.17 0.01" rgba="0.25 0.65 0.75 1"/>
      <geom name="cup1_wall_x_minus" type="box" pos="-0.16 0 0.12" size="0.01 0.17 0.10" rgba="0.25 0.65 0.75 1"/>
      <geom name="cup1_wall_x_plus" type="box" pos="0.16 0 0.12" size="0.01 0.17 0.10" rgba="0.25 0.65 0.75 1"/>
      <geom name="cup1_wall_y_minus" type="box" pos="0 -0.16 0.12" size="0.15 0.01 0.10" rgba="0.25 0.65 0.75 1"/>
      <geom name="cup1_wall_y_plus" type="box" pos="0 0.16 0.12" size="0.15 0.01 0.10" rgba="0.25 0.65 0.75 1"/>
    </body>

    <body name="cup1_catch_guide" pos="-4.76 0.12 0">
      <geom name="cup1_catch_guide_back" type="box" pos="-0.16 0 0.535" size="0.01 0.17 0.315" rgba="0.45 0.65 0.75 0.35"/>
      <geom name="cup1_catch_guide_side_a" type="box" pos="0 -0.16 0.535" size="0.15 0.01 0.315" rgba="0.45 0.65 0.75 0.35"/>
      <geom name="cup1_catch_guide_side_b" type="box" pos="0 0.16 0.535" size="0.15 0.01 0.315" rgba="0.45 0.65 0.75 0.35"/>
    </body>
  </worldbody>

  <tendon>
    <spatial name="lever1_toggle_spring" stiffness="80" damping="0.02" springlength="0.15 0.15" width="0.002" rgba="0.7 0.7 0.7 0.5">
      <site site="lever_spring_anchor"/>
      <site site="lever_spring_tip"/>
    </spatial>
    <spatial name="door1_toggle_spring" stiffness="12" damping="0.02" springlength="0.15 0.15" width="0.002" rgba="0.7 0.7 0.7 0.5">
      <site site="door_spring_anchor"/>
      <site site="door_spring_tip"/>
    </spatial>
    <spatial name="pendulum1_toggle_spring" stiffness="70" damping="0.02" springlength="0.20 0.20" width="0.002" rgba="0.7 0.7 0.7 0.5">
      <site site="pendulum_spring_anchor"/>
      <site site="pendulum_spring_tip"/>
    </spatial>
    <spatial name="seesaw1_toggle_spring" stiffness="100" damping="0.02" springlength="0.10 0.10" width="0.002" rgba="0.7 0.7 0.7 0.5">
      <site site="seesaw_spring_anchor"/>
      <site site="seesaw_spring_tip"/>
    </spatial>
  </tendon>

  <keyframe>
    <key name="start" time="0"/>
  </keyframe>
</mujoco>
```

MuJoCo ran your scene for 20 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 20.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_sphere; starts at (-0.26, -0.02, 1.15) m, at rest
- lever1: hinge joint lever1_hinge about axis (0.00, -1.00, 0.00), range 0° to 45° as MuJoCo applies it; its geoms: lever1_beam, lever1_kicker; starts at 0.0°, still
- cart1: slide joint cart1_slide about axis (-1.00, 0.00, 0.00), range 0 m to 0.42 m as MuJoCo applies it; its geoms: cart1_box, cart1_roller; starts at 0.000 m, still
- domino1: free body; its geoms: domino1_box; starts at (-0.37, 0.12, 0.61) m, at rest
- ball2: free body; its geoms: ball2_sphere; starts at (-0.55, 0.12, 0.54) m, at rest
- door1: hinge joint door1_hinge about axis (0.00, -1.00, 0.00), range 0° to 70° as MuJoCo applies it; its geoms: door1_panel; starts at 0.0°, still
- pendulum1: hinge joint pendulum1_hinge about axis (0.00, 1.00, 0.00), range 0° to 38° as MuJoCo applies it; its geoms: pendulum1_rod, pendulum1_bob; starts at 0.0°, still
- block1: free body; its geoms: block1_box; starts at (-2.38, 0.12, 0.06) m, at rest
- cart2: slide joint cart2_slide about axis (-1.00, 0.00, 0.00), range 0 m to 0.42 m as MuJoCo applies it; its geoms: cart2_box; starts at 0.000 m, still
- seesaw1: hinge joint seesaw1_hinge about axis (0.00, 1.00, 0.00), range 0° to 42° as MuJoCo applies it; its geoms: seesaw1_beam, seesaw1_striker_extension; starts at 0.0°, still
- ball3: free body; its geoms: ball3_sphere; starts at (-4.08, 0.12, 1.22) m, at rest
- domino2: free body; its geoms: domino2_box; starts at (-4.05, 0.12, 0.54) m, at rest
- flap1: hinge joint flap1_hinge about axis (0.00, -1.00, 0.00), range 0° to 60° as MuJoCo applies it; its geoms: flap1_panel; starts at 0.0°, still
- ball4: free body; its geoms: ball4_sphere; starts at (-4.62, 0.12, 0.62) m, at rest

What happened, in order:
 0.00 s  flap1_panel starts touching domino2_support_top
 0.00 s  ball2_sphere starts touching ramp1_entry_plate
 0.00 s  block1_box starts touching floor
 0.00 s  ball4_sphere starts touching shelf1_plate
 0.00 s  ball2_sphere starts touching ramp1_surface
 0.00 s  domino1_box starts touching domino1_support_top
 0.00 s  lever1 starts at its 0° stop (neither end sits lower)
 0.00 s  cart1 starts at its lower stop (0 m)
 0.00 s  door1 starts at its 0° stop (the end where it sits higher)
 0.00 s  pendulum1 starts at its 0° stop (the end where it sits lower)
 0.00 s  pendulum1 is at its largest at the start, 0.0°
 0.00 s  cart2 starts at its lower stop (0 m)
 0.00 s  cart2 is at its largest at the start, 0.0 m
 0.00 s  seesaw1 starts at its 0° stop (neither end sits lower)
 0.00 s  flap1 starts at its 0° stop (the end where it sits higher)
 0.00 s  domino2_box first touches domino2_support_top
 0.00 s  seesaw1_beam first touches ball3_sphere
 0.01 s  ball1 starts moving
 0.01 s  seesaw1 is at its smallest, -0.0°
 0.25 s  ball1 passes 0.03 m from ring1 (ring1_15) without touching it: nearest points (-0.22, -0.05, 0.85) m and (-0.19, -0.06, 0.85) m
 0.30 s  ball1 passes 0.28 m from cart1 (cart1_box) without touching it: nearest points (-0.21, -0.02, 0.71) m and (0.07, -0.02, 0.71) m
 0.32 s  ball1_sphere first touches lever1_beam
 0.33 s  lever1_beam first touches cart1_roller
 0.33 s  lever1 is at its largest, 1.3°
 0.33 s  ball1 passes 0.20 m from lever1_mount (lever1_mount_bearing_a) without touching it: nearest points (-0.21, -0.03, 0.63) m and (-0.02, -0.06, 0.58) m
 0.33 s  cart1 is at its smallest, -0.0 m
 0.34 s  ball1_sphere leaves lever1_beam
 0.35 s  lever1_beam leaves cart1_roller
 0.35 s  lever1 reaches its 0° stop (neither end sits lower) again moving -44°/s
 0.36 s  lever1 is at its smallest, -0.1°
 0.42 s  ball1 is at the top of its flight, at (-0.26, -0.02, 0.67) m
 0.43 s  lever1_beam touches cart1_roller again
 0.50 s  ball1_sphere touches lever1_beam again
 1.25 s  ball1_sphere leaves lever1_beam
 1.27 s  ball2_sphere leaves ramp1_surface
 1.38 s  ball1 passes 0.05 m from domino1 (domino1_box) without touching it: nearest points (-0.38, 0.03, 0.51) m and (-0.38, 0.08, 0.51) m
 1.38 s  ball1 passes 0.12 m from ball2 (ball2_sphere) without touching it: nearest points (-0.42, 0.01, 0.51) m and (-0.51, 0.09, 0.53) m
 1.39 s  ball1 passes 0.04 m from domino1_support (domino1_support_top) without touching it: nearest points (-0.38, 0.03, 0.49) m and (-0.38, 0.07, 0.49) m
 1.41 s  ball1 passes 0.06 m from ramp1_entry (ramp1_entry_plate) without touching it: nearest points (-0.44, 0.00, 0.46) m and (-0.49, 0.02, 0.47) m
 1.57 s  ball1_sphere first touches floor
 1.59 s  ball1_sphere leaves floor
 1.65 s  ball1 is at the top of its flight, at (-0.47, -0.02, 0.07) m
 1.72 s  ball1_sphere touches floor again
 4.49 s  ball1_sphere first touches door1_panel
 4.49 s  ball1 passes 0.03 m from door1_mount (door1_mount_bearing_a) without touching it: nearest points (-1.58, -0.04, 0.03) m and (-1.60, -0.04, 0.01) m
 4.49 s  ball1 passes 0.39 m from pendulum1 (pendulum1_bob) without touching it: nearest points (-1.59, -0.01, 0.05) m and (-1.96, 0.11, 0.03) m
 4.49 s  ball1 passes 0.43 m from pendulum1_mount (pendulum1_mount_post) without touching it: nearest points (-1.59, 0.00, 0.05) m and (-1.97, 0.20, 0.05) m
 4.51 s  ball1_sphere leaves door1_panel
 5.04 s  door1_panel first touches floor
 5.04 s  door1 is at its largest, 30.9°
 5.05 s  door1 passes 0.14 m from pendulum1 (pendulum1_rod) without touching it: nearest points (-1.84, 0.12, 0.36) m and (-1.98, 0.12, 0.36) m
 5.05 s  door1 passes 0.13 m from pendulum1_mount (pendulum1_mount_post) without touching it: nearest points (-1.84, 0.21, 0.36) m and (-1.97, 0.21, 0.36) m
 5.05 s  door1 passes 0.45 m from block1_guide (block1_guide_b) without touching it: nearest points (-1.84, 0.19, 0.36) m and (-2.23, 0.19, 0.14) m
 5.53 s  ball1 passes 0.03 m from ramp1 (ramp1_surface) without touching it: nearest points (-1.48, -0.02, 0.10) m and (-1.48, -0.02, 0.13) m
 7.38 s  ball3 starts moving
 7.59 s  seesaw1_beam leaves ball3_sphere
 7.64 s  ball3_sphere first touches ball3_launch_guide_lower_a
 7.73 s  ball3_sphere leaves ball3_launch_guide_lower_a
 7.91 s  ball3 passes 0.04 m from ring2 (ring2_08) without touching it: nearest points (-4.22, 0.12, 0.91) m and (-4.18, 0.12, 0.90) m
 7.92 s  seesaw1_striker_extension first touches domino2_support_leg_a
 7.94 s  seesaw1_striker_extension leaves domino2_support_leg_a
 7.94 s  ball3_sphere first touches flap1_panel
 7.95 s  ball3 passes 0.23 m from domino2 (domino2_box) without touching it: nearest points (-4.25, 0.12, 0.81) m and (-4.07, 0.12, 0.66) m
 7.96 s  flap1 is at its largest, 0.0°
 7.97 s  ball3_sphere leaves flap1_panel
 7.98 s  seesaw1_striker_extension touches domino2_support_leg_a again
 7.98 s  flap1 is at its smallest, -0.0°
 7.98 s  seesaw1_striker_extension leaves domino2_support_leg_a
 8.00 s  ball3 is at the top of its flight, at (-4.30, 0.12, 0.85) m
 8.02 s  seesaw1_striker_extension touches domino2_support_leg_a again
 8.06 s  seesaw1_striker_extension leaves domino2_support_leg_a
 8.10 s  seesaw1_striker_extension touches domino2_support_leg_a again
 8.22 s  ball3_sphere first touches shelf1_plate
 8.22 s  ball3 passes 0.14 m from domino2_support (domino2_support_top) without touching it: nearest points (-4.41, 0.12, 0.56) m and (-4.40, 0.12, 0.42) m
 8.22 s  ball3 passes 0.20 m from flap1_mount (flap1_mount_bearing_a) without touching it: nearest points (-4.38, 0.10, 0.58) m and (-4.27, 0.03, 0.43) m
 8.23 s  seesaw1_striker_extension leaves domino2_support_leg_a
 8.24 s  ball3_sphere leaves shelf1_plate
 8.27 s  seesaw1_striker_extension touches domino2_support_leg_a 93 more times between 8.27 s and 19.99 s
 8.31 s  ball3_sphere touches shelf1_plate again
 8.47 s  ball3_sphere leaves shelf1_plate
 8.47 s  ball3_sphere first touches ball4_sphere
 8.47 s  ball4 starts moving
 8.49 s  ball3_sphere leaves ball4_sphere
 8.51 s  ball3_sphere touches shelf1_plate again
 8.98 s  ball4_sphere leaves shelf1_plate
 9.28 s  ball4_sphere first touches cup1_bottom
 9.30 s  ball4_sphere leaves cup1_bottom
 9.36 s  ball4 is at the top of its flight, at (-4.84, 0.12, 0.09) m
 9.41 s  ball4_sphere first touches cup1_wall_x_minus
 9.43 s  ball4_sphere leaves cup1_wall_x_minus
 9.44 s  ball4_sphere touches cup1_bottom again
10.73 s  ball4_sphere first touches cup1_wall_x_plus
10.74 s  ball4_sphere leaves cup1_wall_x_plus
11.81 s  ball2 starts moving
11.92 s  seesaw1 is at its largest, 26.3°
11.92 s  seesaw1 passes 0.22 m from domino2 (domino2_box) without touching it: nearest points (-3.83, 0.12, 0.32) m and (-4.03, 0.12, 0.42) m
11.92 s  seesaw1 passes 0.44 m from flap1_mount (flap1_mount_bearing_a) without touching it: nearest points (-3.88, 0.12, 0.23) m and (-4.26, 0.03, 0.42) m
11.95 s  ball2_sphere leaves ramp1_entry_plate
11.95 s  ball2_sphere first touches domino1_support_top
12.13 s  ball2_sphere leaves domino1_support_top
12.13 s  ball2_sphere touches ramp1_entry_plate again
12.25 s  ball2_sphere leaves ramp1_entry_plate
12.25 s  ball2_sphere touches domino1_support_top again
12.34 s  ball2_sphere touches ramp1_entry_plate again
12.34 s  ball2_sphere leaves domino1_support_top
12.41 s  ball2_sphere leaves ramp1_entry_plate
12.41 s  ball2_sphere touches domino1_support_top again
12.46 s  ball2_sphere touches ramp1_entry_plate again
12.46 s  ball2_sphere leaves domino1_support_top
12.46 s  ball2 comes to rest at (-0.47, 0.12, 0.54) m
12.49 s  ball2_sphere touches domino1_support_top again
15.47 s  ball3_sphere leaves shelf1_plate
15.60 s  ball4_sphere touches cup1_wall_x_minus again
15.62 s  ball4_sphere leaves cup1_wall_x_minus
15.72 s  ball3 passes 0.07 m from cup1_catch_guide (cup1_catch_guide_back) without touching it: nearest points (-4.84, 0.12, 0.22) m and (-4.91, 0.12, 0.22) m
15.74 s  ball3_sphere touches ball4_sphere again
15.75 s  ball4_sphere touches cup1_wall_x_minus again
15.77 s  ball3_sphere leaves ball4_sphere
15.77 s  ball4_sphere leaves cup1_wall_x_minus
15.79 s  ball4 comes to rest at (-4.86, 0.12, 0.07) m
15.83 s  ball3_sphere first touches cup1_bottom
15.88 s  ball3_sphere leaves cup1_bottom
15.88 s  ball3_sphere first touches cup1_wall_x_plus
15.90 s  ball3_sphere leaves cup1_wall_x_plus
15.95 s  ball3_sphere touches cup1_bottom again
16.76 s  ball3_sphere touches ball4_sphere again
16.76 s  ball3 comes to rest at (-4.72, 0.12, 0.07) m
16.78 s  ball3_sphere leaves ball4_sphere
20.00 s  ball1 is still moving at the end, 0.06 m/s
20.00 s  cart1 is at its largest, 0.0 m

State every 0.25 s:
0.00 s: ball1 at (-0.26, -0.02, 1.15) m, at rest; touching nothing | lever1 at 0.0°, still; touching nothing | cart1 at 0.000 m, still; touching nothing | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.55, 0.12, 0.54) m, at rest; touching ramp1_entry_plate, ramp1_surface | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 0.0°, still; touching nothing | ball3 at (-4.08, 0.12, 1.22) m, at rest; touching nothing | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching nothing | flap1 at 0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
0.25 s: ball1 at (-0.26, -0.02, 0.85) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | lever1 at 0.0°, still; touching nothing | cart1 at 0.000 m, still; touching nothing | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.55, 0.12, 0.54) m, at rest; touching ramp1_entry_plate, ramp1_surface | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
0.50 s: ball1 at (-0.27, -0.02, 0.65) m, moving 0.16 m/s (vx -0.04, vy -0.00, vz -0.16); touching lever1_beam | lever1 at 0.6°, still; touching ball1_sphere, cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.55, 0.12, 0.54) m, at rest; touching ramp1_entry_plate, ramp1_surface | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
0.75 s: ball1 at (-0.28, -0.02, 0.65) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching lever1_beam | lever1 at 0.6°, still; touching ball1_sphere, cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.55, 0.12, 0.54) m, at rest; touching ramp1_entry_plate, ramp1_surface | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
1.00 s: ball1 at (-0.30, -0.02, 0.65) m, moving 0.08 m/s (vx -0.08, vy -0.00, vz -0.00); touching lever1_beam | lever1 at 0.6°, still; touching ball1_sphere, cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.55, 0.12, 0.54) m, at rest; touching ramp1_entry_plate, ramp1_surface | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
1.25 s: ball1 at (-0.34, -0.02, 0.63) m, moving 0.48 m/s (vx -0.33, vy -0.00, vz -0.35); touching nothing | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.55, 0.12, 0.54) m, at rest; touching ramp1_entry_plate, ramp1_surface | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
1.50 s: ball1 at (-0.42, -0.02, 0.25) m, moving 2.79 m/s (vx -0.34, vy -0.00, vz -2.77); touching nothing | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.55, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
1.75 s: ball1 at (-0.51, -0.02, 0.05) m, moving 0.38 m/s (vx -0.38, vy -0.00, vz -0.01); touching nothing | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.55, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
2.00 s: ball1 at (-0.60, -0.02, 0.05) m, moving 0.38 m/s (vx -0.38, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.54, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
2.25 s: ball1 at (-0.70, -0.02, 0.05) m, moving 0.38 m/s (vx -0.38, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.54, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
2.50 s: ball1 at (-0.79, -0.02, 0.05) m, moving 0.38 m/s (vx -0.38, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.54, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
2.75 s: ball1 at (-0.89, -0.02, 0.05) m, moving 0.38 m/s (vx -0.38, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.54, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
3.00 s: ball1 at (-0.98, -0.02, 0.05) m, moving 0.38 m/s (vx -0.38, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.54, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
3.25 s: ball1 at (-1.07, -0.02, 0.05) m, moving 0.38 m/s (vx -0.38, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.54, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
3.50 s: ball1 at (-1.17, -0.02, 0.05) m, moving 0.38 m/s (vx -0.38, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.54, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
3.75 s: ball1 at (-1.26, -0.02, 0.05) m, moving 0.38 m/s (vx -0.38, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.53, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
4.00 s: ball1 at (-1.36, -0.02, 0.05) m, moving 0.38 m/s (vx -0.38, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.53, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
4.25 s: ball1 at (-1.45, -0.02, 0.05) m, moving 0.38 m/s (vx -0.38, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.53, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
4.50 s: ball1 at (-1.54, -0.02, 0.05) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz +0.01); touching door1_panel | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.53, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 0.1°, turning +7°/s; touching ball1_sphere | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
4.75 s: ball1 at (-1.53, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.53, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 3.3°, turning +26°/s; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
5.00 s: ball1 at (-1.51, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.53, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 23.0°, turning +175°/s; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
5.25 s: ball1 at (-1.50, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.53, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
5.50 s: ball1 at (-1.48, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.52, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
5.75 s: ball1 at (-1.47, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.52, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
6.00 s: ball1 at (-1.46, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.52, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
6.25 s: ball1 at (-1.44, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.52, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
6.50 s: ball1 at (-1.43, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.52, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
6.75 s: ball1 at (-1.42, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.52, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
7.00 s: ball1 at (-1.40, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.52, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.09, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
7.25 s: ball1 at (-1.39, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.51, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.10, 0.12, 1.22) m, at rest; touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
7.50 s: ball1 at (-1.37, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.51, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at -0.0°, still; touching ball3_sphere | ball3 at (-4.11, 0.12, 1.22) m, moving 0.21 m/s (vx -0.20, vy -0.00, vz -0.07); touching seesaw1_beam | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
7.75 s: ball1 at (-1.36, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.51, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 0.4°, turning +9°/s; touching nothing | ball3 at (-4.20, 0.12, 1.14) m, moving 0.72 m/s (vx -0.43, vy -0.00, vz -0.57); touching nothing | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
8.00 s: ball1 at (-1.35, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.51, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 23.1°, turning +45°/s; touching nothing | ball3 at (-4.31, 0.12, 0.85) m, moving 0.45 m/s (vx -0.45, vy +0.00, vz -0.05); touching nothing | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at 0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
8.25 s: ball1 at (-1.33, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.51, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 22.5°, turning -22°/s; touching nothing | ball3 at (-4.42, 0.12, 0.62) m, moving 0.50 m/s (vx -0.45, vy -0.00, vz +0.21); touching nothing | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at 0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate
8.50 s: ball1 at (-1.32, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.51, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.4°, turning +60°/s; touching nothing | ball3 at (-4.52, 0.12, 0.62) m, moving 0.12 m/s (vx -0.05, vy -0.00, vz -0.11); touching nothing | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.62, 0.12, 0.62) m, moving 0.14 m/s (vx -0.14, vy +0.00, vz +0.00); touching shelf1_plate
8.75 s: ball1 at (-1.31, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.51, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.9°, turning +71°/s; touching nothing | ball3 at (-4.53, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.66, 0.12, 0.62) m, moving 0.14 m/s (vx -0.14, vy +0.00, vz +0.00); touching shelf1_plate
9.00 s: ball1 at (-1.29, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.50, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.9°, turning +5°/s; touching nothing | ball3 at (-4.53, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at 0.0°, still; touching domino2_support_top | ball4 at (-4.71, 0.12, 0.60) m, moving 0.66 m/s (vx -0.35, vy +0.00, vz -0.56); touching nothing
9.25 s: ball1 at (-1.28, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.50, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.2°, turning -17°/s; touching domino2_support_leg_a | ball3 at (-4.54, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.80, 0.12, 0.15) m, moving 3.03 m/s (vx -0.35, vy +0.00, vz -3.01); touching nothing
9.50 s: ball1 at (-1.26, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.50, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.0°, turning +57°/s; touching nothing | ball3 at (-4.55, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at 0.0°, still; touching domino2_support_top | ball4 at (-4.85, 0.12, 0.07) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz +0.00); touching cup1_bottom
9.75 s: ball1 at (-1.25, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.50, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.8°, turning +220°/s; touching nothing | ball3 at (-4.55, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at 0.0°, still; touching domino2_support_top | ball4 at (-4.81, 0.12, 0.07) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz +0.00); touching cup1_bottom
10.00 s: ball1 at (-1.24, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.50, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.0°, turning -63°/s; touching domino2_support_leg_a | ball3 at (-4.56, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.77, 0.12, 0.07) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz -0.00); touching cup1_bottom
10.25 s: ball1 at (-1.22, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.50, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.5°, turning +178°/s; touching nothing | ball3 at (-4.56, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at 0.0°, still; touching domino2_support_top | ball4 at (-4.73, 0.12, 0.07) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz -0.00); touching cup1_bottom
10.50 s: ball1 at (-1.21, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.50, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.0°, turning +176°/s; touching nothing | ball3 at (-4.57, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at 0.0°, still; touching domino2_support_top | ball4 at (-4.69, 0.12, 0.07) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz +0.00); touching cup1_bottom
10.75 s: ball1 at (-1.19, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.49, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.8°, turning +294°/s; touching nothing | ball3 at (-4.57, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.66, 0.12, 0.07) m, at rest; touching cup1_bottom
11.00 s: ball1 at (-1.18, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.49, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.0°, turning -82°/s; touching domino2_support_leg_a | ball3 at (-4.58, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at 0.0°, still; touching domino2_support_top | ball4 at (-4.67, 0.12, 0.07) m, at rest; touching cup1_bottom
11.25 s: ball1 at (-1.17, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.49, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.1°, turning +18°/s; touching nothing | ball3 at (-4.58, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at 0.0°, still; touching domino2_support_top | ball4 at (-4.68, 0.12, 0.07) m, at rest; touching cup1_bottom
11.50 s: ball1 at (-1.15, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.49, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.7°, turning -53°/s; touching nothing | ball3 at (-4.59, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at 0.0°, still; touching domino2_support_top | ball4 at (-4.69, 0.12, 0.07) m, at rest; touching cup1_bottom
11.75 s: ball1 at (-1.14, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.49, 0.12, 0.54) m, at rest; touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.9°, turning +3°/s; touching nothing | ball3 at (-4.60, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.70, 0.12, 0.07) m, at rest; touching cup1_bottom
12.00 s: ball1 at (-1.13, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.46, 0.12, 0.54) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.02); touching domino1_support_top | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 22.6°, turning +20°/s; touching nothing | ball3 at (-4.60, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.71, 0.12, 0.07) m, at rest; touching cup1_bottom
12.25 s: ball1 at (-1.11, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, moving 0.15 m/s (vx +0.14, vy -0.00, vz -0.06); touching ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.3°, turning -3°/s; touching domino2_support_leg_a | ball3 at (-4.61, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.72, 0.12, 0.07) m, at rest; touching cup1_bottom
12.50 s: ball1 at (-1.10, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.3°, turning -97°/s; touching domino2_support_leg_a | ball3 at (-4.61, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at 0.0°, still; touching domino2_support_top | ball4 at (-4.73, 0.12, 0.07) m, at rest; touching cup1_bottom
12.75 s: ball1 at (-1.08, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.2°, turning -217°/s; touching nothing | ball3 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.74, 0.12, 0.07) m, at rest; touching cup1_bottom
13.00 s: ball1 at (-1.07, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.7°, turning +367°/s; touching nothing | ball3 at (-4.62, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.75, 0.12, 0.07) m, at rest; touching cup1_bottom
13.25 s: ball1 at (-1.06, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.2°, turning +149°/s; touching nothing | ball3 at (-4.63, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.76, 0.12, 0.07) m, at rest; touching cup1_bottom
13.50 s: ball1 at (-1.04, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.5°, turning -143°/s; touching domino2_support_leg_a | ball3 at (-4.63, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at 0.0°, still; touching domino2_support_top | ball4 at (-4.77, 0.12, 0.07) m, at rest; touching cup1_bottom
13.75 s: ball1 at (-1.03, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.8°, turning -15°/s; touching nothing | ball3 at (-4.64, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.78, 0.12, 0.07) m, at rest; touching cup1_bottom
14.00 s: ball1 at (-1.02, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 23.2°, turning +260°/s; touching nothing | ball3 at (-4.64, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.79, 0.12, 0.07) m, at rest; touching cup1_bottom
14.25 s: ball1 at (-1.00, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.2°, turning +5°/s; touching domino2_support_leg_a | ball3 at (-4.65, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.80, 0.12, 0.07) m, at rest; touching cup1_bottom
14.50 s: ball1 at (-0.99, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.0°, turning +22°/s; touching nothing | ball3 at (-4.66, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.81, 0.12, 0.07) m, at rest; touching cup1_bottom
14.75 s: ball1 at (-0.97, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 23.3°, turning -295°/s; touching nothing | ball3 at (-4.66, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.83, 0.12, 0.07) m, at rest; touching cup1_bottom
15.00 s: ball1 at (-0.96, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.1°, turning -95°/s; touching domino2_support_leg_a | ball3 at (-4.67, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.84, 0.12, 0.07) m, at rest; touching cup1_bottom
15.25 s: ball1 at (-0.95, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.4°, turning +66°/s; touching nothing | ball3 at (-4.67, 0.12, 0.62) m, at rest; touching shelf1_plate | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.85, 0.12, 0.07) m, at rest; touching cup1_bottom
15.50 s: ball1 at (-0.93, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.3°, turning -50°/s; touching domino2_support_leg_a | ball3 at (-4.72, 0.12, 0.59) m, moving 0.71 m/s (vx -0.33, vy -0.00, vz -0.63); touching nothing | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.86, 0.12, 0.07) m, at rest; touching cup1_bottom
15.75 s: ball1 at (-0.92, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 23.3°, turning +174°/s; touching nothing | ball3 at (-4.79, 0.12, 0.14) m, moving 1.05 m/s (vx +0.70, vy +0.00, vz -0.78); touching ball4_sphere | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.86, 0.12, 0.07) m, moving 0.26 m/s (vx -0.26, vy +0.00, vz -0.01); touching ball3_sphere, cup1_bottom
16.00 s: ball1 at (-0.91, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.7°, turning +81°/s; touching nothing | ball3 at (-4.67, 0.12, 0.07) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching cup1_bottom | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.85, 0.12, 0.07) m, at rest; touching cup1_bottom
16.25 s: ball1 at (-0.89, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 23.2°, turning +67°/s; touching nothing | ball3 at (-4.69, 0.12, 0.07) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching cup1_bottom | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.84, 0.12, 0.07) m, at rest; touching cup1_bottom
16.50 s: ball1 at (-0.88, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.6°, turning +205°/s; touching domino2_support_leg_a | ball3 at (-4.70, 0.12, 0.07) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching cup1_bottom | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.83, 0.12, 0.07) m, at rest; touching cup1_bottom
16.75 s: ball1 at (-0.86, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.7°, turning -45°/s; touching nothing | ball3 at (-4.72, 0.12, 0.07) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching cup1_bottom | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.82, 0.12, 0.07) m, at rest; touching cup1_bottom
17.00 s: ball1 at (-0.85, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 22.3°, turning -224°/s; touching nothing | ball3 at (-4.72, 0.12, 0.07) m, at rest; touching cup1_bottom | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.82, 0.12, 0.07) m, at rest; touching cup1_bottom
17.25 s: ball1 at (-0.84, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 22.5°, turning -87°/s; touching nothing | ball3 at (-4.71, 0.12, 0.07) m, at rest; touching cup1_bottom | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.82, 0.12, 0.07) m, at rest; touching cup1_bottom
17.50 s: ball1 at (-0.82, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.0°, turning +2°/s; touching nothing | ball3 at (-4.71, 0.12, 0.07) m, at rest; touching cup1_bottom | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at 0.0°, still; touching domino2_support_top | ball4 at (-4.82, 0.12, 0.07) m, at rest; touching cup1_bottom
17.75 s: ball1 at (-0.81, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.3°, turning -60°/s; touching nothing | ball3 at (-4.71, 0.12, 0.07) m, at rest; touching cup1_bottom | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.83, 0.12, 0.07) m, at rest; touching cup1_bottom
18.00 s: ball1 at (-0.79, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.2°, turning +7°/s; touching nothing | ball3 at (-4.71, 0.12, 0.07) m, at rest; touching cup1_bottom | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at 0.0°, still; touching domino2_support_top | ball4 at (-4.83, 0.12, 0.07) m, at rest; touching cup1_bottom
18.25 s: ball1 at (-0.78, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.1°, turning +63°/s; touching nothing | ball3 at (-4.70, 0.12, 0.07) m, at rest; touching cup1_bottom | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.83, 0.12, 0.07) m, at rest; touching cup1_bottom
18.50 s: ball1 at (-0.77, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.1°, still; touching domino2_support_leg_a | ball3 at (-4.70, 0.12, 0.07) m, at rest; touching cup1_bottom | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.83, 0.12, 0.07) m, at rest; touching cup1_bottom
18.75 s: ball1 at (-0.75, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.8°, turning -31°/s; touching nothing | ball3 at (-4.70, 0.12, 0.07) m, at rest; touching cup1_bottom | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.83, 0.12, 0.07) m, at rest; touching cup1_bottom
19.00 s: ball1 at (-0.74, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.5°, turning -192°/s; touching nothing | ball3 at (-4.70, 0.12, 0.07) m, at rest; touching cup1_bottom | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.84, 0.12, 0.07) m, at rest; touching cup1_bottom
19.25 s: ball1 at (-0.73, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 23.3°, turning +112°/s; touching nothing | ball3 at (-4.70, 0.12, 0.07) m, at rest; touching cup1_bottom | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.84, 0.12, 0.07) m, at rest; touching cup1_bottom
19.50 s: ball1 at (-0.71, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 25.6°, turning +146°/s; touching domino2_support_leg_a | ball3 at (-4.69, 0.12, 0.07) m, at rest; touching cup1_bottom | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at 0.0°, still; touching domino2_support_top | ball4 at (-4.84, 0.12, 0.07) m, at rest; touching cup1_bottom
19.75 s: ball1 at (-0.70, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 24.0°, turning +160°/s; touching nothing | ball3 at (-4.69, 0.12, 0.07) m, at rest; touching cup1_bottom | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.84, 0.12, 0.07) m, at rest; touching cup1_bottom
20.00 s: ball1 at (-0.68, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | lever1 at 0.6°, still; touching cart1_roller | cart1 at 0.000 m, still; touching lever1_beam | domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top | ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate | door1 at 30.1°, still; touching floor | pendulum1 at 0.0°, still; touching nothing | block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | seesaw1 at 22.1°, turning -106°/s; touching nothing | ball3 at (-4.69, 0.12, 0.07) m, at rest; touching cup1_bottom | domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top | flap1 at -0.0°, still; touching domino2_support_top | ball4 at (-4.85, 0.12, 0.07) m, at rest; touching cup1_bottom

At the end (20.00 s):
- ball1 at (-0.68, -0.02, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor
- lever1 at 0.6°, still; touching cart1_roller
- cart1 at 0.000 m, still; touching lever1_beam
- domino1 at (-0.37, 0.12, 0.61) m, at rest; touching domino1_support_top
- ball2 at (-0.47, 0.12, 0.54) m, at rest; touching domino1_support_top, ramp1_entry_plate
- door1 at 30.1°, still; touching floor
- pendulum1 at 0.0°, still; touching nothing
- block1 at (-2.38, 0.12, 0.06) m, at rest; touching floor
- cart2 at 0.000 m, still; touching nothing
- seesaw1 at 22.1°, turning -106°/s; touching nothing
- ball3 at (-4.69, 0.12, 0.07) m, at rest; touching cup1_bottom
- domino2 at (-4.05, 0.12, 0.54) m, at rest; touching domino2_support_top
- flap1 at -0.0°, still; touching domino2_support_top
- ball4 at (-4.85, 0.12, 0.07) m, at rest; touching cup1_bottom

Openings (fixed rings, open through the middle; height is the middle of the whole thing), and each loose thing that comes down through one's height:
ring1: an opening 0.20 m across, centre (-0.26, -0.02, 0.85) m
- ball1 comes down through ring1's height at 0.25 s, 0.00 m from its centre: through it
- ball3 comes down through ring1's height at 7.94 s, 4.02 m from its centre: outside it, missing by 3.92 m (down through that height 2 times; this is the closest)
ball3_launch_guide: an opening 0.14 m across, centre (-4.08, 0.12, 1.60) m
- nothing loose comes down through ball3_launch_guide's height
ring2: an opening 0.20 m across, centre (-4.08, 0.12, 0.90) m
- ball1 comes down through ring2's height at 0.23 s, 3.83 m from its centre: outside it, missing by 3.73 m
- ball3 comes down through ring2's height at 7.92 s, 0.19 m from its centre: outside it, missing by 0.09 m
cup1_catch_guide: an opening 0.32 m across, centre (-4.77, 0.12, 0.54) m
- ball1 comes down through cup1_catch_guide's height at 1.36 s, 4.40 m from its centre: outside it, missing by 4.24 m
- ball3 comes down through cup1_catch_guide's height at 15.56 s, 0.03 m from its centre: through it
- ball4 comes down through cup1_catch_guide's height at 9.07 s, 0.03 m from its centre: through it
</history>


The debugger, another agent that can run your scene and try changes, looked into the first link that fails. Its
report, which you may use or disagree with:

<debugger>
First failure: cart1 never reaches domino1 because the lever–cart contact jams almost immediately.

Evidence from the original run:
- Ball1 hits lever1 at 0.32 s.
- Lever1 contacts cart1’s roller at 0.33 s, at only about 1° of rotation.
- Cart1 remains at slide displacement 0.000 m throughout the observed motion.
- Lever1 rebounds to 0° at 0.35 s, then settles near 1°. The reported link-3 success is this return to the initial stop, not the required 45° swing.

The fault is contact placement, not insufficient cart travel or incorrect mass. Cart1’s box overlaps the beam’s lateral sweep, and its roller sits immediately above the nearly horizontal beam. This makes an early, predominantly upward contact against a cart constrained to move horizontally, obstructing the lever before it can deliver a useful leftward strike.

Recommended edits, tested together:
- Line 65: pos="0.18 0.075 0.665"
        → pos="0.18 0.145 0.665"
- Line 68: pos="0.115 -0.075 -0.050"
        → pos="0.050 -0.145 0.100"
- Line 52: axis="0 -1 0" → axis="0 1 0"
           range="0 0.785398163" → range="-0.785398163 0"

The placement changes put the cart box 5 mm outside the beam’s width and move the roller’s initial world center to (0.230, 0, 0.765). The lever can therefore rise before engaging the roller rather than jamming near horizontal.

The axis/range reversal preserves the same physical direction and 45° sweep, but makes the destination the lower joint stop, as requested. It does not change the physical motion or add initial velocity.

Checked result:
- The placement-only trial made link 4 hold without losing links 1–3.
- The full recommended trial, including the axis/range correction, also held links 1–4.
- Links 5–16 remain broken; the first break advances to link 5, “domino1 touches ball2.” This is not a complete-chain repair.

No specified dimensions, masses, spacing, travel, damping, friction, gravity, or swing magnitude are changed.
</debugger>


Does the world do what the brief says? First describe what happens in the run. Then end your reply with a ```json block
holding one object:

{"what_happens": "<what happens in the run>", "works": <true or false>, "problem": "<one sentence, or empty>"}

If it does not work, also reply with the complete corrected file in one ```xml block, keeping the names the
brief needs. If it works, no file is needed.
