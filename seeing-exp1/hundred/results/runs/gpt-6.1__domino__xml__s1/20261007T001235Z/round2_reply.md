```xml
<mujoco model="ramp_domino_cup_corrected">
  <compiler angle="radian" inertiafromgeom="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="100" tolerance="1e-10"/>
  <size njmax="1000" nconmax="300"/>

  <visual>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.65 0.65 0.65" specular="0.15 0.15 0.15"/>
  </visual>

  <worldbody>
    <light name="main_light" pos="0.3 -2 4" dir="0 0 -1"/>
    <camera name="overview" pos="2.6 -4.4 2.6" xyaxes="0.86 0.51 0 -0.23 0.39 0.89"/>

    <geom name="floor" type="plane" size="4 3 0.1" rgba="0.22 0.25 0.28 1" friction="0.9 0.005 0.0002" condim="3" solref="0.008 1" solimp="0.95 0.99 0.001"/>

    <!-- The ramp descends toward +x at 20 degrees. -->
    <body name="ramp" pos="0 0 0">
      <geom name="ramp_deck" type="box" pos="-0.637496 0 0.397624" quat="0.984807753 0 0.173648178 0" size="0.6 0.22 0.04" rgba="0.48 0.54 0.62 1" friction="0.7 0.003 0.0002" condim="6" solref="0.008 1" solimp="0.95 0.99 0.001"/>
      <geom name="ramp_left_rail" type="box" pos="-0.618685 0.235 0.449307" quat="0.984807753 0 0.173648178 0" size="0.6 0.015 0.06" rgba="0.32 0.38 0.46 1" friction="0.7 0.003 0.0002" condim="6" solref="0.008 1" solimp="0.95 0.99 0.001"/>
      <geom name="ramp_right_rail" type="box" pos="-0.618685 -0.235 0.449307" quat="0.984807753 0 0.173648178 0" size="0.6 0.015 0.06" rgba="0.32 0.38 0.46 1" friction="0.7 0.003 0.0002" condim="6" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <!-- Initial surface contact is one metre up the ramp from its lower edge. -->
    <body name="ball1" pos="-0.973972 0 0.642685">
      <freejoint/>
      <geom name="ball1_sphere" type="sphere" size="0.075" mass="0.4" rgba="0.95 0.25 0.12 1" friction="0.7 0.003 0.0002" condim="6" priority="1" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="d1" pos="0.16 0 0.2205">
      <freejoint/>
      <geom name="d1_block" type="box" size="0.018 0.09 0.22" mass="0.25" rgba="0.95 0.65 0.12 1" friction="1.0 0.005 0.0002" condim="3" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="d2" pos="0.40 0 0.2205">
      <freejoint/>
      <geom name="d2_block" type="box" size="0.018 0.09 0.22" mass="0.25" rgba="0.25 0.70 0.35 1" friction="1.0 0.005 0.0002" condim="3" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="d3" pos="0.64 0 0.2205">
      <freejoint/>
      <geom name="d3_block" type="box" size="0.018 0.09 0.22" mass="0.25" rgba="0.20 0.50 0.95 1" friction="1.0 0.005 0.0002" condim="3" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball1_stop" pos="0.28 0 0.06">
      <geom name="ball1_stop_block" type="box" size="0.022 0.22 0.06" rgba="0.38 0.40 0.43 1" friction="0.9 0.005 0.0002" condim="3" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <!-- The perch ends at x=0.895, leaving 5 mm clearance from the cup. -->
    <body name="ball2_perch" pos="0.87 0 0.1605">
      <freejoint/>
      <geom name="ball2_perch_block" type="box" size="0.025 0.11 0.16" mass="0.05" rgba="0.48 0.50 0.54 1" friction="0.45 0.003 0.0002" condim="3" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball2" pos="0.87 0 0.396">
      <freejoint/>
      <geom name="ball2_sphere" type="sphere" size="0.075" mass="0.08" rgba="0.85 0.20 0.65 1" friction="0.7 0.015 0.02" condim="6" priority="2" solref="0.012 1" solimp="0.95 0.99 0.001"/>
    </body>

    <!-- Low receiving rim, dissipative bottom, and high containment walls. -->
    <body name="cup" pos="0 0 0">
      <geom name="cup_bottom" type="box" pos="1.40 0 0.02" size="0.50 0.34 0.02" rgba="0.55 0.73 0.78 1" friction="0.8 0.015 0.02" condim="6" solref="0.012 1" solimp="0.95 0.99 0.001"/>
      <geom name="cup_rear_wall" type="box" pos="0.92 0 0.03" size="0.02 0.34 0.03" rgba="0.35 0.58 0.65 1" friction="0.8 0.015 0.02" condim="6" solref="0.012 1" solimp="0.95 0.99 0.001"/>
      <geom name="cup_front_wall" type="box" pos="1.90 0 0.27" size="0.02 0.34 0.27" rgba="0.35 0.58 0.65 1" friction="0.8 0.015 0.02" condim="6" solref="0.012 1" solimp="0.95 0.99 0.001"/>
      <geom name="cup_left_wall" type="box" pos="1.40 0.32 0.27" size="0.52 0.02 0.27" rgba="0.35 0.58 0.65 1" friction="0.8 0.015 0.02" condim="6" solref="0.012 1" solimp="0.95 0.99 0.001"/>
      <geom name="cup_right_wall" type="box" pos="1.40 -0.32 0.27" size="0.52 0.02 0.27" rgba="0.35 0.58 0.65 1" friction="0.8 0.015 0.02" condim="6" solref="0.012 1" solimp="0.95 0.99 0.001"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start"/>
  </keyframe>
</mujoco>
```