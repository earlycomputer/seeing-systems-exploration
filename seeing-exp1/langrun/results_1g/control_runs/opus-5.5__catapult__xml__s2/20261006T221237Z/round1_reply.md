The ball falls short of the bucket.

**What happens in the run**
- The arm swings up and stops at about 40.7° at 0.17 s, moving at the planned ω ≈ 5.67 rad/s.
- The ball leaves from the planned spot, about (−0.56, 1.07) m.
- Its launch velocity is wrong: about (3.28, 2.17) m/s, which is 3.93 m/s at about 33.5°. I had planned 4.55 m/s at 45°.
- The loss is in the arm-normal component, and the ball also gets an inward kick. That points to the lip contact dragging on the ball at release.
- The ball comes down at x ≈ 1.86, outside the bucket's near wall at x = 1.9. It clips the bucket's lower edge, bounces back and stops on the floor at x = 1.75.

**Fix**
- I keep the catapult geometry the same. I assume the release loss scales with speed, so launch direction stays at about 33.5° and speed stays at about 0.866·ω·r.
- A 33.5° launch from the observed release point needs about 4.47 m/s to drop into the bucket centre. That means ω ≈ 6.44 rad/s, so ctrl goes from 5.73 to 6.50.
- I also widen the bucket from 0.3 m to 0.4 m inner apothem. The centre stays at x = 2.2, still 3 m from the ball start, so there is more margin.
- The ball should now cross the rim near x ≈ 2.08 and hit the bottom near x ≈ 2.3, inside the walls at 1.8 and 2.6.
- This is still predicted, not run. It depends on the linear-scaling assumption.

```xml
<mujoco model="catapult_to_bucket">
  <compiler angle="radian"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="1 0 4" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="6 6 0.1" pos="0 0 0" rgba="0.8 0.8 0.8 1"/>

    <!-- Catapult frame (static) -->
    <body name="catapult_frame" pos="0 0 0">
      <geom name="catapult_base" type="box" size="0.12 0.16 0.01" pos="0 0 0.01" rgba="0.45 0.3 0.15 1"/>
      <geom name="catapult_post_left" type="box" size="0.03 0.015 0.25" pos="0 0.1 0.25" rgba="0.45 0.3 0.15 1"/>
      <geom name="catapult_post_right" type="box" size="0.03 0.015 0.25" pos="0 -0.1 0.25" rgba="0.45 0.3 0.15 1"/>

      <!-- Throwing arm: points toward -x at angle 0, swings up and forward about +y -->
      <body name="catapult_arm" pos="0 0 0.5">
        <joint name="catapult_hinge" type="hinge" axis="0 1 0" limited="true" range="0 0.7105" solreflimit="0.005 1" damping="0"/>
        <geom name="catapult_pin" type="cylinder" size="0.015 0.12" pos="0 0 0" euler="1.5708 0 0" mass="0.05" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
        <geom name="catapult_beam" type="box" size="0.45 0.03 0.02" pos="-0.4 0 0" mass="0.5" solref="0.005 1" rgba="0.6 0.4 0.2 1"/>
        <geom name="catapult_lip" type="box" size="0.01 0.04 0.0225" pos="-0.85 0 0.0425" mass="0.02" solref="0.005 1" rgba="0.6 0.4 0.2 1"/>
        <geom name="catapult_rail_left" type="box" size="0.04 0.01 0.02" pos="-0.8 0.055 0.04" mass="0.01" solref="0.005 1" rgba="0.6 0.4 0.2 1"/>
        <geom name="catapult_rail_right" type="box" size="0.04 0.01 0.02" pos="-0.8 -0.055 0.04" mass="0.01" solref="0.005 1" rgba="0.6 0.4 0.2 1"/>
      </body>
    </body>

    <!-- Ball, resting in the cup at the arm tip -->
    <body name="ball" pos="-0.8 0 0.56">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.268" condim="6" friction="1 0.02 0.02" solref="0.005 1" rgba="0.9 0.1 0.1 1"/>
    </body>

    <!-- Bucket: centre 3 m (in x) from the ball start, open octagonal cup -->
    <body name="bucket" pos="2.2 0 0">
      <geom name="bucket_bottom" type="cylinder" size="0.43 0.01" pos="0 0 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_0" type="box" size="0.01 0.174 0.165" pos="0.41 0 0.185" euler="0 0 0" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_1" type="box" size="0.01 0.174 0.165" pos="0.2899 0.2899 0.185" euler="0 0 0.7854" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_2" type="box" size="0.01 0.174 0.165" pos="0 0.41 0.185" euler="0 0 1.5708" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_3" type="box" size="0.01 0.174 0.165" pos="-0.2899 0.2899 0.185" euler="0 0 2.3562" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_4" type="box" size="0.01 0.174 0.165" pos="-0.41 0 0.185" euler="0 0 3.1416" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_5" type="box" size="0.01 0.174 0.165" pos="-0.2899 -0.2899 0.185" euler="0 0 3.9270" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_6" type="box" size="0.01 0.174 0.165" pos="0 -0.41 0.185" euler="0 0 4.7124" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_7" type="box" size="0.01 0.174 0.165" pos="0.2899 -0.2899 0.185" euler="0 0 5.4978" rgba="0.2 0.4 0.8 1"/>
    </body>
  </worldbody>

  <actuator>
    <velocity name="catapult_motor" joint="catapult_hinge" kv="50" ctrllimited="true" ctrlrange="0 10" forcelimited="true" forcerange="-25 25"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0 -0.8 0 0.56 1 0 0 0" qvel="0 0 0 0 0 0 0" ctrl="6.50"/>
  </keyframe>
</mujoco>
```

```json
{"what_happens": "The motor swings the arm to its 40.7° stop at 0.17 s and the ball is thrown from about (-0.56, 1.07) m at roughly 3.9 m/s and 33.5°, slower and flatter than planned because the cup lip drags it at release. It comes down at x ≈ 1.86 m, just short of the bucket's near wall at x = 1.9 m, clips the bucket's lower edge, bounces back and comes to rest on the floor at x = 1.75 m, outside the bucket.", "works": false, "problem": "The ball is launched too slowly and too flat and lands just short of the bucket, coming to rest on the floor outside it."}
```

---
thinking (summarized):

The ball landed short, hitting near the wall bucket at x≈1.9 instead of further out. Working backward from the actual trajectory, the real launch speed was about 3.94 with an angle near 33.5°, noticeably less than my predicted 4.55 — so I need to recheck how arm angular velocity translates to launch speed.

Checking the components: vx=3.28 matches expectation (3.215) but vz=2.17 is much lower than the expected 3.215, meaning the ball lost vertical velocity somewhere. Back-calculating the release point (x=-0.56, z=1.068 at t=0.17) confirms the position lines up fine, so the deficit is purely in vz, about 1 m/s short. My best guess is that when the arm decelerates abruptly, the ball stays pressed against the lip under centripetal force (~6.9N) and friction at that contact (μ=1) absorbs some of the vertical momentum during the brief deceleration — I'm estimating that impulse now.

Decomposing the actual velocity into normal and axial components relative to the arm, I find the normal component lost about 0.75 m/s while there's an unexpected inward component of -0.73 toward the pivot compared to expected. This suggests the ball got deflected by something during release rather than just losing speed from friction alone.

I suspect this is the lip edge of the arm — once the ball's compressed penetration into the stiff lip surface exceeds some threshold, the contact normal shifts and the edge pushes back on the ball, redirecting its velocity away from pure outward motion along the arm.

But the actual speed loss, about 25% below the expected value, feels too large for just a geometric deflection — that points more toward friction or an impact absorbing energy during this contact phase. I'm wondering whether the real cause is the arm's own deceleration near the soft limit: it may overshoot slightly past the limit angle before settling, and during that overshoot the lip is still pressing into the ball, draining its momentum through friction.

Rather than guessing at numeric fixes, I think the cleaner approach is to eliminate friction on the lip and rail contacts entirely by giving those geoms higher priority with zero friction, so the contact uses frictionless physics for the launch instead of the ball's default friction dominating. I should apply the same idea to the beam contact if the ball is rolling on it.

The actual culprit for the inward velocity is likely the lip edge itself — as the ball rises past the lip during release while pinned to the rotating arm, penetration against the lip pushes it inward and the high friction converts some outward motion into spin and drag along the normal direction. A cleaner redesign might remove the lip entirely so the ball isn't constrained by that edge at all.

Checking the spring-energy estimate against the observed velocity, it's way too small, so I suspect friction is the real driver — but then I need an inward force to explain the -0.73 component, and that doesn't obviously come from the arm decelerating away from the ball. I'm trying to figure out if deeper lip compression during the abrupt stop could generate that inward push.

Looking at the release geometry, the position roughly matches the expected launch point, so that part seems fine. I'm now wondering if the ball's spin state or MuJoCo's soft contact model with a pyramidal friction cone could account for the discrepancy, but I can't pin it down exactly, so I'm leaning toward just adjusting the release conditions empirically instead.

I'm tracing where the velocity deficit comes from: both the normal and tangential components are losing speed in the same direction, which points to the lip's friction and normal contact force both acting to decelerate and pull the ball inward during release, rather than a clean separation.

I'm checking if spin-induced friction at the contact point could explain the kick, but that velocity seems too small to matter. I'm also wondering if the tight contact solver settings (solref near the timestep limit) could be causing numerical chatter when the arm decelerates abruptly, rather than any real physical penetration.

Looking more carefully, within a single timestep the ball can travel past the lip's top edge before the contact updates, meaning it ends up contacting the lip's edge rather than its face—and that edge contact geometry could actually push the ball inward and upward instead of releasing it cleanly. Since I can't fully resolve which effect dominates, I think the more robust fix is to redesign the release geometry entirely—either making the lip frictionless and lower so it's clear of the ball at release, or replacing it with a tilted V-seat so there's no edge-contact ambiguity at all.

Alternatively, rather than redesigning the geometry, I could treat the velocity deficit empirically: assume the loss scales proportionally with speed since it comes from contact impulses tied to velocity, so the launch direction stays roughly constant around 33.5° while the output speed is about 0.866 of the wheel's rim speed. I'm now working out what rim speed would be needed to hit the target by using the release point and target coordinates to get the required displacement.

Using the projectile range equation with the launch angle fixed at 33.5°, I solve for the needed velocity squared and get about 4.47 m/s, compared to the current observed 3.93 m/s — a ratio of roughly 1.14x. I'm checking this against the current speed to see where the ball would actually land with the unscaled velocity as a sanity check.

This gives a new angular velocity target of about 6.44, so the controller value should be around 6.50 once I add the offset. I verify the timing works out given the acceleration constraint, then move to re-check the flight parameters with the new velocity value.

Checking trajectory intersections at rim and bottom heights confirms entry around x≈2.08 to 2.31, and clearance near the wall at x≈1.88 looks fine with margin above the 0.39 threshold.

Working out tolerance margins: bottom landing gives roughly 5% range in position, translating to about 2.7% speed tolerance, and the rim crossing shows a similar 5% margin — both seem workable. I'm a bit wary of assuming linear scaling though, since the actual loss mechanism (friction, contact impulses) may not scale perfectly proportionally; better to keep the geometry fixed and only adjust the control parameter rather than also tweaking ball-lip friction, which could introduce unpredictable effects. I'm also considering whether enlarging the bucket radius for extra margin makes sense, though that only shifts the center — maybe increasing the inner apothem slightly would help.

Moving the walls out to radius 0.41, with the tangential half-width computed from the hex angle giving about 0.174, and a bottom radius of 0.43 — this gives more clearance: near wall margin around 1.8 and far wall around 2.6. I'll go with this. Checking that the ball still rests inside after landing at 2.3 and bouncing, keeping wall height at 0.35, and the near-wall clearance works out fine at about 0.68. The diagonal spacing between wall positions at radius 0.41 comes out to about 0.2899.

