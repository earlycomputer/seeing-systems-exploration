The cup lies on its side, with its open mouth facing the balls. The first ball starts with matching forward and rolling velocities.

```xml
<mujoco model="three_balls_into_cup">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" cone="elliptic" iterations="100"/>
  <statistic center="-0.15 0 0.12" extent="1.6"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.65 0.65 0.65" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="key_light" pos="-1 -2 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <camera name="overview" pos="-0.3 -2.8 1.65" xyaxes="1 0 0 0 0.47 0.883" fovy="40"/>
    <geom name="floor" type="plane" pos="0 0 0" size="3 2 0.1" rgba="0.78 0.79 0.81 1" condim="6" priority="1" friction="0.6 0.001 0.002" solref="0.006 1"/>

    <body name="ball1" pos="-1.1 0 0.0602">
      <freejoint name="ball1_free"/>
      <geom name="ball1_sphere" type="sphere" size="0.06" mass="0.15" rgba="0.9 0.2 0.12 1" condim="3" friction="0.02 0.001 0.0001" solref="0.02 0.15" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball2" pos="-0.6 0 0.0602">
      <freejoint name="ball2_free"/>
      <geom name="ball2_sphere" type="sphere" size="0.06" mass="0.15" rgba="0.48 0.25 0.8 1" condim="3" friction="0.02 0.001 0.0001" solref="0.02 0.15" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball3" pos="-0.1 0 0.0602">
      <freejoint name="ball3_free"/>
      <geom name="ball3_sphere" type="sphere" size="0.06" mass="0.15" rgba="1 0.73 0.08 1" condim="3" friction="0.02 0.001 0.0001" solref="0.02 0.15" solimp="0.95 0.99 0.001"/>
    </body>

    <!-- Local +z points toward the mouth; the body rotation points it toward world -x. -->
    <!-- The lowest inner wall lies just below the floor, leaving a level entrance. -->
    <body name="cup" pos="0.63 0 0.15" euler="0 -90 0">
      <geom name="cup_base" type="cylinder" pos="0 0 -0.265" size="0.185 0.015" rgba="0.08 0.35 0.55 1" priority="2" condim="6" friction="1 0.005 0.02" solref="0.006 1"/>

      <geom name="cup_wall00" type="box" pos="0.17 0 0" euler="0 0 0" size="0.015 0.037 0.25" rgba="0.1 0.5 0.8 0.6" priority="2" condim="6" friction="1 0.005 0.02" solref="0.006 1"/>
      <geom name="cup_wall01" type="box" pos="0.157060 0.065056 0" euler="0 0 22.5" size="0.015 0.037 0.25" rgba="0.1 0.5 0.8 0.6" priority="2" condim="6" friction="1 0.005 0.02" solref="0.006 1"/>
      <geom name="cup_wall02" type="box" pos="0.120208 0.120208 0" euler="0 0 45" size="0.015 0.037 0.25" rgba="0.1 0.5 0.8 0.6" priority="2" condim="6" friction="1 0.005 0.02" solref="0.006 1"/>
      <geom name="cup_wall03" type="box" pos="0.065056 0.157060 0" euler="0 0 67.5" size="0.015 0.037 0.25" rgba="0.1 0.5 0.8 0.6" priority="2" condim="6" friction="1 0.005 0.02" solref="0.006 1"/>
      <geom name="cup_wall04" type="box" pos="0 0.17 0" euler="0 0 90" size="0.015 0.037 0.25" rgba="0.1 0.5 0.8 0.6" priority="2" condim="6" friction="1 0.005 0.02" solref="0.006 1"/>
      <geom name="cup_wall05" type="box" pos="-0.065056 0.157060 0" euler="0 0 112.5" size="0.015 0.037 0.25" rgba="0.1 0.5 0.8 0.6" priority="2" condim="6" friction="1 0.005 0.02" solref="0.006 1"/>
      <geom name="cup_wall06" type="box" pos="-0.120208 0.120208 0" euler="0 0 135" size="0.015 0.037 0.25" rgba="0.1 0.5 0.8 0.6" priority="2" condim="6" friction="1 0.005 0.02" solref="0.006 1"/>
      <geom name="cup_wall07" type="box" pos="-0.157060 0.065056 0" euler="0 0 157.5" size="0.015 0.037 0.25" rgba="0.1 0.5 0.8 0.6" priority="2" condim="6" friction="1 0.005 0.02" solref="0.006 1"/>
      <geom name="cup_wall08" type="box" pos="-0.17 0 0" euler="0 0 180" size="0.015 0.037 0.25" rgba="0.1 0.5 0.8 0.6" priority="2" condim="6" friction="1 0.005 0.02" solref="0.006 1"/>
      <geom name="cup_wall09" type="box" pos="-0.157060 -0.065056 0" euler="0 0 202.5" size="0.015 0.037 0.25" rgba="0.1 0.5 0.8 0.6" priority="2" condim="6" friction="1 0.005 0.02" solref="0.006 1"/>
      <geom name="cup_wall10" type="box" pos="-0.120208 -0.120208 0" euler="0 0 225" size="0.015 0.037 0.25" rgba="0.1 0.5 0.8 0.6" priority="2" condim="6" friction="1 0.005 0.02" solref="0.006 1"/>
      <geom name="cup_wall11" type="box" pos="-0.065056 -0.157060 0" euler="0 0 247.5" size="0.015 0.037 0.25" rgba="0.1 0.5 0.8 0.6" priority="2" condim="6" friction="1 0.005 0.02" solref="0.006 1"/>
      <geom name="cup_wall12" type="box" pos="0 -0.17 0" euler="0 0 270" size="0.015 0.037 0.25" rgba="0.1 0.5 0.8 0.6" priority="2" condim="6" friction="1 0.005 0.02" solref="0.006 1"/>
      <geom name="cup_wall13" type="box" pos="0.065056 -0.157060 0" euler="0 0 292.5" size="0.015 0.037 0.25" rgba="0.1 0.5 0.8 0.6" priority="2" condim="6" friction="1 0.005 0.02" solref="0.006 1"/>
      <geom name="cup_wall14" type="box" pos="0.120208 -0.120208 0" euler="0 0 315" size="0.015 0.037 0.25" rgba="0.1 0.5 0.8 0.6" priority="2" condim="6" friction="1 0.005 0.02" solref="0.006 1"/>
      <geom name="cup_wall15" type="box" pos="0.157060 -0.065056 0" euler="0 0 337.5" size="0.015 0.037 0.25" rgba="0.1 0.5 0.8 0.6" priority="2" condim="6" friction="1 0.005 0.02" solref="0.006 1"/>

      <geom name="cup_handle_back" type="capsule" fromto="0 0.17 -0.13 0 0.28 -0.13" size="0.013" rgba="0.08 0.35 0.55 1" priority="2" friction="1 0.005 0.02" solref="0.006 1"/>
      <geom name="cup_handle_outer" type="capsule" fromto="0 0.28 -0.13 0 0.28 0.13" size="0.013" rgba="0.08 0.35 0.55 1" priority="2" friction="1 0.005 0.02" solref="0.006 1"/>
      <geom name="cup_handle_front" type="capsule" fromto="0 0.28 0.13 0 0.17 0.13" size="0.013" rgba="0.08 0.35 0.55 1" priority="2" friction="1 0.005 0.02" solref="0.006 1"/>
    </body>
  </worldbody>

  <contact>
    <pair name="ball1_floor_contact" geom1="ball1_sphere" geom2="floor" condim="6" friction="0.6 0.6 0.001 0.010 0.010" solref="0.006 1" solimp="0.95 0.99 0.001"/>
    <pair name="ball2_floor_contact" geom1="ball2_sphere" geom2="floor" condim="6" friction="0.6 0.6 0.001 0.007 0.007" solref="0.006 1" solimp="0.95 0.99 0.001"/>
    <pair name="ball3_floor_contact" geom1="ball3_sphere" geom2="floor" condim="6" friction="0.6 0.6 0.001 0.002 0.002" solref="0.006 1" solimp="0.95 0.99 0.001"/>
  </contact>

  <keyframe>
    <key name="start" qpos="-1.1 0 0.0602 1 0 0 0  -0.6 0 0.0602 1 0 0 0  -0.1 0 0.0602 1 0 0 0" qvel="3.8 0 0 0 63.333333 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
ball1 touches ball2
ball2 touches ball3
ball3 comes to rest in cup
```

---
thinking (summarized):

**Assessing rolling speed and collisions**

I'm analyzing the initial speed of Ball1, which is 4, while exploring mass relationships between b1, b2, and b3. I'm considering whether all balls can push into the cup without violating constraints. The collisions might follow a Newton's cradle model, and I’m wondering if using a ramp with a slight incline, making balls very small, could maintain sufficient velocities. I need to calculate the necessary speed, and it looks like V3 isn't hitting the needed velocity just yet.

**Evaluating energy factors**

I'm thinking through the energy requirements for rotation in my calculations. I'm starting with a speed of 3.3, and considering the contact elasticity around 0.7. There's also a floor slip acceleration that decreases speed — it seems to be around negative 3.5 before collisions, with a spacing of about 0.25. I need to ensure I balance these elements correctly to get my desired results.

**Evaluating cup design parameters**

I’m working on a cup design with a ramp rise of .115 and a cup radius of .28, with impact occurring below the rim. All walls are around .30, except for the front lip, which is .11. It seems like a notched cup with a funnel ramp could work. I'm also thinking about an alternative cup design laid on its side with a horizontal ball entry. I need to ensure everything is reliable and straightforward visually, just keeping it simple.

**Exploring cup design adjustments**

I'm considering whether to add an entry that slopes or set lower segments on the cup wall so it can remain open until a certain point. The cup would be laid on its side, allowing a ball to roll horizontally inside. I think I could arrange the cup body at a 90-degree yaw. The interior design has an .008 threshold, but I'm worried that might cause the ball to get stuck. I also need to check if the wall intrusion will interfere with the placement.

**Calculating coordinates for rings**

I'm looking at rings with box sizes of ".015", ".034", and ".25", which I need to rotate about the local Z-axis to get the radial normal along the local X-axis. For each position, I'm calculating the coordinates as follows: the local X is at ".17 * cos(θ)" and the local Y at ".17 * sin(θ)". It feels a bit mathematical, but getting these coordinates right is essential for clarity!