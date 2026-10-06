The pendulum is released from 0.684 rad (about 39°) and strikes the ball at x = 0 at about 1.5 m/s. The ball rolls along the floor and up a 10° ramp. It drops over the 5 cm rim into a square cup centred at x = 1 m. I haven't run this in MuJoCo; the numbers below come from hand calculations.

- **Strike speed:** the steel bob is about 8× heavier than the ball, so the ball should roll at about 1.3–1.4 m/s whether the impact is mostly inelastic or somewhat bouncy.
- **Ramp window:** the ramp lets the ball land inside the cup if it rolls anywhere from about 0.95 to 1.65 m/s. Slower and it fails to climb the ramp; faster and it overshoots the far wall.
- **Settling:** only the cup's geoms have rolling friction, so the ball rolls freely on the floor. Once inside the cup it should come to rest within a couple of seconds.

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.5 -1 2" dir="0 0.4 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="pendulum" pos="-0.045 0 0.527">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.475" size="0.004" density="2700" rgba="0.5 0.5 0.5 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.025" density="7800" rgba="0.3 0.3 0.35 1"/>
    </body>

    <body name="ball" pos="0 0 0.025">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.025" density="1000" rgba="0.9 0.2 0.2 1"/>
    </body>

    <body name="ramp" pos="0 0 0">
      <geom name="ramp" type="box" pos="0.7601 0 0.01341" euler="0 -10 0" size="0.154 0.1 0.01" rgba="0.6 0.45 0.3 1"/>
    </body>

    <body name="cup" pos="1 0 0">
      <geom name="cup_base" type="box" pos="0 0 0.0025" size="0.09 0.09 0.0025" condim="6" friction="1 0.005 0.003" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_near" type="box" pos="-0.085 0 0.025" size="0.005 0.09 0.025" condim="6" friction="1 0.005 0.003" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_far" type="box" pos="0.085 0 0.025" size="0.005 0.09 0.025" condim="6" friction="1 0.005 0.003" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_left" type="box" pos="0 0.085 0.025" size="0.08 0.005 0.025" condim="6" friction="1 0.005 0.003" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_right" type="box" pos="0 -0.085 0.025" size="0.08 0.005 0.025" condim="6" friction="1 0.005 0.003" rgba="0.2 0.4 0.8 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.684 0 0 0.025 1 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to design a physically plausible scene: a ball on a floor, a cup positioned at some distance, and a pendulum hinged above that swings down to strike the ball, sending it rolling toward the cup. Since I can't run a simulation to verify, I'm reasoning through the physics manually, considering default friction and contact behavior for the sphere on the plane.

The tricky part is actually getting the ball to stop inside the cup since a solid floor can't have a hole in it—the cup needs walls, but then the ball must get over a wall to enter, which risks it bouncing out instead. I'm considering a horseshoe-shaped cup with an opening facing the ball's path, letting it roll in and settle after hitting the back wall, with rolling friction or damping to dissipate energy so it comes to rest rather than bouncing around.

A doorway opening might not read as a true "cup" though. Let me reconsider the ramp approach instead: a rotated box wedge, static in the world so it doesn't collide with the floor, letting the ball roll up smoothly and drop over the rim. I need enough rolling kinetic energy to climb the ramp's height given the 0.7 factor for a rolling sphere versus gravity.

But once the ball lands inside the cup, I worry about it bouncing or rolling back and forth on a flat bottom indefinitely, since there's no rolling friction to damp that motion—contact collisions alone with default solref may not fully settle it within 6 seconds.

I'm working out whether to add rolling friction to the ball through condim 6 with a friction vector, estimating the resulting deceleration from rolling resistance so the ball actually comes to rest in the cup rather than oscillating forever.

I'm weighing whether the ramp risks the ball bouncing out at the rim versus a shallower design. A low lip made from a thin horizontal capsule could let the ball roll over a small bump instead — I'm working out the geometry of a 0.03 radius ball meeting a 0.006 radius lip, checking the contact distance and angle to see if it's a smoother transition than the ramp.

Calculating the impact angle (~42°) and comparing the energy needed to climb the lip against what's lost from the inelastic collision suggests the ball retains roughly two-thirds of its tangential velocity, so I'm checking whether that's enough to clear the bump reliably.

Then I'm reconsidering the overall geometry — maybe a low front lip with a tall back wall, or really a ramp-fed container where the ball launches up an incline into the cup rim. Picking a ball radius of 0.025 gives a mass around 0.065 kg with default density, which seems reasonable for this setup.

I'll build the cup out of simple box walls (square, thin walls, small base plate) rather than a hollow cylinder, then position a ramp leading up to the cup's rim at a 10° incline so the ball rolls up and drops in.

Working out the ramp geometry: it starts around x=0.626 and meets the rim at x≈0.91, with the ball leaving the edge at roughly (0.906, 0.0746) given its radius, angled 10° upward—I need to check whether it clears the near wall's top edge or just continues its arc into the cup before hitting the far wall at x=1.08.

Working through the energy equations, I estimate the drop needed over that horizontal distance requires the top speed to stay around 1.6 m/s or less, then I trace back what entry velocity at the ramp's base would produce that, factoring in the gravitational loss over the 0.05 height gain and accounting for the energy kink where the ball transitions onto the 10° incline with no-slip rolling.

Given rolling friction complicates predictions, I decide to isolate it to the cup geoms only by using condim 6 with rolling friction there while keeping the floor and ramp at condim 3 with plain friction, so contact friction mixing only applies inside the cup and the rest of the path stays simple.

Rolling friction should keep creep under 5 cm/s, and the soft contact settings keep bounces fairly inelastic so the ball won't hop back over the near wall. Landing impact after a ~0.07 m drop is slow enough to be absorbed fine. I'm considering making the far wall taller just to be extra safe against any escape.

Actually, I need to check exactly where the ball leaves the ramp edge—since it's rolling at speed, it won't follow the corner's arc exactly but will launch into flight once centripetal force requirements aren't met, so I should approximate the launch point as being right at the top of the ramp, slightly above it, moving at a shallow upward angle.

Now with r=0.025 and wall height h_w=0.05, I'm setting up the inner cup region spanning x from 0.92 to 1.08, and tracking the ball's parabolic trajectory to see whether it lands inside the cup, hits the far wall's inner face below the rim, or clips the rim corner. I'm testing a trial speed of v=1.2 to compute the horizontal and vertical velocity components and solving for the time it takes to reach the far wall's x-position.

Working through v=1.2, the height at that time comes out around 0.0265, safely below the 0.05 threshold, confirming a clean landing inside. I check v=1.5 next and find it's marginal at z≈0.053 (just above the wall height, risky), while v=1.4 comes in comfortably at 0.0465. Testing v=0.9 shows the ball lands even earlier since it falls below zero height before reaching the wall, so that's also fine — now I'm thinking about what minimum speed is needed to clear the corner without being too slow to risk falling short.

I decide the ball needs enough speed to get over the near wall and drop in, but not so little that it barely crests the top and rolls back down the ramp instead. So I'm targeting v_top around 1.1 m/s with an acceptable range of roughly 0.4 to 1.4, which gives a pretty wide safety margin. Working backward to find the launch speed at the ramp base, I account for energy losses from the ramp's 10-degree incline (roughly a 3% loss from the sine-squared term) plus friction and slip adjustments, landing on an estimate of about 1.4 m/s as a reasonable starting velocity.

Now I'm checking the window more carefully: solving for v0 given the acceptable v_top range gives v0 between about 0.94 and 1.66 m/s, which confirms there's a comfortable margin for error.

Next I'm thinking about the physics of the strike itself: when the ball is hit horizontally at its center with no spin, it starts out sliding before friction converts that into pure rolling, and the final rolling speed ends up at 5/7 of the initial struck speed due to energy loss in that transition. Since I need a rolling speed near 1.3 m/s, that means the initial struck speed needs to be around 1.8 m/s, and now I'm working out the sliding distance needed for that transition assuming a friction coefficient of 1.

Then I turn to modeling the pendulum-ball collision — the pendulum bob of mass M hits the ball at some bottom speed V, and I need to think about how MuJoCo's soft contact model handles the restitution for this collision, since the critically-damped spring-damper contact doesn't behave like a perfectly inelastic or perfectly elastic collision, and I'm reasoning through how much residual bounce that contact model would actually produce.

Working through restitution uncertainty with e ranging 0 to 0.4, I find picking V=1.5 with M much larger than m gives u landing in a reasonable window of 1.42 to 2.0. I'm also considering whether setting high damping on the pendulum contact solref could force near-zero restitution to tighten this range further.

But the physics gets messier than that simple model: friction decelerates the ball significantly during sliding (about 9.8 m/s² if μ≈1), while the pendulum's horizontal tip velocity also drops as it swings upward past contact. So the final ball speed isn't a clean V·M/(M+m) formula -- there's a more complex handoff happening during the contact and subsequent sliding phase that I need to account for.

I also need to worry about geometry: if the pendulum bob strikes the ball above its center, friction torque from the impact could matter, and I should keep the bob's contact point near the ball's center height while making sure the bob itself doesn't clip into the floor at the bottom of its swing -- I'll need a small clearance there.

To get a decent mass ratio, I'll make the pendulum bob a dense steel sphere and the ball a lighter wood sphere, giving roughly an 8:1 mass ratio, then position the bob with a couple millimeters of floor clearance so the strike is effectively at the ball's center. The connecting rod should be a light capsule so it doesn't add significant mass to the swing.

Working out release angle: with the swing arm length and desired impact velocity, I calculate the drop angle using energy conservation (v² = 2gL(1-cosθ)), landing around 40 degrees from vertical, treating the rod's moment of inertia as negligible since its mass (~0.025 kg) is tiny compared to the bob (~0.52 kg).

Now I'm placing the pivot so the bob makes contact with the ball exactly at the bottom of its swing — setting the pivot's x-coordinate so the gap between bob center and ball center equals the sum of their radii (0.05 total) at the lowest point.

I'm also working out the rotation math for the hinge: rotating the bob position about the y-axis by angle θ using the standard rotation formulas, so I can compute the bob's world position at any swing angle for the keyframes.

After the collision, the pendulum continues swinging with reduced velocity, arcing up toward the +x side before returning through the bottom and swinging back out to -x -- but by that point the ball is no longer there to interact with.

I don't think hinge damping is needed since this only matters for the ball settling, not the pendulum. The ball just needs to slide and roll the remaining distance to the ramp with floor friction at μ=1, maintaining constant speed as it rolls without additional rolling resistance.

For the ramp, I'm working out the rotation needed so the box's top surface rises toward +x — rotating about y by -10° (using degree-based euler angles, since MJCF's default angle unit is degrees) gives the correct upward-tilted normal direction.

Now I'm computing the exact geometry: using the slope and target endpoint coordinates, I find the start position and surface length, then offset by the box's half-thickness along the surface normal to get the box's actual center position and extents.

I should instead extend the ramp's half-length to 0.154 and nudge its center down-slope so the surface meets z=0 smoothly, recalculating the top-right end position accordingly, which lands near (0.910, 0.050) — right where the cup wall begins.

Since both the ramp and cup geoms are static, they won't collide with each other even if slightly overlapping, so I don't need to worry about exact penetration there. I'm now deciding whether the ramp should be its own separate static body or a child of the cup body, and confirming the cup's position should be centered 1m from the ball's start — these are just structural modeling choices that shouldn't affect physics as long as both remain static.

I'm checking the ball's trajectory as it rolls up the ramp and clears the inner top corner of the cup wall near (0.92, 0.05) — tracing the ball's center position at that point to confirm it has enough vertical clearance given its radius and the ramp's 10° incline angle, so it doesn't clip the corner before landing inside.

Now I'm laying out the cup's geometry: a base plate within the walls, four wall boxes (near, far, and two sides) positioned to form the cup's rim, making sure the inner width matches the ball's straight-line path in x with negligible y drift so it lands centered inside the cup.

I'm estimating the ball's rolling friction and dynamics: with μr=0.003 and radius 0.025, deceleration comes out to about 0.84 m/s², so from an initial speed near 1.1-1.3 m/s the ball should settle within the cup's width after several wall bounces, well before the 6 s mark. I'm also timing the pendulum swing — roughly 0.355-0.37 s for a quarter period at 40° amplitude — to sync when the ball gets struck and begins its travel toward the cup.

Checking wall heights now: the near wall is only 0.045 above the base, so a 0.025-radius ball can't easily hop over it without significant air time, which seems unlikely here. I'm also confirming that flight trajectories into the far wall hit a normal face rather than skimming the top corner, keeping the collision physics clean.

To add safety margin, I'm considering whether to raise the far wall slightly or just keep all walls uniform and slightly enlarge the cup's inner half-width to around 0.08 — roughly a 16cm cup, which should still look right.

Now I'm recomputing the pendulum bob mass more carefully: a 0.025m radius steel sphere gives about 0.51 kg, and I'm working out the aluminum rod's volume including its capsule end caps to get its mass contribution too.

I'm carrying this through to find the effective moment of inertia about the pivot (combining bob and rod contributions) and the torque term from gravity, then solving for the angular velocity needed so the bob's release angle θ0 produces the target swing speed of 1.5 m/s. Working through the energy equation, I get ω²=9 requires 1-cosθ0≈0.225, giving θ0 around 39 degrees.

Now I'm comparing the effective mass of the pendulum system at the point of contact to the ball's mass (computed from its density), getting roughly an 8:1 ratio. For the collision, I'm checking both inelastic and elastic limits to bracket the post-collision velocity — inelastic gives about 1.33 m/s combined, while elastic gives nearly 2.67 m/s for the ball — and I'm considering how MuJoCo's default contact solver (critically damped, low effective restitution) would land somewhere between these, meaning the actual outcome depends on how the ball separates from the still-moving pendulum after impact.

Since the ball decelerates from sliding friction while the pendulum keeps moving near its post-collision speed, the pendulum effectively continues pushing on the ball until it slows enough — I'm working out that the bob's horizontal velocity only decays slowly as it swings upward, since its angular deceleration is proportional to the sine of a small angle, so initially there's almost no slowdown, meaning the pendulum keeps shoving the ball forward even as friction fights to decelerate it.

Now I'm calculating when sliding stops, which happens once the ball's translational speed matches its spin speed times radius. The friction-driven spin-up rate works out to about 24.5 m/s², giving a spin-up time around 0.053 seconds, during which the pendulum only moves a small distance and its horizontal deceleration is negligible — but I also need to account for the reaction friction force slowing the pendulum itself, which adds a modest deceleration to the combined ball-pendulum system during this spin-up phase.

In the inelastic case, the ball ends up rolling at roughly 1.28 m/s after accounting for the brief slipping loss, while in the elastic case the ball starts faster (around 2.67 m/s) and then transitions through the same sliding-to-rolling process, converging toward the 5/7 rolling fraction.

Working through partial restitution values, I find that for moderate e the ball may decelerate to its rolling speed but then get caught again by the pendulum, which pushes it forward once more — so the final speed ends up bounded between about 1.28 and 1.43 m/s depending on e, rather than following a single clean formula.

Checking top-of-loop speeds for v0=1.3 and v0=1.43, both come out comfortably within the required [0.4,1.4] window, so this range looks safe with margin. I'm also noting the ramp transition at the kink introduces roughly a 3% energy loss, which I've already accounted for, and flagging that I still need to check what happens once the ball rolls onto the cup's base.

Rolling friction should slow the ball before it hits the far wall, and with condim 6 that contact should behave fine. I'm now second-guessing the timestep of 0.002 against the impact speed of the bob hitting the ball at 1.5 m/s — the soft contact timeconst of 0.02 satisfies the minimum requirement, but working through the approximate penetration depth suggests it could be close to a centimeter, which seems like a lot and makes me want to double check whether the contact would behave unrealistically soft during that collision.

Checking the bob's contact geometry against the floor and ball — the bob sits slightly higher than the ball so the contact normal stays roughly horizontal, and the bob's lowest point barely clears the floor so there's no unwanted floor contact there. I'm confirming the pendulum won't accidentally collide with the ramp or cup since they're positioned far apart, and after the strike the pendulum should swing freely back and forth without the ball interfering further, so hinge damping isn't necessary. I'm also checking whether the ball could contact the pendulum rod itself given the rod's end position.

Collisions within a body are excluded anyway, so that's settled. Now I'm setting up the keyframe qpos: ball resting at z=0.025 with its default orientation, pendulum hinge angle first, then the ball's free joint values, with zero velocities. For the pendulum body, I'm placing it at the pivot point with a hinge joint along the y-axis, then defining the rod capsule and bob sphere geoms relative to that origin.

Checking the geometry: at θ=0.684, the bob swings to roughly x=-0.361, z=0.139, which matches where it should meet the ball. I'm now solving for the angle where the bob's surface actually touches the resting ball — working out that the bob center needs to reach about x≈-0.05 relative offset, meaning sinθ≈0.01, giving a very small θ for first contact.

Now I'm sorting out the floor and contact material settings: enlarging the floor plane, setting default friction, and defining the ball as condim 3 with default friction while the cup geoms use condim 6 with friction "1 0.005 0.003" so the cup-ball contact friction takes the max of each component. I'm also adding lighting and checking colors, and considering whether MuJoCo's default pyramidal friction cone might cause a rolling ball on the floor to slow down slightly due to soft contact dynamics.

I conclude that a ball with condim 3 rolls nearly indefinitely, so that's fine. I'm checking for penetration where the ramp emerges from below the floor near x=0.6264, confirming the ball's slight sinking into the floor is negligible, and setting the ramp's half-width to 0.1 in y. I'm also thinking through the ball's trajectory over the ramp's top edge and whether it could climb back out of the cup after landing, before turning to the cup's bottom plate height.

Sizing the cup's bottom plate to span under its walls (half-extent 0.09 over x∈[0.92,1.08]) without causing overlap issues, since it's part of the same body. I estimate the ball will settle near (1.0±0.08, 0, 0.03) inside the cup within about 3 seconds, accounting for deceleration and wall collisions, and I'm satisfied with the torsional friction value. Now I'm starting to write the actual MJCF file, naming the bodies: floor, pendulum, pendulum_rod, pendulum_bob, and the pendulum hinge.

Next I'm defining the ramp geom's pose and rotation, verifying that a -10° rotation about y correctly tilts the ramp's normal toward -x so the surface rises toward +x — this confirms the rotation sign is correct for the intended incline direction.

I check the ramp's top-right and top-left corner positions using the center plus half-length along the slope and half-thickness along the normal, confirming both corners land where expected (top-left dips below the floor as intended). Then I move on to placing the cup body and its base geom relative to it.

The near, far, and side wall geoms get positioned symmetrically around the cup base to form its container shape. For the pendulum, I'm setting the bob density to 7800, the rod to 2700, and leaving the ball at its default density of 1000, then recording the qpos value of 0.684 before noting the hinge has no range restriction.

