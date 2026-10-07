```xml
<mujoco model="ramp_domino_ball_cup">
  <compiler angle="degree" inertiafromgeom="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" cone="elliptic" iterations="100" tolerance="1e-10"/>
  <size njmax="1000" nconmax="300"/>
  <statistic center="0.05 0 0.3" extent="1.8"/>

  <visual>
    <headlight ambient="0.4 0.4 0.4" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
    <rgba haze="0.9 0.95 1 1"/>
  </visual>

  <worldbody>
    <light name="main_light" pos="-0.5 -1 3" dir="0.2 0.2 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="3 2 0.1" rgba="0.84 0.86 0.88 1" friction="0.9 0.005 0.002" condim="6"/>

    <!-- The ramp descends toward +x at 15 degrees. -->
    <body name="ramp" pos="-0.7132046 0 0.4295949" quat="0.991444861 0 0.130526192 0">
      <geom name="ramp_surface" type="box" size="0.65 0.16 0.04" rgba="0.48 0.55 0.62 1" friction="0.65 0.001 0.0001" condim="6" solref="0.01 1"/>
      <geom name="ramp_left_rail" type="box" pos="0 0.145 0.08" size="0.65 0.015 0.04" rgba="0.32 0.39 0.46 1" friction="0.65 0.001 0.0001"/>
      <geom name="ramp_right_rail" type="box" pos="0 -0.145 0.08" size="0.65 0.015 0.04" rgba="0.32 0.39 0.46 1" friction="0.65 0.001 0.0001"/>
    </body>

    <!-- Ball1's initial contact point is exactly 1 m along the ramp from its low end. -->
    <body name="ball1" pos="-1.0253967 0 0.6167746">
      <freejoint name="ball1_free"/>
      <geom name="ball1_sphere" type="sphere" size="0.06" mass="0.075" rgba="0.95 0.28 0.12 1" friction="0.65 0.001 0.0001" condim="6" solref="0.008 1"/>
    </body>

    <body name="domino_stage" pos="0.0975 0 0.06">
      <geom name="domino_stage_surface" type="box" size="0.4975 0.24 0.06" rgba="0.64 0.59 0.49 1" friction="1 0.005 0.001" solref="0.01 1"/>
    </body>

    <!-- A low curb catches the trigger ball while allowing d1 to fall well past vertical. -->
    <body name="trigger_catch" pos="0.125 0 0.1425">
      <geom name="trigger_catch_curb" type="box" size="0.015 0.10 0.0225" rgba="0.42 0.44 0.46 1" friction="1 0.005 0.001" solref="0.008 1"/>
    </body>

    <body name="d1" pos="0 0 0.29">
      <freejoint name="d1_free"/>
      <geom name="d1_block" type="box" size="0.018 0.06 0.17" mass="0.30" rgba="0.95 0.73 0.15 1" friction="1 0.005 0.0001" condim="3" solref="0.008 1"/>
    </body>

    <body name="d2" pos="0.18 0 0.29">
      <freejoint name="d2_free"/>
      <geom name="d2_block" type="box" size="0.018 0.06 0.17" mass="0.17" rgba="0.24 0.67 0.42 1" friction="1 0.005 0.0001" condim="3" solref="0.008 1"/>
    </body>

    <body name="d3" pos="0.36 0 0.29">
      <freejoint name="d3_free"/>
      <geom name="d3_block" type="box" size="0.018 0.06 0.17" mass="0.10" rgba="0.22 0.48 0.88 1" friction="1 0.005 0.0001" condim="3" solref="0.008 1"/>
    </body>

    <!-- The perch presents ball2 to d3 and leads directly over the cup's entry rim. -->
    <body name="ball2_perch" pos="0.54 0 0.19">
      <geom name="ball2_perch_surface" type="box" size="0.055 0.12 0.07" rgba="0.64 0.59 0.49 1" friction="0.8 0.005 0.001" solref="0.008 1"/>
    </body>

    <body name="ball2" pos="0.54 0 0.315">
      <freejoint name="ball2_free"/>
      <geom name="ball2_sphere" type="sphere" size="0.055" mass="0.045" rgba="0.76 0.24 0.77 1" friction="0.8 0.005 0.003" condim="6" solref="0.008 1"/>
    </body>

    <!-- Open-top catching cup with a lowered entry rim and dissipative bottom. -->
    <body name="cup" pos="0.875 0 0">
      <geom name="cup_bottom" type="box" pos="0 0 0.01" size="0.28 0.22 0.01" rgba="0.18 0.57 0.64 1" friction="0.9 0.01 0.02" condim="6" solref="0.008 1"/>
      <geom name="cup_entry_wall" type="box" pos="-0.27 0 0.13" size="0.01 0.22 0.11" rgba="0.22 0.65 0.72 1" friction="0.9 0.01 0.012" condim="6" solref="0.008 1"/>
      <geom name="cup_far_wall" type="box" pos="0.27 0 0.17" size="0.01 0.22 0.15" rgba="0.22 0.65 0.72 1" friction="0.9 0.01 0.012" condim="6" solref="0.008 1"/>
      <geom name="cup_left_wall" type="box" pos="0 0.21 0.17" size="0.26 0.01 0.15" rgba="0.22 0.65 0.72 1" friction="0.9 0.01 0.012" condim="6" solref="0.008 1"/>
      <geom name="cup_right_wall" type="box" pos="0 -0.21 0.17" size="0.26 0.01 0.15" rgba="0.22 0.65 0.72 1" friction="0.9 0.01 0.012" condim="6" solref="0.008 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Calculating ramp descent parameters**

I'm working on the ramp descent calculations, focusing on the friction values. For Domino, I have a friction of .8, and I'm using a mixed friction rule. I’ve set the max values for the same priority, so the default rolling might be .0001 for the floor and .001 overall, making ball1 at .001. For ball2, I've set it at .01, which seems good. However, I’m contemplating if more detailed geometry should be considered in these calculations.

**Calculating ramp dynamics**

I'm building an elevated stage and ramp to set up a scenario with balls and dominoes. I've figured out the height and positions: the ball strikes the domino at a specific height. I’m examining the dimensions and slopes of the ramp, as well as calculating the ball's mass, speed, and volume. A lot relies on those factors to ensure everything works as planned. It feels kinda complex, but I'm committed to getting it just right!

**Analyzing mass and impacts**

I’m looking to understand how mass affects the collision dynamics between the balls and the dominoes. Using a specific mass and dimensions, I’m calculating volumes and densities to get effective mass at impact. I also need to figure out velocities and angles of rotation before and after collisions. It’s a bit complicated, but I want to ensure all factors are accounted for, including removing a ball from the chain to maintain clarity.

**Calculating ball2 motion**

I’m working through the roll resistance for ball2, looking at factors like the coefficient of rolling resistance and the stopping distance formula, which depends on velocity and acceleration. It seems like I’m estimating the acceleration and trying to see if a starting velocity of about 0.8 is sufficient for a distance of 0.25. I’m also considering the mass of ball2 and its diameter. There’s a lot happening here! I'll need to make sure all my calculations align.