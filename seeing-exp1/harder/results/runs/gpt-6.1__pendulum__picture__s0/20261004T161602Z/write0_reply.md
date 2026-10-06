```xml
<mujoco model="pendulum_ball_cup">
  <compiler angle="radian" inertiafromgeom="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" cone="elliptic" iterations="100"/>
  <size nconmax="200" njmax="1000"/>

  <visual>
    <global azimuth="125" elevation="-25"/>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="0.5 -1 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <camera name="overview" pos="1.7 -2.8 1.6" xyaxes="0.925 0.380 0 -0.165 0.402 0.901"/>

    <geom name="floor" type="plane" pos="0 0 0" size="3 2 0.1" condim="6" friction="0.35 0.001 0.00001" solref="0.008 1" rgba="0.75 0.78 0.80 1"/>

    <body name="support">
      <geom name="support_left" type="capsule" fromto="-0.09 -0.15 0.015 -0.09 -0.15 0.64" size="0.012" contype="0" conaffinity="0" rgba="0.25 0.28 0.32 1"/>
      <geom name="support_right" type="capsule" fromto="-0.09 0.15 0.015 -0.09 0.15 0.64" size="0.012" contype="0" conaffinity="0" rgba="0.25 0.28 0.32 1"/>
      <geom name="support_axle" type="capsule" fromto="-0.09 -0.17 0.64 -0.09 0.17 0.64" size="0.012" contype="0" conaffinity="0" rgba="0.25 0.28 0.32 1"/>
    </body>

    <!-- The raised initial angle supplies the strike energy through gravity. -->
    <body name="pendulum" pos="-0.09 0 0.64">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" damping="0.0001"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.54" size="0.007" mass="0.003" friction="0.25 0.001 0.00001" solref="0.008 1" rgba="0.30 0.32 0.35 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.59" size="0.045" mass="0.04" friction="0.25 0.001 0.00001" solref="0.008 1" rgba="0.85 0.25 0.12 1"/>
    </body>

    <body name="ball" pos="0 0 0.04">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.06" condim="6" friction="0.35 0.001 0.00001" solref="0.008 1" rgba="0.95 0.75 0.12 1"/>
    </body>

    <!-- Centre is exactly 1 m from the ball's starting centre in the floor plane.
         Three lowered rim segments provide a rolling entrance.
         Rolling resistance on the cup bottom brings the ball to rest inside. -->
    <body name="cup" pos="1 0 0">
      <geom name="cup_bottom" type="cylinder" pos="0 0 0.001" size="0.152 0.001" condim="6" friction="0.7 0.005 0.0025" solref="0.008 1" rgba="0.18 0.52 0.75 1"/>

      <geom name="cup_wall_00" type="box" pos="0.146 0 0.045" size="0.006 0.0295 0.045" euler="0 0 0" friction="0.7 0.005 0.00001" solref="0.008 1" rgba="0.15 0.45 0.70 1"/>
      <geom name="cup_wall_01" type="box" pos="0.134886 0.055872 0.045" size="0.006 0.0295 0.045" euler="0 0 0.392699" friction="0.7 0.005 0.00001" solref="0.008 1" rgba="0.15 0.45 0.70 1"/>
      <geom name="cup_wall_02" type="box" pos="0.103238 0.103238 0.045" size="0.006 0.0295 0.045" euler="0 0 0.785398" friction="0.7 0.005 0.00001" solref="0.008 1" rgba="0.15 0.45 0.70 1"/>
      <geom name="cup_wall_03" type="box" pos="0.055872 0.134886 0.045" size="0.006 0.0295 0.045" euler="0 0 1.178097" friction="0.7 0.005 0.00001" solref="0.008 1" rgba="0.15 0.45 0.70 1"/>
      <geom name="cup_wall_04" type="box" pos="0 0.146 0.045" size="0.006 0.0295 0.045" euler="0 0 1.570796" friction="0.7 0.005 0.00001" solref="0.008 1" rgba="0.15 0.45 0.70 1"/>
      <geom name="cup_wall_05" type="box" pos="-0.055872 0.134886 0.045" size="0.006 0.0295 0.045" euler="0 0 1.963495" friction="0.7 0.005 0.00001" solref="0.008 1" rgba="0.15 0.45 0.70 1"/>
      <geom name="cup_wall_06" type="box" pos="-0.103238 0.103238 0.045" size="0.006 0.0295 0.045" euler="0 0 2.356194" friction="0.7 0.005 0.00001" solref="0.008 1" rgba="0.15 0.45 0.70 1"/>

      <geom name="cup_entry_07" type="box" pos="-0.134886 0.055872 0.002" size="0.006 0.0295 0.002" euler="0 0 2.748894" condim="6" friction="0.6 0.002 0.00001" solref="0.008 1" rgba="0.18 0.52 0.75 1"/>
      <geom name="cup_entry_08" type="box" pos="-0.146 0 0.002" size="0.006 0.0295 0.002" euler="0 0 3.141593" condim="6" friction="0.6 0.002 0.00001" solref="0.008 1" rgba="0.18 0.52 0.75 1"/>
      <geom name="cup_entry_09" type="box" pos="-0.134886 -0.055872 0.002" size="0.006 0.0295 0.002" euler="0 0 3.534292" condim="6" friction="0.6 0.002 0.00001" solref="0.008 1" rgba="0.18 0.52 0.75 1"/>

      <geom name="cup_wall_10" type="box" pos="-0.103238 -0.103238 0.045" size="0.006 0.0295 0.045" euler="0 0 3.926991" friction="0.7 0.005 0.00001" solref="0.008 1" rgba="0.15 0.45 0.70 1"/>
      <geom name="cup_wall_11" type="box" pos="-0.055872 -0.134886 0.045" size="0.006 0.0295 0.045" euler="0 0 4.319690" friction="0.7 0.005 0.00001" solref="0.008 1" rgba="0.15 0.45 0.70 1"/>
      <geom name="cup_wall_12" type="box" pos="0 -0.146 0.045" size="0.006 0.0295 0.045" euler="0 0 4.712389" friction="0.7 0.005 0.00001" solref="0.008 1" rgba="0.15 0.45 0.70 1"/>
      <geom name="cup_wall_13" type="box" pos="0.055872 -0.134886 0.045" size="0.006 0.0295 0.045" euler="0 0 5.105088" friction="0.7 0.005 0.00001" solref="0.008 1" rgba="0.15 0.45 0.70 1"/>
      <geom name="cup_wall_14" type="box" pos="0.103238 -0.103238 0.045" size="0.006 0.0295 0.045" euler="0 0 5.497787" friction="0.7 0.005 0.00001" solref="0.008 1" rgba="0.15 0.45 0.70 1"/>
      <geom name="cup_wall_15" type="box" pos="0.134886 -0.055872 0.045" size="0.006 0.0295 0.045" euler="0 0 5.890486" friction="0.7 0.005 0.00001" solref="0.008 1" rgba="0.15 0.45 0.70 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.55 0 0 0.04 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Calculating collision factors**

I’m looking at a collision involving two objects: a ball with mass .045 and a rod with a mass of .005. The coefficient of restitution is zero, leading me to calculate the final velocity of the ball after the collision to be roughly .51. I’m wondering about the speed of the ball (.4) and how it interacts with the cup, especially over a span of 2-3 seconds. There’s a lot to think through with the dynamics!

**Considering physical parameters**

I'm thinking about the hits on a wall where a bounce will have a low retention due to high friction. Since walls have a friction coefficient of .8 and won't bounce back (overdamped), the object will enter a cup with low rolling resistance and stop. I wonder if I need to consider specific joint names and configurations when computing the strike analytically. It seems like I need to ensure I've named each component correctly and used the right joint types.

**Evaluating friction dynamics**

I'm considering how the static body of a cup affects friction during mixing. There's a geometric factor depending on the sphere and floor dimensions. I note that the rolling friction coefficient is small but may exert high torque. The stopping deceleration looks to be around 0.44, which is quite fine. I wonder if I can guarantee the impact of the ball will be around 0.65! That could be useful information to refine my calculations.