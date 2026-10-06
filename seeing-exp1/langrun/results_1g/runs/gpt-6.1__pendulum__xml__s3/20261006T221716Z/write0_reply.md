```xml
<mujoco model="pendulum_ball_and_cup">
  <compiler angle="radian" inertiafromgeom="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" iterations="80"/>
  <size njmax="500" nconmax="200"/>

  <visual>
    <headlight ambient="0.4 0.4 0.4" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="scene_light" pos="0.5 -2 3" dir="0 0 -1"/>
    <camera name="overview" pos="0.5 -2.7 1.7" xyaxes="1 0 0 0 0.5 0.8660254"/>
    <geom name="floor" type="plane" size="4 3 0.1" friction="0.65 0.005 0.0008" condim="6" rgba="0.72 0.75 0.78 1"/>

    <body name="pendulum" pos="-0.095 0 0.71">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" damping="0.012"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 -0.015 0 0 -0.65" size="0.012" mass="0.035" friction="0.5 0.005 0.0005" rgba="0.32 0.35 0.4 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.65" size="0.055" mass="0.3" friction="0.5 0.005 0.0005" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.8 0.3 0.15 1"/>
    </body>

    <body name="ball" pos="0 0 0.045">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.045" mass="0.07" friction="0.65 0.005 0.0008" condim="6" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.95 0.75 0.12 1"/>
    </body>

    <body name="cup" pos="1 0 0">
      <geom name="cup_base" type="cylinder" pos="0 0 0.004" size="0.184 0.004" friction="0.9 0.005 0.002" condim="6" solref="0.008 1" rgba="0.15 0.45 0.65 1"/>
      <geom name="cup_front_lip" type="box" pos="-0.16 0 0.03" size="0.015 0.0662742 0.03" friction="0.9 0.005 0.002" condim="6" solref="0.008 1" rgba="0.15 0.45 0.65 1"/>
      <geom name="cup_back" type="box" pos="0.16 0 0.07" size="0.015 0.0662742 0.07" friction="0.9 0.005 0.002" condim="6" solref="0.008 1" rgba="0.15 0.45 0.65 1"/>
      <geom name="cup_left" type="box" pos="0 0.16 0.07" size="0.0662742 0.015 0.07" friction="0.9 0.005 0.002" condim="6" solref="0.008 1" rgba="0.15 0.45 0.65 1"/>
      <geom name="cup_right" type="box" pos="0 -0.16 0.07" size="0.0662742 0.015 0.07" friction="0.9 0.005 0.002" condim="6" solref="0.008 1" rgba="0.15 0.45 0.65 1"/>
      <geom name="cup_front_left" type="box" pos="-0.1131371 0.1131371 0.07" euler="0 0 0.7853981634" size="0.0662742 0.015 0.07" friction="0.9 0.005 0.002" condim="6" solref="0.008 1" rgba="0.15 0.45 0.65 1"/>
      <geom name="cup_front_right" type="box" pos="-0.1131371 -0.1131371 0.07" euler="0 0 -0.7853981634" size="0.0662742 0.015 0.07" friction="0.9 0.005 0.002" condim="6" solref="0.008 1" rgba="0.15 0.45 0.65 1"/>
      <geom name="cup_back_left" type="box" pos="0.1131371 0.1131371 0.07" euler="0 0 -0.7853981634" size="0.0662742 0.015 0.07" friction="0.9 0.005 0.002" condim="6" solref="0.008 1" rgba="0.15 0.45 0.65 1"/>
      <geom name="cup_back_right" type="box" pos="0.1131371 -0.1131371 0.07" euler="0 0 0.7853981634" size="0.0662742 0.015 0.07" friction="0.9 0.005 0.002" condim="6" solref="0.008 1" rgba="0.15 0.45 0.65 1"/>
      <geom name="cup_ramp" type="box" pos="-0.2935448 0 0.0241791" euler="0 -0.2449786631 0" size="0.1236932 0.06 0.006" friction="0.8 0.005 0.0008" condim="6" solref="0.008 1" rgba="0.25 0.55 0.7 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.8 0 0 0.045 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
pendulum touches ball
ball touches cup_ramp
ball comes to rest in cup
```

---
thinking (summarized):

**Calculating cup geometry**

I'm working on the geometry for a cup. I’ve got a ball with a radius of 0.04 that can pass through if the entry rim is at 0.03, while the ramp rises to 0.03, making it quite easy. I need to ensure the cup's geometry matches, naming the ramp as "cup_ramp." For the cup base, the top should be at z = 0.005, and the wall height at 0.10. The front rim's x-value is 0.82, with the ramp starting at 0.65 and ending at 0.86, rising 0.085. The ball can climb 0.10, needing potential energy at 0.9 for speed on impact greater than 1.3. Finally, the back wall is needed to hold the cup in place.

**Calculating ball dynamics**

I'm trying to understand the ball's movement. The center will roll over the ramp at a height of 0.85, and then there's a drop of 0.045 into the base. I need to make sure I consider how the height affects the ball's speed and trajectory. Each part of the ramp and drop should be taken into account to get an accurate picture of how this all works together. It’s interesting to think about the physics involved!

**Evaluating ball dynamics**

I'm thinking about the situation where a ball hits the rear wall at a high velocity. It seems if it does that, it can't escape over the top because of the wall height, which is 0.14 meters. The ball’s center is at 0.048 meters, so climbing over is impossible without a speed close to 1 m/s. Plus, a horizontal collision usually comes to a stop. There’s a lot to consider here with the physics involved!

**Adjusting sphere parameters**

I'm thinking about the center height, which is at a minimum of .055 for no penetration. The default contact margin is zero, so the sphere might only touch the floor briefly. If I raise the bob's bottom by .01, making the center .065 with a downward impulse of .263, it could be a bit stronger. I also want to adjust the ball's radius to .045 with the head at .055 for the total to sum correctly.

**Evaluating contact stiffness**

I’m thinking about the contact stiffness, and I wonder if I need a softer time constant of .008 for the ball and pendulum to transfer some restitution. It might also involve the default damper ratio of 1. I’m considering what happens to the ball's velocity after it collides with a rigid object; does it come to a stop after that impact? There’s definitely a lot to sort through to ensure I get the settings right here.