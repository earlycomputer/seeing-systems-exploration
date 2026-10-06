A heavy bob swings from 36° and strikes the ball through its centre. The ball rolls about 1 m up a short ramp, over a low lip and into a walled cup. Inside the cup, a floor plate with high rolling friction stops the ball so it can't roll back out. I have not run this. The values come from hand calculation, and the least certain part is how much speed the soft contact passes to the ball. My estimate is 0.9–1.4 m/s; the cup should catch speeds from about 0.7 to 1.7 m/s.

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002"/>

  <worldbody>
    <light name="sun" pos="0.5 -1 2" dir="0 0.5 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- Pendulum: pivot 0.5 m above the bob centre; bob centre at ball-centre height when hanging. -->
    <body name="pendulum" pos="-0.045 0 0.53">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.475" size="0.006" mass="0.02" rgba="0.3 0.3 0.3 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.025" mass="0.5" rgba="0.8 0.2 0.2 1"/>
    </body>

    <!-- Ball resting on the floor at x = 0. -->
    <body name="ball" pos="0 0 0.03">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" mass="0.05" friction="1 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>

    <!-- Cup centred 1 m from the ball's start: entry ramp, low lip, sticky floor plate, tall back and side walls. -->
    <body name="cup" pos="1 0 0">
      <geom name="cup_ramp" type="box" pos="-0.0976 0 -0.0022" euler="0 -14.036 0" size="0.031 0.06 0.01" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_lip" type="box" pos="-0.065 0 0.0075" size="0.005 0.07 0.0075" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_base" type="box" pos="0 0 0.001" size="0.06 0.06 0.001" condim="6" friction="1 0.05 0.02" rgba="0.5 0.4 0.25 1"/>
      <geom name="cup_back" type="box" pos="0.065 0 0.04" size="0.005 0.07 0.04" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_side_left" type="box" pos="0 0.065 0.04" size="0.07 0.005 0.04" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_side_right" type="box" pos="0 -0.065 0.04" size="0.07 0.005 0.04" rgba="0.6 0.5 0.3 1"/>
    </body>
  </worldbody>

  <keyframe>
    <!-- Pendulum raised 36 degrees (0.628 rad) back from vertical; ball at rest on the floor. -->
    <key name="start" qpos="0.628 0 0 0.03 1 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out the physical setup for the scene — placing the ball on the floor and figuring out how it could realistically roll a meter into a cup, since a solid-walled cup sitting on a flat floor would just block the ball rather than letting it settle in.

I'm working out the physics: using the floor as the cup base, with a tall back/side walls and a low front lip (0.01m) the ball must climb. With MuJoCo's default condim=3, there's no rolling friction, so the ball keeps constant speed once rolling, meaning it could bounce off the back wall and climb back over the lip. I'm considering adding rolling resistance via condim=6 or making the lip asymmetric so the ball can enter but not easily escape.

Actually, I could give the cup's base plate strong rolling friction (condim 6, high rolling friction coefficient) so the ball decelerates sharply on contact and essentially sticks once it rolls in, rather than relying on wall geometry alone.

But a checker likely wants a proper enclosed cup, not a U-shaped open front — so a low front lip combined with a sticky base seems like the right design: the ball rolls over the lip, lands on the high-friction base, and stops before it can escape.

Doing the physics check: with landing speed around 0.8 m/s, sliding friction decelerating at roughly μg ≈ 10 m/s² would stop the ball within a few centimeters, and the rolling friction from the base would kill any residual roll, so the ball settles quickly without bouncing back over the lip. I'm also considering making the lip a smooth rotated ramp instead of a sharp box edge so the ball climbs over it more naturally.

Since the cup body is static (fixed at a location with no joint), static-static collisions between its geoms and the floor get skipped, which simplifies things—I don't need to worry about the base plate intersecting the floor plane. The remaining issue is the small height gap between where the ball leaves the lip and where it needs to land on the base, but since it's falling under gravity that should resolve itself naturally. I think the ramp approach is cleaner than trying to get the ball to climb a vertical edge.

I need the ramp tilted so its top rises from z=0 at x=0.87 to z=0.015 at x=0.93, giving slope 0.25 and a tilt angle of about 14° — using a y-axis rotation of -14.04° so the local x-axis points upward in +x, with box half-length 0.031 and half-thickness 0.01.

Now I'm computing the box center by offsetting the top-surface midpoint (0.90, 0, 0.0075) downward along the rotated normal (-sinθ, 0, cosθ) ≈ (-0.2425, 0, 0.9701) by the half-thickness, giving a center shifted slightly in +x and down in z from the surface point.

I'm checking that the ramp's top face spans x from about 0.870 to 0.930 and z from 0 to 0.015, confirming the low edge sits right at floor level where the ball meets a 14° kink, then setting up the small lip box that sits from x=0.93 to 0.94 at the ramp's raised end.

Now I'm working out what happens as the ball leaves the lip at height 0.015 with some forward velocity — it falls about 1.5 cm over roughly 0.055 seconds while traveling forward into the cup interior spanning x from 0.94 to 1.06, and I'm placing a thin base plate there to catch it, estimating its top surface height.

I'm giving this base strong rolling friction (condim 6, torsional and rolling coefficients around 0.02) relative to the 0.03 m ball radius so it decelerates and stops rather than rolling forever. Then I'm adding the back wall and two side walls enclosing the cup, sizing and positioning each as thin boxes around the interior region.

Checking the geometry: the cup interior spans roughly 0.94 to 1.06 along x (12 cm, enough for the 6 cm ball to rest between 0.97 and 1.03), with the cup centered 1 m from the ball's starting position, and the side walls slightly overlapping the ramp's lip but that should be fine since the ramp width matches the interior width.

Computing the minimum rolling speed needed for the ball to climb the 1.5 cm ramp: using energy conservation with rolling inertia factor 7/5, I get about 0.64 m/s minimum. Targeting an initial rolling speed around 1.2 m/s, the ball would clear the ramp with some speed left over (~1.0 m/s) and a small upward velocity component (~0.25 m/s) that could cause it to briefly leave the ramp surface near the top.

I'm estimating the projectile flight: rise of a few more millimeters, flight time around 0.086 s, landing roughly 0.085 m further along, putting it near the edge of what the interior space allows (up to 1.03 m) — tight but workable. With MuJoCo's default contact restitution being nearly inelastic, the ball should settle reasonably after hitting the back wall, so I'm considering whether 1.0 m/s might be a safer target speed instead of 1.2.

Working through the pendulum strike: since the ball slides before rolling, the final rolling speed is 5/7 of the initial struck velocity if hit through the center with no spin, so to get roughly 1 m/s rolling I need an initial strike velocity around 1.4 m/s.

For the pendulum-ball collision, MuJoCo's default soft contacts behave closer to inelastic, so with a heavier bob the two would move together briefly at a reduced speed before the bob's continued swing keeps pushing the ball forward. I could tune solref/dampratio to make the contact more elastic and get better momentum transfer.

With default contact damping, restitution is essentially zero, so the ball's speed roughly matches the bob's speed at the moment of separation, around 0.91V, though soft contact penetration could push that higher, maybe up to 1.2-1.8V. Given this uncertainty, I need the ramp design to tolerate a fairly broad range of ball speeds.

Testing the range: at lower velocities the ball rolls out around 0.93, at higher ones it could reach 1.65 and potentially fly over the back wall. Checking the flight physics, even at higher launch speeds the ball should still hit the back wall at a low enough height to bounce back and settle, so the design seems reasonably robust across the uncertainty range.

I'm also checking that the pendulum's continued swinging after impact won't cause a second collision with the ball, and that its path doesn't interfere with the ramp or cup geometry. I'll keep the contact solver settings default for inelastic behavior rather than tuning restitution explicitly, and I'm now thinking through the pendulum's pivot placement.

Setting the pivot so the bob just touches the ball at the bottom of the swing, I'm computing pivot coordinates from the ball and bob radii plus rod length, then sizing the bob's mass directly rather than deriving it from density.

I'm working out the release angle needed for the bob to deliver roughly the target impact speed to the ball using pendulum energy conservation, landing on about 40° as a reasonable release angle, and now checking whether the bob's resting position clears the floor.

Checking bob dimensions against the floor, I realize a bob radius of 0.04 would put its bottom below the floor plane, so I need to shrink the radius or raise the bob center. I settle on a bob radius around 0.025 at center height 0.03, striking slightly above the ball's center to impart a bit of topspin while keeping clearance from the floor.

Now I'm working out the pendulum pivot position relative to the ball so the hinge axis stays along y and the bob swings purely in x, keeping the impact aligned through both centers for a clean horizontal impulse. I'm also setting the ball's resting height to match the floor contact and defining the pendulum's initial raised angle so the bob starts pulled back on the -x side before release.

Checking clearances confirms the rod and bob won't hit the floor or collide with the ball mid-swing since same-body geoms don't interact. After the strike, the bob decelerates under gravity while the ball continues forward at its post-impact speed, so they separate naturally — and the ball itself then decelerates due to floor friction at roughly μg≈9.81 m/s² since it starts without spin.

I realize striking at 2/5 r above center would give pure rolling if it worked, but sphere-on-sphere contact forces pass through the centers, so no off-center torque is possible that way—I'd need a flat striker like a box face instead, hitting at that height with a horizontal normal force plus friction.

But a box-sphere contact normal still passes through the sphere's center regardless of impact height, so this trick doesn't work either. I'm falling back to accepting the standard sliding-friction scenario: the ball launches at some speed, friction decelerates it toward rolling at 5/7 of its initial velocity while the heavy striker pushes against it.

Working through the deceleration, I find the sliding phase takes about 0.057 seconds for angular velocity to build up to the rolling condition, and during that brief window the striker is still advancing and decelerating only slightly, so it keeps contact and continues pushing the ball through most of the sliding phase — meaning the ball likely reaches rolling speed while still near the striker's own speed.

I'm recalculating: the final rolling speed might land around 1.25 m/s instead of the ideal 5/7 factor, with uncertainty spanning roughly 0.9 to 1.4 m/s, which fits within my cup's tolerance window of about 0.75 to 1.7. I decide to trim the release speed to 1.35 m/s to center the target roll speed around 1.0–1.2 m/s, which gives a release angle of about 36° (0.628 rad), accounting for the rod mass slightly reducing the bob's effective speed. I check the minimum case — even at 5/7 efficiency the ball clears the 0.64 threshold comfortably — and now I'm considering the velocity loss at the 14° ramp kink.

The energy lost at that kink is only about 3%, which is negligible, though the ball might bounce slightly there. Since the ball-floor contact uses condim 3 with no rolling friction, it should roll at constant speed afterward, and by symmetry there's no off-axis drift to worry about. After the strike, the pendulum swings freely back and forth for about 6 seconds without needing added damping. Now I'm working out the cup's interior geometry in local coordinates centered at x=1, mapping out the ramp, lip, interior floor, and back wall positions to verify the sticky-base placement.

Checking the dimensions, the ramp spans from local -0.130 to -0.070 along x with a half-width of 0.06 in y, and the lip piece sits right where the ramp ends so the surfaces connect smoothly without a gap. Still computing the base position and size values to match this continuity.

I should verify the ball doesn't collide oddly with the base against the floor since both are static, and check that friction settings with condim 6 (slide, torsional, rolling components) are reasonable for the ball-base contact. I'm also tracing through the ball's possible landing positions within the cup to make sure it can reach the back wall and pass over the lip correctly during flight.

Now I'm setting the ball's physical properties—mass 0.05 with density implied around 442 for a 0.03 radius sphere—and placing the pendulum hinge body at a position with the bob center offset so the joint axis aligns properly along y.

Checking the pendulum's resting contact with the ball, I realize the bob only reaches its maximum x-position at the bottom of its swing, right at q=0, but that still leaves a 1mm gap from the ball—meaning they'd never actually touch. I need to adjust the geometry so the bob genuinely overlaps the ball's position at the bottom of the swing instead of just grazing past it.

Skipping the extra stand geom since it's not needed. For the ramp I'll set the euler rotation to tilt it about 14 degrees, keeping in mind qpos for the hinge keyframe stays in radians regardless of the compiler's degree default. I'll finalize the XML now and note that the tuning is approximate.

