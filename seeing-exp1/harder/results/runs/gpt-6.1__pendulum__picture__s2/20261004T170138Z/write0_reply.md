```xml
<mujoco model="pendulum_ball_cup">
  <compiler angle="degree" autolimits="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="80" cone="elliptic"/>

  <visual>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.65 0.65 0.65" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="0.4 -1.5 3" dir="0 0 -1"/>
    <camera name="overview" pos="1.7 -2.7 1.7" xyaxes="0.92 0.39 0 -0.19 0.45 0.87"/>

    <geom name="floor" type="plane" size="4 3 0.1" rgba="0.82 0.83 0.85 1" condim="6" friction="0.7 0.005 0.0002" solref="0.008 1"/>

    <!-- The support is visual only; the hinge supplies the fixed suspension. -->
    <body name="support">
      <geom name="support_left" type="capsule" fromto="-0.07 -0.22 0.02 -0.07 -0.22 0.565" size="0.018" rgba="0.3 0.32 0.35 1" contype="0" conaffinity="0"/>
      <geom name="support_right" type="capsule" fromto="-0.07 0.22 0.02 -0.07 0.22 0.565" size="0.018" rgba="0.3 0.32 0.35 1" contype="0" conaffinity="0"/>
      <geom name="support_crossbar" type="capsule" fromto="-0.07 -0.22 0.565 -0.07 0.22 0.565" size="0.018" rgba="0.3 0.32 0.35 1" contype="0" conaffinity="0"/>
    </body>

    <!-- A positive initial hinge angle raises the bob to the left. -->
    <body name="pendulum" pos="-0.07 0 0.565">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" damping="0.012"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.5" size="0.009" mass="0.025" rgba="0.35 0.37 0.4 1" friction="0.3 0.003 0.0001"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.06" mass="0.2" rgba="0.85 0.25 0.12 1" condim="6" friction="0.4 0.003 0.0001" solref="0.006 1"/>
    </body>

    <body name="ball" pos="0 0 0.04">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" rgba="0.95 0.75 0.12 1" condim="6" friction="0.7 0.005 0.0002" solref="0.006 1"/>
    </body>

    <!-- Cup centre is exactly 1 m from the ball's starting centre in plan.
         A shallow ramp crosses the lowered front rim; the remaining rim
         is tall enough to retain the ball after it strikes the back wall. -->
    <body name="cup" pos="1 0 0">
      <geom name="cup_bottom" type="cylinder" pos="0 0 0.006" size="0.158 0.006" rgba="0.15 0.45 0.75 1" condim="6" friction="0.7 0.005 0.0002" solref="0.012 1"/>
      <geom name="cup_entry_ramp" type="box" pos="-0.205 0 0.008" euler="0 -9.7 0" size="0.065 0.065 0.003" rgba="0.15 0.45 0.75 1" condim="6" friction="0.7 0.005 0.0002" solref="0.012 1"/>

      <geom name="cup_wall_00" type="box" pos="0.15 0 0.067" euler="0 0 90" size="0.032 0.008 0.055" rgba="0.15 0.45 0.75 1" solref="0.012 1"/>
      <geom name="cup_wall_01" type="box" pos="0.138582 0.057403 0.067" euler="0 0 112.5" size="0.032 0.008 0.055" rgba="0.15 0.45 0.75 1" solref="0.012 1"/>
      <geom name="cup_wall_02" type="box" pos="0.106066 0.106066 0.067" euler="0 0 135" size="0.032 0.008 0.055" rgba="0.15 0.45 0.75 1" solref="0.012 1"/>
      <geom name="cup_wall_03" type="box" pos="0.057403 0.138582 0.067" euler="0 0 157.5" size="0.032 0.008 0.055" rgba="0.15 0.45 0.75 1" solref="0.012 1"/>
      <geom name="cup_wall_04" type="box" pos="0 0.15 0.067" euler="0 0 180" size="0.032 0.008 0.055" rgba="0.15 0.45 0.75 1" solref="0.012 1"/>
      <geom name="cup_wall_05" type="box" pos="-0.057403 0.138582 0.067" euler="0 0 202.5" size="0.032 0.008 0.055" rgba="0.15 0.45 0.75 1" solref="0.012 1"/>
      <geom name="cup_wall_06" type="box" pos="-0.106066 0.106066 0.067" euler="0 0 225" size="0.032 0.008 0.055" rgba="0.15 0.45 0.75 1" solref="0.012 1"/>

      <geom name="cup_front_rim_07" type="box" pos="-0.138582 0.057403 0.017" euler="0 0 247.5" size="0.032 0.008 0.005" rgba="0.15 0.45 0.75 1" solref="0.012 1"/>
      <geom name="cup_front_rim_08" type="box" pos="-0.15 0 0.017" euler="0 0 270" size="0.032 0.008 0.005" rgba="0.15 0.45 0.75 1" solref="0.012 1"/>
      <geom name="cup_front_rim_09" type="box" pos="-0.138582 -0.057403 0.017" euler="0 0 292.5" size="0.032 0.008 0.005" rgba="0.15 0.45 0.75 1" solref="0.012 1"/>

      <geom name="cup_wall_10" type="box" pos="-0.106066 -0.106066 0.067" euler="0 0 315" size="0.032 0.008 0.055" rgba="0.15 0.45 0.75 1" solref="0.012 1"/>
      <geom name="cup_wall_11" type="box" pos="-0.057403 -0.138582 0.067" euler="0 0 337.5" size="0.032 0.008 0.055" rgba="0.15 0.45 0.75 1" solref="0.012 1"/>
      <geom name="cup_wall_12" type="box" pos="0 -0.15 0.067" euler="0 0 0" size="0.032 0.008 0.055" rgba="0.15 0.45 0.75 1" solref="0.012 1"/>
      <geom name="cup_wall_13" type="box" pos="0.057403 -0.138582 0.067" euler="0 0 22.5" size="0.032 0.008 0.055" rgba="0.15 0.45 0.75 1" solref="0.012 1"/>
      <geom name="cup_wall_14" type="box" pos="0.106066 -0.106066 0.067" euler="0 0 45" size="0.032 0.008 0.055" rgba="0.15 0.45 0.75 1" solref="0.012 1"/>
      <geom name="cup_wall_15" type="box" pos="0.138582 -0.057403 0.067" euler="0 0 67.5" size="0.032 0.008 0.055" rgba="0.15 0.45 0.75 1" solref="0.012 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.65 0 0 0.04 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Designing a pendulum system**

I need to create a setup for a pendulum that strikes a ball and rolls it into a cup, positioned 1 meter away from the starting point. Since I can’t use simulation tools, I’ll focus on a thoughtful physics design. My idea involves a pendulum swinging down to hit a ball on the floor. I’m contemplating different cup designs, ensuring the entry is low enough for the ball to climb in easily. The dimensions of the cup need consideration, perhaps resembling a cylindrical bowl with sloped walls.

**Designing the cup and pendulum system**

I need to consider that the ball speed is around 1 m/s when it travels 1 meter, and friction losses should be minimal. The cup needs a low front rim or gap to help the ball rise. My design involves a circular cup with inclined ramps formed by 360-degree box segments. A flat base of height .003 will support a main cylinder that can be .16 in radius. For the pendulum, I’ll ensure the hinge pivot and bob position are optimized for striking the ball effectively.

**Configuring the pendulum system**

I’m working on the pendulum setup, and I note that the pivot point has a length of .50 and is positioned at z .57, which gives a center minimum of .07. The ball’s radius is .05 and is centered accordingly. The bob striker will be at x -0.10 while the bob height is z .071, ensuring the ball is slightly downward. I need to carefully consider angles and gravity's effect on the pendulum’s motion throughout the design process.

**Planning wall dimensions**

I'm working on the wall dimensions. I need a front lip that's .022 high from the floor, with a radius less than .04 to make climbing easier. The ramp should be .022 high as well. The back wall will be .10 tall, while the front rim will be lower. For the front box, I can make the top .02, the bottom .012, and the other walls at .10. Let’s keep these specifications in mind!