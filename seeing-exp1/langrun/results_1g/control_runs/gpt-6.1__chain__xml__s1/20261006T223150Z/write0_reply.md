The cup lies on its side, with its open mouth facing the balls. The `start` keyframe gives only the first ball an initial rolling velocity.

```xml
<mujoco model="three_balls_into_cup">
  <compiler angle="radian"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" cone="elliptic" iterations="100" impratio="5"/>
  <size nconmax="200" njmax="1000"/>
  <statistic center="0.15 0 0.12" extent="1.8"/>

  <visual>
    <global azimuth="140" elevation="-25"/>
    <headlight ambient="0.4 0.4 0.4" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
    <rgba haze="0.85 0.88 0.92 1"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="-0.3 -1.2 3" dir="0.1 0.3 -1" diffuse="0.8 0.8 0.8"/>
    <camera name="overview" mode="targetbody" target="cup" pos="-1.8 -2.4 1.5"/>

    <geom name="floor" type="plane" size="4 3 0.1" pos="0 0 0" rgba="0.78 0.80 0.82 1" condim="6" priority="1" friction="0.65 0.004 0.0015" solref="0.008 1" solimp="0.95 0.99 0.001"/>

    <body name="ball1" pos="-0.65 0 0.06">
      <freejoint name="ball1_free"/>
      <geom name="ball1_sphere" type="sphere" size="0.06" density="500" rgba="0.85 0.12 0.10 1" condim="3" friction="0.05 0.001 0.0015" solref="-60000 -18" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball2" pos="-0.23 0 0.06">
      <freejoint name="ball2_free"/>
      <geom name="ball2_sphere" type="sphere" size="0.06" density="500" rgba="0.95 0.66 0.08 1" condim="3" friction="0.05 0.001 0.0015" solref="-60000 -18" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball3" pos="0.13 0 0.06">
      <freejoint name="ball3_free"/>
      <geom name="ball3_sphere" type="sphere" size="0.06" density="500" rgba="0.12 0.30 0.90 1" condim="3" friction="0.05 0.001 0.0015" solref="-60000 -18" solimp="0.95 0.99 0.001"/>
    </body>

    <!-- A hollow, twelve-sided cup lying along x, open toward -x. -->
    <body name="cup" pos="0.755 0 0.16">
      <geom name="cup_wall_00" type="box" size="0.275 0.049 0.010" pos="0 0 0.17" quat="1 0 0 0" rgba="0.22 0.52 0.48 1" condim="6" priority="2" friction="0.65 0.004 0.0015" solref="0.008 1"/>
      <geom name="cup_wall_01" type="box" size="0.275 0.049 0.010" pos="0 -0.085 0.147224" quat="0.9659258 0.2588190 0 0" rgba="0.22 0.52 0.48 1" condim="6" priority="2" friction="0.65 0.004 0.0015" solref="0.008 1"/>
      <geom name="cup_wall_02" type="box" size="0.275 0.049 0.010" pos="0 -0.147224 0.085" quat="0.8660254 0.5 0 0" rgba="0.22 0.52 0.48 1" condim="6" priority="2" friction="0.65 0.004 0.0015" solref="0.008 1"/>
      <geom name="cup_wall_03" type="box" size="0.275 0.049 0.010" pos="0 -0.17 0" quat="0.7071068 0.7071068 0 0" rgba="0.22 0.52 0.48 1" condim="6" priority="2" friction="0.65 0.004 0.0015" solref="0.008 1"/>
      <geom name="cup_wall_04" type="box" size="0.275 0.049 0.010" pos="0 -0.147224 -0.085" quat="0.5 0.8660254 0 0" rgba="0.22 0.52 0.48 1" condim="6" priority="2" friction="0.65 0.004 0.0015" solref="0.008 1"/>
      <geom name="cup_wall_05" type="box" size="0.275 0.049 0.010" pos="0 -0.085 -0.147224" quat="0.2588190 0.9659258 0 0" rgba="0.22 0.52 0.48 1" condim="6" priority="2" friction="0.65 0.004 0.0015" solref="0.008 1"/>
      <geom name="cup_wall_06" type="box" size="0.275 0.049 0.010" pos="0 0 -0.17" quat="0 1 0 0" rgba="0.22 0.52 0.48 1" condim="6" priority="2" friction="0.65 0.004 0.0015" solref="0.008 1"/>
      <geom name="cup_wall_07" type="box" size="0.275 0.049 0.010" pos="0 0.085 -0.147224" quat="0.2588190 -0.9659258 0 0" rgba="0.22 0.52 0.48 1" condim="6" priority="2" friction="0.65 0.004 0.0015" solref="0.008 1"/>
      <geom name="cup_wall_08" type="box" size="0.275 0.049 0.010" pos="0 0.147224 -0.085" quat="0.5 -0.8660254 0 0" rgba="0.22 0.52 0.48 1" condim="6" priority="2" friction="0.65 0.004 0.0015" solref="0.008 1"/>
      <geom name="cup_wall_09" type="box" size="0.275 0.049 0.010" pos="0 0.17 0" quat="0.7071068 -0.7071068 0 0" rgba="0.22 0.52 0.48 1" condim="6" priority="2" friction="0.65 0.004 0.0015" solref="0.008 1"/>
      <geom name="cup_wall_10" type="box" size="0.275 0.049 0.010" pos="0 0.147224 0.085" quat="0.8660254 -0.5 0 0" rgba="0.22 0.52 0.48 1" condim="6" priority="2" friction="0.65 0.004 0.0015" solref="0.008 1"/>
      <geom name="cup_wall_11" type="box" size="0.275 0.049 0.010" pos="0 0.085 0.147224" quat="0.9659258 -0.2588190 0 0" rgba="0.22 0.52 0.48 1" condim="6" priority="2" friction="0.65 0.004 0.0015" solref="0.008 1"/>

      <!-- A nearly flush interior landing surface dissipates rolling motion. -->
      <geom name="cup_landing" type="box" size="0.23 0.065 0.005" pos="0.035 0 -0.164" rgba="0.18 0.43 0.39 1" condim="6" priority="2" friction="0.8 0.004 0.006" solref="0.008 1"/>
      <geom name="cup_base" type="cylinder" size="0.182 0.015" pos="0.29 0 0" quat="0.7071068 0 0.7071068 0" rgba="0.22 0.52 0.48 1" condim="6" priority="2" friction="0.8 0.004 0.006" solref="0.008 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-0.65 0 0.06 1 0 0 0  -0.23 0 0.06 1 0 0 0  0.13 0 0.06 1 0 0 0" qvel="1.9 0 0 0 31.6666667 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Analyzing momentum transfer**

I'm thinking about contact friction and restitution, particularly with high elasticity. Using solref values like ".004" and ".15" can be tricky. I calculated that the bounce restitution is approximately .62 for a ζ of .15. I want to set up a Newton's cradle, where I roll the first ball to the second and then to the third, ensuring there's enough momentum transfer happening. It's all about getting the physics just right!

**Analyzing cup and ball physics**

I’m working on the cup bottom's box center and its dimensions. I’m considering how it interacts with the ground and whether there’s an overlap that requires adjustments. The floor properties need priority settings for better interactions with the ball. I want to ensure no bounce between the ball and the floor while maintaining good simulations for collision dynamics. Overall, I have to ensure that everything functions harmoniously without any unexpected issues.

**Calculating ball dynamics**

I'm looking into the mechanics of ball contact with low sliding friction to minimize backspin, adjusting the coefficient of friction from .6 to .05 on the floor. This affects the tangent impulse and roll speed, with calculations showing a final speed for v1 at approximately .61. The speeds after collisions demonstrate how ball dynamics shift, particularly with different friction surfaces. The eventual stops and continued movements are important for understanding how the balls interact and affect each other.

**Evaluating ball dynamics**

I'm simulating the initial rolling behavior with a speed of v1.7, which seems sufficient even with low friction. The final speed comes out to be .56 after testing various collisions. I need to make sure to minimize the loss of initial angular velocity due to friction on the floor. The rolling coefficients for different surfaces are crucial to manage the interactions between balls effectively, especially with various friction settings for the floor, walls, and cup, ensuring smooth rolling dynamics.

**Tuning simulation parameters**

I'm working on setting options for an integrator with implicit fast cone elliptic iterations at 80. The timestep is set to .002, and I'm using a gravity value of -9.81. I want to see if a high impratio improves performance with no slip. It seems I need to adjust damping and stiffness for stability, especially for contact dynamics. I’m also considering negative stiffness values to improve yielding and impact response while ensuring everything stays well resolved and stable.

**Refining penetration parameters**

I’m evaluating soft penetration settings, aiming for about .012 m under certain conditions. With a high stiffness constant of 100,000 and damping at 50, I’ve got a damping ratio of .079 and an energy coefficient around .779. Time steps are set across five intervals, and I'm considering direct options for reliability. Using negative values seems to improve restitution. I also need to ensure adequate velocity and gap settings to accommodate various interactions without causing issues like bouncing. I’m keeping an eye on collision duration and angular velocity for optimal performance.