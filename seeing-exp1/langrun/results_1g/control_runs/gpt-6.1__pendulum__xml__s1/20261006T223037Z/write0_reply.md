```xml
<mujoco model="pendulum_ball_cup">
  <compiler angle="radian" autolimits="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" cone="elliptic" iterations="80"/>
  <size nconmax="200" njmax="1000"/>

  <visual>
    <headlight ambient="0.4 0.4 0.4" diffuse="0.7 0.7 0.7"/>
    <global azimuth="125" elevation="-25"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="0.4 -1.5 3" dir="0 0 -1"/>
    <camera name="overview" pos="0.5 -3 1.65" xyaxes="1 0 0 0 0.45 0.893"/>

    <geom name="floor" type="plane" size="3 2 0.1" rgba="0.78 0.81 0.84 1" friction="0.35 0.005 0.0001" condim="6" solref="0.008 1" solimp="0.95 0.99 0.001"/>

    <!-- Gravity releases the raised pendulum; its bob strikes toward +x. -->
    <body name="pendulum" pos="-0.1 0 0.815">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" damping="0.012"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.75" size="0.012" mass="0.05" rgba="0.25 0.28 0.32 1" friction="0.2 0.001 0.0001" solref="0.008 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.75" size="0.055" mass="0.4" rgba="0.75 0.18 0.12 1" friction="0.2 0.001 0.0001" condim="6" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball" pos="0 0 0.04">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.06" rgba="0.12 0.42 0.88 1" friction="0.35 0.005 0.0001" condim="6" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <!-- The cup is centred 1 m along the floor from the ball's starting point.
         Its low front lip and approach ramp admit the rolling ball.
         Higher side and rear walls retain it in the shallow interior. -->
    <body name="cup" pos="1 0 0">
      <geom name="cup_bottom" type="cylinder" pos="0 0 0.009" size="0.19 0.009" rgba="0.78 0.52 0.20 1" friction="0.8 0.02 0.004" condim="6" solref="0.008 1" solimp="0.95 0.99 0.001"/>

      <geom name="cup_ramp" type="box" pos="-0.257386 0 0.022848" euler="0 -0.26449 0" size="0.124323 0.095 0.01" rgba="0.88 0.64 0.28 1" friction="0.65 0.005 0.0002" condim="6" solref="0.008 1" solimp="0.95 0.99 0.001"/>

      <geom name="cup_wall_00" type="box" pos="0.18 0 0.10" euler="0 0 0" size="0.01 0.037 0.10" rgba="0.83 0.57 0.23 1" friction="0.8 0.02 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_01" type="box" pos="0.166298 0.068883 0.10" euler="0 0 0.392699" size="0.01 0.037 0.10" rgba="0.83 0.57 0.23 1" friction="0.8 0.02 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_02" type="box" pos="0.127279 0.127279 0.10" euler="0 0 0.785398" size="0.01 0.037 0.10" rgba="0.83 0.57 0.23 1" friction="0.8 0.02 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_03" type="box" pos="0.068883 0.166298 0.10" euler="0 0 1.178097" size="0.01 0.037 0.10" rgba="0.83 0.57 0.23 1" friction="0.8 0.02 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_04" type="box" pos="0 0.18 0.10" euler="0 0 1.570796" size="0.01 0.037 0.10" rgba="0.83 0.57 0.23 1" friction="0.8 0.02 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_05" type="box" pos="-0.068883 0.166298 0.10" euler="0 0 1.963495" size="0.01 0.037 0.10" rgba="0.83 0.57 0.23 1" friction="0.8 0.02 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_06" type="box" pos="-0.127279 0.127279 0.10" euler="0 0 2.356194" size="0.01 0.037 0.10" rgba="0.83 0.57 0.23 1" friction="0.8 0.02 0.004" condim="6" solref="0.008 1"/>

      <geom name="cup_lip_07" type="box" pos="-0.166298 0.068883 0.0225" euler="0 0 2.748894" size="0.01 0.037 0.0225" rgba="0.88 0.64 0.28 1" friction="0.8 0.02 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_lip_08" type="box" pos="-0.18 0 0.0225" euler="0 0 3.141593" size="0.01 0.037 0.0225" rgba="0.88 0.64 0.28 1" friction="0.8 0.02 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_lip_09" type="box" pos="-0.166298 -0.068883 0.0225" euler="0 0 3.534292" size="0.01 0.037 0.0225" rgba="0.88 0.64 0.28 1" friction="0.8 0.02 0.004" condim="6" solref="0.008 1"/>

      <geom name="cup_wall_10" type="box" pos="-0.127279 -0.127279 0.10" euler="0 0 3.926991" size="0.01 0.037 0.10" rgba="0.83 0.57 0.23 1" friction="0.8 0.02 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_11" type="box" pos="-0.068883 -0.166298 0.10" euler="0 0 4.319690" size="0.01 0.037 0.10" rgba="0.83 0.57 0.23 1" friction="0.8 0.02 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_12" type="box" pos="0 -0.18 0.10" euler="0 0 4.712389" size="0.01 0.037 0.10" rgba="0.83 0.57 0.23 1" friction="0.8 0.02 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_13" type="box" pos="0.068883 -0.166298 0.10" euler="0 0 5.105088" size="0.01 0.037 0.10" rgba="0.83 0.57 0.23 1" friction="0.8 0.02 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_14" type="box" pos="0.127279 -0.127279 0.10" euler="0 0 5.497787" size="0.01 0.037 0.10" rgba="0.83 0.57 0.23 1" friction="0.8 0.02 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_15" type="box" pos="0.166298 -0.068883 0.10" euler="0 0 5.890486" size="0.01 0.037 0.10" rgba="0.83 0.57 0.23 1" friction="0.8 0.02 0.004" condim="6" solref="0.008 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.9 0 0 0.04 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Evaluating pendulum design**

I need to engineer a reliable system involving a pendulum strike that rolls into a cup. The center of the cup should be 1 meter away from the starting point of the ball. I’m checking tools since none are available for execution right now. I want a self-contained and robust design that considers gravity and how the ball imparts energy when it contacts the cup. Can the cup be a sideways cylinder or must it be upright? It’s essential to ensure the entry ramp is functional with the floor setup I have in mind.

**Designing a cup and pendulum system**

I’m designing a cup that’s 1 meter from the ball’s starting point, which will roll horizontally. The cup’s radius will be 0.17, and its length is 0.30 to create an opening at the back. The ball will enter this slightly raised cylinder, with a radius of 0.14. Alternatively, I could make the cup upright with a low entry ramp. I want to ensure everything works smoothly, considering the pendulum's swing and its impact on the ball. I need to keep the controls straightforward!

**Configuring pendulum measurements**

I’m setting the pendulum length to 0.76, with a pivot at z = 0.86 and a bob length of 0.10. However, I run into an issue since the bob’s bottom clearance should be at z = -0.025, which would cause collisions if it swings down. The bob’s sphere radius is 0.055, allowing a 0.005 clearance from the floor. When the bob touches the ball at a certain angle, I want to maintain good control to prevent unnecessary movement towards the cup.

**Analyzing collision wall design**

I'm working on collision wall arc primitives involving 16 boxes and their front segments. I’ll set the angles near π and use specific dimensions like h at 0.03 for the top and 0.06 for the bottom. The ramp ends are positioned close to x = -0.16 and set at a height of 0.065. For the ring, the high side extends with arcs where the front portions create an opening width of 0.17 if the angle exceeds 30 degrees.

**Adjusting geometries**

I'm setting the bottom geometry relative to z at -0.031 and the top at 0.018. The geometry position relative to origins feels cumbersome. I see that I can adjust the cup body position to 0 and 0.04. Additionally, I’m considering making ramp positions relative to the body’s z offsets. It seems like there are quite a few adjustments to make for everything to align properly!