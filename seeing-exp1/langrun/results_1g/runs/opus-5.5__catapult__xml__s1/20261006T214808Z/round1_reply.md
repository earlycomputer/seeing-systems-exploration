## What happened in the run

- **Arm:** worked as designed. It hit its 38.16° stop at 563°/s (9.83 rad/s) at 0.09 s.
- **Launch:** went wrong. The ball left the cup in the right place, at about (−0.35, 0.76) m. But it was moving at only about 4.15 m/s at 28° above horizontal, instead of the planned 4.95 m/s at 45°.
- **Flight and landing:** it peaked at 0.95 m and landed on the floor at x ≈ 2.0 m. It bounced, clipped the near wall and bottom of the bucket, and came to rest outside the bucket at x = 2.22 m.

Compared with the plan, the ball lost about 1.1 m/s along its direction of travel and gained about 1.1 m/s back toward the pivot. My best explanation is friction against the cup walls and floor as the arm stops abruptly; I have not confirmed this.

## Fix

I made the cup frictionless so the ball leaves with exactly the cup's velocity:

- The arm geoms no longer collide with the ball through the normal collision rules.
- Explicit frictionless (`condim="1"`) contact pairs between the ball and each arm geom are added in their place.

```json
{"what_happens": "The arm swings to its 38° stop at 9.8 rad/s, but the ball leaves at only ~4.15 m/s and ~28° elevation instead of 4.95 m/s at 45°, apparently robbed of speed by friction with the cup as the arm stops. It falls short, lands on the floor at x≈2.0 m, bounces off the near side of the bucket and comes to rest outside it at x=2.22 m.", "works": false, "problem": "Friction between the ball and the cup during the abrupt stop sapped and deflected the launch velocity, so the ball fell short of the bucket."}
```

```xml
<mujoco model="catapult_bucket">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="1 -2 4" dir="-0.2 0.4 -1" directional="true"/>
    <geom name="floor" type="plane" size="6 3 0.1" rgba="0.8 0.8 0.75 1"/>

    <geom name="catapult_base" type="box" pos="0 0 0.03" size="0.3 0.15 0.03" contype="0" conaffinity="0" rgba="0.45 0.3 0.15 1"/>
    <geom name="catapult_post_left" type="box" pos="0 0.07 0.215" size="0.02 0.012 0.185" contype="0" conaffinity="0" rgba="0.45 0.3 0.15 1"/>
    <geom name="catapult_post_right" type="box" pos="0 -0.07 0.215" size="0.02 0.012 0.185" contype="0" conaffinity="0" rgba="0.45 0.3 0.15 1"/>
    <geom name="catapult_axle" type="cylinder" fromto="0 -0.09 0.4 0 0.09 0.4" size="0.012" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>

    <body name="catapult_arm" pos="0 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" limited="true" range="0 38.16" solreflimit="0.004 1"/>
      <geom name="catapult_arm_beam" type="box" pos="-0.27 0 0" size="0.28 0.025 0.02" mass="0.6" contype="2" conaffinity="2" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_cup_outer" type="box" pos="-0.5455 0 0.05" size="0.005 0.04 0.03" mass="0.02" contype="2" conaffinity="2" rgba="0.5 0.3 0.15 1"/>
      <geom name="catapult_cup_inner" type="box" pos="-0.435 0 0.03" size="0.005 0.04 0.01" mass="0.01" contype="2" conaffinity="2" rgba="0.5 0.3 0.15 1"/>
    </body>

    <body name="ball" pos="-0.5 0 0.46">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" solref="0.004 1" condim="6" friction="0.8 0.01 0.005" rgba="0.9 0.1 0.1 1"/>
    </body>

    <body name="bucket" pos="2.5 0 0">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 0.01" size="0.23 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall0" type="box" pos="0.21 0 0.17" size="0.01 0.06 0.15" euler="0 0 0" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall1" type="box" pos="0.18187 0.105 0.17" size="0.01 0.06 0.15" euler="0 0 30" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall2" type="box" pos="0.105 0.18187 0.17" size="0.01 0.06 0.15" euler="0 0 60" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall3" type="box" pos="0 0.21 0.17" size="0.01 0.06 0.15" euler="0 0 90" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall4" type="box" pos="-0.105 0.18187 0.17" size="0.01 0.06 0.15" euler="0 0 120" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall5" type="box" pos="-0.18187 0.105 0.17" size="0.01 0.06 0.15" euler="0 0 150" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall6" type="box" pos="-0.21 0 0.17" size="0.01 0.06 0.15" euler="0 0 180" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall7" type="box" pos="-0.18187 -0.105 0.17" size="0.01 0.06 0.15" euler="0 0 210" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall8" type="box" pos="-0.105 -0.18187 0.17" size="0.01 0.06 0.15" euler="0 0 240" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall9" type="box" pos="0 -0.21 0.17" size="0.01 0.06 0.15" euler="0 0 270" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall10" type="box" pos="0.105 -0.18187 0.17" size="0.01 0.06 0.15" euler="0 0 300" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall11" type="box" pos="0.18187 -0.105 0.17" size="0.01 0.06 0.15" euler="0 0 330" rgba="0.2 0.4 0.8 1"/>
    </body>
  </worldbody>

  <contact>
    <pair name="ball_beam" geom1="ball" geom2="catapult_arm_beam" condim="1" solref="0.004 1"/>
    <pair name="ball_cup_outer" geom1="ball" geom2="catapult_cup_outer" condim="1" solref="0.004 1"/>
    <pair name="ball_cup_inner" geom1="ball" geom2="catapult_cup_inner" condim="1" solref="0.004 1"/>
  </contact>

  <actuator>
    <velocity name="catapult_motor" joint="catapult_hinge" kv="20" forcelimited="true" forcerange="-25 25"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0 -0.5 0 0.46 1 0 0 0" qvel="0 0 0 0 0 0 0" ctrl="9.92"/>
  </keyframe>
</mujoco>
```

```expect
ball touches catapult_arm_beam
ball touches bucket_bottom
ball comes to rest in bucket
```

---
thinking (summarized):

The arm hits its stop at roughly 9.83 rad/s. Tracking the launch point, I estimate release velocity components around (3.68, 1.93), giving a launch angle near 27.7° and speed about 4.15 — close to the expected values I'm comparing against.

I'm trying to figure out why the ball didn't actually leave at the tangent angle expected at release, since its velocity magnitude is smaller than predicted and the vertical component especially lags. I wonder if the ball was lagging behind the arm's motion due to friction and contact dynamics, maybe not fully spinning up to match the arm's angular velocity before separating from the floor of the catapult arm.

I'm wondering if the wall geometry or contact point affects things, but that seems fine given the ball's center height relative to the wall face. Maybe during spin-up the ball lags behind due to softness in the contact solver — checking the solref parameters on the ball geom and beam to see if penetration is causing the discrepancy.

Now I'm tracing through the launch kinematics: computing vz and position at the point of last contact (~0.09s), confirming it matches the expected launch height of 0.756 and x-position of -0.356. But the launch speed comes out to 4.15 m/s at 27.7°, which doesn't match the expected direction, so the position is correct but the velocity vector is off.

Comparing against the arm's outward and tangential unit vectors at φ=38°, I find the ball is missing tangential speed while gaining some inward velocity—suggesting it lagged behind the arm's motion, possibly due to the arm overshooting its soft limit near 38.7° with damping effects.

Checking the geometry: the cup floor sits below the ball and the arm's tangential motion pushes it upward, so when the arm decelerates at the limit, the floor slows while the ball's inertia carries it forward, causing separation. That part checks out—now I need to consider whether the ball's spin and friction against the outer wall during this separation phase matters.

I'm computing the centrifugal normal force against the wall (about 4.8 N) and the resulting friction force (~3.8 N at μ=0.8), which gives only ~38 m/s² of deceleration—way too small to shed the needed 1.1 m/s velocity within the few-millisecond stopping window. This makes me suspect the wall contact force must be larger than I'm assuming, or there's some other damping effect from the soft limit I haven't accounted for yet.

Checking the actuator soft-limit settings, I confirm the overshoot is tiny (0.54°), so that's not the source of the discrepancy. I start wondering if the ball never actually reached full tangential speed during spin-up—maybe it slipped relative to the arm rather than staying in perfect contact at radius R. Comparing expected versus measured speeds, I get a ratio of about 0.84 (4.15 m/s measured vs. 4.95 m/s expected), which suggests real slippage during the spin-up phase rather than a loss occurring only at release.

Comparing expected versus actual values, the inward component is much larger than predicted and the normal component smaller, suggesting the velocity got rotated inward along the arm direction—likely because the ball had been pressed against the outer wall by centrifugal force before the stop, and as the arm decelerated and the ball separated from that wall, it carried extra inward momentum from the spring-like release.

Another possibility is friction at the floor contact interacting with the ball's rolling angular velocity as normal force dropped during deceleration, though it's hard to pin down exactly without more data. I'm also considering whether the outer wall's limited height relative to the ball's center plays a role during that deceleration phase.

Rather than keep chasing a full diagnosis, maybe I should just take the empirically observed launch speed and angle and apply a pragmatic correction, though that risks masking the real loss mechanism tied to ω. Thinking more about the deceleration phase, I suspect the friction coefficient at the outer wall contact might be defaulting to 1 instead of the intended 0.8, which could explain the discrepancy.

I work out that during steady rotation there's no slip at the wall contact—the ball's spin exactly matches the arm's motion so surface velocities align. Once the arm stops, though, the ball's contact point keeps moving tangentially relative to the now-stationary wall, so friction kicks in to decelerate both translation and spin, but the contact itself only persists briefly since centrifugal pressing disappears and the soft-contact penetration releases over a few milliseconds. I also start considering the floor contact analogously, with the floor normal acting as the tangent direction below the ball.

The numbers are striking: the ball loses about 1.1 m/s tangentially while gaining almost exactly 1.1 m/s inward, which looks like an energy-preserving redirection rather than pure friction loss—as if it bounced off a surface angled roughly 45° between the tangential and inward directions, like hitting a corner. That makes me question whether the cup geometry near the inner wall is actually set up the way I intended.

Checking the spin contribution instead: with the ball spinning about the arm-frame y-axis and contacting the floor at its bottom point, the induced velocity from that spin at the contact point works out to push outward (-x), not inward, so spin-floor friction alone doesn't explain the inward kick I'm seeing.

Actually, friction opposes the relative slip, so if the contact point is sliding outward, friction on the ball acts inward (+x), which would reduce spin and add inward velocity—this could be the missing mechanism. But I need to check whether normal force even persists during deceleration, since if the floor separates from the ball there's no friction at all to drive this effect.

I'm checking whether friction at the outer wall contact could explain it: the contact point's relative slip is tangential, so friction there would just decelerate tangential speed, not generate inward velocity. That leaves soft-contact normal force dynamics as the more likely source—maybe the solver's velocity-dependent contact reference is producing an inward kick when the wall suddenly decelerates.

Rather than chase this artifact, the more robust fix is redesigning the release mechanism itself: maybe remove or loosen the cup wall friction so sliding can't generate spurious push, or alter the geometry entirely to rely on a cleaner source of centripetal force.

Without friction the ball shouldn't spin up or get thrown off awkwardly. I'm now second-guessing whether explicit pair overrides actually suppress the default dynamic collision generation for that same geom pair, since MuJoCo's docs suggest both could fire simultaneously rather than the explicit pair replacing the default.

A cleaner fix is to just set the catapult arm's contype/conaffinity so it doesn't collide with the ball dynamically at all—using separate bits so arm-ball and arm-floor interactions are skipped, while the explicit pair relationship still governs what I actually want.

Then I add explicit pairs for ball-beam, ball-outer, and ball-inner with condim 1, so the "ball touches catapult_arm_beam" expectation still holds. The measured arm stop speed of 9.83 rad/s matches 563°/s, and with frictionless contact the launch speed should be about 4.95 m/s at 45°, targeting entry near x≈2.5. I'm checking whether the friction diagnosis makes sense—the loss of 1.1 m/s tangential velocity and gain inward is consistent with floor friction acting on the ball's spin, where the slipping contact point at the bottom converts outward spin into inward motion.

With frictionless surfaces, this issue resolves itself regardless of the exact friction mechanism, and condim 1 should handle ball penetration fine. During spin-up, I'm reasoning through the force balance: at low angular velocity near φ=0, gravity has no along-arm component, so there's no early inward sliding concern. Time to write the corrected file.

