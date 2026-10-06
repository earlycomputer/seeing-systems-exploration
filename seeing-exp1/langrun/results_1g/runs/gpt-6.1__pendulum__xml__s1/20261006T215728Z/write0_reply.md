The pendulum is released under gravity. A low entry lip lets the ball roll into the cup, whose higher rolling friction helps bring it to rest.

```xml
<mujoco model="pendulum_ball_into_cup">
  <compiler angle="degree" inertiafromgeom="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" iterations="80"/>
  <size njmax="200" nconmax="100"/>

  <visual>
    <global azimuth="120" elevation="-25"/>
    <headlight ambient="0.4 0.4 0.4" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="light" pos="0.5 -1 3" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="3 2 0.1" pos="0 0 0" condim="6" friction="0.6 0.002 0.00015" solref="0.01 1" solimp="0.95 0.99 0.001" rgba="0.78 0.80 0.82 1"/>

    <body name="frame" pos="-0.09 0 0">
      <geom name="frame_left_post" type="capsule" fromto="0 -0.18 0.02 0 -0.18 0.70" size="0.018" contype="0" conaffinity="0" rgba="0.3 0.32 0.35 1"/>
      <geom name="frame_right_post" type="capsule" fromto="0 0.18 0.02 0 0.18 0.70" size="0.018" contype="0" conaffinity="0" rgba="0.3 0.32 0.35 1"/>
      <geom name="frame_axle" type="capsule" fromto="0 -0.20 0.70 0 0.20 0.70" size="0.016" contype="0" conaffinity="0" rgba="0.3 0.32 0.35 1"/>
    </body>

    <body name="pendulum" pos="-0.09 0 0.70">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" limited="true" range="-35 35" damping="0.015"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 -0.025 0 0 -0.58" size="0.012" mass="0.025" friction="0.4 0.001 0.0001" rgba="0.35 0.38 0.42 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.63" size="0.06" mass="0.4" condim="6" friction="0.4 0.001 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.85 0.28 0.12 1"/>
    </body>

    <body name="ball" pos="0 0 0.04">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.08" condim="6" friction="0.6 0.002 0.00015" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.95 0.75 0.12 1"/>
    </body>

    <body name="cup" pos="1 0 0">
      <geom name="cup_base" type="cylinder" pos="0 0 0.002" size="0.18 0.002" condim="6" friction="0.8 0.01 0.006" solref="0.01 1" solimp="0.95 0.99 0.001" rgba="0.15 0.45 0.65 1"/>
      <geom name="cup_wall_0" type="box" pos="0.18 0 0.064" size="0.012 0.05 0.06" euler="0 0 0" condim="6" friction="0.8 0.01 0.006" solref="0.012 1" rgba="0.18 0.55 0.75 1"/>
      <geom name="cup_wall_30" type="box" pos="0.155885 0.09 0.064" size="0.012 0.05 0.06" euler="0 0 30" condim="6" friction="0.8 0.01 0.006" solref="0.012 1" rgba="0.18 0.55 0.75 1"/>
      <geom name="cup_wall_60" type="box" pos="0.09 0.155885 0.064" size="0.012 0.05 0.06" euler="0 0 60" condim="6" friction="0.8 0.01 0.006" solref="0.012 1" rgba="0.18 0.55 0.75 1"/>
      <geom name="cup_wall_90" type="box" pos="0 0.18 0.064" size="0.012 0.05 0.06" euler="0 0 90" condim="6" friction="0.8 0.01 0.006" solref="0.012 1" rgba="0.18 0.55 0.75 1"/>
      <geom name="cup_wall_120" type="box" pos="-0.09 0.155885 0.064" size="0.012 0.05 0.06" euler="0 0 120" condim="6" friction="0.8 0.01 0.006" solref="0.012 1" rgba="0.18 0.55 0.75 1"/>
      <geom name="cup_entry_150" type="box" pos="-0.155885 0.09 0.006" size="0.012 0.05 0.002" euler="0 0 150" condim="6" friction="0.5 0.002 0.00015" solref="0.01 1" rgba="0.18 0.55 0.75 1"/>
      <geom name="cup_entry_180" type="box" pos="-0.18 0 0.006" size="0.012 0.05 0.002" euler="0 0 180" condim="6" friction="0.5 0.002 0.00015" solref="0.01 1" rgba="0.18 0.55 0.75 1"/>
      <geom name="cup_entry_210" type="box" pos="-0.155885 -0.09 0.006" size="0.012 0.05 0.002" euler="0 0 210" condim="6" friction="0.5 0.002 0.00015" solref="0.01 1" rgba="0.18 0.55 0.75 1"/>
      <geom name="cup_wall_240" type="box" pos="-0.09 -0.155885 0.064" size="0.012 0.05 0.06" euler="0 0 240" condim="6" friction="0.8 0.01 0.006" solref="0.012 1" rgba="0.18 0.55 0.75 1"/>
      <geom name="cup_wall_270" type="box" pos="0 -0.18 0.064" size="0.012 0.05 0.06" euler="0 0 270" condim="6" friction="0.8 0.01 0.006" solref="0.012 1" rgba="0.18 0.55 0.75 1"/>
      <geom name="cup_wall_300" type="box" pos="0.09 -0.155885 0.064" size="0.012 0.05 0.06" euler="0 0 300" condim="6" friction="0.8 0.01 0.006" solref="0.012 1" rgba="0.18 0.55 0.75 1"/>
      <geom name="cup_wall_330" type="box" pos="0.155885 -0.09 0.064" size="0.012 0.05 0.06" euler="0 0 330" condim="6" friction="0.8 0.01 0.006" solref="0.012 1" rgba="0.18 0.55 0.75 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.4 0 0 0.04 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
pendulum touches ball
ball comes to rest in cup
```

---
thinking (summarized):

**Analyzing pendulum mechanics**

I’m considering how a pendulum's movement affects a ball's speed and friction. The ball will decelerate due to friction, while a cup can help retain it with its specific geometry. I need to ensure that as the pendulum swings, it doesn’t keep nudging the ball unnecessarily. Choosing the right parameters like ball radius and mass is crucial since it affects angular momentum and contact efficiency. I’m analyzing whether the bob and pivot positions are correct for optimal movement.

**Calculating pendulum motion**

I’m analyzing the motion of a pendulum bob using its rotation about the y-axis. The starting angle is positive, causing the bob's x-coordinate to become negative due to gravity, which then decreases the angle. For instance, the initial position is around -0.312 in the x-direction and 0.110 in the z-direction. As the pendulum impacts, I see the center at about -0.095 in x, which seems to be a good measurement. Tracking the vertical difference and radii sum helps confirm accuracy.

**Revising energy calculations**

I’m thinking about the energy of a rolling ball, using the kinetic energy formula \(0.5 \times (1.4) \times v^2\). I realize that deceleration is influenced by torque, which I need to consider when thinking about rolling motion. Friction torque is determined by the rolling coefficient of friction, \( \mu_{\text{roll}} \times mg\). It seems like the effective deceleration can be simplified to \( (\mu_{\text{roll}} / R) \times g / 1.4 \). There’s a lot to unpack here!

**Clarifying expectations for geometry**

I'm working on understanding the geometry elements needed for a specific scene. I think I need to list each element's name and attributes in a single line. No claims about verification are necessary; I just want to make sure the scene file is clear. My key expectations are that the "pendulum touches the ball" and that "the ball comes to rest in the cup." It feels straightforward, but I want to ensure I get it right!