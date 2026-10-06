```xml
<mujoco model="three_balls_into_a_cup">
  <compiler angle="degree" inertiafromgeom="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="80" cone="elliptic"/>
  <size nconmax="200" njmax="1000"/>

  <visual>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
    <rgba haze="0.85 0.89 0.94 1"/>
  </visual>

  <worldbody>
    <light name="overhead_light" pos="-0.3 -1.5 3" dir="0.1 0.3 -1" diffuse="0.9 0.9 0.9"/>
    <camera name="overview" pos="-0.3 -3.4 2.4" xyaxes="1 0 0 0 0.577 0.817"/>

    <geom name="floor" type="plane" size="5 3 0.1" rgba="0.78 0.81 0.84 1" condim="6" priority="1" friction="0.5 0.005 0.008" solref="0.01 1" solimp="0.95 0.99 0.001"/>

    <body name="ball1" pos="-1.35 0 0.06">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.06" mass="0.25" rgba="0.85 0.15 0.12 1" condim="6" friction="0.5 0.005 0.008" solref="0.01 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball2" pos="-0.75 0 0.06">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.06" mass="0.25" rgba="0.95 0.68 0.08 1" condim="6" friction="0.5 0.005 0.008" solref="0.01 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball3" pos="0 0 0.06">
      <freejoint name="ball3_free"/>
      <geom name="ball3_geom" type="sphere" size="0.06" mass="0.25" rgba="0.12 0.38 0.9 1" condim="6" friction="0.5 0.005 0.008" solref="0.01 1" solimp="0.95 0.99 0.001"/>
    </body>

    <!-- Open-top receiving cup, with a short ramp over its low front lip. -->
    <body name="cup" pos="0 0 0">
      <geom name="cup_ramp" type="box" pos="0.240986 0 0.014082" euler="0 -9.462322 0" size="0.121655 0.18 0.006" rgba="0.32 0.58 0.48 1" condim="6" priority="2" friction="0.8 0.01 0.02" solref="0.01 1" solimp="0.95 0.99 0.001"/>
      <geom name="cup_front_lip" type="box" pos="0.37 0 0.02" size="0.01 0.20 0.02" rgba="0.22 0.48 0.38 1" condim="6" priority="2" friction="0.8 0.01 0.02" solref="0.01 1" solimp="0.95 0.99 0.001"/>
      <geom name="cup_bottom" type="box" pos="0.68 0 0.004" size="0.30 0.18 0.004" rgba="0.32 0.58 0.48 1" condim="6" priority="2" friction="0.8 0.01 0.02" solref="0.01 1" solimp="0.95 0.99 0.001"/>
      <geom name="cup_left_wall" type="box" pos="0.68 0.19 0.11" size="0.32 0.01 0.11" rgba="0.22 0.48 0.38 1" condim="6" priority="2" friction="0.8 0.01 0.02" solref="0.01 1" solimp="0.95 0.99 0.001"/>
      <geom name="cup_right_wall" type="box" pos="0.68 -0.19 0.11" size="0.32 0.01 0.11" rgba="0.22 0.48 0.38 1" condim="6" priority="2" friction="0.8 0.01 0.02" solref="0.01 1" solimp="0.95 0.99 0.001"/>
      <geom name="cup_back_wall" type="box" pos="1.0 0 0.11" size="0.02 0.20 0.11" rgba="0.22 0.48 0.38 1" condim="6" priority="2" friction="0.8 0.01 0.02" solref="0.01 1" solimp="0.95 0.99 0.001"/>
    </body>
  </worldbody>

  <!-- Resilient, frictionless ball-to-ball impacts transfer forward motion. -->
  <contact>
    <pair name="ball1_ball2_contact" geom1="ball1_geom" geom2="ball2_geom" condim="1" solref="-20000 -25" solimp="0.97 0.99 0.001"/>
    <pair name="ball2_ball3_contact" geom1="ball2_geom" geom2="ball3_geom" condim="1" solref="-20000 -25" solimp="0.97 0.99 0.001"/>
    <pair name="ball1_ball3_contact" geom1="ball1_geom" geom2="ball3_geom" condim="1" solref="-20000 -25" solimp="0.97 0.99 0.001"/>
  </contact>

  <!-- Ball1 begins rolling along +x; the other two balls begin stationary. -->
  <keyframe>
    <key name="start" qpos="-1.35 0 0.06 1 0 0 0 -0.75 0 0.06 1 0 0 0 0 0 0.06 1 0 0 0" qvel="4 0 0 0 66.666667 0 0 0 0 0 0 0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
ball1 touches ball2
ball2 touches ball3
ball3 touches cup_ramp
ball3 comes to rest in cup
```

---
thinking (summarized):

**Analyzing ball dynamics**

I'm considering a scenario with solid balls experiencing low to no friction. When ball1 rotates and translates, it creates collisions with ball2 and ball3, which also involves friction torque. With a small floor friction coefficient of around 0.05 to 0.08, the balls acquire spin quickly. I want to calculate various aspects like rolling friction and deceleration. I'm exploring energy requirements for climbing ramps and ensuring the speed is sufficient for the final ball's movement.

**Evaluating ball spacing and dynamics**

I need to ensure there's over 1 meter of gap for the follower after collisions. With floor damping around 0.15 or 0.2, I can stop the residual motion in about 2 seconds. I'm considering the positions of the balls, and timing their movements to ensure the third ball can climb properly after reaching the cup. If I increase the rolling friction, it could enhance deceleration. I should also adjust the initial distances and mass spin for optimal performance.

**Exploring sphereball dynamics**

I'm considering the sphereball dynamics where there's no rolling involved. If the collisions happen without damping, the sphereball could keep moving indefinitely. This raises concerns about how quickly the cup can stop the ball, especially with different friction values playing a role. Without the right damping, it seems challenging to manage the ball's motion effectively. I need to think about how to adjust these factors to ensure everything interacts smoothly.

**Evaluating contact parameters in MuJoCo**

I’m working on cup dynamics, where deceleration and contact parameters are crucial. Setting low damping ratios affects energy transfer and might lead to unstable integrations. I need to choose damping and time constants carefully, ensuring they provide a balance between stability and responsiveness. Running through parameters like damping ratios and time constants, I see their impact on spring oscillators and contact responses. It's tricky to find the sweet spot for efficient calculations!

**Analyzing ball movement dynamics**

I'm figuring out the movement of several balls. The first ball won't collide with the second if it’s ahead, given the gaps I’ve calculated. I see that by the time the first ball reaches the end, the second ball will be climbing the ramp. But I realize I need to stop the second ball before it reaches the ramp since it won't have enough energy to cross it. It could potentially block the first ball, but I suspect the second might gently roll into position without settling in the cup itself.

**Evaluating ball movement and friction**

I’m considering increasing the floor rolling friction to 0.008, which would change the dynamics a bit. The first ball would stop around 0.9, while the second might stop around 0.28 without entering the cup, only reaching the ramp. The third ball moves at roughly 1.3 but loses energy. If I raise initial values and adjust speeds, I might find collision points. However, there seems to be a risk of certain balls not entering the cup properly due to insufficient speed. I’ll need to keep tracking their positions and momentum closely!

**Evaluating ball movement dynamics**

I'm thinking about the energy and speed of the balls on the ramp. It looks like Ball1 at a speed of roughly 0.7 could hit Ball3 in the cup after colliding with Ball2. The calculations suggest that there's enough energy for them to move via gravity, but the velocities could be too low for the optimal climb. Also, it seems like there's potential to improve this setup with less spin through joint damping. Finally, I'm ensuring I'm using joint settings correctly per the regulations.

**Considering bowling sphere design**

I’m thinking about using fluid viscosity to affect the velocity and angular momentum differently for the spheres. No rolling is needed on the floor since drag is high. I want to create aesthetically credible bowling-sized spheres with a short lip ramp for the cup. I’ve decided on certain parameters like radius, mass, and positions for each ball, and I'll need to manage their speeds properly to ensure they can enter the cup effectively.

**Analyzing ramp design requirements**

I'm considering the height of the lip, which is 0.04, and the ball radius of 0.06 means it exceeds the lip. The ramp isn’t strictly necessary for the ball to enter, as the ball’s center can bump the lip at 0.06, generating lift. This gives me some flexibility in design since the ball can still manage to enter the cup without the ramp being essential. It’s intriguing to see how these dimensions interact!

**Refining touch expectations**

I’m thinking about how to name my variables like "floor" and "ball1_geom." I should focus on capturing the scenario where "ball1" and "ball2" touch, followed by "ball2" and "ball3," then "ball3" coming to rest in the cup. However, I realize I don't need a separate expectation for touching the floor since it’s redundant. I want to emphasize that "ball3 comes to rest in the cup" clearly describes the final action.