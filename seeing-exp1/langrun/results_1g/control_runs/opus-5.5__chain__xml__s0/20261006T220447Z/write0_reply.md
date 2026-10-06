Ball 1 starts with a rolling velocity and knocks the others along the line. The cup lies on its side with its mouth facing the balls. It is sunk so its inside bottom is flush with the floor, and ball 3 can roll straight in.

These estimates were worked by hand; I have not run the simulation.

**Collisions:** Ball-to-ball contacts are frictionless and close to elastic, so most of the momentum passes along the row.

**Stopping on the floor:** The floor has a little rolling resistance, about 0.14 m/s² of deceleration.
- Balls 1 and 2 keep only their leftover spin, so they should stop around x ≈ 0.6–0.8 m, short of the cup mouth at x = 1.1 m.
- Ball 3 is the fastest at about 0.58 m/s. It should reach the mouth at roughly 0.4 m/s, about 1.6 s in.

**Stopping in the cup:** The cup's bottom panel has stronger rolling resistance, so ball 3 should stop a few centimetres inside the cup. If it is faster than expected, the back wall catches it.

```xml
<mujoco model="three_ball_relay_into_cup">
  <option timestep="0.002"/>

  <worldbody>
    <light name="sun" pos="0.6 -1 2" dir="0 0.4 -1" diffuse="0.9 0.9 0.9"/>
    <camera name="side" pos="0.6 -1.6 0.6" xyaxes="1 0 0 0 0.35 1"/>

    <geom name="floor" type="plane" size="3 3 0.1" pos="0 0 0" rgba="0.8 0.8 0.75 1" condim="6" friction="1 0.001 0.0006"/>

    <body name="ball1" pos="0 0 0.03">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.03" density="1000" friction="1 0.001 0" rgba="0.85 0.2 0.2 1"/>
    </body>

    <body name="ball2" pos="0.2 0 0.03">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.03" density="1000" friction="1 0.001 0" rgba="0.2 0.6 0.2 1"/>
    </body>

    <body name="ball3" pos="0.4 0 0.03">
      <freejoint name="ball3_free"/>
      <geom name="ball3_geom" type="sphere" size="0.03" density="1000" friction="1 0.001 0" rgba="0.2 0.3 0.85 1"/>
    </body>

    <!-- Cup lying on its side: octagonal shell around the x axis, mouth at x=1.1, closed back at x=1.24, inner bottom flush with floor -->
    <body name="cup" pos="1.17 0 0.06">
      <geom name="cup_bottom" type="box" size="0.07 0.027 0.003" pos="0 0 -0.063" euler="0 0 0" condim="6" friction="1 0.001 0.01" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_45" type="box" size="0.07 0.027 0.003" pos="0 0.04455 -0.04455" euler="45 0 0" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_90" type="box" size="0.07 0.027 0.003" pos="0 0.063 0" euler="90 0 0" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_135" type="box" size="0.07 0.027 0.003" pos="0 0.04455 0.04455" euler="135 0 0" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_180" type="box" size="0.07 0.027 0.003" pos="0 0 0.063" euler="180 0 0" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_225" type="box" size="0.07 0.027 0.003" pos="0 -0.04455 0.04455" euler="225 0 0" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_270" type="box" size="0.07 0.027 0.003" pos="0 -0.063 0" euler="270 0 0" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_315" type="box" size="0.07 0.027 0.003" pos="0 -0.04455 -0.04455" euler="315 0 0" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_back" type="cylinder" size="0.069 0.003" pos="0.073 0 0" euler="0 90 0" rgba="0.85 0.6 0.15 1"/>
    </body>
  </worldbody>

  <contact>
    <exclude name="ex12" body1="ball1" body2="ball2"/>
    <exclude name="ex23" body1="ball2" body2="ball3"/>
    <exclude name="ex13" body1="ball1" body2="ball3"/>
    <pair name="pair12" geom1="ball1_geom" geom2="ball2_geom" condim="1" solref="-50000 -1"/>
    <pair name="pair23" geom1="ball2_geom" geom2="ball3_geom" condim="1" solref="-50000 -1"/>
    <pair name="pair13" geom1="ball1_geom" geom2="ball3_geom" condim="1" solref="-50000 -1"/>
  </contact>

  <keyframe>
    <key name="start" qpos="0 0 0.03 1 0 0 0  0.2 0 0.03 1 0 0 0  0.4 0 0.03 1 0 0 0" qvel="1.2 0 0 0 40 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm planning out a scene with three balls in a row along the x-axis, where the first ball gets an initial velocity and collisions transfer momentum between them. I need to account for soft contact physics in MuJoCo affecting exact momentum transfer, and set up initial angular velocities so the balls roll naturally with friction rather than just sliding.

For the cup design, I'm considering how a ball could enter it realistically — since the floor is a flat plane without holes, a standing cup with walls would require the ball to clear the rim, which seems awkward. I'm leaning toward orienting the cup on its side like a sideways cylinder made of boxes, so the ball rolls directly into an opening facing it and stops against a back wall, avoiding the need for a ramp.

Maybe better to tilt the cup sideways on the floor with its mouth facing the balls, keeping the bottom panel's top surface flush with z=0 so the ball transitions seamlessly from floor to cup interior without a bump, since it's a static body and self-collision isn't an issue.

However, I realize the ball could just bounce back out after hitting the cup's back wall if restitution isn't dissipated enough — default contact damping in MuJoCo isn't perfectly inelastic, so the ball might slowly creep back out. Tilting the cup's interior floor downward toward the back wall would help trap it, but that would push the interior below the floor plane, which would then cause unwanted collisions between the ball and the floor itself.

Actually with near-zero restitution the ball shouldn't bounce back, but its forward spin could keep driving it into the wall via floor friction, and the wall's friction response to that spin might push it upward rather than settling — I need to check if that spin-wall interaction could cause the ball to climb or pop out of the pocket instead of resting.

Given this uncertainty, a safer approach is a different cup geometry entirely: build the cup upright but with a ramp integrated into its body, so the ball rolls up and over the rim and drops in from above. Using rolling energy conservation, (7/10)v² = gh, a rim height of 0.06m needs an approach speed around 0.92 m/s — I should add margin for this so the ball doesn't overshoot the cup on the other side.

Adding condim 6 with rolling friction on the ball could work, but I'd need to calculate the deceleration carefully so it slows the ball without stopping it too far from the cup. Maybe better to concentrate high rolling friction just on the cup's interior bottom panel, since contact friction takes the max across geoms — that way the ball travels normally until it enters the cup, then decelerates sharply once inside.

A side-lying cup would realistically rest on its wall's outer surface, meaning the interior bottom sits at a height equal to the wall thickness—too tall a step for the ball to roll over without a ramp. Simpler to just sink the wall below the floor so the cup's bottom is flush with the floor itself, letting the floor plane effectively serve as the cup's bottom and avoiding the lip problem entirely.

Friction is default so collisions transfer some spin between balls, which seems fine. For rolling friction I'm thinking through MuJoCo's friction parameters — sliding, torsional, and rolling coefficients — where the rolling term acts as a constraint opposing angular velocity, so a value like 0.02 with the ball's radius would bring it to rest fairly quickly.

Now I'm working out positions and velocities: balls with radius 0.03 and default density, spaced along x at 0, 0.3, and 0.6, with the cup mouth at 0.9. I'm setting the first ball's initial velocity and figuring out the angular velocity needed for rolling without slipping, working through the cross product of angular velocity and contact point to match the rolling condition.

Then I'm thinking through the first collision—ball1 hitting ball2 with equal masses transfers most of the linear momentum while ball1 retains its spin, so friction then re-accelerates ball1 forward toward a new rolling speed, using conservation of angular momentum about the contact point to work out the post-collision rolling velocity.

Following the momentum chain: ball1 ends up rolling at about 0.29 m/s while ball2 picks up roughly 5/7 of the initial speed, around 0.71 m/s. Ball2 then strikes ball3, handing off most of its speed (ball3 ends up at ~0.51 m/s toward the cup) while ball2 retains some spin-driven speed around 0.2 m/s, and ball1 trailing behind at 0.29 m/s threatens to catch up to ball2 — so it looks like all three balls could end up heading into the cup, possibly even ball2 along with ball3.

Since the problem likely wants only ball3 to end at rest in the cup, I need to stop ball1 and ball2 from reaching it without friction losses on the floor halting their momentum naturally. I'm considering introducing a small rolling friction coefficient on the floor so ball1 and ball2 decelerate and stop short of the cup while ball3, launched with enough speed, still makes it in.

Simplifying to a = 5μ_r g/(7r) confirms my formula. Checking travel distances with μ_r=0.0003: ball3 covers 1.86m, ball2 0.29m, ball1 0.6m but catches ball2 — not ideal, so I'm considering raising μ_r to 0.001, giving a=0.234 m/s², and re-checking how far ball1 travels before colliding.

I'm also worrying about whether MuJoCo's default spring-damper contact model gives near-elastic collisions — with critical damping, the contact force drops to zero before full separation, meaning the effective restitution isn't zero even without explicit restitution set, since the clamped constraint force releases at nonzero relative velocity.

That's too inelastic — ball1 would keep too much velocity. I need more elastic contacts, so I should try a lower damping ratio in solref, maybe something like "0.004 0.05", since a smaller dampratio gives higher restitution (e approaching 0.73-0.85 range rather than 0.13).

But I realize timeconst needs to be at least twice the timestep (0.002), so 0.004 is right at the edge and might clamp or cause instability with discrete integration — better to bump timeconst up to 0.01 and work out the implied stiffness and damping from MuJoCo's formulas relating timeconst, dampratio, and the natural frequency of the contact.

I'm checking stability limits against ωdt for different timeconst/dampratio combos, trying to balance accuracy against penetration depth at impact velocity — settling on something like T=0.05, ζ=0.1 giving reasonable penetration for a 30mm radius ball, though maybe larger balls would help. I'm also considering an alternative approach using direct negative solref values for near-elastic contact with zero damping.

With d around 0.9-0.95, effective stiffness becomes d*k, giving near-ideal elastic transfer in the cradle—ball1 stops linearly while retaining spin, and ball2 picks up the linear velocity without spin. But I need to be careful: if solref is only set on the balls, contacts with the floor or cup will mix ball and floor solref parameters via solmix, which is problematic when combining negative and positive solref values. It's probably better to use explicit contact pairs for ball-to-ball interactions to isolate this elasticity setting.

So I'd define explicit pairs for ball1-ball2, ball2-ball3, and ball1-ball3 with their own solref—since explicit pairs are added alongside dynamic contacts rather than replacing them, and the exclude element only removes dynamic broadphase-generated contacts, not explicit pairs, so there shouldn't be unwanted duplication issues there. Alternatively, I could simplify and just accept a lower restitution where ball1 keeps some velocity plus spin, ball2 gets the rest, and this partial transfer cascades through to ball3 when it gets hit next.

Working through the friction physics at each collision: with ball1 spinning and ball2 stationary, the contact-point surface velocities differ, so friction acts on that vertical slip—pushing ball1's leading edge upward (which reduces its spin and lifts it slightly) while pressing ball2 downward into the floor, with the friction impulse capped by the normal impulse times the friction coefficient.

I want to keep pair friction between balls low or effectively frictionless so collisions don't produce unwanted hopping. Then I'm tracing the post-collision motion: ball1 ends up nearly at rest but spinning fast, and floor friction converts that spin into rolling at roughly 2/7 of the original speed, letting it trail behind and eventually catch up to ball2, which rolls off at about 5/7 speed with no spin; ball3 then inherits a similar fraction once it gets struck, and I'm working out the sliding-to-rolling transition time assuming high friction.

Ball3 ends up fastest (~0.51 v0) while balls 1 and 2 are slower (~0.27-0.29 v0), so rolling friction needs to stop the two slower balls before the cup while ball3's stopping distance is roughly 3x further given the squared speed ratio. I should pick a floor friction deceleration rate, something like a = 5μ_r g/(7r), and work out positions accordingly.

Setting ball radius at 0.03 with balls spaced at x=0, 0.15, 0.30, I want the cup mouth placed so ball3 arrives there with enough leftover speed for the cup's own stronger friction to finish stopping it, while balls 1 and 2 stall out short of the mouth using their smaller stopping distance.

Trying v0=1.2 and deceleration a=0.15, I'm computing ball3's stopping distance against the required mouth position to confirm the geometry works.

With L=0.7m, ball3 arrives at the mouth with about 0.40 m/s remaining, taking roughly 1.4s, while balls 1 and 2 stop around 0.66m - well short of the mouth, giving good margin.

I'm second-guessing how MuJoCo actually models rolling friction here - whether it's a constant decelerating torque or something closer to a frictional cone constraint that could behave differently than my simplified physics assumes.

Working through the friction coefficient: μ_r comes out to roughly 0.0006, giving a deceleration around 0.14 — small enough not to significantly affect my margin calculations, though I should double check the torsional friction component in condim 6 too.

Checking the contact friction combination rules: since MuJoCo takes the max across each component, the ball's default torsional friction of 0.005 would carry through even though it's negligible here with no spin about z — I'll just zero out the ball's rolling and torsional friction explicitly to be safe. For the ball-ball contact pair I'm working out appropriate solref values, settling on a stiff negative spring constant with a small damping term to avoid excessive bounce.

I'm reconsidering restitution e=0.8: ball1 keeps some linear velocity plus spin, giving roughly 0.357v0, ball2 about 0.643v0, and ball3 trailing near 0.41v0, with rolling friction likely closing the gaps enough that each ball still reaches its target despite the lower transferred speed.

The solver's impedance varies with penetration but stays symmetric between loading and unloading, so it stays conservative overall, and symplectic Euler should keep energy roughly bounded—e should land around 0.95+. Timing-wise, ball1's spin-up to rolling takes about 0.04s while ball2 covers the 0.09 gap to ball3 in 0.08s, so there's no interference risk; I'm now considering whether giving ball1 zero initial spin would avoid the follower issue.

I could also consider a near Newton's-cradle setup where balls touch almost directly: ball2 passes nearly all its velocity to ball3 with little spin, leaving ball1 with most of the backspin at 2/7 v0 while ball3 rolls at close to 5/7 v0, giving a better separation ratio. But with a small gap, ball2 picks up partial spin before hitting ball3, so I need to work out the friction deceleration over that gap distance to see how much spin transfers.

I'm settling on concrete numbers: ball radius 0.03, deceleration 0.14 for rolling resistance, balls positioned at 0, 0.2, and 0.4, cup mouth at 1.1, initial velocity 1.2 and spin 40, then tracking how far ball1 travels before its spin and velocity equalize into pure rolling.

Now I'm chaining through the collisions: ball1 hits ball2 at roughly 1.18 m/s, transferring motion so ball2 ends up rolling near 0.82 after a brief slide, which then passes about 0.585 to ball3, while ball1 and ball2 settle into their own post-collision rolling speeds based on angular momentum conservation.

Tracking each ball's free-rolling distance to the mouth at x=1.1, I find they all arrive with comfortable margins—roughly 0.4 m of slack even accounting for a less elastic coefficient like e≈0.85, so the setup should work.

Now I'm sketching the cup's geometry: lying on its side with its axis along x, mouth at x=1.1, inner radius equal to twice the ball radius, and the bottom interior sitting at z=0 so the axis height is 0.06.

I'm approximating the curved shell by arranging eight box "staves" rotated around the axis, positioning each so the bottom one sits mostly below floor level and sizing them to the inner radius plus wall thickness, then placing the back cap as a disk further along x to close the cup.

Using half-width ~0.027 I compute all eight stave positions around the octagon, checking that the inner surface sits flush at radius 0.06 for the φ=0 case, then I check whether the staves at 45° and 315° still clear the ball positioned at z=0.03 on the world axis.

I'm working through the clearance math for the ball against the 45° stave plane and finding about 0.009 margin, which is enough. Then I verify the bottom stave's flat span covers the ball's resting position with zero lateral drift, confirming the ball sits properly without touching the edges.

For the back disk geometry, I'm placing it at the body's edge with a small radius and half-length, rotated so its axis points along x, noting the bottom half dips below the floor but stays hidden visually. Then I estimate the deceleration of ball 3 on the high-friction bottom stave, calculating it stops within about 1.6cm after entering at 0.39 m/s, and start checking where the ball's center needs to be when it first contacts the stave's front edge at x=1.1.

Testing a lower rolling friction coefficient around 0.008 to get the ball to travel deeper into the cup across the likely speed range of 0.23-0.5 m/s, I check scenarios where faster balls might hit the back wall at x=1.24 and settle there via rolling friction after a soft bounce.

Actually, I realize the margin is thin for the slowest speed case, so I'm reconsidering μ_r=0.005 instead, which gives better spread across the full speed range while still keeping the fast-ball case within the back wall. I'm also second-guessing how rolling friction actually distributes between the two simultaneous contacts (floor and cup wall) when the ball rests on both, since the normal force split between them is indeterminate.

A raised step edge might cause a small hop at the stave lip, but with a 1mm step and 30mm radius the velocity bump would be tiny, so it's probably fine. To avoid odd edge-hop risk entirely though, I think I'll just keep the stave flush with the floor and set cup rolling friction to 0.01 for an effective ~0.005 — simpler and safer, just need to double check the box edge collision behavior at x=1.1 as the ball approaches it.

I'm also confirming the balls settle properly: rolling friction brings balls 1 and 2 to rest on the floor, ball 3 stops against the back wall, and any later push from ball 1 onto ball 2 is already accounted for.

On the contact model, I'm sticking with the default pyramidal cone at condim 6 since it combines normal and friction directions fine, but worried that torsional friction of exactly 0 could be degenerate for a condim-6 pyramid — so I'll set torsional to a small nonzero value like 0.001 instead, giving floor friction "1 0.001 0.0006". Then the effective ball-floor friction will be the max between the floor's and ball's friction settings.

Setting ball friction values and tuning cup geom friction, I'll only apply condim 6 with a small rolling coefficient to the bottom stave since that's the only surface that really needs it. For ball-ball contacts I'm defining a pair with condim 1 and a negative solref for stiffness/damping, checking whether both values need the negative sign convention.

I'm digging into how MuJoCo interprets negative solref values—when solref[0] is negative, it switches to direct stiffness/damping mode rather than the standard time-constant/damping-ratio formulation. Using a small damping value like 1 against the natural frequency of ~212 gives a negligible damping ratio, so I want to verify how the reference acceleration gets computed from these parameters to make sure the scaling is right.

Working through the effective stiffness with impedance scaling, the numbers come out to around 40000 giving ω≈200, which checks out fine for penetration depth at that impact speed—roughly 6mm, acceptable.

Now I'm considering how to exclude unwanted ball-pair contacts using the exclude element, and whether explicit pair definitions would still get auto-generated despite the exclusion.

I'm confident now that explicit pair elements bypass the exclude filtering entirely, and pair margin defaults to zero. For the keyframe, I'm setting up qpos for the three free-jointed balls spaced along x at 0.2m intervals with z=0.03, giving ball1 an initial velocity of 1.2 m/s forward plus some angular spin, while the other two start at rest—since angular velocity for a freejoint is in body frame which matches world frame at identity orientation. The cup itself is static with no joints or actuators, so its keyframe entry is just the fixed qpos values. Now I'm thinking through whether the balls will properly collide with the cup's staves walls.

Checking the timing: ball3 gets struck around 0.2s and travels roughly 0.7m, arriving near 1.6s, well within the 6s simulation window, and balls 1/2 decelerate and stop around 2.4s due to friction—all consistent with the setup. With mass and physical parameters confirmed reasonable (sphere density 1000, radius 0.03 giving about 0.113 kg), I'm ready to finalize the scene description and move on to writing the back wall geometry, positioning its cylinder slightly offset in x to account for wall thickness.

Figuring out the back and side stave positions, making sure the bottom staves sit at or slightly below floor level without creating collision issues since both are static bodies. Everything checks out geometrically, so now I'll write the complete file.

