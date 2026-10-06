The cup is upright, with a low front lip and an entry ramp. Its centre is 1 m from the ball’s starting position along the floor.

```xml
<mujoco model="pendulum_ball_into_cup">
  <compiler angle="degree" autolimits="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="100" cone="elliptic"/>
  <size njmax="2000" nconmax="400"/>

  <visual>
    <global azimuth="135" elevation="-25"/>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="0 0 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <camera name="overview" pos="2.3 -3.2 1.8" xyaxes="0.866 0.5 0 -0.19 0.329 0.925"/>

    <geom name="floor" type="plane" pos="0 0 0" size="4 3 0.1" rgba="0.82 0.84 0.86 1" friction="0.55 0.002 0.0002" condim="6" solref="0.008 1" solimp="0.95 0.99 0.001"/>

    <body name="support" pos="-0.072 0 0">
      <geom name="support_left_foot" type="box" pos="0 -0.18 0.012" size="0.18 0.045 0.012" rgba="0.25 0.28 0.32 1" contype="0" conaffinity="0"/>
      <geom name="support_right_foot" type="box" pos="0 0.18 0.012" size="0.18 0.045 0.012" rgba="0.25 0.28 0.32 1" contype="0" conaffinity="0"/>
      <geom name="support_left_post" type="capsule" fromto="0 -0.18 0.024 0 -0.18 0.95" size="0.015" rgba="0.25 0.28 0.32 1" contype="0" conaffinity="0"/>
      <geom name="support_right_post" type="capsule" fromto="0 0.18 0.024 0 0.18 0.95" size="0.015" rgba="0.25 0.28 0.32 1" contype="0" conaffinity="0"/>
      <geom name="support_crossbar" type="capsule" fromto="0 -0.20 0.95 0 0.20 0.95" size="0.017" rgba="0.25 0.28 0.32 1" contype="0" conaffinity="0"/>
    </body>

    <!-- The start keyframe releases the pendulum from 50 degrees, at rest. -->
    <body name="pendulum" pos="-0.072 0 0.95">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" limited="false" damping="0.002" armature="0.00005"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.875" size="0.008" mass="0.020" rgba="0.40 0.43 0.48 1" friction="0.4 0.002 0.0002" solref="0.008 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.91" size="0.035" mass="0.300" rgba="0.85 0.30 0.12 1" friction="0.4 0.002 0.0002" condim="6" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball" pos="0 0 0.035">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.035" mass="0.050" rgba="0.95 0.76 0.12 1" friction="0.55 0.002 0.0002" condim="6" solref="0.008 1" solimp="0.95 0.99 0.001"/>
    </body>

    <!-- Upright cup: circular floor, segmented walls, and a lowered front lip. -->
    <!-- The ramp rises from floor level at x=0.38 to z=0.11 at x=0.84. -->
    <body name="cup" pos="1 0 0">
      <geom name="cup_bottom" type="cylinder" pos="0 0 0.0075" size="0.212 0.0075" rgba="0.18 0.48 0.68 1" friction="1.0 0.01 0.025" condim="6" solref="0.008 1" solimp="0.95 0.99 0.001"/>
      <geom name="cup_entry_ramp" type="box" pos="-0.388605 0 0.049164" euler="0 -13.45 0" size="0.236485 0.075 0.006" rgba="0.26 0.56 0.73 1" friction="0.55 0.002 0.0002" condim="6" solref="0.008 1" solimp="0.95 0.99 0.001"/>

      <geom name="cup_wall_00" type="box" pos="0.200000 0 0.105" euler="0 0 0" size="0.012 0.040 0.095" rgba="0.18 0.48 0.68 1" friction="0.8 0.01 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_01" type="box" pos="0.184776 0.076537 0.105" euler="0 0 22.5" size="0.012 0.040 0.095" rgba="0.18 0.48 0.68 1" friction="0.8 0.01 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_02" type="box" pos="0.141421 0.141421 0.105" euler="0 0 45" size="0.012 0.040 0.095" rgba="0.18 0.48 0.68 1" friction="0.8 0.01 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_03" type="box" pos="0.076537 0.184776 0.105" euler="0 0 67.5" size="0.012 0.040 0.095" rgba="0.18 0.48 0.68 1" friction="0.8 0.01 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_04" type="box" pos="0 0.200000 0.105" euler="0 0 90" size="0.012 0.040 0.095" rgba="0.18 0.48 0.68 1" friction="0.8 0.01 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_05" type="box" pos="-0.076537 0.184776 0.105" euler="0 0 112.5" size="0.012 0.040 0.095" rgba="0.18 0.48 0.68 1" friction="0.8 0.01 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_06" type="box" pos="-0.141421 0.141421 0.105" euler="0 0 135" size="0.012 0.040 0.095" rgba="0.18 0.48 0.68 1" friction="0.8 0.01 0.004" condim="6" solref="0.008 1"/>

      <geom name="cup_wall_07" type="box" pos="-0.184776 0.076537 0.055" euler="0 0 157.5" size="0.012 0.040 0.045" rgba="0.18 0.48 0.68 1" friction="0.8 0.01 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_08" type="box" pos="-0.200000 0 0.055" euler="0 0 180" size="0.012 0.040 0.045" rgba="0.18 0.48 0.68 1" friction="0.8 0.01 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_09" type="box" pos="-0.184776 -0.076537 0.055" euler="0 0 202.5" size="0.012 0.040 0.045" rgba="0.18 0.48 0.68 1" friction="0.8 0.01 0.004" condim="6" solref="0.008 1"/>

      <geom name="cup_wall_10" type="box" pos="-0.141421 -0.141421 0.105" euler="0 0 225" size="0.012 0.040 0.095" rgba="0.18 0.48 0.68 1" friction="0.8 0.01 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_11" type="box" pos="-0.076537 -0.184776 0.105" euler="0 0 247.5" size="0.012 0.040 0.095" rgba="0.18 0.48 0.68 1" friction="0.8 0.01 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_12" type="box" pos="0 -0.200000 0.105" euler="0 0 270" size="0.012 0.040 0.095" rgba="0.18 0.48 0.68 1" friction="0.8 0.01 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_13" type="box" pos="0.076537 -0.184776 0.105" euler="0 0 292.5" size="0.012 0.040 0.095" rgba="0.18 0.48 0.68 1" friction="0.8 0.01 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_14" type="box" pos="0.141421 -0.141421 0.105" euler="0 0 315" size="0.012 0.040 0.095" rgba="0.18 0.48 0.68 1" friction="0.8 0.01 0.004" condim="6" solref="0.008 1"/>
      <geom name="cup_wall_15" type="box" pos="0.184776 -0.076537 0.105" euler="0 0 337.5" size="0.012 0.040 0.095" rgba="0.18 0.48 0.68 1" friction="0.8 0.01 0.004" condim="6" solref="0.008 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.872664626 0 0 0.035 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Considering cup design for ball reception**

I need to create a robust physical swing strike with a cup designed for ball reception, preferably starting at one meter. Unfortunately, there are no available simulation tools for this. I need to think about designing passive geometry that allows for plausible rolling balls into the cup, possibly considering a shallow recessed cup. Would a cylindrical orientation work better for catching a rolling ball? Finally, I could explore options for constructing a U-shaped catch bowl with a low entrance ramp.

**Designing a functional cup for ball capture**

I need to create a convincing cup rather than a U-shaped trough. I'm thinking about using cylindrical walls combined with box segments, tilted for the design. The full rim requires a ramp to reach the necessary height. I can use circular walls with outer and inner radii, and the ramp at the front must allow the ball to bounce inside effectively. The target impact speed is around 1.2 to 1.7 m/s, ensuring the ball can successfully enter the cup without overshooting. I'll also consider the damping effects from impacts.

**Designing ramp-integrated cup geometry**

I can use a ramp integrated into the cup's geometry, which I’ll call cup_ramp, to rise to the front lip at x .86. This will help launch the ball slightly upwards towards the far wall at 1.14 unless it jumps over the rim due to a stronger launch. I’m considering the velocities; a lower speed of around .8 near the ramp could mean a launch time of .21. The parameters suggest I’ll need a wider cup and adjustments to the wall heights for effective capture. An asymmetrical cup design might work just fine!

**Evaluating geometry tools**

I’m thinking about how to fulfill the spirit of a task involving a ball inside a cylindrical cup. It seems like the goal involves evaluating how the ball rolls into the cup, which relates to geometry metrics. I should create a clear upright cup with a ramp that holds it as a standard set-up. I also need to consider the collision and energy aspects to ensure everything functions correctly. Let's figure this out!

**Calculating requirements**

I'm looking at some calculations related to performance. It seems like 9 KE per kilogram could be relevant, and if I multiply .7 by .81, I get .567. That feels important for figuring something out, maybe a climb calculation. Then there's a .05 that I might need to consider for speed, which is set at 1.2. I wonder how all these figures fit together, but I'll need to clarify precisely what they're all used for next!