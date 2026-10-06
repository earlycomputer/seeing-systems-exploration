The scene uses a frictionless, nearly elastic contact pair between neighbouring balls, so each impact passes most of the speed down the line. Ball 1 starts rolling at 2 m/s. Ball 3 leaves the second impact at about 1 m/s. It rolls up a 3 cm ramp that ends flush with the rim of a fixed, open-top cup, and drops in. Rolling friction brings every ball to rest.

These speeds come from hand estimates. I have not run the file in MuJoCo.

```xml
<mujoco model="three_ball_relay_into_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="0.6 -0.5 1.5" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" pos="0 0 0" rgba="0.8 0.8 0.75 1"/>

    <!-- ramp: top surface rises from z=0 at x=0.80 to z=0.03 at x=1.00, meeting the cup rim -->
    <body name="ramp" pos="0 0 0">
      <geom name="ramp_slab" type="box" size="0.10112 0.05 0.01" pos="0.90148 0 0.00511" euler="0 -8.5308 0" rgba="0.55 0.45 0.35 1"/>
    </body>

    <!-- cup: fixed, open-top box cup; inner floor at z=0.004, rim at z=0.03, interior 0.12 x 0.12 -->
    <body name="cup" pos="1.065 0 0">
      <geom name="cup_base" type="box" size="0.065 0.065 0.002" pos="0 0 0.002" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_front" type="box" size="0.0025 0.065 0.015" pos="-0.0625 0 0.015" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_back" type="box" size="0.0025 0.065 0.015" pos="0.0625 0 0.015" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_left" type="box" size="0.065 0.0025 0.015" pos="0 0.0625 0.015" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_right" type="box" size="0.065 0.0025 0.015" pos="0 -0.0625 0.015" rgba="0.2 0.4 0.8 1"/>
    </body>

    <body name="ball1" pos="0 0 0.02">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.02" condim="6" friction="1 0.005 0.001" rgba="0.9 0.2 0.2 1"/>
    </body>

    <body name="ball2" pos="0.2 0 0.02">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.02" condim="6" friction="1 0.005 0.001" rgba="0.2 0.8 0.2 1"/>
    </body>

    <body name="ball3" pos="0.4 0 0.02">
      <freejoint name="ball3_free"/>
      <geom name="ball3_geom" type="sphere" size="0.02" condim="6" friction="1 0.005 0.001" rgba="0.95 0.8 0.1 1"/>
    </body>
  </worldbody>

  <contact>
    <!-- nearly elastic, frictionless ball-to-ball impacts so momentum is handed down the line -->
    <pair name="pair_b1_b2" geom1="ball1_geom" geom2="ball2_geom" condim="1" solref="-100000 -5"/>
    <pair name="pair_b2_b3" geom1="ball2_geom" geom2="ball3_geom" condim="1" solref="-100000 -5"/>
  </contact>

  <keyframe>
    <key name="start" qpos="0 0 0.02 1 0 0 0  0.2 0 0.02 1 0 0 0  0.4 0 0.02 1 0 0 0" qvel="2 0 0 0 100 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm thinking through three balls in a row along the x-axis, with ball1 given an initial velocity toward the others. Since MuJoCo contacts are soft rather than perfectly elastic, the collision between equal-mass spheres won't be a clean Newton's-cradle transfer—momentum will be shared somewhat depending on solref settings, so ball1 likely continues forward with reduced velocity rather than stopping completely.

I need ball1 and ball2 to come to rest while ball3 ends up in the cup, so adding rolling friction (condim 6) could help decelerate them naturally. For the cup itself, since the floor is a flat plane with no holes possible, I'm considering a cup with a ramp leading to the rim so ball3 can roll up and drop in, or alternatively a low-walled cup where the front wall is short enough for a ball to roll over given its radius.

I'm also weighing a cup lying on its side with the open mouth facing the balls, so ball3 rolls straight in and the closed back stops it — this seems like the most robust and simplest approach compared to ramps or partial walls that risk the ball rolling back out.

Maybe simplify to a shallow cup with low walls, around 1cm, so the ball can climb the lip with enough speed but then needs to stop inside rather than exit the back. I'm considering making the back wall taller than the front so the ball gets trapped asymmetrically, like a one-way catch basin.

Actually a ramp might work better: have the ball roll up a static ramp body to some height, then launch off the end and drop into the cup, since the floor plane is an infinite half-space and can't accommodate a sunken cup below z=0.

I'm working out the energy balance for a rolling sphere climbing height H, so I can tune the ramp height and cup wall dimensions to catch the ball without it overshooting or falling short.

Working through the contact mechanics, I'm considering how the spinning ball's contact point has a tangential velocity component that friction will act on, pushing ball2 slightly downward and ball1 slightly upward during the collision—a mild effect given typical MuJoCo contact solver parameters.

With the critically damped solver, the collision behaves nearly perfectly inelastic, so both balls end up moving together around v/2 right after contact. From there ball1 retains most of its spin (rolling normally) while ball2 starts sliding with no spin, and friction then needs to bring ball2 up to the 5/7 rolling speed while slowing ball1's excess spin—so they likely approach similar rolling speeds afterward.

Rather than dealing with this inelastic mess, I'm reconsidering using an elastic collision setup to mimic a Newton's cradle, where ball1 stops and transfers its velocity entirely to ball2. I'm testing solref parameters with negative stiffness/damping values or a small dampratio to introduce bounce into the contact model.

I recall exclude only affects dynamically generated contacts, not explicit pairs, so I can safely use exclude for body pairs alongside an explicit pair with bouncy solref for the elastic collision behavior. But I also need to think about how spin affects post-collision velocity for rolling balls in an elastic central collision.

With enough rolling resistance, balls 1 and 2 might stop before the ramp while the faster ball 3 keeps going—I'm working out the deceleration formula from rolling friction torque to get stopping distance in terms of μ_r, g, and r. I'm also wondering if I should sidestep the spin complexity entirely by simplifying the initial setup rather than tracking elastic collision details so precisely.

Elastic collisions seem cleaner than letting things go inelastic and relying on ramp/cup geometry to separate the balls, so I'll set a pair interaction with condim=1 to strip out tangential friction effects between the colliding balls. Using r=0.02m and default density, I'm calculating ball mass at about 0.0335 kg, then working through the momentum transfer: ball1 at velocity V transfers roughly 0.51V to ball3 after slipping, while ball2 picks up close to V with the friction coefficient driving a slip deceleration around 10 m/s².

Checking the slip-phase duration confirms it wraps up quickly, settling at 5/7 V, and I'm verifying the gap spacing (0.2 m) is enough for slipping to finish before the next collision — roughly 0.06s and 0.1m of travel for V=2, so it should be fine even accounting for rolling friction during that window. Now I need to pick the ball spacing and rolling friction so ball3 reaches the ramp around 1.0–1.2 m/s while balls 1 and 2 stop short of it, keeping in mind rolling friction also decelerates ball3 on its approach.

Trying V=2.5 with ball1 at 0, ball2 at 0.25, ball3 at 0.5, ramp starting around 0.8: ball3's post-collision speed is about 1.28 m/s, ball1's about 0.71, ball2's about 0.51. Using the rolling stop-distance formula, I'm solving for the rolling friction coefficient that lets ball1 stop within about 0.4 m, getting μ_r ≈ 0.0018, while ball3 still needs enough speed left to hit the ramp at roughly 1.0 m/s.

Checking ball3's decel over the remaining 0.3 m with that μ_r gives about 1.12 m/s at the ramp, which works. But I need to check whether ball1, after its collision, might actually catch up to ball2 again since ball1 ends up moving faster than ball2's post-collision speed — that could cause an unwanted second collision.

Working through the positions, both balls lose speed quickly from rolling friction and should settle around x≈0.7-0.75 before the ramp, leaving ball3 enough room (~0.33 m) to travel freely. I'm now second-guessing whether MuJoCo actually models rolling friction this way, or whether I need condim=6 for the rolling resistance to even apply.

Checking the friction spec, the contact uses slide/torsional/rolling values and MuJoCo combines geom friction by taking the max, so my rolling friction estimate should roughly hold even with soft constraint behavior at rest. Torsional friction about the z-axis doesn't matter here since nothing spins in place.

Now I need to figure out the ramp geometry — the rise height must clear the cup's front wall, so I'm working out how the cup's base thickness and wall height interact with the ramp's end height.

Simplifying this: I'll have the ramp's top edge align with the cup's front wall top, at the same height, with the wall thickness accounted for, so the ball naturally rolls off the ramp and drops straight into the cup's interior.

Accounting for energy loss at the ramp-to-flat transition, velocity drops to around 0.76 m/s after friction, leaving comfortable margin over the 0.75 m/s threshold given the 1.12 m/s starting speed. But I need to check the edge transition more carefully since the ball rolling over the cup's lip could introduce additional loss.

For the projectile phase after launching off the edge, I'm computing the drop height (about 0.035 m) and vertical launch velocity (0.12 m/s), solving the quadratic for fall time (~0.098 s) and resulting horizontal distance (~0.075 m) to verify it clears into the cup.

If the ball's faster, the landing distance grows accordingly, so I'm checking the cup's interior width is large enough to contain this trajectory—treating it more like a shallow tray than a deep cup. After landing, the ball bounces and rolls toward the back wall at roughly 0.7 m/s; since the wall's inner height sits above the ball's center, it should bounce back rather than climb over, then bounce again off the front wall and settle from rolling friction.

Mapping out the full timeline, the chain of collisions and settling events fits comfortably within about 2.5 seconds, well under my 6-second budget, and since I'm using default (near-inelastic) contact properties, the walls should absorb energy rather than bounce the ball around excessively. Now I'm working out the ramp geometry—sizing it as a rotated box with a thin cross-section, positioning it so its top surface rises from floor level to the target height over the run length, and computing the slope length from the horizontal and vertical legs.

The lower end's top corner sits right at floor level where the ball transitions onto the ramp with a slight kink, which is acceptable. At the upper end, the top surface reaches height 0.04 aligning with the cup's front wall, so the ramp's end face tilts slightly but sits adjacent to the wall just fine.

Now I'm defining the cup geometry: a base box plus four walls forming an open container with 0.005 wall thickness, interior roughly 0.16 by 0.12, floor raised to 0.005 to match base thickness, and walls reaching up to 0.04 to meet the ramp top. I'm deciding the cup should be a static body with no joint, welded to the world, which should work fine since all geoms belong to the body.

Now I'm computing precise positions: the ramp starts at x=0.85 and ends at x=1.10, where the cup's front wall sits; the cup body center lands at x=1.1875, with front and back wall centers offset by ±0.0825, interior spanning 1.105 to 1.265, and I'm working out the half-dimensions for the base and side walls to match a 0.12 interior width and 0.05 ramp lateral half-width.

On the 9° slope, gravity along the incline gives roughly 1.1 m/s² acceleration while rolling friction decelerates at about 0.63 m/s², so balls that reach the ramp too slowly will roll back down and settle on the floor rather than reaching the cup — which is fine since they won't make it in anyway. I'm checking whether ball1 or ball2, after losing momentum, might collide with ball3 while it's still on the ramp, though ball3 should be well ahead by that point.

Now I want to double-check the elasticity assumption for the pair collision more carefully using V=2.5, since bumping up rolling friction for safety would also slow down ball3. I'm working through how MuJoCo's solref parameters translate into an effective restitution coefficient — for a damped spring with damping ratio ζ=0.05, the restitution comes out to roughly 0.855, though solimp also factors in and complicates a clean mapping to true restitution. I recall that specifying both solref values as negative numbers lets MuJoCo interpret them directly as stiffness and damping rather than time constants, which might give more control over achieving a fully elastic-like bounce.

Working through the math, low dampratio with a small timeconst makes the spring absurdly stiff since stiffness scales with 1/dampratio², and the resulting oscillation period ends up shorter than the timestep, which is unstable. I think I need a larger timeconst like 0.01 paired with a higher dampratio like 0.1 to keep the implied period safely above the timestep.

Since the constraint force is solved implicitly, stability holds up better than with explicit springs, so I'm recalling that negative solref values (specifying stiffness/damping directly in force units) are what people typically use to get a clean elastic bounce, though I'm fuzzy on the exact values that give near-perfect restitution.

Doing the math, treating the contact like an undamped oscillator with ω=√k, I need k around 24,700 to get enough steps per bounce, but that predicts roughly 16mm of penetration for balls that are only 20mm across — clearly too deep, so this approach needs rethinking.

Trying a shorter half-period (5 steps, 0.01s) gives ω=314, k=1e5, penetration ~8mm — still substantial, but MuJoCo's implicit solver handles stiff constraints better than this naive oscillator estimate suggests, since the impedance mixing (force ≈ d·aref + (1-d)·unconstrained) with d≈0.9-0.95 softens the effective dynamics, and stability for semi-implicit Euler just requires ω·dt < 2.

I'm also considering avoiding elasticity entirely by varying ball masses — but a fully inelastic collision would just make the balls stick together, which is bad since I need separation. Maybe I can rely on spin: after an inelastic central collision both balls move at V/2, with ball1 carrying forward spin and ball2 none, and then floor friction could act differently on each depending on whether their contact point is sliding backward or forward.

Working through it, though, the friction actually pushes ball1 forward into ball2 and slows ball2, so they'd stay in contact — that approach fails. A frictionless setup wouldn't work either. So I'll go back to using elastic collisions with a moderate velocity, and figure out just how small V can be while still letting ball3 clear the ramp base with enough margin.

Tracing through the chain: ball1 hits ball2 at speed V transferring pure linear velocity (no spin), friction then spins ball2 up to rolling at 5/7 V, which transfers to ball3 at 5/7 V again, giving ball3 a rolling speed of roughly 25/49 V ≈ 0.51V. To clear the 1.0 threshold after losses, I'm estimating V needs to be around 2.3 — unless I lower the ramp height instead, which would reduce the required speed to around 0.65. I also need to check the cup geometry to make sure the ball fits properly given its radius and the wall height.

I'm also considering alternate collision mechanics: keeping the ball-ball pair frictionless rather than introducing friction mid-impact, since adding spin coupling there complicates the impulse calculation unnecessarily. Another option is making ball1 heavier or larger to boost the elastic transfer via the mass ratio formula, but a different radius would shift the contact point off-center and tilt the line of centers, complicating the whole collision geometry — probably not worth the trade-off if balls are meant to be uniform.

Now I'm checking stiffness-timing stability: setting penetration depth to achieve a specific response at the expected impact speed gives an angular frequency near the edge of stability for semi-implicit integration, so I need to look more carefully at MuJoCo's reference acceleration and timeconst clamping to make sure the constraint solve stays stable at zero damping.

With symplectic Euler the energy is roughly conserved, so maybe larger balls (r=0.03) would make the 8mm penetration look smaller relative to the ball, without changing velocity. I'm also considering whether a sideways cup could let ball3 reach it at a much gentler speed (~1 m/s, 3mm penetration), though a checker might detect "inside cup" via bounding box in a way that still works — though an upright cup fed by a ramp feels more natural for the setup.

Now I'm working through the geometry of a shorter cup wall (Hc=0.03, r=0.02) so the wall contact sits above the ball's center, and estimating the energy needed from the ramp: solving g*0.03/0.7≈0.42 gives a required speed around 0.65 m/s after the cosθ loss, so with a ramp angle of about 8.5° (run 0.2) and initial V=2.0, ball3 would enter around 1.02 m/s, adjusted slightly for rolling friction.

With a small rolling resistance (μ_r=0.001, decel ~0.35 m/s²), ball3's speed drops to about 0.9 after 0.3m and the ramp climb, landing around 0.5 m/s at the top -- comfortably above the ~0.75 m/s threshold needed. I'm also checking stopping distances for ball1 and ball2 under the same friction assumption to make sure they settle appropriately short of the ramp.

I'm double-checking the solref/solimp formula to confirm the effective spring stiffness scales correctly with the negative solref convention, and that the penetration depth stays reasonable given the contact impedance parameters.

With gravity being negligible in that correction term, the main question becomes whether the symplectic Euler integration preserves energy well enough to give near-unity restitution, since MuJoCo's default integrator only applies implicit treatment to joint damping, not contact constraints.

Checking the discrete activation: contact triggers only once penetration exceeds zero with no margin, which seems fine, and the constraint force stays non-negative so it never pulls objects together during separation.

I'm also trying an alternative solref formulation with a small damping ratio, recomputing the resulting frequency and checking whether ωdt stays in a stable range.

Working through the negative solref option instead, since it directly sets stiffness and damping ratio rather than deriving them from time constant and damping ratio parameters—settling on something like -10000 and a small negative damping value to get a reasonable restitution-like effect while staying stable. I also want to double check whether a condim=1 contact pair still needs friction coefficients specified, and whether I need to exclude redundant contact pairs between the balls to avoid duplicate constraints.

I'm also second-guessing myself on the semantics of `<exclude>` versus explicit `<pair>` elements—whether exclusion only applies to the dynamically generated contact mechanism and doesn't override pairs that are explicitly declared, which matters for whether I need separate exclude directives for ball1-ball3 contacts.

So I'll leave out exclude since it's harmless and explicit pairs override dynamic ones anyway. For friction mixing, condim ends up 6 from the ball geoms (since contact condim takes the max of the two geoms), and friction values mix by taking the max across normal, torsional, and rolling components—giving roughly 1, 0.005, 0.001 for ball-floor contacts. The ball's initial resting position at z=0.02 should allow for small penetration from the soft contact settling.

Now I'm checking the rolling condition: setting ωy = +100 rad/s satisfies pure rolling for V=2.0 m/s with r=0.02, since the contact point velocity cancels out correctly. With balls spaced at x=0, 0.2, 0.4, ball1 should collide with ball2 around t≈0.08s given the 0.16m gap, kicking off the slip phase for ball2.

Working through the slip dynamics: the sphere decelerates linearly under friction while spinning up, with slip ending once v drops to 5/7 of its post-collision value—roughly 0.058s and 0.1m of travel, which stays within the 0.16m gap. This gives ball2 hitting ball3 at about 1.43 m/s, after which ball3 slips down to roughly 1.02 m/s over about 0.07m, landing near x≈0.5. I'm placing the ramp start at x0=0.8, giving ball3 a 0.3m runway to reach steady rolling speed before impact.

Tracking ball1's trajectory after spin-up: it settles to rolling at about 0.57 m/s and, using rolling friction deceleration, would travel roughly 0.47m before stopping—unless it catches up to ball2, which has settled around 0.38m position at 0.41 m/s and would itself stop near 0.62m. Since ball1's stopping point of 0.65m would overshoot that, I conclude ball1 catches ball2. Overall the balls seem to settle out somewhere near 0.7-0.8m, possibly interacting with the ramp base, and with rolling friction decelerating everything at about 0.35 m/s², all balls should drop below 5 cm/s well within the 6 second window—likely within about 2 seconds.

Now checking ball3's path down the ramp: with a 0.2 run and 0.03 rise, it reaches roughly 0.5 m/s at the top, launches off the ramp edge (ball center near 0.05), and needs to clear the front wall (also at 0.03 height) before dropping into the cup. The fall into the interior floor (center height 0.024) is about 0.026m, giving a fall time near 0.073s and horizontal travel around 0.036-0.06m depending on launch speed—well within the 0.12m interior length, so it should land inside.

Checking the distance to the corner confirms clearance stays above the ball radius throughout the fall, and since the velocity-squared term exceeds gravity times radius, the ball leaves the edge immediately rather than pivoting around it. So the ball should roll cleanly into the cup and continue at roughly 0.5 toward the back wall, where the default contact parameters will absorb most but not all of the energy.

I'm now double-checking the ramp-to-floor transition geometry, specifically whether the box's top face meets the floor exactly at x0 and whether part of the end face extends above the floor near that junction, since that could create an unintended collision point.

Then I'm verifying the ramp's upper end aligns smoothly with the cup wall—checking that the top edge heights match (both around 0.03) so the ball transitions cleanly without a bump, and noting the small 3mm overlap between the ramp end and the wall is harmless since both are static geometry.

Working through the cup's inner geometry, I confirm the ball settles at center height 0.024, comfortably below the rim at 0.03 and well under the wall top at 0.044, satisfying the "ball in cup" condition. I consider whether a taller cup with a longer ramp would look better but decide to keep the current dimensions since they already work.

Now I'm computing the ramp's incline angle from the 0.2 run and 0.03 rise, getting about 8.53°, and continuing to work out the slope length for positioning the ball's starting point.

Working out the remaining wall and base dimensions for the cup (side walls, front/back walls, base), the ramp half-width, and the ball's density and mass. Now I'm also sorting out the qpos/qvel structure for the three freejoints plus the cup's fixed position, starting to assign initial ball positions.

Checking the ball2-ball3 initial spacing and verifying the elastic collision physics—computing the spring stiffness, resulting frequency, contact duration, and peak penetration depth to make sure the simulation timestep resolves the impact correctly.

Confirmed, so I'm setting up the ball1-ball2 contact pair with that same stiff solref. Ball1-ball3 contact isn't really relevant since ball3 moves ahead out of range before any collision could occur. One thing to track: when ball1 collides with ball2, ball1 still carries its spin into that frictionless elastic collision, which matters for the subsequent dynamics.

Right after, ball1 sits stationary but spinning at 100, so friction kicks in and accelerates it forward to 2/7 of its surface velocity (~0.57) within about 0.04s and 0.01m of travel, while ball2 continues moving away. I need condim 6 on the ball geoms for torsional and rolling friction, while floor and ramp/cup stay at default condim 3. Now I'm finalizing the floor plane size and adding a light before writing the file.

