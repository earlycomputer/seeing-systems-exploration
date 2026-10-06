In the run the pendulum swings down and hits the ball at 0.37 s, but the strike is badly wrong. The ball leaves at about 18.5 m/s and sails clean over the cup, never touching it. It lands around 15 m away and is still rolling at 15 m/s when the run ends, 87 m from the start. The pendulum also gains energy from the hit: it was released at 45° but afterwards swings to ±107°.

That rules out a physical bounce. The strike contact was unstable: its time constant (0.004 s) sat at the 2-timestep limit and its damping was very low, so the solver pumped energy into the collision. The corrected file keeps the mild bounce but uses a time constant five times the timestep (0.01 s) with more damping. The ball should then leave at about 1.9 m/s and settle to rolling at about 1.4 m/s. That is fast enough to hop the 1.5 cm front lip and slow enough to stop against the tall back wall.

```json
{"what_happens": "The pendulum strikes the ball at 0.37 s, but the contact injects a huge amount of energy: the ball is launched at about 18.5 m/s, flies over the cup without touching it and rolls off past 87 m. The pendulum ends up swinging to ±107° despite starting at 45°.", "works": false, "problem": "The bob-ball contact pair used solref timeconst 0.004 (twice the timestep) with damping ratio 0.15, which is numerically unstable and blasted the ball far past the cup."}
```

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="0.5 -1 2" dir="0 0.5 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- static support for the pendulum (visual only, no collisions) -->
    <body name="support" pos="-0.075 0 0.53">
      <geom name="support_beam" type="box" size="0.02 0.08 0.01" pos="0 0 0.012" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
      <geom name="support_post" type="cylinder" fromto="0 0.08 0.02 0 0.08 -0.53" size="0.01" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
    </body>

    <!-- pendulum: pivot 0.5 m above the bob centre; bob centre at ball-centre height at the bottom of the swing -->
    <body name="pendulum" pos="-0.075 0 0.53">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.46" size="0.008" mass="0.05" contype="0" conaffinity="0" rgba="0.5 0.5 0.6 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.04" mass="0.5" contype="0" conaffinity="0" rgba="0.8 0.2 0.2 1"/>
    </body>

    <!-- ball resting on the floor at the origin -->
    <body name="ball" pos="0 0 0.03">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" mass="0.1" condim="6" friction="1 0.005 0.0002" rgba="0.2 0.4 0.9 1"/>
    </body>

    <!-- cup centred 1 m from the ball start: low front lip, tall back and side walls -->
    <body name="cup" pos="1 0 0">
      <geom name="cup_base" type="box" size="0.1 0.1 0.003" pos="0 0 0.003" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_front" type="box" size="0.005 0.1 0.0075" pos="-0.095 0 0.0075" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_back" type="box" size="0.005 0.1 0.04" pos="0.095 0 0.04" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_left" type="box" size="0.1 0.005 0.04" pos="0 0.095 0.04" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_right" type="box" size="0.1 0.005 0.04" pos="0 -0.095 0.04" rgba="0.9 0.7 0.2 1"/>
    </body>
  </worldbody>

  <contact>
    <!-- the only pendulum contact: a mildly elastic, numerically stable strike with the ball -->
    <pair name="strike" geom1="pendulum_bob" geom2="ball" condim="3" friction="0.2 0.2 0.005 0.0001 0.0001" solref="0.01 0.3"/>
  </contact>

  <keyframe>
    <key name="start" qpos="0.785 0 0 0.03 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
pendulum touches ball
ball touches cup
ball comes to rest in cup
```

---
thinking (summarized):

I'm checking the energy transfer: the pendulum started at 45° but swings up to 107° after impact, meaning the ball injected substantial energy. At 0.25s the pendulum is at 21.5° moving around -170°/s, roughly matching the expected angular velocity near the bottom, and I'm now tracing the collision timing around 0.37s to pin down the ball's launch speed.

The likely culprit is numerical instability from the soft-contact solref settings — the timeconst sits near the stability limit relative to timestep with low damping ratio, which can cause semi-implicit Euler to inject energy rather than conserve it, especially given the mass ratio between the 0.1 kg ball and 0.5 kg pendulum affecting constraint stiffness. The fix would be switching to a more critically-damped solref or just accepting a simpler pushing contact instead of trying to get elastic bounce behavior.

Ball decelerates from 1.15u sliding down to a rolling speed of 0.82u, while the bob trails behind at around 0.78u, so the ball stays just ahead the whole time without the bob catching up. With u≈1.71, the rolling speed works out to roughly 1.4 m/s, which should be fine for clearing the lip.

Keeping the explicit contact pair with solref "0.01 0.3" seems safer than default contact, since a timeconst of 0.004 at twice the timestep is right on the instability boundary with low damping—0.01 gives more margin. Friction of 0.2 between bob and ball will impart some spin, which is fine, and I don't think mass ratio affects stability given MuJoCo's solref is relative to effective mass. The pendulum will keep swinging after the ball is gone, which is harmless, so no extra hinge damping is needed. Ready to finalize the answer.

