```xml
<mujoco model="pendulum_ball_and_cup">
  <compiler angle="radian" autolimits="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="80" cone="elliptic"/>
  <size njmax="2000" nconmax="400"/>
  <statistic center="0.45 0 0.3" extent="1.4"/>

  <visual>
    <global azimuth="125" elevation="-25"/>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="0.4 -1 3" dir="0 0.2 -1"/>
    <camera name="overview" pos="1.4 -2.2 1.4" xyaxes="0.918 0.396 0 -0.165 0.383 0.909"/>

    <geom name="floor" type="plane" size="3 2 0.1" rgba="0.78 0.80 0.82 1" condim="6" friction="0.65 0.002 0.0001" solref="0.006 1" solimp="0.95 0.99 0.001"/>

    <body name="stand" pos="-0.09 0.2 0">
      <geom name="stand_post" type="box" pos="0 0 0.33" size="0.025 0.025 0.33" rgba="0.25 0.28 0.32 1"/>
      <geom name="stand_foot" type="box" pos="0 0 0.015" size="0.12 0.09 0.015" rgba="0.25 0.28 0.32 1"/>
      <geom name="stand_axle" type="cylinder" fromto="0 -0.23 0.64 0 0.025 0.64" size="0.015" rgba="0.45 0.48 0.52 1"/>
    </body>

    <!-- Gravity releases the raised pendulum toward the ball. -->
    <body name="pendulum" pos="-0.09 0 0.64">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" damping="0.002"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 -0.015 0 0 -0.565" size="0.008" mass="0.02" contype="0" conaffinity="0" rgba="0.35 0.38 0.42 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.6" size="0.035" mass="0.35" rgba="0.85 0.32 0.12 1" condim="3" friction="0.25 0.001 0.0001" solref="0.006 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball" pos="0 0 0.04">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.045" rgba="0.95 0.76 0.12 1" condim="6" friction="0.65 0.002 0.0001" solref="0.006 1" solimp="0.95 0.99 0.001"/>
    </body>

    <!-- The cup origin is exactly 1 m from the initial ball centre.
         An integral ramp crosses its low front lip; taller sides retain the ball. -->
    <body name="cup" pos="1 0 0.04">
      <geom name="cup_base" type="cylinder" pos="0 0 -0.036" size="0.218 0.004" rgba="0.12 0.42 0.65 1" condim="6" friction="0.8 0.01 0.002" solref="0.006 1" solimp="0.95 0.99 0.001"/>

      <geom name="cup_wall_00" type="box" pos="0.2 0 0.043" size="0.012 0.04 0.075" euler="0 0 0" rgba="0.16 0.50 0.75 1" friction="0.65 0.005 0.0002" solref="0.006 1"/>
      <geom name="cup_wall_01" type="box" pos="0.184776 0.076537 0.043" size="0.012 0.04 0.075" euler="0 0 0.392699" rgba="0.16 0.50 0.75 1" friction="0.65 0.005 0.0002" solref="0.006 1"/>
      <geom name="cup_wall_02" type="box" pos="0.141421 0.141421 0.043" size="0.012 0.04 0.075" euler="0 0 0.785398" rgba="0.16 0.50 0.75 1" friction="0.65 0.005 0.0002" solref="0.006 1"/>
      <geom name="cup_wall_03" type="box" pos="0.076537 0.184776 0.043" size="0.012 0.04 0.075" euler="0 0 1.178097" rgba="0.16 0.50 0.75 1" friction="0.65 0.005 0.0002" solref="0.006 1"/>
      <geom name="cup_wall_04" type="box" pos="0 0.2 0.043" size="0.012 0.04 0.075" euler="0 0 1.570796" rgba="0.16 0.50 0.75 1" friction="0.65 0.005 0.0002" solref="0.006 1"/>
      <geom name="cup_wall_05" type="box" pos="-0.076537 0.184776 0.043" size="0.012 0.04 0.075" euler="0 0 1.963495" rgba="0.16 0.50 0.75 1" friction="0.65 0.005 0.0002" solref="0.006 1"/>
      <geom name="cup_wall_06" type="box" pos="-0.141421 0.141421 0.043" size="0.012 0.04 0.075" euler="0 0 2.356194" rgba="0.16 0.50 0.75 1" friction="0.65 0.005 0.0002" solref="0.006 1"/>

      <geom name="cup_wall_07" type="box" pos="-0.184776 0.076537 0.008" size="0.012 0.04 0.04" euler="0 0 2.748894" rgba="0.16 0.50 0.75 1" friction="0.65 0.005 0.0002" solref="0.006 1"/>
      <geom name="cup_wall_08" type="box" pos="-0.2 0 0.008" size="0.012 0.04 0.04" euler="0 0 3.141593" rgba="0.16 0.50 0.75 1" friction="0.65 0.005 0.0002" solref="0.006 1"/>
      <geom name="cup_wall_09" type="box" pos="-0.184776 -0.076537 0.008" size="0.012 0.04 0.04" euler="0 0 3.534292" rgba="0.16 0.50 0.75 1" friction="0.65 0.005 0.0002" solref="0.006 1"/>

      <geom name="cup_wall_10" type="box" pos="-0.141421 -0.141421 0.043" size="0.012 0.04 0.075" euler="0 0 3.926991" rgba="0.16 0.50 0.75 1" friction="0.65 0.005 0.0002" solref="0.006 1"/>
      <geom name="cup_wall_11" type="box" pos="-0.076537 -0.184776 0.043" size="0.012 0.04 0.075" euler="0 0 4.319690" rgba="0.16 0.50 0.75 1" friction="0.65 0.005 0.0002" solref="0.006 1"/>
      <geom name="cup_wall_12" type="box" pos="0 -0.2 0.043" size="0.012 0.04 0.075" euler="0 0 4.712389" rgba="0.16 0.50 0.75 1" friction="0.65 0.005 0.0002" solref="0.006 1"/>
      <geom name="cup_wall_13" type="box" pos="0.076537 -0.184776 0.043" size="0.012 0.04 0.075" euler="0 0 5.105088" rgba="0.16 0.50 0.75 1" friction="0.65 0.005 0.0002" solref="0.006 1"/>
      <geom name="cup_wall_14" type="box" pos="0.141421 -0.141421 0.043" size="0.012 0.04 0.075" euler="0 0 5.497787" rgba="0.16 0.50 0.75 1" friction="0.65 0.005 0.0002" solref="0.006 1"/>
      <geom name="cup_wall_15" type="box" pos="0.184776 -0.076537 0.043" size="0.012 0.04 0.075" euler="0 0 5.890486" rgba="0.16 0.50 0.75 1" friction="0.65 0.005 0.0002" solref="0.006 1"/>

      <!-- Ramp top runs from world (0.42, 0, 0) to (0.83, 0, 0.10). -->
      <geom name="cup_entry_ramp" type="box" pos="-0.372630 0 0.000285" size="0.211010 0.085 0.01" euler="0 -0.239232 0" rgba="0.22 0.57 0.78 1" condim="6" friction="0.65 0.002 0.0001" solref="0.006 1" solimp="0.95 0.99 0.001"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.95 0 0 0.04 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Evaluating pendulum dynamics**

I’m considering the situation after the ramp accelerates and how the ball collides with moderate restitution in MuJoCo, resulting in nearly zero bounce. The heavy bob shares its velocity with the ball, impacting their speeds. I need to check the required energies and distances, which seem marginal for climbing. The pendulum swings may risk contact with the ball, but the geometry seems well-calibrated to avoid issues. Everything looks good regarding clearances and parameters!

**Evaluating ramp and ball placement**

I’m looking at a scenario involving a cylinder with a base radius of .184 and a cup interior radius of .158. There’s a ball with a diameter of .32 that needs to be shot into the cup. The ramp end height is .86, and I need to consider the necessary angles for the ball to fall into the cup correctly. The ball must fit between the center positions of x .882 and .1.118.