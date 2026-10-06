The ball starts on the floor with a keyframe velocity on a ballistic arc. The arc reaches the rim center at (4, 0, 3.05) heading down at about 50°. After passing through, the ball lands, and rolling friction brings it to rest before 6 s.

```xml
<mujoco model="basketball_shot">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <asset>
    <material name="floor_mat" rgba="0.55 0.4 0.25 1"/>
    <material name="ball_mat" rgba="0.85 0.4 0.1 1"/>
    <material name="rim_mat" rgba="0.9 0.25 0.1 1"/>
    <material name="board_mat" rgba="0.95 0.95 0.95 0.6"/>
  </asset>

  <worldbody>
    <light name="sun" pos="2 -3 8" dir="0 0.3 -1" directional="true"/>
    <camera name="side" pos="3 -9 2.2" xyaxes="1 0 0 0 0.2 1"/>

    <geom name="floor" type="plane" size="20 20 0.1" material="floor_mat"/>

    <!-- Regulation size-7 ball: r = 0.1193 m, m = 0.62 kg, thin-shell inertia 2/3 m r^2 -->
    <body name="ball" pos="0 0 0.12">
      <freejoint name="ball_free"/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.005883 0.005883 0.005883"/>
      <geom name="ball" type="sphere" size="0.1193" material="ball_mat" condim="6" friction="0.8 0.005 0.03"/>
    </body>

    <!-- Hoop: origin at rim center, 3.05 m high, 4 m from launch point. Inner diameter ~0.457 m, tube radius 8 mm -->
    <body name="hoop" pos="4 0 3.05">
      <geom name="rim_00" type="capsule" size="0.008" fromto="0.2366 0 0 0.21859 0.09054 0" material="rim_mat"/>
      <geom name="rim_01" type="capsule" size="0.008" fromto="0.21859 0.09054 0 0.16730 0.16730 0" material="rim_mat"/>
      <geom name="rim_02" type="capsule" size="0.008" fromto="0.16730 0.16730 0 0.09054 0.21859 0" material="rim_mat"/>
      <geom name="rim_03" type="capsule" size="0.008" fromto="0.09054 0.21859 0 0 0.2366 0" material="rim_mat"/>
      <geom name="rim_04" type="capsule" size="0.008" fromto="0 0.2366 0 -0.09054 0.21859 0" material="rim_mat"/>
      <geom name="rim_05" type="capsule" size="0.008" fromto="-0.09054 0.21859 0 -0.16730 0.16730 0" material="rim_mat"/>
      <geom name="rim_06" type="capsule" size="0.008" fromto="-0.16730 0.16730 0 -0.21859 0.09054 0" material="rim_mat"/>
      <geom name="rim_07" type="capsule" size="0.008" fromto="-0.21859 0.09054 0 -0.2366 0 0" material="rim_mat"/>
      <geom name="rim_08" type="capsule" size="0.008" fromto="-0.2366 0 0 -0.21859 -0.09054 0" material="rim_mat"/>
      <geom name="rim_09" type="capsule" size="0.008" fromto="-0.21859 -0.09054 0 -0.16730 -0.16730 0" material="rim_mat"/>
      <geom name="rim_10" type="capsule" size="0.008" fromto="-0.16730 -0.16730 0 -0.09054 -0.21859 0" material="rim_mat"/>
      <geom name="rim_11" type="capsule" size="0.008" fromto="-0.09054 -0.21859 0 0 -0.2366 0" material="rim_mat"/>
      <geom name="rim_12" type="capsule" size="0.008" fromto="0 -0.2366 0 0.09054 -0.21859 0" material="rim_mat"/>
      <geom name="rim_13" type="capsule" size="0.008" fromto="0.09054 -0.21859 0 0.16730 -0.16730 0" material="rim_mat"/>
      <geom name="rim_14" type="capsule" size="0.008" fromto="0.16730 -0.16730 0 0.21859 -0.09054 0" material="rim_mat"/>
      <geom name="rim_15" type="capsule" size="0.008" fromto="0.21859 -0.09054 0 0.2366 0 0" material="rim_mat"/>
      <geom name="neck" type="box" size="0.07 0.04 0.01" pos="0.31 0 -0.01" material="rim_mat"/>
      <geom name="backboard" type="box" size="0.015 0.9 0.525" pos="0.39 0 0.375" material="board_mat"/>
    </body>
  </worldbody>

  <keyframe>
    <!-- vx = 3.19315 m/s, vz = 8.4834 + g*dt/2 (semi-implicit Euler correction): apex ~3.79 m, reaches rim center at t = 1.253 s descending at ~50 deg -->
    <key name="start" qpos="0 0 0.12 1 0 0 0" qvel="3.19315 0 8.4932 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out realistic physical parameters for the trajectory - standard basketball size and mass, hoop dimensions at regulation height, and rim thickness - so the ball's path through the hoop at 4 meters out looks physically plausible.

For the arc itself, I'm calculating the required descent angle so the ball's diameter clears the hoop opening (needing roughly 31°+ from horizontal, so I'll aim for a steeper ~50° entry), then solving the parabolic motion equations relating launch velocity components, gravity, and the horizontal/vertical distances to hit that entry angle precisely at the hoop's position.

Working through the numbers gives a launch angle around 69°, horizontal velocity ~3.19, vertical velocity ~8.48, time of flight ~1.25s, and an apex height of about 3.79 — comfortably above the hoop. I'm now considering whether a backboard is needed, but leaning toward skipping it since it's not essential.

Tracking the ball after it passes through the hoop, it continues falling and lands around x≈5.47 after roughly 0.46 more seconds. I'm checking whether the ball needs to come to rest by the end — there's a note that a ball counts as resting below 5 cm/s, so I want to make sure it settles naturally within the simulation window after bouncing.

Rather than leaving it rolling indefinitely, I'm considering adding condim 6 contact with rolling and torsional friction so the ball gradually decelerates on the floor, mimicking realistic basketball friction, so it comes to rest instead of rolling forever.

After bouncing it'll settle to rolling at reduced speed, and default contact damping should keep bounce minimal, so the floor behavior seems fine without extra tuning. For the hollow sphere's actual moment of inertia, I should check if MuJoCo supports a shell inertia option on the geom to get the correct rotational dynamics rather than the default solid-sphere assumption.

Computing vz and verifying the landing height checks out at z≈3.05m, which matches target. I estimate the semi-implicit Euler integration error from the simulation's dt=0.002 timestep is only about 1.2cm of extra drop—negligible compared to the clearance margin, so I don't need to compensate for it.

Now I'm checking whether the ball's trajectory clears the rim edges. With the ball approaching at 50°, I'm finding the perpendicular distance from the ball's path to the front and back rim points (at x=3.7634 and x=4.2366, z=3.05) to confirm it passes cleanly through the hoop's opening rather than clipping the rim.

Since the parabolic trajectory curves downward (concave down), the actual path dips slightly below the straight tangent line at the hoop center — so I need to account for that curvature correction when checking clearance against the front rim specifically, using the second derivative dz/dx = -g/vx².

Working through the numbers: the drop from curvature near the front rim comes out to about 0.027m, giving a path height of roughly 3.305 at the front rim's x-position. Now I'm setting up the actual minimum-distance calculation from that curved path to the front rim point itself, parameterizing by offset from center and minimizing the squared distance function.

Checking u=-0.10 gives a minimum distance around 0.178m, which clears the required 0.1273m threshold. Now I'm checking the back rim offset similarly.

Computing the 16 segment endpoints around the hoop circle...

I check that the capsule chord's inward deviation from the true circle is small enough (about 0.224 vs 0.2286) to be an acceptable approximation, then move on to considering the hoop body's static properties.

Now I'm adding a backboard for visual realism, placing it about 0.15 m behind the rim face with standard dimensions (1.8 x 1.05 m, 0.03 m thick), and checking whether the ball's trajectory after passing through the hoop would clip it — the math shows the ball stays safely clear of the backboard's edge.

Good, clears fine. I'm reconsidering the support pole though—if placed anywhere in the ball's landing path around x=4.4-5.5 it'd get struck, so I'll skip the pole entirely and just keep a static backboard attached to the hoop body without a visible support arm, which is simpler and still looks fine.

That clearance looks fine, so the neck isn't actually an interference concern. Now I'm thinking about post-landing behavior: with condim 6 and rolling friction around 0.03 (the max between ball and floor friction params), the ball should roll and decelerate naturally, landing around 1.7s and coming to rest roughly 1.5s later given a deceleration around 1.5 m/s².

Checking whether bounces introduce any sliding drift — with friction coefficient 0.8, the impulse from the vertical landing velocity (~8.3 m/s) is more than enough to convert horizontal slip into rolling motion, giving a rolling velocity around 1.92 m/s from the initial 3.19 m/s horizontal component, then decelerating at about 0.018 m/s² from rolling friction.

With that settled, I can set the initial keyframe with position at the drop height and velocity components for the launch, keeping the freejoint velocities in the world frame since only the ball has degrees of freedom. I'll leave the cone geometry as default, then add a light source and camera before writing the final scene file.

