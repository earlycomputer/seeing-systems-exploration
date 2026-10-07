

---
thinking (summarized):

I need to design a working Rube Goldberg chain in MuJoCo without being able to simulate it first, so I have to be careful with the physics. I'm working out the pendulum geometry: setting a pivot height, a length of 0.8m, and calculating the release angle needed so the bob drops 0.6m before striking the next element.

Now I'm tracing the rest of the chain — the bob hits a sliding cart, which pushes a weight off a ledge onto one end of a seesaw, which then flips a ball into a cup. Since exact trajectories are hard to guarantee without running the sim, I'm leaning toward making the cup large and positioned close to the seesaw's throw point to make the landing more forgiving, and I'm thinking through the tangential velocity direction the ball gets as the seesaw rotates.

I'm working out the pendulum geometry precisely: pivot at (0, 1.0) with length 0.8, so the bob's lowest point sits at z=0.2 with radius 0.05. For the rotation about the y-axis, I derive that placing the bob at negative x requires a positive angle q, and solving cos θ = 0.25 gives θ ≈ 1.3181 rad (75.5°), which I'll use as the keyframe starting qpos so the bob swings forward and strikes the cart at the bottom of its arc.

Now I'm positioning the cart on the track, centering it at z=0.2 to match the bob and placing it at x≈0.16 so there's clearance for the swing. The cart uses a slide joint along x with small damping, equal mass to the bob (~1 kg each), so the inelastic-ish contact in MuJoCo should transfer velocity reasonably, giving the cart roughly 1.7 m/s after impact — I'm considering whether to add a slide range limit so the cart stops at a defined point rather than sliding indefinitely.

Thinking about the next stage after the cart: maybe the weight sits on a pedestal in front of the cart, gets struck, slides off the edge due to friction deceleration, and falls onto one end of a seesaw. Since the exact launch velocity is uncertain, landing position will vary, so I want to make the receiving arm of the seesaw wide enough that the weight lands successfully anywhere on the correct side of the pivot, with a ball balanced on the opposite end.

I need to check the vertical spacing more carefully—cart spanning 0.14-0.26 would collide with the shelf top at 0.15, so I should shift the cart center up to 0.22, spanning 0.16-0.28, and adjust the pendulum pivot and weight position to match. Actually, the seesaw needs to sit below the weight, which is getting cramped given the shelf height, so I think I should raise the whole assembly and reposition the pendulum pivot higher to make room.

I'm working out cart dimensions so it clears the shelf, placing it initially with a small gap from the bob and weight. I'm checking whether the cart's slide range lets it strike the weight hard enough to push it off the shelf edge, factoring in friction and the resulting velocity transfer.

Simplifying, I place the weight right at the shelf's edge so even a light nudge sends it falling, with some residual horizontal velocity, down onto the seesaw's right arm. Now I need to figure out where the seesaw pivot and arms sit so the right arm catches the falling weight without the left arm (holding the ball) colliding with the shelf structure above.

Let me reposition pivot at x=1.0, left arm from 0.6 to 1.0 taking the falling weight, right arm from 1.0 to 1.4 holding the ball. Resting state has the ball side down at its stop since the seesaw isn't balanced, so when the weight drops on the left it tips the right side up, launching the ball — I need to work out the rotation direction and resulting velocity components carefully.

At the stop, velocity tilts back by α toward -x as the plank decelerates, so a ball on the right end gets flung toward the pivot side. By symmetry, placing the ball on the left end instead would launch it toward +x — meaning I need the ball on the left arm and the weight on the right arm so the throw direction matches where the cup should sit.

Thinking in 3D, if the seesaw runs along y with hinge axis x, the falling weight brings an x-velocity onto a wide landing platform (maybe 0.4m in x to catch the spread). But simplifying back to a seesaw along x: weight lands on the left arm near the shelf, ball sits on the right end, and gets launched up and toward -x back over the pivot — so the cup needs to be positioned at -x relative to the ball's starting point.

Placing the cup there risks collision with the shelf or weight though, so I consider having the ball on the left end instead with the weight landing on the right arm, meaning the shelf (giving +x velocity) sits above the pivot/left-arm region. That still risks the ball passing too close to the shelf on its way up. Maybe reversing the whole setup — having the pendulum on the right and flowing everything toward -x — could resolve this geometry problem.

Rather than reasoning along the x-axis for the seesaw, I try orienting the plank along the y-axis instead: the pendulum-cart-weight chain stays along x, dropping the weight onto the seesaw near x≈0.8, but the seesaw's pivot and arms are now arranged along y, with the receiving arm extending through y=0 and the ball-launch arm reaching up toward y≈0.65. I'm working out which way the ball should be tilted on launch given this new arm placement.

However, following the physics through, I realize the ball-end velocity at the stop always ends up tilted back toward the pivot side, which seems to generalize no matter which end the ball sits on — meaning the ball gets launched inward rather than outward. That's a problem unless something about the ball's release timing or the plank shape changes this, so I'm reconsidering whether the ball could actually leave the plank before it hits the stop.

It's also tricky because the ball slides along the plank outward due to centrifugal effect and friction, and with a small tilt angle the ball launches nearly straight up, landing close to where it started—meaning the cup would need to sit right above the plank, which seems awkward. Maybe a backstop or wall could redirect it, but that feels overcomplicated, so perhaps an asymmetric seesaw setup could angle the launch better.

The weight-end reaching its upper limit while the ball end dips negative still counts as the "lower stop" semantically, so that's fine. For actual launch distance, I want the ball-end stop angle more like -0.6 rad for a steeper, more outward trajectory, but I need to make sure the ball doesn't roll off the plank prematurely while resting — maybe add a small lip or cup geometry at the ball end to hold it in place before release.

Now I'm reconsidering the mechanics: starting the plank at a steeper incline like -0.7 rad (40°) so the ball settles into the lip at the outer, lower end, then as the plank swings upward the lip carries the ball along until release at φ_stop, giving a launch velocity roughly perpendicular to the plank. With φ_stop around -0.35 rad (20°), that's about 70° elevation, which seems reasonable. I'm also wondering if a different launcher design — like having the plank strike the ball directly rather than carry it — might give more predictable results, since the main uncertainty is how consistent the weight's effective speed will be.

Given that speed uncertainty, I think the robust solution is to make the catch itself forgiving rather than trying to nail the exact trajectory — for instance, launching the ball toward a tall backboard so it falls into a cup positioned against that wall, which would tolerate variation in launch speed much better than trying to land the ball directly in a small target. I can build the cup and backboard as a single fixed body so the ball reliably drops into the cup after hitting the wall.

I'm also considering the settling requirement: once the ball lands, it needs to stop moving within six seconds, but a sphere with friction alone may keep rolling around inside the cup. I may need to add some damping to the ball's freejoint to help it settle faster.

Timing checks out across all stages within 6 seconds. Now I'm working out exact coordinates and masses: pendulum pivot location, bob and rod masses, and the starting angle needed so the bob swings to hit its target with the right position and height.

Checking that the rod geometry stays clear of the cart during the swing, then continuing to place the cart body and its sliding joint.

Working through the collision physics: the bob at 3.43 m/s hitting the equal-mass cart should give roughly 1.7 m/s each in an inelastic collision, after which the cart continues forward while the pendulum swings back and decelerates under gravity. Then I need the cart to travel across a gap and strike a weight — considering making that weight lighter, maybe 0.5 kg, so the cart can push it off after impact.

Now I'm checking the collision outcome again and the exact geometry — if it's elastic-ish the weight ends up with more speed while the cart hits its joint limit and stops, letting the weight slide off alone. I'm working out where the weight needs to sit on the shelf so its center and the cart's contact face overlap correctly in z, placing the shelf edge and weight dimensions so the push happens before the cart maxes out its range.

The cart's joint limit acts as a soft stop so the weight separates cleanly with its own velocity. Checking collisions: the cart's bottom clears the shelf top fine, and the shelf geometry and supporting post sit well clear of the seesaw's path so nothing interferes. The weight should leave the shelf edge around x≈0.57 with roughly 1.0–1.5 m/s of forward velocity.

Now I'm working out the seesaw geometry — placing the pivot so the receiving arm is on the left to catch the falling weight, with the ball arm on the right launched outward in +x when the weight's impact tips the left side down. I need the initial rest state to have the ball end down against its stop, which means balancing the arm lengths or adding a counterweight so the seesaw sits correctly before impact.

I'm thinking about adding a small cup or lip at the plank's end to hold the ball before launch, checking that it won't block the ball's near-perpendicular trajectory once the plank stops rotating since the lip is shallow relative to the ball radius. I'm also considering whether a horizontal-at-stop configuration with vertical launch might simplify things, but that loses the horizontal travel I need, so I'm leaning toward picking φ0 around 0.5 rad with the ball end tilted down initially.

Now I'm working out the launch angle from vertical based on φ_stop, trying to get closer to a 45° trajectory for good horizontal distance, but the geometry constraints (φ0 must exceed φ_stop in magnitude) are pushing toward steeper setups than I want. I'm settling for a roughly 23° angle from vertical and estimating that with a 3 m/s launch speed, the horizontal and vertical velocity components would give reasonable height and distance for the ball's flight.

This risks landing short on the rim rather than in the cup, so I need to reconsider the release mechanics more carefully: the ball's velocity at release equals the cradle's velocity when the seesaw hits its stop, directed perpendicular to the plank. I'm thinking through angle choices — starting around 40° and rotating through roughly 0.35 radians before stopping — since the weight's impact delivers speed immediately, so the rotation range just needs to be sufficient rather than large.

Now I'm estimating whether the weight might slide off a steep incline arm after landing, though since the momentum transfer happens mostly at impact, that shouldn't matter too much. Working through the physics: the weight falls about 0.26 m giving roughly 2.3 m/s vertical speed, and with a light 0.2 kg plank (moment of inertia ~0.0107) impacting at about 0.25 m from the pivot, I can start estimating the resulting angular velocity transferred to the ball.

Continuing the gravity torque over the swing gives ω²≈34, so ω≈5.8 rad/s and ball speed around 2.3 m/s — still underwhelming. I'm reconsidering the lever arms, making the ball's arm longer than the weight's arm, and wondering whether a heavier weight dropped from a greater height could do better despite the added uncertainty.

With a 1 kg weight and 1 kg cart, I estimate the cart arrives around 1.6 m/s, handing the weight roughly 0.8-1.6 m/s. Raising the whole mechanism — pendulum pivot near 1.8 m, cart at 1.0 m, shelf at 0.9 m, seesaw pivot at 0.2 m — gives the weight a longer 0.6 m fall and about 3.4 m/s, producing a stronger ω. I also need to check that a tall backboard keeps the ball's trajectory forgiving even at lower speeds, since low initial velocities are the real risk.

I'll target a nominal ball speed around 4 m/s with reasonable range. For the seesaw, I'm placing the pivot at height 0.25 with arm lengths 0.35 on the left and 0.55 on the right, so the plank naturally rests right-side down even before adding the ball. Then I work out that the falling weight, leaving the shelf edge around x=0.57-0.6 with vx near 1 m/s and dropping about 0.55 m, lands roughly 0.2-0.5 m horizontally depending on speed, which tells me where it strikes the seesaw's left arm.

But the landing spread is actually wider than I'd like — closer to x=0.8-1.1 — partly because the weight tips as it goes over the edge. That means I need a longer left arm (around 0.5) with the pivot shifted to x=1.2, putting the ball on the right arm near x=1.8, though landing closer to the pivot reduces torque. I'm also considering whether to add a guide or funnel — like a stopper wall right after the shelf edge — to narrow the landing spot instead of relying on the seesaw geometry alone.

Checking clearance so the seesaw's left end can swing down freely without colliding with the wall or shelf bottom—should be fine. Then for the ball side, I'll mirror this with a backboard cup design, and start pinning down exact coordinates: pendulum pivot and bob position, cart body dimensions and slide range, and shelf top placement.

Now I'm working out the weight block's position relative to the shelf and cart, checking vertical overlap and clearance so the cart can push the weight without collision, then figuring out how far the cart's stroke can shove the weight toward the edge before it needs a stop wall to prevent it falling off.

Moving the wall out to x=0.76 gives a 0.23 gap, wide enough that the weight's width (0.12, diagonal 0.17) shouldn't jam between the shelf edge and wall as it tumbles off and falls toward the wall after being pushed.

For the seesaw stage, I'm placing the pivot at (1.0, 0.3) with the left arm 0.55 long, resting at x=0.45 when horizontal and starting tilted up at the left so the weight's landing zone (x 0.55-0.70) sits safely below both the wall bottom (0.55) and shelf bottom (0.85). I need to check that the wall at x=0.76-0.81, positioned above the left arm's path, still clears the plank height as it swings.

With left end extended to 0.65, z works out fine clearing the shelf bottom, and the post is clear too. At the stop angle the left end still sits above the floor, so that's safe, but I realize the rotation range is only 0.25 rad, which seems like a modest tilt—and since the left end is the higher side, the weight would actually slide downhill toward it rather than away.

Actually the weight slides toward the pivot, potentially continuing onto the right arm and risking sliding too far toward the cup—I should add a stopper bump on the plank near the pivot to keep it from wandering into the cup area.

I should try different starting and stopping angles for more horizontal launch—say φ0 = 0.75 and stopping at 0.45, giving roughly 26° tilt. But really the launch direction depends on the velocity of the cradle's contact point, which is perpendicular to the radius from the pivot—so if I offset the cradle on a post above the plank, that radius direction changes and I can tune launch angle independent of the plank's incline.

So instead of a straight arm, I could bend the lever: keep the plank for the weight, but angle the ball-holding arm downward so its endpoint sits at -45° relative to the pivot at the stop position, giving the desired 45° outward launch.

Working out the specific geometry now — defining the pivot and arm directions at the stop pose, with the left arm (plank) oriented near-horizontal and the right arm bent downward at roughly -40° so the ball releases at about 50° elevation.

Checking the clearance there: shelf bottom at 0.85 leaves barely any fall distance for the weight, which is bad, so I should raise the whole shelf/cart/pendulum assembly by 0.4 or shorten the right arm to fix it. I also need to double check the rotation sign convention for the hinge so the left arm moves down correctly.

Working through the seesaw mechanics, positive q lowers the right end and raises the left, so with right-heavy torque the seesaw naturally rests at its upper limit — I'll set the joint range to 0–0.35 and start qpos at 0.35 so it's resting against that stop before the weight lands.

I need to make sure right-side torque exceeds left-side torque, so instead of adding a counterweight (which would slow the launch), I'm lightening the left plank and calculating each component's torque contribution — left plank mass 0.1 at radius 0.325, right arm mass 0.15 with its horizontal lever arm, plus the ball cradle — to balance things so the mechanism rests correctly before firing.

This matters because if the left side is heavier, the arm would rotate the wrong way and hit the lower stop prematurely instead of staying cocked at the upper limit. I'll refine the exact pivot geometry later, then move to figuring out the launch speed starting from the weight falling off the shelf.

Now I'm working through concrete coordinates: the seesaw pivot sits at (1.0, 0, 0.55), with the right arm at 0.45 length reaching the cradle position at the stop angle, and slightly further at the starting rotated angle to confirm it stays above the floor. The left arm, at 0.65 length and raised 0.35 radians at start, lands around (0.389, 0.773), which I need to check against the shelf position.

Checking clearances, I find the drop from shelf bottom to the plank is only about 0.19 m, which feels too small, so I'm raising the shelf and cart by 0.4 m—shelf top to 1.3, cart z to 1.4, pendulum pivot to 2.2, bob lowest point to 1.4—giving a more satisfying 0.6 m drop.

Checking the wall stop and impact velocity (roughly 3.4 m/s) against the plank geometry, everything seems to clear properly, with the wall sitting between 0.75 and 1.6 in height. I'm also considering shifting the pivot so the weight lands farther out for more torque, landing somewhere in the 0.55-0.72 x-range, and estimating the final impact with a 1 kg weight falling about 0.58 m onto the plank.

Now I'm working through the seesaw's angular impulse at impact—computing the torque from the weight's vertical velocity times its horizontal distance from the pivot, then summing up the moments of inertia for each component: the left plank, the right arm, and the cradle-ball assembly.

Treating the collision as inelastic gives an angular velocity around 6 rad/s, so the ball launches around 2.7 m/s, but then I account for continued gravity torque as the weight keeps rotating down, which adds more kinetic energy and bumps the ball's speed up toward 3-3.5 m/s. I'm noting the contact isn't perfectly rigid since the weight can slide along the incline too, so I'm treating the launch speed as a range (roughly 2.5-3.5 m/s) and now moving to calculate the projectile range at the ~50° launch angle.

Now I'm trying to tune the masses to get the geometry to balance correctly — making the cradle and ball lighter to boost speed, then checking whether the resting torque on the right side still holds the arm in place given the new left-side mass and arm length, working through the horizontal lever-arm components to see what right-side mass is needed for equilibrium.

Checking the margin confirms the right side still slightly overbalances the left, giving good stability. Then I work through the moment of inertia for each piece, combine with gravitational work to get angular velocity after release, and from that derive the ball's launch speed and resulting projectile range.

Now I'm second-guessing whether the ball truly launches at the stop with that computed velocity, since before hitting the stop the cradle is still accelerating and the ball should stay seated — only at the abrupt deceleration does it fly free. I also need to account for centripetal force: the cradle must support the ball radially toward the pivot throughout its swing, so I'm thinking through how to shape the cradle floor so its normal force provides that inward component correctly.

So the cradle forms an L-shape: the arm itself as the floor, plus a perpendicular wall at the outer end, with the ball resting in that corner both at rest and during motion. At release (arm at -40°), the ball shoots off perpendicular to the arm, giving the 50° elevation I wanted, sliding along that outer wall as it launches — I might add small side rails just to keep it from drifting sideways, though no real force pushes it that way.

Now I need to pin down the exact launch point: the ball sits on top of the arm surface (the side facing away from the pivot), resting against the end wall, and I'm working out its position in the body frame relative to the pivot, arm thickness, and ball radius.

Working out the arm's box geometry in the body frame—its direction vector, center position, and rotation about y to align with the 40° arm angle.

To avoid unit confusion between joint ranges and euler angles, I'll switch the compiler to radians, converting 40° to 0.6981 rad. Then I'm positioning the end wall box perpendicular to the arm, computing its center offset along the normal direction and its half-sizes so it sits flush against the arm's outer end.

I'm recalculating ball and wall positions to keep the ball tucked against the arm surface while the wall extends above it—adjusting the d and n coordinates so the wall's rotation (via the y-axis euler) correctly aligns its local z-axis with the normal direction.

Now I'm working out the side rails flanking the arm at ±y, sized to leave an inner gap matching the ball radius plus clearance. Then I'm computing the ball's actual starting world position by taking its body-frame point and rotating it by the initial joint angle q=0.35 about the y-axis.

I'm checking whether the ball rests cleanly on the floor or needs a slight offset, and then thinking about how to handle the pivot support post — making it visual-only with no collision so it doesn't interfere with the swinging arms.

For the left plank, I'm sizing a box geom horizontal in body-space to catch the weight, widening it slightly to account for drift, and adding a small bump stopper near the pivot. Since the plank starts tilted about 20° and settles horizontal, the weight shouldn't slide far once things stop.

I'm now tracing world-space coordinates for the weight as the seesaw rotates, checking the top surface position at the wall's x-location (0.76), and finding the wall bottom needs to be set to 0.72 to clear it properly.

Then I check the raised shelf position at 1.3 against the left plank's reach, confirming plenty of clearance with the shelf bottom at 1.25. I compute the fall distance for the weight dropping onto the plank near the pivot, getting a drop of 0.61 and velocity of 3.46, noting the weight is likely a box that lands on a corner as it falls, which should be fine given the bump near the pivot catches the sliding motion.

Checking the cart's max rightward position against the wall boundary confirms no collision there. For the pendulum setup, I verify the bob and cart body spans overlap correctly with the shelf, with the cart bottom clearing the shelf top. I'm also tracking that the cart's joint range allows it to hit its limit while the bob is still moving forward after impact, which should be fine as the bob continues at a reduced speed.

Working through the collision dynamics: the cart moving at ~1.7 m/s travels to hit the weight, then the inelastic collision brings the combined cart+weight to ~0.85 m/s before the cart hits its joint limit and stops, letting the weight continue forward alone. Since the weight's center ends up past the shelf edge, it tips and falls, eventually striking the wall and dropping to land somewhere around x=0.64-0.7.

Actually extending cart travel to 0.34 pushes the weight's center past 0.61, fully clearing the shelf edge so it falls off completely rather than just tipping, carrying roughly the cart's velocity as it goes. I'm now computing the ball's launch position and velocity direction at the moment the pivot stops, working out the world coordinates from the pivot offset and rotation.

Now I'm testing a few launch speeds (2.5, 3.4, 4.2) to trace the ball's parabolic path toward the cup, checking the apex height and where it crosses back down to the rim level, trying to see if it lands inside the cup rather than overshooting or falling short.

Checking the v=4.2 case hitting backboard at z=0.84 confirms it clears the 1.5 height, and for v=2.0 I trace the arc back down to cup floor height, landing around x=1.85. This confirms the cup's interior should span roughly x=1.70 to 2.10 to catch the full range of launch speeds from 2.0 up to 4.2.

Now I'm checking the front wall clearance: launching from x=1.33, z=0.32, the ball passes x=1.68 at z≈0.38 for v=2.0, which clears a rim height of 0.2-0.3 fine. I'm now designing the cup as a physical box container — floor resting on the ground, a short front wall, a tall backboard wall up to z=1.5, and side walls about 0.2m high to keep the ball contained.

Thinking through the ball's behavior once inside: with MuJoCo's default low restitution, after hitting the backboard the ball drops about 0.6m, lands on the cup floor, bounces slightly, then rolls back toward the front wall with residual velocity before settling. I'm estimating rolling friction deceleration using μ_roll*g/r scaled by the standard 5/7 factor for a sphere to figure out how quickly it comes to rest.

Using μ_roll=0.005 gives a deceleration around 1.6 m/s², enough to stop the ball within about a second from 1 m/s, which checks out. Checking the symmetric y-direction setup confirms the ball stays centered at y=0 within the ±0.2 side walls, and I'm verifying backboard contact physics at launch speeds of 2-3 m/s remain low-bounce under the default soft contact parameters. For higher launch speeds like v=5, the apex height still clears the 1.5m backboard comfortably, so trajectories at the top end of the range are fine too.

Now I'm thinking through edge cases: low-v shots that land short of the backboard, whether the ball might slide sideways off the mechanism from seesaw dynamics, and what happens after the weight lands and slides the seesaw toward its pivot — it settles near the bump without affecting the cup. I'm also considering the ball's position when the seesaw hits its lower stop, whether it stays cradled or slides off along the end wall under its own momentum, and how friction and any residual centripetal effects factor into whether it stays in place at that point.

I'm checking whether centripetal contact drops to zero right after release, confirming the ball stays cradled by the arm through the rotation. I also verify the cradle and arm clear the cup's front wall and floor throughout the motion, with the cradle maxing out around x≈1.36 and starting near z≈0.16, and that the pivot support doesn't collide with anything. Finally, I'm working out rotation direction: the weight landing on the left arm pushes it down, decreasing q and driving the seesaw toward its lower limit.

Confirming the lower limit stop is at 0, and that the right arm correspondingly swings upward from -60° toward -40° with velocity directed perpendicular outward at the cradle. I'm also noting the seesaw starts right at its upper limit (q=0.35), so with soft limits it'll settle slightly past that due to compliance, which is fine, and visual stop geoms aren't necessary. I confirm the left plank moves away from the weight-stop wall as q decreases from 0.35 to 0, then start checking the left plank's interaction with other parts.

Checking clearances: the left plank clears the shelf post at both limits, the cup's front wall doesn't interfere with the weight, and the pendulum rod and bob don't strike anything as it swings back and forth after impact. I verify the bob just barely touches the cart at the bottom of its swing when q=0, exactly at the boundary given its radius.

Confirming the cart's bottom clears the shelf top with margin, and there's no interference with the weight-stop wall. All moving bodies share default contact settings, so collisions are handled uniformly.

Now I'm thinking about the optional visual rail for the cart, making it non-colliding so it doesn't interfere with physics, plus a visual support post for the pendulum. For the weight body, I'm setting friction low (0.3) to match the shelf, noting that MuJoCo uses the max friction between contacting pairs, so this keeps things consistent even though it might cause slightly more sliding on the seesaw plank later.

Since the cart fully pushes the weight off the shelf (travel range covers the full 0.34 offset needed), friction mostly stops mattering once the push completes—so I settle on weight friction 0.5 and shelf friction 0.5 as reasonable defaults. I'm now tracing through the geometry of the push: the weight's center crosses the shelf edge partway through the cart's travel, at which point it starts tipping clockwise while the cart continues pushing against its upper-left corner.

I work out the launch conditions—roughly 0.85 m/s horizontal velocity as the weight clears the shelf—then trace the fall: it drops about 0.6 m in 0.35 seconds, which would carry it 0.3 m horizontally without obstruction, but a wall at 0.76 intercepts it first. I calculate that it strikes the wall about 0.1 s into the fall, then continues falling along the wall surface, landing with its center near x=0.70, giving a horizontal torque arm of about 0.30 m.

Computing the angular momentum transfer with J≈1.02 and moment of inertia around 0.10, I get an angular velocity near 7.7 rad/s, which translates to a ball speed around 3.5-3.8 m/s after accounting for gravity's contribution—enough to reach the backboard around 0.75-0.84 m height. I note the idealization of a perfectly inelastic collision isn't fully realistic since the weight hits the plank at an angle and could bounce, but since the impulse happens quickly and the plank is light, the approximation should hold, and the backboard design seems tolerant of a range of impact speeds.

Checking the lower bound of that range, I trace through the trajectory for v≈1.5: the ball would land right at the rim area, marginally hitting the front wall's upper edge around 1.66-1.68. This is a tight margin, so I'm considering shifting the front wall closer, recalculating where the cradle should rest to keep the landing zone comfortably within the target area.

Checking v=1.2 still clears the rim comfortably, so the catch works down to about 1.2 m/s. I'm considering whether to keep the backboard at 2.12 or shrink it to 2.0 for compactness, but checking the v=2.5 case shows it lands around x=2.08.

Going with inner cup face at 2.0, interior spanning x 1.50–2.00, y ±0.2 — essentially a 0.5×0.4 m tray with rolling friction against the walls. Now I'm verifying the starting conditions: gravity should pull the ball into the cradle corner, and the seesaw should rest at its upper limit, so I'm recomputing the torque balance at start including the plank mass and center of mass offset.

The left mass contribution lowers that end (tending to decrease q) while the right-side masses push the opposite way, so I'm tallying each component — plank, bump, arm, end wall, and rails — weighting them by their rotated x-offsets to confirm the net torque keeps the seesaw pinned at the upper limit.

Checking the right-side total against the left confirms it's larger, giving a small but adequate net torque toward the upper stop. The plank mass of 0.06 kg feels physically reasonable for thin wood or plastic, and since MuJoCo derives inertia from the geoms automatically, I don't need to specify it explicitly. I'm now double-checking whether a falling weight landing near x~0.70 on the left plank might instead strike the bump near the pivot instead of the plank itself.

After the weight hits the wall and loses horizontal momentum, it falls and presses the left end of the seesaw down to the lower limit, settling on the plank there — with 1 kg at r=0.3m clearly dominating the torque balance, so the seesaw stays pinned at the lower stop as intended. I'm weighing whether the default limit softness (solref ~0.02) is adequate given the 0.002 timestep, or whether I should stiffen it with a tighter solreflimit to avoid unwanted bounce-through at contact.

I'll set the cart limit's solreflimit to 0.005 too, and check that the weight's torque (~3 Nm) won't cause excessive penetration given the stiff solref. Now I'm setting up the cup body as a fixed structure at the end with floor, walls, and side geoms, making sure the ball's position aligns correctly within it.

I'm wondering whether overlapping static geoms, like the cup floor sitting on the floor plane, even generate contacts — since both bodies are welded to the world with no degrees of freedom, MuJoCo likely skips collision checks between them entirely.

Confirming this filtering logic, I move on to timing: estimating the pendulum swing from its 75° start (~0.45s), the cart's travel to the weight (~0.15s), the push (~0.13s), and the weight's fall (~0.35s), putting the seesaw impact around 1.15s, then continuing to work out the ball's flight time afterward.

Checking what happens after the collision, I realize the bob could rebound off the cart again — after the inelastic impact it's moving at 1.7 m/s and rises to about 36°, putting its max x-position near where the cart is settling at its travel limit, so there's a real chance of a second collision while the cart is still near its stop.

Even with a harder, more elastic bounce, the cart still ends up pinned at its limit and the weight still falls — so that case stays safe. Checking landing positions confirms the weight stays within the plank's bounds whether it lands directly or bounces off the wall first, so there's no scenario where it overshoots toward the cup.

Switching now to verifying the cart's slide joint alignment and the pendulum rod's geometry — the rod's lower end stays clear of the cart at the vertical position, but I need to check contact as the pendulum swings forward.

Even at a 25-degree swing, the rod's lowest point remains above the cart's top surface, so I'll disable collision on the rod anyway for safety by setting contype and conaffinity to 0.

For the keyframe, I'm figuring out qpos ordering based on joint tree order: pendulum hinge, cart slide, weight free joint, seesaw hinge, ball free joint, giving nq=17 total, and now working out the weight's initial position values.

Now I'm computing the weight sitting exactly on the shelf top, setting the seesaw angle, and working through the precise geometry for the ball's position—checking that it rests on the arm surface with proper clearance and sits correctly against the end wall, computing the rotated coordinate components for the final placement.

I double-check the rotation matrix convention for the y-axis hinge and confirm it matches what I derived, then verify the arm box euler angle gives the correct local-to-world direction vector. I also confirm that a positive seesaw angle raises the left end as expected.

Now I'm working through the exact body-frame positions and sizes for the seesaw's component geoms — the plank, bump, arm, and endwall — computing their offsets using the arm's direction and normal vectors so everything fits together correctly within the same body.

For the axle I'll orient it along y with a quarter-turn euler rotation and keep it small-mass with no collision. For the hinge joint I'm setting axis along y with range 0 to 0.35 and light damping, checking that the seesaw's upper limit matches the starting keyframe at 0.35 so there's no soft-limit penetration issue at rest.

I'm placing a visual support box from floor to 0.55 height at x=1.0, offset in y so it doesn't overlap the plank, with no collision. Then I'm positioning a weight-stop wall at x≈0.785-0.81 and checking clearance against the cart's max reach and the plank's bump position at full tilt, confirming about 0.07 clearance, and now I'm working out where the weight actually lands between the shelf edge and the wall once the plank tilts.

Checking the geometry, at a 20° tilt the sliding weight would actually jam against the wall's bottom edge since its top surface exceeds the wall's clearance there — but since the seesaw snaps back toward horizontal quickly, the gap opens to 0.16 which is enough for the 0.12-tall weight to pass, so it should work out as the weight lands while the plank drops. Still, I'll raise the wall's bottom edge to 0.78 as a safety margin and recheck the clearance at the tilted position.

Raising the wall bottom to 0.82 instead, confirming it still catches the falling weight around z≈1.2, within the wall's range of 0.82 to 1.6, with the wall centered at z=1.21 with a half-height of 0.39. I'm also placing a shelf box spanning x from 0.25 to 0.53 with its top at 1.30 and friction 0.5, plus a support post beneath it.

I'm reconsidering the cart rail visual since a capsule there would overlap the shelf, so I'll skip the rail rather than risk collision artifacts, since the cart runs on a slide joint anyway. I'm also adding a non-colliding visual frame for the pendulum support—a post and crossbar set with contype 0 so it doesn't interfere physically. Now I'm defining the ball body using the keyframe position, with a small sphere geom and appropriate mass.

Setting friction coefficients for the ball contact...

