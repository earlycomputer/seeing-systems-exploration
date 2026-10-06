The pendulum starts raised and swings under gravity. A shallow entry ramp leads over the cup’s low front rim, while rolling friction inside the cup stops the ball.

```xml
<mujoco model="pendulum_putt">
  <compiler angle="radian" inertiafromgeom="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" cone="elliptic" iterations="80"/>
  <size njmax="2000" nconmax="300"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.65 0.65 0.65"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="0.5 -1 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <camera name="overview" pos="0.45 -2.3 1.25" xyaxes="1 0 0 0 0.46 0.888"/>

    <geom name="floor" type="plane" size="3 2 0.1" rgba="0.78 0.80 0.82 1" condim="6" friction="0.2 0.001 0.0001" solref="0.004 1" solimp="0.95 0.99 0.001"/>

    <body name="stand" pos="-0.08 0 0">
      <geom name="stand_left" type="capsule" fromto="0 -0.18 0.015 0 -0.18 0.687" size="0.015" rgba="0.25 0.28 0.32 1" contype="0" conaffinity="0"/>
      <geom name="stand_right" type="capsule" fromto="0 0.18 0.015 0 0.18 0.687" size="0.015" rgba="0.25 0.28 0.32 1" contype="0" conaffinity="0"/>
      <geom name="stand_crossbar" type="capsule" fromto="0 -0.20 0.687 0 0.20 0.687" size="0.015" rgba="0.25 0.28 0.32 1" contype="0" conaffinity="0"/>
      <geom name="stand_foot_left" type="box" pos="0 -0.18 0.012" size="0.16 0.045 0.012" rgba="0.25 0.28 0.32 1" contype="0" conaffinity="0"/>
      <geom name="stand_foot_right" type="box" pos="0 0.18 0.012" size="0.16 0.045 0.012" rgba="0.25 0.28 0.32 1" contype="0" conaffinity="0"/>
    </body>

    <body name="pendulum" pos="-0.08 0 0.687">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" damping="0.003"/>
      <geom name="pendulum_arm" type="capsule" fromto="0 0 0 0 0 -0.62" size="0.008" mass="0.025" rgba="0.32 0.36 0.40 1" friction="0.2 0.001 0.0001" solref="0.004 1"/>
      <geom name="pendulum_bob" type="capsule" fromto="0 -0.04 -0.65 0 0.04 -0.65" size="0.03" mass="0.3" rgba="0.85 0.28 0.12 1" condim="3" friction="0.2 0.001 0.0001" solref="0.004 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball" pos="0 0 0.035">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.035" mass="0.05" rgba="0.15 0.65 0.25 1" condim="6" friction="0.2 0.001 0.0001" solref="0.004 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="cup" pos="1 0 0">
      <geom name="cup_bottom" type="cylinder" pos="0 0 0.004" size="0.16 0.004" rgba="0.22 0.43 0.72 1" condim="6" friction="0.8 0.005 0.005" solref="0.004 1" solimp="0.95 0.99 0.001"/>
      <geom name="cup_entry_ramp" type="box" pos="-0.225 0 0.004" quat="0.99875026 0 -0.04997917 0" size="0.08 0.07 0.003" rgba="0.30 0.51 0.80 1" condim="6" friction="0.2 0.001 0.0001" solref="0.004 1" solimp="0.95 0.99 0.001"/>

      <geom name="cup_wall_00" type="box" pos="0.15 0 0.06" size="0.012 0.042 0.06" rgba="0.22 0.43 0.72 1" condim="6" friction="0.8 0.005 0.005" solref="0.004 1"/>
      <geom name="cup_wall_30" type="box" pos="0.1299038 0.075 0.06" quat="0.9659258 0 0 0.2588190" size="0.012 0.042 0.06" rgba="0.22 0.43 0.72 1" condim="6" friction="0.8 0.005 0.005" solref="0.004 1"/>
      <geom name="cup_wall_60" type="box" pos="0.075 0.1299038 0.06" quat="0.8660254 0 0 0.5" size="0.012 0.042 0.06" rgba="0.22 0.43 0.72 1" condim="6" friction="0.8 0.005 0.005" solref="0.004 1"/>
      <geom name="cup_wall_90" type="box" pos="0 0.15 0.06" quat="0.7071068 0 0 0.7071068" size="0.012 0.042 0.06" rgba="0.22 0.43 0.72 1" condim="6" friction="0.8 0.005 0.005" solref="0.004 1"/>
      <geom name="cup_wall_120" type="box" pos="-0.075 0.1299038 0.06" quat="0.5 0 0 0.8660254" size="0.012 0.042 0.06" rgba="0.22 0.43 0.72 1" condim="6" friction="0.8 0.005 0.005" solref="0.004 1"/>

      <geom name="cup_lip_150" type="box" pos="-0.1299038 0.075 0.007" quat="0.2588190 0 0 0.9659258" size="0.012 0.042 0.007" rgba="0.30 0.51 0.80 1" condim="6" friction="0.2 0.001 0.0001" solref="0.004 1"/>
      <geom name="cup_lip_180" type="box" pos="-0.15 0 0.007" quat="0 0 0 1" size="0.012 0.042 0.007" rgba="0.30 0.51 0.80 1" condim="6" friction="0.2 0.001 0.0001" solref="0.004 1"/>
      <geom name="cup_lip_210" type="box" pos="-0.1299038 -0.075 0.007" quat="-0.2588190 0 0 0.9659258" size="0.012 0.042 0.007" rgba="0.30 0.51 0.80 1" condim="6" friction="0.2 0.001 0.0001" solref="0.004 1"/>

      <geom name="cup_wall_240" type="box" pos="-0.075 -0.1299038 0.06" quat="-0.5 0 0 0.8660254" size="0.012 0.042 0.06" rgba="0.22 0.43 0.72 1" condim="6" friction="0.8 0.005 0.005" solref="0.004 1"/>
      <geom name="cup_wall_270" type="box" pos="0 -0.15 0.06" quat="-0.7071068 0 0 0.7071068" size="0.012 0.042 0.06" rgba="0.22 0.43 0.72 1" condim="6" friction="0.8 0.005 0.005" solref="0.004 1"/>
      <geom name="cup_wall_300" type="box" pos="0.075 -0.1299038 0.06" quat="-0.8660254 0 0 0.5" size="0.012 0.042 0.06" rgba="0.22 0.43 0.72 1" condim="6" friction="0.8 0.005 0.005" solref="0.004 1"/>
      <geom name="cup_wall_330" type="box" pos="0.1299038 -0.075 0.06" quat="-0.9659258 0 0 0.2588190" size="0.012 0.042 0.06" rgba="0.22 0.43 0.72 1" condim="6" friction="0.8 0.005 0.005" solref="0.004 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.44 0 0 0.035 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
ball touches pendulum
ball touches cup_entry_ramp
ball comes to rest in cup
```

---
thinking (summarized):

**Designing a pendulum ball mechanism**

I need to create a functional design for a pendulum ball rolling into a cup that’s positioned 1 meter away. I’m considering tools for simulation, but it seems I don't have those available. I must ensure robust dynamics for this mechanism. The cup could be recessed or accessible from a low ramp. I want a conventional design using simple geometries, like a U-shaped basin with an entry ramp and walls surrounding the cup. The ball will start at (0, 0, 0.04) with the cup center at (1, 0).

**Building a circular cup design**

I’m aiming to create a cup shaped like a circular ring using segmented boxes, with a radius of 0.14 meters and a thin bottom disk just above the floor. I need the rim height to be about 0.045 meters to accommodate kinetic energy. Surrounding the cup, there should be a ramp, sloping down to an entry point that’s 0.008 meters high. The design features a low front entry with higher walls elsewhere to retain the ball. This creates an open U-shaped cup that is visually appealing while allowing the ball to roll in smoothly.

**Setting up the pendulum-ball mechanism**

I want to create a system where a ball touches a pendulum and comes to rest in a cup. The expectation is that the ball will interact with the pendulum and the floor before settling in the cup. I can design a ramp attached to the cup, named cup_entry_ramp. The ramp will start at 0.71 meters and lead to a cup rim at 0.83 meters. The cup will have a diameter of 0.32 meters, with a back rim height of 0.12 meters. The pendulum energy will be calibrated for a stable setup that doesn't interfere with the ball's movement.

**Calculating mass values**

I’m working on figuring out the values I need for a ball and rod setup. The ball has a radius of 0.035 and a mass of 0.04. The bob is set to 0.3, and the rod's mass is 0.03. I also need to account for an effective mass of 0.31. It looks like I'm laying the groundwork for some calculations related to these measurements, which is important to get right!

**Analyzing rolling friction**

I’m thinking about how a cup's base can affect high rolling friction, which seems to stop a rolling ball before it properly makes contact with the rim. Even when I consider a position like x = 0.827, where the sphere contacts near the top lip, the ball still needs to roll to about 0.86 to engage with the base. This indicates how friction can play a significant role in the ball's movement.

**Evaluating coordinates and gaps**

I'm working with coordinates related to a wall centered at (150, 210) and an inner endpoint near the center at y .039. The ball radius is .035, and it seems to pass through a width gap at x -.15. I'll need to ensure that all these coordinates align properly and confirm whether the ball can fit through the gap. This could involve checking the calculated values against the physical constraints!

**Evaluating design openings**

I’m assessing my design for a larger entrance using 16 segments with a front width to ensure better clearance. The current dimensions show a narrow opening that doesn’t fit a ball properly. I found that adjusting certain walls can help widen the entrance. I've calculated the necessary adjustments and the clearance needed. The path of the sphere should allow a close fit while ensuring safety from contact. Overall, it looks like I've got a solid plan in place!

**Configuring geometric segments**

I'm working on a design that requires twelve box geometries arranged at specific angles: 0, 30, 60, and so on up to 330 degrees. The radial thickness needs to be set, and I'm thinking about how to account for overlaps when forming a complete ring. Adjusting parameters like the base cylinder radius and the cup geometry is critical to avoid collisions. I also want to include friction and conditional attributes in the setup. Finally, I'm keeping an eye on stability with specific simulation settings.

**Adjusting ball contact parameters**

I'm fine-tuning the damping parameters for the ball's behavior, considering a value of 0.7 but also thinking about weak restitution boosts for better contact. For the solver, I’m planning to set solref to optimize inelastic interactions. I need to ensure the floor and ball have consistent settings at 0.0041, and I’m also adjusting the pendulum bob's value. The damping hinge is at 0.003 to account for energy loss during initial travel, which is important for a good pivot effect.

**Analyzing sphere rotation**

I'm thinking about how friction affects the rotation of a sphere, particularly noting the negative angular momentum in the y-direction. The friction at the point of contact causes a downward force on the sphere. When the ball collides with the ramp, it can both depress the floor and spin. I see the speeds after rolling and the losses due to friction; in this case, the ball loses some speed and may stop well before expected.