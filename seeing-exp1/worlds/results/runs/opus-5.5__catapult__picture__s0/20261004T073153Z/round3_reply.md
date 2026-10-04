## What the picture shows

The third run looks almost the same as the first two.

- **Catapult:** The arm swings up and throws the ball forward. The visible ball copies follow a low, flat path, roughly through x ≈ 0.3 m, z ≈ 0.9 m and x ≈ 1.4 m, z ≈ 0.65 m.
- **Where the ball ends:** It ends on the floor short of the bucket. Its copies trail from about x ≈ 1.8 m up to the outer face of the near wall at x ≈ 2.5 m. No copy is inside the bucket.

## What the result tells me

The damped drive (a fixed arm speed instead of a fixed torque) and the earlier torque changes did not change the outcome. So the shortfall is probably not the arm speed. It looks like the hand-off between the cup and the ball.

From those few low-resolution copies, the ball seems to leave about 15° flatter than the arm's 45° stop implies, and noticeably slower.

My best guess at why:
- Just after release the ball drifts slightly inward along the arm. The inner lip sits only 5 mm away, so the ball rubs or catches on it.
- With friction coefficient 1 and the ball spinning with the arm, that contact drags and deflects it as it leaves.

## The change

The hand-off is now cleaner:
- The inner lip is removed. Centrifugal force keeps the ball pressed against the outer lip for the whole swing.
- The ball–arm contact is frictionless (condim 1), so the ball does not pick up spin and nothing drags on it at release. Contacts with the floor and bucket still have friction.
- The 45° stop is stiffer, so release happens right at the stop.

The damped drive stays, so the arm still reaches the 45° stop at a fixed speed of about 10.9 rad/s, which flings the ball at roughly 5.5 m/s and about 39°. I have not run this version. I only checked by hand that this path clears the near rim of the 0.9 m-wide, 0.55 m-tall bucket.

```json
{"what_happens": "The arm swings and throws the ball, but the ball leaves on a low, flat path, falls short, and ends on the floor rolling up against the outside of the bucket's near wall around x = 1.8-2.5 m; it never gets into the bucket.", "works": false, "problem": "The ball leaves the cup flatter and slower than the arm's 45-degree stop implies, apparently because the inner lip and friction catch it at release, so it falls short of the bucket."}
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

      <!-- throwing arm: hinge about y, damped so it reaches a fixed terminal speed before the stiff 45 deg stop -->
      <body name="catapult_arm" pos="0 0 0.4">
        <joint name="catapult_hinge" type="hinge" axis="0 1 0" limited="true" range="0 45" solreflimit="0.005 1" damping="4"/>
        <geom name="catapult_hub" type="cylinder" fromto="0 -0.03 0 0 0.03 0" size="0.02" mass="0.02" contype="2" conaffinity="2" condim="1" rgba="0.3 0.3 0.3 1"/>
        <geom name="catapult_beam" type="box" size="0.3 0.03 0.01" pos="-0.28 0 0" mass="0.3" contype="2" conaffinity="2" condim="1" rgba="0.6 0.45 0.25 1"/>
        <geom name="catapult_lip_outer" type="box" size="0.015 0.03 0.03" pos="-0.555 0 0.04" mass="0.02" contype="2" conaffinity="2" condim="1" rgba="0.6 0.45 0.25 1"/>
      </body>
    </body>

    <!-- ball resting on the arm against the outer lip -->
    <body name="ball" pos="-0.5 0 0.45">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" contype="1" conaffinity="3" condim="1" rgba="0.9 0.2 0.2 1"/>
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

I'm comparing the dot positions against the previous image and they're still landing in nearly the same spot, just slightly further out, with the trajectory again ending on the floor near the wall outside the bucket. Three runs in a row giving essentially the same result.

Testing the parabola math against the two dot points, I notice the actual path is flatter than a 45° launch would produce. Working backward with a 0.26s interval between dots gives a horizontal velocity around 4.27 m/s, which matches a 39° launch angle at speed 5.5 — consistent with what I found before — and solving for vertical velocity at the first dot gives roughly 0.23 m/s.

But the numbers don't reconcile cleanly: tracing back from launch, the apex height would exceed the top band and the ball should be clipped from view there, yet also the implied release point doesn't match where I'd expect based on x displacement. So I suspect I'm misreading something — maybe those "dots" aren't actually the ball in flight but something else, like arm copies, since I can't trust the flight trajectory as I've reconstructed it. What stays consistent across all three runs is the ball's resting position on the floor to the left of the bucket, which is suspicious given the different torques and designs — I'm now wondering if the floor itself, rendered edge-on as a line in this side view, is something I've misread.

I'm matching that gray rectangle to the catapult base's footprint in plan view, which checks out positionally. Then I trace the ball's flight copies across the plan—spotting a dot near x≈1.2 and a streak around x 1.75-2.5, and reasoning about the spacing between flight copies (roughly every 1.1m given the horizontal velocity) to figure out whether the next copy lands mid-flight, on the floor, or inside the bucket where it'd appear as a dark dot seen from above.

I'm now second-guessing whether that streak actually represents the ball on the floor at all, or if it's something else—maybe part of the bucket's rendering—since the geometry doesn't quite line up with the bucket's expected footprint or the ball rolling inside it.

Trying a different trajectory calculation at x=2.54 with f=1.04 gives a height around 0.90 m, clearing the bucket wall by a comfortable 0.35 m. That means if the ball really is hitting the near wall, the actual launch performance must be significantly worse than what my model predicts, even accounting for damping—so maybe the release angle isn't actually 45° like I assumed.

I'm wondering if the ball separates from the arm surface early rather than staying in contact through full travel. With acceleration starting around 630 rad/s² and decreasing sharply as the arm nears terminal velocity, the ball could decompress and spring off the surface ahead of the arm, launching at a much steeper angle—maybe 65°+ instead of 45°—and at a lower effective speed. That steep, shorter trajectory would make much more sense of the ball falling short and hitting the bucket wall.

Since the arm keeps a constant angular speed while gravity slows the ball's normal motion, the arm actually catches up to the ball rather than separating from it, so the ball just rides along with small bounces. Trying to trace the trajectory more carefully, the streak's end position at roughly x=2.52 lines up almost exactly with the outer face of the near wall, suggesting the ball ends up resting against that wall rather than flying past it.

Without rolling friction in MuJoCo, that resting position means the ball rolled toward the wall and stopped there inelastically, with the earlier copies in the streak showing a slow roll of only about 0.15–0.3 m/s over roughly 0.7 m. That slow rolling speed implies the ball landed with very little horizontal velocity around x≈1.8, which points to a steep, near-vertical lob — launched high enough to leave the frame, with a small vx near 1.2 m/s, before coming down and rolling gently into the wall.

Working through this geometrically: if separation happens at a small arm angle, the launch direction is close to vertical. For a velocity of about 5.5 m/s at a 75° angle, that gives vx≈1.4, vz≈5.3, flight time around 1.2s, and a horizontal travel of roughly 1.7m — landing somewhere around 1.2–1.5m, which roughly fits. I'm now considering why separation would happen early, thinking it's tied to the spring-back of the soft contact model when the arm's angular acceleration drops off, and comparing this to the constant-torque runs where the arm's acceleration behaves differently at the start.

I'm also questioning whether the ball might ride up over the outer lip due to centrifugal force, but since the lip's contact point sits near the ball's equator rather than below it, there's no real climbing geometry — the contact normal stays essentially horizontal as long as the ball touches the box face.

During the high initial angular acceleration, inertial and gravitational forces press the ball firmly into the surface with significant penetration, so no separation occurs yet. Once the acceleration drops off, that compressed contact releases suddenly, popping the ball off with some extra relative velocity, after which it travels in a straight line while the arm continues rotating underneath it, causing their paths to diverge.

Since the ball moves tangentially, its radial distance from the pivot grows over time, letting it rise relative to the arm's surface and climb past the containing lip, escaping outward. But because the arm's angular rate stays constant while the ball's angular rate about the pivot decreases as it moves outward, the arm can catch up and strike the ball again — suggesting this isn't a single clean release but potentially a messy series of repeated kicks.

The real fix might be shape: a flat paddle with soft contact can't cradle a ball properly, unlike a classic catapult cup with walls holding the ball until release. A deep cup lets the ball escape only along its normal direction, but rotation complicates things since the cup's outer wall moves as the ball drifts outward and upward — making the escape geometry tricky to pin down cleanly.

But checking whether gentle, constant-torque drive avoids early separation: with acceleration around 75 rad/s², contact forces stay modest and penetration is tiny (under a millimeter), so critical damping should prevent the ball from popping off prematurely. Yet those runs failed identically to the others, which suggests the early-separation issue isn't really about drive smoothness or initial transients at all.

I start wondering what could cause the same steep, short trajectory across all three runs regardless of drive type. Maybe release is happening at a small angle every time, and I wonder if the joint's lower limit at zero is somehow staying active or getting misread—like the limit being interpreted in the wrong units, which could force an early release point independent of how the arm is driven.

With damping at constant angular velocity, the ball would separate once gravity's normal component overcomes the centrifugal hold, likely past vertical, meaning the launch direction wouldn't match a clean forward trajectory—so I'm trying to pin down the actual arm angle from the sparse pixel data, but it's too ambiguous to confirm. I'm also double-checking that `limited="true"` combined with a range attribute on a hinge joint is valid syntax.

Since results keep coming out identical regardless of drive parameters, maybe separation happens at a consistent geometric condition rather than depending on dynamics—so I'm setting up the rigid-body analysis properly in the rotating arm frame, accounting for centripetal and tangential accelerations, the paddle's normal force, and the lip's inward-pushing force, all balanced against gravity.

The tangential equation shows normal force stays positive for reasonable angles, which suggests release should occur at 45° in the rigid-body case—so all three runs should launch at that consistent 39° angle regardless of drive speed. I wonder if instead the issue is that the ball geometrically overlaps the beam at the start, since the ball's bottom sits just below the beam's top surface by a small margin.

Checking the contact filtering rules between the ball and arm confirms contact should actually register, since the arm's contype and the ball's conaffinity overlap nonzero. So I'm now considering whether the ball might instead fall through and land on the base box if that contact somehow fails.

I'm trying to cross-check the observed dots against the predicted 39° trajectory: computing the parabola's z-value at x=0.34 gives roughly 1.21, but the image shows 0.91, which doesn't match. I'm now attempting to fit a parabola through three observed points to see if a different trajectory fits better.

Working through the curvature, I get vx≈4.04 and a launch slope near 25° rather than 39°. Checking a second run's dots confirms a similar pattern, suggesting the actual launch angle is around 25° with speed roughly 4.5, flatter than my original plan.

Actually, relating this back to release angle: the tangent direction implies θ_r ≈ 59°, meaning the ball releases well past the 45° joint limit — the arm must overshoot to ~60° before letting go, with the joint's soft limit stopping it over roughly 0.05s given the stiffness and damping parameters in the constraint model.

Checking whether the ball actually clears the lip edge as the arm overshoots — tracking the ball's position against the lip top during the 6ms deceleration window, it seems to mostly clear except for a brief overlap at the start, with no sign of deflection toward positive x.

For a flatter launch angle, I need an inward radial velocity component added to the 45° direction, which would push the trajectory downward. That inward push likely comes from the outer lip itself acting like a compressed spring — as the arm decelerates, the lip's stored elastic energy from centrifugal loading (around 6N in run 3) releases and shoves the ball inward just before separation.

But checking magnitudes, that soft-contact release with only ~1mm penetration wouldn't produce anywhere near the needed velocity difference, which is mostly vertical (about 1.6 m/s downward) rather than purely radial — so I'm reconsidering whether it's actually lip contact at all, or whether spin-induced friction against the lip is responsible instead, since the ball's rotation would create a tangential force at the contact point.

I realize the ball actually moves outward as it travels along the tangent line, since its distance from the pivot grows with displacement—so instead of separating cleanly from the lip, the ball's edge penetrates past the lip's fixed radius of 0.54, creating a large inward normal force plus friction opposing the motion.

So the lip acts like a radial stop: the ball must clear the lip's top corner at radius 0.54, height 0.07, meaning the ball center needs to rise enough that its distance from that corner exceeds the ball's radius of 0.04 before it's truly free.

Thinking more carefully, in the arm's frame the ball's tangent-line velocity isn't purely along the normal to the arm — since the ball center sits at r=0.5 along the arm but offset 0.05 up, the true tangent direction is perpendicular to that offset vector, giving a motion that's mostly in the h-direction with a small radial component.

Using v=ω×r in arm coordinates, I find the ball actually moves slightly inward (toward the pivot) as it moves outward in h, at roughly a 10% ratio — so it's drifting away from the lip edge rather than wedging against it. That seems fine for clearing the outer lip, so now I need to check whether that slight inward drift could instead cause trouble with the inner lip surface.

Working through the geometry, there's only a 5mm gap at the inner lip, and the ball's inward velocity combined with its upward rise means it reaches the inner lip position while still below the lip's top height — so the ball would actually strike the top corner of the inner lip. That collision would deflect the ball further outward and upward rather than flattening its trajectory, which isn't the correction I was hoping for.

Actually rechecking positions, the ball center starts below the corner height, so it initially contacts the lip's side face rather than the corner, with the normal pointing inward (+u). That means the impulse mainly kills the small inward velocity, and with friction capped at μ times that impulse, the upward speed only drops by a tiny amount—not enough to explain a large effect unless contact persists longer.

Also factoring in the ball's own spin at the inner contact point: since the ball rotates rigidly with the arm, the contact surface there moves downward along the normal relative to center, so it's sliding upward against the lip. With kinetic friction μ=1, the normal impulse from the 0.55 inward velocity bounds the friction impulse to about 0.055 N·s, limiting how much the lip can change the ball's velocity.

I'm struggling to reconcile these numbers cleanly — the outcomes keep converging near a 25° launch angle and roughly 4.5 m/s regardless of how I vary the drive parameters. Rather than keep chasing this contact-mechanics rabbit hole, I think the more practical fix is to simplify the cup geometry itself: drop the inner lip entirely and use a flat paddle-like holder with only an outer lip, so release behavior becomes more predictable and decoupled from these messy friction effects.

Maybe the ball sticks with the arm past the 45° limit due to soft contact, releasing later at a higher angle and lower speed—exactly the flatter, slower signature I'm seeing. That would mean the arm overshoots by roughly 14° while decelerating gradually rather than stopping abruptly, which could trace back to how the joint limit's soft constraint and damping interact in the simulation.

Checking whether the ball gets wedged between the lips rules that out given the gap is larger than the ball diameter. Since I can't fully resolve this analytically, I'll try some structural changes instead: removing the inner lip to avoid corner collisions, stiffening the limit with tighter solreflimit/solimplimit values, and reconsidering friction between the ball and arm surface.

I'm also thinking about setting condim="1" on the ball and arm geoms so contacts become frictionless, since rigid rotation barely needs friction and this could eliminate drag at release caused by the spinning ball sliding along the lip.

I'm second-guessing the "flatter" image reading, and wondering if the bucket walls are actually blocking the ball trajectory despite the computed 0.35m clearance. I'm leaning toward a structural fix: remove the inner lip, make the arm contacts frictionless, stiffen the limit, and keep deterministic damping drive. I'm also revisiting run 3's huge initial acceleration (630 rad/s²), which pressed the ball hard enough to cause about 6mm of arm penetration.

The ball likely pops off the surface at roughly 0.5 m/s relative velocity once the compression releases, flying ahead while the arm rotates and eventually catches back up — since there's no tangential friction, only the normal contact and lip matter. I'm trying to work out how the ball's angular position relative to the pivot evolves as it moves straight while the arm keeps constant angular velocity.

I then test reducing the damping parameter to see if it smooths the initial transient, reworking the time constant and torque equations to find when the arm reaches 45° — but this makes the release angular velocity less deterministic, so I decide to keep the original damping value of 4 rather than switch to 2 or 3. I'm also planning to check what happens if the inner lip is removed from the design.

So the ball gets pushed outward against the outer lip immediately—I should remove the inner lip since it was only risking a collision at release, and with a frictionless surface there's no spin to worry about. I'll tighten solreflimit to "0.005 1" since that's compatible with the timestep, keep the outer lip height as is, and confirm the contact conditions (ball condim 1, floor and bucket condim 3) are fine. I'll write it out now while being honest about the remaining uncertainty.

