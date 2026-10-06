**What happens in the run.**

- The motor swings the arm up and it hits its 45° stop at about 0.12 s.
- The ball leaves the arm with the expected horizontal speed of 3.70 m/s, but with only about 1.3 m/s upward. The design called for about 3.0 m/s. It peaks at only 0.89 m height.
- It lands on the floor at x ≈ 1.8 m, short of the bucket at x = 2.5.
- It rolls into the outside of the bucket's near wall, bounces back, and creeps away across the floor at 0.06 m/s. It is still outside the bucket at 6 s.

**Why.** The likely cause is friction on the lip. The centripetal load presses the ball hard against the lip at the arm tip. When the arm stops, the ball slides along the lip face while still pressed against it. With friction 1, this probably drags off part of the launch velocity along the arm's normal, which is the forward-up direction. The horizontal speed matched the design exactly, so the motor speed itself is right.

**Fixes.**

- The lip now overrides the contact pair with `priority="1" condim="1"`, so it is frictionless and only holds the ball radially.
- The bucket is widened to an inner apothem of about 0.36 m, which gives more margin. Its centre stays 3 m from the ball's start.

```json
{"what_happens": "The motor swings the arm to its 45° stop by about 0.12 s. The ball is released with the planned horizontal speed (3.70 m/s) but only about 1.3 m/s upward, so it flies too flat, peaks at 0.89 m, and lands on the floor at x≈1.8 m, short of the bucket at x=2.5. It rolls into the outside of the bucket's near wall, bounces back, and ends rolling slowly (0.06 m/s) on the floor at x=1.86, outside the bucket.", "works": false, "problem": "Friction between the ball and the arm-tip lip, which the ball is pressed against, probably strips much of the upward launch velocity when the arm stops, so the throw falls about 0.7 m short of the bucket."}
```

```xml
<mujoco model="catapult_bucket">
  <option timestep="0.002"/>

  <worldbody>
    <light name="sun" pos="1 -2 4" dir="-0.2 0.4 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- catapult frame (visual only, non-colliding) -->
    <geom name="catapult_base" type="box" pos="0 0 0.01" size="0.1 0.12 0.01" contype="0" conaffinity="0" rgba="0.4 0.25 0.1 1"/>
    <geom name="catapult_post_left" type="box" pos="0 0.08 0.2" size="0.03 0.02 0.2" contype="0" conaffinity="0" rgba="0.4 0.25 0.1 1"/>
    <geom name="catapult_post_right" type="box" pos="0 -0.08 0.2" size="0.03 0.02 0.2" contype="0" conaffinity="0" rgba="0.4 0.25 0.1 1"/>

    <!-- catapult arm: hinge about y at z=0.4, arm points along -x, swings up to 45 deg -->
    <body name="catapult_arm" pos="0 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 45" limited="true" solreflimit="0.01 1"/>
      <geom name="catapult_beam" type="box" pos="-0.26 0 0" size="0.30 0.04 0.01" mass="0.3" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_lip" type="box" pos="-0.55 0 0.04" size="0.01 0.04 0.03" mass="0.03" priority="1" condim="1" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_axle" type="cylinder" pos="0 0 0" euler="90 0 0" size="0.015 0.06" mass="0.02" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
    </body>

    <!-- bucket: centre at x=2.5, 3 m from ball start at x=-0.5 -->
    <body name="bucket" pos="2.5 0 0">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 0.01" size="0.39 0.01" condim="6" friction="1 0.01 0.001" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall0" type="box" pos="0.37 0 0.17" euler="0 0 0" size="0.01 0.158 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall1" type="box" pos="0.2616 0.2616 0.17" euler="0 0 45" size="0.01 0.158 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall2" type="box" pos="0 0.37 0.17" euler="0 0 90" size="0.01 0.158 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall3" type="box" pos="-0.2616 0.2616 0.17" euler="0 0 135" size="0.01 0.158 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall4" type="box" pos="-0.37 0 0.17" euler="0 0 180" size="0.01 0.158 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall5" type="box" pos="-0.2616 -0.2616 0.17" euler="0 0 225" size="0.01 0.158 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall6" type="box" pos="0 -0.37 0.17" euler="0 0 270" size="0.01 0.158 0.15" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall7" type="box" pos="0.2616 -0.2616 0.17" euler="0 0 315" size="0.01 0.158 0.15" rgba="0.2 0.4 0.8 1"/>
    </body>

    <!-- ball resting on the arm against the lip -->
    <body name="ball" pos="-0.5 0 0.45">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>

  <actuator>
    <velocity name="catapult_motor" joint="catapult_hinge" kv="20" forcelimited="true" forcerange="-10 10"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0 -0.5 0 0.45 1 0 0 0" qvel="0 0 0 0 0 0 0" ctrl="9.56"/>
  </keyframe>
</mujoco>
```

```expect
ball touches catapult_beam
catapult_arm reaches its upper stop
ball touches bucket
ball comes to rest in bucket
```

---
thinking (summarized):

The horizontal velocity checks out at 3.70, matching my expected calculation, but the vertical velocity at release seems off—the timing suggests the ball left the hand around 0.12s with vz near 1.27 rather than the expected 3.03, implying it released before reaching the intended 45° angle.

Working backward from the top of the trajectory, release position lines up with the known arm geometry around -0.31, 0.81, but the resulting velocity angle is more like 19° than 39°, even though vx matches perfectly. This is strange since both components come from the same rotational velocity formula, so I'm wondering if the lip continued contacting the ball briefly after nominal release, perhaps during the arm's deceleration/overshoot phase (with the soft limit causing it to swing past 45° to around 46.7°), and friction from that contact altered the ball's effective launch velocity before true separation.

Checking the 25° release angle doesn't match as well as 45° does, since the trajectory timing gives a lower height than observed. The speed magnitude also comes out lower than expected, with the vertical component specifically reduced rather than the whole vector being rotated, suggesting friction is damping vz specifically rather than just changing release angle.

I'm considering whether friction against the lip face during arm deceleration could explain this: the lip presses against the ball along the arm's normal direction, and friction there could drag down velocity along that same diagonal direction. But that would reduce both vx and vz proportionally, whereas vx actually matches the expected value exactly — so this mechanism doesn't quite explain the asymmetric loss.

I'm also wondering if the discrepancy comes from a wrong assumed ω, but that would scale both components together too, not just vz. The clean 1.7 m/s loss appears purely vertical, which points toward some other vertical-impulse source — maybe the beam's tangential friction contributing a force roughly aligned with the vertical axis rather than the lip contact.

I'm reconsidering the friction mechanism: maybe it's the lip pushing the ball rather than the beam decelerating relative to it. As the arm decelerates sharply, the ball's velocity stays roughly fixed while the arm frame changes rapidly, so the lip contact stays active with friction (μ=1) and a normal force pushing the ball toward the pivot while sliding along the lip face.

Right, when the arm stops abruptly the ball's velocity still has that tip-direction component -ωd carrying it away from the lip, which checks out but doesn't explain much vertical energy loss. The arm overshoot/rebound seems minor too, so I'm wondering if the real cause is that the ball wasn't rigidly co-rotating with the arm — maybe some slipping or rolling occurred that changes the picture.

If the ball starts with zero spin while the arm spins up fast, friction from both the lip and beam contacts would gradually spin the ball up toward matching the arm's angular velocity. During that spin-up phase, the ball might roll along the lip face rather than staying fixed, since the contact geometry resembles a corner where spin lag could push it in an unexpected direction.

Checking my spin-up estimate against the 45° timing, it roughly checks out — around 0.11s to reach 45°, matching when ω should be achieved. But I'm still missing where the vertical velocity loss comes from, which I need to track down.

Thinking about the lip contact friction: if the lip maintains penetration for about 0.01-0.02s with a normal force around 4.5 N decaying from centripetal preload, the impulse works out to roughly 0.07 N·s, giving a velocity change of about 0.7 m/s for the 0.1 kg ball — that's a meaningful contribution, directed along the inward normal.

Combining the friction component with the lip's rebound push, I'm getting vx roughly unchanged and vz reduced by about 1.0, which is reasonably close to the observed ~1.7 reduction, so the lip interaction does seem to be the culprit. Rather than chase an exact diagnosis, I'd rather just redesign around it — making the lip low-friction by setting its friction values explicitly and using geom priority so the lip's friction settings override the default combination rule instead of friction being taken as the max of the two geoms.

I'm questioning whether the rebound push from lip penetration is really the dominant effect, or if the deceleration itself creates an unexpected force on the ball in the arm's frame. Maybe I should rethink the whole geometry—perhaps a tilted surface or notch could provide centripetal force without relying on lip contact, or even consider a completely different release mechanism than the arm stop.

Estimating the rebound velocity from spring damping gives something tiny, around 0.05 m/s, so that's too small to explain the observed vx. Beam friction doesn't quite work either since it requires sustained normal force that vanishes as the arm decelerates, leaving the vx behavior unexplained by that mechanism. I'm leaning toward the frictionless lip fix as the main plan, with the vx match being incidental.

Removing lip friction and the offset issue should let the release velocity match theory, with ratio vz/vx=0.818, and at ω=9.514 the predicted landing should hit the bucket, though empirically tuning remains unreliable given the unexplained residuals. The floor rolling at the end at 0.06 m/s is irrelevant since there's no rolling friction there. I'm considering widening the bucket to an inner radius of 0.35, keeping its center at 3 m, and recalculating the octagon wall half-length from the apothem, getting about 0.158.

I'm also checking the geometry positions (0.37, 0.2616) and bottom radius 0.39, confirming the beam separates from the ball before the lip does so timing isn't an issue, and noting ball spin during flight doesn't matter. For the lip's friction in MuJoCo, I need to recall that priority determines which geom's friction value is used, and that friction values can't go to zero—MuJoCo likely clamps to some minimum like 1e-5—so I should pick a very small but valid friction value for the lip.

I'm reasoning through the physics of ball spin-up: since the lip is frictionless, the ball's rotation depends on tangential friction at the beam contact, and if the ball's spin lags the arm's rotation, sliding at that contact induces a torque that spins the ball up while reaction forces carry it outward along the beam.

Checking the expected landing against observations, with ω=9.514 the velocity matches 0.3889*9.514=3.70, confirming the gravity correction is working, so I'll keep the control value at 9.56. Rolling friction on the floor isn't needed, and the bucket's condim 6 setting should handle the final stop. With predicted vz=3.03 giving a peak height of 1.26m and a fairly steep landing slope, the wider bucket rim at 0.32 should still catch it fine.

But actually checking the simulated trajectory, the ball leaves the arm at 0.12s around 3.9 m/s but flies much flatter than intended at only ~19°, so it lands on the floor at x≈1.8, hits the exterior of the bucket's near wall, bounces back, and creeps along the floor at 0.06 m/s before stopping at x=1.86 — completely missing the bucket.

