The spring-loaded arm swings up from horizontal and stops hard at 36°. That throws the ball at about 45° and roughly 5 m/s, so it drops into a deep, dead-bounce bucket whose centre is 3 m along from the ball's start.

The numbers below are my own hand estimates. Nothing has been run yet.

- **Catapult:** the pivot is 50 cm up and the arm is 50 cm long. The ball starts against the scoop's back wall, 46 cm from the pivot.
- **Spring and release:** the spring pulls toward 90°, but the hinge stops the arm at 36°. That releases the ball about 13 cm forward of and 26 cm above where it started. To reach the bucket the arm needs about 10.6 rad/s, and a spring of about 4.85 N·m/rad gives that against the arm's inertia, gravity and a little damping.
- **Bucket:** it is 70 cm wide with 40 cm walls. Its width allows roughly ±10% error in the throw's distance.
- **Check:** the ball's start height and both "in" placements rely on my reading of the reference.

```world
world  catapult into a bucket

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

catapult
  is a          catapult
  pivot height  50 cm
  arm length    50 cm
  arm mass      300 g
  swings        from 0° to 36°
  spring        4.85 N·m/rad toward 90°
  damping       0.02 N·m·s/rad
  armature      0.01 kg·m²
  friction      0.8

ball
  is a      sphere 4 cm radius, 60 g
  rolls
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on catapult.scoop base, at catapult.scoop base's near end

bucket
  is an     open box
  length    70 cm
  width     70 cm
  walls     40 cm
  bounce    dead
  friction  0.9
  colour    grey
  its base 3 m beyond ball

expect
  ball touches catapult
  ball touches bucket
  ball comes to rest in bucket
```

---
thinking (summarized):

I'm working out the catapult's geometry—sizing the stand, arm, and pivot placement so the throwing motion can launch a ball roughly 3 meters into the bucket, positioning the hinge and scoop base accordingly.

Rotating the arm about the pivot axis, I derive that a positive rotation lifts the scoop end upward and forward, with release velocity direction depending on the swing angle—around 45° giving a nicely balanced upward-forward launch. I'm now planning the joint limits and spring/stop angles (something like 0° to 60°) so the arm halts near 45° and flings the ball on the right trajectory, keeping in mind MuJoCo's soft hinge constraints.

For placement, resting the ball "in catapult" should work since the scoop base piece ends in " base," satisfying the "in bucket" placement rule—it'll center on that surface. I settle on starting the arm at 0° (horizontal) with the ball resting at rest on the flat scoop, and letting a spring immediately drive the arm toward 90°, which naturally sets the whole mechanism into motion without needing an extra trigger.

Checking the arm against the stand for collisions, there's a clean 4cm gap so no interference. Now I'm working out the release physics at 45°: computing the ball's position relative to the pivot using the arm length and angle to figure out exactly where it launches from.

I realize the velocity direction isn't simply perpendicular to the arm at 45°—differentiating the rotated position gives speed ω√(a²+b²) with a direction angle depending on both a, b, and θ, so getting a true 45° launch means solving atan2(a cosθ − b sinθ, a sinθ + b cosθ) = 45° for the stopping angle θ rather than just picking θ=45°.

But I also need to question whether the ball actually detaches right at the arm's stop position—physically, the ball sits in a scoop and is pushed by the scoop's base and back wall as the arm decelerates, so I need to reconsider the contact forces at release rather than assuming a clean detachment at the geometric stop.

Now I'm thinking through the physical layout: setting the horizontal distance to the bucket at around 3 meters, giving the bucket walls roughly 30 cm height and 50 cm footprint, and setting the catapult pivot height around 50 cm to work out a plausible release point and trajectory.

Ball radius of 4 cm works fine given the scoop dimensions. Now I'm figuring out the target: bucket center is 3m from start, and I want the ball's descending trajectory to cross the bucket's wall-top height near the center, aiming slightly short since it's still falling at 45°. That gives a horizontal distance of about 2.88m from release and a height drop of roughly 0.448m to work out.

Solving the 45° launch equations with that drop and distance gives v ≈ 4.95 m/s at release. Checking against the arm's angular velocity (ω ≈ 11.6 rad/s) and effective radius confirms this is achievable once the arm stops abruptly. Now I need to work out the spring energy required to produce that speed over the arm's swing from 0 to 35°.

I'm estimating the total rotational inertia: computing contributions from the arm itself, the scoop base, the back piece, and the ball, each at their respective distances from the pivot, to get a combined moment of inertia value.

Now I'm calculating the energy requirements: the kinetic energy needed from angular velocity, plus the gravitational potential energy gain as the arm, ball, and scoop rise during the throw, summing these to find the total energy budget the spring needs to supply, then setting a small damping coefficient.

I'm estimating damping losses at roughly 0.07-0.18 J depending on the coefficient chosen, bringing total required energy to about 4.2 J, then working out the spring's stored energy formula based on the angular displacement from rest to the release angle, assuming a 90° reference angle for the spring's natural position.

Solving for stiffness gives k≈5.43 N·m/rad, which checks out against gravity torques from the arm, ball, and scoop (totaling about 1.1 Nm) leaving a net torque around 7.4 Nm — plenty to drive the mechanism. I'm also sanity-checking that the resulting angular acceleration (~142 rad/s²) gives a reasonable tangential acceleration at the ball's radius, confirming the ball stays in contact with the scoop during the initial launch phase.

After the arm hits its stop, I'm now thinking through what happens at separation: the arm decelerates abruptly while the ball continues forward, with friction against the scoop base imparting some spin to the ball, which seems fine for the overall motion. Then I'm checking the radial direction — at release, centripetal acceleration (ω²R ≈ 58 m/s²) pushes the ball outward against the scoop's back wall, so I need to verify the scoop geometry (10 cm tall wall, ball radius 4 cm resting on a 1 cm base) keeps the ball properly contained at a center height of about 5 cm above the arm's top surface.

Now I'm realizing the ball isn't initially touching the back wall — it starts centered over the 16 cm base, 8 cm from the wall's inner face, so it has room to slide outward about 4 cm before contacting the back during the launch. This shifts the effective radius calculation, since the back wall sits just outside the base's near end, meaning the ball would end up at roughly a = 0.46 m if it slides all the way to contact — but I need to check whether centripetal force and friction from the base actually drive it that far given how angular velocity builds up over time.

Rather than guessing how far it slides, it's cleaner to just explicitly position the ball resting against the scoop back from the start, flush with the base's near end, so its center sits at x = −L + r — that removes the ambiguity entirely.

With the across-direction likely defaulting to centered, I'll trust that behavior rather than adding an extra constraint, consistent with how the earlier block example handled unfixed directions.

Now I'm recalculating the geometry with L = 0.5, r = 0.04 giving a = 0.46, and b = 0.07, to work out the resulting radius.

Computing α = atan(0.07/0.46) ≈ 8.65°, so the effective stop angle becomes about 36.4°, rounded to 36°. Since launch angle near 45° barely affects range, small overshoot from the soft joint limits shouldn't matter much — what really drives distance is release speed. I'm now computing the release position at θ=36° using the rotated coordinates from a and b.

Now I work out the launch angle as 90 − 36 − 8.65 ≈ 45.35°, and pick a pivot height of 0.5 m, giving a release height around 0.827. I'm trying to decide how to position the whole catapult assembly relative to the floor and ball, leaning toward keeping the pivot at x=0 for simplicity and figuring out the ball's starting x from there.

For the bucket, I'm thinking through its dimensions (50 cm length and width, 30 cm walls) and how to phrase its placement relative to the ball — using a reference like "its base 3 m beyond ball" to fix horizontal position while letting the floor placement handle vertical alignment, though I'm still unsure how the across-axis default will resolve.

Now I'm working out the geometry more precisely: walls sit at the base's ends with the inner face at roughly ±0.24 m from center, and the ball (radius 0.04) needs to clear the near wall's 0.30 m height while still landing before hitting the far wall. I'm estimating where the ball's trajectory crosses the wall height and how much horizontal distance it covers during descent to make sure it lands inside the bucket rather than hitting either wall.

Raising the wall top to 0.40, I want the ball's path to cross z=0.44 near x_c−0.12 before descending into the base. Working through the geometry, that gives a horizontal distance of about 2.751 and a drop of 0.387, so I'm solving for the launch angle (~45.35°) that satisfies this trajectory equation.

Solving gives vx≈3.42, total speed ≈4.87 m/s, with flight time 0.804s and a descent slope near 52°, landing comfortably within the target zone (x_c+0.16, margin 0.24). Now I'm double-checking the clearance near the wall at that crossing point.

My aim near x_c−0.12 sits close to the window's middle, so I'll shift the aim to x_c−0.05 to center it better; the ±0.25m window gives roughly ±2.3% tolerance in velocity, which is tight but workable. Reconsidering bucket size at 70cm with 40cm walls, the window becomes [x_c−0.33, x_c+0.27] with center at x_c−0.03, so I'll aim there instead and recompute the distance accordingly.

Solving the equations gives vx² = 12.13, so vx ≈ 3.483 m/s and total v ≈ 4.956 m/s, which translates to an angular velocity of about 10.65 rad/s at the ball's radius. I'm now working through the arm dynamics, confirming the ball takes on the scoop's velocity at the contact point, and recomputing the moment of inertia for the arm treated as a box rotating about its pivot end.

Summing contributions from the arm, scoop base, scoop back, ball, and armature gives a total inertia of about 0.0542 kg·m², and plugging into the kinetic energy formula with the angular velocity I found yields roughly 3.073 J.

Computing the height gain for each component's center of mass as they rotate through the swing angle, I get gravitational PE contributions of 0.433 J (arm), 0.151 J (ball), 0.047 J (scoop base), and 0.028 J (back), totaling about 0.659 J. Now I'll pick a reasonable damping coefficient of 0.01 N·m·s/rad for the system.

Estimating damping losses as roughly 0.04-0.08 J depending on the coefficient chosen, and noting the arm will rest against its upper stop since the spring pushes toward 90° but the limit holds it at 36°. Adding everything up gives a total energy around 3.81 J, and now I need to work out the spring's stored energy as it rotates from 0 to 36°.

Solving k·0.6283·1.2566 = 0.7896k against the target energy gives k ≈ 4.83 N·m/rad.

There are a few second-order effects I should flag as uncertain: soft contact penetration between the ball and scoop could absorb a small amount of energy, and the arm's soft limit at the stop means it decelerates over a few milliseconds with possible overshoot of a degree or two, which could slightly shift the ball's launch angle and release timing.

Checking the rest of the setup — the arm's full swing from 0° to 36° doesn't collide with the stand, the ball stays pinned against the back of the scoop throughout since centripetal force pushes it outward, and friction causes it to spin along with the arm at the same angular rate, giving it a small additional rotational kinetic energy I should account for.

So the ball slides along the scoop's inner back face without penetrating it, and any slight rebound of the arm from its limit shouldn't collide with the ball since it's already moving away. There's no air resistance to worry about, and the ball sits on the scoop base which rests on the arm, so I just need to place the bucket roughly 3 m beyond the ball's position.

Everything stays centered on y=0 — the catapult, arm, stand, ball, and bucket all align on that axis. I'm uncertain whether the catapult part itself needs an explicit position clause since it's the first thing placed with nothing above it but the floor; there's no listed clause like "stands on floor" so I'll just omit a position for it to avoid an invalid construct. For the ball, I'm placing it resting on the catapult's scoop base, referencing the scoop's coordinates directly.

Now I'm working out the catapult's numeric parameters — pivot height, arm length and mass, swing range, spring torque, damping, and armature inertia — and writing them into the catapult part definition.

For friction, I'm setting defaults on the catapult body while giving the ball slightly higher friction (0.8) with rolling contact since it rolls inside the scoop, and leaving bounce at default except for a dead bounce on the bucket. Then I'm checking the ball's launch trajectory, estimating it lands roughly 0.16+ meters past the catapult's center with a horizontal speed around 3.5 m/s.

With a dead bounce the ball should hit the base, slide or roll toward the far wall, and stop there without climbing the 40cm wall, so that seems fine, and nothing else intersects the flight path. I'm also checking sensitivity: the velocity scales roughly with the square root of kinetic energy, and comparing spring energy (3.81) against kinetic energy (3.07) gives a landing window of about ±0.3m on a ~2.85m range — translating to roughly ±10% range tolerance, which seems acceptable. Now I'm double-checking the arm's rotational inertia using the box inertia formula for rotation about the y-axis.

Total inertia comes to about 0.025, which looks right. For the ball I'm settling on a 4cm radius sphere weighing 60g, and confirming the 0.02 N·m·s/rad damping value is reasonable. I'm also making sure the description says the ball comes to rest in the bucket rather than "cup," and adjusting the spring constant to 4.85 N·m/rad — the arm's stop softness shouldn't matter since the ball releases before then.

