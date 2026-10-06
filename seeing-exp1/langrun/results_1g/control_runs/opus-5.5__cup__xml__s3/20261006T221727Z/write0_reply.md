The ball starts at rest near the top of a 15° ramp. Gravity rolls it down about 7.5 cm of height to roughly 1 m/s. The ramp's lower edge sits just above the rim of an octagonal cup, so the ball rolls off, drops in and lands on the cup floor. Its forward speed takes it into the tall far wall, where it should stop. Rolling friction on the ball should then absorb whatever motion is left. I worked out the geometry and speeds by hand and have not run the scene, so the bounce and the final resting speed are unchecked.

```xml
<mujoco model="ball_ramp_cup">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <asset>
    <material name="floor_mat" rgba="0.8 0.8 0.8 1"/>
    <material name="ramp_mat" rgba="0.6 0.45 0.3 1"/>
    <material name="cup_mat" rgba="0.2 0.5 0.8 1"/>
    <material name="ball_mat" rgba="0.9 0.2 0.2 1"/>
  </asset>

  <worldbody>
    <light name="sun" pos="0.3 -0.5 1.5" dir="0 0.3 -1" directional="true"/>
    <camera name="side" pos="0.35 -1.0 0.35" xyaxes="1 0 0 0 0.3 1"/>

    <geom name="floor" type="plane" size="2 2 0.1" material="floor_mat"/>

    <!-- Ramp: 15 deg incline, top surface from (0.081, 0.198) down to (0.39, 0.115) -->
    <geom name="ramp_board" type="box" size="0.16 0.05 0.01" pos="0.2329 0 0.1467" euler="0 15 0" material="ramp_mat"/>
    <geom name="ramp_support_high" type="box" size="0.01 0.04 0.088" pos="0.12 0 0.088" material="ramp_mat"/>
    <geom name="ramp_support_low" type="box" size="0.01 0.04 0.06" pos="0.33 0 0.06" material="ramp_mat"/>

    <!-- Cup: octagonal walls, inner apothem 0.11 m, rim at z = 0.11 -->
    <body name="cup" pos="0.5 0 0">
      <geom name="cup_bottom" type="cylinder" size="0.13 0.005" pos="0 0 0.005" material="cup_mat"/>
      <geom name="cup_wall_0" type="box" size="0.01 0.054 0.055" pos="0.12 0 0.055" euler="0 0 0" material="cup_mat"/>
      <geom name="cup_wall_45" type="box" size="0.01 0.054 0.055" pos="0.0849 0.0849 0.055" euler="0 0 45" material="cup_mat"/>
      <geom name="cup_wall_90" type="box" size="0.01 0.054 0.055" pos="0 0.12 0.055" euler="0 0 90" material="cup_mat"/>
      <geom name="cup_wall_135" type="box" size="0.01 0.054 0.055" pos="-0.0849 0.0849 0.055" euler="0 0 135" material="cup_mat"/>
      <geom name="cup_wall_180" type="box" size="0.01 0.054 0.055" pos="-0.12 0 0.055" euler="0 0 180" material="cup_mat"/>
      <geom name="cup_wall_225" type="box" size="0.01 0.054 0.055" pos="-0.0849 -0.0849 0.055" euler="0 0 225" material="cup_mat"/>
      <geom name="cup_wall_270" type="box" size="0.01 0.054 0.055" pos="0 -0.12 0.055" euler="0 0 270" material="cup_mat"/>
      <geom name="cup_wall_315" type="box" size="0.01 0.054 0.055" pos="0.0849 -0.0849 0.055" euler="0 0 315" material="cup_mat"/>
    </body>

    <!-- Ball: radius 3 cm, starts resting on the upper end of the ramp -->
    <body name="ball" pos="0.118 0 0.22">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" mass="0.1" condim="6" friction="0.8 0.005 0.001" material="ball_mat"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.118 0 0.22 1 0 0 0" qvel="0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm planning the physical setup: a tilted ramp box with a ball of radius 0.03 m rolling down from a height of about 0.2 m, giving a landing speed around 1.67 m/s, then designing a cup at the base sized to catch and stop the ball by 6 seconds.

I'm thinking through energy dissipation so the ball actually settles instead of bouncing or rolling forever—using fairly inelastic contact solref plus rolling friction parameters (condim=6 with a small rolling friction coefficient) so the ball loses energy against the cup walls and bottom until it comes to rest.

For geometry, I'm working out a ramp around 0.6m long at a 20° angle, with the ball starting at rest at the top and rolling down into a cup placed right past the ramp's end, built from a cylindrical base plus wall segments.

I'm calculating the ball's exit velocity from the ramp (~1.68 m/s, split into horizontal and vertical components) and checking the fall trajectory into the cup, making sure the far wall is tall enough to catch it before it clears the rim.

Since static geometries don't collide with each other, I realize the ramp can physically overlap the cup's near wall without issue — so I could extend the ramp further into the cup interior to shorten the drop and reduce the risk of the ball overshooting into the far wall.

I should lower the drop height instead—using a 10° ramp of length 0.5m gives a drop of just 0.087m, yielding v≈1.1 m/s, which feels more reasonable. Wall impacts should also help: the ball hits with forward spin, bounces into backspin-sliding, and sliding friction against the wall dissipates significant energy each time, which is good for settling behavior. I'm also considering whether the cup bottom needs a slight concave shape so the ball naturally rolls back toward the ramp and climbs it a little before settling.

The ball will likely end up resting on the cup floor near the ramp's base rather than on the ramp itself, since resting on an incline isn't stable. I need to make sure the ramp's lower end meets the cup floor cleanly—extending the ramp box slightly below the floor surface so there's no visible edge, letting the ball transition smoothly from ramp to floor. The success check is probably just verifying the ball's final position falls within the cup's bounds.

For the physics, I'm estimating the ball enters the cup around 1.1 m/s and rolls across the floor until it contacts the far wall. With MuJoCo's default solref settings (critically damped, dampratio 1), the collision response won't produce a real bounce—the penetration decays back to zero asymptotically rather than reversing velocity, so there's essentially no restitution and the ball should settle quickly rather than bouncing around.

But the ball also has topspin from rolling, and when it hits the wall, friction at the contact point acts upward on the ball due to the spin direction, so there's a chance it could climb partway up the wall. With friction coefficient 0.8, the upward friction impulse could reach roughly 0.88 m/s, so I should check whether that's enough for the ball to climb over the rim or just rise slightly before settling back down.

No need for per-pair friction overrides since default max-friction combination works fine. After the wall impact, the ball's normal velocity is mostly absorbed, and remaining spin drives it back against the wall where friction damps it out, settling the ball at rest in the cup touching the far wall — good enough behavior for this purpose.

I do need to make sure the cup geometry doesn't clip the ramp: I'm checking that at the near wall's position, the ramp surface height (from the slope) sits above the wall's top height so the ramp doesn't collide with the wall itself as the ball rolls down.

Actually, this requires too long a cup for a 10° slope, so I'm considering alternatives — maybe skipping the near wall segment entirely, or having the ramp end as a flat elevated lip at the rim so the ball rolls off horizontally and drops into the cup, using projectile motion (v·sqrt(2h/g)) to check it lands within the cup's inner diameter.

Checking a lower exit speed (~0.75 m/s dropping 0.08m) so the ball lands inside the cup around 0.107m in before hitting the far wall, while making sure the lip is positioned just above the near wall's top so the ball clears it on the way out.

Simplifying by removing the flat lip and having the ramp end right above the near wall's inner edge, just slightly elevated above the wall top. Testing a 15° ramp angle with a 0.3 length giving roughly 1.04 m/s exit velocity, then working out the fall time to see where the ball lands relative to the cup.

Checking that the landing position stays within the inner cup diameter before hitting the far wall, and confirming the wall height is tall enough to contain it even with minor bounce from the vertical landing velocity. Also verifying the ball's forward spin stays roughly consistent with its rolling motion on impact, and that hitting the far wall around 1 m/s won't let it climb over.

Now I'm working out the cup's precise geometry: setting the body position, sizing the cylindrical bottom and its floor height, then calculating the octagonal wall segments' radial thickness, height, and tangential length based on the apothem and side-length trigonometry.

Working out the ramp geometry: computing the top surface's start point from the 15° angle and length, then finding the box center position and figuring out the rotation needed so the ramp slopes correctly downward in the +x direction.

I'm sizing two vertical support boxes under the ramp's upper and lower ends, calculating their positions and heights from the ramp surface geometry so they reach the floor without colliding with the cup or ball.

I'll skip adding side rails since the ball rolls straight down with no lateral forces. Now I'm computing the ball's starting position by placing it a small distance down the slope from the top edge, offsetting by its radius along the surface normal so it sits properly on the ramp.

Checking the physics: rolling distance to the edge of about 0.29m gives a drop height yielding roughly 1 m/s at the bottom, with rolling friction from the contact parameters causing only minor deceleration, which should help the ball settle naturally once it lands in the cup.

After it rolls off the corner, I'm tracking its trajectory to confirm it lands inside the floor area near the far wall rather than overshooting, then checking that its remaining horizontal speed when it hits the wall only lets it climb a few centimeters — well under the wall's height — so it stays contained.

With soft contacts there might be a little restitution causing a bounce back and forth, but rolling friction should kill the velocity within about a second, so it settles within the 5 second window. I'm bumping the rolling friction coefficient up slightly to 0.001 for safety margin, checking that this doesn't meaningfully sap the energy gained from the ramp's incline.

For the cup floor, I'm weighing whether to model it as a cylinder or a box — sphere-cylinder contact should be handled fine by MuJoCo's collider, but using a flat box bottom might be a simpler, more robust choice under the octagonal cup shape.

Now I'm setting up the scene basics: adding a ground plane, a light, and a keyframe that initializes the ball's position and orientation at rest at the top of the ramp with zero velocity, then checking clearance so the ball can pass over the near wall without clipping through it.

Now I'm computing the eight wall positions around the circle at 45-degree increments using cosine/sine of each angle times the radius, and setting the wall box heights to span from the base up to a reasonable height.

Working out the tangential half-length so inner corners stay closed while outer corners have small acceptable gaps, settling on 0.054. Adding ball mass and visual colors to finish up.

