

---
thinking (summarized):

Since I can't actually simulate physics, I need to reason carefully about the geometry to design a working Rube Goldberg chain in MuJoCo. I'm working through the pendulum setup, figuring out the arm length and pivot height needed so the bob drops 0.6 meters before striking the next element.

Then the bob hits a cart on a slide rail with velocity ~3.43 m/s, pushing a weight off a ledge so it falls onto one end of a seesaw. The seesaw's opposite end holds a ball, and the falling weight drives that end down to launch the ball toward the cup. I'm trying to make each handoff as deterministic as possible, with enough margin for error, since predicting exact trajectories without simulation is risky and the ball needs to land and stay in the cup.

At θ=π/2 the bob sits horizontal at x=-0.6 relative to pivot, so starting qpos=1.5708 lets it swing down 0.6m and strike the cart moving in +x. I'm placing the cart so its left face sits just past the bob's lowest point with a small gap, and now I'm working through the momentum transfer between bob mass and cart mass at impact.

With a 1kg bob and 0.5kg cart, elastic collision math gives the cart a velocity around 4+ m/s, which seems too fast and would launch the weight too far. I should add damping to the cart or have it hit a stop after a short travel distance so the weight gets a controlled launch instead of flying off.

I'm reconsidering mass ratios to tame the uncertainty—maybe make the cart heavier (2kg vs 1kg bob) and add slide damping so collision velocities land in a more predictable, moderate range.

I'm estimating the weight's projectile fall after leaving the edge — roughly 0.25s fall time giving maybe 0.12–0.5m horizontal travel depending on speed uncertainty. I'm considering whether a wide catching tray at the seesaw end would tolerate that range, or whether positioning the shelf edge directly above the seesaw end could minimize horizontal drift so the weight falls nearly straight down instead.

Then the ball launches off the low end once the seesaw snaps to its stop, but the ball's exit velocity depends unpredictably on the impact torque from the falling weight, so catching it reliably is tricky. I'm thinking a large catching cup near the ball's launch point could absorb that uncertainty, sized generously relative to the ball so the range of plausible trajectories still lands inside it.

Working through the geometry, I place the weight end at +x and ball end at −x on the seesaw arm, then differentiate the ball's position to find its velocity direction as the arm rotates. At the stopping angle, the velocity points back toward the pivot and weight side, which means the ball would be thrown backward over the fulcrum rather than forward — I need to reconsider which configuration actually launches it outward.

Placing a cup at the launch point doesn't make sense since the seesaw occupies that spot. If the arm stops near −5° instead of horizontal, the ball's velocity tilts slightly outward, giving a shallow near-vertical trajectory—around 0.07 m of horizontal drift for v=2 m/s. I'll just accept some uncertainty here and design for a moderate arc with a sufficiently wide cup, rather than trying to pin down the exact landing spot analytically.

Actually, a better approach: if the weight drops into a small pocket/tray at the seesaw's end rather than bouncing unpredictably, the impact becomes mostly inelastic and vertical, so the impulse imparted to the seesaw depends predictably on drop height via v=√(2gh). Gravity torque then takes over, making the rotation speed at the stop fairly estimable, though contact dynamics in MuJoCo still leave roughly ±20% error in my hand calculations.

The ball may stay in contact during impact but it's held in a holder, so that's fine. I'm reconsidering whether to make the launch simpler — maybe the ball should just be thrown into the cup, built as a square container from a base box and four wall geoms grouped as one body, deep enough that MuJoCo's non-bouncy contacts let it settle without popping out.

I'm also exploring whether a near-vertical throw reduces horizontal sensitivity: the seesaw end stays up after the weight hits its stop, and the ball launches nearly straight up with a slight tilt, landing back near its start. The horizontal range still scales with v² sin(2β)/g, so even with velocity uncertainty, a small tilt angle keeps the displacement small and more predictable.

Since range sensitivity is proportional regardless of angle, a smaller mean range actually gives a smaller absolute spread, so I'm leaning toward a short, low throw with a cup sized around 0.3 m to catch the ball — but I need to make sure the ball clears the cup wall and the seesaw's own end as it launches.

I also need to check the tilt geometry: with the ball end elevated negatively at stop (say -15° with β=15°), the weight end swings between +35° and +15°, giving a 20° swing range, which seems workable as a limiting stop for the downward travel.

Actually, raising the ball on a small post changes the velocity direction more favorably—if the arm is horizontal at stop but the ball sits elevated above the arm on a post, the pivot-to-ball vector tilts upward, which tilts the launch velocity outward even more. With a post height of 0.1 at radius 0.4, that's about a 14° outward tilt, letting the seesaw motion be nearly symmetric: starting the ball end at -20° and stopping at horizontal (0°), with the ball resting in a small elevated cup holder at the end.

But then I need to check whether the ball actually clears the holder cleanly when it stops—the holder's outer wall could clip the ball if it's moving outward as it leaves, so a shallow pad with a low outer lip (versus a deep cup) seems safer to let the ball roll off without catching.

Checking geometry at the lip edge: the contact normal points from the edge to the ball center, roughly 50° from vertical inward, while the ball's velocity is tilted only 14° outward from vertical. Comparing these directions shows the velocity has a positive component along the normal, meaning the ball moves away from the lip and separates cleanly.

Now I'm sketching the seesaw's physical layout: pivot height, arm lengths (0.3 m to the weight tray, 0.4 m to the ball), a light plank, and a heavier weight mass to drive the motion.

Let me work out the ball mass (0.02 kg, radius 0.02), plank dimensions and mass (0.2 kg), and where the tray walls on the weight end need to sit so they actually catch the falling weight given its horizontal velocity component.

Now I'm turning to the cart-pendulum collision: a 1 kg bob at 3.43 m/s hitting a 1 kg cart, using MuJoCo's soft contact model with critical damping to approximate a near-inelastic but slightly bouncy collision.

I also need to account for the pendulum's constraint — the bob's effective mass at the impact point is roughly I/L² ≈ 1 kg, not the full bob mass. With equal masses and e≈0.135, the cart ends up at about 1.95 m/s and the bob at 1.48 m/s, so they separate cleanly as the bob swings up and decelerates under gravity while the cart continues at roughly constant speed. Since I want a more moderate cart speed, I should try increasing the cart mass to around 2 kg.

With a 2 kg cart, the post-collision speeds come out to about 1.3 m/s for the cart and 0.83 m/s for the bob, which keeps the bob trailing and decelerating while the cart carries a steady 1.3 m/s with no damping (joint, no surface contact). I'll keep the travel distance from cart to weight short to avoid damping uncertainty, then have the 2 kg cart strike a 1 kg weight resting on a shelf and work out that collision's outcome.

Now I'm worried about the shelf's friction default of 1.0 being too high, since that would decelerate the weight almost instantly and let the cart catch back up and shove it again. Since MuJoCo takes the max of the two contacting surfaces' friction coefficients, I'll try lowering both the weight's and shelf's friction values to around 0.2 to get smoother sliding behavior.

A cleaner alternative occurs to me: use a sphere instead of a box as the weight, so it rolls off the shelf edge predictably instead of tipping over with messy rotations. With condim 3 and default zero rolling friction, the sphere would mostly slide-then-roll with some energy loss during that transition when the cart hits it.

But I realize the cart would keep chasing and repushing the sphere unless I constrain its motion—maybe give the cart's slide joint a range limit so it stops shortly after the initial impact, letting the sphere roll off on its own afterward.

Actually, maybe simpler to skip the cart and just use a fixed shelf geom at some height where the sphere rests near an edge, rolling off at roughly 0.7 m/s and falling to the tray below with some horizontal landing distance. I still need to work out how the cart track and shelf height relate geometrically.

I'm placing the cart and sphere heights so contact normals stay horizontal, then checking whether the bob's post-impact swing (max ~20°, reaching x≈0.2) could catch up and re-hit the cart, since the cart moves away faster at 1.3 m/s versus the bob's 0.83 m/s.

I'm adjusting the cart's travel limit and the weight's position so the cart hits the sphere first, then the stop limit, while keeping the bob's small rise harmless and avoiding a second unwanted collision.

As the sphere transitions from sliding to rolling it decelerates below the cart's speed, so the cart catches up and pushes again before hitting its travel limit of 0.08. Working through the extra push, I estimate the sphere ends up somewhere around 0.6-0.85 m/s, roughly matching the cart's speed since there's no torque from a center push.

Then the sphere rolls across the shelf toward the edge at about 0.7 m/s over roughly 0.155 m, taking around 0.2 s. Checking whether it leaves the edge cleanly: since v²/r (12.25) exceeds g, the sphere loses contact with the edge immediately rather than rotating around it, giving a clean projectile launch from the shelf height.

Now I'm working out where the sphere lands on the seesaw tray, choosing a drop height of about 0.12 m so the fall takes roughly 0.156 s, giving a horizontal travel near 0.11 m and a landing position around x≈0.51±0.025, with a vertical impact speed of about 1.53 m/s.

I'm checking whether this conflicts with the shelf geometry — the shelf edge sits at x=0.40 and extends down to the floor, so the seesaw's weight-end tray needs to sit past that boundary. I need to figure out the pivot location, since the tray surface is initially only about 0.025 m above the floor, which may not leave enough room for the weight end to swing down properly.

I decide to raise everything by adding height to the base: shifting the pendulum pivot, bob, cart, shelf, and sphere positions all upward so there's adequate floor clearance. Then for the seesaw, I'm working out the pivot height and arm length so the weight end goes from roughly +15° down to a horizontal stop at 0°, while the ball end moves from −θ0 up to meet it at 0° as well.

The ball end sits further in the +x direction (outward from the weight end), so a ball launched outward clears the chain mechanism fine. Initially the ball side must rest down against a stop since it's unloaded and the arm is longer there, making it heavier before the weight is added.

Working through the hinge rotation math: with the hinge about the y-axis, positive rotation raises the weight end since it sits at −x. So the initial qpos should be +0.349 radians (20°), settling toward 0 as the mechanism moves, with a lower stop defining the limit.

I'm weighing whether to use a physical stop block or a joint range limit to enforce the lower stop — a solid geom contacting at θ=0 feels more explicit than relying on joint limits alone, though it risks slight penetration if contact is soft. I'll go with physical stop blocks for both ends and keep the joint range generous as a backup.

I'll keep the lower stop physical and use the joint range for the upper limit, with a small negative margin on the lower bound for safety. For the ball holder, I'm positioning the ball slightly elevated above the plank at the seesaw end, which tilts its launch angle about 11 degrees from vertical — though I'm reconsidering whether that gives enough horizontal reach to clear the seesaw and land in the cup.

I'm weighing whether to increase the launch angle further, maybe by raising the post height or adjusting the stop angles at each end so the combined tilt pushes the trajectory outward enough, before settling on exact numbers I need to work out the launch velocity from the seesaw dynamics with the weight ball landing in its tray.

Now I'm sketching concrete numbers: tray and ball distances from pivot, plank dimensions and mass distribution favoring the ball side, and placing small tray walls to catch the landing weight, with a post supporting the ball holder.

Running torque balance: before the weight lands, the ball side wins by about 0.018 N·m, holding the plank stable; after the weight drops in, it flips hard to about 2.27 N·m on the weight side. Now I'm working out the moment of inertia of the plank and components about the pivot to see how fast it will swing.

Working out ω0 ≈ 4.26 rad/s from the angular momentum transfer at impact, accounting for the weight's partial bounce. Then applying gravity's torque over the remaining 0.36 rad swing gives ω² ≈ 37.5, so ω ≈ 6.1 rad/s, which I'll use to get the ball's speed at radius r.

I'm estimating the ball speed at around 2.5 m/s, then checking the launch trajectory at 11° from vertical: computing the rise height (~0.31m), horizontal velocity component (~0.48 m/s), and the flight time back to launch height (~0.5s), giving a horizontal range of roughly 0.19-0.30m depending on speed variation, plus some additional descent to reach the cup. I'm checking this range against the cup's inner width and making sure the cup placement clears the seesaw mechanism.

Now I'm working out the ball's exact landing position relative to the pivot point, factoring in the seesaw's stopped angle and the extra travel if the cup rim sits below launch height, while confirming the ball clears the near wall of the cup given its trajectory.

Checking the range further: v=1.8 gives landing offset ~0.14, v=3.2 gives ~0.41, so the viable velocity window spans roughly 1.6 to 3.2 to land within the cup's inner radius of 0.10 to 0.42. The cup itself is about 0.32m wide with generous lateral tolerance, so I just need to make sure the walls are tall enough to catch the ball properly.

With low restitution on the cup floor, the ball should land with minimal bounce once it hits bottom, but since rolling friction is zero in condim 3, it might roll around and bounce off the walls a few times before settling, losing energy each hit from the restitution. That should still settle within a couple seconds, but I could tighten it up by giving the ball geom a higher condim value with rolling friction to help it stop faster.

I don't think the holder stop will bounce much given low restitution, and the weight sphere separates cleanly from the ball at the moment of impact since the ball keeps moving upward while the holder decelerates fast. I need to double check the tray geometry holds the weight sphere in place on the arm — with mass 1 kg and radius around 0.04, I should verify the shelf dimensions are sized correctly to keep it from rolling off.

Rotating the ball's position vector by the tilt angle θ=0.36 to find where it rests against the lip, I get coordinates around (0.402, -0.066), confirming the ball stays against the outer edge in that tilted equilibrium state before the fast seesaw motion begins.

The impulsive jolt at impact presses the ball into the pad along its normal, so centripetal effects stay negligible and the ball holds in place as the seesaw jumps rapidly from rest to its spin rate. Now I need to work out the tray geometry in the plank's body frame to check whether the landing weight actually stays in the tray or risks bouncing out, starting with the tray center position and plank thickness relative to the pivot axis.

Checking the tray bounds: walls span roughly 0.14 m with a 0.04 m height, and comparing that against the sphere's 0.04 m radius suggests the wall is just barely tall enough to contain the sphere if it lands within about a 0.12 m window — otherwise it clips the wall top. I still need to see how this window shifts once the plank is tilted by angle θ rather than sitting flat.

I'll shorten the tray so the resting position is well-defined, with the sphere settling against the inner wall around r≈0.23. Working out world coordinates, the tray surface center sits near (Xp−0.230, Hp+0.097), and I need the sphere's landing position to align with the desired target near x≈0.51, accounting for the tilt when converting surface position to sphere center.

Solving for pivot placement, I get Xp=0.74 and Hp=0.325 so the tray center lines up at the landing point, then I check the seesaw ball-holder position at the stop to confirm it matches the expected geometry.

Now I'm positioning a stop block beneath the weight end of the plank — placing it at roughly x=0.45–0.46 so its top sits at z=0.315, keeping it clear of the shelf edge at x=0.40 while small enough (half-width 0.03) to act as a pillar support.

I'm checking whether the shelf interferes with the plank's rotation: at θ=0.36 the plank end lands around x=0.44, z=0.44, well clear of the shelf which tops out at x=0.40. I'm now working through the tray's left wall position under the same rotation to see where it lands.

I'm also verifying that the sphere rolling off the shelf edge clears the tray wall — at x=0.46, with the sphere dropping due to gravity over its travel time, its bottom stays above the wall's top height even at a slower rolling speed, so the clearance checks out.

Since the tray slopes toward the inner (right) wall anyway, I realize the outer left wall barely matters for catching the sphere — it just needs to be low or can essentially be omitted, since the sphere naturally rolls toward the inner wall once it lands.

Now I'm working out the landing position: the sphere leaves the edge around x≈0.40 and I need to find where its parabolic trajectory intersects the sloped tray surface, factoring in the tray's z-slope relative to x and solving for the time when the sphere's center reaches the surface plus its radius offset.

Continuing with v=0.9, I get x≈0.549, so landing positions range roughly between 0.474 and 0.549 across these velocities. Now I'm checking where the tray surface actually spans in world coordinates, converting from body-frame x values, so I can see if the sphere center lands within that range and figure out how the contact normal is tilted given the surface's rising slope toward negative x.

I should reposition the tray so the nominal landing sits centrally with more margin — shifting it to span body x −0.36 to −0.19 with the expected contact around −0.27.

I'm also second-guessing how much uncertainty there really is in the cart and sphere speeds, since the pendulum bob's impact velocity and the bob-cart restitution could vary more than I assumed given MuJoCo's soft contact parameters and timestep.

Tracing through the chain — cart reaching ~1.3 then transferring momentum to the sphere through friction and catch-up collisions — the final sphere speed could land anywhere from 0.7 to 0.85, which is messy to pin down exactly. I'm weighing whether stopping the cart right at impact via a joint limit would simplify things, but that's still a soft collision that would decelerate it unpredictably while in contact with the sphere. Another option is just shrinking the drop so landing spread stays small regardless of velocity uncertainty, since spread scales with velocity error times flight time.

There's also uncertainty from the impact itself—whether the sphere bounces in the tray—giving a range of final angular velocities around 5–6.8, so ball speed lands somewhere between 2.0–2.8, cup covering 1.6–3.2. I also need to account for the weight shifting position in the tray as it tilts, changing its effective radius and torque, and for whether the tray could separate from the weight mid-swing if its downward acceleration exceeds gravity.

Checking the numbers, the tray's acceleration at that radius comes out below g, so it stays in contact—but comparing velocities right after impact, the tray moves slower than the sphere initially, which means in an inelastic sense they should quickly equalize to a shared velocity near 1.0 m/s, consistent with treating this as a simple inelastic collision. I should also verify whether the seesaw starts held at its upper limit before release.

Working through the full timing chain: pendulum swing from horizontal takes about 0.46 s using the quarter-period formula for large amplitude, then cart and sphere rolling adds roughly 0.2 s, falling 0.16 s, seesaw tipping 0.1 s, and ball flight 0.5 s—putting the ball in the cup around 1.5 s total, with about 4.5 s more for everything to settle. Now I need to work out the cup's placement based on where the ball launches from.

Figuring out the ball's resting position and support geometry... I'm sizing the ball at radius 0.02 sitting on a pad, then building the post and pad as boxes with specific heights so the pad top sits right under the ball center at z=0.08.

I'm placing an outer lip box at the edge of the pad to stop the ball from rolling off, then working out where the ball's center lands when resting against that lip given its radius.

I'm working out the contact normal direction at the lip edge, which points mostly inward at about 66° from vertical, so the ball gets supported by both the pad's normal force and the edge contact, keeping it stable — and I'm confirming MuJoCo's box-sphere contact handles this edge case correctly.

Checking the ball's launch velocity, I find it's tilted 11.1° outward from vertical based on the geometry, and the angle between velocity and the contact normal comes out to 77°, which is under 90° — meaning the ball is indeed separating from the lip as expected. I'm also considering the centrifugal force during rotation, which pushes the ball outward with significant acceleration near the end of the motion, and comparing that outward radial direction against the lip edge's normal vector to see whether the edge can still contain the ball under that load.

That upward lip force also pushes the ball slightly away from the pad, but checking the net body-frame balance—gravity's component, the Euler pressing effect from angular acceleration, and the centrifugal upward component—the total still comes out negative, meaning the ball stays pressed against the pad even as ω grows toward the end.

Considering whether a taller lip is safer, I realize a taller lip makes the contact normal more horizontal, which affects the separation angle at launch. Testing lip height 0.015 gives a normal angle of about 76°, which is marginal, so I'll keep the lip at 0.012 for a safer 66° angle, and I need to also account for the ball contacting both the pad and the lip simultaneously.

At launch the ball also needs positive separation from the pad, and checking the lip exit angle gives roughly 77° between velocity and normal, which keeps a positive separation rate as the ball rises. I'm also considering the stop block geometry under the weight end of the plank, checking where it contacts relative to the pivot.

Now I'm laying out the seesaw body geometry: the plank box, an inner tray wall acting as a stop for the weight, and side rails — working through the center positions and half-extents for each piece.

For the pivot, I'll make the visual axle and stand world geoms non-colliding (contype/conaffinity set to 0) so they don't interfere with the seesaw's physical contacts, and I'll assign small masses directly via the mass attribute on each geom.

Checking the torque balance at qpos=0.36: summing each component's contribution (plank, inner wall, rails, post, pad, lip, ball) gives a net positive value around 0.0159, meaning the ball side is heavier and should rotate downward — confirming the expected tipping direction.

Now I'm working out where the tray surface sits in world coordinates once tilted to θ0=0.36 radians, converting the body-frame tray point to world x and z using the rotation's cosine and sine components, so I can locate where the weight ends up resting against the inner wall.

Then I'm figuring out the target landing spot for the sphere — somewhere between body x −0.36 and −0.19 — accounting for the sphere's radius so its center can't get too close to the wall, and back-solving for the tray position (Xp, Hp) that makes the v=0.7 launch trajectory land right at that point.

Trying v=0.7, picking a landing drop of about 0.12 gives Z=0.465 at X≈0.509, so Xp≈0.75, Hp≈0.32. I'm then setting up the equation for the surface center line and plugging the projectile trajectory into it to solve for a consistent time t where the ball lands on the tilted surface.

Solving the quadratic for v=0.7 gives t≈0.157, landing at X≈0.510 with x_b≈−0.275, which checks out against the surface equation. Then I try v=0.4, solving the corresponding quadratic to get t≈0.144, landing at X≈0.458 with x_b≈−0.331.

I realize that since the surface normal in the body frame is purely along z, the contact point's x_b coordinate equals the sphere center's x_b directly, simplifying things. Checking v=0.4 again confirms it lands at x_b≈−0.331, just within the plank's end at −0.36. Testing v=0.3 similarly gives x_b≈−0.348, barely on the plank, and I'm now moving to check v=1.0.

For v=1.0, I calculate x_b≈−0.209, which is close to the inner wall (wall face around −0.19 to −0.18, with its top at body z 0.05). Since the sphere radius is 0.04 and the horizontal gap is only about 0.019, the sphere would likely strike the wall's top edge rather than clearing it, which means the contact there could deflect it back into the tray instead of over the wall.

Checking v=0.9 similarly gives x_b≈−0.232, landing safely. So the viable launch speed range seems to be roughly 0.3 to 0.95.

I also need to account for whether the sphere immediately departs the edge or pivots around it first — departure requires v²>gr, meaning v>0.63; below that threshold it rotates slightly before leaving, gaining extra velocity but landing at roughly the same spot. I should also verify the sphere's fall trajectory doesn't clip any other geometry on the way down.

Checking clearance against the tray's side rails and the plank's end position, the sphere passes well above both. Now I'm working out the shelf's location and dimensions to make sure the cart can slide freely above it.

Cart bottom clears shelf top by 5mm as intended. Checking the cart's x-position relative to the shelf edge and confirming the bob's swing clears the cart face with minimal angle needed. Now I'm positioning the sphere's resting location on the shelf relative to the cart's right face with a small gap.

Working through contact timing: the cart pushes the sphere at its slide limit of 0.10, and the sphere moves beyond the cart's reach before the cart stops. I'm verifying the vertical overlap between the cart face and the sphere's center is consistent with contact. Then I'm tracking whether the bob's forward swing after impact could later collide with the stopped cart, computing the bob's post-impact velocity and swing angle to find its new x,z position and comparing it against the cart's left face location.

Checking the cart-sphere-cart collision outcome: estimating post-collision speeds using momentum conservation for a 2 kg cart hitting a 1 kg sphere, then working out how friction with the shelf would spin up the sphere toward rolling motion, computing the time to reach the rolling velocity of 5/7 of its initial speed.

Computing the gap, I find it's slightly positive (~0.0009), so the cart catches up and hits the sphere again almost immediately. This second collision is trickier since the sphere is now rolling, but the cart keeps pushing until it hits its travel limit at qpos 0.10, leaving the sphere somewhere around 0.75-0.8 while the cart stops short.

I'm also checking whether MuJoCo's default contact model could behave more elastically than I assumed — a fully elastic case would push the cart and sphere speeds well beyond my estimates, but MuJoCo's defaults are typically quite inelastic, so I'm fairly confident in the lower bound. I'm also factoring in the pendulum bob's mass versus a lighter arm, and considering that contact happens slightly before the pendulum reaches true bottom, which reduces sensitivity further.

I'm weighing whether adding cart damping would actually help, but it probably won't change the sphere's resulting speed much. A cleaner fix might be limiting the cart's travel so it stops right after contact, concentrating the transfer into one clean push — though that's a partial solution. I'm also considering a more robust design where the sphere's speed comes from rolling down an incline after being knocked off a ledge, but that feels like overkill given the current 0.3–0.95 range already works reasonably well. My main worry is whether a sphere speed around 1.2 would send it too far, hitting the inner wall or bouncing back out of the tray, so I'm running the numbers to check where it would land in that case.

I should factor in the pendulum arm mass too—adding the capsule's inertia barely nudges the effective mass up to about 1.017, so that's negligible. Landing speed around 0.65 puts the ball at roughly x=−0.28, and as it rolls to the inner wall near −0.23 I need to recompute the seesaw's moment of inertia, summing contributions from the plank, inner wall, and rails to get the final angular velocity.

Adding in the post, pad, lip, and ball contributions brings total seesaw inertia to about 0.0203, plus the sphere's own rolling inertia if it moves with the plank. Now I'm working out the angular momentum at impact using the sphere's velocity components and its position relative to the pivot at landing.

Converting coordinates to world frame, I compute L_y = z·vx − x·vz, getting a negative value, which makes sense since it should decrease θ and lower the weighted end. I'm now isolating only the component of this angular momentum normal to the tray surface, since that's what actually transfers through contact, by projecting onto the tray's rotated normal direction.

I find the normal velocity component is about -1.21 and the tangential component (down the slope toward the wall) is about 1.15. Treating the seesaw's effective mass at the contact point as I_s/x_b² ≈ 0.259 kg and the sphere as 1 kg, I'm computing an inelastic collision along the normal direction to get the resulting common velocity.

That gives a seesaw angular velocity of roughly 3.43 rad/s, though the friction impulse's tangential torque contribution looks small given the short lever arm. Then I'm considering how the sphere, now moving down-slope at about 1 m/s, hits the wall at the given radius, and whether the resulting wall-impact torque (with a small lever arm of about 0.05) adds to or opposes the rotation — it looks like it slightly works against it, but the effect is minor.

Working through the gravity torque at the wall contact radius gives about 2.1 N·m, and with total moment of inertia near 0.076, the angular acceleration comes out to roughly 27.6 rad/s². Accounting for the sphere sliding inward conserving angular momentum bumps the starting angular velocity up to around 4 rad/s, and integrating over the angle change gives ω² ≈ 35.

I get ω around 6, putting the ball's launch speed near 2.5 m/s, consistent with my earlier estimate in the 2-3 m/s range. I check the timing: the seesaw rotation takes about 0.07s while the sphere rolls its 0.05m in about 0.05s, so the two processes are roughly synced. Then I work out the ball's launch position in world coordinates, around (1.159, 0.40), with velocity direction about 11° from vertical, and start thinking about how the stop's soft contact affects the impact.

After separation, I note the seesaw rebounds slightly with restitution around 0.13, sending the weight end back up while the ball is already gone. I then compute the ball's trajectory components, vx≈0.481 and vz≈2.453, and start placing the cup to figure out landing — trying a cup rim around z=0.30 with some depth for the wall and floor.

I check when the ball's center clears the rim height (0.32m) for different launch speeds, solving the quadratic for time and getting x-crossing points around 1.41 for v=2.5 and a similar calculation underway for v=2.0.

Checking whether the ball's trajectory clears the cup's inner walls near x=1.25 to 1.60 — testing offsets and heights for different velocities to confirm the ball rises high enough above the rim height of 0.32 before reaching the near wall.

I'm also checking whether the seesaw's plank end and lip (near x=1.19) might collide with the cup's near wall at x=1.24, both at rest and when tilted — computing the plank end's actual position using the tilt angle to verify adequate clearance.

Now I'm redesigning the cup geometry, placing its base flush with the floor and giving it 0.28m deep walls, and checking that with the ball falling roughly 0.7m and bouncing with 13% restitution, the resulting bounce height stays comfortably inside the cup.

Checking the ball's y-drift stays near zero by symmetry, then verifying the trajectory clears the near wall's top corner with enough margin as it crosses into the cup. That geometry looks fine, so now I'm working out where the stop block sits under the weight end relative to the plank's bottom face.

I'm placing the stop block at world x 0.415–0.455 so it clears the shelf edge at 0.40, with its top aligned to the plank's resting height, and giving it a y-size of 0.05 to match the contact region under the weight.

For the pivot stand, I'm making it purely visual by setting contype 0 so it doesn't collide with the plank as it rotates, and extending it from the floor up to just below the plank's underside near the pivot. I'm also disabling collisions on the hinge axle cylinder (contype/conaffinity 0) since it doesn't need to interact with anything physically.

Now I'm adding a visual support frame for the pendulum at the pivot point, with a post offset in y so it doesn't intersect the swinging bob, plus a crossbeam — also non-colliding. Then I'm defining the pendulum body itself at the pivot position with a hinge joint along the y-axis.

