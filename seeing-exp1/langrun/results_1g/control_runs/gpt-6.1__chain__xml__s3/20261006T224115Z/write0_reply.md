```xml
<mujoco model="three_balls_into_cup">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" cone="elliptic" iterations="80"/>
  <size nconmax="200" njmax="1000"/>

  <visual>
    <global azimuth="225" elevation="-25"/>
    <headlight ambient="0.4 0.4 0.4" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="-0.3 -0.5 2" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <camera name="overview" pos="-1.1 -1.5 0.95" xyaxes="0.806 -0.592 0 0.265 0.360 0.895"/>

    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.78 0.79 0.81 1" condim="6" friction="0.65 0.0001 0.0025" solref="0.006 1" solimp="0.95 0.99 0.001"/>

    <!-- Center-weighted balls retain less spin after transferring momentum. -->
    <body name="ball1" pos="-0.60 0 0.06">
      <freejoint name="ball1_free"/>
      <inertial pos="0 0 0" mass="0.1" diaginertia="0.000036 0.000036 0.000036"/>
      <geom name="ball1_geom" type="sphere" size="0.06" rgba="0.88 0.18 0.12 1" condim="6" friction="0.65 0.0001 0.0025" solref="0.006 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball2" pos="-0.33 0 0.06">
      <freejoint name="ball2_free"/>
      <inertial pos="0 0 0" mass="0.1" diaginertia="0.000036 0.000036 0.000036"/>
      <geom name="ball2_geom" type="sphere" size="0.06" rgba="0.95 0.68 0.10 1" condim="6" friction="0.65 0.0001 0.0025" solref="0.006 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball3" pos="-0.06 0 0.06">
      <freejoint name="ball3_free"/>
      <inertial pos="0 0 0" mass="0.1" diaginertia="0.000036 0.000036 0.000036"/>
      <geom name="ball3_geom" type="sphere" size="0.06" rgba="0.18 0.70 0.30 1" condim="6" friction="0.65 0.0001 0.0025" solref="0.006 1" solimp="0.95 0.99 0.001"/>
    </body>

    <!-- A fixed cup lying on its side, with its open mouth facing the balls.
         Its inner bottom is flush with the floor, avoiding an entrance step. -->
    <body name="cup" pos="0.18 0 0.085">
      <geom name="cup_wall_00" type="box" pos="0 0 0.095" euler="0 0 0" size="0.12 0.026 0.01" rgba="0.15 0.38 0.75 0.65" condim="6" friction="0.65 0.0001 0.0025" solref="0.008 1"/>
      <geom name="cup_wall_01" type="box" pos="0 -0.0475 0.0822724" euler="30 0 0" size="0.12 0.026 0.01" rgba="0.15 0.38 0.75 0.65" condim="6" friction="0.65 0.0001 0.0025" solref="0.008 1"/>
      <geom name="cup_wall_02" type="box" pos="0 -0.0822724 0.0475" euler="60 0 0" size="0.12 0.026 0.01" rgba="0.15 0.38 0.75 0.65" condim="6" friction="0.65 0.0001 0.0025" solref="0.008 1"/>
      <geom name="cup_wall_03" type="box" pos="0 -0.095 0" euler="90 0 0" size="0.12 0.026 0.01" rgba="0.15 0.38 0.75 0.65" condim="6" friction="0.65 0.0001 0.0025" solref="0.008 1"/>
      <geom name="cup_wall_04" type="box" pos="0 -0.0822724 -0.0475" euler="120 0 0" size="0.12 0.026 0.01" rgba="0.15 0.38 0.75 0.65" condim="6" friction="0.65 0.0001 0.0025" solref="0.008 1"/>
      <geom name="cup_wall_05" type="box" pos="0 -0.0475 -0.0822724" euler="150 0 0" size="0.12 0.026 0.01" rgba="0.15 0.38 0.75 0.65" condim="6" friction="0.65 0.0001 0.0025" solref="0.008 1"/>
      <geom name="cup_wall_06" type="box" pos="0 0 -0.095" euler="180 0 0" size="0.12 0.026 0.01" rgba="0.15 0.38 0.75 0.65" condim="6" friction="0.65 0.0001 0.0025" solref="0.008 1"/>
      <geom name="cup_wall_07" type="box" pos="0 0.0475 -0.0822724" euler="210 0 0" size="0.12 0.026 0.01" rgba="0.15 0.38 0.75 0.65" condim="6" friction="0.65 0.0001 0.0025" solref="0.008 1"/>
      <geom name="cup_wall_08" type="box" pos="0 0.0822724 -0.0475" euler="240 0 0" size="0.12 0.026 0.01" rgba="0.15 0.38 0.75 0.65" condim="6" friction="0.65 0.0001 0.0025" solref="0.008 1"/>
      <geom name="cup_wall_09" type="box" pos="0 0.095 0" euler="270 0 0" size="0.12 0.026 0.01" rgba="0.15 0.38 0.75 0.65" condim="6" friction="0.65 0.0001 0.0025" solref="0.008 1"/>
      <geom name="cup_wall_10" type="box" pos="0 0.0822724 0.0475" euler="300 0 0" size="0.12 0.026 0.01" rgba="0.15 0.38 0.75 0.65" condim="6" friction="0.65 0.0001 0.0025" solref="0.008 1"/>
      <geom name="cup_wall_11" type="box" pos="0 0.0475 0.0822724" euler="330 0 0" size="0.12 0.026 0.01" rgba="0.15 0.38 0.75 0.65" condim="6" friction="0.65 0.0001 0.0025" solref="0.008 1"/>
      <geom name="cup_back" type="cylinder" pos="0.13 0 0" euler="0 90 0" size="0.105 0.01" rgba="0.12 0.30 0.65 1" condim="6" friction="0.65 0.0001 0.0025" solref="0.008 1"/>
    </body>
  </worldbody>

  <!-- Springy, frictionless ball-to-ball contacts transfer forward momentum.
       Floor and cup contacts remain dissipative. -->
  <contact>
    <pair name="impact_12" geom1="ball1_geom" geom2="ball2_geom" condim="1" solref="-30000 -20" solimp="0.95 0.99 0.001"/>
    <pair name="impact_23" geom1="ball2_geom" geom2="ball3_geom" condim="1" solref="-30000 -20" solimp="0.95 0.99 0.001"/>
    <pair name="impact_13" geom1="ball1_geom" geom2="ball3_geom" condim="1" solref="-30000 -20" solimp="0.95 0.99 0.001"/>
  </contact>

  <keyframe>
    <key name="start" time="0" qpos="-0.60 0 0.06 1 0 0 0 -0.33 0 0.06 1 0 0 0 -0.06 0 0.06 1 0 0 0" qvel="1 0 0 0 16.6666667 0 0 0 0 0 0 0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Designing a Rolling Cup Prototype**

I need to design a system where elastic impacts cause balls to roll into a cup within 6 seconds. However, I’m struggling because there's no computational tool available to help with this task. I’m considering the physics involved, like the radius of the balls and their distance from the cup. It seems I might need an upright cup with an opening or a ramp to facilitate the balls entering. This is quite a challenge!

**Constructing a Rolling Ball Cup**

I'm thinking about using a rectangular U-shaped trough for the cup that has an opening on one end and no floor bump. I could design it tilted onto its side with segmented boxes along the x-axis for the cylinder shell. The ball should fit well with a radius of .06. The center of the horizontal cylinder should have a specific clearance, ensuring the ball will roll smoothly into it. I envision 16 box panels approximating a circle for the cup's body. Let's figure out the dimensions to make it work!

**Designing a Ball and Cup Interaction**

I'm considering a capped cylinder positioned at x = .81, with the mouth at x = .4. I need to calculate the momentum of the third ball as it reaches the cup. The spheres are typically inelastic, so I have to work with the default MuJoCo contact settings. If the first ball rebounds, it can cause the second and third balls to roll into the cup, but without bounce, they'll just push forward. Let's figure out the right parameters for this setup!

**Considering floor friction**

I'm reflecting on the idea of using very low friction on the floor to allow balls to slide and rotate without getting stuck. It seems like achieving this would require some additional rolls to build up the necessary speed. I also think about how inertia plays a role, needing to keep it small with the formula 0.002 mass times radius squared, while ensuring the weight is centered. It's all interconnected!

**Visualizing cup orientation**

I’m thinking about a cup lying sideways, and it’s obvious from how the walls are a blue color with some transparency. The ball inside is visible too. I might want to make the rear of the cup translucent as an option. I’m considering using solid panels for the cup while positioning the camera at the front left, showing the mouth of the cup, which faces the negative x-axis, making it look like a naturally tipped cup.