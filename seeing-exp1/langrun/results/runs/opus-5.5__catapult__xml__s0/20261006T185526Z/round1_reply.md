**What happened in the run**

- The arm swings up and hits its 40° stop at 0.16 s, moving 299°/s (5.22 rad/s). That is the planned speed.
- The ball leaves from about where I predicted, around (−0.64, 1.13).
- Its launch velocity is wrong: about (3.32, 2.45) m/s, which is 4.13 m/s at 36°. The plan was (3.26, 3.39), which is 4.70 m/s at 46°.
- The ball peaks at 1.45 m and comes down short, at x ≈ 1.8, the near edge of the bucket. It clips the bottom disc's rim and the near wall, drops to the floor beside the stand, and rests at x ≈ 1.88. It is never inside the bucket.

**Diagnosis**

The ball's velocity change at release points back toward the arm face and inward along the arm. Only the cup wall can push in those directions: its normal force acts inward and its friction acts along its surface. The friction was at the full μ = 1 limit.

The log also shows the ball leaving the wall at 0.01 s and coming back at 0.05 s. This suggests friction at the wall set the ball spinning and rolling in the cup during spin-up. At the stop, wall friction then dragged the ball and took away much of its upward speed.

**Fix**

I made the ball–arm contacts frictionless. Explicit `condim="1"` contact pairs replace the default ones, and the default contacts between the arm and the ball are excluded. The ball now sits in the corner held only by normal forces, so it can't pick up spin. It should leave along the planned tangent at ω·r ≈ 4.70 m/s.

Nothing else changes; the brief's names are kept. I have not re-run the scene. The landing point is still a hand calculation and needs confirming in a new run.

```xml
<mujoco model="catapult_bucket">
  <compiler angle="degree"/>
  <option timestep="0.002" integrator="implicitfast" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="1 -2 4" dir="-0.2 0.4 -1" directional="true"/>
    <geom name="floor" type="plane" size="10 10 0.1" rgba="0.8 0.85 0.8 1"/>

    <!-- catapult frame (visual only, does not collide) -->
    <geom name="catapult_base" type="box" pos="-0.3 0 0.03" size="0.7 0.2 0.03" rgba="0.45 0.3 0.15 1" contype="0" conaffinity="0"/>
    <geom name="catapult_post_left" type="box" pos="0 0.12 0.28" size="0.02 0.02 0.22" rgba="0.45 0.3 0.15 1" contype="0" conaffinity="0"/>
    <geom name="catapult_post_right" type="box" pos="0 -0.12 0.28" size="0.02 0.02 0.22" rgba="0.45 0.3 0.15 1" contype="0" conaffinity="0"/>
    <geom name="catapult_axle" type="cylinder" fromto="0 -0.14 0.5 0 0.14 0.5" size="0.015" rgba="0.3 0.3 0.3 1" contype="0" conaffinity="0"/>
    <geom name="catapult_stop_post_left" type="capsule" fromto="-0.28 0.12 0.06 -0.2839 0.12 0.7839" size="0.012" rgba="0.45 0.3 0.15 1" contype="0" conaffinity="0"/>
    <geom name="catapult_stop_post_right" type="capsule" fromto="-0.28 -0.12 0.06 -0.2839 -0.12 0.7839" size="0.012" rgba="0.45 0.3 0.15 1" contype="0" conaffinity="0"/>
    <geom name="catapult_stop_bar" type="cylinder" fromto="-0.2839 -0.14 0.7839 -0.2839 0.14 0.7839" size="0.015" rgba="0.3 0.3 0.3 1" contype="0" conaffinity="0"/>

    <!-- catapult arm: pivot at z=0.5, angle 0 = pointing along -x, rotates up to 40 deg -->
    <body name="catapult_arm" pos="0 0 0.5">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 40" limited="true" solreflimit="0.006 1"/>
      <geom name="catapult_beam" type="box" pos="-0.43 0 0" size="0.53 0.04 0.02" mass="0.3" solref="0.005 1" rgba="0.6 0.4 0.2 1"/>
      <geom name="catapult_cup_wall" type="box" pos="-0.95 0 0.06" size="0.01 0.04 0.04" mass="0.02" solref="0.005 1" rgba="0.5 0.3 0.15 1"/>
    </body>

    <!-- ball resting on the arm against the cup wall -->
    <body name="ball" pos="-0.9 0 0.56">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" solref="0.005 1" rgba="0.85 0.1 0.1 1"/>
    </body>

    <!-- stand under the bucket -->
    <geom name="stand" type="cylinder" pos="2.1 0 0.2" size="0.15 0.2" rgba="0.5 0.5 0.55 1"/>

    <!-- bucket: centre exactly 3 m from the ball's start -->
    <body name="bucket" pos="2.1 0 0.56">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 -0.14" size="0.32 0.02" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_00" type="box" pos="0.31 0 0" euler="0 0 0" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_01" type="box" pos="0.2864 0.1186 0" euler="0 0 22.5" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_02" type="box" pos="0.2192 0.2192 0" euler="0 0 45" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_03" type="box" pos="0.1186 0.2864 0" euler="0 0 67.5" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_04" type="box" pos="0 0.31 0" euler="0 0 90" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_05" type="box" pos="-0.1186 0.2864 0" euler="0 0 112.5" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_06" type="box" pos="-0.2192 0.2192 0" euler="0 0 135" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_07" type="box" pos="-0.2864 0.1186 0" euler="0 0 157.5" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_08" type="box" pos="-0.31 0 0" euler="0 0 180" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_09" type="box" pos="-0.2864 -0.1186 0" euler="0 0 202.5" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_10" type="box" pos="-0.2192 -0.2192 0" euler="0 0 225" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_11" type="box" pos="-0.1186 -0.2864 0" euler="0 0 247.5" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_12" type="box" pos="0 -0.31 0" euler="0 0 270" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_13" type="box" pos="0.1186 -0.2864 0" euler="0 0 292.5" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_14" type="box" pos="0.2192 -0.2192 0" euler="0 0 315" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_15" type="box" pos="0.2864 -0.1186 0" euler="0 0 337.5" size="0.01 0.062 0.16" solref="0.005 1" rgba="0.2 0.4 0.8 1"/>
    </body>
  </worldbody>

  <contact>
    <!-- ball sits frictionlessly in the cup so it cannot spin up or be dragged by the cup wall at release -->
    <exclude name="no_default_arm_ball" body1="catapult_arm" body2="ball"/>
    <pair name="ball_on_beam" geom1="ball" geom2="catapult_beam" condim="1" solref="0.005 1"/>
    <pair name="ball_on_cup_wall" geom1="ball" geom2="catapult_cup_wall" condim="1" solref="0.005 1"/>
  </contact>

  <actuator>
    <!-- velocity servo with a filtered (smoothly ramping) target: torque = 100*(act - qvel), act -> ctrl with tau 0.02 s -->
    <general name="catapult_motor" joint="catapult_hinge" dyntype="filter" dynprm="0.02" gaintype="fixed" gainprm="100" biastype="affine" biasprm="0 0 -100" ctrlrange="0 10" ctrllimited="true"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0 -0.9 0 0.56 1 0 0 0" qvel="0 0 0 0 0 0 0" act="0" ctrl="5.233"/>
  </keyframe>
</mujoco>
```

```json
{"what_happens": "The motor swings the arm up to its 40 deg stop at 0.16 s at the planned speed, but the ball leaves at about 4.1 m/s and 36 deg instead of 4.7 m/s and 46 deg. Friction at the cup wall during the stop appears to have taken much of its upward speed. The ball falls short, clips the near edge of the bucket (bottom rim and near wall) at 0.88 s, drops to the floor beside the stand and rests at x = 1.88 m, outside the bucket.", "works": false, "problem": "Friction between the ball and the cup wall (and probably spin picked up in the cup) cuts the ball's launch speed and angle at release, so it lands short of the bucket."}
```

---
thinking (summarized):

The ball came up short — recalculating, the release angle looks shallower than expected, around 36.4° with speed closer to 4.13 rather than 4.70, which explains the shorter throw even though arm angular velocity seems fine.

I'm wondering if the ball wasn't rigidly released but instead rolled along the cup face during the spin-up, with tangential friction forces inducing rolling rather than a clean separation. That would explain why vx came out higher than expected while vz dropped well below prediction — the ball might have been slipping relative to the arm face during contact rather than being purely carried along with it.

Maybe during the impact, the ball pressed against the outer wall by centripetal force gets dragged by wall friction instead — with a high normal force around 2.45 N over roughly 0.01 s, that only shaves off about 0.245 m/s tangentially without changing direction much. There's also the arm's overshoot to 41.4° before settling back, suggesting the face decelerates while the ball is still sliding along it, which could explain part of the directional shift.

I'm checking whether the ball stays pressed against the wall during contact — it looks like the velocity component moves it away from the face quickly, so contact is lost right after. That resolves why the wall touched briefly at 0.01s and again at 0.05s, after which the ball should move rigidly without further contact.

Back-extrapolating from the 0.25s position to the release time at 0.163s gives a predicted position of about (-0.651, 1.124), which matches well, but the velocity doesn't: expected roughly (3.256, 3.394) versus actual (3.32, 2.45). So the vertical velocity lost about 0.94 m/s at release while horizontal gained slightly — something in the arm's impact must have absorbed that vertical component, possibly from stiffness causing an overshoot.

Decomposing that velocity discrepancy in the arm's frame at 40°, the impulse points mostly inward and back toward the face rather than outward, suggesting the arm pushed back against the ball rather than cleanly releasing it.

The 1.4° overshoot and rebound explain it — the soft contact spring stored compression from the centripetal load, then released as the arm snapped back, producing a normal impulse (~6.6 N effective) bigger than the steady centripetal force itself, with friction dragging along at the saturated cone. I should try reducing the friction between contacts to tame this spike.

I realize the pair alone won't suppress the default dynamic contact, so I'd need an exclude directive between the arm and ball bodies while keeping the explicit pair active, possibly setting condim=1 for a frictionless contact. But I should double check whether this is actually the root cause, since the inward normal impulse isn't friction-driven in the first place—it's a geometric effect from the contact normal direction itself.

Actually the face normal can't pull the ball, so it must be the wall exerting that impulse — normal plus saturated friction. That points to an Euler-type effect: as the arm decelerates rapidly, the ball in the rotating frame gets pressed into the wall, producing the inward impulse I'm seeing.

Maybe I should sidestep the cup-wall mess entirely by reshaping the ball's resting geometry, or focus on the arm's stop transient instead — the 1.4° overshoot at 523 Nm could be storing energy that leaks into the launch. Rather than chasing this nonlinear perturbation, it might be simpler to just retune against the known target of 4.13 at 36.4°, or eliminate the wall-contact dependency altogether by changing the release tilt.

Trying friction alone to hold the ball against centripetal force doesn't work — the numbers don't support it, so that's a dead end. Switching the ball-arm contact to frictionless doesn't resolve the puzzle either, since the inward normal impulse into the wall is still unexplained even with tiny analytic penetration estimates — I'm starting to wonder if the ball was actually positioned differently than I assumed, not sitting in the corner at all.

Checking whether deceleration-induced Euler forces could push the ball into the wall instead, but that actually pushes it away from the face; centrifugal force from residual angular velocity only accounts for a tiny fraction of the observed impulse, nowhere near 0.066. I'm going to abandon this line of micro-analysis and look for a sturdier underlying mechanism instead.

Maybe I should reconsider the geometry so the ball sits in a pocket rather than against a vertical wall, or just accept contact noise as deterministic and empirically correct for it—figuring out what launch conditions get the ball from its release point near (-0.64, 1.134) to the target around x≈2.1, z=0.48.

I'm checking where the ball actually landed: it hit the bucket bottom and side wall around 0.88 s, falling short by roughly 0.35 m. I'm trying scaling the launch speed while keeping the same 36.4° angle, solving the projectile equations for the required speed to cover the remaining horizontal distance and vertical drop to hit the target.

I get v² ≈ 21.25, meaning v ≈ 4.61 versus the current 4.13 — a scale factor of about 1.116, which would push ω up to around 5.83. But I suspect the error might instead grow with ω² if the impulse mechanism is centripetal-driven, so simple linear scaling might not be right. I think I should go back and reconsider the detachment mechanism itself, particularly how the ball separates from the spinning face during the 0.01–0.05 s window.

Thinking through the forces: the face's normal force passes through the ball's center so it gives no torque, while friction acting along the face could impart spin — with the wall contact point on the ball's outer side moving tangentially, dragging the ball into rotation as the arm accelerates. I'm trying to work out whether the ball ends up rolling inward along the face due to this friction-induced spin, which would explain why it separates from the wall early in the cycle.

My robust fix is to make the ball-arm contact frictionless (set that collision pair's condim to 1), so the arm can't impart spin — leaving the ball to just slide in the corner, with the wall normal supplying centripetal force and the face normal supporting it.

I'm confirming that explicit contact pairs bypass the exclude filter, since MuJoCo always generates contacts for named pairs regardless of exclusion rules—so my setup should still work. The arm's 1.4° overshoot limit seems fine, and the release conditions check out: ω×r gives roughly 4.70 velocity at the predicted radius of 0.902, matching expectations for the frictionless case.

