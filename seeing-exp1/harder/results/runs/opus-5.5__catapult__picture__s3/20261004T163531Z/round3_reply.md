**What this run shows**

The ball still falls short. In the side view the ball leaves the cup early and steeply, peaking around z ≈ 1.4 m only a little past x ≈ −0.3. It comes down near the catapult base at x ≈ 0. It then rolls along the floor and stops against the outside of the bucket's near wall at x ≈ 1.45.

The run looks almost identical to the previous one. So the spring settings, including the radian/degree question, were not the cause, and my last diagnosis was wrong.

**My new diagnosis, which is an inference, not a measurement**

- **Vertical speed is as predicted.** The peak height implies about 2.1 m/s upward at release, which matches what the spring should give.
- **Horizontal speed is far too low.** The ball moves only about 0.7 m/s in x instead of about 3.7 m/s.
- **The missing velocity points outward along the arm.** Turned into the arm's frame, the ball moved outward along the arm at about 1.4 m/s.

That fits the ball escaping outward over the cup's back lip. The back wall rises only 3 cm above the ball's centre. During the swing, centrifugal force presses the ball outward hard (about 18 m/s²), so the ball can climb over that lip and leave at a steep angle with little forward speed.

**The fix**

I made the cup hold the ball properly:
- The back wall now rises well above the top of the ball.
- I added side walls.
- The front, toward the hinge, stays open so the ball can still leave along its intended path when the arm hits its 55° stop.

The ball's start position is unchanged and the cup floor is in the same place. The spring is still k = 2.6, with angles in radians. The bucket centre is still exactly 3 m from the ball's start.

```json
{"what_happens": "The arm springs up, but the ball leaves the cup early on a steep, short arc. It peaks around z≈1.4 m near x≈−0.3, lands near the catapult base and rolls along the floor until it stops against the outside of the bucket's near wall.", "works": false, "problem": "The cup's back wall is only 3 cm above the ball's centre, so centrifugal force lets the ball roll outward over it during the swing, and it leaves steeply with almost no forward speed instead of being flung toward the bucket."}
```

```xml
<mujoco model="catapult_fixture">
  <compiler angle="radian"/>
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="8 8 0.1"/>
    <geom name="catapult_base" type="box" pos="0 0 0.170" size="0.08 0.12 0.170"/>
    <body name="catapult_arm" pos="0 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" limited="true" range="0 0.9599" stiffness="2.6" springref="2.618" damping="0.05" armature="0.01"/>
      <geom name="catapult_beam" type="box" pos="-0.500 0 0" size="0.500 0.03 0.02" mass="0.3"/>
      <geom name="catapult_cup_floor" type="box" pos="-0.920 0 0.025" size="0.08 0.08 0.005" mass="0.02"/>
      <geom name="catapult_cup_back" type="box" pos="-1.005 0 0.115" size="0.005 0.08 0.095" mass="0.01"/>
      <geom name="catapult_cup_left" type="box" pos="-0.920 0.085 0.08" size="0.08 0.005 0.05" mass="0.005"/>
      <geom name="catapult_cup_right" type="box" pos="-0.920 -0.085 0.08" size="0.08 0.005 0.05" mass="0.005"/>
    </body>
    <body name="ball" pos="-0.920 0 0.4895">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.06" mass="0.15" condim="6" friction="0.8 0.01 0.004" solref="0.01 1"/>
    </body>
    <body name="bucket" pos="2.08 0 0">
      <geom name="bucket_base" type="box" pos="0 0 0.01" size="0.4 0.4 0.01"/>
      <geom name="bucket_near" type="box" pos="-0.4 0 0.2" size="0.01 0.4 0.2"/>
      <geom name="bucket_far" type="box" pos="0.4 0 0.2" size="0.01 0.4 0.2"/>
      <geom name="bucket_left" type="box" pos="0 0.4 0.2" size="0.4 0.01 0.2"/>
      <geom name="bucket_right" type="box" pos="0 -0.4 0.2" size="0.4 0.01 0.2"/>
    </body>
  </worldbody>
</mujoco>
```

---
thinking (summarized):

My hypothesis seems wrong since the picture looks the same. I'm re-examining the ball's dot positions in the row 47 region and checking whether that height actually matches z=0.2 rather than the floor level I assumed.

Let me compute the expected trajectory pixel-by-pixel instead: launching from roughly (28,17), the ball should arc through about (43,11), (59,11), (74,17), (90,28), landing near (105,47) at 0.14s intervals. Comparing this against the dots I can make out in the image around (22,15), (32,11), (42,13)... the arc shape seems roughly consistent, so I'm checking whether my predicted curve lines up with what's actually rendered.

Let me double check the ball really sits inside the cup given the geometry — cup floor and ball radius seem consistent with it resting there. Then I reconsider the arm hinge rotation direction, working through the rotation matrix about the y-axis to confirm that a positive rotation actually lifts the -x end upward, which matches what I expected.

Now I'm trying to reconcile the apparent z≈0.2 trajectory with my pixel-row reading, suspecting a small offset from downsampling. Maybe the ball is actually rolling along the floor at constant speed, hits the near wall around x~1.5-1.6, and the remaining frames show the arc near the top-left — I'm trying to split the total 23 copies between a floor-rolling phase (~10 copies, ~1.4s) and an arc phase (~5 copies) to see if the timing adds up to the 3.25s total.

The arc seems to land near x=0, but my predicted launch point can't produce that trajectory unless the velocity is mostly vertical with a small horizontal component matching the roll speed (~1.2). That would happen if the ball separates from the arm/cup early, at a small swing angle where the velocity direction is nearly vertical — so I'm considering whether the ball releases early in the arm's swing rather than at the top, perhaps due to some deceleration or spring behavior in the arm.

Now I'm wondering if the arm itself collides with the base structure as it swings — checking the base box's geometry and how the beam's hinge-end corner moves relative to it as the arm rotates.

Actually, world-parented bodies exclude parent-child collisions anyway, so that's not causing anything odd. I'm reconsidering the joint limit setup at 0-55° — the arm starts at the limit, which seems fine.

Maybe what I'm seeing as a large residual arc isn't the ball at all but the catapult's cup bouncing against its joint limit with spring-like oscillation, tracing repeated copies, while the ball's trajectory is actually the separate line.

So I'm thinking through whether the ball slides off the cup due to friction and centripetal force — as the arm rotates, the ball needs centripetal acceleration toward the hinge, and contact forces from the cup floor plus friction could push it outward along the arm toward the back wall, which sits around x=-1.005 with a certain height range. I'm checking whether the ball's surface could clip through that wall under these dynamics.

At the moment the arm hits its stop at 55°, the ball's velocity direction becomes tangent to its circular path, which I'm computing relative to the arm frame — this tangent points mostly "up" out of the cup with a slight tilt, suggesting the ball should clear the back wall rather than collide with it.

Something's bugging me though — I expected the springref/k changes to noticeably alter the landing point, but the trajectories across my test images look nearly identical. That suggests the ball might not actually be getting launched by the arm's motion at all, so I should check whether the ball's freejoint body is overlapping or improperly coupled to the cup.

Maybe the arm hitting the floor isn't it either. I'm uncertain whether the dots I'm picturing at row 47 actually align with the predicted trajectory points, since they seem evenly spaced in a way that doesn't match. Since I can't fully trust my visual read, I'll treat the row near the bucket as the trail of ball copies approaching the near wall, acknowledging my reading could be off.

Let me reconsider the ball's resting height against the bucket wall — row 47 roughly corresponds to z≈0.2, mid-height of the wall, which fits a ball resting on the floor against it rather than rolling on some other surface. I'm also trying to account for the arm's leftover position, a beam resting near z=0.4 extending toward the bucket, plus another line trailing further up-left.

Looking at the trajectory arc of the ball, the dots suggest a steep descent with low horizontal velocity, meaning the arm swung gently and released the ball slowly — consistent with a launch speed around 1.4-1.5 m/s rather than anything higher, giving a modest kinetic energy at release.

Checking the physics parameters against this: spring energy, damping, armature inertia, and ball contact stiffness all seem reasonable individually, so none of them obviously explains a weak launch. I'm wondering now whether the arm is actually reaching the full 55° stop or getting cut short somewhere along the swing.

I also reconsider whether the fanned lines I'm seeing are motion trails of the arm sweeping slowly rather than something else, with the ball tracing an arc through sequential positions — that would actually be consistent with normal throwing behavior rather than a bug.

But I keep probing for a physical explanation for premature release: maybe the ball isn't just resting on the cup floor but actually rolls toward the hinge as the arm tilts, since gravity would pull it along the inclined cup surface toward the pivot rather than outward, which could explain an earlier-than-expected separation.

So that outward force dominates, meaning no inward roll makes sense physically. I'm stuck pinpointing why the row 47 dots appear as they do — maybe it's unrelated to the ball's position and instead reflects something else evenly spaced across the frame, so I should reconsider whether the ball actually landed in the bucket and this row is tracking a different element entirely.

The fact that the ball's trajectory barely shifts across k=2.0 to 2.6 and the degree-to-radian correction suggests the outcome is insensitive to spring parameters, which points to the ball not really being thrown by the arm's spring dynamics at all — maybe the arm moves with enough force in all cases to fling the ball regardless, or maybe something about how springref was configured in run 1 differs from the others.

If run 2 (degrees) and run 3 (radians) look identical, that confirms springref is being converted properly, which means the real issue lies elsewhere — perhaps the joint limit at 55 degrees is capping the arm's motion prematurely, causing the ball to launch with weak velocity every time.

Actually, I wonder if the arm is colliding with the catapult base itself. MuJoCo's parent-child contact filter typically excludes collisions between a body and its parent, but I recall that this exclusion doesn't apply when the parent is the world body — meaning the arm could be contacting the base box as it rotates, even though there's initially a small gap between them.

I'm double-checking the spring torque sign and joint limit behavior — the formula looks correct and the soft limit penetration is negligible. So the arm should release the ball around 55° with roughly 4.2 m/s at a 29° angle as predicted, yet this seems to contradict what I'm seeing, which means I must be missing something else.

Let me reconsider the plan view image more carefully — maybe the ball actually does land in the bucket. The evenly-spaced copies in the plan view suggest constant velocity, but comparing the predicted spacing from flight versus rolling against the observed 6-8 px spacing doesn't quite match either scenario, so I need to recheck my velocity assumptions.

The side view dots look level, meaning height isn't changing, so the ball is likely rolling or sliding along the floor at roughly 1.9 m/s rather than flying. It seems to travel short of the bucket, hit the near wall, and stop there, placing it adjacent to the bucket in the plan view. I'm still trying to figure out why my calculations keep being off — maybe the ball gets released early due to the arm decelerating before full extension.

The ball sitting on the cup should be fine, since at release at 55° the velocity is mostly upward with a slight inward component. But I'm now checking whether the ball could roll outward along the arm during the swing, against the back wall — comparing centrifugal force to gravity's component along the arm, outward force dominates early on, which should push the ball against the back wall rather than off the front, so that seems consistent with staying in the cup.

Wait, I need to reconsider the joint's "limited" attribute — in MuJoCo, if "limited" isn't explicitly set and autolimits isn't enabled, the range I specified might be ignored entirely, letting the arm swing far past 55° toward 150° or more. That would mean the ball stays pinned by centrifugal force well beyond where I assumed release happens, and separates only once the arm's rotation carries the cup over the top and deceleration lets go of it.

At θ=90° with the arm vertical, the tangent direction works out nearly horizontal pointing right, which would give high vx — though I'm not fully certain of this. I'm uncertain whether autolimits is default true in this MuJoCo version, but adding limited="true" explicitly shouldn't hurt either way. I'm also reconsidering whether the ball actually releases early because the cup is too shallow, causing it to hop right at the initial acceleration spike, or whether the arm simply stops at a joint limit before my kinetic estimate accounted for.

Now I'm cross-checking the observed ball positions in the image against computed trajectory math — trying to see if a launch from roughly (-0.454, 1.205) with vz≈2.07 produces an apex height and x-position that matches the dots plotted around pixel coordinates (24,15), (33,10), (41,13), and it seems to line up reasonably well with an apex near z=1.42 and x≈0.32.

But comparing the predicted apex x against the observed one reveals a mismatch: the vertical velocity component matches almost perfectly, but the horizontal velocity seems much smaller than expected (around 0.8 m/s instead of 3.67 m/s). I'm trying to figure out why the ball would lose most of its horizontal speed — possibly something about how the cup's tilt and normal force direction constrain the horizontal push during launch.

I'm rechecking my sign conventions for the cross product ω×r, verifying against the known upward direction at θ=0, which seems consistent, but the required elevation angle still doesn't match up with a plausible release height, so I'm trying other θ values to reconcile the geometry.

Recomputing the apex x-position with this release angle gives -0.32, which actually matches the observed apex pixel data well, confirming θ≈15° and speed ~4 m/s. That's puzzling though — it implies the arm reaches ω≈4.3 rad/s already at just 15°, which seems too fast given the spring stiffness I used, so I'm checking whether that's physically consistent with the torque equations.

But maybe the release isn't driven by angular velocity threshold at all — maybe the arm physically collides with something around 15° and stops abruptly, launching the ball then. I'm wondering if this could be the catapult base itself, and recalling MuJoCo's contact filtering rules about parent-child body collisions being excluded by default (except involving the world body) — this could explain why the arm doesn't collide with its own base until a specific point.

Now I'm working through the geometry: tracking how the beam's corner points transform under rotation to see if the beam's bottom edge intersects the base at some rotation angle.

I'm checking whether something physically stops the arm at 15° rather than the expected 55°, considering the soft-limit and back wall interaction. Maybe the arm decelerates abruptly at the joint limit, but the ball in the cup keeps moving due to its own momentum and separates early rather than at the full swing angle.

I'm stuck trying to pin down the mechanism — possibly my x-velocity estimate assumes the ball slides freely, when really the cup floor exerts a normal force while friction provides centripetal constraint toward the hinge, which would change the release dynamics.

Maybe I should sidestep the uncertainty entirely by keyframing the launch velocity directly rather than deriving it from spring/arm physics, though convention expects the ball to start at rest and actually be thrown. A deeper cup with side walls could also help contain the ball until the arm stops, though without y-forces there's no reason it'd slip sideways anyway.

I'm double-checking the hinge axis placement, joint defaults, and whether the arm or ball might collide with the catapult base somewhere I overlooked.

Based on observed results, the ball landed near x~0 and rolled to about 1.44, so the trajectory isn't matching my expectations. Rather than redesigning the catapult entirely, I'm leaning toward trusting the spring-arm physics and reconsidering the joint limit's soft stop parameters and timing instead.

Let me trace the frame intervals more carefully: with residue showing every 0.14s and the ball leaving within the first 0.3s, I'm calculating the arm's angular position at each captured frame to figure out exactly where the ball is relative to the arm as it swings toward release.

Working through the predicted pixel positions at each timestep, I keep getting coordinates that are roughly 18 pixels apart, but I'm not confident I'm reading the actual dots in the image correctly against these predictions - the match isn't clean. If my trajectory calculation is right, the copies at later rows shouldn't exist at all, which means something is off between my physics model and what's actually shown.

I'm noticing a persistent row of markers spanning a wide pixel range that appears consistently across all the image views, which doesn't fit any simple constant-height flight explanation. I start questioning whether there's a structural collision issue - checking whether the ball's initial position overlaps with the beam or cup floor geometry, verifying the heights and positions don't conflict. Finding that the ball sits just above the cup floor, which seems fine, so I'm now considering whether the arm position itself is the source of the discrepancy and resolving to try a more robust approach using spring dynamics.

I'm now wondering if the cup might have an unintended front lip blocking proper launch, or whether the arm hitting its limit causes a rebound effect. I'm also considering the possibility that the ball slides inward along the cup floor toward the hinge due to gravity's component along the arm versus centrifugal force, which could explain premature or low-angle release - weighing how tangential effects factor into this sliding motion.

Given how many subtle contact issues keep arising, I'm starting to think this cup-and-arm catapult design has too many fragile dependencies, and maybe I should consider a fundamentally different launch mechanism altogether, like a spring-loaded plunger.

I should double-check the solver timing parameters for the ball's contact solref against the timestep, but those seem fine. The real puzzle is why the actual simulated trajectory ends up with far less energy than predicted — something is dissipating kinetic energy or releasing the ball early, possibly through an unintended collision with the arm's beam geometry or a hinge limit being triggered prematurely.

Checking the picture against my reconstruction, the ball seems to land right in front of the catapult base rather than far off, suggesting a short horizontal travel. I'm wondering if the arm could actually catch up and re-strike the ball mid-flight if released too early relative to the arm's continued rotation — that would require a sharp drop in torque that I can't easily justify with the current spring parameters.

Maybe the issue isn't with release timing but with how I'm modeling contact: perhaps the ball separates from a back wall rather than the floor, or the joint limit at 55° isn't actually enforced the way I assumed, letting the arm swing further than expected.

Checking that position, that exit velocity would send the ball rightward and down, but the residue lines in the image only appear on the left side, so the limit is indeed active. Since I can't fully diagnose the discrepancy, maybe the real issue is that the ball separates too early with insufficient horizontal velocity across all three runs — I should reconsider the back wall geometry, since cup_back spans roughly x -1.01 to -1.0.

I recompute the gravity torque at the start: beam contributes about 1.47, cup components add roughly 0.28, ball adds about 1.35, totaling around 3.1 against a spring torque of 6.8, which still seems fine. I'm now considering whether the contact solver parameters between ball and cup floor — differing solref values — could be causing an unexpected mixing effect.

Checking the condim=6 friction settings (torsional 0.01, rolling 0.004), those look reasonable too. Working back from the apex position in the observed trajectory, I estimate the launch velocity components: vz around 2.15, vx around 0.7, giving a speed of about 2.26 at roughly 72° elevation — much steeper than the 29° I'd expect from a 55° release angle, which is the discrepancy I need to explain.

Comparing this 72° direction to the arm's geometry at release, the ball's motion seems to combine both the cup's normal direction and some outward slide along the arm — suggesting centrifugal sliding during release rather than a clean launch along the normal. That outward slide could mean the ball briefly lifts off the cup floor, which would let the back wall contact a higher point on the ball and potentially let it roll over the wall instead of launching cleanly.

The 43° discrepancy between the 72° and 29° elevation results looks like it matches an outward radial velocity component comparable to the tangential speed, which would happen if the ball slid outward before being caught by the back wall. Since the ball does collide with the wall geom, I'm starting to think the real fix might just be redesigning the cup geometry—using a back wall taller than the ball itself, fully enclosing it, paired with a small front lip.

But I'm reconsidering whether the escape is real: as the spring torque weakens near the end, tangential deceleration kicks in while centrifugal force still pushes outward, which could reduce the floor contact pressure just as the ball needs to be held. The back wall contact should still occur at the ball's equator since the wall's inner face stays vertical in the arm frame and the ball's center sits below the wall's top edge, so geometrically there shouldn't be an escape path there. Still, I'm now considering the deceleration itself—arm going from ω 4.5 to 0 over about 0.02s gives roughly -225 rad/s², and wondering how that impulsive stop interacts with the cup wall at the moment of impact.

Once the arm stops, there's no more centrifugal push so the back wall contact force drops to zero and the ball just travels straight. I'm stuck trying to resolve this theoretically though — empirically the vertical speed matches my prediction almost exactly (2.07 vs 2.15) but the horizontal speed came out way lower than expected (0.7 vs 3.67), which is strange since the vertical match seems too precise to be coincidence. Something must be killing the horizontal component specifically.

Maybe it's the cup's back wall at release — I'm working out the arm's local coordinate axes in world frame and projecting the ball's velocity onto them to see if the wall geometry explains why only the horizontal motion got suppressed.

Checking the math, the ball moves mostly upward out of the cup with just a slight shift toward the hinge, so nothing in the collision geometry should be blocking it — physics says this motion should work fine. That makes me doubt my reading of the image; maybe I'm misinterpreting which band of pixels corresponds to which part of the trajectory, so I should reconsider what that row of repeated shapes near the top actually represents.

Let me reconsider: maybe the ball only interacts with the cup's floor frictionlessly, and transforming the final velocity into the arm's local frame shows the ball actually moving outward along the arm axis at 1.36 m/s — meaning it escapes over the back wall rather than launching forward.

I wonder if hitting the limit stop causes a sharp rebound instead—the arm snapping back with negative ω, pulling the cup floor away and reversing the back wall's motion relative to the ball, which could be what actually launches it outward rather than steady centrifugal pressure.

Alternatively, maybe the ball never reached full angular velocity—if observed speed is only 2.26 m/s, that implies ω closer to 2.4, with an outward component I hadn't accounted for. I should also double check my hinge direction assumption—maybe I have the rotation sign flipped, or the arm doesn't stop exactly at 55° but at some other final position I need to recompute.

I'll focus instead on making the design more robust: a deeper cup with a tall back wall (higher than the ball's top) and side walls to prevent any escape over the lip, letting the spring hold the ball in place until release at the stop. This way, even if my exact cause analysis is off, the physical fix should still contain the ball properly.

The contact normal there is purely horizontal, so there shouldn't be any climbing effect at that point. Though I'm not fully convinced this resolves things—there's also a possibility that the arm's joint limit itself is soft and oscillating after it hits the stop, springing back and forth while the ball is already gone, which could be a separate source of the problem. Let me instead think about when the ball actually separates from the floor: it separates when the required normal force for its tangential acceleration would have to go negative, so I should work out N/m as a function of angular acceleration, radius, and the gravity component along the normal direction.

Checking this, the term stays positive as long as angular acceleration is positive, so that's not it either. Small overlap with the stiff contact solver could cause a small pop but that seems too minor to explain things. Given that vertical speed matched prediction but horizontal didn't, something reduced the ball's horizontal velocity by about 3 m/s—likely friction acting along the outward local direction of the arm, which would reduce vx while slightly boosting vz, matching what I'm seeing. That points toward friction causing an outward slide as the real culprit.

I'm now fairly convinced the ball actually escaped outward over the short back wall—since the wall only extends 0.03 above the ball's center, the ball could climb over it once spin from floor friction causes it to rise slightly while the arm rotates, especially against centrifugal acceleration of 18 m/s². The fix is simply to make the back wall taller so the ball can't climb over it.

Adding side walls and skipping a front lip since it would block the release direction...

