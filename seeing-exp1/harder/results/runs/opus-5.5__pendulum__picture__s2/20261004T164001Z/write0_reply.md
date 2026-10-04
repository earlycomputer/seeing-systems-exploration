The pendulum's 1 kg bob starts 0.86 rad up and swings down. It reaches the bottom of its swing exactly where it touches the ball, at the ball's centre height, so it hits the ball straight on.

The ball rolls about 0.6 m to a short ramp. The ramp ends level with the top of the cup's 6 cm wall. The ball rolls over the wall and drops into the cup. The cup's walls are taller than the ball, so it can't climb back out.

I worked out the speed window by hand, not by running it. Expected speed after the strike is about 1.2–1.75 m/s. The ball needs at least about 0.95 m/s to make it up the ramp. At about 1.8 m/s it would hit the far wall too high and could clear it. I made the cup 24 cm across inside so that the faster end of the range still lands inside.

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="0.5 -1 3" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.75 1"/>

    <!-- visual-only support frame for the pendulum -->
    <geom name="frame_post_left" type="cylinder" fromto="-0.056 0.15 0 -0.056 0.15 0.56" size="0.01" contype="0" conaffinity="0" rgba="0.3 0.3 0.35 1"/>
    <geom name="frame_post_right" type="cylinder" fromto="-0.056 -0.15 0 -0.056 -0.15 0.56" size="0.01" contype="0" conaffinity="0" rgba="0.3 0.3 0.35 1"/>
    <geom name="frame_axle" type="cylinder" fromto="-0.056 -0.15 0.53 -0.056 0.15 0.53" size="0.008" contype="0" conaffinity="0" rgba="0.3 0.3 0.35 1"/>

    <!-- pendulum: hinge at 0.53 m, bob centre 0.5 m below hinge (z = 0.03 at bottom, same height as ball centre) -->
    <body name="pendulum" pos="-0.056 0 0.53">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.475" size="0.006" mass="0.05" rgba="0.6 0.6 0.65 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.025" mass="1.0" rgba="0.75 0.2 0.2 1"/>
    </body>

    <!-- ball resting on the floor at x = 0 -->
    <body name="ball" pos="0 0 0.03">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" mass="0.1" rgba="0.95 0.95 0.95 1"/>
    </body>

    <!-- entry ramp: top surface rises from (0.62, 0) to (0.87, 0.06), meeting the cup rim -->
    <geom name="ramp" type="box" pos="0.74733 0 0.02028" euler="0 -13.496 0" size="0.12855 0.05 0.01" rgba="0.55 0.45 0.3 1"/>

    <!-- cup centred 1 m from the ball's start: base disc plus 16 wall slats, inner radius 0.12, height 0.06 -->
    <body name="cup" pos="1 0 0">
      <geom name="cup_base" type="cylinder" pos="0 0 0.002" size="0.13 0.002" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_00" type="box" pos="0.125 0 0.03" euler="0 0 0" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_01" type="box" pos="0.11548 0.04784 0.03" euler="0 0 22.5" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_02" type="box" pos="0.08839 0.08839 0.03" euler="0 0 45" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_03" type="box" pos="0.04784 0.11548 0.03" euler="0 0 67.5" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_04" type="box" pos="0 0.125 0.03" euler="0 0 90" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_05" type="box" pos="-0.04784 0.11548 0.03" euler="0 0 112.5" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_06" type="box" pos="-0.08839 0.08839 0.03" euler="0 0 135" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_07" type="box" pos="-0.11548 0.04784 0.03" euler="0 0 157.5" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_08" type="box" pos="-0.125 0 0.03" euler="0 0 180" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_09" type="box" pos="-0.11548 -0.04784 0.03" euler="0 0 202.5" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_10" type="box" pos="-0.08839 -0.08839 0.03" euler="0 0 225" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_11" type="box" pos="-0.04784 -0.11548 0.03" euler="0 0 247.5" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_12" type="box" pos="0 -0.125 0.03" euler="0 0 270" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_13" type="box" pos="0.04784 -0.11548 0.03" euler="0 0 292.5" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_14" type="box" pos="0.08839 -0.08839 0.03" euler="0 0 315" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_15" type="box" pos="0.11548 -0.04784 0.03" euler="0 0 337.5" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.86  0 0 0.03  1 0 0 0" qvel="0  0 0 0  0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out the physical setup: a ball at the origin resting on the floor, a pendulum hinged above it that swings down to strike the ball forward, and a cup positioned further along the x-axis that the ball needs to roll into — thinking through how the cup's geometry needs to allow the ball to enter despite having walls.

Actually a ramp risks the ball bouncing back out the open front. Maybe simpler to tip the cup on its side so its mouth faces the incoming ball directly, with the back wall stopping it and damped contact preventing bounce-back — that feels more natural than an upright cup with a low lip and ramp.

I calculate the ball needs about 0.75 m/s to clear the 0.04m lip, then it'll fly off the ramp end into the cup and bounce against the far wall (0.08m), rolling back to hit the shorter 0.04m front wall, which should be tall enough relative to the ball's center to contain it. I'm also weighing whether the tilted ramp's base meets the floor smoothly enough physically, and considering simplifying by skipping the ramp entirely for a shallower cup design.

Working through the rolling dynamics: with launch speed around 1.2 m/s, using energy conservation for a rolling sphere (KE = 0.7mv²) up the 0.04m rise, I get v_top ≈ 0.94 m/s directed along the ramp's 11° incline. Then I'm calculating the projectile drop as it leaves the ramp into the cup, accounting for the roughly 0.04m height difference before landing.

I'm also considering the ball's spin as it strikes the back wall at ~0.9 m/s — topspin friction against a vertical wall could push it upward slightly, so I need to check whether this climbing effect matters given the 0.1m wall height, plus the subsequent damped bouncing and rolling friction that eventually brings it to rest.

Since I can't run an actual simulation, I'm reasoning through whether the open-front cup design, tipped forward, might be the more robust choice — the ball only needs enough speed to enter and not bounce back out, and with a critically damped back wall (low restitution) plus rolling friction, it should settle inside rather than escape.

Thinking through the geometry more, a tipped cup with its centre 1m away means the back wall sits around 1+L/2, so with the cup length at 0.12 the ball would settle around x=1.03, which checks out fine either way. I'm weighing whether an upright cup with a ramp reads more convincingly as "landing in a cup" versus the tipped version, though a verifier checking z-height or radial distance from the cup axis should accept both — the tipped cup would need a hollow tube built from slatted boxes plus a bottom disk to close it off.

Since the tube's floor sits above ground level due to wall thickness, the ball would clip the slat edge rather than roll in smoothly, so I'm leaning away from that design and instead considering an upright cup with a ramp as part of its body, even though having a ramp geom belong to the cup object feels a little unconventional.

I could instead treat the ramp as a separate static geom in the worldbody, named simply "ramp," which seems cleaner. Now I need to check the launch speed tolerance — somewhere around 0.85 to 1.4 m/s at the ramp's base — since going too fast, like 1.5 m/s, would send the ball flying too far and risk it smashing into the back wall mid-flight rather than landing cleanly inside.

Too slow, under about 0.75 m/s, and the ball just rolls back down toward the pendulum, so I'm aiming for something like 1.3 m/s as a safe middle ground with margin on both sides. I also want the front wall's lip to be tall enough (around 0.04) relative to the ball's radius (0.03) so a slow-rolling ball physically can't climb back out over the edge — that step height exceeding the radius should make it impossible.

Now I'm thinking through how the ramp meets the cup's rim so the ball transitions smoothly rather than snagging, aligning the ramp's end with the wall's outer face and top height so the ball briefly crosses the thin wall top before dropping into the cup. I'm also reconsidering the cup's shape — whether to build it from a ring of angled box "slats" to approximate a circular cup, and whether the walls should have uniform height (which risks the ball overshooting the back wall) versus the uneven-height approach I was using before.

Working out the friction direction at the wall contact: with forward spin, the contact surface moves downward relative to the ball, so friction pushes the ball upward, letting it climb. Converting spin kinetic energy (0.2mv²) into height gain gives a rough climb estimate of about 0.2v²/g.

Comparing that to the gap between the ball's resting height and the wall top, it's borderline, so I'm reconsidering the geometry -- maybe raising the walls or adjusting the ramp height so the ball doesn't climb out, but I realize that risks the ball colliding with the front wall instead. Looking at the actual landing position, the ball lands close to the back wall at roughly x=1.02 while the wall is at x=1.09, so it's going to strike the back wall almost right after landing.

I try a different approach: tip the cup on its side so its mouth faces the ball directly on the floor, letting the ball roll in rather than fly over a rim. The lowest wall of the tipped cup becomes a thin slat resting on the floor, just a few millimeters thick -- small enough that the ball's radius lets it roll over that tiny step without issue.

Inside, I worry about whether the ball will settle or bounce back out over that same small step, since nothing physically blocks an exit path once it's rolling inside -- I'm counting on topspin and low restitution to keep it in, though default contact properties might still allow it to escape. I also consider adding a small lip at the mouth, though real cups don't have that, or reconsidering an upright cup with a ramp tall enough to require sufficient initial velocity to clear it.

Working through the numbers: I need roughly 1.6 m/s launch velocity, computing the ramp angle, flight trajectory, and fall time to check where the ball lands relative to the cup's inner wall height and diameter, making sure it doesn't strike the back wall mid-flight.

Testing the boundaries: at v0=2.0 the ball clears to 0.12 m at the back wall point, which exceeds the 0.10 wall height and fails, so the viable launch velocity window narrows to roughly 1.25-1.8 m/s.

I'm reconsidering cup geometry — maybe a bigger inner radius of 0.12 gives more tolerance. With a lower wall height of 0.06, I check whether topspin-induced climb is enough to clear it; spin energy at 1 m/s only adds about 0.02 m of rise, which isn't sufficient, but the minimum ramp velocity to clear a 0.06 m wall works out to about 0.92 m/s, so I'm testing a target v0 of 1.3 m/s for this configuration.

I'm now checking the trajectory with v0 at 1.3 and 1.8 m/s, calculating fall time and horizontal travel distance to confirm the ball lands inside the cup (radius 0.1-0.12) and rolls back against the far wall rather than overshooting, since the landing position needs to clear the near wall while still staying within the cup's diameter.

There's a lot of uncertainty in the collision physics—restitution coefficient from MuJoCo contacts, plus the sliding-to-rolling conversion factor of 5/7 for a sphere. Given the window of acceptable ball speeds (0.95 to 1.8), I'm targeting a geometric mean of 1.31, which means assuming a restitution-based factor of 1.5 and solving backward for the required pendulum release velocity, landing around V≈1.22.

Working through the critical-damping case, separation happens once the contact force crosses zero, giving a restitution around e^{-2}≈0.135 — consistent with MuJoCo's default contacts being quite inelastic, since dropped balls barely bounce. So I'll estimate e≈0.1–0.2, which narrows things down nicely; with e near zero, the ball and bob essentially move off together at speed ~MV/(M+m).

Since the pendulum bob decelerates as it rises while the ball keeps moving, they separate shortly after impact, giving ball speed roughly 1.1·MV/(M+m) with e~0.1. Then accounting for the sliding-to-rolling transition (losing 2/7 of speed since the strike is at center height with no initial spin), the rolling speed comes out to about 5/7 of that, roughly 0.786·MV/(M+m) — assuming MuJoCo's default friction (condim 3) applies this factor correctly during the brief sliding phase.

There's also energy loss at the ramp's kink where the ball transitions from flat ground to the 13° slope — the velocity component normal to the ramp direction is lost, giving a factor of roughly cos²θ ≈ 0.946, with the speed scaling by about cosθ ≈ 0.97 plus some additional loss from spin mismatch. Targeting a rolling v0 of about 1.35, and given uncertainty in e (0 to 0.5), I'm working out that setting MV/(M+m) = 1.6 yields a rolling speed ranging from 1.14 (if e=0) up to 1.71.

With e around 0.15, I get roughly 1.31 — comfortably inside the (0.95, 1.8) target range. I'm also considering whether the cup's inner radius of 0.1 gives enough margin, and thinking about whether MuJoCo's condim 3 contact model (no rolling friction) means the ball could roll back and forth inside the cup indefinitely without losing energy, bouncing between walls but staying contained — as long as it can't accumulate enough speed or spin to climb over the 0.03 lip at the front wall after multiple bounces.

I briefly consider adding rolling friction (condim 6) to slow the ball down over the 0.7 m approach, estimating the deceleration would only drop the velocity from 1.3 to about 1.23 m/s — not a big enough effect to bother with, so I'll stick with condim 3 and not add the extra friction model.

Now for the pendulum: I need to check geometry so the bob doesn't intersect the floor. With bob radius 0.04 at bottom height 0.03, the bob's underside would dip to -0.01, clipping through the floor, so I shrink the bob radius to 0.025, which keeps its bottom just above ground at 0.005. I still need to work out the mass density for the bob sphere to get a reasonably heavy pendulum weight.

Mass ratio consideration: with ball mass 0.1 and swing mass M, M/(M+m) comes out to about 0.91 for M=1.0. Rod should be a thin capsule connecting hinge to bob, and I need to place the hinge directly above the ball's resting position so the pendulum swings from the side and clears the ball until the strike point.

Checking exact geometry: with hinge at -0.06 and ball at 0, contact wouldn't happen right at the bottom since the distance exceeds the touching threshold — contact would occur slightly after bottom as the bob rises again, with a tilted normal. I'll settle on placing the hinge at x=-0.056, giving a 1mm gap, and need to make sure the connecting rod clears the ball since the rod sits above the bob near the ball's top height.

Now I'm working out the velocity needed at the bottom of the swing. For a point-mass pendulum, V comes from energy conservation, but I need to account for rod mass affecting the effective mass at contact — aiming for MV/(M+m) = 1.6 m/s, meaning V ≈ 1.76 m/s. With a length of 0.5m, I'm computing the hinge height and checking what V² that requires.

Solving the energy equation gives θ ≈ 46.8°. I'm figuring out how this hinge angle translates into the keyframe qpos — the pendulum swings in the xz plane about the y-axis, so I'm deriving how the bob's local position rotates to find the right sign convention for positive θ.

Setting θ0 = 0.82 rad, I compute the velocity at the bottom of the swing from energy conservation, getting V ≈ 1.77 m/s, then I'm checking how the rod's mass distribution and the bob's own rotational inertia contribute small corrections to the effective mass at the bob.

With restitution e=0.15, I work out the ball's post-collision speed using momentum transfer scaled by rolling factor 5/7, landing around 1.32 m/s, which fits the target range of 1.15-1.7. Now I'm wondering whether the pendulum bob swings back and strikes the ball a second time after the initial collision.

Checking this, the bob decelerates to about 1.6 m/s while the ball moves faster at 1.85 m/s but sliding with friction causing it to decelerate at μg≈9.81 m/s². Tracking both velocities over time, I find the ball slows below the bob's speed around t=0.025s, so I'm computing the gap between them at that moment to see if contact is reestablished.

I'm working through the gap equation more precisely, including the bob's deceleration term, and checking values around t=0.04 to 0.05 seconds — the gap seems to shrink to nearly zero but stays barely positive, so I need to double check whether the bob's horizontal position (using L sinφ) and its slight rise actually bring the contact point to exactly zero or keep it just above.

I'm also considering whether a second, gentler contact between the bob and ball could occur given the vertical shift in the bob's center and the resulting change in horizontal separation needed between centers. If this happens, it would only nudge the ball's speed and potentially impart slight backspin, but these effects seem small enough to stay within the problem's required window, so I don't think I need to change the setup further.

I'm double-checking the ball's initial resting stability and how the keyframe qpos ordering should work -- the pendulum hinge angle comes first, then the ball's free joint position and orientation, with the ball's position overriding the body's default pos. There may be slight penetration settling due to soft contact physics, but that's negligible.

Now I'm working out the cup geometry: a static body with a base disc (cylinder) sitting on the floor, slightly raising the interior landing surface for the ball, which should be fine visually and physically.

For the walls, I'm placing a ring of 12 box slats at radius ~0.105 with thickness 0.01 and height 0.06, spaced every 30 degrees, calculating their tangential width so adjacent slats slightly overlap. The front slat faces the ball's approach direction, so I need the ramp to reach the top of that slat's outer face.

The ball rolls down the ramp and over the tops of the front slat and its two neighbors, all flush at the same height so there's no catching or snagging, then drops into the cup. I'm making sure the ramp's top surface aligns exactly with the wall tops so the transition is smooth.

I'm working out the ramp geometry: tilting a box by angle α so its sloped top runs from the lower starting point up to the wall-top height, computing the slope length, angle, and box dimensions, then positioning the box center by offsetting from the surface midpoint along the surface normal.

Verified the top normal direction matches the rotation convention. I'm also checking that the tilted ramp box doesn't cause collision issues since both it and the floor are static geoms in the world body, so there's no self-contact to worry about—just a 13.5° kink where the ball transitions between surfaces at the base, which should be fine physically.

That confirms static-static pairs are skipped, which doesn't matter for the simulation anyway. I'm now checking the ramp width and top edge transitions against the neighboring slats' rotated boxes at 150° and 210°, comparing their y-extents to the ball's ±0.03 range to rule out collisions.

I work through the geometry: the neighboring slat spans roughly y=0.028 to 0.077, and at y=0.028 the ball's surface height is about 0.079, above the 0.06 wall top, so no contact occurs there. I confirm the ball lands on the base and hits the back wall as expected, and check that the launch off the ramp's top kink at 13.5° clears the 1cm wall edge without issue.

Checking the speed margins: rolling up the ramp needs v>0.917 before kink losses, so about 0.96 required against an expected 1.32, giving good margin. On the upper end, with restitution e=0.5 the computed exit speed of 1.8 still keeps the ball's center below the 0.06 wall height when it reaches the back wall, so that's fine too. I also start considering what happens as the pendulum continues swinging after the strike, coming back down around t≈1.5s.

The ball will be long gone by the time the pendulum swings back — it continues oscillating indefinitely since there's no damping, but that's not a concern. I estimate the pendulum's swing amplitude stays well clear of the ball's path, and the ball reaches the ramp in about 0.5 seconds. I'm also confirming the ball's mass and radius give a sensible automatically-computed inertia, and noting the pendulum rod/bob geometry and body position for the model.

I could add an optional static gantry frame for the pendulum with posts and a crossbar, set to non-colliding since it's purely visual. The hinge uses default friction and damping, and checking the bob-ball contact heights confirms both sit at z=0.03, so they'll meet correctly at rest.

Now I'm working out the cup geometry—base cylinder dimensions, wall positions, and the angular placement of six slats spaced 30° apart around the rim, computing each slat's x,y coordinates from the cosine and sine of its angle.

I check that the gaps between slats at inner versus outer radius are small enough that the 0.03-radius ball can't slip through, so the tangential overlap works out fine. Box-sphere collision for the slat edges should be straightforward, and I'm now considering whether the ball could just rest on top instead of going through.

For the setup, I'm planning the worldbody order with the pendulum body first, then the ball, giving it an initial qpos for the freejoint at roughly height 0.82 with no rotation. I'm leaving contact solver parameters at default and thinking through the collision dynamics — with the bob following closely and pushing repeatedly, the ball should settle to a sliding speed near 1.6 and a rolling speed around 1.2-1.4, which seems reasonable given near-zero restitution.

Testing without follow-up contact gives 1.15 scaling down to about 1.11, still comfortably above the 0.96 threshold, though the margin is a bit tight. I'm considering bumping the initial angle to 0.9 rad to get more energy transfer, but recalculating shows the upper-bound restitution case gets close to the 1.8 limit, so I need to pin down what effective restitution MuJoCo's default sphere-sphere contact actually produces given its solver reference parameters.

Settling on θ0 = 0.86 rad gives a good spread of outcomes across restitution assumptions, from 1.20 at fully inelastic up to about 1.75-1.80 at the high end, which fits the target range well. Now I'm checking the velocity and distance at the top of the ramp to make sure the ball clears the gap to the back wall given its radius.

Checking the ball's trajectory more precisely, I find the center lands right at 0.058 versus a wall top at 0.06 — a borderline case where the contact normal is nearly horizontal and could let the ball roll over rather than bounce back cleanly. This is risky, so I'm considering fixes like raising the wall height to 0.08 while keeping the ramp at 0.06, though that creates an uneven cup; alternatively I could enlarge the inner radius of the cup to 0.12, or redesign the whole cup geometry.

With a 0.12 inner radius, recalculating the center's reach gives about 0.22, which pushes the landing time out to where z drops to roughly 0.030 — meaning the ball lands with good margin well before reaching the rim, so this adjustment looks like the right fix.

Now I'm working out the slat geometry around the basket, settling on 16 slats at 22.5° increments with a mid radius of 0.125, computing the half-width tangentially at the outer radius, and locating the front slat and its neighbors to check where the ball lands relative to their tops.

Then I'm calculating the ramp's endpoints and center position based on the front slat's outer face at x=0.87, deriving the midpoint and offset coordinates for the ramp geometry.

Checking the tilt angle gives about 13.5°, and I verify the ramp's end face sits correctly against the front slat with no gap, and the top surfaces align so the ball falls cleanly into the cup.

Confirming the ball can't roll back out since the inner wall height matches twice the ball radius, and checking rolling speeds at both restitution extremes clear the minimum threshold needed, with distances and masses all checked. Now I'm finalizing the floor dimensions and object masses before writing the scene, including a keyframe for the ball.

Adding gantry post and crossbar visuals, non-colliding, with proper naming, then wrapping up with a brief mention in prose.

