The pendulum starts held at about 37° and swings down. Its 1 kg bob strikes the 5 cm ball at the bottom of the arc and sends it rolling along +x. The ball climbs a 12° ramp, drops over a low front lip into a boxy cup centred at x = 1 m, and settles there. The cup's back and side walls are tall and thick so a fast ball cannot get over or through them.

I have not run this. Every number below comes from hand calculations, so the speed targets are estimates.

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.5 -1 2" dir="0 0.5 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- Pendulum: pivot 0.5 m above the bob centre; bob centre at ball height (0.03) at the bottom of the swing, 0.5 mm short of touching the ball -->
    <body name="pendulum" pos="-0.0555 0 0.53">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.47" size="0.005" mass="0.02" contype="2" conaffinity="2" rgba="0.3 0.3 0.3 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.025" mass="1" contype="2" conaffinity="2" rgba="0.8 0.2 0.2 1"/>
    </body>

    <!-- Ball resting on the floor at x = 0 -->
    <body name="ball" pos="0 0 0.03">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" mass="0.05" condim="6" friction="1 0.005 0.0003" contype="1" conaffinity="3" rgba="0.2 0.4 0.9 1"/>
    </body>

    <!-- Cup centred at x = 1 m: ramp, low front lip, tall thick side/back walls, thin base -->
    <body name="cup" pos="1 0 0">
      <geom name="cup_ramp" type="box" pos="-0.162 0 0.0102" euler="0 -12 0" size="0.1 0.055 0.01" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_base" type="box" pos="0.015 0 0.002" size="0.08 0.085 0.002" rgba="0.5 0.5 0.6 1"/>
      <geom name="cup_front" type="box" pos="-0.06 0 0.019" size="0.005 0.055 0.019" rgba="0.5 0.5 0.6 1"/>
      <geom name="cup_back" type="box" pos="0.075 0 0.06" size="0.02 0.085 0.06" rgba="0.5 0.5 0.6 1"/>
      <geom name="cup_left" type="box" pos="0.015 0.07 0.06" size="0.08 0.015 0.06" rgba="0.5 0.5 0.6 1"/>
      <geom name="cup_right" type="box" pos="0.015 -0.07 0.06" size="0.08 0.015 0.06" rgba="0.5 0.5 0.6 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.6435 0 0 0.03 1 0 0 0"/>
  </keyframe>
</mujoco>
```

How the parts are expected to behave:

- **Strike speed.** Releasing from cos θ = 0.8 should give a bob speed of about 1.4 m/s at impact. Allowing for soft-contact restitution, the bob pushing the ball again, and the ball sliding before it rolls, I expect the ball to roll at roughly 1.1–1.5 m/s.
- **Ramp.** The ball needs about 0.75 m/s to climb the 4 cm ramp.
- **Cup.** The back wall is 0.12 m tall and 4 cm thick, so even the fastest case should stay inside.
- **Coming to rest.** The ball has a small rolling friction (condim 6). Together with the energy lost in wall contacts, this should bring it below 5 cm/s well before 6 s.
- **Collisions.** The pendulum geoms use contype/conaffinity 2, so they collide only with the ball, never the floor or the cup.

---
thinking (summarized):

I'm thinking through the physics setup: a small ball with radius 0.03m rolling on a floor with sliding friction but no rolling resistance, meaning it would keep rolling indefinitely, so I need a cup with walls to actually capture and stop it.

I'm considering making the cup a ring with a ramp so the ball can roll up and drop inside, requiring enough speed to climb the ramp height but then needing to settle below 5cm/s within 6 seconds. To make the ball actually come to rest rather than bounce around forever, I should add rolling friction to the ball's contact properties so it decelerates naturally once inside.

Alternatively, I'm thinking a snug-fitting cup, where the inner radius is just slightly larger than the ball, could trap it quickly since MuJoCo's default contact damping dissipates bounce energy, helping the ball settle faster without needing precise rolling-friction tuning.

Let me place the cup centered at x=1 with a ramp leading up to the rim on the approach side, so the ball launches off the ramp and falls into the cup. I need the fall time from rim height to cup floor and the horizontal distance traveled to stay within the cup's inner radius so it lands inside rather than overshooting the far wall.

Actually I realize the far wall could be a problem — since the ball's center is still above the wall height when it reaches that side, it might clip the rim edge and bounce outward instead of staying contained. To fix this, I'll make the far wall taller than the near wall, creating an asymmetric cup shape that better traps the ball.

For the ramp, I'm thinking of using a tilted box that intersects the floor level, since both the ramp and floor are static bodies and static-static collisions aren't computed in the physics engine, this should work cleanly without extra joint complexity.

I'm sketching out the speed math: with a front wall height of 0.04 and ball radius 0.03, rolling up requires v>0.75 m/s to clear it, so I'm targeting an impact speed around 1.2 m/s, giving roughly 0.94 m/s at the ramp top before it drops into the cup.

Then I work through the fall into the cup interior, factoring the ramp's launch angle (~12-15°) adding upward velocity, and the cup's dimensions (floor thickness, interior length ~0.12 m, back wall height 0.12) so the ball lands, hits the back wall, and rattles rather than overshooting. I'm also calculating the horizontal run needed for the ramp to climb 0.04 m at a 12° angle (~0.188 m) and how that ramp edge should meet the front wall's top for a smooth transition.

I consider simplifying the geometry: instead of a separate thin front wall, let the ramp's tilted top surface serve as the lip into the cup, accepting that a tilted box creates a tilted end face and minor discontinuities are fine. I weigh whether to keep simple box shapes versus a cylindrical cup base, and think about whether the ball rolling up a 12° ramp transitions smoothly at the floor junction or creates a small kink the ball would bump against.

I estimate roughly a 4% energy loss from the ramp's angled impact, which seems acceptable, then work out the actual placement: ball at x=0, cup center at x=1.0, cup interior spanning 0.94–1.06 with a 0.12 width to fit the 0.06 diameter ball, plus a thin front wall at x≈0.935 with small thickness and 0.04 height.

I decide the cup needs a thin base (half-thickness 0.002, centered at z=0.002) rather than just resting directly on the floor, so the ball sits properly inside. Then I work out the ramp geometry: it needs to reach z=0.04 at x=0.93 with a 12° slope, giving a run of about 0.188, so the ramp spans from x=0.742 to x=0.93, and I calculate the box half-length along the slope to be about 0.1.

Working out the rotation math for tilting the ramp box about the y-axis by -12° so its surface normal aligns correctly with the slope direction...

I'm computing the box center position by offsetting from the midpoint of the slope segment along the normal direction, then checking the top surface extends properly from x=0.738 to x=0.934, noting the far end slightly overlaps where the front wall sits.

Actually the ramp's high end overlaps the front wall's position, and I'm worried about a thin gap under the ramp near the wall — the slab is only 0.02 thick, leaving empty space below it down to the floor, and I need to check whether a ball (0.06 diameter) rolling back toward the front could get caught or pass under that gap.

I'm computing the exact gap height at the ramp's end and confirming the ball will hit the ramp's end face rather than slip through, so it's safe to still add a thin front wall just below the ramp edge for solidity. I'm setting the front wall slightly lower than the ramp end so the ball clears it cleanly, then working out where the cup interior should sit — centered around x=1.0, spanning roughly 0.945 to 1.055 — before placing the back wall.

Sizing the back and side walls, checking ramp width versus cup width, and deciding to position the cup body at (1,0,0) with all geoms defined relative to that center. I'm also tracing where the ball's center will be as it leaves the ramp edge to confirm it lands inside the cup's interior bounds.

I'm checking that the ball clears the front wall's top edge while still rising, which it does comfortably. I'm also testing speed variability — faster launches just hit the back wall harder without clearing it, and slower ones still carry enough momentum post-kink, so a 1.2–1.5 range seems safe. Then I'm thinking through whether the ball will actually settle inside the small cup within 6 seconds given bouncing between close walls.

Each wall collision should dissipate energy under the default solver settings, and even with rolling spin, the ball pressed against a wall should have its spin killed by wall friction while floor friction keeps it damped, so it likely settles fine. To be extra safe, I'm considering switching the ball to condim 6 with a small rolling friction coefficient to guarantee decay.

Checking defaults: floor rolling friction is 0.0001 but ball's 0.0003 dominates since MuJoCo takes the max across contacting geoms, and condim/cone type (pyramidal) stay default, so that resolves cleanly. Now shifting to the pendulum strike geometry — the hinge pivots about the y-axis above the ball, and the bob swings down to hit the ball moving in +x at the bottom of its arc, with the ball sitting at x=0, z=0.03.

I'm placing the pivot slightly offset in x so the bob's bottom-of-swing position just grazes the ball's contact point, accounting for the bob's 0.04 radius versus the ball's 0.03 radius — positioning it so contact happens just before dead-bottom to keep the impulse mostly horizontal.

Shrinking the bob radius to 0.025 keeps its bottom clear of the floor at z=0.03. I also need to make sure the pendulum doesn't collide with the floor itself, so I'm setting contype/conaffinity bits so the pendulum only interacts with the ball and not the ground plane, verifying the bitmask logic works out so ball-pendulum collisions still register.

Now I'm thinking about momentum transfer during the collision — MuJoCo's default soft contact with critical damping behaves closer to inelastic, so I need to consider how much restitution the default solref actually gives versus a true elastic swing.

while elastic case roughly doubles it. But then there's rolling friction converting the ball's initial sliding speed down to 5/7 of its struck velocity, since the sphere is hit through its center without the offset needed for pure rolling. So I need to factor that 5/7 reduction into the final rolling speed estimate.

Checking the upper range, I worry about the ball hitting the back wall too hard at around 1.85-2 m/s, and whether MuJoCo's contact stiffness and thin wall thickness could let the ball tunnel through given its per-step displacement relative to wall thickness.

I should thicken the back and side walls to 0.04 to avoid penetration issues, and aim for a lower bob speed. I'll pick v_bob around 1.4 m/s so the resulting ball speed falls between the inelastic (~1.27) and elastic (~1.8) extremes, since MuJoCo's critical damping behavior sits somewhere in between.

This zero crossing happens at t=2τ, giving v = v0 e^{-2}(1-2) ≈ -0.135v0, so the effective restitution coefficient is about 0.14 — nearly inelastic. The ball then picks up roughly (1+e)v_bob from the heavy-bob limit, reduced further by friction to about 5/7 of that, landing near 0.81v_bob; the tangential contact direction stays simple since the normal is horizontal at impact. With M≫m the pendulum barely slows down, so it continues on essentially unchanged after the collision.

Afterward the faster ball separates from the bob but decelerates under friction from 1.14v_bob down toward rolling speed in roughly 0.04s, while the bob's speed stays close to v_bob as it swings along its arc. Since their average speeds are close, there's a real chance the bob catches up and collides with the ball a second time, adding another push — making the overall dynamics messy but still just incrementally boosting the ball's speed.

To avoid this uncertainty, I'm considering tuning the contact solver parameters (solref/solmix) so the pendulum bob's material properties dominate over the ball's and floor's in any contact mix, effectively making the collision behave more predictably like an elastic bump.

I'm estimating a restitution coefficient around 0.6 from the damping ratio, checking the timeconst against the timestep for stability, then working through what the ball's velocity would be after the bounce — roughly 1.6 times the bob's velocity initially, settling to about 1.14 times once rolling, which stays above the bob's own speed.

I need to sort out sensible masses for the simulation: giving the ball about 0.05 kg and the bob 1 kg, adjusting densities accordingly since the sizes are fixed by radius. But I'm second-guessing whether MuJoCo's soft-contact model actually produces a clean restitution coefficient — the constraint solver releases contact when the reference acceleration would start pulling rather than pushing, and with a small damping ratio the position trajectory decays like a damped oscillation, which makes the exact release timing trickier to pin down than I'd like.

Working through the math, I estimate the effective restitution lands somewhere around 0.14 to 0.8, which translates to a rolling ball speed range of roughly 0.81 to 1.29 times the bob velocity (ignoring secondary impacts that would only add energy). Since I want the ball rolling in the 0.95–1.8 range at the base of the ramp, I try v_b = 1.4 (giving 1.13–1.8, a bit high on top) versus v_b = 1.3 (giving 1.05–1.68, which looks more reasonable with thicker walls as a buffer). I'll go with 1.3 and continue checking what happens after the ball travels 0.74 m.

Thinking through the second collision more carefully: the ball decelerates from 1.14v_b down toward 0.81v_b while the bob swings past bottom and catches back up, pushing the ball again before separation, so the final rolling speed likely settles somewhere around 0.9-1.0 v_b, giving roughly 1.2-1.4 m/s — acceptable. I'll set the pendulum length to 0.5.

Working out the release angle: using v=sqrt(2gL(1-cosθ0)) with v=1.4 gives cosθ0=0.8, so θ0≈36.9°. But since the rod has mass too, I need to account for its contribution to the effective pendulum dynamics using the physical pendulum formula balancing torque and moment of inertia, treating the bob's mass times distance and its inertia term as the dominant contributions.

Confirming the numbers work out to v_bob ≈1.40 at θ0=36.87°, I'll just set this via a keyframe qpos for the hinge rather than simulating a release velocity, so the pendulum "swings down" naturally in the animation. Now I'm positioning the pivot point geometry.

As the bob swings through, the gap closes almost immediately near the bottom, which is negligible for the setup. I'm defining the hinge axis along y so the pendulum swings in the x-z plane, with the rod and bob geoms placed along -z from the pivot, and working out how rotation about y maps the bob's position as it swings from the -x side toward +x.

Starting at qpos ≈0.6435 rad places the bob at roughly x=-0.3555, z=0.13, and gravity will swing it through the bottom toward +x with the right sign convention. I'm also checking whether the pendulum could hit the ball again after the initial strike, but since it oscillates freely afterward and the ball is gone by then, that's not an issue.

The ball should settle at rest around z=0.03 with minor contact jiggle, and since the push is purely along x by symmetry, y stays zero — the cup's 0.11 interior width comfortably fits the 0.06 ball.

Now I'm working out the cup geometry itself: positioning the base, front wall, side walls, and back wall relative to the cup body so the interior forms a roughly square pocket around ±0.055 with wall thickness and heights sized to contain the ball.

Then I'm checking that the ramp's end lines up with the cup's front wall opening in world coordinates, noting a small 3mm step down where the ball would leave the ramp and land inside, and converting the ramp's world-space center into cup-relative coordinates for the final placement.

The low end sits just below the floor, so the ball transitions smoothly from floor to ramp near x≈0.742. The cup and ramp are both static bodies, so overlaps there don't matter. I estimate the pendulum's quarter-period from 37° using the period formula with I and the torque arm, giving roughly 0.2255 times 2π seconds until impact.

Timing-wise, impact lands around 1.4s, with the ball traveling 0.74m at about 1.2 m/s taking roughly 0.62s, so the ball reaches the cup around 1.1s in, leaving about 5s to settle. I'm now thinking through whether the ball rattles inside the cup — after hitting the back wall with restitution ~0.14, its forward spin from rolling would press it back into the wall via floor friction, and I'm working out how wall friction interacts with that spin given the contact point's velocity from the cross product of angular velocity and radius.

Wall friction acting upward opposes the downward-sliding contact point, while floor friction pushes the ball forward against the wall — this creates a complex but net dissipative interaction, so the spin should decay fairly quickly rather than let the ball climb the wall, and it should settle into the cup near x≈1.03.

I'm checking the ball hits the wall while still airborne, falls, and bounces on the base - that seems fine. With rolling friction condim 6 helping it come to rest and speed dropping below 0.05 m/s in the cup, that should be okay. The torsional friction defaults and the μ=1 sliding friction during pendulum impact also look fine. One more thing to verify: after the ball leaves, the pendulum keeps swinging with some amplitude, and I need to make sure the bob doesn't catch up to interfere with the ball once it's settled, since by the time the pendulum swings forward again the ball should already be far away.

Now I'm working out the ball's mass - settling on 0.05 kg given the sphere's volume, giving a reasonable density, and setting the mass ratio relative to the pendulum bob at about 10-20x. I'm structuring the qpos ordering in the keyframe with the pendulum hinge first, then the ball's freejoint values, and setting up the floor plane size and ball/cup starting positions so everything fits within the floor bounds. I still need to add the hinge damping parameters.

I'm double-checking that the pendulum rod's capsule geometry clears the ball at the bottom of its swing without unwanted collisions, verifying the contact geometry math, and confirming the momentum transfer makes sense between the 1 kg bob and 0.05 kg ball. I'm also considering how the ball behaves on the ramp, rolling up and launching off the edge, and thinking through whether its velocity at the ramp top could send it upward into the cup correctly.

With velocity around 1.5 m/s at the ramp top, the ball should land cleanly at the back wall, so penetration depth stays manageable for the physics engine to resolve. I'm settling on a timestep of 0.002 with the default Euler integrator, and now I'm finalizing the XML structure—naming every body, geom, and light, and setting the ramp's rotation using degree-based Euler angles.

I'm verifying the collision filtering: ball uses contype 1/conaffinity 3, pendulum parts use contype 2/conaffinity 2, so the ball collides with the pendulum and floor but the pendulum doesn't collide with the floor or cup, which matches the intended setup. Hinge joint positions stay in radians regardless of the compiler's angle setting, so I need to keep that in mind when specifying joint ranges.

