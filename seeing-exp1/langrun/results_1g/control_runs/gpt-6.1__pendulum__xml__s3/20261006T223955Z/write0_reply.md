```xml
<mujoco model="pendulum_ball_and_cup">
  <compiler angle="degree" autolimits="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="100" tolerance="1e-10"/>
  <size njmax="1000" nconmax="200"/>
  <visual>
    <global azimuth="125" elevation="-22"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="0.5 -1 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <camera name="overview" pos="0.5 -3 1.7" xyaxes="1 0 0 0 0.45 0.893"/>

    <geom name="floor" type="plane" size="3 2 0.1" pos="0 0 0" rgba="0.72 0.75 0.78 1" condim="6" friction="0.3 0.002 0.0002" solref="0.006 1" solimp="0.95 0.99 0.001"/>

    <!-- Gravity releases the raised pendulum; its bob strikes toward +x. -->
    <body name="pendulum" pos="-0.115 0 0.67">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" damping="0.002" frictionloss="0.0002"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 -0.025 0 0 -0.54" size="0.012" mass="0.01" rgba="0.28 0.30 0.34 1" friction="0.2 0.002 0.0002"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.6" size="0.065" mass="0.22" rgba="0.85 0.35 0.12 1" condim="6" friction="0.2 0.002 0.0002" solref="0.006 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball" pos="0 0 0.04">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.06" rgba="0.95 0.82 0.16 1" condim="6" friction="0.3 0.002 0.0002" solref="0.006 1" solimp="0.95 0.99 0.001"/>
    </body>

    <!-- Upright cup, centered exactly 1 m from the ball's starting position.
         Its front wall has a low entrance notch. The nearly flush base
         admits the rolling ball and supplies increased rolling resistance. -->
    <body name="cup" pos="1 0 0">
      <geom name="cup_base" type="cylinder" pos="0 0 -0.003" size="0.21 0.005" rgba="0.18 0.48 0.70 1" condim="6" friction="0.8 0.01 0.012" solref="0.008 1" solimp="0.95 0.99 0.001"/>

      <geom name="cup_wall_00" type="box" pos="0.193 0 0.071" euler="0 0 0" size="0.012 0.041 0.069" rgba="0.18 0.48 0.70 1" condim="6" friction="0.8 0.01 0.012" solref="0.008 1"/>
      <geom name="cup_wall_01" type="box" pos="0.178309 0.073858 0.071" euler="0 0 22.5" size="0.012 0.041 0.069" rgba="0.18 0.48 0.70 1" condim="6" friction="0.8 0.01 0.012" solref="0.008 1"/>
      <geom name="cup_wall_02" type="box" pos="0.136471 0.136471 0.071" euler="0 0 45" size="0.012 0.041 0.069" rgba="0.18 0.48 0.70 1" condim="6" friction="0.8 0.01 0.012" solref="0.008 1"/>
      <geom name="cup_wall_03" type="box" pos="0.073858 0.178309 0.071" euler="0 0 67.5" size="0.012 0.041 0.069" rgba="0.18 0.48 0.70 1" condim="6" friction="0.8 0.01 0.012" solref="0.008 1"/>
      <geom name="cup_wall_04" type="box" pos="0 0.193 0.071" euler="0 0 90" size="0.012 0.041 0.069" rgba="0.18 0.48 0.70 1" condim="6" friction="0.8 0.01 0.012" solref="0.008 1"/>
      <geom name="cup_wall_05" type="box" pos="-0.073858 0.178309 0.071" euler="0 0 112.5" size="0.012 0.041 0.069" rgba="0.18 0.48 0.70 1" condim="6" friction="0.8 0.01 0.012" solref="0.008 1"/>
      <geom name="cup_wall_06" type="box" pos="-0.136471 0.136471 0.071" euler="0 0 135" size="0.012 0.041 0.069" rgba="0.18 0.48 0.70 1" condim="6" friction="0.8 0.01 0.012" solref="0.008 1"/>

      <geom name="cup_entrance_top_07" type="box" pos="-0.178309 0.073858 0.12" euler="0 0 157.5" size="0.012 0.041 0.02" rgba="0.18 0.48 0.70 1" condim="6" friction="0.8 0.01 0.012" solref="0.008 1"/>
      <geom name="cup_entrance_top_08" type="box" pos="-0.193 0 0.12" euler="0 0 180" size="0.012 0.041 0.02" rgba="0.18 0.48 0.70 1" condim="6" friction="0.8 0.01 0.012" solref="0.008 1"/>
      <geom name="cup_entrance_top_09" type="box" pos="-0.178309 -0.073858 0.12" euler="0 0 202.5" size="0.012 0.041 0.02" rgba="0.18 0.48 0.70 1" condim="6" friction="0.8 0.01 0.012" solref="0.008 1"/>

      <geom name="cup_wall_10" type="box" pos="-0.136471 -0.136471 0.071" euler="0 0 225" size="0.012 0.041 0.069" rgba="0.18 0.48 0.70 1" condim="6" friction="0.8 0.01 0.012" solref="0.008 1"/>
      <geom name="cup_wall_11" type="box" pos="-0.073858 -0.178309 0.071" euler="0 0 247.5" size="0.012 0.041 0.069" rgba="0.18 0.48 0.70 1" condim="6" friction="0.8 0.01 0.012" solref="0.008 1"/>
      <geom name="cup_wall_12" type="box" pos="0 -0.193 0.071" euler="0 0 270" size="0.012 0.041 0.069" rgba="0.18 0.48 0.70 1" condim="6" friction="0.8 0.01 0.012" solref="0.008 1"/>
      <geom name="cup_wall_13" type="box" pos="0.073858 -0.178309 0.071" euler="0 0 292.5" size="0.012 0.041 0.069" rgba="0.18 0.48 0.70 1" condim="6" friction="0.8 0.01 0.012" solref="0.008 1"/>
      <geom name="cup_wall_14" type="box" pos="0.136471 -0.136471 0.071" euler="0 0 315" size="0.012 0.041 0.069" rgba="0.18 0.48 0.70 1" condim="6" friction="0.8 0.01 0.012" solref="0.008 1"/>
      <geom name="cup_wall_15" type="box" pos="0.178309 -0.073858 0.071" euler="0 0 337.5" size="0.012 0.041 0.069" rgba="0.18 0.48 0.70 1" condim="6" friction="0.8 0.01 0.012" solref="0.008 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.65 0 0 0.04 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Evaluating test design for physics**

I’m thinking about constructing a test for a physics tool. I need to design a pendulum that strikes a ball, which then rolls into a cup and settles within 6 seconds. I’m unsure whether the cup should be horizontal or an open top. I have to consider whether to build a recessed cup, which seems tricky if there's an infinite floor. The cup could be positioned sideways with an opening toward the ball. I want to ensure the cup is upright and accessible via a ramp.

**Designing a cup for physics experiment**

I’m considering an upright U-shaped cup with a circular base, which has a thickness of 0.005 at the top and overlaps with the floor. The ball would stay on the floor, enter the cup through an open front, and stop upon hitting the back. The cup needs to be precisely centered at 1 meter. I'm also thinking about using a pendulum that doesn’t use motors, just gravity, to keep everything consistent. The pendulum should impart a speed of 0.8 to 1.4 m/s without launching the ball.

**Analyzing pendulum swing dynamics**

I'm working on the pendulum setup where the pivot is at x = -0.12 and the pendulum bob is positioned at z = 0.065. For the swing, I’m considering negative theta so that the bob moves to the left while being behind the ball at x = -0.48. I want to start with a theta of 0.65. I'll need to account for the acceleration related to the angle as it swings. At theta = 0, the bob's position should be x = -0.12 and z = 0.065.

**Evaluating pendulum mechanics**

I'm working through the mechanics of a pendulum. If the elevation of the lip is 2mm and the step passes mechanically with a coefficient greater than 0.8, then that's good. The pendulum should swing low enough at the bottom without making contact, which I think should be 0.005. I’m considering if the rod or cylinder ends need to be adjusted to ensure there's no collision at the pivot. I’ll need to clarify the geometry and how inertia plays into this.