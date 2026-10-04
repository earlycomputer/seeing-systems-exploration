## What the picture shows

At 128 px the picture only roughly shows what happened, so this reading is uncertain in places.

- **Catapult:** The arm swings up and stays parked at its 45° stop.
- **Ball in flight:** There are one or two faint ball copies above the field, around x ≈ 0–1.1 m.
- **Where the ball ends:** In both views there is a trail of ball copies at floor level between about x ≈ 1.8 m and 2.7 m. That trail runs right up to the near outer wall of the bucket. No ball copy is visible inside the bucket.
- **Conclusion:** The throw came up short. The ball either clipped the near rim or landed in front of the bucket, and then rolled along the floor against the bucket's outside.

## Why it missed

My hand calculation left only about 0.28 m of clearance over the near rim. That works out to roughly a 9% error in range, or about 4–5% in launch speed. Small energy losses in the soft contacts and the joint limit are enough to use up that margin. I can't find the exact loss from this picture.

## Changes

- **Bucket:** Inner radius goes from 0.30 m to 0.45 m, and the walls go from 0.36 m to 0.55 m tall. The ball now has to clear the near rim and can bank off the tall far wall. By my own projectile estimate (not yet run), a throw lands inside for launch energy roughly 0.92–1.18× nominal. Before, the margin was about ±7% in range.
- **Motor torque:** Raised from 6.22 to 6.6 N·m. This puts the shot near the middle of that window even with losses about as large as this run seemed to have.

```json
{"what_happens": "The arm swings to its 45-degree stop and throws the ball forward, but the ball's copies end up on the floor between about x = 1.8 and 2.7 m, against the outside of the bucket's near wall; no copy is seen inside the bucket.", "works": false, "problem": "The throw falls short (or clips the near rim) because the bucket's entry window was too tight for the small energy losses in the launch, so the ball ends on the floor outside the bucket."}
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

      <!-- throwing arm: hinge about y, swings from horizontal (pointing -x) up to a 45 deg stop -->
      <body name="catapult_arm" pos="0 0 0.4">
        <joint name="catapult_hinge" type="hinge" axis="0 1 0" limited="true" range="0 45" solreflimit="0.01 1" damping="0"/>
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
    <motor name="catapult_motor" joint="catapult_hinge" gear="1" ctrllimited="true" ctrlrange="0 10"/>
  </actuator>

  <keyframe>
    <key name="start" ctrl="6.6"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

Looking at the tiny 128x128 image, I'm tracing the catapult position on the left and bucket on the right, spotting faint residue dots that mark the ball's trajectory at different timestamps—a few near the catapult and one further along in both the top band and plan view, which should help me reconstruct the flight path.

I convert pixel coordinates to meters using roughly 27.1 pixels per meter, placing the bucket at x=3m (pixel 108) and the catapult near x=0 (pixel 27). One dot at pixel 57 corresponds to about x=1.11m, and mapping its row in the top band suggests a height around z=0.73m, which I'm checking against where the trajectory should be at that x position.

Actually that dark streak near the bucket at row ~37 lines up with z≈0.03, right at floor level — so the ball must have rolled along the ground up to the bucket's wall rather than landing inside it. That suggests the ball fell short of the bucket and rolled forward, landing around x≈1.1, which points to the shot being underpowered rather than overpowered.

I'm trying to figure out why: using range ∝ v², the launch speed seems way lower than planned (~3.5 m/s vs expected), so something is causing energy loss — maybe the ball releases before reaching the intended 45° angle, slips on the arm, or the joint limit softness (solreflimit) is absorbing energy rather than launching cleanly.

Checking the dot positions over time doesn't quite line up with a simple constant-velocity trajectory either, which makes me suspect the ball might be spinning off the arm with some rolling motion rather than flying freely — I need to think through whether the ball's spin direction about the y-axis is consistent with it rolling forward correctly after landing.

I'm still not confident what exactly causes the discrepancy. It could be a lower release speed from the lip constraint, friction torque during release, or possibly something about how the joint limits are set up in the simulation affecting the arm's actual release angle.

I'm also considering whether the ball struck the bucket rim and bounced outward, rolling back toward x~1.8 on the floor, versus simply continuing forward to 2.7. The isolated dot near (1.11, 0.73) might represent the ball mid-flight, but I need to check if that height matches the expected trajectory at that x position.

Running the numbers for a path from the release point through (1.11, 0.73), I get a required launch speed around 3.7 m/s — noticeably lower than I'd expect, which makes me wonder if there's an energy loss I'm not accounting for, like drag or a mechanical limitation in the throwing mechanism.

Without a precise diagnosis, scaling torque feels like guesswork — better to reduce dependence on uncertain dynamics. My reading of the tiny image is uncertain too, but the floor streak from 1.8 to 2.7 seems the more trustworthy feature, suggesting the ball lands short of the bucket rather than overshooting, likely resting around 2.7 against something.

I'm reconsidering whether the ball separates from the arm earlier than 45°, thinking through the forces at play — centrifugal and inertial effects from rotation plus gravity acting on the arm itself, and how the arm's angular acceleration depends on torque versus the gravity torque with the ball's weight included. Separation would occur when the normal force between ball and arm surface drops to zero, so I'm setting up that condition explicitly.

I'm also double-checking the contact filtering logic between ball and arm geoms using their contype/conaffinity bitmasks, confirming collisions are enabled where needed and disabled for the hub/axle, and verifying the joint limit solver reference settings in the MuJoCo model are correctly named.

Comparing expected ball trajectory points against the observed data, I'm computing where the ball should be at specific time steps after release, like x=0.13, z=1.10 at t=0.26s, and trying to reconcile these with the plotted positions to figure out whether the shot actually falls short or if my timing/position assumptions are off.

Calculating velocity components from the two observed points gives vx≈4.1 m/s, matching the planned horizontal velocity, but vz works out lower than expected—suggesting the actual launch angle was flatter than planned, which would explain why the shot didn't land in the bucket.

Actually, maybe the ball leaves tangentially when the arm stops, so release direction is perpendicular to the arm — but any overshoot from the soft limit (roughly w*timeconst ≈ 6°) would only shift things slightly, not explain the big discrepancy. Possibly there's an outward radial velocity component building up during flight as the ball presses against the arm before separating, which could skew the launch angle more than simple tangential release would suggest.

Rather than chase exact torque, maybe a bigger bucket would help practically. Checking the expected position at t=0.26 for a launch at 5.3 m/s, 39°, I get roughly (0.13, 1.10), while the observed point is (0.04, 0.95) — close but off by about 4 pixels, which could be reading error. The second planned dot near the top of the band might be clipped or invisible due to the ball's radius, so that stray dot at (1.11, 0.73) may be something else entirely.

Tracing further copies: at t=0.78 the ball would be around x=2.27, z=0.95, and at t=1.04 it drops to about z=-0.1, meaning it lands in the bucket if everything follows the plan. But that conflicts with the floor streak seen between x=1.8 and 2.7 outside the bucket. I wonder if that streak isn't a shadow but actually the flight copies viewed from above, since the x-positions roughly match up in pixels — still working through whether that interpretation holds.

Combining with the plan-view streak at the same x, it looks like the ball's rolling along the floor around x=1.8–2.5, suggesting it landed short of the bucket rather than reaching it cleanly. Trying to back out the vertical velocity from the trajectory points gives inconsistent numbers, but the overall picture still points to a short landing somewhere around x=1.5–1.7.

The likely explanation is a flatter launch angle than intended — maybe the arm overshoots the 45° release point because the ball stays in contact with the arm longer than expected. That could happen if the joint limit constraint is soft (given the solref/impedance settings) and the motor torque is strong enough to keep driving past the intended release angle before the constraint fully engages.

I can't fully resolve the discrepancy through reasoning alone, so maybe I should accept the physics uncertainty and instead design for robustness — making the target bucket bigger or adjusting aim to tolerate the ~50% shortfall I'm observing, rather than chasing an exact analytical fix for why the ball lands at 1.6-1.8m instead of the planned 3.5m.

I'm checking the geometry — the frame posts, axle, and base box don't seem to obstruct the ball's flight path at x=0. So maybe the real issue is the release angle itself: if the ball leaves at a smaller θ than I assumed, the launch angle would be steeper, which changes the range calculation significantly.

Given the uncertainty, the safest path is to flag that the current setup likely isn't working as intended and propose corrected parameters, since adjusting torque or release timing would shift the landing distance toward the needed ~3.3 units rather than the ~1.6–1.8 currently observed.

Computing the impedance stiffness, I estimate the constraint stops motion on a timescale of about 0.01s, giving roughly 6° of overshoot past 45° release with deceleration around 1000 rad/s² — which doesn't fully explain the discrepancy. I'm now wondering if the outer lip of the arm stays in contact with the ball slightly longer during deceleration, effectively carrying it further before true separation.

Maybe I'm overanalyzing the lip-contact geometry — let me step back and consider the ball's spin effects, which seem negligible, and reconsider whether it actually clears the near rim cleanly at x=2.70, z=0.64 with a 0.28 margin, or whether the trajectory overshoots the bucket entirely.

The streak location, between 1.8 and 2.7, falls short of the bucket rather than beyond it. Given the x-velocity reading of about 4.1 m/s seems solid, I'm testing whether a lower z-velocity, consistent with a steeper release angle, better explains where the ball lands — working through the numbers suggests vz is close to zero near the launch point around x≈-0.3, which roughly lines up with the later position readings.

I'm also considering that the release might have been from a higher point with a steeper angle, like 70°, and recalculating the release coordinates and velocity components from the geometry to see if that fits better, though the numbers keep shifting with small changes in angle assumption.

Rather than keep chasing the exact angle interpretation, I should focus on making the design more robust overall—possibly adding a physical constraint related to when the ball separates from the arm rather than relying solely on the soft joint limit.

Redoing the velocity calc with the steeper angle gives a required speed around 6.2, which is roughly double the observed 4.2 in kinetic energy terms — inconsistent with my earlier estimate under the other hypothesis. The two scenarios don't agree well, so I'm reconsidering whether the ball is actually pressed against the outer lip at all, since centrifugal force in the rotating frame should push it outward toward the tip near -0.555.

I'm checking contact setup between ball and surface — both lips and beam share contact type/affinity, so contact should register. Initial conditions look fine too: keyframe sets the control and qpos0 matches arm and ball starting positions. Gravity torque direction also checks out — arm hangs along -x, gravity pulls it down, and positive motor torque correctly lifts it.

I'm now wondering what else could be sapping speed — inertia values seem properly computed from geometry and mass attributes, so that's probably not it. Maybe the joint limit is engaging earlier than expected, since the default margin is zero.

I'm ruling out soft constraint width as the cause, and also doubting that ball penetration or friction mismatch between the ball's spin and arm rotation is responsible — those seem consistent. I keep wondering if the ball is somehow released before reaching the expected angle, but I can't pin down why the arm would decelerate except at the limit itself. Since I can't isolate the exact issue, I think the better approach is to change the design to be more robust rather than keep chasing the unknown — perhaps lengthening the arm and adjusting speed instead of relying on the soft joint-limit release mechanism.

I'm struggling to pin down exact pixel coordinates for the catapult arm and base from the image, so I can't be fully certain of the geometry. I'll decide instead to focus on increasing the energy and making the release point more deterministic, and reconsider whether the ball's initial freejoint position relative to the nested arm body actually matters here.

Checking other possible mechanical effects like joint limit constraints, damping from the integrator, or soft contact behavior from mass ratio, but none of these seem to explain a meaningful discrepancy. I'll settle on proposing the energy increase plus a more reliable release point as the fix.

Actually, I wonder if the ball separates early because it rolls over the outer lip — with the lip top slightly above the ball's center height, the centrifugal and tangential inertial forces could push it against the lip face rather than the arm surface, changing the effective release timing.

So no climbing occurs, and there's no relevant Coriolis effect since there's no relative motion. Angular acceleration stays positive near the end of the swing given gravity torque calculations, so that's consistent. I'm starting to wonder if the "streak on floor" I interpreted is actually just the bucket's own shading rather than the ball itself, and reconsidering whether the ball would even be visible from a top-down view if it's inside the bucket.

Trying to match the plan-view dots and timing against my computed flight path, the numbers don't line up cleanly — some positions suggest the ball near the top edge rather than where I'd expect mid-flight. Given the ambiguity, I think I just need to commit to describing the image as showing a horizontal gray line in front of the bucket on the floor.

I'm concluding the ball fell short and rolled against the outer wall, so I need to increase the torque to boost kinetic energy and correspondingly adjust work and torque values. I'm also considering stiffening the stop and tweaking the bucket's inner radius and wall height to give more margin for the ball to land inside rather than rolling past it.

Reconsidering whether a soft limit could let the arm carry the ball past 45°, I realize that's physically impossible since a decelerating arm releases the ball right at release angle—so the low-angle hypothesis doesn't hold. That means the speed itself must be the issue, and working through the landing geometry with a 39° angle and short range, I calculate v² ≈ 13.7, giving v ≈ 3.7.

Comparing this to the expected 5.33 gives a kinetic energy ratio around 0.48, meaning roughly half the energy seems to be missing somewhere—maybe absorbed by friction, a torque discrepancy, or some joint constraint I haven't accounted for. I start considering whether ball rolling energy could explain the gap.

Checking the two position samples 0.26s apart gives vx≈4.1, which actually matches the planned launch velocity closely, so the initial launch parameters seem right after all—meaning the short landing must come from something happening mid-flight, like the ball colliding with an obstacle during its trajectory. I start computing the apex of the flight path to see where that might occur.

The apex lands near x=1.11, z=1.375, right where the top band edge sits at z=1.39, so the ball's upper edge would barely clip into that band—possibly explaining why I thought it looked short or partially obscured. I reconsider whether I misread the row position of that dot, and the trajectory timing actually seems consistent with a clean flight after all.

The gray streak near the bucket from x=1.8 to 2.7 at floor level is harder to explain. Since nothing else moves except the arm (which stays near the catapult) and the ball, this has to be the ball's path. A streak spanning many frames suggests slow rolling motion along the floor rather than a single bounce, with darker shading marking later positions—so I'm trying to figure out whether the ball rolled back from the bucket's rim toward lower x, or whether it landed short and is rolling toward the bucket.

If the ball clipped the bucket's near rim—say because the actual velocity was slightly lower than planned, shrinking its clearance—it could have hit the outer wall face, dropped near x≈2.6, and rolled backward at a slow residual speed, producing exactly this kind of streak. That's a plausible mechanism: a mostly inelastic collision against the wall, consistent with MuJoCo's contact damping, leaving just enough rebound velocity to roll back toward x≈1.8 over several seconds.

If the shortfall is small, this looks like a near-rim hit rather than a full miss — only about 9% short on range, or roughly 4.5% in speed, which could plausibly come from minor contact losses or the launch angle not being exactly 45°.

Given this uncertainty, I decide the safest fix is to widen the target and add a bit more launch energy for margin. I'm sizing the bucket with an inner radius of 0.45 m (opening spanning roughly x=2.55 to 3.45) and a wall height of 0.40 m, then re-targeting the nominal trajectory to cross near x≈2.95 at z=0.44 to account for expected losses.

Working through the numbers: with Δx=3.268 and Δz=-0.349, I compute the needed velocity-squared, kinetic energy, and required work, landing on a baseline torque around 6.3, then padding it by about 10% for efficiency losses to roughly 6.9.

Factoring in a near-rim hit scenario with about 9% range shortfall, I estimate the actual energy loss at roughly 0.35 J, which pushes the required torque up to about 6.75-6.8. Checking this against the window constraints, I find the trajectory at τ=6.8 would cross near x=3.28 at z=0.44, which is tight but just inside the far wall limit of 3.37 — though I need to verify it clears the rim height properly at that crossing point.

Given the risk of hitting the rim top if there's significant energy loss (observed shortfalls could drop the crossing point to around 2.95, and larger shortfalls would fail regardless), I'm considering raising the bucket walls to catch the ball on the far side. Since a uniform wall height makes the near side harder to clear, I'm checking clearance at the near side first — at x=2.55 the ball has about 0.80m of height versus the wall, giving plenty of margin, so raising the walls to 0.55 still leaves roughly 0.25m of clearance near the launch point at nominal parameters.

Now I'm working out the energy-loss factor f that keeps the trajectory inside this new window: the near wall at x=2.55 requires f > 0.915, while the far wall at x=3.41 requires f to satisfy a separate inequality — solving for the threshold where the ball drops below 0.50m there.

With both constraints combined, f must sit between 0.915 and 1.18, so I'm targeting around 1.04–1.06. Testing a few torque values, τ=6.6 gives lossless f near 1.06, and with roughly 0.35 J of loss factored in, the effective f lands around 0.97, comfortably inside the window — so I'll settle on τ=6.6.

I also want to confirm walls are tall enough to prevent bouncing out, then I'm setting up the bucket's wall geometry: inner radius 0.45, wall thickness, and height spanning 0 to 0.55 centered at 0.275.

Now I'm computing the tangential spacing between wall segments around the circle (16 segments, so each spans about 0.18 of the circumference) and working out their angular positions using cosine/sine at 22.5° and 45° increments to place each panel correctly. The bottom plate sits just above the floor, and since all these pieces belong to the same static body, there's no self-collision concern to worry about. I'll finalize this geometry as the last step before writing the full configuration.

