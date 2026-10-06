Ball 1 starts rolling at 3 m/s. The ball-to-ball contacts are frictionless and nearly elastic, so the motion passes down the row. Rolling friction stops balls 1 and 2 well short of the cup. Ball 3 is the fastest, so it climbs a shallow ramp, drops over a 7 mm inner lip into the cup, and settles against the low-friction back wall.

This is designed from hand estimates and has not been run. The weakest point is ball 3's speed at the lip, which depends on how bouncy the ball-to-ball contacts really are. If ball 3 stalls on the ramp, raise ball 1's starting speed (and its matching spin) or lower the balls' rolling friction a little.

```xml
<mujoco model="three_ball_chain_into_cup">
  <option timestep="0.002"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="0.8 -1 3" dir="0 0.3 -1" diffuse="0.9 0.9 0.9"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.8 0.8 0.75 1"/>

    <body name="ball1" pos="0 0 0.03">
      <freejoint/>
      <geom name="ball1_geom" type="sphere" size="0.03" condim="6" friction="1 0.005 0.0021" rgba="0.85 0.2 0.2 1"/>
    </body>
    <body name="ball2" pos="0.25 0 0.03">
      <freejoint/>
      <geom name="ball2_geom" type="sphere" size="0.03" condim="6" friction="1 0.005 0.0021" rgba="0.2 0.6 0.2 1"/>
    </body>
    <body name="ball3" pos="0.5 0 0.03">
      <freejoint/>
      <geom name="ball3_geom" type="sphere" size="0.03" condim="6" friction="1 0.005 0.0021" rgba="0.2 0.3 0.85 1"/>
    </body>

    <body name="cup" pos="1.65 0 0">
      <geom name="cup_ramp" type="box" size="0.07524 0.045 0.005" pos="-0.0746 0 0.001016" euler="0 -4.574 0" rgba="0.6 0.45 0.3 1"/>
      <geom name="cup_base" type="box" size="0.075 0.055 0.0025" pos="0.075 0 0.0025" rgba="0.6 0.45 0.3 1"/>
      <geom name="cup_back" type="box" size="0.01 0.055 0.05" pos="0.14 0 0.05" priority="1" condim="3" friction="0.1 0.005 0.0001" rgba="0.7 0.5 0.3 1"/>
      <geom name="cup_side_left" type="box" size="0.075 0.005 0.035" pos="0.075 0.05 0.035" priority="1" condim="3" friction="0.1 0.005 0.0001" rgba="0.7 0.5 0.3 1"/>
      <geom name="cup_side_right" type="box" size="0.075 0.005 0.035" pos="0.075 -0.05 0.035" priority="1" condim="3" friction="0.1 0.005 0.0001" rgba="0.7 0.5 0.3 1"/>
    </body>
  </worldbody>

  <contact>
    <exclude name="ex12" body1="ball1" body2="ball2"/>
    <exclude name="ex23" body1="ball2" body2="ball3"/>
    <exclude name="ex13" body1="ball1" body2="ball3"/>
    <pair name="p12" geom1="ball1_geom" geom2="ball2_geom" condim="1" solref="-60000 -5"/>
    <pair name="p23" geom1="ball2_geom" geom2="ball3_geom" condim="1" solref="-60000 -5"/>
    <pair name="p13" geom1="ball1_geom" geom2="ball3_geom" condim="1" solref="-60000 -5"/>
  </contact>

  <keyframe>
    <key name="start" qpos="0 0 0.03 1 0 0 0 0.25 0 0.03 1 0 0 0 0.5 0 0.03 1 0 0 0" qvel="3 0 0 0 100 0 0 0 0 0 0 0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm planning the scene setup: three balls in a row where ball1 strikes ball2, ball2 strikes ball3, and ball3 rolls into a cup resting on the floor, with ball3 needing to end at rest inside it. I'm thinking through the physics of sphere-sphere collisions in MuJoCo to make this chain reaction work correctly.

With near-zero restitution the balls would just clump together moving at half speed rather than cleanly chain-reacting, which isn't what I want. I'm thinking I need to override the default contact solref with a bouncier setting, maybe using explicit contact pairs for ball1-ball2 and ball2-ball3 so I can tune elasticity separately from the floor contacts.

I'm also thinking about friction at the ball-ball contact points—spin from rolling could push the balls up or sideways, so I'll set a low pair friction coefficient between balls to minimize that effect. Then for the cup itself, I need to design walls low enough that a rolling ball can enter but still contains it once inside.

I'm thinking through a low-lip cup design: walls on three sides plus a short front lip (around 6mm for a 25mm ball radius) that the ball can roll over with enough speed but gets trapped behind once it bounces back with less energy. I'm working out the physics of a rolling sphere crossing a step edge, estimating the velocity threshold needed to clear the lip given energy loss from dissipative contacts, roughly landing around 0.3-0.5 m/s.

Since static geometries don't collide with each other in the physics engine, I realize I can add a gentle ramp — a slightly rotated box leading up to the lip — without worrying about it clipping into the floor, letting the ball roll up and drop into the cup's interior where taller walls keep it contained.

Now I'm working out concrete dimensions: balls with radius 0.03 placed at various x positions, and a cup around x≈1.2 with a thin base plate and surrounding walls roughly 0.05 high, with a slightly lower front wall to let the ball enter after rolling up the ramp.

I'm calculating the minimum ball speed needed to climb the ramp lip using rolling-without-slipping energy conservation (v²≥10gh/7), checking values like h=0.03 and h=0.015 to find a reasonable ramp angle and length so balls can clear the lip but still stop inside the cup once they fall off the lip into it.

Then I'm thinking through the physics once the ball is inside the cup: it drops onto the base, hits the back wall at speed, and bounces back with small restitution under MuJoCo's default soft-constraint contact dynamics, so the rebound should be weak enough that the ball doesn't climb back out over the lip (comparing against the same sqrt(10gh/7) threshold for the inner step height). I'm also considering whether the ball's spin and friction against the back wall could push it upward enough to escape.

I'm setting up ball1's initial velocity and angular velocity so it rolls without slipping (ω_y = v/r), while double-checking how MuJoCo interprets the angular velocity component of a free joint's qvel — whether it's in the body's local frame or the world frame.

Then I'm working through the sequence of elastic ball-ball collisions, tracking each ball's velocity after friction-induced slipping and rolling transitions: ball1 hits ball2 transferring momentum (ball2 slides then rolls to 5/7 v), ball2 then hits ball3, and ball1 (retaining some residual spin-driven velocity) potentially catches up to collide again — trying to trace through these successive speed fractions to see if ball1 ever re-collides with ball2 before the sequence settles.

Given the cascading velocity losses, I estimate the trailing balls end up moving too slowly (~0.25-0.3 m/s) to climb the cup ramp, which requires roughly 0.46 m/s — so I need v0 around 1.2 m/s to give ball3 enough margin, but that leaves ball1 and ball2 too slow to follow it up.

To be safe, I should add rolling friction using condim="6" with a rolling friction coefficient to decelerate the balls over time, though I need to work out the physics carefully since it affects ball3's speed too—estimating deceleration around 0.1 m/s² with a small rolling friction coefficient and typical ball radius.

Instead, I'm considering spacing geometry so ball2 slows down and stops short while ball3 still reaches the cup, calibrating the rolling friction coefficient so stopping distances differ enough between their respective speeds.

I'm checking whether ball2 could end up resting on the ramp itself rather than at its base—worrying about whether rolling friction alone is enough to hold a sphere static on an incline, since that requires comparing the friction torque to the gravitational torque component along the slope. This makes me reconsider whether ball2 should just come to rest near the foot of the ramp instead of partway up it.

I'm also realizing collision elasticity is a big unknown here—without elastic contact pairs, the default soft contact gives low restitution, so I need to tune the solref parameters to get a realistic bounce. I'm estimating that a lightly underdamped spring contact (damp ratio around 0.1) could produce roughly 70% restitution, which might be closer to what's physically plausible for these collisions.

With e=0.8, ball2 ends up at 0.9v which seems fine, so I'll stick with elastic pairs rather than overcomplicating with mass ratios. For contacts, I'll use condim 1 (frictionless, normal-only) for ball-ball pairs to keep things simple, while ball-floor contact will need higher condim for rolling friction.

Using condim 6 with friction values covering sliding, torsional, and rolling components on the balls, combined with default floor friction, the max-combining rule across contacts should work out reasonably. Now I'm checking whether explicitly defined contact pairs between ball1 and ball2 might duplicate the automatically generated collision pairs, which could be a problem I need to exclude.

I'm estimating collision timing: ball1 starts at v0=1.5 with a 0.24 gap, giving roughly 0.16s before contact. Working through restitution (e≈0.8), ball2 gets transferred velocity around 1.35 then slides down to a rolling speed of about 0.964 via the 5/7 friction factor, and I'm now tracking what happens to ball1's remaining velocity after the hit.

Ball3 ends up around 0.62 after hitting ball1's momentum transfer; meanwhile ball2 settles near 0.344 then collides again with ball1, leaving speeds around 0.5 and 0.36 respectively. Tracking deceleration from friction, ball3 reaches the ramp first with roughly 0.52 m/s, since it's ahead of the others at that point.

rolling at ~0.66 into the back wall. With low restitution, linear velocity drops near zero on impact, but the forward spin remains, and floor friction keeps pushing the ball into the wall while wall friction pushes it upward—so the spinning ball could actually climb the wall on impact, a classic spinning-ball-against-wall effect.

To prevent that from eating all the physical realism, I'm considering giving the cup wall geoms a lower friction coefficient and using the priority attribute so contacts between ball and wall use the wall's lower friction value instead of combining to the ball's higher friction. That way the upward climbing force gets suppressed appropriately.

With that fixed, the ball should sit against the wall spinning down, decelerating via floor friction pressing it into the wall rather than climbing it, eventually coming to rest. I'm also checking rebound dynamics off the back wall and whether the ball could bounce back over the inner lip step (about 0.01m), which would require a velocity around 0.37 m/s to escape -- unlikely given MuJoCo's fairly inelastic default contact solver settings.

Now I'm reconsidering the ramp/cup geometry: the ramp rises from the floor to the lip height, and the base cup sits beyond it so the ball drops into the cup once past the lip, with side walls keeping it contained laterally. I want to simplify the construction so the ramp's top edge directly meets the start of the base rather than needing a separate front wall piece.

Computing the box center by offsetting from the top surface along the rotated normal direction, which gives center coordinates around (xa+0.0755, 0, 0.0025) after accounting for thickness.

The top edge at x=xa sits right at z=0, so the ball transitions smoothly from the floor onto the ramp with just a small angle kink, no lip to worry about. At the top end (xb, z=0.015), the ramp connects into a cup base spanning 0.12m with walls tall enough for the 0.03 radius ball, so I'm now tracking the ball's velocity (0.64 m/s) as it leaves the lip to see where it lands inside.

I'll set interior half-width to 0.045, with side walls running from xb to xb+0.12 and the back wall topping out at 0.08. Since the ball just moves straight along x with no lateral drift, side walls along the ramp itself aren't really needed — the open front acting as the lip should be fine for a checker that likely just tests whether ball3's position falls within the cup geoms' bounding box.

Now I need to recheck whether ball1 or ball2 might also end up climbing into the cup with v0=2 instead of 1.5. Redoing the collision chain: ball2 rolls at 1.286, ball1 at 0.714, ball3 at 0.827, giving ball2 a post-collision velocity around 0.459 — then ball1 catches up to it with a relative velocity of 0.255, and applying e=0.8 elastic collision math bumps ball2 up to roughly 0.689, which is concerning since that's above the 0.46 threshold needed to climb the ramp.

So ball2 ends up at roughly 0.62 and ball1 at 0.55 — both potentially fast enough to also climb the ramp and crash into ball3 in the cup, which would be a bad outcome. The issue is that momentum transfer through the chain combined with rolling spin keeps propagating forward motion rather than stopping the trailing balls; since rolling friction decelerates everything roughly equally over distance, I'm not seeing an obvious mechanism that lets ball3 pull ahead enough while balls 1 and 2 stall out.

Maybe varying the masses could help — a heavier ball hitting a lighter one transfers more speed forward, while a lighter ball hitting a heavier one loses speed and bounces back. If ball1 is heaviest and ball3 lightest, ball3 would end up fastest while ball1 could slow down or reverse after impact. But if ball1 is heavy and keeps moving forward after hitting ball2, that doesn't solve the stopping problem either. I think the real lever is making ball3 travel much farther than balls 1 and 2, so rolling friction drains enough speed from the trailing balls that they stop short of the ramp while ball3 still has enough momentum to climb in.

Actually, maybe ball-ball friction could cancel spin: friction acts upward at the contact point on ball1, producing a torque that reduces its angular velocity, which seems promising for the design.

But the symmetric effect would give ball2 backspin while also adding messy vertical impulses. I'm also wondering if I can modify geometry—shallow pockets or other static bodies—to control the balls, though the brief says they sit on the floor, so maybe I need a different path where ball2 physically can't follow ball1's trajectory.

I'm trying tuning the cup ramp threshold so ball2 rolls back while ball3 continues, but the speed margin (0.62 vs 0.83) feels too tight given uncertainty in the restitution coefficient. Testing perfectly elastic collisions with equal masses and rolling friction instead: working through the momentum transfer chain ball1→ball2→ball3→ball2→ball1 to see if the resulting speeds naturally separate enough for a reliable outcome.

With d<1 the constraint mixes with unconstrained dynamics, which can reduce effective restitution, so I recall bouncy ball examples in MuJoCo use small dampratio or negative solref values for near-elastic bounces. I'll aim for a dampratio around 0.02, giving an effective restitution of roughly e≈0.94.

But I realize stiffness k scales inversely with dampratio squared, so dampratio=0.02 would make k enormous—about 2500x larger—which would make the contact absurdly stiff and likely unstable, since timeconst alone governs damping while dampratio drives stiffness this way.

Switching to the negative solref format instead, where b=damping/dmax and k=stiffness*d(r)/dmax², lets me directly set stiffness and damping independently. I want the contact's natural frequency tuned so the bounce period is resolvable at dt=0.002—aiming for a half-period around 10 steps (0.02s), giving ω≈157 rad/s, and solving for the corresponding k from there.

MuJoCo's semi-implicit Euler integration with constraint solving keeps energy approximately conserved, and the default solimp parameters ramp the impedance d from 0.9 to 0.95 over a small penetration width, which effectively scales down the stiffness so the actual acceleration blends the reference constraint acceleration with the unconstrained one.

I'm now double-checking the solref convention for negative values representing direct stiffness/damping specification — to be safe I should avoid a zero damping term and instead use something like -60000 for stiffness and -5 for damping, giving a natural frequency around 245 rad/s and a damping ratio near 0.01.

With a restitution coefficient around 0.95, I'm recalculating the post-collision velocities: ball1 rolling into a stationary ball2 transfers about 0.975v0 to ball2 linearly with no spin, giving roughly 0.696v0 once rolling resistance is accounted for.

I'm propagating this collision chain forward—tracking linear and spin velocities through ball1 hitting ball2, then ball2 hitting ball3, and back-reaction where ball1 catches up to ball2 again, converging toward rolling speeds around 0.21-0.3v0 for the trailing balls.

Ball1 decelerates slower than ball2 so it never catches up again, since both start at the same point and decay at the same friction rate but ball1 has lower speed. That confirms no further collisions between ball1 and ball2, so now I need to pick actual numeric values for v0, rolling friction coefficient, and the distance to the target cup.

Working through the energy balance: ball3 needs enough speed at the ramp to clear the lip height, requiring roughly u≈0.6 while the minimum is about 0.41. Testing v0=2, I check whether ball2 stops short of the ramp distance using the deceleration relation 2aD=0.581, computing ball2's stopping distance as a fraction of D to confirm it stays clear.

I then solve for the rolling friction coefficient needed to produce that deceleration at D=1.0m, getting μr≈0.00124 for the ball versus the floor's default 0.0001, while reasoning through how MuJoCo's rolling friction torque actually decelerates the ball and whether this approximation holds at higher speeds.

I'm worried the true effective friction could be softer or stiffer than planned, changing how far balls travel — if deceleration is too weak ball2 overshoots but still works out, while if deceleration is too strong (×1.5) ball3 might not have enough speed to climb the ramp. To build in margin against this uncertainty, I decide to bump up ball1's launch speed to 2.5 m/s.

Checking the f=1.5 and f=0.5 edge cases shows the design still roughly holds up, with ball3 landing in the cup at around 0.94 m/s against the back wall. Since MuJoCo's rolling friction constraint is fairly reliable, I'll settle on this μr estimate.

Working through the stopping times, ball2 travels roughly 0.57m after the collision and stops around 1.7s, ball1 stops around 1.44s — all balls come to rest well before 6 seconds. I'm double-checking the positions involved: ball2 collides with ball3 near x≈0.44, so its subsequent travel distance matches up with the deceleration figures already computed.

Now I need to figure out the ramp's starting position relative to ball3's initial location — placing it at roughly xa=1.5 based on the offset D=1.0 from ball3's start. I'm also reconsidering whether ball1 catches up to ball2 for a second collision, tracing through ball2's post-collision speed and position to see where that second interaction might occur.

I'm also verifying ball1's spin: with v0=2.5 m/s, the angular velocity ω_y comes out to 83.3 rad/s, and since the free joint's orientation is identity, the local and global frames match for the qvel entries. Then I'm checking the small ramp kink geometry — about 4.6° — and estimating that a ball moving at 1 m/s hitting this kink produces only a tiny normal velocity component, around 0.08 m/s.

Following the ball over the top edge at roughly 0.95 m/s, I'm working out its short projectile drop (about 0.007 m) and the slight upward velocity component from the ramp tilt, then estimating where it lands before rolling into the back wall. I'm placing the ball's impact point near the inner face of the back wall and considering how the low wall friction (0.1) and default contact solref parameters would produce a modest rebound given near-critical damping.

Checking whether the ball could lift slightly on impact due to spin interacting with wall friction, I'm bumping the back wall height from 0.08 to 0.1 to be safe, and calculating the escape velocity (~0.31 m/s) needed for the ball to clear the small inner step near the base.

Now I'm thinking through friction priorities: ramp and base inherit the ball's higher-friction defaults, while the low-friction walls (priority 1) use condim 3 as intended. I'm also setting the ball's rolling friction on the floor to a combo of sliding, torsional, and rolling coefficients with condim 6 for full contact resolution.

For ball-to-ball contacts I'm using condim 1 pairs with a soft negative solref for direct stiffness/damping control, checking that the resulting contact timescale is fast enough relative to the integration step to avoid instability.

I'm also verifying the penetration depth stays small relative to ball size (~1cm into a 6cm diameter ball), confirming the soft-constraint impedance is near 1 beyond the solimp width, and that the effective stiffness from the regularized solver matches the intended value despite the blending between reference and free acceleration.

Now I'm reasoning through the collision pairs between the three balls, deciding to exclude duplicate contact pairs, and setting up their initial x-positions symmetrically around the center.

I'm estimating ball2's stopping distance after collisions, checking whether rolling friction lets it reach the ramp and partially climb before rolling back, then working through ball3's arrival timing based on its post-collision velocity.

Continuing the velocity calculations, I'm checking that ball2 retains enough speed after rolling friction losses to transfer to ball3 at the next collision, and confirming ball3's resulting speed is sufficient to reach the ramp.

Now I'm deriving the rolling friction deceleration constant by working through the torque balance: friction force acts at the floor contact, producing linear deceleration while also generating a torque about the contact axis that affects the angular momentum equation, which I need to combine with the rolling constraint a = αr to get the net deceleration.

Working through the algebra, I find a = μr·g/(1.4r), giving μr ≈ 0.00178, which I'll round to 0.0018.

On MuJoCo's soft friction constraints: at low speeds they behave like heavy viscous damping that effectively halts rolling, which is what I want for a ball settling at rest against a cup's back wall with the floor stopping any residual spin. That checks out for the resting condition. Now I'm working out the cup geometry with xa=1.5, solving for h.

Computing the ramp's position and orientation: with the 0.08 rise over 1.5, I get a tilt angle near 4.57°, and from there I derive the ramp length, center coordinates, and euler rotation, then verify the top surface corners land exactly at (1.5, 0) and (1.65, 0.012) as expected.

Now I'm laying out the box geometry for the back wall and base — figuring interior wall thickness (0.02), positioning the back wall from x=1.78 to 1.80, and sizing a base box from x=1.65 to 1.78 with half-height 0.0025, while considering whether the base should extend further to support the walls.

I'm checking the end face geometry where the ramp overlaps the base slightly, which should be fine since both surfaces share similar friction settings that mix with the ball's condim 6 contact properties. Then I'm verifying ball3's entry speed of 0.75 m/s gives enough energy to climb the 0.012 lip height, accounting for rolling friction losses over the ramp distance.

With e=0.8 the gap actually fails—ball3 barely has enough energy to clear the lip while ball2 falls short too. I need to rethink the separation: maybe shorten the rolling-friction distance D or lower the cup lip so the climb cost is smaller, while still keeping ball2 from accidentally climbing in. The real design lever is tuning D and μr so the energy threshold cleanly separates ball2's arrival speed from ball3's.

Trying μr≈0.00128, which feels fragile, so I'm testing scaling v0 up to 3 instead—recomputing ball3 and ball2 arrival speeds with 2aD=1.0, checking both the e=0.8 restitution case and whether ball3 still clears the lip and hits the back wall reasonably. This version seems more robust, so I'm continuing to refine with v0=3.

Checking stop positions confirms ball2 settles around 1.14 m, well within bounds, and ball1 ends up behind it near 0.92 m, so no overlap issues. The sliding and friction phases all look consistent, and mass calculations from the default density check out to about 0.113 kg per ball.

With dynamics confirmed, I'm setting up the floor plane with appropriate size, then defining the keyframe: qpos for the three freejoint balls plus qvel values giving ball1 an initial velocity and spin, with the cup and other bodies static.

I also need to add lighting and figure out the cup's placement — I'll make the cup body sit at a fixed position with geoms defined relative to it (ramp, base, back wall, side walls), positioning the ball so it rests against the back wall inside the cup, and setting wall friction and contact properties for realistic interaction.

For contact pairs between balls, I'm defining a contact element with specific condim and solref values for stiffer collision response, and double-checking that friction limits won't let the ball slide through the wall during resting contact or the small bounce after it clears the lip.

