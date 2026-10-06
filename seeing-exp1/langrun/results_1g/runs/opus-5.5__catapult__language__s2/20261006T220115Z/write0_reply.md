The arm is spring-loaded and released at once. It swings up to a stop at 45°. The ball rests against the scoop's back wall and leaves at about 4.6 m/s, roughly 38° above horizontal.

**Settings**

| Item | Value |
|---|---|
| Arm | 60 cm long, 300 g |
| Pivot height | 50 cm |
| Ball start | 56 cm behind the pivot (x = −0.56 m), 4 cm radius, 100 g |
| Spring | 4 N·m/rad, pulling toward 90° |
| Hinge range | 0° to 45° |
| Bucket | 80 cm square, centre 3 m beyond the ball's start (x = 2.44 m) |

**Energy budget, from 0° to the stop**
- The spring delivers about 0.925 × k J. At k = 4 N·m/rad that is about 3.7 J.
- Raising the arm, scoop and ball takes about 1.1 J.
- Damping takes about 0.04 J.
- The rest, about 2.6 J, becomes kinetic energy. With about 0.078 kg·m² about the pivot, that gives ω ≈ 8.2 rad/s.

**Predicted flight**
- The ball leaves from about (−0.35, 0.95) m.
- It should cross the 25 cm rim at x ≈ 2.39 m and land on the base at x ≈ 2.57 m.
- Usable inner span for the ball's centre is about 2.09–2.79 m.

This is a hand estimate. The joint stop is soft, so the real release speed may differ by a few per cent. If the run shows a miss, k is the knob to adjust.

```world
world  catapult into a bucket

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

catapult
  is a          catapult
  pivot height  50 cm
  arm length    60 cm
  arm mass      300 g
  swings        from 0° to 45°
  spring        4 N·m/rad toward 90°
  damping       0.01 N·m·s/rad
  armature      0.001 kg·m²
  colour        wood
  stands        on floor

ball
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.01
  colour    orange
  moves     freely
  rests     on catapult.scoop base, at catapult.scoop base's near end

bucket
  is an     open box
  length    80 cm
  width     80 cm
  walls     25 cm
  friction  1.0, spinning 0.01, rolling 0.01
  bounce    dead
  colour    grey
  stands    on floor, its base 3 m beyond ball

expect
  catapult reaches its upper stop
  ball comes to rest in bucket
```

---
thinking (summarized):

I'm working out the physics and geometry for a catapult that launches a ball 3 meters into a bucket, structuring the stand, pivoting arm, and scoop dimensions and placement relative to the pivot point.

With the scoop mounted at the arm's near end, I work out the rotation math around the y-axis: the arm starts pointing backward, and positive rotation swings it up and over to launch the ball forward, with the release velocity direction depending on the angle. I settle on a spring pulling the arm toward roughly 90°, with a hard stop around 45° to control the launch angle and timing of release.

For placement, I need the ball to rest naturally in the scoop at the starting position — I'll use "rests in catapult" since the scoop base is the piece ending in "base," matching the bucket-style convention. The ball should launch once the arm decelerates at its rotational limit, releasing at that stop angle.

With a hard stop at θmax, the ball leaves with velocity v=Lω directed along the tangent, giving an elevation angle of 90°−θmax — so a 45° stop gives a 45° launch angle. I'm checking that the scoop geometry makes sense through the swing: at θ=0 the scoop base supports the ball upward, centrifugal force pushes it against the scoop back near the outer radius, and at the 45° stop the ball releases forward along the tangent direction as the scoop back no longer blocks it.

Now I'm working out the ball's release position precisely: with pivot height h and arm length L, placing the scoop base near the arm's outer end, I'm computing the ball center's horizontal offset (L minus roughly 8 cm for the scoop's half-length) and vertical offset (accounting for arm thickness, base thickness, and ball radius) relative to the pivot.

I want the catapult stand placed at the origin so the pivot sits at x=0, with the ball starting at x = −d (d being the horizontal offset from pivot) and the bucket's rim positioned 3 meters beyond the ball's landing point, likely expressed by placing the bucket relative to another part's piece.

I'll describe the bucket as an open box with its base 3 m beyond the ball and resting on the floor, combining those two spatial clauses. Now I need to pick a sphere for the ball and work out the actual trajectory math.

I'm settling on a 4 cm radius, 100 g ball, a 60 cm arm length, and a pivot height of 50 cm, then checking the clearances — the scoop's starting position relative to the stand, how far the arm extends past the stand at rest, and whether the rotating arm would clip the stand as it swings upward toward the pivot.

I'm also starting to check whether the arm needs a stop or support at rest, since gravity acting on the arm's offset mass creates a torque about the pivot that I need to account for.

The torque from gravity pulls the arm toward decreasing θ, so it naturally rests at the lower limit of 0°—and since the spring is set to pull toward the positive direction, it launches immediately from that rest position, which is exactly the intended mechanism. Now I'm working out the ball's release point at the upper stop, computing its position in the arm's rotating frame.

Trying θmax = 45° as a test case: calculating the release coordinates and velocity direction from the rotation formulas, getting position roughly (−0.318, 0.917) with velocity components around (0.59, 0.45)ω.

But I realize there's a deeper issue with the joint limit mechanics in MuJoCo — soft limits cause overshoot and bounce, so the ball likely separates from the scoop at the moment the arm decelerates, not exactly at θmax. I also need to account for the centripetal force requirement: the ball moving in a circular arc around the pivot needs inward force, and I should check whether the scoop geometry (with the pivot offset outward) actually provides that properly during the swing.

Now I'm working out the target geometry: bucket center at x=2.48, with the ball needing to clear the walls and land inside around z=0.3. That gives a horizontal travel distance of about 2.80 m and a vertical drop of roughly 0.617 m from the release point, which I can plug into the projectile equations using the elevation angle I found earlier.

Solving the trajectory equation for v, I get v²≈22.08, so v≈4.70 m/s, and dividing by the arm's radius gives an angular velocity ω≈8.96 rad/s needed at release.

Now I need to think about how much spring energy produces that release speed, which is trickier since it depends on arm inertia, damping, and exactly when the ball separates from the scoop as the arm decelerates.

Taking the spring torque model with target angle θ0=90°, I'm computing the work done over the 45° swing to 0.925k, and I'm starting to account for gravitational potential energy as the arm and scoop rise during the throw.

Breaking down the geometry, I'm tracking how much each component — arm center, scoop body, scoop back, and ball — rises vertically at 45°, then settling on a 300g arm mass to estimate the total gravity PE needed to overcome.

Now I'm computing the moment of inertia at the pivot for each part: the arm treated as a rotating box, the scoop base and back approximated as point masses at their respective offsets, summing their contributions using the parallel axis theorem.

Adding up all components gives total inertia around 0.0737 kg·m². From there, KE = 0.5·I·ω² comes out to roughly 2.96 J, and I'm estimating damping losses using a small damping coefficient applied over the average angular velocity and angle swept, adding about 0.04 J to account for that dissipation.

Solving for the spring energy needed, I get about 4.07 J total, which translates to a spring constant k ≈ 4.40 N·m/rad. Then I check whether the ball stays seated in the scoop at the start: computing the initial spring torque and net angular acceleration, I confirm the ball gets pressed into the base and scoop by the combination of the arm's upward push and centrifugal effects, so it shouldn't slip out initially.

But then I realize the ball could roll backward along the scoop base toward the back wall due to centrifugal force — tracing the geometry, it has about 4 cm of room to roll before hitting the back, which would shift its effective radius and change the launch speed calculation. I'm considering explicitly fixing the ball's starting position against the back of the scoop to avoid this ambiguity.

Checking whether centrifugal force dominates early in the swing versus gravity pulling the ball toward the pivot — centrifugal clearly wins, so the ball stays pressed against the back. Recomputing the radius with d=0.555 and e=0.07 to get the effective distance.

I'm working out the release geometry at 45°: computing the x and z position, then the velocity direction and resulting elevation angle, getting roughly 37.8° above horizontal. Then I'm setting up the target — since the ball starts 3 m from the bucket, the horizontal and vertical offsets to the landing point work out to about Δx=2.788 and Δz=−0.642, which I'll use to aim the throw.

Accounting for the ball's radius, I want the center to cross around z=0.34 near the bucket opening, but since a descending ball keeps moving forward, I'm testing aiming a bit shorter instead, trying z=0.2 at the same x, giving Δz=−0.742. Plugging in, Δx·tanθ comes to about 2.163, and adding the drop term gives roughly 2.905, which I set equal to the standard projectile range equation to solve for the required launch speed.

Solving gives v²≈21.03, so v≈4.586 m/s, and with the wheel radius that corresponds to an angular speed ω≈8.20 rad/s. I'm now verifying this by computing the velocity components (vx≈3.624, vz≈2.812) and solving the quadratic for when the ball's height reaches z=0.34, finding t≈0.739s, which puts x≈2.336 — noticeably off from my target of 2.445, so this launch condition doesn't quite land where I wanted.

This margin is only about 4 cm from the wall, which is too tight given the trajectory angle (~50°) through the bucket opening. I'm thinking the fix is to make the bucket wider (e.g. 60 cm) and adjust the aim so the ball crosses the rim height closer to center rather than near the edge.

Switching to a 60 cm bucket with 25 cm walls, I'm recalculating so the ball's center crosses the rim at x≈2.40 and lands around x≈2.60 on the base, comfortably inside the far wall's inner face at 2.695 — that should keep it inside after it settles. Now I'm solving for the launch velocity needed to hit that crossing point, working through the trig and getting v² around 21.

Refining with v=4.6 m/s and ω=8.22 rad/s, I trace the trajectory: landing on the bucket base at x≈2.569 and crossing the rim height at x≈2.394, both comfortably within the 2.195–2.695 inner range with 10-13 cm of margin on each side — giving decent tolerance for small speed errors.

Since my model's uncertainty in release dynamics and soft limits is probably larger than a tight 2% speed tolerance, I'm opting for a bigger 80 cm bucket with 25 cm walls, giving an inner range of about 2.095–2.795 m after accounting for ball radius, and centering my aim near 2.445 m works well with both the crossing and landing points staying safely inside this wider margin.

With the joint limit, MuJoCo's soft constraint allows slight penetration before decelerating, so the ball likely separates from the arm just past 45°, moving tangentially at roughly peak angular velocity. I need to check whether this tangent direction clears the scoop's back wall, since that wall's normal runs along the arm itself rather than blocking the ball's path of motion.

The ball stays pressed against the back during the deceleration, then slides upward and away once the arm stops, with friction against the back possibly imparting minor spin. I'm also checking the trajectory doesn't intersect the arm or stand — tracing the path over the pivot confirms it clears safely behind the arm's extent.

Now I'm recalculating the energy balance using the updated distance d=0.555, factoring in the ball's moment of inertia and its rise height.

Totaling up moments of inertia for the arm, base, back, ball, and armature gives roughly 0.0775 kg·m², leading to a kinetic energy at ω=8.22 of about 2.62 J, against a combined potential energy rise of 1.10 J across all components. Now I'm factoring in damping with coefficient c=0.01 to refine the angular velocity estimate.

Working through friction and gravity losses, I land on a total energy of 3.754 J equaling k times the angular displacement term, solving for a spring constant around k=4.06 N·m/rad. I pause to double-check whether the ball actually rotates rigidly with the arm since it's pressed against the back and base, concluding that friction makes this a reasonable approximation, and verifying the arm pivot geometry once more.

Checking the arm's mass and dimensions, 300g seems plausible even though it's a bit heavy for the stated wood block size. I then verify the torque balance at the initial position: spring torque versus combined gravity torques from arm, base, back, and ball, confirming a net positive torque that successfully launches the mechanism from the lower limit.

Next I'm working out exact ball placement — whether it sits flush against the scoop's back face or slightly offset, computing the resulting centre position and distance along the arm, since this placement barely changes the overall setup.

Recomputing angular velocity and energy with the slightly adjusted distance: the needed spring constant comes out close to 4.0 N·m/rad after rounding, so I'll settle on that value. Then I want to double-check how the arm's near end position interacts with the scoop base position at the other extreme.

For placing the ball, I'll describe it as resting on the catapult scoop base at that base's near end, leaving the across-axis position at its default center since nothing specifies otherwise — adding a conflicting "centred over" constraint would fight with the along-axis placement, so I'll skip that. For the bucket, I'm positioning its base 3 meters beyond the ball's location along the same axis.

Now I'm computing the release point from a 45-degree launch: with the ball starting around x=-0.56, the release coordinates work out to roughly x=-0.346, z=0.945. Then I'm thinking through whether the ball will actually settle in the bucket — with a dead bounce off the walls and some rolling friction, it should roll around and eventually come to rest rather than bouncing out, so I'm considering bumping up the rolling friction coefficient a bit to help it settle within the time limit, keeping in mind MuJoCo takes the max of combined friction parameters.

Bucket is an open box 25 cm walls, 80x80 cm floor, with the catapult stand positioned clear of the ball's path. I'll set damping to 0.01 and armature to 0.001, and define end conditions like "ball comes to rest in bucket" and "catapult reaches its upper stop" — keeping phrasing simple even if some terms risk being unparseable, since they'll just get flagged if so.

