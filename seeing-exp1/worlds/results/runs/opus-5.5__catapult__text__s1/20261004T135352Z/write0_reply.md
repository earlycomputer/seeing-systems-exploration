The arm is a balanced hinge driven by a velocity servo. At t = 0 the keyframe sets its target speed to 10.15 rad/s. The arm swings up from −60° and stops at a joint limit at +45°. At that point the ball leaves the cup at about 5.06 m/s, 38.7° above horizontal. Its predicted path crosses the bucket rim at x ≈ 2.89 m and lands near the bucket centre at x = 3.0 m. The bucket's inner wall spans x = 2.70–3.30 m. I worked these numbers out by hand; I have not run the simulation.

```xml
<mujoco model="catapult_bucket">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="1.5 -2 4" dir="0 0.4 -1" diffuse="0.9 0.9 0.9"/>
    <geom name="floor" type="plane" size="6 3 0.1" pos="1.5 0 0" rgba="0.75 0.8 0.75 1"/>

    <!-- catapult frame (static) -->
    <geom name="catapult_base" type="box" pos="-0.1 0 0.025" size="0.3 0.2 0.025" rgba="0.45 0.3 0.15 1"/>
    <geom name="catapult_post_left" type="box" pos="0 0.13 0.335" size="0.03 0.02 0.285" rgba="0.45 0.3 0.15 1"/>
    <geom name="catapult_post_right" type="box" pos="0 -0.13 0.335" size="0.03 0.02 0.285" rgba="0.45 0.3 0.15 1"/>
    <geom name="catapult_axle" type="cylinder" fromto="0 -0.15 0.6 0 0.15 0.6" size="0.012" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>

    <!-- throwing arm: pivot at z=0.6, arm points along -x in its own frame, cup at radius 0.5 -->
    <body name="catapult_arm" pos="0 0 0.6">
      <joint name="catapult_pivot" type="hinge" axis="0 1 0" limited="true" range="-70 45" solreflimit="0.005 1"/>
      <inertial pos="0 0 0" mass="5" diaginertia="0.5 0.5 0.5"/>
      <geom name="catapult_hub" type="cylinder" fromto="0 -0.06 0 0 0.06 0" size="0.03" rgba="0.35 0.25 0.12 1"/>
      <geom name="catapult_beam" type="box" pos="-0.27 0 0" size="0.29 0.05 0.015" solref="0.005 1" rgba="0.6 0.42 0.2 1"/>
      <geom name="catapult_lip" type="box" pos="-0.55 0 0.0375" size="0.01 0.05 0.0225" priority="1" condim="1" solref="0.005 1" rgba="0.6 0.42 0.2 1"/>
      <geom name="catapult_counterweight" type="box" pos="0.1 0 0" size="0.07 0.05 0.04" rgba="0.3 0.3 0.3 1"/>
    </body>

    <!-- ball resting in the cup (arm at -60 deg) -->
    <body name="ball" pos="-0.297631 0 0.194487">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.04" mass="0.1" solref="0.005 1" rgba="0.85 0.1 0.1 1"/>
    </body>

    <!-- bucket: inner radius 0.30, height 0.30, centred 3 m downrange -->
    <body name="bucket" pos="3 0 0">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 0.01" size="0.30 0.01" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall_00" type="box" pos="0.31 0 0.15" euler="0 0 0" size="0.01 0.064 0.15" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall_01" type="box" pos="0.28640 0.11863 0.15" euler="0 0 22.5" size="0.01 0.064 0.15" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall_02" type="box" pos="0.21920 0.21920 0.15" euler="0 0 45" size="0.01 0.064 0.15" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall_03" type="box" pos="0.11863 0.28640 0.15" euler="0 0 67.5" size="0.01 0.064 0.15" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall_04" type="box" pos="0 0.31 0.15" euler="0 0 90" size="0.01 0.064 0.15" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall_05" type="box" pos="-0.11863 0.28640 0.15" euler="0 0 112.5" size="0.01 0.064 0.15" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall_06" type="box" pos="-0.21920 0.21920 0.15" euler="0 0 135" size="0.01 0.064 0.15" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall_07" type="box" pos="-0.28640 0.11863 0.15" euler="0 0 157.5" size="0.01 0.064 0.15" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall_08" type="box" pos="-0.31 0 0.15" euler="0 0 180" size="0.01 0.064 0.15" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall_09" type="box" pos="-0.28640 -0.11863 0.15" euler="0 0 202.5" size="0.01 0.064 0.15" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall_10" type="box" pos="-0.21920 -0.21920 0.15" euler="0 0 225" size="0.01 0.064 0.15" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall_11" type="box" pos="-0.11863 -0.28640 0.15" euler="0 0 247.5" size="0.01 0.064 0.15" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall_12" type="box" pos="0 -0.31 0.15" euler="0 0 270" size="0.01 0.064 0.15" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall_13" type="box" pos="0.11863 -0.28640 0.15" euler="0 0 292.5" size="0.01 0.064 0.15" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall_14" type="box" pos="0.21920 -0.21920 0.15" euler="0 0 315" size="0.01 0.064 0.15" rgba="0.2 0.35 0.7 1"/>
      <geom name="bucket_wall_15" type="box" pos="0.28640 -0.11863 0.15" euler="0 0 337.5" size="0.01 0.064 0.15" rgba="0.2 0.35 0.7 1"/>
    </body>
  </worldbody>

  <actuator>
    <velocity name="catapult_motor" joint="catapult_pivot" kv="13" ctrlrange="0 20"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="-1.047198 -0.297631 0 0.194487 1 0 0 0" qvel="0 0 0 0 0 0 0" ctrl="10.15"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to design a catapult that reliably launches a ball into a bucket 3 meters away, making sure the physics actually works in simulation. I'm thinking through the mechanism—an arm on a hinge driven by a motor or initial velocity—while keeping in mind the ball must start at rest in the catapult's cradle.

A simpler, more predictable design is to use a joint limit stop: the arm accelerates under a constant torque until it hits a hard stop, and the ball releases from a cup at that point with velocity ω·r perpendicular to the arm. I'm setting up the geometry—hinge axis along y, arm swinging in the xz plane, starting pointing backward—so I can calculate the release angle and speed needed to land the ball in the bucket.

The arm just needs an end lip so the ball stays put until release, since at release the ball moves perpendicular to the arm and clears the lip naturally. I'll let the joint limit with soft solref handle the stop, accepting some arm rebound since the ball's already departed by then.

Now I need to work out the launch geometry: bucket is about 3 m away, roughly 0.3 m tall with 0.2 m radius opening, and the ball is 0.04 m radius, so the trajectory needs to land cleanly inside. Rather than relying on a torque motor where release velocity depends on gravity-coupled dynamics, I'm considering a velocity actuator with high gain so the arm snaps to a target angular velocity predictably.

For stability with a stiff velocity servo I'd want the implicitfast integrator, since it handles velocity actuator derivatives implicitly and avoids instability at small timesteps. I also need to think through the initial impulse — when the arm suddenly accelerates from rest, the ball gets pressed into it and contacts need to absorb that transient cleanly.

Once the arm reaches constant ω, the ball should be stable against it since gravity's tangential component pulls the ball back into the arm's surface, keeping contact without needing extra tangential force.

For the centripetal requirement, the lip at the arm's end provides the necessary inward force. I should also figure out a sensible starting angle, maybe around -15°, so the arm begins angled slightly downward with the ball resting against the end lip from the start, giving a stable initial condition and enough arc length before stopping at 45°.

I also need to be careful about the exact placement of the ball against the lip to avoid initial penetration. I'm weighing options: starting the ball slightly above the arm and letting it settle, or precisely computing its resting position in the arm's frame. Given the arm starts moving immediately, I'll just go with a velocity actuator and implicitfast integration, computing the contact position carefully rather than trying to add artificial delay.

If the ball separates slightly ahead of the arm, gravity would pull it back relative to the arm over that short window, so a constant-torque motor giving smooth acceleration might keep things in better contact than a velocity ramp. I could estimate release speed via energy balance—torque times angle swept minus gravitational potential change—though gravity torque varies with angle so it's approximate, but that's acceptable for a rough estimate.

I'm considering a velocity actuator with gain kv instead, producing an exponential ramp toward target speed with a time constant set by inertia over kv—around 0.03s, meaning by the time the arm reaches release (~0.13s) it's nearly at steady speed. I'm weighing whether to make the arm heavy relative to the ball so the ball's inertia doesn't perturb the dynamics much, and making sure the actuator's force range is generous. The initial acceleration from a step torque is still quite high, so I'm checking whether that's smooth enough or if the ball might skip off the arm at the start.

Working through the angle equation to hit 1.05 rad arc with ω_T=8 and τc=0.02s, I get t≈0.151s, which checks out since the exponential term is negligible by then. I'm also noting that gravity torque on the arm will reduce the steady-state speed somewhat, so I need kv large enough to make this effect small.

I'm estimating kv from inertia: with arm mass giving I~0.1 kg·m², kv=5, gravity torque from arm plus ball comes out to roughly 3 Nm, producing about a 0.6 rad/s error — a 7% deviation, which is too much. The ball's added inertia and centripetal effects complicate things further, so I'm considering either lightening the arm, using a counterweight, or just cranking kv higher with a smaller τc to tighten the response.

Working through the math for a uniform rod of length L and mass M rotating about one end, the gravity error scales like 0.147/L, giving roughly 0.3 rad/s for L=0.5m — still too large. The fix is to make the arm symmetric about the pivot (or add a counterweight) so the arm's own gravity torque cancels out entirely, leaving only the ball's gravity torque to deal with.

That remaining torque comes out to about 0.25 Nm, which with an arm inertia around 0.1 and kv=10 gives only about a 0.3% velocity error — acceptable given the bucket's radius provides some tolerance. I'm also considering just computing release speed directly and compensating for these small errors rather than eliminating them, since a position actuator isn't suitable here and velocity control works fine. With implicitfast integration handling damping implicitly, kv=10 stays stable even checking it explicitly, so this configuration should work.

I'm now thinking about the Euler integrator as a simpler default, since kv·dt/I comes out stable there too. The real concern is what happens when the arm hits its joint limit around 45° at roughly 8 rad/s — the actuator keeps commanding torque against the stop, and I need to work out the steady-state penetration this causes given the default solver stiffness and impedance parameters.

Plugging in numbers, steady-state penetration comes out around 0.015 rad, roughly 1°, which seems acceptable. But the transient overshoot during impact could be larger—maybe 0.1 rad or 6°, since the arm hits the spring-damper at 8 rad/s. The release angle matters for trajectory direction, and the ball separates once the arm starts decelerating while the ball continues on its own path.

I'm now checking whether the arm or lip could re-strike the ball as it decelerates—since the ball travels along a straight tangent line while the lip continues rotating slower along its circular arc, the ball's distance from the pivot actually increases faster than the lip's, meaning the ball moves outward relative to the lip and clears over it. So the lip height needs to be low enough that this outward escape isn't blocked.

Without the lip's constraint force the ball would travel straight, which in polar terms shows up as the radial distance increasing — so the lip pushes against the ball to supply that missing centripetal force. When the arm decelerates suddenly, the ball keeps its angular speed and slides ahead along the lip face, with its radial displacement growing quadratically as s²/(2r) over the slip distance s.

With a lip height of about 4 cm and arm radius 0.5 m, clearing the lip corresponds to roughly a 1.6 mm push inward — small but real. Since the arm itself is still rotating (just slower), there's also a tangential friction component as the ball slides against the lip, which could nudge its velocity slightly. One fix is tilting the lip outward or shortening it so the ball radius sits above the lip height, meaning contact happens near the lip's top edge where the normal direction has both radial and tangential components rather than purely radial — which should still work geometrically, though I'm also considering whether avoiding the lip entirely might be simpler.

I'm estimating the radial interference from the lip separation at roughly 0.6mm, which seems minor enough to ignore given the short deceleration window. Friction at the lip contact might add a slight spin or velocity perturbation, but I'll just make the bucket radius generous (0.25) to absorb this uncertainty rather than modeling it precisely.

I considered alternatives—releasing the ball before full stop, or tilting the arm's cup surface instead of using a lip—but realize a tilted scoop surface is geometrically equivalent to a lip anyway, since the normal force needs an inward component to provide centripetal force. I'll stick with the simple lip design and move on to computing the ball's trajectory, starting with choosing a pivot height.

Now I'm working through the position vectors: defining the pivot height, arm radius, and ball offset, then expressing the ball's center position as the pivot location plus a vector along the arm direction plus an offset along the surface normal. I'm setting up the rotation about the y-axis so the arm sweeps from a back-low position to up, defining the arm tip position as a function of angle θ and differentiating to get velocity direction.

So defining q=0 as arm horizontal pointing along -x, rotating about +y by q matches θ=q exactly. With q0 at -15° and joint limits roughly -0.5 to 0.7854 rad, the actual release point would occur near where the arm starts decelerating under those limits.

MuJoCo's limit constraint kicks in right at q=0.785, so deceleration effectively starts there and the ball releases at 45°. For ball placement, I'm treating the ball as offset from the arm axis by a normal vector n=(sinθ,cosθ), confirming it sits on the leading face of the arm during motion, consistent with being on top at θ=-15°.

Working out the velocity vector at release (θ=45°), I get v = ω·0.7071·(r_b+d, r_b-d), giving a launch angle just under 45° due to the offset term. I'm picking concrete geometry: pivot height 0.4m, arm length r_b=0.5, arm half-thickness 0.015, ball radius 0.04, offset d=0.055, with ball mass set explicitly rather than relying on default density.

Computing the release point numerically gives roughly (-0.31, 0.79) in world coordinates, with launch angle ~38.7° and speed ω·0.503. Now I'm placing the bucket target 3m from the pivot along x, with height 0.3, to set up the projectile landing condition.

Solving for the trajectory, I want the ball center to cross z=0.2 right at the bucket's x position, so I work through the quadratic for time of flight, getting t≈0.814s, which gives vx≈4.072 and corresponding vz, letting me back out the required angular velocity ω.

I'm converting those velocity components into ω=4.072/0.3924≈10.38 rad/s with a resultant speed of 5.22 m/s, then double-checking by computing where the ball actually crosses the rim height (z=0.34) to make sure it clears the rim edge before reaching bucket center—solving another quadratic gives t≈0.784s and x≈2.876, close to where I need it.

Now I'm checking whether the ball actually lands within the bucket's inner radius rather than hitting the wall—comparing the ball's left edge (center at 2.876, radius subtracted) against the inner wall position at x=2.8, since the margin is tight.

I'm tracing where the ball hits the bucket's bottom surface: solving the quadratic for when z≈0.06 gives t≈0.843s, landing x≈3.118, so the right edge (3.158) just clears the far wall at 3.2—tight but workable, though it'll likely bounce before settling. I'm considering nudging the aim point slightly earlier to give more margin on the far side.

Checking the entry/bottom numbers confirms a centered path at midpoint 3.0. With MuJoCo's fairly inelastic default contacts, the ball shouldn't bounce much on impact and should settle in the bucket. I'll build the bucket walls from boxes arranged in a polygon as a static body (no joint needed), keeping it simple.

For the arm, I want to zero out gravity torque by setting the COM at the pivot explicitly via an inertial tag, overriding geom-derived mass properties so the arm itself doesn't sag under gravity -- leaving only the ball's weight to calculate as a lever torque.

With kv=20 for the velocity controller, the resulting time constant and steady-state error look small, around 0.2% at max load, and the damping ratio checks out for stability. But checking the actual numbers, the initial torque spike from a 10 rad/s velocity error is huge — over 800 m/s² tangential acceleration on the ball, about 85g, which translates into an 83 N contact force. That's way too aggressive and I need to reconsider the gains or add torque limiting.

I'm also now working through whether the default soft-contact parameters can handle that kind of load without excessive penetration — estimating the steady-state penetration depth using MuJoCo's contact reference acceleration formula to see if the ball would sink unrealistically far into the arm under this force.

The numbers show gravity-only penetration is negligible (~0.19mm), but a large driving acceleration would cause a 16mm sink and a spring rebound that could launch the ball off unrealistically, so I'm reasoning about reducing the acceleration (via a longer time constant τc) so penetration stays small and the ball follows the contact quasi-statically instead of bouncing.

I'm considering stiffening the contact by adjusting the solref parameter directly on the ball geometry, factoring in MuJoCo's timestep constraint (solref time constant should be at least twice the timestep) and checking that the resulting stiffness keeps penetration around 0.15mm even under a higher acceleration. I'm also noting that when two geoms with different solref values interact, MuJoCo blends them via solmix averaging, so I need to account for how the ball's stiffer solref combines with the arm's.

With a 0.04s time constant, I'm working through the arc dynamics: the angular velocity approaches terminal exponentially, and reaching near-terminal velocity by release requires roughly 5 time constants (0.2s), which traces out about 95° of arc — meaning I need to set the starting angle well before the 45° target, something like -50° to -60°.

But starting at -60° raises a geometric concern: the ball resting on the arm surface at that steep angle would tend to roll toward the outer lip rather than staying put. I need to check whether the lip is tall enough to form a proper pocket — looking at the angle between the sloped arm surface and the lip's inward-facing normal to confirm the ball actually sits cradled in a V-shape rather than sliding off.

Solving a=0.5, b=0.866 confirms both coefficients positive, so it's a stable V-shaped resting configuration. I'm now thinking about the lip's geometry: the contact point sits at height R above the arm surface along the normal direction, so a lip shorter than R would touch the ball at its edge rather than its face. For the ball to escape, it needs to slide along the lip until its center clears the lip's edge.

Rather than chase this geometry further, I think it's cleaner to work out ω at release analytically — since the arm accelerates exponentially under a known torque (with the ball's inertia folded into the total moment of inertia), I can get ω(t) in closed form without needing to track steady-state behavior.

Checking the gravity torque against the arm's inertia, though, shows it's not negligible relative to the velocity constant — with modest arm inertia the error creeps toward 1.5%, but bumping the arm inertia up (heavier, more flywheel-like arm) brings that error down to a more tolerable ~0.4%, which I can likely compensate for anyway.

I'm also working through the initial acceleration transient: with the velocity time constant set, the initial angular acceleration is quite high (~260 rad/s²), translating to ~130 m/s² tangential acceleration at the ball, so I'm relying on stiff contact parameters to keep the ball pinned against the arm during that ramp-up, checking that gravity, centripetal, and tangential forces all resolve sensibly through the contact surface. Now I'm setting up the differential equation for the arm's angular velocity response to solve for the exact release speed accounting for gravity's drag on the acceleration.

I'm computing the gravitational torque on the ball about the pivot by taking the cross product of its position and the weight vector, finding that the torque opposes positive rotation whenever the ball's horizontal position relative to the pivot is negative, with magnitude mg(r_b cosθ − d sinθ), and noting the ball's own rotational inertia is negligible here.

Rather than solving the full ODE, I'm approximating with a quasi-steady model since the contact time is short compared to the arc duration: ω lags the target by τ_g/k_v, and plugging in the numbers at θ=45° gives a torque of about 0.309 Nm, an effective k_v of 13.1, and a resulting deficit Δω of roughly 0.024. I still need to account for the exponential remnant term and solve for the target ω so that the release velocity comes out to 10.38, which means evaluating the decay factor at the release time.

Refining the inertia estimate: the arm contributes 0.5 about the y-axis, and the ball adds about 0.0253 from its offset position (with its own spin inertia negligible), giving a total near 0.5253 and an effective time constant τ of about 0.0404 with k_v around 13. I'm also reconsidering the starting angle q0, testing whether -60° makes more sense for the arc geometry before settling on a value.

Solving for the time to traverse the 1.8326 rad arc with the exponential velocity profile, I get t ≈ 0.2161 s with the velocity correction factor converging after a couple iterations since the exponential term becomes negligible. I note gravity effects will slightly slow things further, and I'm now checking how gravity-induced lag on the ball behaves in quasi-steady state near release, which comes out very small relative to kv.

Looking at the filtered gravity torque, since the filter has a lag of about 0.04s, I need to average τ_g over roughly 0.4 rad of prior angle rather than using the instantaneous value. Computing this weighted average gives a correction of about Δω ≈ 0.03, so the relative angular velocity ends up at roughly 0.99 times ω_T.

Working through this, ω_T comes out to about 10.46. Now I need to check the joint limit overshoot effect on release angle — the ball separates when the arm starts decelerating at 45°, which seems fine. Then I need to work out the ball's initial position in the arm's body frame: with the pivot at origin and the arm extending along -x, I'm placing the beam geometry (top surface at z=0.015, ball center offset by the ball radius to get d=0.055) and computing the ball's x-coordinate accordingly.

I'm figuring out the lip geometry too — its inner face position, center, and height — so the ball sits flush against both the arm surface and the lip. I want to avoid an initial gap or penetration that could mess up the simulation's contact behavior, so I'm considering whether a tiny overlap is safer than a tiny gap given how the contact margin is defined.

Since the ball sits symmetrically at y=0 and the arm only rotates about y, there's no lateral drift to worry about, so side rails aren't necessary and could actually interfere with the ball's release motion.

Now I'm computing the ball's world position at the initial hinge angle by rotating its body-frame coordinates through the pivot transform, using the rotation matrix with q0=-60 degrees to get the x and z components.

Checking the result shows it dips below the floor, so the pivot sits too low for that starting angle. I'm tracing the arm's lip and end corners through the same rotation to find how high the pivot needs to be raised, concluding a pivot height of at least 0.52 is needed and settling on 0.6 as a safer choice, or alternatively adjusting the start angle.

With pivot at 0.6 and starting angle -60°, the arm never dips below the floor as it sweeps up to 45°, so that range looks safe — I could also shorten the arc by reducing the velocity constant instead. Now I'm checking the opposite side of the arm near x=0.15, which rotates downward as the arm goes up, and confirming its lowest point at 45° still clears the floor, though I should check whether this side could intersect the ball's flight path.

Since the ball launches from around (-0.3, 1.0) and travels forward-up through the xz plane while the arm stays at y=0, I'm tracing whether the trajectory passes clear of the pivot hub — it looks like it passes safely above it, so I don't need to worry about the counter-side stub. I'll simplify the arm to run from x=-0.56 to the hub at x=0.03, treating the hub as a cylinder along y, and now I'm recalculating the release point in world coordinates with the pivot height set to 0.6.

Now I'm solving for the launch angle and speed that will land the ball at the target bottom near the window's center, testing z_c=0.2 and working out the time, vx, angular velocity, and vz needed, then checking where the trajectory crosses the entry height to make sure it threads the window properly.

I find entry at x=2.888 and bottom hit at x=3.107, giving a midpoint near 3.0 — good clearance against the bucket's inner radius with margins of about 0.1 on each side. I'm now checking the range sensitivity to small changes in angular velocity to see how tight this margin really is.

Expanding the bucket to inner radius 0.3 and height 0.35 gives wider margins of 0.15 on each side, tolerating roughly ±2.2% variation in ω, which feels like a safer design choice. Settling on inner radius 0.28, height 0.3 as a workable compromise, I'm checking the ball's position relative to the bucket rim as it enters near x=2.7.

Now I'm refining the target angular velocity, iterating between the exponential remnant and arc time to converge on ω_T≈10.14, while noting the gravity deficit also lengthens travel time slightly, shrinking the remnant further. I'm also confirming the joint limit behavior in MuJoCo is only active when actually violated, and double-checking the gravity-induced Δω estimate more carefully.

Looking at the torque contribution during the last 0.04s window, I'm computing τ_g at angles near release (45° and 22°), weighting them to get an effective average torque near 0.39, giving Δω ≈ 0.030. I want to double check the total moment of inertia value next.

Confirming τ = I_tot/kv = 0.5253/13 = 0.0404, which checks out; the ball's own rotational inertia is negligible, there's no joint damping or friction to account for, and the hinge limits comfortably contain the starting angle. I'm also verifying the ball won't clip the frame, posts, or hub during its swing.

Checking the geometry, posts at y=±0.12 with width 0.04 leave inner faces at ±0.10, giving the 0.05-half-width arm plenty of clearance from the ball at y=0. I need to figure out whether arm-frame collisions matter at all — if the arm body is a child of the static world body holding the frame geoms, MuJoCo's default parent-child collision filtering would exclude those contacts anyway.

Actually, that parent-child exclusion doesn't apply when the parent is the world body, so collisions between the arm and the frame are included by default; luckily geometric clearance in y already keeps them from touching. I also want to double check the arm doesn't clip the base box at its lowest swing angle — at -60° the arm end sits around z≈0.11, so as long as the base box stays shorter than that it should clear fine.

Rather than worry about geometric stops, I could just rely on the joint limit constraint and skip adding a physical stop bar. If I want a visual touch, I could add a non-colliding crossbar (contype=0, conaffinity=0) positioned near the 45° stop to suggest where the arm halts, placed along the arm's direction at that angle.

I'm checking the ball's trajectory against that crossbar position to confirm it passes well clear — the ball's height at the bar's x-location comes out much higher than the bar itself, so no interference even though the bar sits right where the arm would hit.

Now I'm computing the ball's exact starting position by rotating its local offset through the pivot angle of -60°, working out the cosine and sine terms to get precise x and z coordinates for placement.

With that settled, I'm figuring out the keyframe qpos ordering based on body tree hierarchy—arm joint, then ball position and quaternion, plus matching qvel and ctrl arrays. I'm also laying out the arm's geometry (beam and lip boxes) with their positions and sizes to make sure the catapult surface aligns correctly with the ball's resting point.

I'm placing the hub as a cylinder spanning along y between the posts, keeping it clear of the posts' positions, and checking that the ball sits exactly against the lip face with matching radius and that the beam's top surface properly supports the ball's resting height.

I'm now working through the edge-release case: whether the ball stays balanced against the lip as the arm decelerates, and what happens geometrically as the ball crosses the lip's edge—especially the worst case where the arm stops abruptly and the ball's straight-line path in world space diverges from the arm's rotating body frame.

I'm working out that with the arm rotating at full speed the ball would need centripetal force to stay at the lip, so a decelerating arm creates a transient where the ball pushes into the lip — tracking the ball's radial distance from the pivot and its angular position relative to the arm to pin down when that contact happens.

Looking closer, over the first few milliseconds the arm keeps up with the ball so there's no body-frame separation, meaning the ball only departs from the lip once the arm actually starts decelerating; I'm trying to express the relative tangential displacement as an integral of that deceleration to pin down the radial interference.

Actually friction may matter more: the centripetal normal force at the lip is around 5 N, and if that persists with friction coefficient μ over a 10 ms contact window, the impulse could shift the ball's velocity by roughly 0.5μ m/s — with μ near 1 that's a 10% error, which is too large. I need a low-friction lip surface or a shorter lip so separation happens before friction accumulates significant impulse.

MuJoCo combines friction and condim as the maximum between the two contacting geoms, so I can't just lower the lip's friction if the ball geom itself has higher friction — I may need to set priority on the lip geom to force its (lower) friction value to dominate.

Checking the frictionless lip holds the ball stable at the -60° rest position, confirming the contact normals span correctly. At release, the beam contact force is small (just gravity component) so there's no spring-back, and the lip's compression under centripetal force is negligible (~0.06mm with the chosen solref). I'm also considering what happens if the arm hits its joint limit while the actuator is still applying torque at that moment.

Thinking through the arm's limit stop: the actuator torque grows toward 130 Nm as the arm decelerates to a stop, and with 0.5 inertia hitting the soft limit at 10 rad/s, the system should be critically damped without bouncing. I'm checking whether the arm could overshoot and catch up to the ball afterward, but since the ball moves away at 5 m/s while the arm's surface decelerates, the arm stays behind the ball — so no secondary collision. I'm also working out the kinetic energy at the limit (~26 J) to verify the soft constraint can absorb the impact without excessive overshoot.

I'm tuning the joint's limit stiffness parameter, aiming for something like 0.005/1 to give a crisper stop, and deciding the actuator should be a velocity actuator on the pivot joint with gain 13 and control range 0 to 20, letting it push with up to 130 Nm continuously once past the limit.

Now I'm checking the time constant from the damping gain relative to the system inertia (comes out around 0.05, which seems fine), then recomputing the total rotational inertia about the pivot including the ball's offset contribution, giving roughly 0.525, and from that estimating the torque-to-angular-acceleration ratio near 0.04 before moving on to factor in gravity's effect on angular velocity.

I'm setting up the governing equation combining the velocity-actuator damping term with a gravity torque that depends on angle, then trying to solve for the deviation from the target velocity by integrating the gravity torque weighted by an exponential decay factor over the approach trajectory up to the release time around t=0.221, approximating the angle's path during that integral.

I'm expanding G(θ) in a Taylor series near θ=0.785, getting a quadratic approximation in s, then integrating against the exponential weighting e^{-s/τ} term by term to get the delay-averaged correction.

This gives Δ ≈ 0.032, and checking the effect of this lag on θ progress over the whole trajectory, I estimate the integrated correction is small — on the order of 0.008 rad, contributing negligibly (~0.0008 s) to the overall timing.

Computing the remnant term more carefully: with t≈0.2211 and the exponential decay giving e^{-5.472}≈0.0042, the remnant contributes about 0.0426 to ω_r. Combining everything, ω_r ≈ 10.075 against a target of 10.072, which checks out well if I nudge ω_T up to 10.15. I should also double check whether the ball's velocity is exactly ω times the position vector to the ball — assuming negligible penetration and that the ball spins rigidly with the arm.

The ball's spin carries over into flight with no aerodynamic drag in MuJoCo, so that's not a concern until it lands in the bucket. No air resistance to worry about either.

Now checking whether the ball stays pressed against the arm surface before the 45° release point — the normal force depends on the tangential acceleration plus the gravity component along the normal direction, and since angular acceleration stays non-negative and cosθ remains positive through this range, the normal force stays positive, meaning the ball doesn't lift off early.

At the lip, I'm checking the radial force balance: the centripetal requirement versus the gravity component along the radial direction. At the 45° release angle, the centripetal term (ω²r ≈ 50) clearly dominates the gravity term (g sin45 ≈ 6.9), so the lip force stays positive there — but I need to check the behavior near the start of the motion where ω is near zero.

Now I'm working out the bucket geometry: center at (3.0, 0), bottom cylinder of radius 0.32 and height 0.02, so I'm placing it at z=0.01 with size "0.32 0.01", making the inner bottom surface at z=0.02 — reconciling that with my earlier bottom-hit calculation at z=0.06.

For the walls, I'm arranging 16 boxes around a radius near 0.31 with inner face at 0.30, giving them thickness 0.02 and spanning z from 0 to 0.3 (center 0.15, half-height 0.15), with the bottom disk sitting at radius 0.30 inside the walls. I'm computing the tangential half-width of each wall segment using the chord length formula for 16 sides at radius 0.31.

Computing wall positions...

Finishing the position list, I check clearance between the ball's trajectory and the inner walls — the near wall gap looks like roughly 0.19 units, which seems safely wide enough to avoid unwanted collisions.

Now I'm verifying the catapult frame geometry, checking the base box position and computing the arm's lowest point at -60° rotation to make sure it doesn't clip into the base or ground.

Checking lip corner clearance and post positions relative to the base and arm—everything clears with adequate margin, so I'm moving on to placing the axle cylinder.

For the stop bar, I realize making it a disconnected floating visual element between the posts looks off, almost like a catapult. I'm weighing whether to skip it entirely or add connecting struts from the post tops instead, and I'll go with skipping it for simplicity.

Checking the physics layout, the ball's flight path clears the posts since it travels along y=0 and the posts sit at y ±0.13, and the ball doesn't contact the hub. The bucket and floor are both static so they won't generate collisions with each other, and the arm doesn't touch the floor either. Clearances between the arm and the static posts/base look fine.

For material properties, I'm checking that the ball's solref, the lip's solref, and the beam's solref are all set to similarly small values so the averaged contact softness stays consistent across the ball-bucket, ball-lip, and ball-beam interactions.

Verifying the solref timestep ratio (0.005 vs 0.002) gives a factor of 2.5, which is acceptable since it needs to exceed 2. I'm also double-checking the hinge joint definition — the range is in degrees due to the compiler's angle setting, but keyframe qpos values are always in radians, so I need to keep that distinction correct when setting the arm's rotation limits and initial pose.

Adding the arm's inertial properties, the ball's velocity actuator, and the starting keyframe with a specific qpos, qvel, and ctrl setup — I'm also double-checking whether the ball's initial quaternion orientation should remain at identity.

I need to make sure the ball body's position in the worldbody matches the arm placement so there's no mismatch with default qpos0 loading. Checking the geometry, the ball center sits right at zero distance from both the beam top and the lip face, so I'm uncertain whether MuJoCo's collision margin will register contact at exactly zero — though gravity should pull the ball into clear contact within the very first simulation step anyway.

Looking at the dynamics more closely: the actuator torque accelerates the arm fast enough that the beam moves a fraction of a millimeter into the ball during the first timestep, so the contact solver catches it with only slight lag. Timing-wise, the ball should land in the bucket around 1.1 seconds into the simulation, leaving plenty of settling time within the 6-second window, and the bucket's contact solref should damp out most of the bounce when the ball hits bottom.

I'm now checking whether the ball could bounce out when it hits the far bucket wall — given the low restitution and the wall height relative to the ball's position, it should stay inside. I'm also double-checking the release velocity computation, recomputing the ball's offset position relative to the arm axis to make sure the trigonometry for the launch vector is correct.

Rechecking the release numbers more carefully: with ω=10.075, I compute velocity components (3.9538, 3.1702) and trace the trajectory forward in time to confirm the landing position near x=3.0 matches the target z-height of about 0.2027, which checks out against the earlier calculation.

The arm hitting the hinge limit may overshoot slightly past 45°, but that's acceptable since it's just a physical stop rather than something requiring precise tuning. I'll skip adding a visual stop bump and keep things simple with basic lighting, material colors via rgba values, and no textures.

Writing MuJoCo XML...

I'm considering adding a small non-colliding counterweight box for visual balance, checking its position at different arm angles (45° and -60°) to make sure it stays plausible relative to the pivot and posts without interfering with the ball's flight path.

Corner z works out to about 0.45 in world coordinates, still clear. That checks out fine, so I'm ready to write up the answer with a brief explanation.

