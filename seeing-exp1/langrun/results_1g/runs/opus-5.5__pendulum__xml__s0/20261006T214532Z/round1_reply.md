**What happened in the run:** the pendulum swung down and its bob reached the ball at 0.33 s. The ball moved only 7 cm, and the bob stayed pressed against it until 0.51 s. By then the pendulum had lost almost all its swing, peaking at only −11° on the far side. The ball crept on to x = 0.13 m and never reached the ramp, which starts at x = 0.52 m.

**Why it jammed:** the bob's centre sat above the ball's centre, at 3.0 cm against 2.5 cm. Once past the bottom of its arc, the bob was rising, so it pushed the ball slightly downward as well as forward. With friction 1 at both the bob–ball and ball–floor contacts, the ball wedged against the floor. The pendulum's energy went into friction and contact damping instead of the ball.

**Changes:**
- The bob is now radius 0.02 m with its centre at the ball's height, 0.025 m, at the bottom of the swing, so the push is horizontal.
- The bob–ball contact is frictionless: an explicit `pair` with `condim="1"`, and the default contact between those two bodies is excluded.
- The pendulum is shifted so the bob just touches the ball when it hangs straight down.
- Rough estimate: the ball should roll at about 1.45 m/s. A rolling ball needs about 1.0 m/s to climb the 6.5 cm ramp, and the tall back wall can catch it up to about 1.85 m/s, so this is near the middle. I have not run this version.

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <asset>
    <material name="floormat" rgba="0.8 0.8 0.75 1"/>
    <material name="wood" rgba="0.6 0.45 0.3 1"/>
    <material name="metal" rgba="0.5 0.5 0.6 1"/>
    <material name="red" rgba="0.85 0.15 0.1 1"/>
    <material name="cupmat" rgba="0.2 0.4 0.8 1"/>
  </asset>
  <worldbody>
    <light name="sun" pos="0.5 -1 3" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" material="floormat" friction="1 0.005 0.0001"/>

    <body name="stand" pos="-0.046 0 0">
      <geom name="stand_post1" type="box" size="0.01 0.01 0.2125" pos="0 0.12 0.2125" material="wood" contype="0" conaffinity="0"/>
      <geom name="stand_post2" type="box" size="0.01 0.01 0.2125" pos="0 -0.12 0.2125" material="wood" contype="0" conaffinity="0"/>
      <geom name="stand_bar" type="cylinder" size="0.006 0.13" pos="0 0 0.425" euler="90 0 0" material="metal" contype="0" conaffinity="0"/>
    </body>

    <body name="pendulum" pos="-0.046 0 0.425">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0" damping="0"/>
      <geom name="pendulum_arm" type="capsule" fromto="0 0 0 0 0 -0.38" size="0.008" mass="0.05" material="metal"/>
      <geom name="pendulum_bob" type="sphere" size="0.02" pos="0 0 -0.4" mass="0.5" material="metal"/>
    </body>

    <body name="ball" pos="0 0 0.025">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.025" mass="0.06" material="red" friction="1 0.005 0.0001"/>
    </body>

    <body name="ramp" pos="0.7216 0 0.0226">
      <geom name="ramp" type="box" size="0.2026 0.06 0.01" axisangle="0 1 0 -9.23" material="wood"/>
    </body>

    <body name="cup" pos="1 0 0">
      <geom name="cup_base" type="box" size="0.08 0.08 0.003" pos="0 0 0.003" material="cupmat" condim="6" friction="1 0.02 0.005"/>
      <geom name="cup_front" type="box" size="0.005 0.08 0.03" pos="-0.075 0 0.03" material="cupmat"/>
      <geom name="cup_back" type="box" size="0.005 0.08 0.06" pos="0.075 0 0.06" material="cupmat"/>
      <geom name="cup_left" type="box" size="0.07 0.005 0.06" pos="0 0.075 0.06" material="cupmat"/>
      <geom name="cup_right" type="box" size="0.07 0.005 0.06" pos="0 -0.075 0.06" material="cupmat"/>
    </body>
  </worldbody>

  <contact>
    <exclude name="no_default_strike" body1="pendulum" body2="ball"/>
    <pair name="strike" geom1="pendulum_bob" geom2="ball" condim="1"/>
  </contact>

  <keyframe>
    <key name="start" qpos="0.88 0 0 0.025 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
pendulum touches ball
ball touches ramp
ball touches cup_base
ball comes to rest in cup
```

```json
{"what_happens": "The pendulum swings down and its bob reaches the ball at 0.33 s, but the bob, centred higher than the ball and rising past the bottom of its arc, wedges the ball against the floor with friction. The ball moves only 7 cm, the pendulum loses nearly all its swing, and the ball creeps to x = 0.13 m, never reaching the ramp or the cup.", "works": false, "problem": "The bob struck the ball above its centre with friction on both contacts, so the ball jammed against the floor and only moved 7 cm instead of being launched toward the cup."}
```

---
thinking (summarized):

Something's off here — the ball barely moved, only about 7 cm, and its z-value of 0.02 instead of 0.025 suggests it might be sinking slightly into the floor. The pendulum seems stuck touching the ball until 0.51s, swinging to -11.2°, which given the sign convention means the bob moved toward -x from its starting angle of 50.4°.

Computing the bob's position at -11.2° puts it at roughly (0.027, 0.038), while the ball sits at (0.07, 0.02) — the vector between them points down and forward, suggesting the bob is pressing the ball into the floor rather than knocking it away cleanly. That could explain why the ball appears wedged, barely sliding, while the pendulum's kinetic energy (about 0.72 J at 1.7 m/s) seems to be dissipating into friction from this jammed contact rather than transferring into clean ball motion.

I'm trying to work out the contact geometry between the bob and ball — with both friction coefficients at 1, the direction of relative sliding at each contact point determines whether friction helps or kills the ball's forward speed, and I'm tracing through the rolling motion to see which way the contact point on the ball's surface is actually moving.

This seems like a wedge-jamming effect where the bob pushes the ball down into the floor, increasing floor friction and dissipating the pendulum's energy instead of transferring motion cleanly. I'm thinking the fix is to override the contact pair between the bob and ball to use near-zero friction there specifically, keeping floor friction intact so the ball can still roll afterward.

I could try excluding the floor-pendulum contact pair directly, or alternatively shrink the bob so its resting center sits clear of the floor, keeping contact precise at the bottom of the swing. I should also reconsider restitution settings since a heavy bob with near-zero bounce will just keep pushing rather than striking cleanly.

I'm estimating spin-up time for the ball once friction starts acting on it while still in contact with the pendulum—calculating the angular acceleration from friction torque and comparing it to how far the pendulum swings during that short interval, roughly 15° in about 0.06 s.

The friction force transmitted back to the bob is small relative to bob mass, so I'm settling on a ball exit velocity somewhere between 0.85-0.9 of bob speed, landing in the 1.3-1.5 m/s range if bob velocity is around 1.7 m/s, with some scope for higher values if the collision is more elastic. I'll keep the default contact settings and floor friction as is.

Checking the geometry now: hinge, arm, and ball positions all clear each other with enough margin (0.05 vs 0.033 needed), so the arm won't clip the ball as it swings through after impact.

Now recomputing the moment of inertia for the pendulum arm plus bob, combining with gravitational torque to find the release angle θ0 needed for the target angular velocity.

Testing 0.95 rad gives a slightly faster ball exit, but staying with 0.88 rad keeps the ball speed in the sweet spot of 1.45-1.55 after rolling friction, which lands nicely in the target window. Now checking whether the pendulum swings back far enough to interfere with the ball after release.

I'm also setting up the contact pair between the pendulum bob and ball with condim 1, and recalling that MuJoCo's explicit pair mechanism should exclude that geom pair from the default dynamic contact generation so it isn't double-counted.

Explicit pairs aren't affected by exclude, so that confirms the approach works. And a pair-generated contact still registers as touching in the data, so "pendulum touches ball" should be satisfied.

