The ball starts at rest near the top of a 15° ramp and rolls down under gravity. It leaves the ramp's lower lip about 0.09 m above the floor, clears the near rim of a 12-segment cup wall, and lands on the cup's base. The base has higher rolling friction, so the ball stops inside the cup within a couple of seconds.

I sized the launch, flight and landing by hand, using rolling-ball kinematics and a ballistic arc. I have not run this file in MuJoCo, so the landing spot and the time it takes to settle are estimates from those calculations, not observed results.

```xml
<mujoco model="ball_ramp_cup">
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <asset>
    <material name="floor_mat" rgba="0.8 0.8 0.8 1"/>
    <material name="ramp_mat" rgba="0.6 0.45 0.3 1"/>
    <material name="cup_mat" rgba="0.2 0.5 0.8 1"/>
    <material name="ball_mat" rgba="0.85 0.15 0.15 1"/>
  </asset>

  <worldbody>
    <light name="key_light" pos="0.3 -0.5 1.2" dir="-0.2 0.4 -1" diffuse="0.8 0.8 0.8"/>
    <light name="fill_light" pos="-0.5 0.5 1.0" dir="0.4 -0.4 -1" diffuse="0.4 0.4 0.4"/>

    <geom name="floor" type="plane" size="1 1 0.1" pos="0 0 0" material="floor_mat"/>

    <!-- Ramp: 0.36 m long, tilted 15 deg, top surface descends toward +x, lower lip top edge at (0, 0.09) -->
    <geom name="ramp_deck" type="box" size="0.18 0.06 0.01" pos="-0.17645 0 0.12693" euler="0 15 0" friction="1 0.005 0.0001" material="ramp_mat"/>
    <geom name="ramp_post_high" type="box" size="0.01 0.04 0.075" pos="-0.30 0 0.075" material="ramp_mat"/>
    <geom name="ramp_post_low" type="box" size="0.01 0.04 0.048" pos="-0.10 0 0.048" material="ramp_mat"/>

    <!-- Cup: base disc plus a 12-segment wall ring, inner radius 0.08 m, rim at z = 0.06 -->
    <body name="cup" pos="0.10 0 0">
      <geom name="cup_base" type="cylinder" size="0.09 0.005" pos="0 0 0.005" friction="1 0.005 0.005" material="cup_mat"/>
      <geom name="cup_wall_0" type="box" size="0.005 0.024 0.025" pos="0.085 0 0.035" euler="0 0 0" material="cup_mat"/>
      <geom name="cup_wall_1" type="box" size="0.005 0.024 0.025" pos="0.07361 0.0425 0.035" euler="0 0 30" material="cup_mat"/>
      <geom name="cup_wall_2" type="box" size="0.005 0.024 0.025" pos="0.0425 0.07361 0.035" euler="0 0 60" material="cup_mat"/>
      <geom name="cup_wall_3" type="box" size="0.005 0.024 0.025" pos="0 0.085 0.035" euler="0 0 90" material="cup_mat"/>
      <geom name="cup_wall_4" type="box" size="0.005 0.024 0.025" pos="-0.0425 0.07361 0.035" euler="0 0 120" material="cup_mat"/>
      <geom name="cup_wall_5" type="box" size="0.005 0.024 0.025" pos="-0.07361 0.0425 0.035" euler="0 0 150" material="cup_mat"/>
      <geom name="cup_wall_6" type="box" size="0.005 0.024 0.025" pos="-0.085 0 0.035" euler="0 0 180" material="cup_mat"/>
      <geom name="cup_wall_7" type="box" size="0.005 0.024 0.025" pos="-0.07361 -0.0425 0.035" euler="0 0 210" material="cup_mat"/>
      <geom name="cup_wall_8" type="box" size="0.005 0.024 0.025" pos="-0.0425 -0.07361 0.035" euler="0 0 240" material="cup_mat"/>
      <geom name="cup_wall_9" type="box" size="0.005 0.024 0.025" pos="0 -0.085 0.035" euler="0 0 270" material="cup_mat"/>
      <geom name="cup_wall_10" type="box" size="0.005 0.024 0.025" pos="0.0425 -0.07361 0.035" euler="0 0 300" material="cup_mat"/>
      <geom name="cup_wall_11" type="box" size="0.005 0.024 0.025" pos="0.07361 -0.0425 0.035" euler="0 0 330" material="cup_mat"/>
    </body>

    <!-- Ball: radius 0.02 m, resting on the upper part of the ramp -->
    <body name="ball" pos="-0.3136 0 0.1955">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.02" condim="6" friction="1 0.005 0.0001" material="ball_mat"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-0.3136 0 0.1955 1 0 0 0" qvel="0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm planning a scene with a tilted ramp box leading to a ball rolling down onto the floor and into a cup, needing to settle within 6 seconds. I'm thinking through the geometry so the cup's walls don't block the ball's entry, likely having the ramp feed directly into the cup opening rather than crossing open floor first.

I'm computing rolling-sphere physics—using solid sphere acceleration (5/7 g sinθ) to find exit velocity from drop height along the ramp, testing different ramp lengths/angles so the ball doesn't exit too fast and overshoot the cup. I'm comparing a short, shallow ramp drop versus a longer one to tune the landing speed so the ball drops cleanly into the cup rather than flying over it.

Then I'm working out the projectile trajectory after the ball leaves the ramp at 15°, decomposing velocity into horizontal and vertical components and setting up the fall-time equation accounting for the ball's radius and base thickness to find where it lands relative to the cup's inner floor.

Given a landing time around 0.099 s and horizontal travel near 0.10 m, I'm checking whether the ball clears the near wall or just nicks the far wall, and I realize with minimal friction the ball could just bounce back and forth in the cup indefinitely, so I need some damping mechanism to let it settle realistically.

Recomputing with a smaller rolling friction coefficient of 0.001, the ramp deceleration is mild enough that the ball still gains speed down the slope but settles reasonably in the cup within a couple seconds. I consider whether a curved bowl shape would help damp motion better, but concave geometry isn't available with primitives, so I'll stick with rolling friction tuned per-contact instead.

Since MuJoCo takes the max of friction and condim values between contacting geoms, I can set the ball with low rolling friction and give the cup's bottom geom higher rolling friction, so the ball rolls freely down the ramp but decelerates sharply once it lands in the cup — leaving the ramp-ball contact negligible while the cup-ball contact absorbs energy quickly. Sliding friction of 1 should be sufficient for the ball to roll properly at the 15° incline angle.

I'm now working out placement: tilting the ramp box by euler="0 15 0" rotates its local x-axis downward as x increases, matching the intended descent direction, and I'm computing the ramp's top surface center and normal vector so I can position the ball resting exactly on that surface (center offset by the ball's radius along the surface normal).

Continuing the computation, the upper end drops to about z=0.183. I'm placing the ball's starting surface point at s=-0.15, giving a center position around (-0.3136, 0, 0.1947), then estimating the rolling acceleration down the incline as roughly 1.814 using the 5/7 factor for a solid sphere on the 15° slope.

With that acceleration over the 0.33m travel, I get final speed around 1.09 m/s, splitting into vx≈1.057 and vz≈-0.283, with about 0.6s spent on the ramp.

I'm also considering whether the ramp needs physical support posts underneath since it's a tilted fixed geometry in the worldbody — thinking about adding a couple of static box posts near the lower end to visually ground it without worrying about collision since they're all static geoms.

Calculating the post position at x=-0.30: using the top surface slope (dz/dx = -tan15°), I find z≈0.170 there, with the underside around 0.160 after accounting for ramp thickness — so I'm sizing a post box with half-height 0.08 (top at 0.16) and a thin profile, roughly 0.01 x 0.05 x 0.08.

For the post at x=-0.1, the underside comes out to about 0.106, giving a half-height near 0.053 — and since both posts sit at x<0 while the ball exits near x≈0, they shouldn't interfere with its flight.

Now I'm tracking the ball as it leaves the ramp edge around (0.005, 0.109) with velocity roughly (1.057, -0.283), then working out the projectile drop of 0.079 to the cup's landing surface by solving the quadratic for time of flight.

I get a flight time near 0.101s, landing the ball at x≈0.112. Now I need to check the cup's wall geometry — the near wall has to sit low enough for the ball's incoming arc to clear it, while the far wall needs to be positioned to catch the ball as it continues rolling forward after landing, so I'm working out wall positions relative to the ball's center trajectory.

Vertical speed at landing is about -1.28 m/s, and with the default soft contact damping bounce should be minimal. The interesting question is the far wall impact: rolling with topspin means the ball's contact point at the front is moving downward relative to its center, so wall friction would actually push the ball upward — meaning it could climb the wall instead of just bouncing back.

Working out the magnitude, the stiction condition for a sphere gives a vertical velocity kick of about 2/7 times the relative slip speed, roughly 0.29 m/s upward, which translates into a small climb height off the wall.

Checking the geometry, I need the wall top around 0.06-0.07 so the ball resting at the base (top at 0.05) stays contained but can escape with enough climb. Given uncertainty in where the ball lands after bouncing, I'll widen the cup to inner radius 0.08, spanning roughly x=0.02 to 0.18 with center at 0.10, to keep the landing comfortably inside.

For the wall itself, instead of flat square panels I'll build it from 12 box segments arranged in a ring around the rim to get a rounder, more cup-like shape—working out the chord length and box dimensions so each segment overlaps slightly with its neighbors, then positioning them at 30° increments around the circle.

For the base, I'll use a flat cylinder with appropriate friction settings so the cup doesn't slide or spin unrealistically when the ball interacts with it, and I'm checking that collision geometry settings (condim) are consistent across contacting surfaces.

Rolling friction is in length units, confirmed. Ball mass with default density works out small and fine, the ramp edge transition should be smooth enough, and rolling deceleration will bring the ball to rest in the cup well within the simulation time—no need for lateral rails since the ball travels straight.

Now I'm setting up the keyframe pose for the ball's freejoint position with a tiny clearance above contact, checking that the ramp posts don't interfere, naming the floor plane and lights, and confirming the cup body is static since it lacks a joint. I'm also verifying the geometry at the ramp's lower end to make sure the ball clears the corner properly as it transitions off the ramp.

I'm checking the clearance between the ramp's bottom corner and the cup's wall segments, confirming the cup wall starts around x=0.01-0.02 and the ramp ends near x=0, giving roughly a 0.01 gap with no overlap. I'm making sure the ball's path near that boundary stays clear of any collision.

Now I'm computing the angular positions for the 12 wall geoms of the cup, using radius 0.085 to find the cosine and sine coordinates at each 30° increment around the circle.

Then I'm placing the ramp geom with its position, rotation, and size, verifying the euler rotation convention about the y-axis gives the correct tilt, before moving on to add the support posts.

I'm working out the underside geometry of the tilted ramp at different x-positions to size and center each support post correctly, correcting an earlier thickness calculation, then considering solver settings like timestep and integrator.

Now I'm defining the ball geometry with appropriate size, friction, and condim settings, aligning its body position with the keyframe qpos, and setting friction values for the cup base and walls to ensure realistic rolling contact throughout the scene.

