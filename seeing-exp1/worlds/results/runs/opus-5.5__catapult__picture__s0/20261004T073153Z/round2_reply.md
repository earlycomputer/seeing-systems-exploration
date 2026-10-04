## What the picture shows

The run looks almost the same as the last one.

- **Catapult:** The arm swings up to its stop and throws the ball.
- **Ball in flight:** The ball's flight copies sit low. One is near x ≈ 0.1 m, z ≈ 0.95 m. Another is near x ≈ 1.15 m, z ≈ 0.8 m. My calculation put the ball near the top of the frame at that point.
- **Where the ball ends:** It finishes on the floor outside the bucket. A trail of slow copies runs from about x ≈ 1.8 m to the near outer wall at x ≈ 2.5 m. No copy is inside the bucket.
- **Comparison with the last run:** 6% more torque and a wider bucket changed almost nothing. The release speed seems to be only about 70–75% of what I calculated, which means roughly half the launch energy never reached the ball.

## Why the throw is short

My release speed came from an energy balance: constant motor torque, ideal rigid contact between ball and arm. I could not find from the picture where the missing energy goes. The fix should therefore not depend on that balance at all.

## The change

I added strong viscous damping to the hinge (4 N·m·s/rad) and raised the motor torque to match. The arm now spins up within a few hundredths of a second and coasts to the 45° stop at a near-constant terminal speed. That speed is set by torque minus the gravity torque, divided by the damping, which is about 10.9 rad/s. That gives a tip speed of about 5.5 m/s. Collision losses or inertia errors no longer change it. By my calculation, the throw now lands in the middle of the bucket's window: it should clear the near rim and either land inside or bank off the tall far wall. I have not run this version.

```json
{"what_happens": "The arm swings to its 45-degree stop and throws the ball, but the ball flies low and short, hits or lands just in front of the bucket's near wall, and ends up rolling on the floor between x of about 1.8 and 2.5 m outside the bucket.", "works": false, "problem": "The release speed is well below the torque-and-energy estimate (some launch energy is lost), so the ball falls short of the bucket's opening."}
```

```xml
<mujoco model="catapult_bucket">
  <compiler angle="degree" inertiafromgeom="true"/>
  <option timestep="0.002"/>

  <worldbody>
    <light name="sun" pos="1.5 -2 4" dir="-0.3 0.5 -1" directional="true"/>
    <geom name="floor" type="plane" size="10 10 0.1" rgba="0.8 0.85 0.8 1"/>

    <!-- static catapult frame -->
    <body name="catapult_frame" pos="0 0 0">
      <geom name="catapult_base" type="box" size="0.4 0.15 0.03" pos="-0.15 0 0.03" rgba="0.5 0.35 0.2 1"/>
      <geom name="catapult_post_left" type="box" size="0.03 0.015 0.185" pos="0 0.08 0.215" rgba="0.5 0.35 0.2 1"/>
      <geom name="catapult_post_right" type="box" size="0.03 0.015 0.185" pos="0 -0.08 0.215" rgba="0.5 0.35 0.2 1"/>
      <geom name="catapult_axle" type="cylinder" fromto="0 -0.1 0.4 0 0.1 0.4" size="0.01" rgba="0.3 0.3 0.3 1"/>

      <!-- throwing arm: hinge about y, strongly damped so it coasts at a fixed terminal speed to the 45 deg stop -->
      <body name="catapult_arm" pos="0 0 0.4">
        <joint name="catapult_hinge" type="hinge" axis="0 1 0" limited="true" range="0 45" solreflimit="0.01 1" damping="4"/>
        <geom name="catapult_hub" type="cylinder" fromto="0 -0.03 0 0 0.03 0" size="0.02" mass="0.02" contype="2" conaffinity="2" rgba="0.3 0.3 0.3 1"/>
        <geom name="catapult_beam" type="box" size="0.3 0.03 0.01" pos="-0.28 0 0" mass="0.3" contype="2" conaffinity="2" rgba="0.6 0.45 0.25 1"/>
        <geom name="catapult_lip_outer" type="box" size="0.015 0.03 0.03" pos="-0.555 0 0.04" mass="0.02" contype="2" conaffinity="2" rgba="0.6 0.45 0.25 1"/>
        <geom name="catapult_lip_inner" type="box" size="0.015 0.03 0.03" pos="-0.44 0 0.04" mass="0.02" contype="2" conaffinity="2" rgba="0.6 0.45 0.25 1"/>
      </body>
    </body>

    <!-- ball resting in the cup at the arm tip -->
    <body name="ball" pos="-0.5 0 0.45">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" contype="1" conaffinity="3" rgba="0.9 0.2 0.2 1"/>
    </body>

    <!-- open bucket centred 3 m downrange: inner radius 0.45 m, walls 0.55 m tall -->
    <body name="bucket" pos="3 0 0">
      <geom name="bucket_bottom" type="cylinder" size="0.47 0.01" pos="0 0 0.01" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_00" type="box" size="0.01 0.092 0.275" pos="0.46 0 0.275" euler="0 0 0" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_01" type="box" size="0.01 0.092 0.275" pos="0.425 0.176 0.275" euler="0 0 22.5" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_02" type="box" size="0.01 0.092 0.275" pos="0.3253 0.3253 0.275" euler="0 0 45" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_03" type="box" size="0.01 0.092 0.275" pos="0.176 0.425 0.275" euler="0 0 67.5" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_04" type="box" size="0.01 0.092 0.275" pos="0 0.46 0.275" euler="0 0 90" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_05" type="box" size="0.01 0.092 0.275" pos="-0.176 0.425 0.275" euler="0 0 112.5" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_06" type="box" size="0.01 0.092 0.275" pos="-0.3253 0.3253 0.275" euler="0 0 135" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_07" type="box" size="0.01 0.092 0.275" pos="-0.425 0.176 0.275" euler="0 0 157.5" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_08" type="box" size="0.01 0.092 0.275" pos="-0.46 0 0.275" euler="0 0 180" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_09" type="box" size="0.01 0.092 0.275" pos="-0.425 -0.176 0.275" euler="0 0 202.5" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_10" type="box" size="0.01 0.092 0.275" pos="-0.3253 -0.3253 0.275" euler="0 0 225" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_11" type="box" size="0.01 0.092 0.275" pos="-0.176 -0.425 0.275" euler="0 0 247.5" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_12" type="box" size="0.01 0.092 0.275" pos="0 -0.46 0.275" euler="0 0 270" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_13" type="box" size="0.01 0.092 0.275" pos="0.176 -0.425 0.275" euler="0 0 292.5" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_14" type="box" size="0.01 0.092 0.275" pos="0.3253 -0.3253 0.275" euler="0 0 315" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall_15" type="box" size="0.01 0.092 0.275" pos="0.425 -0.176 0.275" euler="0 0 337.5" rgba="0.2 0.4 0.8 1"/>
    </body>
  </worldbody>

  <actuator>
    <motor name="catapult_motor" joint="catapult_hinge" gear="1" ctrllimited="true" ctrlrange="0 60"/>
  </actuator>

  <keyframe>
    <key name="start" ctrl="44.7"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

Checking the pixel coordinates again, the streak near the bucket maps to roughly x=1.76 to 2.52, right by the wall where the bucket sits at 2.53 — so the ball is landing outside the bucket on the floor again, same failure mode despite the added energy and larger bucket size.

Tracing the trajectory through the other dots, the ball is still following a low, shallow arc — roughly 15-20° launch angle, with similar horizontal speed near 4 m/s. This is strange given more torque should have changed the result, which makes me reconsider whether the arm actually overshoots 45° substantially before releasing the ball, or whether I've got the rotation direction or contact surface wrong — maybe the ball isn't resting on the top of the arm the way I assumed.

The z-offset seems linear in time rather than quadratic, suggesting the vertical launch velocity is lower than I estimated—around 1.9 m/s instead of 3.4, giving a shallower 25° angle at similar speed. My row readings might just be imprecise, but both runs land the ball in roughly the same spot despite the torque difference, which matches the streak extending from pixel 72 to 90 in the plan.

I'm wondering if release happens later than the assumed 45° arm angle, maybe closer to 55°, which would change the release direction and effective angle to around 29°—this could come from joint softness or solver impedance settings rather than a radial velocity component.

Given the critically-damped stop dynamics with timeconst 0.01, the arm's overshoot at the joint limit works out to roughly 0.04 rad, which is a similar scale regardless of the exact damping ratio used. Now I need to check whether the ball actually separates from the arm during this deceleration phase.

I'm also realizing I need to account for the ball's spin — it's rotating about the y-axis at roughly 10.6 rad/s while rolling with the arm, so at the moment of release there's relative sliding at the outer lip contact point due to friction, which depends on whether the ball's surface velocity from spin matches the arm's velocity at that contact point.

Once the arm stops, though, the normal force at the lip essentially vanishes, so friction there stops mattering much. The real effect might instead be the contact springing back after compression from centrifugal force, which would push the ball outward and shift velocity components rather than change them in the direction I was assuming — I'm estimating this springback force is on the order of a few newtons based on the tangential push during spin-up.

I should also double check whether I'm misreading the z-values from the plot. Looking at both runs, the ball consistently lands just short of the bucket around x~1.8-2.5, and even with more torque and a wider bucket the landing spot barely shifts. That consistency makes me think the ball is actually hitting the outside of the bucket's near wall rather than falling in — and tracing the pixel positions, the right edge of the landing streak lines up almost exactly with where the near wall moved to in the wider-bucket case, while the left edge stays nearly fixed. So the ball seems to be striking and resting against the wall's exterior.

Given how uncertain this reconstruction is, I think I need to step back and consider whether there's a bigger systemic error — maybe the ball's energy is genuinely lower than I assumed because it loses contact with the track partway through, which would change my whole picture of the trajectory.

The energy doesn't balance — predicted KE is roughly 4.13 J but observed kinetic energy from the ball's speed is only about 2 J, a gap too large to explain by the torque difference alone. I'm wondering if the ball actually releases before reaching 45°, at some earlier angle θ_r, where the energy balance would be torque times θ_r minus potential energy at that point, and the launch angle would then be steeper than I assumed.

I check whether an earlier release gives a steeper, lower-speed launch that could match a flatter observed trajectory, but that seems contradictory. I also double-check the contact settings between the ball and arm geoms using their contype/conaffinity values, confirming contact is indeed enabled, so that's not the issue.

Since I can't pin down the exact cause of the discrepancy, I decide to switch strategies: instead of relying on gravity/torque dynamics, I'll use a velocity actuator with high gain to drive the arm at a fixed angular speed, making the release speed simply ω·r once the actuator reaches its target before the 45° limit.

I'm checking the stability of this velocity servo against the integrator timestep — with gain too high relative to inertia and dt, explicit Euler could go unstable, so I need to pick a gain low enough to stay stable while still being fast enough to settle before the ball releases. I'm also worried the sudden velocity jump will impulsively jerk the ball, possibly causing it to bounce off the arm's contact surface rather than smoothly accelerating to match the arm's speed.

So I'm trying a softer servo with a time constant around 0.05s, checking whether the arm covers the needed travel angle before saturating at the target angular velocity, computing the angle traversed and the resulting velocity at a sample time to see if the motion profile is realistic for the throw.

Given the uncertainty in tuning this rotational launcher precisely, I'm considering switching to a fundamentally more deterministic mechanism: a linear slide (prismatic joint) angled at 45°, with a flat paddle pushing the ball along a straight track via constant force until hitting a hard stop. This way the ball just inherits the plate's velocity directly along the launch axis, avoiding any rotational effects, centrifugal uncertainty, or lip geometry issues that plagued the rotating arm design.

That said, I worry a piston-launcher deviates from what the brief calls a "catapult" in spirit, so I'm hesitant to abandon the rotating arm entirely. I'm now digging into exactly what happens during the swing: soft contact dynamics could cause the ball to bounce off the beam surface mid-launch, separating and re-contacting, and each bounce through a damped contact model would bleed off kinetic energy unpredictably -- which could explain inconsistent launch results.

I'm also checking whether the ball ends up wedged against both the surface and the lip, rotating rigidly with no sliding, which would rule out friction losses there, and whether anything else near the joint or release point could be eating energy before launch.

I wonder if instead of trying to predict the exact bounce behavior, I should just pick a design robust enough that small errors don't cause a miss—though a bigger bucket won't help since the size is fixed. I should test whether ball "chatter" against the lip is actually causing nonlinear energy loss as torque increases, and also double check the joint's range limit, since it's specified in degrees and converts to about 0.785 rad, which could be the real constraint shaping the arm's swing.

Actually I should verify the arm really hits that 45° limit rather than something else—checking collision groups, arm only contacts the ball, not other geoms, so that's not it. Gravity torque already accounts for the ball's mass too. Since my readings of the trajectory dots are unreliable, I'm now wondering if the ball could simply be overshooting and flying past the bucket entirely rather than falling short.

Trying to pin down the loss model from two runs isn't working cleanly—the landing position seems similar despite extra energy, suggesting the streak's left end might not actually mark the landing point but rather where the ball rolls in. I should stop trying to reverse-engineer the physics from noisy comparisons and instead design more directly for the intended outcome.

Thinking structurally about what's actually going wrong: the chatter at the start happens because the ball sits with some gap or penetration against the arm, then the arm suddenly accelerates and they repeatedly separate and recollide, bleeding energy each time. Since I can't ramp the control signal, I need another fix—maybe reshaping the cup geometry or adjusting contact stiffness so the ball stays engaged with the arm surface instead of chattering loose.

Going back to the energy accounting, I can't account for a 50% loss yet: motor work comes out to about 4.88 J, potential energy rise totals roughly 1.05 J, and I'm now re-checking whether MuJoCo's computed inertia for the arm box is larger than my estimate of 0.068, which would change how much kinetic energy the arm actually carries.

Recomputing the box inertia gives roughly the same value as before, so that's not the source of the discrepancy. Using energy conservation, release angular velocity comes out near 10.5 rad/s and ball speed near 5.3 m/s, which actually matches the horizontal velocity reading at 39°, suggesting the launch speed is probably correct after all — so the vertical mismatch must come from either a misread row in my data or the release angle being steeper than the 45° I assumed, meaning the motor does more work and launches the ball flatter than expected.

Testing a steeper release angle doesn't fix the horizontal velocity match either. I'm now wondering if the discrepancy comes from the ball physically colliding with the launcher frame or arm after release rather than flying freely under gravity, though the geometry doesn't obviously support that. Since MuJoCo doesn't model spin effects like Magnus force, the clean ballistic trajectory should hold, which makes me suspect something about my assumed release conditions is off rather than the physics itself.

That clears the wall by 0.2 so the launch parameters must be off somewhere. Maybe I'm misreading the plan view — that line to the left of the bucket at floor level isn't part of the bucket geometry but residual ball positions, meaning the ball was rolling slowly across that range rather than sitting at one spot, which would explain the streak better than a bad launch calculation.

Since MuJoCo balls keep rolling indefinitely without rolling friction, this slow backward streak from 2.5 to 1.8 over about 5 seconds (roughly 0.14 m/s) makes sense if the ball bounced off the bucket's outer wall and rolled back at constant speed — darkest near 1.8 where it ends up.

Checking the trajectory data though, both the old wall (2.70, height 0.36) and new wall (2.54, height 0.55) show the ball landing noticeably lower than my predicted parabola suggests — consistently about 0.25-0.3 m below expected height around x≈2.6. I'm trying to work out what speed shortfall would account for that deficit using the trajectory equation.

Solving for the efficiency factor f, both data points point toward f≈0.8 or lower, but using an earlier data point around x=1.43 with z≈0.8 gives f≈0.5, which is inconsistent. If f were actually 0.5, the ball would hit the ground around x=1.78 well before reaching the wall at all, so I need to reconsider whether the ball bounces or rolls the rest of the way to make contact.

Given this uncertainty in f, I should look for a physical mechanism I trust more rather than relying on noisy fits. Comparing arm angular acceleration without the ball (131 rad/s²) versus with the ball attached (82 rad/s²) suggests the contact isn't rigid — the arm likely accelerates briefly alone before compressing into the ball through a soft contact, which could explain the energy loss.

This could mean the ball separates and re-collides with the arm multiple times as it overshoots, each inelastic impact bleeding away kinetic energy, though probably not enough alone to account for a 50% loss. Friction and sliding at the contact surface might also contribute, since centrifugal force presses the ball into the arm as it swings.

Since I can't run an actual simulation, I'm thinking through alternative designs instead—maybe a longer smoother acceleration profile, a deeper cradle to prevent separation, or rethinking the release geometry entirely. The core issue seems to be the ball-arm interface itself.

I'm trying to back into the right torque value using an estimated efficiency factor: if efficiency is around 0.5-0.65, I need to scale up the theoretical kinetic energy and resulting torque accordingly to still hit the target launch energy.

Now I'm reconsidering what the efficiency actually looks like based on the trajectory data from both runs—trying to narrow down whether f is closer to 0.5 or higher, cross-checking against where each shot landed relative to the walls, and using the angle/velocity readings to see if a launch angle near 39° with f≈0.5 reproduces the observed landing position.

Testing a later release time doesn't match the dot positions well either. I'm leaning toward f≈0.5 as the best fit, since that launch angle and speed traces through the (1.15,0.77) point consistent with a roughly 39° trajectory, whereas an earlier release at 30° gives too steep an arc to match the observed path.

Half-energy-loss patterns like equal-mass inelastic collisions don't obviously apply here, so I'm considering other explanations: maybe the ball isn't actually held at r=0.5 when centrifugal force pushes it outward against the lip, or maybe the lip isn't truly constraining the ball at release — checking the geometry, with the lip top at 0.07 relative to the arm center and the ball center at 0.05, the ball could be sitting right at the edge of being released early rather than at the expected position.

Now I'm analyzing forces along the arm itself: gravity has a component pulling inward toward the pivot (about 6.9 m/s² at 45°), while centrifugal force pushes outward at ω²r, so centrifugal only wins once ω exceeds roughly 3.7 rad/s — meaning early in the swing the ball is actually pulled inward toward the pivot rather than outward against the lip.

So the ball likely rolls just 5mm inward toward the inner lip first, sits there until spin builds up, then rolls back out to hit the outer lip — a negligible effect on the overall motion. I'm setting that root-cause investigation aside and double-checking the energy partition instead: the ball's share of kinetic energy comes out to about 37%, giving a ball velocity around 5.33 m/s, confirming that part of the calculation was already handled correctly.

I keep running through other possible culprits — arm inertia estimation, motor/joint limit settings, armature, friction loss, gravity compensation — but none of them seem to be the actual issue, and I'm fairly confident the ball isn't getting wedged or dragged unexpectedly by the arm's motion. Given the uncertainty, I'm leaning toward picking a mechanism that doesn't depend on hitting a precise speed at all, like exploring a different design such as a dump-based release instead.

Since range scales with velocity squared regardless of launch angle, and sensitivity near 45° is minimal, speed really is the critical variable I need to control precisely. That pushes me toward a velocity-capped arm design: by tuning joint damping, the arm would approach a terminal angular velocity set by torque over damping, which would make release speed insensitive to inertia estimates or mechanical losses — I just need the time constant (inertia over damping) to be short compared to the swing duration so it reaches that terminal velocity before release.

The arm reaches 10 rad/s within 0.05s, so the ball should accelerate fine unless the loss is specifically at the ball-arm contact interface rather than the arm dynamics. Pressing against the limit stop with 43 N·m torque should hold firmly, and release speed comes out to roughly ωr once gravity's contribution at 45° is factored in.

I'm now computing the gravity torque more precisely: moment arm times mass gives about 1.1 N·m at 45°, so the control target becomes damping torque plus this gravity offset. Checking the time constant with the ball's inertia included (~0.017s), the system reaches terminal velocity well before 45° is reached, confirming the approach is robust to typical energy losses — though it still wouldn't address a problem originating in the release angle or rotation timing itself.

I'm also considering whether the actual observed ω was lower (around 7.5 instead of 10.6), which would point to an energy-loss factor rather than a flaw in the deterministic damping approach, since the ball's reaction torque during steady rotation is purely centripetal and doesn't affect the arm's angular velocity. I'm now checking the initial acceleration spike to see if it could cause contact chatter.

No bounce concern resolved there. Now turning to the f mapping question, I'm solving for ω that gives f=1.04: working through v²=30.09, v=5.485, ω=10.92, giving τ≈44.8. I'm refining the gravity torque estimate at θ=45°, computing the arm's COM position and the resulting torque contribution from gravity, getting roughly -0.583.

Adding up the ball and lip contributions brings the total gravity torque to about 1.02 N·m, so τ = 43.68+1.02 ≈ 44.7 — the gravity correction is a minor fractional adjustment relative to the dominant 43 N·m term. The ball doesn't add any reaction at steady state. I'm setting ctrlrange to 0-60 with joint damping of 4, and checking that the soft limit handles the 44.7 N·m press fine, though I want to double check the deceleration behavior as the arm hits the limit at ω≈11.

The overshoot from this looks small, and the exponential decay with T=0.017 over ~0.09s checks out. I'm also confirming the ball stays seated through release since at constant ω the surface only needs to counter gravity's normal component, with centrifugal force holding it against the lip — that's fine. The bucket center lands at 1.04 within the 0.915-1.18 window, accurate to about ±1% from the damping model, so I'll finalize the description and write the final file.

