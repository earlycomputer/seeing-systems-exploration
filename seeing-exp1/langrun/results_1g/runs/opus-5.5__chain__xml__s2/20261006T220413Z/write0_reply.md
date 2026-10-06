Ball1 starts rolling at 4 m/s and runs into ball2, which then runs into ball3. Ball3 rolls up a gentle ramp onto a 5 cm platform and drops into a low box cup. The ball-ball contacts are springy (low damping), so the momentum is passed down the chain. The cup's geoms have strong rolling friction, so a ball that lands inside stops, and the 5 cm step keeps it from rolling back out.

Ball1 and ball2 keep some of their rolling speed after each hit. They may follow ball3 over the ramp, so the cup is long enough to hold all three balls.

```xml
<mujoco model="three_ball_chain_into_cup">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.8 -1 2" dir="0 0.4 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="3 1 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="ball1" pos="0 0 0.03">
      <freejoint/>
      <geom name="ball1_geom" type="sphere" size="0.03" solref="0.005 0.1" rgba="0.9 0.2 0.2 1"/>
    </body>
    <body name="ball2" pos="0.3 0 0.03">
      <freejoint/>
      <geom name="ball2_geom" type="sphere" size="0.03" solref="0.005 0.1" rgba="0.2 0.8 0.2 1"/>
    </body>
    <body name="ball3" pos="0.6 0 0.03">
      <freejoint/>
      <geom name="ball3_geom" type="sphere" size="0.03" solref="0.005 0.1" rgba="0.2 0.3 0.9 1"/>
    </body>

    <geom name="ramp" type="box" pos="1.20062 0 0.02004" euler="0 -7.125 0" size="0.20156 0.1 0.005" rgba="0.6 0.4 0.2 1"/>
    <geom name="platform" type="box" pos="1.45 0 0.025" size="0.05 0.1 0.025" rgba="0.6 0.4 0.2 1"/>

    <body name="cup" pos="1.5 0 0">
      <geom name="cup_base" type="box" pos="0.175 0 0.0025" size="0.175 0.1 0.0025" condim="6" friction="1 0.01 0.01" rgba="0.9 0.7 0.1 1"/>
      <geom name="cup_near" type="box" pos="0.005 0 0.025" size="0.005 0.1 0.025" condim="6" friction="1 0.01 0.01" rgba="0.9 0.7 0.1 1"/>
      <geom name="cup_far" type="box" pos="0.345 0 0.075" size="0.005 0.1 0.075" condim="6" friction="1 0.01 0.01" rgba="0.9 0.7 0.1 1"/>
      <geom name="cup_left" type="box" pos="0.175 0.105 0.075" size="0.175 0.005 0.075" condim="6" friction="1 0.01 0.01" rgba="0.9 0.7 0.1 0.5"/>
      <geom name="cup_right" type="box" pos="0.175 -0.105 0.075" size="0.175 0.005 0.075" condim="6" friction="1 0.01 0.01" rgba="0.9 0.7 0.1 0.5"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 0 0.03 1 0 0 0 0.3 0 0.03 1 0 0 0 0.6 0 0.03 1 0 0 0" qvel="4 0 0 0 133.333 0 0 0 0 0 0 0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
ball1 touches ball2
ball2 touches ball3
ball3 touches ramp
ball3 comes to rest in cup
```

---
thinking (summarized):

I'm thinking through how to set up three balls in a row using free joints, with the first ball getting an initial push and transferring momentum through collisions until the third rolls into a cup—accounting for rolling friction and how spin versus sliding affects the energy transfer between equal-mass spheres.

Since MuJoCo's default contacts are fairly soft and inelastic (critically damped), I'm considering tuning the solref parameters to make collisions bouncier so the first ball transfers more of its momentum forward rather than all three balls clumping together and moving as one, ensuring the third ball reaches the cup cleanly.

I also realize there's no rolling friction by default, so balls would roll indefinitely — I need to think through how the cup is actually positioned relative to the floor, maybe as a low-walled enclosure with an open front that the ball can roll into, rather than something it would need to climb.

For the energy transfer: a ball rolling at v0 hits a stationary one, and with elastic collision and no induced spin on the second ball, its rolling speed afterward becomes reduced relative to pure translational velocity until friction restores rolling without slipping, which I need to account for when calculating whether it clears the rim height.

So I'm leaning toward a simpler design: skip the embedded cup and instead use a shallow box with low walls as the cup, approached by a gentle ramp that leads up to the rim. The ball rolls up, launches slightly over the rim edge, and drops in—avoiding the need for a floor hole while keeping wall height modest relative to ball radius.

I'm thinking through the physics of what happens once the ball lands inside: with default contact damping it should lose energy on each wall bounce, and rolling friction against the floor should eventually damp out any residual spin-driven motion so the ball settles rather than oscillating forever. I might need to bump up condim on the cup floor geoms to get enough rolling friction for that settling behavior.

Since condim is the max of both geoms, I could give cup geoms condim 6 with strong rolling friction so the ball settles there while the floor stays frictionless for rolling. For the ramp, I'm considering making it a separate static body with its own geom using normal condim 3, though I'm now second-guessing whether the ramp approach is even the simplest way to get the ball moving.

Now I'm working out the rolling kinematics: with radius 0.03 and roughly 0.113 kg mass from default density, placing balls along x at 0, 0.3, 0.6, and deriving that for a ball rolling in +x on the floor, the angular velocity about y equals v/r (positive), since the contact point velocity must vanish — v minus r·ω_y equals zero.

I'm estimating the collision chain with a coefficient of restitution around 0.8: ball1 transfers most of its momentum, ball2 ends up with linear speed ~2.25 m/s before settling into rolling at 5/7 of that (~1.61 m/s), then ball3 picks up ~1.45 m/s translating to ~1.03 m/s rolling, while ball1 retains a small residual speed from the partial transfer.

This actually resembles a Newton's cradle on a rolling floor — all three balls end up moving forward at decent speeds toward the ramp, since ball1 recoils and can catch up and hit ball2 again. This raises the question of whether ball2 also ends up in the cup, which may or may not be a problem depending on whether the cup can hold multiple balls — I'll treat that as acceptable as long as ball3 is the one confirmed to land in it.

I'm reconsidering the approach—maybe it's safer to not rely on precise velocity margins at all. Instead of fine-tuning speeds so only ball3 clears the ramp, I could just accept that multiple balls might end up near or in the cup, and size the cup to hold a few balls. Then I'd simplify my success criteria to something robust like "ball1 touches ball2," "ball2 touches ball3," and "ball3 comes to rest in cup," rather than requiring exact exclusivity.

I'm working out the ramp-to-cup transition: a gentle 5.7° slope losing about 0.42 m²/s² of speed to a 0.03 m rise, so an incoming ball near 1 m/s should clear it with margin while slower balls near 0.65 m/s are right at the edge. Now I need to make sure the cup rim height matches up with the ramp top so a ball crossing over actually falls in rather than skating past.

Checking whether the ball can escape the cup once inside — with a 2 cm wall against a 3 cm ball radius, the ball's center sits above the wall top, so it could technically climb back out if it keeps enough speed, though rolling friction inside the cup should bleed off most of that energy. I'm considering raising the ramp height to 0.06 to give more clearance and make sure the ball settles rather than escaping.

I also need to account for how MuJoCo's soft contact parameters (dampratio) translate into effective restitution — a damping ratio of 0.2 gives roughly 0.53 effective bounce, while 0.1 gives about 0.73 — and I need to tune the initial velocity and restitution assumptions so each successive bounce (ball1 → ball2 → ball3) still has enough energy to behave realistically without being too marginal.

Recomputing: after the ramp, ball1's post-collision speed ends up faster than ball2's post-collision speed, so there's a risk ball1 catches up and collides with ball2 again, speeding it up further. This chain reaction could push both ball1 and ball2 into the cup rather than just ball2, so I need to check the cup's interior length (~0.3) against how many balls might actually arrive.

For the physical layout, I'm thinking the ramp should feed into a flat lip at the same height as the top of the near cup wall, so the ball rolls straight across rather than needing a separate drop. Simplest approach: build a solid platform box up to 0.05 height, have the ramp lead into it, then immediately follow with the cup enclosure whose floor sits near z=0 with a thin base plate — the ball rolls off the platform and drops directly into the cup.

For friction inside the cup, I'm setting condim 6 on the cup floor with rolling friction coefficients to properly damp the ball's motion once it lands, checking that the rolling friction torque scales sensibly given the ball's radius.

The friction values need to use the max across sliding, torsional, and rolling components, so I'll combine ball and cup defaults accordingly. For the ramp, I'm computing a shallow 7.1° incline angle from the 0.05 rise over 0.4 run, which should be gentle enough not to cause a jarring bounce at the kink, and now I'm sizing the thin ramp box geometry to match.

Computing the slope length and half-length for the ramp geometry, then checking that the box meets the floor cleanly at the lower edge since world geoms don't collide with each other anyway. I'll stick with the box approach rather than switching to a cylinder, and now I'm positioning the platform box at the top of the ramp with its center and half-extents.

Then laying out the three balls along x at 0.3 spacing, radius 0.03, sitting at z=0.03, with the ramp spanning 1.0 to 1.4 and the platform 1.4 to 1.5. I'm working out the cup geometry next — base plate and near wall dimensions and positions relative to the cup body frame.

I'm checking the far wall, taller at the back (height 0.15) centered further along x, and the two side walls which run the length of the cup and also stand 0.15 tall. Since everything stays on the y=0 centerline by symmetry, I only need to verify x and z collisions, and the side walls near the platform entrance look tall enough that a ball rolling straight in wouldn't clip them.

Tracing the trajectory: the ball leaves the platform at 1.2 m/s and falls about 0.045 m before landing inside the cup near x≈1.5+0.12, which lands it safely inside. From there, rolling friction decelerates it at roughly 2.3 m/s², which means from 1.2 m/s it would travel about 0.31 m before stopping — comfortably less than the 0.33 m gap to the far wall, so it should settle inside without colliding.

Checking timing across all three balls: ball1 at 4 m/s reaches ball2 in about 0.06 s, ball2 at 2.4 m/s reaches ball3 in about 0.1 s, and ball3 takes roughly 0.25-0.3 s to cross the ramp and land in the cup by about 1 second in — well within the 6 second window, with plenty of room for the cup to hold all three balls given its 0.33 m interior length versus each ball's 0.06 m diameter.

The far wall should absorb most energy so the ball settles back into the cup without escaping, and the cup height is tall enough to prevent any ball from flying out. Now I'm setting up the initial keyframe with position and velocity values for the three free-jointed balls, giving ball1 forward velocity and spin while the others start at rest.

I'm checking contact solver parameters -- ball-ball softness with a short time constant stays above the minimum allowed relative to the timestep, so it should be stable without excessive jitter, and the spin rate on ball1 seems reasonable. I'm also confirming the near wall's top edge aligns with the platform surface so the ball transitions smoothly without catching on a lip.

Now I'm finalizing the scene with lighting and a properly sized floor plane, then writing out the file. I'm listing the expected contact sequence -- ball1 to ball2, ball2 to ball3, ball3 to the ramp, and ball3 settling in the cup -- and need to write the checker that verifies the ball actually comes to rest inside the cup.

