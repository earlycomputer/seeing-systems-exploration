The pendulum's bob has the same mass as each ball, and the ball-to-ball contacts are springy, so most of the impact momentum passes down the chain to ball4. I haven't run this, so the numbers below are hand estimates, not results.

- **Release:** the bob starts level with its pivot, which puts it 0.5 m above its lowest point.
- **Rail:** the rail has low sliding friction plus some rolling friction. Balls 1–3 should keep only a little leftover drift after passing the impact on, and should stop on the rail.
- **Box:** ball4 leaves the rail end at about 2.5 m/s and drops into the box. High friction and rolling friction there should bring it to rest.

```xml
<mujoco model="pendulum_ball_chain">
  <option timestep="0.002"/>
  <worldbody>
    <light name="main_light" pos="0.5 -1 2" dir="0 0.5 -1"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="pendulum" pos="0 0 0.625">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 -0.5 0 0" size="0.004" mass="0.001" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
      <geom name="pendulum_bob" type="sphere" pos="-0.5 0 0" size="0.025" mass="0.1" rgba="0.8 0.2 0.2 1"/>
    </body>

    <body name="rail" pos="0.325 0 0">
      <geom name="rail_base" type="box" size="0.375 0.03 0.05" pos="0 0 0.05" condim="6" friction="0.05 0.005 0.003" rgba="0.4 0.4 0.5 1"/>
      <geom name="rail_guide_left" type="box" size="0.375 0.003 0.0075" pos="0 0.033 0.1075" condim="6" friction="0.05 0.005 0.003" rgba="0.4 0.4 0.5 1"/>
      <geom name="rail_guide_right" type="box" size="0.375 0.003 0.0075" pos="0 -0.033 0.1075" condim="6" friction="0.05 0.005 0.003" rgba="0.4 0.4 0.5 1"/>
    </body>

    <body name="ball1" pos="0.0505 0 0.125">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.025" mass="0.1" friction="0.05 0.005 0.003" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="ball2" pos="0.2005 0 0.125">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.025" mass="0.1" friction="0.05 0.005 0.003" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="ball3" pos="0.3505 0 0.125">
      <freejoint name="ball3_free"/>
      <geom name="ball3_geom" type="sphere" size="0.025" mass="0.1" friction="0.05 0.005 0.003" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="ball4" pos="0.5005 0 0.125">
      <freejoint name="ball4_free"/>
      <geom name="ball4_geom" type="sphere" size="0.025" mass="0.1" friction="0.05 0.005 0.003" rgba="0.9 0.7 0.1 1"/>
    </body>

    <body name="box" pos="1.07 0 0">
      <geom name="box_floor" type="box" size="0.36 0.16 0.005" pos="0 0 0.005" condim="6" friction="1 0.02 0.03" rgba="0.5 0.35 0.2 1"/>
      <geom name="box_front" type="box" size="0.01 0.16 0.03" pos="-0.34 0 0.03" condim="6" friction="1 0.02 0.03" rgba="0.5 0.35 0.2 1"/>
      <geom name="box_back" type="box" size="0.01 0.16 0.1" pos="0.34 0 0.1" condim="6" friction="1 0.02 0.03" rgba="0.5 0.35 0.2 1"/>
      <geom name="box_left" type="box" size="0.36 0.01 0.05" pos="0 0.15 0.05" condim="6" friction="1 0.02 0.03" rgba="0.5 0.35 0.2 1"/>
      <geom name="box_right" type="box" size="0.36 0.01 0.05" pos="0 -0.15 0.05" condim="6" friction="1 0.02 0.03" rgba="0.5 0.35 0.2 1"/>
    </body>
  </worldbody>

  <contact>
    <exclude name="ex_pend_rail" body1="pendulum" body2="rail"/>
    <exclude name="ex_pend_b1" body1="pendulum" body2="ball1"/>
    <exclude name="ex_b1_b2" body1="ball1" body2="ball2"/>
    <exclude name="ex_b2_b3" body1="ball2" body2="ball3"/>
    <exclude name="ex_b3_b4" body1="ball3" body2="ball4"/>
    <pair name="pair_pend_b1" geom1="pendulum_bob" geom2="ball1_geom" condim="1" solref="-60000 -8" solimp="0.95 0.95 0.001"/>
    <pair name="pair_b1_b2" geom1="ball1_geom" geom2="ball2_geom" condim="1" solref="-60000 -8" solimp="0.95 0.95 0.001"/>
    <pair name="pair_b2_b3" geom1="ball2_geom" geom2="ball3_geom" condim="1" solref="-60000 -8" solimp="0.95 0.95 0.001"/>
    <pair name="pair_b3_b4" geom1="ball3_geom" geom2="ball4_geom" condim="1" solref="-60000 -8" solimp="0.95 0.95 0.001"/>
  </contact>
</mujoco>
```

---
thinking (summarized):

I'm working out the physics of a Newton's cradle setup on a rail, calculating how a pendulum released from 0.5m height transfers velocity through the chain to the final ball so it rolls into a box.

The tricky part is MuJoCo's default contact behavior is fairly inelastic (critically damped), which would make balls clump together and share momentum rather than cleanly transferring it like a real Newton's cradle. I'm considering tuning solref/restitution parameters or just accepting that the balls might move together as a cluster into the box, which could actually simplify the design.

I'm also realizing rolling friction adds complexity — a struck ball transitions from sliding to rolling via friction (converging to 5/7 of the initial velocity), while the striker retains some residual spin and creeps forward, potentially causing repeated contacts rather than a single clean impact.

Maybe the simplest fix is making the rail frictionless, so balls slide without spinning at all and elastic collisions transfer velocity cleanly, stopping the struck ball dead. Ball4 would then slide into the box and stop against friction there or hit the wall — a much cleaner outcome than dealing with rolling spin dynamics.

With imperfect restitution, ball1 keeps residual velocity and could drift into ball2 again, so leftover motion might never fully settle unless I add rolling friction to the rail to damp out small velocities—maybe using condim 6 with friction parameters tuned so sliding balls eventually stop.

I'm reconsidering the pendulum-ball mass ratio: making the bob lighter than the ball gives a smaller elastic velocity transfer but lets the pendulum rebound backward and keep swinging, which is acceptable since it doesn't need to come to rest. Since I can't verify this numerically without running the simulation, I'm just reasoning through plausible physical outcomes.

For the design, I'm thinking of containing the balls in a shallow channel rail — a flat base with two low side walls as one body — so collisions stay perfectly aligned and nothing drifts sideways. For the pendulum, I'm setting the pivot height and arm length so a 0.5 m release height corresponds to length 0.5 and a 90-degree starting angle, with the bob beginning horizontal at the bottom of its arc.

I'm working out the exact heights so the swinging bob strikes ball1 at the same center height as the rail balls, while making sure the bob clears the rail surface without grazing it — possibly by positioning the rail to start just past the pendulum's lowest point to avoid collision at the bottom of the swing.

Actually, I'll just add an explicit contact exclude between the pendulum and rail bodies and set the rod's geom to contype 0 so it doesn't collide unwantedly. Then I'm spacing out ball positions: ball1 touches the bob at x=0.05 (sum of radii), with subsequent balls spaced 0.15 apart along the rail.

I'm reconsidering timing—the bob takes roughly 0.4s to swing to the bottom, so ball1 should sit just slightly closer (around 0.051) to guarantee contact right at the bottom of the swing. I also need to account for friction converting sliding to rolling motion for the struck ball before it reaches the next ball across the 0.10 gap, so I'm working out the sliding-to-rolling transition distance using the standard rolling-friction formula with an assumed velocity and friction coefficient.

This gets messy fast—each collision transfers only part of the velocity depending on whether the ball is sliding or already rolling, and the balls end up moving at different fractions of speed, meaning ball1 could end up slower than ball2 after their collision and never catch up before ball2 hits ball3. That leads to a cascade of secondary collisions rather than a clean chain reaction, which seems too messy to model well, so I should look for a simpler setup.

I'm thinking it's cleaner to just make the rail low-friction so the balls mostly slide across their short travel, setting friction low and condim 3 for the contacts.

But I realize sliding friction alone won't fully kill the problem — at low μ the balls eventually transition to rolling and then just keep going at 5/7 their original speed forever, which isn't physical here. So I probably need higher condim (like 6) with a rolling friction coefficient on the rail contacts to actually damp out that residual rolling motion.

Actually, maybe it's simpler to sidestep this whole friction headache: make the rail essentially frictionless and instead rely on near-perfect elastic collisions to dissipate the leftover velocity naturally, rather than fighting with torque and rolling-resistance estimates.

Maybe freejoint damping of around 0.01 would slow things too much, including the fall itself, so I'll keep it light and instead rely on a high-friction box floor to kill horizontal momentum once the ball lands. Since default contacts are fairly inelastic, the ball shouldn't bounce much after dropping from the rail into the box, and it'll settle as it rolls to a stop on the floor.

Since friction mixes by max element-wise, I should give balls low sliding friction and keep the rail low too, letting the box floor's high friction dominate when balls arrive there. I'm weighing whether to add rolling friction to the rail to kill leftover drift from balls 1-3, but if restitution is around 0.9 their residual velocities should be small enough that they either settle or roll gently toward the box within the time window.

Now I'm working through pendulum bob mass choices—if the bob mass equals the ball mass, an elastic collision stops the bob and sends ball1 off at roughly 3.13 m/s, which seems too fast since that would launch the ball off the rail end and carry it about 0.75 m horizontally after falling 0.3 m.

I'm testing a lighter bob instead, at 0.25 times the ball mass, which gives ball1 a gentler 1.25 m/s while the bob rebounds backward at about -1.88 m/s, swings up to roughly 0.18 m height, then swings forward again toward the empty spot where ball1 used to sit.

Checking the geometry, the bob only clears the balls' height once it's risen past about 2.5 cm, which happens around a 26° swing angle — but ball1 may still be sitting at x≈0.15-0.22 after its collision with ball2, meaning the bob's forward swing could clip ball1 a second time. This creates a messy repeated-collision scenario, so I'm considering adding hinge damping to bleed off the pendulum's energy, or rethinking the setup so ball1 moves clear of the bob's swing path.

With e<1, the bob retains a small forward velocity, swings slightly forward then settles back into a small oscillation near the bottom while ball1 moves off at roughly 3 m/s down the chain. I'm checking whether rail friction could slow ball4 enough before it reaches the box—estimating that with sliding friction transitioning to rolling, the travel distance before pure rolling kicks in comes out to about 12 meters.

Running through the four successive collisions (bob→1→2→3→4) with restitution 0.9, each transfer multiplies velocity by about 0.95, so after four hits ball4 ends up around 2.5 m/s leaving the rail. Now I'm thinking about how to position the box relative to the rail's end height so it reliably catches the ball at that lower speed.

Continuing, friction then decelerates rolling at about 5.5 m/s² so it stops within roughly 0.3 m, likely tapping the back wall near 1 m/s, which is soft enough to settle rather than bounce hard. I'm wondering if 2.5 m/s initial speed is too fast and whether I should soften box contacts with damped solref parameters instead of trying to fight the speed through friction alone.

For timing, the pendulum released at 90° with L=0.5 m hits bottom around t≈0.42 s, then the chain reaction through the gaps adds maybe 0.1 s, so ball4 should land in the box around t≈0.7 s, leaving plenty of settling time before t=6. Rail friction for the balls resting before impact should be fine.

I also need to handle elastic contact between the bob and ball1, not just ball-rail contact. Since MuJoCo mixes solref values from both geoms by default, I should instead define explicit contact pairs for ball-ball and bob-ball interactions to avoid unwanted jitter from mismatched damping on the rail contacts.

I'll add body exclusions for adjacent ball pairs so the default dynamic contact detection doesn't create duplicate contacts, since explicit pairs are processed separately from the broad-phase candidate set. The pairs I need are bob–ball1, ball1–ball2, ball2–ball3, and ball3–ball4.

For the solref values on these elastic contacts, I'm weighing whether to use the negative (direct stiffness/damping) form or the timeconst/dampratio form, thinking about how MuJoCo's restitution behaves with soft constraints and recalling that Newton's cradle examples typically use near-zero damping with specific negative solref values to get a crisp, low-dissipation bounce.

Testing stiffness values to bound penetration depth: with k≈25000 I get about 2cm overlap which is too much for 5cm balls, but bumping to k=1e5 gets penetration down to under 1cm with a half-period around 5 timesteps, which seems reasonable. I'm checking that ω·dt stays in a range the semi-implicit solver can handle stably.

Now I'm working through MuJoCo's solref parameterization — trying the positive form (timeconst, dampratio) but the math gives absurdly high stiffness with low dampratio, so that combination is unstable. Switching to the negative form instead, specifying stiffness and damping directly.

I'm working out appropriate solref damping values so the contact settles within a reasonable number of steps without excessive penetration, testing values like "-60000 -8" and estimating the resulting decay time and penetration depth.

I should also account for the default solimp impedance curve, which ramps from 0.9 to 0.95 over a small penetration width, and consider how semi-implicit Euler integration affects energy and restitution at this stiffness. I'm now turning to the bob-ball1 contact pair to apply similar reasoning with the bob's mass relative to the ball.

Since the rod is lightweight compared to the bob, the pendulum's effective mass at the point of contact is close to the bob's own mass, so with nearly equal masses the bob should almost fully stop on impact, leaving a small residual forward velocity that causes a slight swing and rise of a couple millimeters. Meanwhile the struck ball1 continues on to hit ball2 and decelerates from friction, leaving a modest residual velocity after the chain of collisions.

On the rail, friction will slow each ball over roughly half a second to a second, converting sliding motion to rolling and bringing them to rest within a few centimeters of travel; ball3's leftover drift after its collision looks like roughly 4 cm given the estimated friction coefficient, while the rolling transition time comes out to around 0.2 seconds for its post-collision velocity.

I'll place the rail end just past ball4's position, maybe 0.1 m further, so it enters the box without overshooting. Since balls transition from sliding to rolling friction and decelerate quickly, I can confirm balls 1-3 stay safely clear of the box edge even accounting for bounce energy, with only a centimeter or so of drift after friction kicks in.

I need to lower the ball geom's sliding friction to match the rail (around 0.05), since contact friction takes the max of the two surfaces, so I'll set ball friction to "0.05 0.005 0.003" and keep box friction higher. Ball-ball contacts stay frictionless with condim 1, which should be fine for the collision physics.

Now for setting up the initial pendulum position at release: I need the hinge body at the pivot with the bob offset locally, rotated so the bob sits horizontal to one side. Rather than computing a full 29-value keyframe qpos covering the hinge plus four free joints, it's simpler to just build the pendulum geometry already rotated to the horizontal release position directly in the body frame, avoiding keyframes altogether.

I'm checking that the bob clears the rail at its lowest swing point, placing the rail off to the side so the pendulum doesn't collide with it—sketching rail dimensions with a top around z=0.10 and a span that keeps clear of the bob's arc.

Since the hinge fixes the pivot to the world, I don't think a separate support body is needed, so I'll skip adding one and move on to positioning the first ball so it just touches the bob at the bottom of its swing.

Spacing the remaining balls along the rail with similar small gaps, then checking that the last ball exits the rail's end around x=0.70 while still moving fast enough to fly off rather than stop. I'm working out the projectile drop from the rail height down to a small landing box, estimating fall time and horizontal travel distance at a few different plausible exit speeds to figure out where to place that box.

I'm placing the box so its inner cavity spans roughly from x=0.72 to 1.42, setting the front wall low enough that the falling ball clears it, and sizing the back and side walls to contain the ball once it lands around x≈1.05-1.1. I'm reasoning through the landing, the low-energy bounce off the back wall, and how rolling friction will gradually bring the ball to rest inside the box.

I'm considering whether to bump up rolling friction on the box, but 0.03 seems fine to keep things stable with condim 6. I'm also checking whether ball4 could bounce off the back wall upward given its height, and reviewing the box geometry — floor, front, back, left, right walls with friction "1 0.02 0.03" applied across all of them, making sure the wall positions and heights line up correctly.

Checking ball clearance over the front wall confirms it lands safely even at slower speeds, since the drop distance stays under the wall's lower edge. At 2.5 m/s the ball leaves the rail edge immediately since centripetal requirements exceed gravity, and dropping onto the box floor with condim 6 should behave normally — now I'm weighing whether rail guide walls are actually necessary given potential y-velocity noise.

I'm sizing up low guide walls flanking the rail, checking ball radius against the gap clearance so the ball doesn't contact them during normal travel, then setting the rail as a static body so it skips rail-floor collision checks against other static geometry, before moving on to defining the pendulum body.

Working out the pendulum hinge, I compute the gravity torque on the bob and confirm it produces a negative rotation about the y-axis, decreasing the swing angle as expected.

I check the bob's resulting position and velocity, confirming it moves toward x=0 at the bottom of the arc with velocity directed toward the balls, which matches the physical intuition. I also note there's no joint limit on the hinge, and I'm verifying whether the bob's swing path might clip through the floor or the rail near x≈-0.5.

I'm now reviewing the exclude pairs for the pendulum-rail and ball-to-ball contacts, noting that ball1-ball3 contact isn't explicitly excluded but should be harmless since they're unlikely to touch directly. Setting up the pendulum-ball1 contact pair with a soft solref/solimp configuration to tune the contact stiffness.

Working through the numbers: with k=60000 and solimp near 0.95, the effective stiffness gives ω≈251 rad/s, and the effective damping ratio works out to roughly 0.95 amplitude retention per half-period—since the reference acceleration is computed in constraint (relative) space, this frequency is mass-independent, which simplifies things. I'm now checking the penetration depth expected at an impact speed of 3.1 m/s.

I'm double-checking that the semi-implicit integration scheme stays stable at this ω·dt, and confirming how the solver blends constrained and unconstrained accelerations—since the unconstrained acceleration here is zero, this simplifies nicely. I'm also accounting for the pendulum's rod mass contributing a small moment of inertia term alongside the bob.

Moving to the ball parameters, I settle on mass 0.1 kg with radius 0.025 m, giving a reasonable density, and confirm the inertia defaults correctly from the sphere's mass. I check the collision sequence (ball1 hitting ball2, etc.) and verify the leftover velocities after each impact using restitution around 0.9–0.95 — ball1 ends up with about 0.15 m/s leftover, and the pendulum bob picks up roughly 0.16 m/s forward, swinging to about 3.6 cm in x. Since ball1's leftover position sits well short of the bob's reach, the bob never catches up to it.

I then stress-test lower restitution values, like e=0.5: this changes the chain dynamics substantially, with ball4 ending up around 1.0 m/s, and the pendulum bob retaining 0.25 of velocity (~0.78 m/s), swinging far enough to potentially re-strike ball1 near x≈0.15–0.17. This creates a messier chain of secondary collisions, but ball4 likely still makes it into the box; I'm weighing whether later balls bouncing around could disturb ball4 near the end, trusting that the box's size and rolling friction should keep things stable by the 6-second mark.

Separately I'm working out the physical setup: floor dimensions, lighting, and friction coefficients for the box, ball, and rail, confirming condim and friction values combine using the maximum rule across contacting surfaces.

Now I'm laying out the actual XML geometry: rail base and guide positions, the box body's placement and inner dimensions, and the floor size.

Default integrator is fine, no need for extra exclusions since nothing references the world body. This should be ready to finalize.

