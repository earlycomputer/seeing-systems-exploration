```xml
<mujoco model="pendulum_ball_cup">
  <compiler angle="degree" autolimits="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" cone="elliptic" iterations="100"/>
  <size nconmax="200" njmax="1000"/>
  <visual>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.75 0.75 0.75" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="0.4 -1 2.5" dir="0 0 -1"/>
    <camera name="overview" pos="0.5 -2.5 1.6" xyaxes="1 0 0 0 0.48 0.88"/>

    <geom name="floor" type="plane" size="3 2 0.1" pos="0 0 0" condim="6" friction="0.6 0.003 0.0008" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.75 0.77 0.80 1"/>

    <!-- The support is offset sideways from the swing and ball trajectory. -->
    <body name="support" pos="-0.09 0.22 0">
      <geom name="support_foot" type="box" pos="0 0 0.015" size="0.12 0.08 0.015" rgba="0.25 0.28 0.32 1"/>
      <geom name="support_post" type="capsule" fromto="0 0 0.03 0 0 0.61" size="0.015" rgba="0.25 0.28 0.32 1"/>
      <geom name="support_axle" type="capsule" fromto="0 0 0.61 0 -0.25 0.61" size="0.012" contype="0" conaffinity="0" rgba="0.25 0.28 0.32 1"/>
    </body>

    <!-- Positive initial hinge angle puts the bob to the left of the ball. -->
    <body name="pendulum" pos="-0.09 0 0.61">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" damping="0.006" limited="false"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.50" size="0.008" mass="0.012" rgba="0.35 0.38 0.42 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.55" size="0.052" mass="0.20" priority="1" condim="3" friction="0.35 0.003 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.85 0.25 0.12 1"/>
    </body>

    <body name="ball" pos="0 0 0.04">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.05" condim="6" friction="0.6 0.003 0.0008" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.95 0.72 0.12 1"/>
    </body>

    <!-- The cup centre is 1 m along the floor from the ball's starting point. -->
    <!-- Its lowered front rim admits the ball; the interior resists rolling. -->
    <body name="cup" pos="1 0 0">
      <geom name="cup_base" type="cylinder" pos="0 0 0" size="0.183 0.001" priority="1" condim="6" friction="0.7 0.005 0.0008" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.16 0.40 0.65 1"/>
      <geom name="cup_inner_floor" type="cylinder" pos="0 0 0.001" size="0.125 0.001" priority="2" condim="6" friction="0.9 0.01 0.015" solref="0.008 1" solimp="0.95 0.99 0.001" rgba="0.12 0.30 0.48 1"/>

      <geom name="cup_wall_00" type="box" pos="0.170000 0 0.061" size="0.012 0.034 0.06" euler="0 0 0" priority="2" condim="6" friction="0.9 0.01 0.015" solref="0.008 1" rgba="0.16 0.40 0.65 1"/>
      <geom name="cup_wall_01" type="box" pos="0.157060 0.065056 0.061" size="0.012 0.034 0.06" euler="0 0 22.5" priority="2" condim="6" friction="0.9 0.01 0.015" solref="0.008 1" rgba="0.16 0.40 0.65 1"/>
      <geom name="cup_wall_02" type="box" pos="0.120208 0.120208 0.061" size="0.012 0.034 0.06" euler="0 0 45" priority="2" condim="6" friction="0.9 0.01 0.015" solref="0.008 1" rgba="0.16 0.40 0.65 1"/>
      <geom name="cup_wall_03" type="box" pos="0.065056 0.157060 0.061" size="0.012 0.034 0.06" euler="0 0 67.5" priority="2" condim="6" friction="0.9 0.01 0.015" solref="0.008 1" rgba="0.16 0.40 0.65 1"/>
      <geom name="cup_wall_04" type="box" pos="0 0.170000 0.061" size="0.012 0.034 0.06" euler="0 0 90" priority="2" condim="6" friction="0.9 0.01 0.015" solref="0.008 1" rgba="0.16 0.40 0.65 1"/>
      <geom name="cup_wall_05" type="box" pos="-0.065056 0.157060 0.061" size="0.012 0.034 0.06" euler="0 0 112.5" priority="2" condim="6" friction="0.9 0.01 0.015" solref="0.008 1" rgba="0.16 0.40 0.65 1"/>
      <geom name="cup_wall_06" type="box" pos="-0.120208 0.120208 0.061" size="0.012 0.034 0.06" euler="0 0 135" priority="2" condim="6" friction="0.9 0.01 0.015" solref="0.008 1" rgba="0.16 0.40 0.65 1"/>

      <geom name="cup_entry_07" type="box" pos="-0.157060 0.065056 0.003" size="0.012 0.034 0.003" euler="0 0 157.5" priority="1" condim="6" friction="0.6 0.003 0.0008" solref="0.008 1" rgba="0.16 0.40 0.65 1"/>
      <geom name="cup_entry_08" type="box" pos="-0.170000 0 0.003" size="0.012 0.034 0.003" euler="0 0 180" priority="1" condim="6" friction="0.6 0.003 0.0008" solref="0.008 1" rgba="0.16 0.40 0.65 1"/>
      <geom name="cup_entry_09" type="box" pos="-0.157060 -0.065056 0.003" size="0.012 0.034 0.003" euler="0 0 202.5" priority="1" condim="6" friction="0.6 0.003 0.0008" solref="0.008 1" rgba="0.16 0.40 0.65 1"/>

      <geom name="cup_wall_10" type="box" pos="-0.120208 -0.120208 0.061" size="0.012 0.034 0.06" euler="0 0 225" priority="2" condim="6" friction="0.9 0.01 0.015" solref="0.008 1" rgba="0.16 0.40 0.65 1"/>
      <geom name="cup_wall_11" type="box" pos="-0.065056 -0.157060 0.061" size="0.012 0.034 0.06" euler="0 0 247.5" priority="2" condim="6" friction="0.9 0.01 0.015" solref="0.008 1" rgba="0.16 0.40 0.65 1"/>
      <geom name="cup_wall_12" type="box" pos="0 -0.170000 0.061" size="0.012 0.034 0.06" euler="0 0 270" priority="2" condim="6" friction="0.9 0.01 0.015" solref="0.008 1" rgba="0.16 0.40 0.65 1"/>
      <geom name="cup_wall_13" type="box" pos="0.065056 -0.157060 0.061" size="0.012 0.034 0.06" euler="0 0 292.5" priority="2" condim="6" friction="0.9 0.01 0.015" solref="0.008 1" rgba="0.16 0.40 0.65 1"/>
      <geom name="cup_wall_14" type="box" pos="0.120208 -0.120208 0.061" size="0.012 0.034 0.06" euler="0 0 315" priority="2" condim="6" friction="0.9 0.01 0.015" solref="0.008 1" rgba="0.16 0.40 0.65 1"/>
      <geom name="cup_wall_15" type="box" pos="0.157060 -0.065056 0.061" size="0.012 0.034 0.06" euler="0 0 337.5" priority="2" condim="6" friction="0.9 0.01 0.015" solref="0.008 1" rgba="0.16 0.40 0.65 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.8 0 0 0.04 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Designing realistic tool dynamics**

I need to create a design that tests tools realistically, since no simulations are available. The focus is on the dynamics of a pendulum ball entering a cup. The ball should swing with gravity and roll into the cup, which is set on a fixed plane. I’m considering using primitive shapes. The cup would need an opening and possibly a ramp for the ball to roll into it. I want it to be functional and authentic!

**Designing the cup dynamics**

I’m envisioning a cup that has a horizontal axis, with its mouth facing towards the ball. It has an outer cylindrical shape made from various segments to create an enclosed tube. The cup could lie at different positions, allowing the ball to enter and bounce back if friction is low. I’m thinking about an upright design, with a retaining basin and an entry ramp. I'll be modeling the cup with tapered sloping walls, ensuring it effectively interacts with the ball!

**Examining dynamics of the cup**

I’m analyzing the cup design, considering that the ball must overcome 15 radial edges. For it to enter the cup, it needs to reach a speed of about 1.6 m/s to climb 0.08 m. The entry ramp will be on the near side, with downhill ramps around the inside to prevent the ball from escaping. I want the back walls to be tall enough at 0.18 and ensuring rolling speed is tuned to about 0.6 m/s at entry.

**Calculating rolling friction and speed**

I need to reduce the speed to about 0.5 based on factors like rolling friction and the floor condition. With a rolling friction torque coefficient of 0.001, I can calculate that the final position might be around 0.93 after adjusting for acceleration. If I adjust the floor for a higher friction of 0.002, it leads to a final speed of approximately 0.72 after 1 meter. There are collision factors involving mass ratios to consider too.

**Analyzing pendulum dynamics**

I'm looking at a pendulum with the rod mass at .008 and the bob at .2, while the ball weighs .05. The initial velocity is 1.81, and the inertial mass is .202. There's an inelastic collision with the ball at 1.4, and it moves quickly over a rough floor with rolling friction at .001. After numerous calculations, the ball's speed settles around 1.02 by the time it stops at about 1.8 seconds.

**Understanding geometry and mechanics**

I'm figuring out some geometric details here, specifically about columns with a low height of .006 and a radius of .014. There are these vertical cylinders at z .003, and the size is .014 with a .003 step, which is interesting. It seems like the ball is positioned atop the cylinder's lip at center x .83, stopping if its velocity reaches .86 energy. There's a lot to process here, and I want to ensure all the details are correct!

**Considering lead spin and friction**

I’m thinking about how leads spin with minimal loss due to sliding. The initial speed could be around 1.4, which seems okay. I wonder about the friction being 0.35 and how that affects the maximum spin ratio. There’s a connection here with the balance between speed and friction, and I’m curious about optimizing that. Would reducing friction increase the spin efficiency? So many factors to think about!

**Explaining ball mechanics**

I'm considering how a low entry rim and a high-friction interior allow the ball to roll into the cup and settle there. It’s simple enough to put that in a single sentence. Then I think about full file names related to that concept like "body pivot support" and how the pendulum might work in terms of its positioning, including support frames and visual trajectories. There's a lot of technical detail here!

**Clarifying body and geometry names**

I need to gather every body and geometry name for the project. It seems "worldbody" itself doesn’t have a legal name, which is a bit odd. There’s a pendulum body with a hinge named "pendulum_hinge," but I wonder about its range. It appears there's no limit on its movements. I'll also check the orientations and key positions like the initial state of the ball, radius, and whether joint positions require degrees or radians. There’s a lot to sort through!