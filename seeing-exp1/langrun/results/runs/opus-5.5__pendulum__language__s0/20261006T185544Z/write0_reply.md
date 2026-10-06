The pendulum's 50 cm arm starts swung back 38°, so the bob reaches about 1.45 m/s at the bottom. There its centre is level with the ball's centre, 5 cm up. The ball leaves rolling at very roughly 1 m/s. The cup has a 12 mm lip that the ball can hop over at that speed but can't climb back out of after it stops against the far wall. The cup's centre is 1 m beyond the ball's start. These figures are hand estimates; I haven't run the scene.

```world
world  pendulum knocks ball into cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.0005

pendulum
  is a               pendulum
  pivot height       55 cm
  length             50 cm
  bob size           4 cm radius
  bob mass           400 g
  rod thickness      1 cm
  rod mass           50 g
  starts swung back  38°

-- bob (4 cm) and ball (5 cm) just touch when the bob hangs straight down; 2 mm gap
ball
  is a      sphere 5 cm radius, 150 g
  rolls
  friction  0.8, spinning 0.005, rolling 0.0005
  colour    orange
  moves     freely
  rests     on floor, 9.2 cm beyond pendulum.pivot

-- a shallow tray with a low near lip: the ball hops over the lip, stops against the far wall,
-- and is too slow to climb back out
cup
  is an             open box
  length            30 cm
  width             24 cm
  walls             10 cm
  wall thickness    2 cm
  base thickness    5 mm
  near wall height  12 mm
  its base 1 m beyond ball

expect
  ball touches pendulum
  ball comes to rest in cup
```

---
thinking (summarized):

I'm thinking through the physics setup for the pendulum, working out how the pivot and bob should be structured and how the hinge connecting them should be named.

Looking at the rotation math, I'm checking that a positive angle about y swings the bob backward so when released it swings forward toward the ball, confirming the setup matches the described motion.

Now I'm sizing things: I need the bob's resting height to align with the ball's center for a clean hit, but also need the bob to clear the floor, so I'm adjusting the ball and bob radii so the bob bottom sits just above ground level while still contacting the ball properly.

I'm also working out placement — how the pivot, rod, and stand arm connect geometrically, figuring out where to anchor the stand arm relative to the pivot so the rod hangs correctly and the bob swings freely into the ball's path.

I'm also considering physics engine details: whether the stand arm and bob body might collide unintentionally, and checking whether MuJoCo's default parent-child contact filtering would prevent that.

For the collision dynamics, I need to figure out how much velocity transfers from pendulum bob to ball on impact, then account for the ball's slide-to-roll transition before it reaches rolling speed. From there I need to make sure the ball has enough energy to travel the full meter and settle into the cup without being blocked by the cup's near wall, since a rolling ball can't climb over an obstacle without ramping.

I'm thinking the cup geometry could work as a very shallow lip instead of a true wall — small enough (a few millimeters) that the ball's radius lets it roll over easily at low speed, rather than bouncing off a tall barrier.

Working through the physics, climbing a step costs velocity via angular momentum conservation about the edge, giving v' ≈ 0.786v for h/r=0.3. Then requiring enough kinetic energy to clear the step height gives a minimum entry speed of about 0.58 m/s.

Though I'm second-guessing the setup: MuJoCo's contact model makes that edge behavior only approximate, and the near wall is really a box corner. I'm wondering if a simpler geometry would be better — maybe no near wall at all, just a dead-stop far wall with rolling friction damping the bounce.

Working through the physics: rolling friction decel comes out around 0.28 m/s² given typical floor coefficients, which is non-trivial over the rollout distance. I'm sketching the sequence — initial post-impact speed reduces to 5/7 of that once slipping ends (assuming no initial spin from a center-height hit), then decays over roughly a meter before reaching the cup's near edge.

Rather than relying on friction to precisely stop the ball inside the cup (too fragile), I'm designing the far wall as a dead-bounce backstop. For the cup geometry I'm settling on a 24x24 cm open box with 8 cm walls, 2 cm wall thickness, 5 mm base, and a shorter 1.5 cm near-wall lip so the ball can roll in without being blocked.

Checking the physics: with h/r=0.2 and r=5cm, the ball needs roughly 0.43 m/s to escape back over the lip once inside, so I want the far-wall rebound speed to stay well below that. For entry I'm aiming for about 1.0 m/s at the lip for margin, which means the far wall needs strong damping (dead bounce) to absorb that energy rather than reflecting it.

Working backward through the rolling-friction deceleration over the ~0.8m approach, I get v0 around 1.7 m/s before slipping transitions to rolling at 5/7 v0 — but the rolling friction coefficient is uncertain enough that I should probably lower it (0.0005 for both ball and floor) to reduce sensitivity, giving a gentler deceleration around 0.07 m/s². I'll set floor friction to 0.8 and work out the spin parameters next.

Now I'm thinking about the pendulum-ball collision itself: with a bob mass of 1 kg versus a lighter ball, the post-collision ball velocity depends on the coefficient of restitution and mass ratio, so a heavier bob should transfer velocity close to (1+e) times the bob's speed, which I need to tune against MuJoCo's default soft-contact behavior.

The relative uncertainty stays about the same either way, so I'll just assume lively bounces on both with e around 0.7–0.9. I also need to account for the rod's mass adding to the effective inertia at the bob, and I'm sketching out a plausible ball size and density to get a reasonable mass estimate.

Working through the numbers with a 4 cm bob, 300 g mass, plus rod inertia, and a 200 g ball, I'm solving for the velocity the bob needs so that the ball ends up moving at the target speed after the collision, accounting for the chosen restitution. I also need to check how the ball's position aligns with the bob's center when the pendulum hangs at rest.

Then I'm picking a pendulum length — say 50 cm below a 55 cm pivot — and using energy conservation to find the swing angle that gives the bob the right speed at the bottom, landing around 35°, while noting the rod's distributed mass will slightly lower that required speed.

Accounting for friction and contact damping, I'm bumping the angle up to about 38°, then recomputing the bob's bottom speed from that angle, and using it to back out the ball's launch speed for a couple restitution coefficients (e=0.8 and e=0.6).

Across these restitution values, even down to e=0.3, the ball has comfortable margin to climb the lip and clear it. The real worry is the opposite case: if it's moving too fast, it climbs the lip, crosses the gap, and hits the far wall — if that's a dead bounce with low restitution, the rebound speed needs to exceed roughly 0.43 m/s to escape back over the lip.

Checking the geometry, the far wall at 8 cm is taller than the ball's contact height, and the side walls are wide enough relative to the ball, so collisions there should behave sensibly without any awkward clipping or edge cases.

I'm also second-guessing whether I actually need the "lively" bounce setting at all — with MuJoCo's default solref parameters the contact is critically damped, which means restitution is essentially zero and the ball wouldn't overshoot on separation anyway.

So maybe the simpler fix is to remove the lip entirely and make the near wall the same height as the base thickness, turning the entry into a flat step. That way the entry threshold works out to roughly v>0.43 m/s, but I realize exiting that same step going downward wouldn't create any barrier at all, which defeats the purpose.

So a lip taller than the base is still necessary for retention, maybe keeping the lip around 1.5 cm with a 0.5 cm base. I also consider alternative shapes like a flat ring, but that doesn't solve the exit problem either — the ball would just roll over the far side.

Really the retention comes down to whether the rebound off the far wall is slow enough to stay below the exit threshold; with a wall coefficient of restitution around 0.5, the rebound speed lands close to that 0.43 m/s cutoff, so it's a near thing.

I realize the rolling spin actually helps here: because the ball keeps spinning forward through the bounce, floor friction after impact drags the rebounding ball back toward rolling motion, which sharply cuts its backward speed — even for a fairly bouncy wall (e=0.8) the final speed only comes out to about 0.25 m/s, safely under threshold. So lively walls might actually be fine too.

I'm hesitant about making the cup "dead" though, since I'm unsure whether bounce/material facts apply cleanly to top-level part objects versus just colored pieces — risky to add and could error, so I'll skip setting bounce on the cup and just make both the bob and ball lively for stronger transfer. But then I start worrying that lively contact at the lip's corner edge could reflect the ball backward instead of letting it roll over, since the corner's normal direction is mostly horizontal at that height-to-radius ratio.

Running the geometry, at h/r=0.3 the normal makes about a 44° angle with horizontal, so a decent chunk of the velocity would reflect straight back or bounce the ball up and over unpredictably. Lowering the lip to h/r=0.2 helps a little (53° angle) but doesn't fully solve it, so I'm now considering redesigning the cup without a lip at all, maybe using a small ramp instead.

The plank thickness and exact contact geometry are getting too ambiguous to model precisely, so I'm abandoning that approach. Instead I'll think about collision materials: giving the ball near-zero restitution against the cup lip so it rolls up smoothly, while making the launching bob heavy relative to the ball (say 1 kg vs 150 g) so I can rely on momentum transfer math to estimate the ball's launch speed.

Depending on how restitution shakes out between the bob and ball, I estimate the ball could leave the lip anywhere from roughly 1 m/s up toward 1.9 m/s -- the higher end risks it hopping airborne over the lip or even sailing past the far wall, which I need to avoid by tuning the restitution and bob mass carefully.

I should probably skip relying on "lively" contact modeling entirely and just use MuJoCo's default near-zero restitution for the ball-bob interaction for robustness, since with critical damping the contact separates once the spring force would go negative, which happens well before any real bounce-back velocity builds up.

The slip phase lasts about 0.055s, but the bob, still near bottom and moving forward, catches up and strikes the ball again during this window, causing multiple impacts that effectively let the bob keep pushing the ball forward. As the bob rises slightly with displacement, it keeps contact until it decelerates, adding extra energy so the ball's final speed ends up somewhere between 0.8 and 1.0 times the bob's velocity rather than cleanly reaching the rolling condition.

I consider whether striking at the "sweet spot" height could avoid slip entirely, but realize for sphere-sphere contact the normal impulse always passes through the ball's center since there's no friction involved in a frictionless collision, so no torque is imparted and the sweet-spot trick doesn't apply here — slip is unavoidable in this geometry.

Working with rolling speed uncertainty in the range 0.55-1.1 times the bob speed, I target a lip speed robust between 0.6 and 2, which pins down a bob speed around 1.45 m/s with L=0.5 and θ≈38.5°, matching what I found before. For masses, I'm leaning toward a moderately heavy bob (500g) against a lighter ball (150g) to keep the push efficient.

Testing bob 400g, ball 150g, rod 50g with restitution 0.15, the collision math gives the bob around 0.70 times v_b while the ball rolls at roughly 0.61 times v_b if no second hit occurs -- since the bob is faster, it catches up for a second collision, pushing the final ball speed to somewhere around 0.65-0.75 times v_b. With v_b=1.45, that lands near 1.0 m/s, comfortably inside the target window.

I'm also checking the geometry: the bob's lowest point sits 1 cm above the floor, clear of the ball, and the pendulum stand's arm height doesn't intersect the ball's rolling path along y=0. I need to verify the rod and stand arm don't collide during the swing, since the stand's left face appears to sit right at the pivot height.

Since the rod is a thin capsule rotating about the pivot and the arm sits just above it, the geometry should clear fine as the simulator handles the contact naturally. I'm also noting that with no damping the pendulum will keep swinging after impact, so I should consider whether it could strike the ball a second time.

For positioning, it's safer to reference the ball relative to the pendulum's pivot rather than its bob, since the bob's position might already reflect the tilted starting angle rather than the neutral layout position.

With a 2mm gap the bob just grazes the ball slightly after passing bottom, so 9.2 cm works fine for that spacing. Now I'm thinking through placing the cup: setting its base 1 m beyond the ball should fix its centre offset along x, but I need to check whether that also constrains its across position or just the forward axis.

Since the cup's base is centred and the walls are centred on the base's edges, the box's overall centre matches the base's centre, with wall thickness straddling the base edges at the ends and sides, and I'm sketching dimensions — 30 cm length, 24 cm width, 10 cm wall height, 2 cm wall thickness — to give the cup enough room.

I'm working out where the ball actually lands: placing the cup's centre 1 m from the ball, the base spans 0.85–1.15 m, with the near wall around 0.84–0.86 m and the far wall's inner face at 1.14 m. Tracing the ball's travel, it would stop near x≈0.8–1.09 m depending on which wall it hits, landing roughly 9 cm inside the cup's centre — which seems to satisfy resting "in" the cup, assuming that means within the inner wall bounds. I'm also double-checking whether the near wall's 1.5 cm height compares properly against the base's thickness.

Now I'm also verifying the side walls (10 cm tall, 30 cm long, centered on the base's left side) and testing whether the ball can clear the lip at different speeds — at v=1.0 the rebound velocity comfortably exceeds the threshold to climb over, but at the slower end (v≈0.65) it's only marginally enough, so I'm considering lowering the lip height to 1.2 cm to give more margin, which drops the needed exit velocity and keeps even slower rolls able to climb over.

Settling on a near wall height of 1.2 cm and base thickness of 5 mm, with the ball traveling about a meter in roughly 1-1.5 seconds, well within the 6-second window, and symmetric in y so no lateral deviation to worry about. For the pendulum, I'm setting pivot height at 55 cm, rod length 50 cm, bob radius 4 cm and mass 400 g, rod thickness 1 cm and mass 50 g, starting swung back 38 degrees.

Confirming that positive rotation about the y-axis correctly pulls the bob backward behind the pivot, matching the "swung back" description. I'm also settling on naming conventions for the pendulum parts and pivot joint, and starting to configure floor friction properties.

For contact expectations, I'll phrase it as "ball touches pendulum" and "ball comes to rest in cup" rather than risking an incorrect part-reference syntax. I'll skip air resistance facts and keep coloring minimal, maybe just the ball, since part-level color facts seem uncertain for the cup.

Setting ball color to orange and rod mass to 50g with default damping, then finalizing the scene.

