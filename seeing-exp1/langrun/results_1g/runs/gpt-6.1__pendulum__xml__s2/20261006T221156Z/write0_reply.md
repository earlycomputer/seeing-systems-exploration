```xml
<mujoco model="pendulum_ball_cup">
  <compiler angle="radian"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" cone="elliptic" iterations="80"/>
  <size nconmax="200" njmax="1000"/>

  <visual>
    <headlight ambient="0.4 0.4 0.4" diffuse="0.7 0.7 0.7"/>
  </visual>

  <worldbody>
    <light name="light" pos="0.5 -1 3" dir="0 0 -1"/>
    <camera name="overview" pos="0.5 -3 1.8" xyaxes="1 0 0 0 0.5 0.866"/>

    <geom name="floor" type="plane" size="3 2 0.1" rgba="0.75 0.77 0.8 1" condim="6" friction="0.6 0.005 0.0008" solref="0.008 1"/>

    <body name="pendulum_support" pos="-0.114 0.16 0">
      <geom name="support_column" type="box" pos="0 0 0.285" size="0.025 0.025 0.285" rgba="0.3 0.32 0.35 1"/>
      <geom name="support_axle" type="capsule" fromto="0 0 0.57 0 -0.19 0.57" size="0.018" rgba="0.3 0.32 0.35 1" contype="0" conaffinity="0"/>
    </body>

    <body name="pendulum" pos="-0.114 0 0.57">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" damping="0.006"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 -0.025 0 0 -0.44" size="0.012" mass="0.015" rgba="0.55 0.57 0.6 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.065" mass="0.2" rgba="0.8 0.3 0.12 1" condim="6" friction="0.5 0.005 0.0008" solref="0.006 1"/>
    </body>

    <body name="ball" pos="0 0 0.05">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.05" mass="0.06" rgba="0.95 0.78 0.12 1" condim="6" friction="0.6 0.005 0.0008" solref="0.008 1"/>
    </body>

    <body name="ramp" pos="0.765 0 0.014">
      <geom name="ramp" type="box" size="0.108 0.065 0.004" quat="0.997226 0 -0.074438 0" rgba="0.4 0.6 0.65 1" condim="6" friction="0.65 0.005 0.001" solref="0.008 1"/>
    </body>

    <!-- The cup's reference centre is exactly 1 m from the ball's initial centre. -->
    <!-- Three low front rim segments let the entry ramp lead into the cup. -->
    <body name="cup" pos="1 0 0.05">
      <geom name="cup_base" type="cylinder" pos="0 0 -0.0425" size="0.195 0.0075" rgba="0.15 0.45 0.7 1" priority="1" condim="6" friction="0.9 0.01 0.018" solref="0.006 1"/>

      <geom name="cup_wall_00" type="box" pos="0.18 0 0.04" size="0.012 0.037 0.09" euler="0 0 0" rgba="0.2 0.55 0.8 1" priority="1" condim="6" friction="0.9 0.01 0.018" solref="0.006 1"/>
      <geom name="cup_wall_01" type="box" pos="0.166298 0.068883 0.04" size="0.012 0.037 0.09" euler="0 0 0.392699" rgba="0.2 0.55 0.8 1" priority="1" condim="6" friction="0.9 0.01 0.018" solref="0.006 1"/>
      <geom name="cup_wall_02" type="box" pos="0.127279 0.127279 0.04" size="0.012 0.037 0.09" euler="0 0 0.785398" rgba="0.2 0.55 0.8 1" priority="1" condim="6" friction="0.9 0.01 0.018" solref="0.006 1"/>
      <geom name="cup_wall_03" type="box" pos="0.068883 0.166298 0.04" size="0.012 0.037 0.09" euler="0 0 1.178097" rgba="0.2 0.55 0.8 1" priority="1" condim="6" friction="0.9 0.01 0.018" solref="0.006 1"/>
      <geom name="cup_wall_04" type="box" pos="0 0.18 0.04" size="0.012 0.037 0.09" euler="0 0 1.570796" rgba="0.2 0.55 0.8 1" priority="1" condim="6" friction="0.9 0.01 0.018" solref="0.006 1"/>
      <geom name="cup_wall_05" type="box" pos="-0.068883 0.166298 0.04" size="0.012 0.037 0.09" euler="0 0 1.963495" rgba="0.2 0.55 0.8 1" priority="1" condim="6" friction="0.9 0.01 0.018" solref="0.006 1"/>
      <geom name="cup_wall_06" type="box" pos="-0.127279 0.127279 0.04" size="0.012 0.037 0.09" euler="0 0 2.356194" rgba="0.2 0.55 0.8 1" priority="1" condim="6" friction="0.9 0.01 0.018" solref="0.006 1"/>

      <geom name="cup_wall_07" type="box" pos="-0.166298 0.068883 -0.0375" size="0.012 0.037 0.0125" euler="0 0 2.748894" rgba="0.2 0.55 0.8 1" condim="6" friction="0.65 0.005 0.001" solref="0.008 1"/>
      <geom name="cup_wall_08" type="box" pos="-0.18 0 -0.0375" size="0.012 0.037 0.0125" euler="0 0 3.141593" rgba="0.2 0.55 0.8 1" condim="6" friction="0.65 0.005 0.001" solref="0.008 1"/>
      <geom name="cup_wall_09" type="box" pos="-0.166298 -0.068883 -0.0375" size="0.012 0.037 0.0125" euler="0 0 3.534292" rgba="0.2 0.55 0.8 1" condim="6" friction="0.65 0.005 0.001" solref="0.008 1"/>

      <geom name="cup_wall_10" type="box" pos="-0.127279 -0.127279 0.04" size="0.012 0.037 0.09" euler="0 0 3.926991" rgba="0.2 0.55 0.8 1" priority="1" condim="6" friction="0.9 0.01 0.018" solref="0.006 1"/>
      <geom name="cup_wall_11" type="box" pos="-0.068883 -0.166298 0.04" size="0.012 0.037 0.09" euler="0 0 4.319690" rgba="0.2 0.55 0.8 1" priority="1" condim="6" friction="0.9 0.01 0.018" solref="0.006 1"/>
      <geom name="cup_wall_12" type="box" pos="0 -0.18 0.04" size="0.012 0.037 0.09" euler="0 0 4.712389" rgba="0.2 0.55 0.8 1" priority="1" condim="6" friction="0.9 0.01 0.018" solref="0.006 1"/>
      <geom name="cup_wall_13" type="box" pos="0.068883 -0.166298 0.04" size="0.012 0.037 0.09" euler="0 0 5.105088" rgba="0.2 0.55 0.8 1" priority="1" condim="6" friction="0.9 0.01 0.018" solref="0.006 1"/>
      <geom name="cup_wall_14" type="box" pos="0.127279 -0.127279 0.04" size="0.012 0.037 0.09" euler="0 0 5.497787" rgba="0.2 0.55 0.8 1" priority="1" condim="6" friction="0.9 0.01 0.018" solref="0.006 1"/>
      <geom name="cup_wall_15" type="box" pos="0.166298 -0.068883 0.04" size="0.012 0.037 0.09" euler="0 0 5.890486" rgba="0.2 0.55 0.8 1" priority="1" condim="6" friction="0.9 0.01 0.018" solref="0.006 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.8 0 0 0.05 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
pendulum touches ball
ball touches floor
ball touches ramp
ball comes to rest in cup
```

---
thinking (summarized):

**Designing a pendulum scenario**

I’m thinking about building a physical scenario using tools, potentially for a pendulum ball and cup setup. I need to capture a 1m drop. I have a budget to work with, and it seems I have enough resources available. I want to simulate this mentally first, with a focus on designing a robust cup. It should have an opening that directs the ball into an elevated position. I’ll need to consider aspects like friction and incline for the ball to roll effectively into the cup.

**Constructing a pendulum cup design**

I'm considering if I can design a cup that stands upright using a polygon of boxes with a flat base and a small ramp for the ball to roll into it. I need to think about the pendulum's impulse, including options for the ball's radius and mass, along with the pendulum's length and bob specifications. 

The alignment on impact is crucial, and I need to ensure everything balances correctly, taking into account various component dimensions to get the pendulum and ball to function together effectively.

**Analyzing pendulum motion**

I’m delving into the pendulum setup and considering the release angle theta, maybe around -0.65. I need to think about the hinge axis and how the rod moves in relation to the vectors. A small change in theta could affect the bob's position to the left. If I choose a positive value like 0.6, the calculations show the ball's speed before striking might be around 1.43 m/s, but I need to assess if that's enough for 1m travel considering friction.

**Considering cup design**

I want to create a file for a cup that’s aesthetically centered, with a geometric U shape and a front opening at the lower sill. The conventional cup should be upright with a small ramp near the front rim. I’m thinking about a shallow pouring design where the back wall is tall to prevent the ball from rolling over it. I also wonder if a recessed cup into the floor plane is an option, but that might be tricky.

**Exploring floor plane design**

I'm considering an infinite floor plane that doesn’t allow for below. To support the floor grid boxes, there would be a cup hole, with a recessed interior of -0.12. This keeps the cup rim at the floor level of z0. When the pendulum hits the ball, it should channel into the recessed cup. The geometry of this cup would have cylindrical sidewalls. I'm pondering whether using a truncated plane could work, but it seems more appropriate to have a side-lying cup with a circular cavity.

**Designing the cup structure**

I'm planning a horizontal cylinder for the cup, made up of multiple capsules or boxes along the x-axis from 0.85 to 1.15, with a radial layout in the y-z dimensions. The rear cap of the cylinder opens at x 0.85, and its outer radius is 0.125, sitting at the bottom level of z0. The ball enters at a height of z 0.04 and will face a small step at the inner shell's bottom at z 0.015, with a ramp of 0.015 ensuring it encounters significant friction at the cap and base.

**Considering ramp design**

I'm looking into the ramp’s design: it sees a controlled descent onto the base after the ramp ends. The cup base spans certain dimensions, and I need to make sure they overlap correctly. The ball enters at a specific position once it fits. 

There are also considerations for using ring cylinders, how to segment them, and the angles involved. I’m calculating to ensure that the ball fits properly within the design. It’s all about getting those dimensions right!

**Considering geometric calculations**

I need to evaluate how the body origins are working with the cup's geometric center. Specifically, I'm looking at the vertical positions of the cup versus a ball. The cup has a measurement of 1 meter, while the ball is at 0.5. I'm curious if they assess the cup's body position by examining the x and y displacements, while also factoring in the z-axis. There's a lot to consider in ensuring this is accurate!