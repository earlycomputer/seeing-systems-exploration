The pendulum swings down from 75°, hits the ball at the bottom of its arc at about 2.4 m/s, and sends it rolling about 1.5–1.8 m/s along +x. Because the floor is a flat plane, the cup can't be a pit. So the ball rolls up a short 10° ramp, hops over the cup's low front lip (4.5 cm), and is stopped by the tall back and side walls of a cup centred at x = 1.0 m. These speeds are hand estimates and I have not simulated the file, so the speed window (about 1.2–2.3 m/s rolling) is the part to check first.

```xml
<mujoco model="pendulum_ball_cup">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="0.5 -1 2" dir="0 0.4 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" pos="0.5 0 0" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- decorative support frame (non-colliding) -->
    <geom name="frame_post" type="cylinder" fromto="-0.056 0.12 0 -0.056 0.12 0.45" size="0.012" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
    <geom name="frame_axle" type="cylinder" fromto="-0.056 0 0.43 -0.056 0.12 0.43" size="0.006" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>

    <!-- pendulum: hinge 0.4 m above the bob; bob just touches the ball at the bottom of its swing -->
    <body name="pendulum" pos="-0.056 0 0.43">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0" damping="0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.375" size="0.006" mass="0.04" rgba="0.5 0.5 0.6 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.4" size="0.025" mass="0.5" rgba="0.7 0.2 0.2 1"/>
    </body>

    <!-- ball resting on the floor at the origin -->
    <body name="ball" pos="0 0 0.03">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" mass="0.1" rgba="0.2 0.4 0.9 1"/>
    </body>

    <!-- 10 degree ramp leading up to the cup lip: surface from x=0.6165 (z=0) to x=0.9 (z=0.05) -->
    <body name="ramp" pos="0.75402 0 0.01410" euler="0 -10 0">
      <geom name="ramp_slab" type="box" size="0.15 0.1 0.01" rgba="0.6 0.5 0.3 1"/>
    </body>

    <!-- cup centred 1 m from the ball start: inner region x 0.91..1.09, y -0.095..0.095 -->
    <body name="cup" pos="1.0 0 0">
      <geom name="cup_base" type="box" pos="0 0 0.002" size="0.09 0.095 0.002" rgba="0.2 0.6 0.3 1"/>
      <geom name="cup_front" type="box" pos="-0.095 0 0.0225" size="0.005 0.105 0.0225" rgba="0.2 0.6 0.3 1"/>
      <geom name="cup_back" type="box" pos="0.095 0 0.1" size="0.005 0.105 0.1" rgba="0.2 0.6 0.3 0.6"/>
      <geom name="cup_left" type="box" pos="0 0.1 0.1" size="0.09 0.005 0.1" rgba="0.2 0.6 0.3 0.6"/>
      <geom name="cup_right" type="box" pos="0 -0.1 0.1" size="0.09 0.005 0.1" rgba="0.2 0.6 0.3 0.6"/>
    </body>
  </worldbody>

  <keyframe>
    <!-- pendulum raised 75 degrees (1.309 rad) toward -x, released from rest; ball at rest on floor -->
    <key name="start" qpos="1.309  0 0 0.03 1 0 0 0" qvel="0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to design the scene so the ball actually lands in the cup—placing the ball at the origin, the cup at x=1.0, and a pendulum hinge above it that swings in the x-z plane to strike the ball at the bottom of its arc. I'm also thinking through how default MuJoCo friction settings mean the ball will roll indefinitely without rolling resistance, so I'll need to account for that in how far it travels.

Since the floor is a flat plane with no hole, I need an alternative way for the ball to be captured—a true cup pit isn't possible, so I'm considering a low-walled container or a short ramp leading up to the rim, letting the ball roll up and drop into the cup's interior rather than relying on it clearing walls through momentum alone.

Checking the back wall height of 0.15 at the far side — the ball should land, hit it, and settle with low restitution, and even if it rebounds toward the near wall, that wall's 0.04 height is still taller than the ball's center height of 0.03, so it can't climb out. I'm also considering whether the cup needs an explicit thin floor box rather than just relying on the room's z=0 plane.

A ramp-based capture design feels cleaner than a three-walled "goal" shape since it's more cup-like, though I need to be careful about the edge transition where the ramp meets the flat floor — a rotated box's bottom edge has to sit flush with the floor so the sphere rolls smoothly onto the incline without catching on a step.

With a shallow slope angle (around 10°), the velocity loss at that transition should be minor — mostly just the normal component (v sin θ) absorbed, keeping most of the ball's speed intact. I'm now thinking through what happens at the top of the ramp: rather than leaving a gap, I should align the ramp's top edge directly with the near wall of the cup so the ball transitions smoothly into the containment rather than launching off an exposed edge.

I'm working out the landing position by estimating the ball's center height at launch versus impact, and calculating the horizontal distance needed to clear the back wall given the cup's wall thickness and radius.

Checking the trajectory with moderate velocities and a 10° launch angle, I confirm the ball stays well below the back wall's height even at higher speeds, so a bounce off the back wall is unlikely to cause it to fly out—MuJoCo's default restitution should keep it contained.

I'm reconsidering the near wall's height since the ball could land close to its inner edge; bumping it to 0.05m and thinning the base to 0.004m should give enough clearance. For the minimum launch speed, I calculate the ball needs roughly 0.84 m/s just to climb the 0.05m ramp, plus some margin for clearing obstacles.

Since friction converts sliding to rolling (final rolling speed is 5/7 of initial impact speed for a center-struck sphere), I want a rolling speed around 1.5 m/s, meaning the initial strike velocity should be about 2.1 m/s.

Checking energy conservation up the 0.05m ramp height, that corresponds to roughly 1.24 m/s at the top, which easily clears the thin 0.01 wall and lands inside, striking the back wall — this seems robust even with some variance in initial velocity between 1.0 and 2.5 m/s. I should also confirm the tall 0.15 side walls keep the ball from bouncing out sideways, and check the cup's width matches where the ball lands.

Now I'm working out the ramp geometry: for a 10° slope rising to 0.05m at x=0.9, the ramp length comes out to about 0.2836m, spanning from x≈0.616 to 0.9, which I'll represent as a rotated box and need to work out the correct rotation transform about the y-axis so the ramp surface aligns properly.

Computing the slope length: floor intersection sits 0.28794 along the slope from the top point, so I'll set the half-length to 0.15 (total 0.3), letting the lower end dip just slightly past the floor. The top surface midpoint works out to roughly (0.75228, 0.02395), stepping back from the wall contact point along the slope direction.

The bottom corner there overlaps the near wall slightly, but since both are static bodies that's harmless. The key question is whether the ball smoothly transitions from the ramp top edge over the flush wall top at z=0.05, since both surfaces align exactly at that height, letting the ball continue its trajectory with its slight upward velocity rather than snagging on an edge.

As for the ramp's body assignment, I'm deciding to keep it as its own separate body rather than folding it into the cup body, since it isn't really part of the cup and including it would distort the cup's bounding box used for "in the cup" checks. So the cup stays centered at (1.0, 0, 0), and I'm working out the wall placements so the inner cavity spans roughly 0.91 to 1.09 in x.

I'm laying out the cup's local geometry now: the near wall centered at x=-0.095 spanning -0.1 to -0.09 with z from 0 to 0.05, the taller back wall at x=+0.095 going up to z=0.15, side walls at y=±0.1 extending to z=0.075, and a thin base plate at z=0.002. Then I'm thinking through where the ball launches from relative to the ramp edge at x=0.9, considering the centripetal condition for when it leaves the surface.

I'm confirming the ball departs immediately at the edge since the required centripetal acceleration exceeds gravity's component, giving a launch point near (0.895, 0.0795) with horizontal velocity 1.22 and vertical 0.215. I'm checking the trajectory clears the near wall's top corner at (0.91, 0.05) by computing the ball's position and comparing the clearance distance (about 0.0314) against the ball's radius (0.03), confirming it just barely clears.

Now I'm worried this clearance is too tight at lower speeds, so I'm considering lowering the near wall's height to 0.045 instead of matching the ramp's 0.05, which should give more margin since the ball's resting center height is only about 0.034. I'm working through how this height change affects the ramp-to-wall geometry where they meet at x=0.9.

Next I'm solving the projectile motion to find where the ball lands after launching off the ramp, getting roughly t=0.1207s and x=1.042, which is comfortably before the back wall at x=1.09, so the ball should land and roll into the wall rather than overshoot it.

Then I'm turning to the pendulum strike: the bob swings down and hits the ball horizontally at the bottom. With ball mass around 0.113 kg (radius 0.03, density 1000) and uncertain effective restitution from MuJoCo's contact model, I estimate the ball's post-collision velocity depends heavily on the bob's mass ratio and elasticity, so I'm aiming for a design that's robust across a plausible rolling speed range of roughly 1.0 to 3 units rather than depending on a precise value.

Checking the upper end of that range: at 3 m/s rolling speed, the ball launches off the ramp top with enough vertical velocity that it reaches the back wall at a height just below the wall's top edge, so it should bounce back rather than clearing it. Depending on how elastic that bounce is, the ball could rebound toward the near wall at around 1.5 m/s and fall short before reaching it, which seems like the kind of margin I want to confirm holds across the whole speed range.

So I'll aim for a rolling speed around 1.2–2.2 m/s, meaning the pendulum strike needs to deliver roughly 1.7–3.1 m/s to the ball. Since the actual transferred velocity depends heavily on the restitution between pendulum and ball, I should either tune the contact parameters to pin down a specific coefficient of restitution, or redesign the pendulum to push rather than strike the ball so the outcome is less sensitive to that uncertain factor.

With the heavy bob transferring most momentum, ball speed roughly equals bob speed at contact, so I'll pick bob velocity V≈2.2 to land v0 in the 2.2–2.9 range, satisfying both the e≈0 and e≈0.3 cases without needing to nail down exact restitution modeling.

Friction will quickly convert sliding to rolling regardless of μ since the physics default friction handles that fine, and the rolling speed ends up 5/7 of v0 independent of friction coefficient. I should place the bob's contact point level with the ball's center at the bottom of the swing so there's no vertical spin component, and since the bob is much heavier it keeps moving near V after striking, rising away so it won't re-strike the ball.

Actually the bob decelerates slower than the ball since its tangential deceleration is smaller, so it keeps pushing the ball forward, transferring more energy before they separate. This makes the final speed uncertain but still likely landing somewhere between 1.6 and 2.2 while rolling.

A cleaner approach is to strike the ball at the center of percussion (2/5 r above center) so the impulse produces pure rolling without slipping from the start, avoiding friction losses entirely. With that exact strike point, I can treat the effective mass at the contact point and relate the impulse directly to the resulting velocity and angular velocity.

Wait, sphere-on-sphere contact: the normal always passes through the ball's center, so a normal impulse alone can't impart torque to spin the ball—only tangential friction could. That means if I want an off-center horizontal strike at the ball's equator height, I actually need a flat-faced bob like a box, so the contact normal is horizontal and hits at the ball's equator, 0.03 height.

Given that, I'll accept there's an inevitable sliding phase after the strike, since a torque-free impulse means the ball initially slides before friction brings it to rolling. So I'll work with final rolling speed somewhere between 5/7 of the strike velocity (pure impulsive case) and the full velocity V if the bob continues pushing through the contact.

One alternative worth considering: constrain the pendulum's hinge range so it stops abruptly right at the bottom of its swing, which would effectively truncate the push right after impact rather than letting the bob drag along.

I need to figure out the drop height for the pendulum to reach 2.1 m/s, which works out to about 0.225 m for a point mass, though I'll need to adjust for the physical pendulum with a rod. Positioning the hinge and bob is tricky though — if the bob radius is 0.04 m and centered at z=0.03 at the bottom of its swing, the bob would clip through the floor, so I probably need to shrink the bob radius to match the ball's or reposition things to avoid that collision.

I'll shrink the bob radius to 0.025 m with its center at z=0.03, leaving a small 0.005 m clearance above the floor so the swing stays clean and horizontal at impact. The hinge then goes at x = -0.055, z = 0.03 + l, and choosing l = 0.4 puts the hinge at z = 0.43 — I'll still need to think about whether a support post is needed or if the hinge can just attach to the world directly.

I'm placing a static support post at x=-0.055, y=0.1 running from the floor to z=0.43, offset in y so it doesn't interfere with the pendulum's swing plane at y=0. For the pendulum body itself, I'm defining a rod capsule plus a steel bob sphere (density 7800, radius 0.025 giving mass ~0.51 kg) and now working out the rod's mass contribution.

Checking the numbers, the rod comes out to roughly 0.042 kg at density 1000, so the bob dominates with a mass ratio around 4.5 to 1. I'm working through the collision dynamics assuming near-zero restitution — computing the effective mass at the contact point and the resulting common velocity after impact, while reconsidering whether to keep the angular limit at 3° or simplify by letting the bob push through freely.

With a joint limit, the bob would stop and the ball comes away with something like 0.82 to 1.64 times V depending on restitution, which is a factor of two uncertainty. Given MuJoCo's default contact settings tend toward nearly inelastic collisions (dropped balls barely bounce), I'll assume restitution around 0 to 0.2, giving an initial ball speed of roughly 0.82 to 1.0 times V, then transitioning from sliding to rolling via the standard 5/7 factor; without the limit, the bob and ball would move together and floor friction would act on the ball.

Working toward a target rolling speed of about 1.6 suggests V around 2.5, with pushing effects possibly raising this toward 0.8V, so I'm settling on a range of 1.6 to 2.2 for V. If the pendulum has no limit, after releasing the ball it'll keep swinging back and forth forever since there's no damping, but that doesn't matter once the ball has departed the scene.

I'm estimating the friction-driven deceleration during the sliding phase: combining the ball's mass with gravity and friction coefficient gives roughly 1.74 m/s² deceleration from the combined system, while spin-up from friction torque grows angular velocity at about 24.5 m/s² equivalent linear rate. Setting these equal to find when rolling begins gives a sliding duration of about 0.076 seconds, bringing the velocity down slightly from its initial 2.05 value by the time pure rolling starts.

Once rolling begins, friction drops out and the ball coasts at constant speed while the pendulum bob continues decelerating under gravity, eventually causing separation around 1.8 m/s — comparing this to the no-slip limit of 5/7 times the initial velocity (about 1.46 m/s) gives a reasonable range of 1.46–1.86 m/s for the final rolling speed, with various restitution coefficients and initial velocities (like V=2.3 giving a lower bound of 1.35) all producing physically sensible results.

I should also verify the ramp transition at the lower speed limit: losing the normal velocity component at the 10° transition, accounting for the height drop and spin, gives a launch speed around 1.03 m/s, and checking the centripetal condition confirms the ball leaves the edge rather than staying on track. Tracing the subsequent projectile motion to see where it lands relative to the wall corner, the clearance comes out to about 0.036 m against a 0.03 m threshold — close but acceptable.

Landing time comes out to about 0.116 s, putting the ball at x≈1.013, which is inside the boundary and clears the far wall corner properly. I also confirm the ball contacts only the ramp's top face at the floor junction, not the lower edge, since the box's low corner sits just slightly below floor level. Now I'm moving to the pendulum: using energy conservation for the physical pendulum with the bob velocity target of V≈2.4 to find the required release angle.

I compute the moment of inertia combining the bob's solid-sphere inertia, its parallel-axis contribution, and the rod's distributed inertia, totaling roughly 0.0837 kg·m². This gives a kinetic energy at the bottom of about 1.507 J, which I now set equal to the gravitational potential energy drop of the bob-rod system to solve for the release angle.

Total inertia comes to 0.082, giving effective mass 0.5125 at the bob and a velocity ratio of 0.837. Solving for target KE=1.476 against the PE coefficient of 2.036 again gives θ≈74°, so now I need to figure out the starting rotation: placing the pendulum with the bob swung up behind (-x direction), using a rotation about the y-axis that maps the local down-vector according to standard rotation formulas.

Checking the geometry, positive rotation angle φ puts the bob at -x, and swinging to φ=0 moves it in +x, which is what I want. Using 75° (1.309 rad) instead of 74° gives 1−cosθ=0.7412, PE=1.509, ω=6.07, V=2.43 — close enough to the target.

I'm now setting up the keyframe qpos string with the pendulum hinge angle and the free ball joint values, noting the joint ordering requirement (pendulum body before ball body in the XML tree) and the total qpos dimension of 8. I'm also checking whether the swinging bob would pass too close to the ball before reaching the bottom of its arc.

Tracing the bob's position as a function of angle, I confirm contact only happens right at the bottom of the swing where distance between centers equals the sum of radii — so no premature collision, though I might add a 1mm gap at the hinge position just to avoid any initial contact issue. Then I estimate the ball's travel timeline: it starts at rest, rolls up the ramp around 0.616 to the top near 0.9, and falls into the cup within about 0.5 seconds, well within the total 6 second simulation window, settling into the cup by the end.

For the decorative support structure, I'm thinking through how to add a post and axle geometry near the hinge without them physically colliding with the swinging pendulum rod — since an axle capsule near the hinge origin would overlap the rod, I plan to mark these decorative pieces with contype and conaffinity set to zero so they're purely visual and don't interact physically.

The ball and cup interactions should stay contained within the ramp walls, and I'm reasoning through the ball's final resting behavior in the cup: with near-zero restitution it should settle quickly after hitting the back wall, though residual spin from contact friction might cause it to roll back and forth a little before fully coming to rest between the cup walls.

So friction from the wall actually points upward on the ball, meaning it could climb slightly on impact. Checking the numbers: with rolling speed around 1.5-2 m/s, the rotational kinetic energy alone could lift the ball a few centimeters, and combined with translational energy it's plausible the ball rises close to the 0.15 wall height—so the wall should be tall enough to contain it even with this climbing effect.

I'm bumping the back wall height to 0.2 for safety margin, and considering whether side walls need the same treatment or if 0.15 suffices there. Then I'm checking the reverse scenario—after bouncing off the back wall, could the ball's spin carry it back up and over the near wall, which is much shorter at 0.045? Working through the geometry, the ball's center would need to rise above the wall top plus some clearance to roll over it.

I conclude the risk is low given reduced rebound speed, and decide not to raise the near wall further since that could interfere with flight clearance. I'm also sanity-checking other physics details: friction at the bob-ball contact seems fine since there's no vertical relative velocity at the hit point, default solver parameters should be adequate, and the timestep of 0.002 keeps per-step ball movement small enough even at 2.4 m/s. I verify the pendulum bob and rod don't clip into the floor, then move to checking the ramp's rotation angle in its Euler orientation settings.

Working through the ramp geometry, I compute the surface normal and midpoint from the slope angle, then derive the center position by offsetting from the top edge along both the slope direction and the normal, arriving at coordinates around (0.754, 0.014) for the box with size "0.15 0.1 0.01". I confirm the local x-axis orientation after the rotation matches expectations, then shift attention to verifying the ball's mass and radius are consistent with solid-sphere inertia assumptions.

Next I'm figuring out where the ramp meets the floor by solving for where the slope's z-coordinate reaches zero, finding x≈0.6165. I also start laying out the scene's lighting, floor plane dimensions, and the cup walls — positioning the near wall, base, and back wall using half-extents and centers so they nest together properly, with side walls still to be placed.

Writing frame geometry...

