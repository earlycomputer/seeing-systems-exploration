The catapult's spring drives the arm into a hard stop at 35°. The stop throws the ball off at about 4.8 m/s, 44° above horizontal. That lands it near the middle of an 80 cm bucket whose base centre is 3 m along from the ball's start.

The spring stiffness comes from an energy balance, which I haven't run. The spring's work from 0° to 35° has to equal the gravity lift plus the kinetic energy of the arm, scoop, ball and armature.

```world
world  catapult into a bucket

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

-- Pivot at 50 cm, arm 40 cm long. The spring pulls toward 90° but the arm
-- is stopped hard at 35°, where the ball (sitting against the scoop back,
-- its centre 11° above the arm line) flies off at 44° above horizontal.
-- Energy: spring work from 0° to 35° = k(1.571·0.611 − 0.611²/2) = 0.773 k
-- covers lift (0.58 J) + kinetic energy at 13.0 rad/s (2.92 J): k ≈ 4.53.
catapult
  is a          catapult
  pivot height  50 cm
  arm length    40 cm
  arm mass      300 g
  swings        from 0° to 35°
  spring        4.53 N·m/rad toward 90°
  damping       0 N·m·s/rad
  armature      0.001 kg·m²
  colour        wood

ball
  is a      sphere 4 cm radius, 100 g
  rolls
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on catapult.scoop base, at catapult.scoop base's near end

-- Base centre 3 m along from the ball's starting centre.
bucket
  is an   open box
  length  80 cm
  width   80 cm
  walls   25 cm
  bounce  dead
  friction  0.9, spinning 0.01, rolling 0.004
  colour  grey
  its base 3 m beyond ball

expect
  ball comes to rest in bucket
```

---
thinking (summarized):

I'm working through the physics setup for a catapult design—sizing the stand, arm, and pivot geometry so the throw trajectory lands the ball three meters into the bucket, reasoning through the dimensions since I can't test it physically.

I'm now computing the hinge rotation math: how the scoop's position and velocity change as the arm rotates about the y-axis, figuring out what release angle gives a 45-degree launch trajectory so the ball leaves the scoop at the right moment and direction.

So the scoop base acts like a flat paddle pushing the ball along its direction of motion, meaning the ball leaves when the paddle decelerates beyond gravity's tangential pull. But I also need centripetal acceleration toward the pivot, which can only come from friction or the scoop's back wall — yet that wall sits at the far end from the pivot, not positioned to provide inward force.

Ball release speed should equal ω·r, with r being the ball's center distance from pivot, slightly offset by its radius above the surface. Instead of a hard mechanical stop, I'm considering a spring targeting something like 45° with a stop further out around 60°, so the ball separates near where the spring's deceleration plus gravity's normal component matches the paddle's own tangential deceleration.

For a uniform rod under gravity alone, the tip's angular deceleration works out to 1.5g·cosθ/L, which exceeds the g·cosθ magnitude needed to keep the ball in contact — meaning gravity alone would cause separation almost immediately once the spring torque weakens below a certain point. This is getting complicated enough that I should consider a different approach to achieve clean, controllable release timing.

After release the ball flies off at roughly 5.4 m/s while the arm oscillates back around 45°, so it won't catch up to the ball — damping can stay moderate since it won't hinder the launch speed much, and I can let the arm swing through a range like 0-100° without the ball getting struck again.

Now I need to nail down the actual geometry: the ball starts at rest at θ=0 and releases at θ=45°, so I need to figure out its distance from the pivot and where it sits relative to the arm's center to get the 3m target distance to the bucket right. I'm working out arm length, pivot height, and box dimensions so the ball's start and release positions line up correctly with the x-offset of the arm.

Scoop back sits just outside the scoop base, flush at the arm's near end. For the ball, a 4cm-radius sphere, I'm weighing whether to center it over the scoop base or push it flush against the scoop back for a more realistic resting position — leaning toward placing it near the back wall, roughly centered at x=−36.

I'm working out the ball's position relative to the pivot by computing its radius and rotating its coordinates through the 45° launch angle to track where it ends up during the swing.

But computing the velocity direction at release, I find it's perpendicular to the radius vector rather than aligned with the base's tilt, giving roughly 34° instead of the intended 45°. So I need to find the release angle that actually produces a true 45° launch trajectory given the ball's offset above the arm.

The ball separates moving tangentially, offset from the base normal by that 11° angle, and since both the base and back wall stop pushing at release simultaneously, the ball just carries its velocity forward cleanly. Setting spring target θ0 = 35° gives a launch elevation of about 44°, which seems like a good working choice.

Now I'm computing the exact release geometry: with θ0=35° the radius vector sits at 46° from the −x axis, giving a release position roughly (−0.255, 0.264) relative to the pivot, and a velocity direction at 44° elevation. From there I'm figuring out the horizontal distance from release point to the bucket center (about 2.89 m) and working out what height the ball needs to be at to land properly in the bucket.

Now I'm sizing the bucket itself—assuming a 40×40 cm open box with 25 cm walls, ball radius 4 cm—and checking that the trajectory clears the near wall while still dropping into the bucket center near the rim height, aiming for roughly a 45° descent angle so the ball doesn't clip the wall edge.

I realize the margins are too tight (ball edge nearly touching the far wall), so I'm bumping the bucket to 60 cm wide, giving an inner half-width of 28 cm for better clearance on both walls.

I should also make the bucket's bounce property dead so the ball settles instead of bouncing out, and I need to figure out positioning syntax — whether to place the bucket by its base or rim relative to the ball's starting point, 3-4 meters away.

I'll go with the along reading for "3 m beyond ball," treating it as horizontal distance rather than full 3D distance, since the checker likely measures horizontal separation. Now working out speed: picking a pivot height, say ph=0.5, gives release z=0.7638, and I need Δz=0.25−0.7638=−0.5138 to hit the target crossing at Δx=2.845.

Using launch angle α=44° (tan≈0.9657, cos≈0.7193), I solve the projectile equation for v², getting v²≈23.53, so v≈4.851 m/s, and angular speed ω=v/r≈13.23 rad/s. Then I check the descent by computing horizontal velocity (≈3.489 m/s), time to crossing (≈0.8154 s), and vertical velocity component at launch.

Vertical velocity at crossing comes out to about −4.63 m/s, giving a descent angle steeper than 45° (around 53°), which confirms the trajectory clears the near wall with good margin — roughly 0.55 m clearance before crossing and landing about 0.09 m past center afterward, well within the inner half-width of 0.28 m. That gives roughly ±0.2 m of range margin, which corresponds to about ±7% tolerance in v², so I start checking how sensitive the landing position is to small variations in launch speed.

Using dR/R ≈ 2dv/v with R ≈ 2.9 and tolerance ±0.2 m, I get a tight ±3.5% speed tolerance, so I need to work through the energy balance carefully. The spring releases energy proportional to θ0² over a 35° swing, and this converts into kinetic energy of the arm plus gravitational PE gain, with the open question of whether to include damping — zero damping would leave the arm oscillating indefinitely after the ball departs, which doesn't matter for the launch itself but complicates clean energy accounting, so I'm weighing whether to just assume zero damping for simplicity.

Now I'm sizing the components: a light ball around 100g and an arm around 300g, then computing the arm's moment of inertia about the pivot using the parallel axis theorem for a 40×6×4 box offset by 20cm, which comes out to roughly m×0.0535 kg·m².

I'm continuing this calculation for the scoop pieces — the base (20g) and back plate (10g) — each getting its own moment of inertia plus parallel-axis correction for their offset positions, summing to about 0.0021 and 0.0017 total respectively.

The default armature value of 0.01 seems too large and would distort the inertia accounting, so I'll reduce it to 0.001. For the ball, I'm computing m·r² at the arm's radius (0.1 kg × 0.1345 ≈ 0.01345) plus its own rotational inertia from spinning with the arm, adding to about 0.01351. Summing everything together gives a total moment of inertia around 0.034.

Now with that total inertia I compute the release kinetic energy as about 3.0 J, and I'm working out the gravitational PE gained as the arm swings from 0° to 35°, using the rotated z-coordinate formula for each mass point — getting roughly 0.338 J for the arm and 0.179 J for the scoop base so far.

Adding the scoop back (0.0216 J) and the ball (0.190 J) gives total PE gain of about 0.584 J. Combining with the kinetic energy, I need about 3.59 J stored in the spring, so solving ½kθ₀² for k gives roughly 19.2 N·m/rad, and now I'm checking the initial spring torque this implies.

Checking the spring torque at θ=0 against gravity torques from the arm, ball, and scoop confirms the spring wins and the arm accelerates away from the lower limit, as expected. Now I need to pin down exactly when the ball separates from the scoop — this happens when the arm's tangential acceleration at the ball's location drops below free-fall, so I'm setting up the torque balance including the spring term k(θ0−θ) to find that release point.

Working through the force balance on the ball from the arm: the contact force must be nonnegative for the ball to stay in contact, so separation happens when the arm's angular acceleration drops below roughly −18.58 rad/s², accounting for the gravity torque contributions from both the arm and the ball itself.

Plugging in the spring torque balance with arm/scoop gravity torque around 0.6 N·m and ball gravity torque 0.25 N·m, I find release occurs when θ − θ0 exceeds about −0.011 rad, meaning the ball essentially separates almost right at θ0, just a fraction of a degree before.

Checking whether separation is stable: after the ball leaves, the arm alone (minus the ball) decelerates much faster under the remaining spring torque than the ball does under gravity, with the arm's tangential deceleration around −10.6 m/s² versus the ball's −6.8 m/s², confirming the arm falls behind and doesn't re-catch the ball.

Now I'm thinking about whether the ball's parabolic trajectory could still collide with the scoop afterward—since the ball moves tangentially outward from the circle while the scoop continues rotating on its radius (0.37 m) with the back edge at 0.41 m, I need to check if the geometry keeps them clear of each other as the arm continues toward its ~70° amplitude.

Comparing the cubic lag term against the arm's angular deceleration, I find the deceleration dominates for t under roughly 0.0187s, after which the ball starts lagging angularly while also drifting outward radially—moving about a centimeter further out by that point, which matters since the back wall extends to radius 0.41 ten centimeters up.

In the rotating frame, the ball's centrifugal drift pushes it outward right toward the back wall's position at the outer end, so after release it likely slides forward along the wall rather than separating from it, since the wall runs tangentially alongside where the ball sits.

Actually let me reconsider without the back wall: in the inertial frame the ball travels straight along the tangent direction, so its radial distance from the pivot grows quadratically over time while the back wall rotates along with the arm. I need to check whether the ball's position along the arm's radial direction stays ahead of or falls behind the wall as both evolve.

I'm computing the tangent direction of the ball's motion relative to the radius vector, finding that the ball initially moves with u decreasing slightly while n grows, then applying the arm's rotation to transform these coordinates into the rotated frame.

So roughly 1.34s² outward drift if the arm keeps spinning at full speed, but since the arm actually decelerates, the lag term subtracts about 0.07δ from u' early on, cutting into that outward motion. I need to check whether this is enough to keep the ball clear of the back wall, which spans from n=0.02 to 0.12 relative to the arm center, with the ball starting at n=0.07.

Now I'm checking the corner clearance — if the ball stays pressed against the wall at u'=0.36, I need to trace how u' evolves afterward using s=4.85t and δ≈15t². Plugging in gives an expansion of roughly 31.5t² − 1.05t² − 71t³, meaning the ball keeps pushing into the back wall up until around t≈0.4 before the cubic term takes over.

Carrying through the expansion, n' simplifies to roughly 0.07 + 0.36δ + 0.26s², meaning relative to the arm the ball creeps forward at about 11.5t² combining both contributions. I need this to grow from 0.07 toward the 0.12+ threshold to figure out the timing.

Checking the corner clearance condition — the corner sits at (0.40, 0.12), and the ball's distance to it must stay beyond 0.04, which requires n ≥ 0.12. Solving 11.5t² = 0.05 gives t ≈ 0.066s for the ball to reach that threshold, during which centrifugal force pushes the ball against the back wall with normal force ~6.4N, and friction (assuming μ≈1) would resist the forward sliding as the arm decelerates.

That friction would decelerate the ball tangentially over 0.066s, producing a velocity change of roughly 4.2 m/s — far too large, meaning the ball essentially gets dragged along with the decelerating arm rather than launching cleanly. But I'm realizing real catapults avoid this because the ball rolls against the wall instead of sliding, so the friction is static rather than kinetic, and rolling contact wouldn't dissipate nearly as much energy — I need to check whether the rolling contact point's velocity actually matches the decelerating wall.

The spin-up from rolling contact converts some translational kinetic energy to rotational, bounded at around 2/7 of the relative kinetic energy for a sphere, and since the relative velocity between ball and arm stays fairly small, the loss might be tolerable, but the net directional effect is too uncertain to trust. I think the cleaner fix is to redesign the cup geometry itself, maybe defining a custom part without a tall trapping back wall so the ball can still get proper centripetal support without getting scooped and dragged.

Looking at the force balance during the throw, the tangential acceleration dominates early on (around 125 m/s²) while centripetal dominates near release (around 64 m/s²), meaning the normal force direction required from the base rotates through the motion -- starting almost purely tangential and ending almost purely centripetal, which implies the base's normal force drops toward zero before release while the back wall takes over providing centripetal support.

I'm now considering whether lowering the back wall height relative to the ball's center (R=4cm) would help, since a shorter wall would mean contact happens at a corner whose normal force has a forward component, potentially causing premature release when centripetal force is still large — so I need a different lip/cup geometry that holds the ball correctly until the intended release angle.

Stepping back, I'm trying alternative designs: removing the back wall entirely and relying on friction (same issue), positioning the ball near the pivot to reduce centripetal demand (doesn't eliminate it), or finding a stop that triggers release exactly where tangential motion dominates. None of these fully escape the fact that centripetal force m v²/r always exists during acceleration, so I need to just work out the actual magnitude and see if the back-wall effect is small enough to ignore.

I'm now checking whether a longer arm radius reduces the required centripetal force for the same exit velocity, and considering whether the abrupt stop of the arm could cause the ball to naturally move away from the back wall rather than into it, since the tangent direction in the arm's frame shifts inward once decelerating.

The key remaining question is how fast MuJoCo's joint limit actually stops the arm — with default solref parameters giving roughly a 0.02s critically damped response, the arm could overshoot by around 15°, which affects whether the ball separates cleanly or gets pinned against the wall during that brief soft-stop window.

So the velocity change over that contact window is small enough to be acceptable. But I realize the hard stop changes the release dynamics entirely: if the spring's target angle is well beyond the physical stop, the arm is still accelerating when it hits the limit, meaning the ball stays pressed against the base until the stop is reached, and release happens right around the stop angle rather than at some earlier point.

With the overshoot small, roughly 0.09 rad or 5°, the ball essentially releases right as the limit engages, with the stop being critically damped so the arm doesn't bounce back—it holds firmly at the limit and the ball flies off cleanly. Checking the ball's velocity direction relative to the arm frame post-stop, it's moving away from the back wall and base, though my earlier analysis of the small-angle expansion for u' showed it initially increasing, which I need to recheck against the stronger deceleration case.

Redoing the first-order expansion for u' with the arm angle lagging the stop angle properly—since the arm doesn't track s/r exactly during the fast deceleration but drops to zero velocity in about 0.015s—the dominant linear-in-time terms compete: one pulling u' negative at a rate around 0.191v, the other depending on the gap between angular displacement and the stop angle. The magnitudes are close enough that it's marginal, but since contact forces are small overall, this shouldn't matter much for the outcome.

Next I need to work out the ball's release elevation angle at the stop point, which should be the complement of the sum of the initial offset angle and the arm's stopping angle.

I'm also weighing whether to enable rolling contact for the sphere — it would help it settle inside the bucket, but without any rolling resistance in MuJoCo a sphere could roll indefinitely on a flat surface, so I should add some rolling friction to make it come to rest naturally rather than bouncing endlessly between walls.

For the catapult's hard stop, I'm confirming the arm swings up to its 35° limit where the spring holds it pinned, so release happens right at that angle — giving an elevation of 44° once I subtract the fixed offset.

I need the spring stiffness k such that the work done from 0° to 35° equals the 3.59 J of kinetic and potential energy required to launch the ball at ω = 13.23 rad/s. Solving with a target angle of 90°, I get k ≈ 4.645 N·m/rad, and I'm now checking the resulting torque at the 35° stop point to confirm it stays physically consistent.

Checking angular acceleration from torque gives about 105 rad/s², producing a linear acceleration at the ball of 38 m/s², which is comfortably above the 6.8 m/s² gravity requirement, so the ball stays pressed against the arm throughout the motion. The ball's own spin inertia from any rolling is negligible, around 0.2%. I'm also considering how sensitive the landing range is to errors in my inertia estimate — a 5% error there translates to roughly 2.5% in speed and about 5% in range, or 0.15 m, which needs to fit within the bucket's tolerance.

I'm enlarging the bucket to an 80×80 cm open box with 25 cm walls to give more margin, and confirming MuJoCo computes the arm's inertia correctly from the combined arm, scoop base, and scoop back geoms with their given masses, matching my own calculation. I'm also verifying the ball's exact starting position — flush against the scoop's near end and back wall, resting on the base — so the initial contact geometry is correct, and checking that the arm starts at its lower limit where the spring immediately pushes it upward.

Now I'm tracing the ball's launch trajectory relative to the stand and arm at the 35° stop angle, confirming no collision with the stand (top at 0.44 vs arm bottom at 0.48) and estimating the ball's path height as it clears the pivot, getting roughly z ≈ 0.51 at the point where Δx = 0.255.

I'm also considering whether overshoot in the arm's swing past the limit could catch up to the ball (it shouldn't, since the ball leaves faster), and now I'm thinking through how to position the catapult part itself — whether default library pieces like the "raised bucket" need an explicit position line or whether the internal "table" piece already handles placement.

Following that model, I'll likely omit the position line for the catapult too, treating the stand-on-floor piece as the implicit anchor, since positions seem optional based on the raised bucket's example. I'm also confirming the bucket base placement should sit 3 m beyond the ball's center (x = -0.36), giving a base center around x = 2.64, which matches my earlier trajectory calc.

Now I'm working through the bucket's wall geometry — base thickness 2 cm, walls 25 cm tall, inner half-width about 0.39-0.40 from center — to figure out where the ball needs to cross z=0.25 so it clears the near wall and lands inside, aiming for a crossing point around center minus 0.12 so the ball settles near the bucket's center after landing.

Solving for the launch speed: computing the horizontal and vertical displacement components gives v² ≈ 22.86, so v ≈ 4.78 m/s, which translates to an angular velocity of about 13.04 rad/s given the wheel radius.

With that angular velocity, I compute the kinetic energy at launch (~2.92 J) and add it to the potential energy change (~0.58 J) to get total energy of about 3.50 J, then divide by the angular displacement to get a spring constant of roughly 4.53 N·m/rad.

Now I'm double-checking the geometry — pivot-to-ball-center offsets give a radius of about 0.3667 m and an initial angle φ0 of about 11° from the horizontal.

I verify the release angle works out to 46° above the −x axis, giving a velocity elevation of exactly 44° as required, and confirm the arm's moment of inertia using the parallel axis theorem comes to about 0.01604 kg·m², matching my earlier value.

Ball mass is 100 g with 4 cm radius, rolling with friction included. Damping stays at 0 since the spring pushes the arm into its stop anyway, and I'm satisfied the 0–35° swing range with the spring target at 90° won't cause issues when the arm hits its limit in MuJoCo.

Checking the scoop geometry on the arm: bottom sits at arm top plus 2cm, with 10cm height putting the top at arm top plus 12cm, ball center at plus 7cm, ball top at plus 11cm — all consistent. I'll finalize the expect block with just "ball comes to rest in bucket," skipping extra contact checks as unnecessary.

Now I'm defining the bucket as an open box 80cm by 80cm with 25cm walls, dead bounce, positioned with its base 3m beyond the ball and centered on y=0. I'm placing the ball resting on the scoop's base at its near end, with the across position defaulting to the centerline, then adding floor friction settings.

