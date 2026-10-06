Ball 1 starts already rolling at 4 m/s and strikes ball 2. Ball 2 then strikes ball 3. Ball 3 climbs a short 15° ramp, goes over the low front wall of a static cup and drops in, where a tall back wall catches it.

I haven't run this. The speeds and the cup's 0.135 m front wall come from rough hand estimates of collision and rolling losses. On those estimates ball 3 clears the wall with margin and ball 2 doesn't reach it.

- **Ball contacts:** they are fairly bouncy (damping ratio 0.02 in `solref`) and nearly frictionless against each other. Each hit should hand most of the momentum forward instead of the balls clumping together.
- **Floor, ramp and cup contacts:** these have `priority="1"`, so their own fully damped contact settings win. Rolling stays clean, and ball 3 should settle in the cup without bouncing out.

```xml
<mujoco model="three_ball_chain_into_cup">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <asset>
    <material name="floor_mat" rgba="0.75 0.78 0.8 1"/>
    <material name="ramp_mat" rgba="0.55 0.4 0.25 1"/>
    <material name="cup_mat" rgba="0.2 0.45 0.8 1"/>
    <material name="ball1_mat" rgba="0.85 0.15 0.15 1"/>
    <material name="ball2_mat" rgba="0.95 0.75 0.1 1"/>
    <material name="ball3_mat" rgba="0.15 0.7 0.25 1"/>
  </asset>

  <worldbody>
    <light name="sun" pos="0.8 -1.0 2.5" dir="-0.2 0.4 -1" diffuse="0.9 0.9 0.9"/>
    <camera name="side" pos="0.9 -1.8 0.6" xyaxes="1 0 0 0 0.3 1"/>

    <geom name="floor" type="plane" size="5 5 0.1" pos="0 0 0" material="floor_mat" friction="1 0.005 0.0001" solref="0.02 1" priority="1"/>

    <!-- 15 degree ramp: top surface meets the floor at x = 1.0 and rises to z = 0.14 at x = 1.5216 -->
    <geom name="ramp" type="box" size="0.27 0.06 0.01" pos="1.2634 0 0.0592" euler="0 -15 0" material="ramp_mat" friction="1 0.005 0.0001" solref="0.02 1" priority="1"/>

    <body name="ball1" pos="0 0 0.02">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.02" density="1000" material="ball1_mat" friction="0.05 0.005 0.0001" solref="0.005 0.02"/>
    </body>

    <body name="ball2" pos="0.3 0 0.02">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.02" density="1000" material="ball2_mat" friction="0.05 0.005 0.0001" solref="0.005 0.02"/>
    </body>

    <body name="ball3" pos="0.6 0 0.02">
      <freejoint name="ball3_free"/>
      <geom name="ball3_geom" type="sphere" size="0.02" density="1000" material="ball3_mat" friction="0.05 0.005 0.0001" solref="0.005 0.02"/>
    </body>

    <!-- static cup sitting on the floor just past the top of the ramp -->
    <body name="cup" pos="0 0 0">
      <geom name="cup_bottom" type="box" size="0.144 0.08 0.005" pos="1.666 0 0.005" material="cup_mat" friction="1 0.005 0.0001" solref="0.02 1" priority="1"/>
      <geom name="cup_front" type="box" size="0.005 0.08 0.0675" pos="1.527 0 0.0675" material="cup_mat" friction="1 0.005 0.0001" solref="0.02 1" priority="1"/>
      <geom name="cup_back" type="box" size="0.005 0.08 0.125" pos="1.805 0 0.125" material="cup_mat" friction="1 0.005 0.0001" solref="0.02 1" priority="1"/>
      <geom name="cup_left" type="box" size="0.144 0.005 0.0675" pos="1.666 0.075 0.0675" material="cup_mat" friction="1 0.005 0.0001" solref="0.02 1" priority="1"/>
      <geom name="cup_right" type="box" size="0.144 0.005 0.0675" pos="1.666 -0.075 0.0675" material="cup_mat" friction="1 0.005 0.0001" solref="0.02 1" priority="1"/>
    </body>
  </worldbody>

  <keyframe>
    <!-- ball1 starts rolling without slip at 4 m/s along +x (spin 200 rad/s about +y) -->
    <key name="start" qpos="0 0 0.02 1 0 0 0  0.3 0 0.02 1 0 0 0  0.6 0 0.02 1 0 0 0" qvel="4 0 0 0 200 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm picturing three balls lined up like a Newton's cradle, with the first ball's momentum passing through to send the third ball toward a cup on the floor. I'm working out how the ball could actually enter the cup given wall height—maybe the cup needs to be recessed into the floor or have a ramp leading in, since a ball rolling flat along the ground can't clear raised walls on its own.

Going with the ramp approach, but I need to check the energy budget — climbing a rim of height h requires enough rolling kinetic energy, so with h=0.05 the ball needs v>0.84 m/s. Then I'm tracing collision dynamics: ball1 hitting ball2 transfers most linear velocity but ball1 retains spin and creeps forward at 2/7 v, while ball2 slides off at 5/7 v before friction reconverts it to rolling; cascading this through ball2 hitting ball3 gives ball3 roughly 0.51 v, with trailing balls possibly also reaching the ramp but more slowly.

Running the numbers with v1=3 m/s, ball3 ends up around 1.4-1.5 m/s while ball2 trails at about 0.6 m/s — enough to climb a small bump but not clear a 0.06 m rim, so it rolls back down while ball3 clears the rim fine. Now I'm worried ball3 might be moving fast enough at the top of the ramp to fly clean over the cup rather than drop in, so the cup needs to be positioned or sized to catch it.

I'm sizing the back wall at 0.15 m tall and the cup's interior length at 0.2 m, with ball radius 0.02 m, and thinking through how the ramp meets the floor — treating it as a tilted box whose lower edge dips slightly below floor level so there's a small kink where the ball transitions, losing the normal velocity component (about 3.4% at 15°, which is negligible). I'm also considering just lowering the cup's front wall instead of dealing with the ramp kink, but decide to stick with the ramp approach and start setting the contact solver parameters.

Default MuJoCo contacts are too inelastic for a proper cradle effect — with critically damped restitution near zero, equal-mass balls would just end up moving at half speed together instead of transferring momentum cleanly, causing the balls to clump messily rather than striking in sequence. So I need to tune the contact solref toward more elastic behavior, maybe using a small damping ratio like "0.005 0.1", to get believable transfer through the chain.

Since mixing solref parameters between the floor's default and bouncier ball settings would make resting contacts undesirably springy, I can use geom priority to decouple them — giving the floor priority so ball-floor contacts use the floor's resting solref, while ball-ball contacts use the balls' bouncier settings independently.

For the cup and ramp, I'll similarly set priority 1 with damping so the ball settles naturally inside the cup rather than bouncing. With damping ratio around 0.05, restitution works out to roughly 0.85, which feels physically reasonable alongside the default solimp values. I'll leave friction and rolling resistance at defaults since condim 3 without rolling resistance is fine — balls rolling indefinitely and interacting with the ramp repeatedly is acceptable for this scene over the 6-second duration.

Now I'm positioning the balls: ball1 at x=0, ball2 at 0.3, ball3 at 0.6, with the ramp starting at 1.0, and ball1 given an initial velocity of 2 m/s. Since only linear velocity is specified, I need to add angular velocity so the ball rolls without slipping — working out that for forward motion the required spin about the y-axis equals v/r.

For MuJoCo's free joint, angular velocity is expressed in the body's local frame, which matches world frame here since orientation is identity, giving ω_y = 2/0.02 = 100 rad/s. I'm then tracking the collision timeline: ball1 reaches ball2 around t≈0.13s, and using the coefficient of restitution to estimate post-collision velocities — ball2 picks up roughly 1.85 m/s before friction brings it toward a rolling speed of about 5/7 of that, while ball1 slows to about 0.15 m/s but retains its spin, eventually settling near 0.68 m/s once rolling resumes.

Continuing this chain, ball2 then hits ball3, transferring momentum so ball3 ends up rolling around 0.87 m/s while ball2 drops to roughly 0.45 m/s. Since ball1 at 0.68 m/s is faster than ball2 at 0.45, it catches up and collides again, bumping ball2 back up to around 0.6 m/s, which I'm now tracing forward to see how it interacts with the ramp.

I need to check the ramp height needed so ball3 climbs into the cup — at 0.87 m/s that only gives about 5.4 cm of climb using the rolling energy formula, so I should try bumping the initial speed up to around 4 m/s, which would push ball3 closer to 1.74 m/s and let it climb about 21.6 cm. But I also need ball2, now around 0.9–1.2 m/s after catching up with ball1, to not also crest the ramp and end up in the cup, since the brief implies only the third ball should land there — so I want to pick a rim height that lets ball3 through but stops ball2 short.

Working out the chain of collisions: ball1 ends around 1.36 m/s and eventually catches ball2 (at 0.9 m/s), transferring momentum so ball2 settles near 1.2 m/s with about a 10 cm climb, while ball3 at 1.74 m/s climbs about 21.6 cm. That suggests setting the rim height around 0.14 m, which with a 15° ramp angle means a ramp length of about 0.54 m, and I'm computing ball3's exit speed off the top of the ramp (~1.03 m/s along the slope) to then check its projectile landing.

Checking the landing: with the ball falling roughly 0.14 m and traveling horizontally at about 1 m/s, it drops into the cup with horizontal travel around 0.17 m, which fits within the cup's 0.25 m interior — margins look reasonable but depend on shaky assumptions about restitution and friction during the collisions, so ball2's climb could fall short of 0.14 m if those estimates are off, though both balls seem to have decent headroom.

Default floor friction should handle sliding between bounces fine. For ball-to-ball restitution, I'm leaning toward near-perfectly elastic contacts since higher restitution helps each hit send the striker onward with spin — keeping that coefficient around 0.02 rather than a softer 0.01 setting. The simulation timestep and contact time constant are set so MuJoCo's clamping works out exactly at the boundary, which should be fine even at higher collision speeds.

Now I'm working out the ramp geometry — ball radius 0.02m giving roughly 0.0335 kg at default density, and figuring out the box dimensions and tilt angle so it rises toward positive x, using a -15° rotation about the y-axis and computing where the top surface actually sits relative to the box center.

I'll keep the ramp as a separate worldbody geom since collisions between static geoms don't matter here, and nudge the lower end slightly below z=0 so there's no visible step at the floor. Setting x0=1.0 puts the ramp's top end at x≈1.5216, z≈0.1398, which I'll use to position the cup's front wall next.

The cup can be a static body welded to the world, so MuJoCo won't generate contacts between it and other static geoms even with slight overlap near the ramp's top edge — that's fine since the goal is just for the ball to roll into it. I'll adjust the front wall's top height to sit just below the ramp's end to keep the geometry clean.

Now working out the cup's dimensions: a thin floor box, front and back walls, and side walls sized to fit the ball (diameter 0.04) comfortably within the interior width of about 0.14, positioned where the ball will land after leaving the ramp.

With damping set high at contact, the ball shouldn't bounce out of the cup, and since everything stays aligned at y=0, collisions remain head-on. I'm considering the trailing balls rolling back and forth on the ramp—they may ping-pong against each other but should stay clear of the cup.

I'll assign geom priority 1 to floor, cup, and ramp surfaces so their contact properties dominate, while ball-ball contacts remain at priority 0 and use their own blended properties.

Checking timing: ball3 slides and reaches the ramp around 0.25s and should settle within about a second, with the sliding-to-rolling transition happening quickly over a short distance—so the overall sequence of events should resolve well within the simulation window.

Rechecking ball2's collision with ball3, it looks like ball2 is still sliding (not yet pure rolling) when it strikes, hitting at a higher speed with only partial spin transferred, which means ball3 ends up gaining a bit more momentum and ball2 retains a smaller leftover spin—but the overall outcome and spacing shouldn't matter much either way, and floor friction settings seem fine as is. Now I'm ready to write the keyframe XML, setting absolute qpos values for the three balls' freejoints.

Writing qvel values...

I'm also thinking through the physics of the ball-ball contact itself: ball1 spins with its top surface moving forward while ball2 isn't spinning, so at the contact point there's a velocity mismatch that creates a downward-directed surface velocity on ball1 relative to ball2, meaning friction at that contact could push ball2 upward slightly, causing a small hop depending on the friction coefficient.

Since the floor-ball friction pair uses the max of the two frictions and floor friction of 1 already dominates, I can safely lower the ball-ball friction coefficient to around 0.05 without affecting floor contacts, which should reduce any unwanted hop. I'll set the ball friction tuple accordingly while keeping cup and ramp friction at 1, then move on to lighting and visuals.

