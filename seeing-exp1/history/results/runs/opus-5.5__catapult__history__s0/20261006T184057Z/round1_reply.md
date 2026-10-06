The ball flies about two metres, lands short of the bucket, bounces into the bucket's near wall and comes to rest outside it.

**What happens in the run.** The spring swings the arm up. The ball rides in the cup until the arm hits its 55° stop at 0.53 s, moving about 3.3 rad/s. The ball leaves at about 2.8 m/s and only about 22° above horizontal. It peaks at 1.28 m at x = −0.17 m and first hits the floor at about x = 1.14 m. It bounces twice, strikes the outside of `bucket_near` at x ≈ 1.6 m, and settles at x ≈ 1.47 m. That is outside the bucket, whose centre is at x = 2.0 m.

**Why.** The launch is too weak and too flat. The ball needs to clear the near wall (top at 0.4 m) and come down near the bucket centre about 2.7 m downrange of the release point.

**Fix.**
- **Stop angle:** I moved the arm's upper stop from 55° to 45°. The ball then leaves about 39° above horizontal before release losses, which come out near the best angle for this drop height. The landing point then barely changes if the true release angle varies by a few degrees.
- **Spring stiffness:** I raised it from 2.0 to 3.2 N·m/rad. That should give an arm speed of about 4.9 rad/s at the stop and a release speed of about 4.25 m/s. I estimated this from the observed run, scaling for the ~9% damping and ~6% release losses seen there; I have not run it.
- **Bucket position:** I moved the bucket to x = 2.08 so its centre is exactly 3.0 m from the ball's start at x = −0.92.

**Predicted flight, not yet confirmed by a run.** Release at about (−0.59, 1.11) m. The ball should pass over the near wall at about z = 0.6–0.7 m and come down near x = 2.08 m. For launch angles between 32° and 40° the computed landing point stays at x ≈ 2.06–2.08 m.

```json
{"what_happens": "The spring flings the arm to its 55° stop at 0.53 s; the ball leaves at about 2.8 m/s on a flat ~22° trajectory, peaks at 1.28 m, lands on the floor at x≈1.14 m, bounces into the outside of the bucket's near wall at x≈1.6 m, and comes to rest at x≈1.47 m, short of and outside the bucket (centre x=2.0).", "works": false, "problem": "The launch is too weak and too flat, so the ball falls about 0.9 m short and never enters the bucket."}
```

```xml
<mujoco model="catapult_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="8 8 0.1"/>
    <geom name="catapult_base" type="box" pos="0 0 0.170" size="0.08 0.12 0.170"/>
    <body name="catapult_arm" pos="0 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 45" stiffness="3.2" springref="150" damping="0.05" armature="0.01"/>
      <geom name="catapult_beam" type="box" pos="-0.500 0 0" size="0.500 0.03 0.02" mass="0.3"/>
      <geom name="catapult_cup_floor" type="box" pos="-0.920 0 0.025" size="0.08 0.08 0.005" mass="0.02"/>
      <geom name="catapult_cup_back" type="box" pos="-1.005 0 0.07" size="0.005 0.08 0.05" mass="0.01"/>
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

I'm checking the trajectory math and realizing the ball falls short of the bucket and bounces off instead of landing in it, so I need to adjust the launch velocity and timing to get the distance and arc right.

The fix is to increase launch speed and set the bucket at exactly 3 m away (around x=2.08), then re-estimate the release point and velocity more carefully—roughly position (-0.47, 1.22) with velocity around (2.63, 1.08), giving a speed near 2.84, which I need to verify clears the near wall and lands inside the bucket.

Working through the geometry, the release velocity direction at 55° comes out to about 35° above horizontal, giving components near (2.48, 1.74), roughly matching the 0.50s data point. But comparing with the observed apex (height 1.28 at t=0.64s), the effective launch seems closer to (2.63, 1.08) from position (-0.47, 1.22), putting the angle around 22° rather than 35°.

I'm solving for a scale factor k on this launch velocity so the ball lands at the bucket (x≈2.08, z≈0.08). Setting up the time-of-flight and vertical drop equations, I get t≈0.668s and k≈1.452. Now I need to check whether this trajectory clears the wall obstacle at x=1.68, height 0.46, by checking the ball's height at that x position.

Checking the wall clearance: at t=0.563s, z comes out to about 0.548m, which is 0.09m above the 0.46m wall—enough margin, and the far wall at 2.48 looks fine too.

But I realize scaling the launch velocity by 1.45 isn't simply linear in the spring parameters, since the release kinetics change—I need to work out the actual spring torque and energy to get the real speed at release.

Now I'm computing the spring work done from 0 to 0.96 radians, the gravitational potential energy lift for the beam, cup, and ball components, and subtracting to find the net kinetic energy available, which comes to about 1.56 J, then starting on the beam's moment of inertia.

I'm reconsidering the release geometry: at 55° arm angle, the tangential velocity direction (perpendicular to the arm) is roughly (0.819, 0.574), and the cup's floor normal aligns with this same perpendicular direction since the plate lies along the arm — so I need to check whether the ball separates cleanly along that normal or gets deflected by the back wall as the arm decelerates past 55°.

Since the measured vz (0.53) is lower than the apex value (0.64), I suspect friction during that last 0.03s of contact with the cup back is shaving off some vertical velocity, so rather than modeling that precisely, it's probably simpler to just use the empirical ratio from the measured ω at stop (3.28) and scale the tangential velocity at radius 0.924 from there.

Working out the wall's orientation after the 55° rotation, its normal points inward toward the pivot at roughly (0.574, -0.819). So when the arm decelerates abruptly at the stop and overshoots to 56.3° then snaps back toward -17°, that sudden motion could be what imparts the extra impulse to the ball through contact with the back wall.

I'm also considering whether the velocity change actually comes from the cup floor's friction rather than the back wall alone, and wondering if removing the back wall entirely would let the ball slide outward instead of being held by centripetal force. Without running the simulation, I think it's best to just empirically tune the power rather than fully resolve this mechanically.

A more robust fix would be adjusting the stop angle toward 45° for a higher arc with more landing tolerance—I'm recalculating the ball's release position for this case, rotating its offset from the pivot and getting a release point around (-0.588, 0.714) relative to the pivot.

Solving for the required launch speed gives u≈3.07, meaning linear speed ~4.34 m/s and ω≈4.70 rad/s to hit the target landing spot. Checking clearance at the near wall position, the ball's height there comes out to about 0.70, which looks like enough clearance to confirm this trajectory works.

I'm a bit worried about sensitivity though—the range is fairly touchy with respect to launch speed, so a ±0.3 m tolerance implies only about ±6% speed margin, and the earlier perturbation where vz dropped unexpectedly is concerning. That overshoot likely came from the arm hitting its joint limit and bouncing back while still in contact with the ball, so I should consider whether the stop needs to be stiffer or the solref tuned differently.

Thinking about the geometry: at the moment of the stop, the centripetal force would have been pressing the ball into the back wall of the cup, pushing it inward toward the pivot. If the contact there is soft, penetration energy stored during the stop could release as an extra inward velocity kick once the arm decelerates, which would explain the vz drop.

This magnitude roughly matches what I'd expect, though friction likely plays a role too. The kick scales with ω², so a faster swing makes it worse, and removing it cleanly is tricky since it's tied to centripetal compression against the back wall. Maybe it's simpler to just let the ball rest only on the cup floor without a back wall acting during the launch.

Though without a back wall the ball would just roll off the end rather than getting the centripetal push — unless I angle the floor itself so its normal has an inward component, effectively substituting for the wall. Another path is to just accept the measured deviation empirically rather than chase full physical realism, treating the effective release angle and speed as reduced from the nominal values.

Let me check the existing catapult trajectory directly: release at (-0.47,1.22) with velocity (2.63,1.08), apex at (-0.17,1.28). Testing whether the bucket, placed 3m away, could sit at a raised position along this path — but plugging in x=2.08 gives a height around -2.3, which is clearly wrong, so the ball would already be underground by then. This means I need to scale up the power while keeping the 55° geometry, then empirically fit the trajectory to land where the bucket actually needs to be.

That estimate doesn't match the observed 0.6 m/s, so the kick must come from elsewhere — maybe the arm's slight overshoot and reversal near the stop, or rolling/spin effects from the ball pressed against the back wall as it rotates with the arm at that angular velocity.

Checking the ball's relative velocity at t=0.50: vz=1.72, vx=2.41, giving an angle of 35.5°. I'm verifying this against the arm's tangent direction, accounting for the ball's offset above the beam centerline—that offset shifts the angle by about 5.6°, bringing the computed tangent angle down to roughly 35°, matching the observed value.

Now I'm recomputing the ball's position at the moment the arm stops (55°), rotating the offset vector to get x'≈-0.455, z≈1.205. With vz=1.49, the predicted apex height comes out around 1.318 at t≈0.68, but the observed data shows 1.28 at t=0.64, so I'm trying to reconcile that discrepancy against the x-position too.

Checking the x-trajectory from -0.455 with vx=2.63, the time to reach x=-0.17 works out to 0.64s, matching observation—so vz should actually be closer to 1.06-1.2 rather than 1.49, meaning there's roughly a 0.35 discrepancy I need to explain, possibly from the arm decelerating before full stop or friction effects during the ball's slide in the cup.

Given the coarse sampling resolution, I'll just use a simplified model: assume the release velocity equals the tangent velocity at stop minus some loss (~0.35 m/s in vz), and design the shot for a robust high arc. I'm thinking about adjusting the stop angle to 45° instead, which would change the effective ball launch angle to around 33-39° after accounting for losses, and want to see how that affects range sensitivity.

I'm checking the release position at 45° stop, computing the required speed for 36° to hit the target, then verifying what happens at 32° with the same speed to check tolerance.

Solving that gives x≈2.64, confirming the angle is near-optimal with low sensitivity near this range. I'm checking speed sensitivity (roughly ±7% speed tolerance for ±12% range) and verifying the near-wall clearance condition at α=32°, where z comes out to about 0.59 m, clearing the 0.46 m threshold even with speed 7% low.

Now I'm working backward to find the required angular velocity at stop: matching the observed tangent speed ratio (0.94) implies I need ω≈4.89 rad/s to hit the target tangent speed of 4.52, consistent with the damping/energy loss ratio of 0.91 seen in the model. I'm then sketching out a spring design that stops the arm at 45°, starting from the gravitational potential energy balance along the beam.

Solving for k gives about 3.2, accounting for the small damping loss from the squared angular velocity term. I'm also sanity-checking the physical setup: the ball should stay seated in the cup under the launch acceleration and centripetal forces, the arm should bounce cleanly at the stop, and the ball's flight path needs to clear the bucket wall and land correctly around 2.08 units in.

I'm now checking what happens once the ball lands inside the bucket — with soft contact parameters it shouldn't bounce much, but it's moving fast enough horizontally that it could slide into the far wall; I need to confirm it won't climb over given the wall height and contact damping. I'm also comparing the torque from the increased arm stiffness against gravitational torque on the beam to make sure the dynamics still check out.

Bucket position at 2.08 gives exactly 3.0 m horizontal travel from the ball's start at -0.92, so that checks out. Now I'll write the file with range "0 45", stiffness 3.2, keeping the catapult geometry and ball start position unchanged.

