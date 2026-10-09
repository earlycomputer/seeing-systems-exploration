Write a MuJoCo MJCF scene for this brief:

<brief>
Use gravity 9.81 m/s2, contact friction 0.70, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, loose blocks are 0.12 m cubes and 0.35 kg, fixed ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Ball1 starts at the high end of ramp1, whose low end is 0.15 m above the floor, and rolls down to touch domino1 after a 0.10 m exit gap. Domino1 then topples across a 0.18 m center spacing and touches domino2. Domino2 topples 0.18 m into the lower half of flap1, a 0.40 by 0.20 by 0.04 m, 0.30 kg hinged panel, making it swing clockwise through 65 degrees to its hard stop and knock cart1. Cart1 then slides 0.45 m along its horizontal slide and touches ball2, which rests at the high end of ramp2 with its low end 0.15 m above the floor. Ball2 rolls down ramp2 and crosses a 0.12 m gap before touching the left end of lever1, a 0.60 by 0.10 by 0.04 m, 0.50 kg center-hinged lever carrying ball3 on its right end. Lever1 rotates clockwise through 45 degrees until its left end reaches the lower stop, and its rising right end launches ball3 vertically. Ball3 rises and then falls through ring1, centered 0.35 m below its initial center. After another 0.25 m fall, ball3 touches the bob of pendulum1, a 0.50 m long, 0.35 kg rigid pendulum hanging vertically. Pendulum1 swings clockwise through 40 degrees and its bob touches domino3 after a 0.32 m arc. Domino3 topples across a 0.18 m gap into door1, a 0.42 by 0.32 by 0.04 m, 0.45 kg panel, making door1 swing clockwise through 70 degrees to its hard stop and knock block1. Block1 slides 0.35 m across the floor and touches cart2 on its horizontal slide. Cart2 slides 0.42 m and touches ball4 at the high end of ramp3, whose low end is 0.15 m above the floor. Ball4 rolls down ramp3 and crosses a 0.10 m gap before touching flap2, a 0.38 by 0.18 by 0.04 m, 0.28 kg hinged panel. Flap2 swings clockwise through 60 degrees to its hard stop and knocks ball5 from shelf1, a fixed 0.30 by 0.25 by 0.04 m shelf 0.80 m above the floor. Ball5 falls 0.30 m and drops through ring2 beneath the shelf edge. Ball5 then falls 0.35 m into bin1, whose inner footprint is 0.32 by 0.32 m with 0.20 m high and 0.02 m thick walls, and comes to rest there.
</brief>

MuJoCo will load the file, reset to the keyframe named `start` if there is one, and simulate it for
20 s. Nothing else acts on the scene: whatever moves must be set moving by the scene itself, for
example by a keyframe velocity, a spring, gravity, or a motor whose control the keyframe sets (controls keep
their keyframe values for the whole run).

A few conventions so the other tools can find things. They fix names and axes, not what you build:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- Name each thing's body exactly: `ball1` (starting ramp ball: a body with a `<freejoint/>`); `ramp1` (first inclined ramp: fixed in place; all its geoms belong to one body); `domino1` (first upright domino: a body with a `<freejoint/>`); `domino2` (second upright domino: a body with a `<freejoint/>`); `flap1` (clockwise striking flap: a body on a hinge joint); `cart1` (first slide cart: a body on a slide joint); `ball2` (second ramp ball: a body with a `<freejoint/>`); `ramp2` (second inclined ramp: fixed in place; all its geoms belong to one body); `lever1` (ball launching lever: a body on a hinge joint); `ball3` (first falling ball: a body with a `<freejoint/>`); `ring1` (first horizontal ring: fixed in place; all its geoms belong to one body); `pendulum1` (impact pendulum: a body on a hinge joint); `domino3` (third upright domino: a body with a `<freejoint/>`); `door1` (clockwise hinged door: a body on a hinge joint); `block1` (door struck block: a body with a `<freejoint/>`); `cart2` (second slide cart: a body on a slide joint); `ball4` (third ramp ball: a body with a `<freejoint/>`); `ramp3` (third inclined ramp: fixed in place; all its geoms belong to one body); `flap2` (second striking flap: a body on a hinge joint); `ball5` (final falling ball: a body with a `<freejoint/>`); `shelf1` (ball support shelf: fixed in place; all its geoms belong to one body); `ring2` (second horizontal ring: fixed in place; all its geoms belong to one body); `bin1` (final catch bin: fixed in place; all its geoms belong to one body). Its geoms may be named with the body's name as a prefix (`ball1_...`).
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures,
  `<default>` classes or `<include>`.
- Give every body and geom a name, and write each element's attributes on a single line.
- Set `<option timestep="0.002"/>`.

Reply with the complete file in one ```xml code block. A sentence or two before the block is fine.

A ball counts as at rest when it moves slower than 5 cm/s at the end.


You wrote this file:

```xml
<mujoco model="passive_chain_reaction_revised">
  <compiler angle="radian" autolimits="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="100" tolerance="1e-9" cone="elliptic"/>
  <size njmax="3000" nconmax="1000"/>

  <!-- Contact damping approximates restitution 0.05; sliding friction is 0.70. -->
  <default>
    <geom friction="0.70 0 0" condim="3" solref="0.010 0.690107" solimp="0.95 0.99 0.001 0.5 2"/>
    <joint armature="0" solreflimit="0.006 1" solimplimit="0.99 0.999 0.001 0.5 2"/>
  </default>

  <visual>
    <global azimuth="110" elevation="-20"/>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.65 0.65 0.65" specular="0.15 0.15 0.15"/>
    <rgba haze="0.85 0.90 0.95 1"/>
  </visual>

  <worldbody>
    <light name="main_light" pos="3.5 -3 7" dir="0 0 -1" directional="true"/>
    <camera name="overview" pos="4 -8 5" xyaxes="1 0 0 0 0.447214 0.894427"/>
    <geom name="floor" type="plane" size="12 6 0.1" friction="0.70 0.005 0.002" condim="6" priority="1" rgba="0.82 0.84 0.86 1"/>

    <body name="ramp1" pos="0.463006 0 0.302216" euler="0 0.3490658504 0">
      <geom name="ramp1_surface" type="box" size="0.50 0.15 0.02" rgba="0.42 0.47 0.55 1"/>
      <geom name="ramp1_left_rail" type="capsule" fromto="-0.48 -0.158 0.045 0.48 -0.158 0.045" size="0.01" rgba="0.25 0.30 0.38 1"/>
      <geom name="ramp1_right_rail" type="capsule" fromto="-0.48 0.158 0.045 0.48 0.158 0.045" size="0.01" rgba="0.25 0.30 0.38 1"/>
    </body>

    <body name="ball1" pos="0.064086 0 0.521904">
      <freejoint name="ball1_free"/>
      <geom name="ball1_sphere" type="sphere" size="0.05" mass="0.20" rgba="0.95 0.25 0.12 1"/>
    </body>

    <body name="domino1" pos="1.0796926 0 0.12">
      <freejoint name="domino1_free"/>
      <geom name="domino1_box" type="box" size="0.04 0.02 0.12" mass="0.25" rgba="0.96 0.72 0.18 1"/>
    </body>

    <body name="domino2" pos="1.2596926 0 0.12">
      <freejoint name="domino2_free"/>
      <geom name="domino2_box" type="box" size="0.04 0.02 0.12" mass="0.25" rgba="0.96 0.72 0.18 1"/>
    </body>

    <body name="flap1" pos="1.4396926 0 0.02">
      <joint name="flap1_hinge" type="hinge" axis="0 1 0" damping="0.04" limited="true" range="0 1.1344640138"/>
      <geom name="flap1_panel" type="box" pos="0 0 0.20" size="0.02 0.10 0.20" mass="0.30" rgba="0.20 0.55 0.80 1"/>
      <site name="flap1_spring_tip" pos="0 0 0.40" size="0.005" rgba="0.25 0.25 0.25 1"/>
    </body>

    <body name="flap1_spring_mount" pos="1.4396926 0 -0.30">
      <site name="flap1_spring_anchor" pos="0 0 0" size="0.005" rgba="0.25 0.25 0.25 1"/>
    </body>

    <!-- The freely rotating rear roller prevents the inclined flap/cart contact from self-locking. -->
    <!-- Cart box plus roller mass is 0.50 kg. -->
    <body name="cart1" pos="1.81 0 0.15">
      <joint name="cart1_slide" type="slide" axis="1 0 0" damping="0.20" limited="true" range="0 0.45"/>
      <geom name="cart1_box" type="box" size="0.11 0.09 0.05" mass="0.49" rgba="0.18 0.65 0.45 1"/>
      <geom name="cart1_pushrod" type="capsule" fromto="0.11 0.20 0.03 0.11 0.20 0.374245" size="0.008" mass="0" rgba="0.18 0.65 0.45 1"/>
      <geom name="cart1_striker" type="capsule" fromto="0.11 -0.035 0.374245 0.11 0.20 0.374245" size="0.012" mass="0" rgba="0.18 0.65 0.45 1"/>
      <geom name="cart1_pushrod_brace" type="capsule" fromto="0.075 0.075 0.025 0.11 0.20 0.03" size="0.008" mass="0" rgba="0.18 0.65 0.45 1"/>
      <body name="cart1_contact_roller" pos="-0.135 0 0.05">
        <joint name="cart1_contact_roller_joint" type="ball" damping="0"/>
        <geom name="cart1_contact_roller_sphere" type="sphere" size="0.025" mass="0.01" rgba="0.40 0.43 0.47 1"/>
      </body>
    </body>

    <body name="ramp2" pos="2.837356 0 0.302216" euler="0 0.3490658504 0">
      <geom name="ramp2_surface" type="box" size="0.50 0.15 0.02" rgba="0.42 0.47 0.55 1"/>
      <geom name="ramp2_left_rail" type="capsule" fromto="-0.48 -0.158 0.045 0.48 -0.158 0.045" size="0.01" rgba="0.25 0.30 0.38 1"/>
      <geom name="ramp2_right_rail" type="capsule" fromto="-0.48 0.158 0.045 0.48 0.158 0.045" size="0.01" rgba="0.25 0.30 0.38 1"/>
      <geom name="ramp2_release_lip" type="capsule" fromto="-0.405 -0.13 0.036 -0.405 0.13 0.036" size="0.012" rgba="0.30 0.35 0.43 1"/>
    </body>

    <body name="ball2" pos="2.432 0 0.524245">
      <freejoint name="ball2_free"/>
      <geom name="ball2_sphere" type="sphere" size="0.05" mass="0.20" rgba="0.95 0.25 0.12 1"/>
    </body>

    <body name="lever1" pos="3.649844 0 0.398398" euler="0 -0.7679448709 0">
      <joint name="lever1_hinge" type="hinge" axis="0 -1 0" damping="0.04" stiffness="2.0" springref="1.20" limited="true" range="0 0.7853981634"/>
      <geom name="lever1_beam" type="box" size="0.30 0.05 0.02" mass="0.50" rgba="0.65 0.35 0.75 1"/>
      <geom name="lever1_ball_tray" type="box" pos="0.327786 0 0.028774" euler="0 0.7679448709 0" size="0.065 0.065 0.01" mass="0" rgba="0.65 0.35 0.75 1"/>
      <geom name="lever1_latch_pad" type="box" pos="-0.317366 0 -0.017984" euler="0 0.7679448709 0" size="0.04 0.055 0.005" mass="0" rgba="0.45 0.22 0.55 1"/>
    </body>

    <!-- Breakaway friction holds the latch until impact; its trigger and links remain below the lever pad. -->
    <body name="lever_latch" pos="3.434042 0 0.145">
      <joint name="lever_latch_slide" type="slide" axis="1 0 0" damping="0.20" frictionloss="0.30" limited="true" range="0 0.18"/>
      <geom name="lever_latch_trigger" type="box" pos="-0.065 0 -0.02" size="0.015 0.055 0.02" mass="0.025" rgba="0.35 0.38 0.42 1"/>
      <geom name="lever_latch_link" type="capsule" fromto="0 0.075 0 -0.065 0.075 -0.02" size="0.006" mass="0" rgba="0.35 0.38 0.42 1"/>
      <geom name="lever_latch_lower_crosspiece" type="capsule" fromto="0 0 0 0 0.075 0" size="0.006" mass="0" rgba="0.35 0.38 0.42 1"/>
      <geom name="lever_latch_upper_crosspiece" type="capsule" fromto="-0.065 0 -0.02 -0.065 0.075 -0.02" size="0.006" mass="0" rgba="0.35 0.38 0.42 1"/>
      <body name="lever_latch_roller" pos="0 0 0">
        <joint name="lever_latch_roller_joint" type="ball" damping="0"/>
        <geom name="lever_latch_roller_sphere" type="sphere" size="0.015" mass="0.005" rgba="0.60 0.63 0.68 1"/>
      </body>
    </body>

    <body name="ball3" pos="3.865646 0 0.706796">
      <freejoint name="ball3_free"/>
      <geom name="ball3_sphere" type="sphere" size="0.05" mass="0.20" contype="2" conaffinity="3" rgba="0.95 0.25 0.12 1"/>
    </body>

    <body name="launch_guide" pos="3.865646 0 0">
      <geom name="launch_guide_left" type="capsule" fromto="-0.057 0 0.50 -0.057 0 1.60" size="0.005" contype="2" conaffinity="2" rgba="0.55 0.65 0.75 0.35"/>
      <geom name="launch_guide_right" type="capsule" fromto="0.057 0 0.50 0.057 0 1.60" size="0.005" contype="2" conaffinity="2" rgba="0.55 0.65 0.75 0.35"/>
      <geom name="launch_guide_front" type="capsule" fromto="0 -0.057 0.50 0 -0.057 1.60" size="0.005" contype="2" conaffinity="2" rgba="0.55 0.65 0.75 0.35"/>
      <geom name="launch_guide_back" type="capsule" fromto="0 0.057 0.50 0 0.057 1.60" size="0.005" contype="2" conaffinity="2" rgba="0.55 0.65 0.75 0.35"/>
    </body>

    <body name="ring1" pos="3.865646 0 0.356796">
      <geom name="ring1_segment01" type="capsule" fromto="0.089724 0 0 0.082894 0.034336 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring1_segment02" type="capsule" fromto="0.082894 0.034336 0 0.063444 0.063444 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring1_segment03" type="capsule" fromto="0.063444 0.063444 0 0.034336 0.082894 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring1_segment04" type="capsule" fromto="0.034336 0.082894 0 0 0.089724 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring1_segment05" type="capsule" fromto="0 0.089724 0 -0.034336 0.082894 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring1_segment06" type="capsule" fromto="-0.034336 0.082894 0 -0.063444 0.063444 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring1_segment07" type="capsule" fromto="-0.063444 0.063444 0 -0.082894 0.034336 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring1_segment08" type="capsule" fromto="-0.082894 0.034336 0 -0.089724 0 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring1_segment09" type="capsule" fromto="-0.089724 0 0 -0.082894 -0.034336 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring1_segment10" type="capsule" fromto="-0.082894 -0.034336 0 -0.063444 -0.063444 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring1_segment11" type="capsule" fromto="-0.063444 -0.063444 0 -0.034336 -0.082894 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring1_segment12" type="capsule" fromto="-0.034336 -0.082894 0 0 -0.089724 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring1_segment13" type="capsule" fromto="0 -0.089724 0 0.034336 -0.082894 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring1_segment14" type="capsule" fromto="0.034336 -0.082894 0 0.063444 -0.063444 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring1_segment15" type="capsule" fromto="0.063444 -0.063444 0 0.082894 -0.034336 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring1_segment16" type="capsule" fromto="0.082894 -0.034336 0 0.089724 0 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
    </body>

    <body name="pendulum1" pos="3.935646 0 0.550227">
      <joint name="pendulum1_hinge" type="hinge" axis="0 -1 0" damping="0.04" limited="true" range="0 0.6981317008"/>
      <geom name="pendulum1_rod" type="capsule" fromto="0 0.13 -0.01 0 0.13 -0.46" size="0.008" mass="0.05" rgba="0.32 0.36 0.42 1"/>
      <geom name="pendulum1_upper_yoke" type="capsule" fromto="0 0 0 0 0.13 0" size="0.006" mass="0" rgba="0.32 0.36 0.42 1"/>
      <geom name="pendulum1_lower_yoke" type="capsule" fromto="0 0.13 -0.46 0 0 -0.46" size="0.006" mass="0" rgba="0.32 0.36 0.42 1"/>
      <geom name="pendulum1_bob" type="sphere" pos="0 0 -0.50" size="0.04" mass="0.30" rgba="0.25 0.28 0.33 1"/>
      <site name="pendulum1_spring_bob" pos="0 0 -0.50" size="0.005" rgba="0.25 0.25 0.25 1"/>
    </body>

    <body name="pendulum_spring_mount" pos="3.935646 0 0.850227">
      <site name="pendulum_spring_anchor" pos="0 0 0" size="0.005" rgba="0.25 0.25 0.25 1"/>
    </body>

    <body name="domino3" pos="4.314244 0 0.12">
      <freejoint name="domino3_free"/>
      <geom name="domino3_box" type="box" size="0.04 0.02 0.12" mass="0.25" rgba="0.96 0.72 0.18 1"/>
    </body>

    <!-- The door now swings clockwise about a vertical side hinge, avoiding a downward wedging force on block1. -->
    <body name="door1" pos="4.554244 -0.16 0.02">
      <joint name="door1_hinge" type="hinge" axis="0 0 -1" damping="0.04" limited="true" range="0 1.2217304764"/>
      <geom name="door1_panel" type="box" pos="0 0.16 0.21" size="0.02 0.16 0.21" mass="0.45" rgba="0.20 0.55 0.80 1"/>
      <geom name="door1_block_striker" type="sphere" pos="0 0.32 0.04" size="0.025" mass="0" rgba="0.20 0.55 0.80 1"/>
      <site name="door1_spring_tip" pos="0 0.32 0.21" size="0.005" rgba="0.25 0.25 0.25 1"/>
    </body>

    <body name="door_spring_mount" pos="4.554244 -0.46 0.23">
      <site name="door_spring_anchor" pos="0 0 0" size="0.005" rgba="0.25 0.25 0.25 1"/>
    </body>

    <body name="block1" pos="4.884244 0 0.06">
      <freejoint name="block1_free"/>
      <geom name="block1_cube" type="box" size="0.06 0.06 0.06" mass="0.35" rgba="0.72 0.42 0.22 1"/>
    </body>

    <body name="cart2" pos="5.404244 0 0.13">
      <joint name="cart2_slide" type="slide" axis="1 0 0" damping="0.20" limited="true" range="0 0.42"/>
      <geom name="cart2_box" type="box" size="0.11 0.09 0.05" mass="0.50" rgba="0.18 0.65 0.45 1"/>
      <geom name="cart2_pushrod" type="capsule" fromto="0.11 0.20 0.03 0.11 0.20 0.394245" size="0.008" mass="0" rgba="0.18 0.65 0.45 1"/>
      <geom name="cart2_striker" type="capsule" fromto="0.11 -0.035 0.394245 0.11 0.20 0.394245" size="0.012" mass="0" rgba="0.18 0.65 0.45 1"/>
      <geom name="cart2_pushrod_brace" type="capsule" fromto="0.075 0.075 0.025 0.11 0.20 0.03" size="0.008" mass="0" rgba="0.18 0.65 0.45 1"/>
    </body>

    <body name="ramp3" pos="6.401600 0 0.302216" euler="0 0.3490658504 0">
      <geom name="ramp3_surface" type="box" size="0.50 0.15 0.02" rgba="0.42 0.47 0.55 1"/>
      <geom name="ramp3_left_rail" type="capsule" fromto="-0.48 -0.158 0.045 0.48 -0.158 0.045" size="0.01" rgba="0.25 0.30 0.38 1"/>
      <geom name="ramp3_right_rail" type="capsule" fromto="-0.48 0.158 0.045 0.48 0.158 0.045" size="0.01" rgba="0.25 0.30 0.38 1"/>
      <geom name="ramp3_release_lip" type="capsule" fromto="-0.405 -0.13 0.036 -0.405 0.13 0.036" size="0.012" rgba="0.30 0.35 0.43 1"/>
    </body>

    <body name="ball4" pos="5.996244 0 0.524245">
      <freejoint name="ball4_free"/>
      <geom name="ball4_sphere" type="sphere" size="0.05" mass="0.20" rgba="0.95 0.25 0.12 1"/>
    </body>

    <body name="flap2" pos="6.978287 0 0.02">
      <joint name="flap2_hinge" type="hinge" axis="0 1 0" damping="0.04" limited="true" range="0 1.0471975512"/>
      <geom name="flap2_panel" type="box" pos="0 0 0.19" size="0.02 0.09 0.19" mass="0.28" rgba="0.20 0.55 0.80 1"/>
      <geom name="flap2_arm_crosspiece" type="capsule" fromto="0 0 0.36 0 0.12 0.36" size="0.008" mass="0" rgba="0.20 0.55 0.80 1"/>
      <geom name="flap2_shelf_arm" type="capsule" fromto="0 0.12 0.36 -0.551480 0.12 0.664808" size="0.008" mass="0" rgba="0.20 0.55 0.80 1"/>
      <geom name="flap2_ball_striker" type="capsule" fromto="-0.551480 -0.04 0.664808 -0.551480 0.12 0.664808" size="0.012" mass="0" rgba="0.20 0.55 0.80 1"/>
      <site name="flap2_spring_tip" pos="0 0 0.38" size="0.005" rgba="0.25 0.25 0.25 1"/>
    </body>

    <body name="flap2_spring_mount" pos="6.978287 0 -0.30">
      <site name="flap2_spring_anchor" pos="0 0 0" size="0.005" rgba="0.25 0.25 0.25 1"/>
    </body>

    <body name="shelf1" pos="7.19 0 0.78">
      <geom name="shelf1_surface" type="box" size="0.15 0.125 0.02" rgba="0.50 0.40 0.30 1"/>
      <geom name="shelf1_leg_left" type="box" pos="-0.10 -0.10 -0.38" size="0.015 0.015 0.38" rgba="0.40 0.32 0.24 1"/>
      <geom name="shelf1_leg_right" type="box" pos="-0.10 0.10 -0.38" size="0.015 0.015 0.38" rgba="0.40 0.32 0.24 1"/>
    </body>

    <body name="ball5" pos="7.325 0 0.85">
      <freejoint name="ball5_free"/>
      <geom name="ball5_sphere" type="sphere" size="0.05" mass="0.20" contype="4" conaffinity="5" rgba="0.95 0.25 0.12 1"/>
    </body>

    <body name="final_drop_guide" pos="7.37 0 0">
      <geom name="final_drop_guide_left" type="capsule" fromto="-0.057 0 0.30 -0.057 0 0.77" size="0.005" contype="4" conaffinity="4" rgba="0.55 0.65 0.75 0.35"/>
      <geom name="final_drop_guide_right" type="capsule" fromto="0.057 0 0.30 0.057 0 0.77" size="0.005" contype="4" conaffinity="4" rgba="0.55 0.65 0.75 0.35"/>
      <geom name="final_drop_guide_front" type="capsule" fromto="0 -0.057 0.30 0 -0.057 0.77" size="0.005" contype="4" conaffinity="4" rgba="0.55 0.65 0.75 0.35"/>
      <geom name="final_drop_guide_back" type="capsule" fromto="0 0.057 0.30 0 0.057 0.77" size="0.005" contype="4" conaffinity="4" rgba="0.55 0.65 0.75 0.35"/>
    </body>

    <body name="ring2" pos="7.37 0 0.55">
      <geom name="ring2_segment01" type="capsule" fromto="0.089724 0 0 0.082894 0.034336 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring2_segment02" type="capsule" fromto="0.082894 0.034336 0 0.063444 0.063444 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring2_segment03" type="capsule" fromto="0.063444 0.063444 0 0.034336 0.082894 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring2_segment04" type="capsule" fromto="0.034336 0.082894 0 0 0.089724 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring2_segment05" type="capsule" fromto="0 0.089724 0 -0.034336 0.082894 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring2_segment06" type="capsule" fromto="-0.034336 0.082894 0 -0.063444 0.063444 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring2_segment07" type="capsule" fromto="-0.063444 0.063444 0 -0.082894 0.034336 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring2_segment08" type="capsule" fromto="-0.082894 0.034336 0 -0.089724 0 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring2_segment09" type="capsule" fromto="-0.089724 0 0 -0.082894 -0.034336 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring2_segment10" type="capsule" fromto="-0.082894 -0.034336 0 -0.063444 -0.063444 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring2_segment11" type="capsule" fromto="-0.063444 -0.063444 0 -0.034336 -0.082894 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring2_segment12" type="capsule" fromto="-0.034336 -0.082894 0 0 -0.089724 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring2_segment13" type="capsule" fromto="0 -0.089724 0 0.034336 -0.082894 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring2_segment14" type="capsule" fromto="0.034336 -0.082894 0 0.063444 -0.063444 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring2_segment15" type="capsule" fromto="0.063444 -0.063444 0 0.082894 -0.034336 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
      <geom name="ring2_segment16" type="capsule" fromto="0.082894 -0.034336 0 0.089724 0 0" size="0.008" rgba="0.90 0.65 0.10 1"/>
    </body>

    <body name="bin1" pos="7.37 0 0">
      <geom name="bin1_base" type="box" pos="0 0 0.14" size="0.18 0.18 0.01" friction="0.70 0.005 0.002" condim="6" priority="1" rgba="0.30 0.48 0.65 1"/>
      <geom name="bin1_wall_left" type="box" pos="-0.17 0 0.25" size="0.01 0.18 0.10" rgba="0.30 0.48 0.65 1"/>
      <geom name="bin1_wall_right" type="box" pos="0.17 0 0.25" size="0.01 0.18 0.10" rgba="0.30 0.48 0.65 1"/>
      <geom name="bin1_wall_front" type="box" pos="0 -0.17 0.25" size="0.16 0.01 0.10" rgba="0.30 0.48 0.65 1"/>
      <geom name="bin1_wall_back" type="box" pos="0 0.17 0.25" size="0.16 0.01 0.10" rgba="0.30 0.48 0.65 1"/>
      <geom name="bin1_support" type="box" pos="0 0 0.065" size="0.14 0.14 0.065" rgba="0.24 0.38 0.52 1"/>
    </body>
  </worldbody>

  <!-- Each assist spring has zero joint moment in its exact initial configuration. -->
  <tendon>
    <spatial name="flap1_assist_spring" stiffness="8" damping="0" springlength="0.42" width="0.003" rgba="0.30 0.30 0.30 0.5">
      <site site="flap1_spring_anchor"/>
      <site site="flap1_spring_tip"/>
    </spatial>
    <spatial name="pendulum1_assist_spring" stiffness="40" damping="0" springlength="0.40" width="0.003" rgba="0.30 0.30 0.30 0.5">
      <site site="pendulum_spring_anchor"/>
      <site site="pendulum1_spring_bob"/>
    </spatial>
    <spatial name="door1_assist_spring" stiffness="200" damping="0" springlength="0.30" width="0.003" rgba="0.30 0.30 0.30 0.5">
      <site site="door_spring_anchor"/>
      <site site="door1_spring_tip"/>
    </spatial>
    <spatial name="flap2_assist_spring" stiffness="8" damping="0" springlength="0.40" width="0.003" rgba="0.30 0.30 0.30 0.5">
      <site site="flap2_spring_anchor"/>
      <site site="flap2_spring_tip"/>
    </spatial>
  </tendon>

  <!-- Default keyframe positions are qpos0; all initial velocities are zero. -->
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
- ball1: free body; its geoms: ball1_sphere; starts at (0.06, 0.00, 0.52) m, at rest
- domino1: free body; its geoms: domino1_box; starts at (1.08, 0.00, 0.12) m, at rest
- domino2: free body; its geoms: domino2_box; starts at (1.26, 0.00, 0.12) m, at rest
- flap1: hinge joint flap1_hinge about axis (0.00, 1.00, 0.00), range 0° to 65° as MuJoCo applies it; its geoms: flap1_panel; starts at 0.0°, still
- cart1: slide joint cart1_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.45 m as MuJoCo applies it; its geoms: cart1_box, cart1_pushrod, cart1_striker, cart1_pushrod_brace; starts at 0.000 m, still
- cart1_contact_roller: ball joint cart1_contact_roller_joint about axis (0.00, 0.00, 1.00); its geoms: cart1_contact_roller_sphere; starts (ball joint)
- ball2: free body; its geoms: ball2_sphere; starts at (2.43, 0.00, 0.52) m, at rest
- lever1: hinge joint lever1_hinge about axis (0.00, -1.00, 0.00), range 0° to 45° as MuJoCo applies it; its geoms: lever1_beam, lever1_ball_tray, lever1_latch_pad; starts at 0.0°, still
- lever_latch: slide joint lever_latch_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.18 m as MuJoCo applies it; its geoms: lever_latch_trigger, lever_latch_link, lever_latch_lower_crosspiece, lever_latch_upper_crosspiece; starts at 0.000 m, still
- lever_latch_roller: ball joint lever_latch_roller_joint about axis (0.00, 0.00, 1.00); its geoms: lever_latch_roller_sphere; starts (ball joint)
- ball3: free body; its geoms: ball3_sphere; starts at (3.87, 0.00, 0.71) m, at rest
- pendulum1: hinge joint pendulum1_hinge about axis (0.00, -1.00, 0.00), range 0° to 40° as MuJoCo applies it; its geoms: pendulum1_rod, pendulum1_upper_yoke, pendulum1_lower_yoke, pendulum1_bob; starts at 0.0°, still
- domino3: free body; its geoms: domino3_box; starts at (4.31, 0.00, 0.12) m, at rest
- door1: hinge joint door1_hinge about axis (0.00, 0.00, -1.00), range 0° to 70° as MuJoCo applies it; its geoms: door1_panel, door1_block_striker; starts at 0.0°, still
- block1: free body; its geoms: block1_cube; starts at (4.88, 0.00, 0.06) m, at rest
- cart2: slide joint cart2_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.42 m as MuJoCo applies it; its geoms: cart2_box, cart2_pushrod, cart2_striker, cart2_pushrod_brace; starts at 0.000 m, still
- ball4: free body; its geoms: ball4_sphere; starts at (6.00, 0.00, 0.52) m, at rest
- flap2: hinge joint flap2_hinge about axis (0.00, 1.00, 0.00), range 0° to 60° as MuJoCo applies it; its geoms: flap2_panel, flap2_arm_crosspiece, flap2_shelf_arm, flap2_ball_striker; starts at 0.0°, still
- ball5: free body; its geoms: ball5_sphere; starts at (7.33, 0.00, 0.85) m, at rest

What happened, in order:
 0.00 s  ball2_sphere starts touching ramp2_surface
 0.00 s  ball5_sphere starts touching shelf1_surface
 0.00 s  block1_cube starts touching floor
 0.00 s  domino3_box starts touching floor
 0.00 s  domino2_box starts touching floor
 0.00 s  ball4_sphere starts touching ramp3_surface
 0.00 s  domino1_box starts touching floor
 0.00 s  flap1 starts at its 0° stop (the end where it sits higher)
 0.00 s  cart1 starts at its lower stop (0 m)
 0.00 s  lever1 starts at its 0° stop (neither end sits lower)
 0.00 s  lever_latch starts at its lower stop (0 m)
 0.00 s  pendulum1 starts at its 0° stop (the end where it sits lower)
 0.00 s  pendulum1 is at its largest at the start, 0.0°
 0.00 s  door1 starts at its 0° stop (neither end sits lower)
 0.00 s  door1 is at its largest at the start, 0.0°
 0.00 s  cart2 starts at its lower stop (0 m)
 0.00 s  cart2 is at its largest at the start, 0.0 m
 0.00 s  flap2 starts at its 0° stop (the end where it sits higher)
 0.00 s  flap2 is at its largest at the start, 0.0°
 0.00 s  lever1_ball_tray first touches ball3_sphere
 0.00 s  ball1_sphere first touches ramp1_surface
 0.00 s  lever1_latch_pad first touches lever_latch_roller_sphere
 0.00 s  ball4_sphere first touches ramp3_release_lip
 0.00 s  ball2_sphere first touches ramp2_release_lip
 0.01 s  lever1 is at its largest, 0.1°
 0.02 s  ball1 starts moving
 0.73 s  ball3_sphere first touches launch_guide_left
 0.75 s  ball3_sphere leaves launch_guide_left
 0.89 s  ball1_sphere leaves ramp1_surface
 0.91 s  ball1_sphere first touches domino1_box
 0.91 s  domino1 starts moving
 0.92 s  ball1_sphere leaves domino1_box
 0.99 s  domino1_box first touches domino2_box
 0.99 s  domino2 starts moving
 0.99 s  ball1_sphere touches domino1_box again
 1.00 s  ball1 passes 0.12 m from domino2 (domino2_box) without touching it: nearest points (1.10, 0.00, 0.14) m and (1.22, 0.00, 0.14) m
 1.01 s  domino1_box leaves domino2_box
 1.03 s  ball1 passes 0.31 m from flap1 (flap1_panel) without touching it: nearest points (1.11, 0.00, 0.13) m and (1.42, 0.00, 0.13) m
 1.05 s  domino1_box touches domino2_box again
 1.05 s  domino1_box leaves domino2_box
 1.09 s  domino1_box touches domino2_box again
 1.09 s  domino1_box leaves domino2_box
 1.11 s  ball1_sphere leaves domino1_box
 1.12 s  domino1_box touches domino2_box again
 1.14 s  ball1_sphere first touches floor
 1.15 s  ball3_sphere touches launch_guide_left again
 1.16 s  domino2_box first touches flap1_panel
 1.17 s  ball3_sphere leaves launch_guide_left
 1.17 s  domino1 passes 0.11 m from flap1 (flap1_panel) without touching it: nearest points (1.31, 0.00, 0.17) m and (1.42, 0.00, 0.17) m
 1.18 s  domino2_box leaves flap1_panel
 1.24 s  domino2_box touches flap1_panel again
 1.25 s  domino2_box leaves flap1_panel
 1.29 s  domino2_box touches flap1_panel again
 1.31 s  ball3_sphere touches launch_guide_left again
 1.47 s  domino2 passes 0.16 m from cart1_contact_roller (cart1_contact_roller_sphere) without touching it: nearest points (1.51, 0.00, 0.12) m and (1.65, 0.00, 0.19) m
 1.47 s  domino1 passes 0.31 m from cart1_contact_roller (cart1_contact_roller_sphere) without touching it: nearest points (1.35, 0.00, 0.12) m and (1.65, 0.00, 0.19) m
 1.47 s  domino1 passes 0.35 m from cart1 (cart1_box) without touching it: nearest points (1.35, 0.00, 0.12) m and (1.70, 0.00, 0.12) m
 1.48 s  flap1_panel first touches cart1_contact_roller_sphere
 1.48 s  domino1_box leaves floor
 1.48 s  domino1 comes to rest at (1.23, 0.00, 0.10) m
 1.48 s  domino2 passes 0.19 m from cart1 (cart1_box) without touching it: nearest points (1.51, 0.00, 0.12) m and (1.70, 0.00, 0.12) m
 1.48 s  flap1 passes 0.04 m from cart1 (cart1_box) without touching it: nearest points (1.67, 0.07, 0.23) m and (1.70, 0.07, 0.20) m
 1.51 s  domino1_box touches floor again
 1.67 s  flap1_panel leaves cart1_contact_roller_sphere
 1.72 s  flap1 reaches its 65° stop (the end where it sits lower) moving +200°/s
 1.73 s  flap1 is at its largest, 65.5°
 1.73 s  flap1 reaches its 65° stop (the end where it sits lower) again moving +50°/s
 1.75 s  domino2 comes to rest at (1.40, 0.00, 0.08) m
 2.07 s  cart1 reaches its upper stop (0.45 m) moving +0.74 m/s
 2.07 s  cart1_striker first touches ball2_sphere
 2.08 s  cart1 is at its largest, 0.5 m
 2.08 s  cart1 passes 0.01 m from ramp2 (ramp2_right_rail) without touching it: nearest points (2.38, 0.16, 0.52) m and (2.39, 0.16, 0.51) m
 2.08 s  cart1_contact_roller passes 0.32 m from ramp2 (ramp2_surface) without touching it: nearest points (2.14, 0.00, 0.22) m and (2.36, 0.00, 0.45) m
 2.08 s  cart1_contact_roller passes 0.37 m from ball2 (ball2_sphere) without touching it: nearest points (2.14, 0.00, 0.22) m and (2.40, 0.00, 0.49) m
 2.09 s  cart1_striker leaves ball2_sphere
 3.48 s  ball1 comes to rest at (0.13, 0.00, 0.05) m
20.00 s  lever_latch is at its largest, 0.0 m

State every 0.25 s:
0.00 s: ball1 at (0.06, 0.00, 0.52) m, at rest; touching nothing | domino1 at (1.08, 0.00, 0.12) m, at rest; touching floor | domino2 at (1.26, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | cart1 at 0.000 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_surface | lever1 at 0.0°, still; touching nothing | lever_latch at 0.000 m, still; touching nothing | lever_latch_roller (ball joint); touching nothing | ball3 at (3.87, 0.00, 0.71) m, at rest; touching nothing | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
0.25 s: ball1 at (0.13, 0.00, 0.50) m, moving 0.60 m/s (vx +0.56, vy +0.00, vz -0.20); touching ramp1_surface | domino1 at (1.08, 0.00, 0.12) m, at rest; touching floor | domino2 at (1.26, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | cart1 at 0.000 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.000 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.87, 0.00, 0.71) m, at rest; touching lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
0.50 s: ball1 at (0.34, 0.00, 0.42) m, moving 1.20 m/s (vx +1.13, vy +0.00, vz -0.41); touching ramp1_surface | domino1 at (1.08, 0.00, 0.12) m, at rest; touching floor | domino2 at (1.26, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | cart1 at 0.000 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.000 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
0.75 s: ball1 at (0.70, 0.00, 0.29) m, moving 1.80 m/s (vx +1.69, vy +0.00, vz -0.61); touching ramp1_surface | domino1 at (1.08, 0.00, 0.12) m, at rest; touching floor | domino2 at (1.26, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | cart1 at 0.000 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.000 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
1.00 s: ball1 at (1.05, 0.00, 0.15) m, moving 0.46 m/s (vx +0.14, vy +0.00, vz -0.44); touching domino1_box | domino1 at (1.14, 0.00, 0.13) m, moving 0.44 m/s (vx +0.43, vy +0.00, vz +0.09), turned 25° from how it started; touching ball1_sphere, domino2_box, floor | domino2 at (1.26, 0.00, 0.12) m, moving 0.39 m/s (vx +0.38, vy -0.00, vz +0.08), turned 2° from how it started; touching domino1_box, floor | flap1 at 0.0°, still; touching nothing | cart1 at 0.000 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.000 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
1.25 s: ball1 at (0.94, 0.00, 0.05) m, moving 0.67 m/s (vx -0.67, vy +0.00, vz +0.01); touching floor | domino1 at (1.20, 0.00, 0.11) m, moving 0.09 m/s (vx +0.09, vy -0.00, vz -0.03), turned 47° from how it started; touching domino2_box, floor | domino2 at (1.34, 0.00, 0.12) m, moving 0.12 m/s (vx +0.12, vy -0.00, vz -0.03), turned 35° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 6.2°, turning +83°/s; touching domino2_box | cart1 at 0.000 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.000 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
1.50 s: ball1 at (0.78, 0.00, 0.05) m, moving 0.61 m/s (vx -0.61, vy +0.00, vz -0.01); touching nothing | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 60° from how it started; touching domino2_box | domino2 at (1.39, 0.00, 0.09) m, at rest, turned 60° from how it started; touching domino1_box, floor | flap1 at 45.4°, turning +43°/s; touching cart1_contact_roller_sphere | cart1 at 0.011 m, moving +0.50 m/s; touching nothing | cart1_contact_roller (ball joint); touching flap1_panel | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.001 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
1.75 s: ball1 at (0.64, 0.00, 0.05) m, moving 0.53 m/s (vx -0.53, vy +0.00, vz +0.01); touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.1°, turning -8°/s; touching domino2_box | cart1 at 0.196 m, moving +0.84 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.001 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
2.00 s: ball1 at (0.51, 0.00, 0.05) m, moving 0.46 m/s (vx -0.46, vy +0.00, vz +0.01); touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.397 m, moving +0.76 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.001 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
2.25 s: ball1 at (0.41, 0.00, 0.05) m, moving 0.39 m/s (vx -0.39, vy +0.00, vz +0.01); touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.438 m, moving -0.08 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.001 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
2.50 s: ball1 at (0.32, 0.00, 0.05) m, moving 0.32 m/s (vx -0.32, vy +0.00, vz +0.00); touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.420 m, moving -0.07 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.001 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
2.75 s: ball1 at (0.24, 0.00, 0.05) m, moving 0.25 m/s (vx -0.25, vy +0.00, vz +0.00); touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.404 m, moving -0.06 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.001 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
3.00 s: ball1 at (0.19, 0.00, 0.05) m, moving 0.18 m/s (vx -0.18, vy +0.00, vz +0.00); touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.389 m, moving -0.06 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.001 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
3.25 s: ball1 at (0.15, 0.00, 0.05) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.376 m, moving -0.05 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.001 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
3.50 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.364 m, moving -0.05 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.001 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
3.75 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.353 m, moving -0.04 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.001 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
4.00 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.343 m, moving -0.04 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.001 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
4.25 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.334 m, moving -0.03 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.002 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
4.50 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.326 m, moving -0.03 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.002 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
4.75 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.319 m, moving -0.03 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.002 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
5.00 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.312 m, moving -0.03 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.002 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
5.25 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.306 m, moving -0.02 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.002 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
5.50 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.301 m, moving -0.02 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.002 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
5.75 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.296 m, moving -0.02 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.002 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
6.00 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.292 m, moving -0.02 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.002 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
6.25 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.288 m, moving -0.02 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.002 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
6.50 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.284 m, moving -0.01 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.002 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
6.75 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.281 m, moving -0.01 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.002 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
7.00 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.278 m, moving -0.01 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.002 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
7.25 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.275 m, moving -0.01 m/s; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.003 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
7.50 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.273 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.003 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
7.75 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.271 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.003 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
8.00 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.269 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.003 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
8.25 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.267 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.003 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
8.50 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.265 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.003 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
8.75 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.264 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.003 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
9.00 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.263 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.003 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
9.25 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.261 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.003 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
9.50 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.260 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.003 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
9.75 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.259 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.004 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
10.00 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.258 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.004 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
(the same through 10.25 s)
10.50 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.257 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.004 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
10.75 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.256 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.004 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
(the same through 11.00 s)
11.25 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 59° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.255 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.004 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
11.50 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 60° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.255 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.004 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
11.75 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 60° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.254 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.004 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
(the same through 12.00 s)
12.25 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 60° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.253 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.004 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
12.50 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 60° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.253 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.005 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
(the same through 12.75 s)
13.00 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 60° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.252 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.005 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
(the same through 14.00 s)
14.25 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 60° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.251 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.005 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
(the same through 15.00 s)
15.25 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.10) m, at rest, turned 60° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.251 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.006 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
(the same through 16.00 s)
16.25 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.09) m, at rest, turned 60° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.251 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.006 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
(the same through 16.50 s)
16.75 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.09) m, at rest, turned 60° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.250 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.006 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
(the same through 17.50 s)
17.75 s: ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor | domino1 at (1.23, 0.00, 0.09) m, at rest, turned 60° from how it started; touching domino2_box, floor | domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.250 m, still; touching nothing | cart1_contact_roller (ball joint); touching nothing | ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface | lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere | lever_latch at 0.007 m, still; touching nothing | lever_latch_roller (ball joint); touching lever1_latch_pad | ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray | pendulum1 at 0.0°, still; touching nothing | domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor | door1 at 0.0°, still; touching nothing | block1 at (4.88, 0.00, 0.06) m, at rest; touching floor | cart2 at 0.000 m, still; touching nothing | ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface | flap2 at 0.0°, still; touching nothing | ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface
(the same through 20.00 s)

At the end (20.00 s):
- ball1 at (0.13, 0.00, 0.05) m, at rest; touching floor
- domino1 at (1.23, 0.00, 0.09) m, at rest, turned 60° from how it started; touching domino2_box, floor
- domino2 at (1.40, 0.00, 0.08) m, at rest, turned 70° from how it started; touching domino1_box, flap1_panel, floor
- flap1 at 65.0°, still; touching domino2_box
- cart1 at 0.250 m, still; touching nothing
- cart1_contact_roller (ball joint); touching nothing
- ball2 at (2.43, 0.00, 0.52) m, at rest; touching ramp2_release_lip, ramp2_surface
- lever1 at 0.1°, still; touching ball3_sphere, lever_latch_roller_sphere
- lever_latch at 0.007 m, still; touching nothing
- lever_latch_roller (ball joint); touching lever1_latch_pad
- ball3 at (3.86, 0.00, 0.71) m, at rest; touching launch_guide_left, lever1_ball_tray
- pendulum1 at 0.0°, still; touching nothing
- domino3 at (4.31, 0.00, 0.12) m, at rest; touching floor
- door1 at 0.0°, still; touching nothing
- block1 at (4.88, 0.00, 0.06) m, at rest; touching floor
- cart2 at 0.000 m, still; touching nothing
- ball4 at (6.00, 0.00, 0.52) m, at rest; touching ramp3_release_lip, ramp3_surface
- flap2 at 0.0°, still; touching nothing
- ball5 at (7.33, 0.00, 0.85) m, at rest; touching shelf1_surface

Openings (fixed rings, open through the middle; height is the middle of the whole thing), and each loose thing that comes down through one's height:
launch_guide: an opening 0.12 m across, centre (3.87, 0.00, 1.05) m
- nothing loose comes down through launch_guide's height
ring1: an opening 0.20 m across, centre (3.87, 0.00, 0.36) m
- ball1 comes down through ring1's height at 0.63 s, 3.35 m from its centre: outside it, missing by 3.25 m
final_drop_guide: an opening 0.12 m across, centre (7.37, 0.00, 0.54) m
- nothing loose comes down through final_drop_guide's height
ring2: an opening 0.20 m across, centre (7.37, 0.00, 0.55) m
- nothing loose comes down through ring2's height
</history>


Does the world do what the brief says? First describe what happens in the run. Then end your reply with a ```json block
holding one object:

{"what_happens": "<what happens in the run>", "works": <true or false>, "problem": "<one sentence, or empty>"}

If it does not work, also reply with the complete corrected file in one ```xml block, keeping the names the
brief needs. If it works, no file is needed.
