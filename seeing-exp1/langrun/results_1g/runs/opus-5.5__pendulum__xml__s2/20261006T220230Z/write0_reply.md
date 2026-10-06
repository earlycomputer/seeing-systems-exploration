The pendulum bob is released from 45° and swings down. It strikes the ball through a slightly bouncy contact pair. The ball then rolls 1 m, hops a low front lip into the cup, stops against the tall back wall and settles there.

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="0.5 -1 2" dir="0 0.5 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- static support for the pendulum (visual only, no collisions) -->
    <body name="support" pos="-0.075 0 0.53">
      <geom name="support_beam" type="box" size="0.02 0.08 0.01" pos="0 0 0.012" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
      <geom name="support_post" type="cylinder" fromto="0 0.08 0.02 0 0.08 -0.53" size="0.01" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
    </body>

    <!-- pendulum: pivot 0.5 m above the bob centre; bob centre at ball-centre height at the bottom of the swing -->
    <body name="pendulum" pos="-0.075 0 0.53">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.46" size="0.008" mass="0.05" contype="0" conaffinity="0" rgba="0.5 0.5 0.6 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.04" mass="0.5" contype="0" conaffinity="0" rgba="0.8 0.2 0.2 1"/>
    </body>

    <!-- ball resting on the floor at the origin -->
    <body name="ball" pos="0 0 0.03">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" mass="0.1" condim="6" friction="1 0.005 0.0002" rgba="0.2 0.4 0.9 1"/>
    </body>

    <!-- cup centred 1 m from the ball start: low front lip, tall back and side walls -->
    <body name="cup" pos="1 0 0">
      <geom name="cup_base" type="box" size="0.1 0.1 0.003" pos="0 0 0.003" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_front" type="box" size="0.005 0.1 0.0075" pos="-0.095 0 0.0075" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_back" type="box" size="0.005 0.1 0.04" pos="0.095 0 0.04" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_left" type="box" size="0.1 0.005 0.04" pos="0 0.095 0.04" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_right" type="box" size="0.1 0.005 0.04" pos="0 -0.095 0.04" rgba="0.9 0.7 0.2 1"/>
    </body>
  </worldbody>

  <contact>
    <!-- the only pendulum contact: a slightly elastic strike with the ball -->
    <pair name="strike" geom1="pendulum_bob" geom2="ball" condim="3" friction="0.2 0.2 0.005 0.0001 0.0001" solref="0.004 0.15"/>
  </contact>

  <keyframe>
    <key name="start" qpos="0.785 0 0 0.03 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
pendulum touches ball
ball touches cup
ball comes to rest in cup
```

---
thinking (summarized):

I'm planning out the physical setup: a pendulum striking a ball that rolls one meter into a cup, with the ball needing to settle inside. I'm thinking through how to construct the cup itself—likely a shallow walled enclosure the ball can roll into and stop within.

Maybe a ramp approach works better: ball rolls up a gentle incline to lip height, flies over the front edge, and lands inside the cup where a taller back wall catches it. Since MuJoCo's default contact model gives the ball no rolling friction, it maintains constant speed once rolling, which actually makes the trajectory more predictable to tune.

Another option is a low 1cm lip so the ball hops over with minor speed loss, then strikes the taller back wall and rebounds slowly back toward the front — if the rebound is weak enough, the small lip itself could trap it. I'm working out the geometry of when a step height blocks a rolling sphere versus letting it climb over.

Energy to climb a 1cm lip requires roughly v > 0.44 m/s, but the edge collision steals velocity via angular momentum conservation — for a solid sphere hitting a step, the post-impact speed scales down by a factor of (1 - 5h/7r), so I need to check whether the ball retains enough speed afterward to actually clear it.

Working through the numbers, v' ends up around 0.76 times v, needing v > ~0.49 m/s to clear the lip, so a ball rolling in near 0.8 m/s should make it over at roughly 0.6 m/s. Then it hits the taller back wall flush on its face since that wall exceeds the ball's radius, and with MuJoCo's default contact solver being fairly inelastic (restitution close to zero), the rebound will be weak.

The forward spin complicates things though — tracing through the rolling kinematics, the contact point on the ball facing the wall is moving downward, so wall friction pushes back upward on the ball, meaning it could actually climb the wall slightly rather than just bounce back.

I'm reconsidering whether the cup needs a front lip at all — a fully open "C"-shaped cup would let the ball settle against the back wall reliably since restitution is near zero, but that's less semantically a cup. A low lip around 0.008 m feels like the right compromise, given the ball's entry speed is only about 1 m/s, so it should settle robustly either way.

I'm now thinking through the cup's construction as walls plus a thin base: using a thin base (around 0.003-0.005 m thick) that itself serves as the front lip, with side and back walls much taller (around 0.08 m) and the front wall shorter (around 0.012-0.015 m), centered at x=1.0 with roughly a 0.16 x 0.16 inner footprint.

I'm figuring the ball ends up resting against the back wall near x=1.05, which keeps it comfortably within the cup, and confirming the cup should just be a static body with no joint needed. For the pendulum, I'm now working out hinge placement so the bob swings down and strikes the ball without overlapping it, suggesting the pivot should be offset in x rather than directly above the ball.

But I'm running into a sizing conflict: if the bob is bigger than the ball, its bottom dips below the floor at the lowest swing point. I'm considering shrinking the bob to match the ball's radius to avoid this floor collision.

Actually, simpler fix: just use contype/conaffinity bitmasks so the pendulum bob never collides with the floor at all, only with the ball.

I keep the bob radius slightly larger so its bottom clears the floor by a small margin, avoiding collision entirely. The rod connecting pivot to bob also gets the same contype so it never interferes with the floor or cup, and since it sweeps away from the ball's path after impact, it shouldn't strike the ball again once the ball has moved off.

With MuJoCo's near-critically-damped contact model, the collision is essentially inelastic, so the bob and ball share a common velocity right after impact proportional to the bob's mass fraction. The bob then decelerates as the pendulum rises while the ball keeps moving, initially sliding before friction brings it to rolling at five-sevenths of that common speed — I'm aiming for a final rolling speed around 1 m/s.

Working through the cup geometry, I'm checking how the ball's speed degrades as it crosses the base lip and front wall steps, using the rolling-friction velocity reduction formula at each step to see if it retains enough speed to clear the front wall height.

I doubt the ball climbs back over the front lip after rebounding, so keeping it at 0.012 seems fine, and sphere-box edge contacts in MuJoCo should give a sensible normal direction toward the sphere center. Now I'm thinking through the pendulum setup: ball mass 0.1, bob mass 0.5, rod mass 0.05, and working out the effective mass at the bob radius using the moment of inertia to approximate post-impact velocity.

Estimating the numbers, I get m_eff around 0.517 and need the bob's pre-impact speed near 2.0 m/s to give the ball a rolling speed of 1.2 after accounting for the rolling-without-slipping factor of 7/5. I'm now reasoning about what happens after a perfectly inelastic collision — whether the bob and ball move together briefly, with the bob coasting near-horizontally at the bottom while friction decelerates the ball until it separates.

Thinking it through, I realize the contact persists during the sliding phase since the bob keeps pushing the ball forward while friction acts on it, making the dynamics messy — the ball spins up, the bob swings through some small angle (roughly 9° over the ~0.05s sliding duration), and the final handoff speed is genuinely ambiguous with a perfectly inelastic model. It seems cleaner to assume some restitution so the ball separates cleanly right after impact rather than staying coupled.

I'm now working out how to set restitution in MuJoCo via solref, using a damped-oscillator formula to relate damping ratio to coefficient of restitution (e.g. ζ=0.2 gives e≈0.53, ζ=0.1 gives e≈0.73), while keeping in mind the timeconst must be at least twice the timestep or it gets clamped. I also need to account for solmix averaging solref parameters between contacting geoms, and worry that giving the ball a bouncy solref would also make it bounce unrealistically off the floor.

My solution is to apply the restitution specifically through an explicit contact pair between the pendulum bob and ball, rather than setting it globally on either geom, so the floor contact stays unaffected while the bob-ball collision gets the desired bounce.

MuJoCo does check for a pair signature match and skips the dynamic collision if an explicit pair already exists, so to be safe I'll set bob and rod's contype/conaffinity to zero and add an explicit pair for bob-ball, ensuring bob only collides via that defined pair. With restitution e around 0.5-0.7, I can work out the post-collision ball velocity from momentum and energy relations, then let it transition to rolling at 5/7 of its slipping speed, and similarly derive the bob's resulting velocity.

The sliding ball decelerates under friction until it reaches rolling speed, giving the bob a slower trailing speed (~0.74u decreasing) while the ball settles around 0.96u — so the ball pulls ahead of the bob over time, which is the behavior I want.

Given uncertainty in the restitution parameter, rolling speed ends up somewhere between 0.86u and 1.06u regardless of exact damping settings. Targeting a rolling speed near 1.2-1.7 m/s to clear the cup lip without overshooting the back wall, I settle on u=1.6 m/s as giving a safe margin on both ends.

Working backward to find the pendulum release angle, I compute the geometry: for a point-mass bob this gives roughly 42 degrees, but accounting for the rod's own mass shifts the energy balance slightly, so I'm working through the compound pendulum equations to get a more accurate initial angle.

Working out the rotation convention: positive θ about the y-axis swings the bob toward -x, so starting at θ=0.785 with axis (0,1,0) and letting it swing to zero moves the bob in the +x direction, matching what I want. So I'll set the pendulum body's pivot position at z=0.53 (accounting for the 0.5 length plus 0.03 bob offset), with the hinge defined at the body origin.

I'm defining the rod as a thin capsule from the pivot down to near the bob, and the bob itself as a small sphere near the rod's end with its own mass. I also need to decide whether to add a static visual support structure with collision disabled, and I'm checking that at the 45° swing extreme the bob clears everything else in the scene with its computed position around x=-0.43, z=0.18, which looks fine. Now I'm working out the qpos ordering in the keyframe, starting with the pendulum hinge followed by the free-floating ball joint.

I'm setting the keyframe so the ball sits essentially on the floor with minimal penetration, confirming the pendulum parts don't need floor collision. I'm thinking through friction behavior: default friction and condim settings mean no rolling resistance, so the ball maintains speed until it strikes the back wall, where the default low-restitution contact should prevent bouncing. But I'm now considering that residual topspin after the wall hit could interact with floor friction and push the ball onward rather than letting it settle quickly.

To make sure the ball actually comes to rest rather than oscillating, I'm considering adding a small rolling friction term to the ball's contact properties—estimating that a coefficient around 0.0005 would produce a gentle deceleration (roughly 0.1 m/s² range) without being too aggressive, settling on a modest value like 0.0002 as a safe, nearly negligible damping addition.

I'm computing the ball's density from its mass and radius to get a physically consistent value, then sketching out the cup geometry—positioning the base box and its walls around a center point with appropriate thicknesses so the ball fits and rests inside without clipping through.

Checking the ball rests properly against the back wall within the cup bounds, with the cup centered a meter from the ball's start. I'm also adding an explicit contact pair for the pendulum bob striking the ball, using low friction values to avoid imparting unwanted spin.

The restitution with solref 0.004 and default solimp works out to roughly 0.62 given the damping ratio. After impact the bob keeps swinging freely (no damping needed since the ball is long gone by the time it would swing back), and the ball itself travels straight after transitioning from sliding to rolling, reaching the cup around 0.7 seconds in.

For the expected events, I'll name them as "pendulum touches ball," "ball touches cup," and "ball comes to rest in cup," keeping body names consistent. I should double check the ball's initial z position isn't penetrating the floor, and set contype/conaffinity groups so the ball, floor, and cup interact (group 1) while the pendulum and support stay non-colliding (group 0). Then I'll add a light and finish the visuals before writing out the file.

