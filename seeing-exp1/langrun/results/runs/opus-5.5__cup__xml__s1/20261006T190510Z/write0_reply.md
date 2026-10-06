The ball starts at rest near the top of a 12° ramp. It rolls off the lower end, which hangs over the cup's near rim, drops in, and is stopped by the far wall. Rolling friction (`condim="6"`) on the ball then brings it to rest on the cup floor.

```xml
<mujoco model="ball_ramp_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="0.3 -0.5 1.5" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" size="2 2 0.1" rgba="0.8 0.8 0.75 1"/>

    <!-- Ramp: 0.5 m long, tilted 12 deg, descending toward +x; lower top edge at (0.5, 0.12) -->
    <body name="ramp_body" pos="0 0 0">
      <geom name="ramp_board" type="box" pos="0.25338 0 0.16220" euler="0 12 0" size="0.25 0.06 0.01" rgba="0.6 0.4 0.2 1"/>
      <geom name="ramp_post_high" type="box" pos="0.06 0 0.095" size="0.02 0.04 0.095" rgba="0.4 0.3 0.2 1"/>
      <geom name="ramp_post_low" type="box" pos="0.40 0 0.06" size="0.02 0.04 0.06" rgba="0.4 0.3 0.2 1"/>
    </body>

    <!-- Cup: octagonal, inner apothem 0.11 m, rim at z = 0.09, fixed to the world -->
    <body name="cup" pos="0.6 0 0">
      <geom name="cup_bottom" type="cylinder" pos="0 0 0.005" size="0.12 0.005" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_0" type="box" pos="0.115 0 0.05" euler="0 0 0" size="0.005 0.05 0.04" rgba="0.2 0.4 0.8 0.8"/>
      <geom name="cup_wall_45" type="box" pos="0.08132 0.08132 0.05" euler="0 0 45" size="0.005 0.05 0.04" rgba="0.2 0.4 0.8 0.8"/>
      <geom name="cup_wall_90" type="box" pos="0 0.115 0.05" euler="0 0 90" size="0.005 0.05 0.04" rgba="0.2 0.4 0.8 0.8"/>
      <geom name="cup_wall_135" type="box" pos="-0.08132 0.08132 0.05" euler="0 0 135" size="0.005 0.05 0.04" rgba="0.2 0.4 0.8 0.8"/>
      <geom name="cup_wall_180" type="box" pos="-0.115 0 0.05" euler="0 0 180" size="0.005 0.05 0.04" rgba="0.2 0.4 0.8 0.8"/>
      <geom name="cup_wall_225" type="box" pos="-0.08132 -0.08132 0.05" euler="0 0 225" size="0.005 0.05 0.04" rgba="0.2 0.4 0.8 0.8"/>
      <geom name="cup_wall_270" type="box" pos="0 -0.115 0.05" euler="0 0 270" size="0.005 0.05 0.04" rgba="0.2 0.4 0.8 0.8"/>
      <geom name="cup_wall_315" type="box" pos="0.08132 -0.08132 0.05" euler="0 0 315" size="0.005 0.05 0.04" rgba="0.2 0.4 0.8 0.8"/>
    </body>

    <!-- Ball: radius 3 cm, resting on the ramp surface near its upper end -->
    <body name="ball" pos="0.08563 0 0.2390">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" density="1000" condim="6" friction="0.8 0.005 0.002" rgba="0.85 0.15 0.15 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.08563 0 0.2390 1 0 0 0" qvel="0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

These checks are hand calculations only; I have not simulated the file:

- **Start:** the ball is about 1 mm above the ramp surface. It has 0.43 m of slope to roll.
- **Can it roll?** The rolling-friction ratio is 0.002/0.03 ≈ 0.07. That is well below tan 12° ≈ 0.21, so the ball should roll down rather than stall.
- **Exit speed:** about 0.9–1.1 m/s at the lower edge.
- **Clearing the rim:** the lower edge's top surface is at 0.12 m and the cup rim is at 0.09 m. The ball's bottom therefore starts about 3 cm above the rim.
- **Landing:** the ball should land roughly 2.5–4.5 cm past the cup centre. The far wall stops the ball centre at 8 cm past centre, so it should land inside the cup.
- **Settling:** after a few soft wall contacts, rolling friction should stop it in about 2 s. That is well within the 6 s run.

---
thinking (summarized):

I'm designing the scene with a tilted ramp box leading down to the floor and into a cup, where the cup is built from a floor disc plus surrounding wall boxes—figuring out how the ball can roll over the rim or whether the cup needs to be sunk into the floor so it settles within the time limit.

Need to handle how the ball comes to rest once inside the cup, since without rolling friction it could oscillate between walls indefinitely—considering using condim 6 with a small rolling friction coefficient on the ball to dampen its motion and let it settle naturally.

Working through the ramp angle: it needs to exceed the rolling friction threshold so the ball accelerates down rather than stalling, and a 20° slope comfortably clears that. Sizing the ramp as a tilted box roughly 0.8 long and the ball at 0.03 radius, keeping the geometry simple without extra rails for now.

Now I'm placing the cup at the base of the ramp, deciding between a simple square cup made of four boxes versus an octagonal cup assembled from eight angled wall segments for a nicer look, and working out the inner radius, wall height, and thickness needed so the ball lands and settles inside.

Walls sit from z=0.01 to 0.08. Now checking the ball's physics down the ramp: with rolling-without-slip dynamics at a 20° slope over 0.6m, I'm getting speed around 1.7 m/s, which seems too fast and would overshoot the cup's 0.18 diameter — I need to shorten the ramp or add a drop to kill some horizontal velocity before it reaches the cup.

I'm worried the ball could clear the far wall if speed is too high, though MuJoCo's default contact damping means bounces should be mild. To be safer I'm dialing the slope down to 12° over 0.4m travel, which gives roughly 1.08 m/s — rolling resistance at that angle still leaves enough net acceleration since tan12° comfortably exceeds the resistive ratio.

Now I'm positioning the ramp's lower edge so it ends just inside the cup's near wall, with the top surface high enough that the ball clears the rim as it lands, working out the exact z-height and x-position so the ramp's bottom edge sits just above the wall's top.

Computing the ball's velocity components off the ramp and its drop trajectory into the cup, I find it takes about 0.125s to fall to the cup's floor height, traveling roughly 0.11m horizontally, landing near x≈xc-0.08 plus small offsets.

Landing inside the cup's radius, the ball still has horizontal velocity and rolls into the far wall a short distance away, hitting at a height well within the cup's depth. It bounces back weakly, and with rolling friction decelerating it at roughly 0.47 m/s², it should settle within about 6 seconds, though wall collisions and slip losses complicate the exact timing. I'm now considering whether a higher initial speed changes this outcome.

Adjusting rim height and ramp position so clearances work out, then deriving the rolling-resistance deceleration properly from torque balance: with rolling friction torque and moment of inertia for a sphere, the acceleration down the ramp comes out to (5/7)g times the net driving term after accounting for the resistance.

I'm tuning ramp length and start position by testing target velocities — trying 0.55 m travel gives v≈1.05 m/s, 0.4 m gives v≈0.9 m/s, so I'll settle around a half-length of 0.25 to land near the desired exit speed.

Now I'm working out the launch trajectory off the ramp edge, computing the ball center's offset from the pivot point and solving the projectile drop equation for when it reaches the lower surface height.

For the slower launch speed, the ball lands around xc+0.025, comfortably within the inner wall limit of xc+0.08. For the faster speed, it lands around xc+0.045, still well within bounds.

Now I'm setting up the ramp's rotation around the y-axis to achieve the correct descending angle along the x direction.

Choosing xc=0.6 for the cup center, I'm positioning the ramp's lower edge at x=0.5, z=0.12, then computing the box center by working backward from that edge point using the rotated axis directions - calculating cosine and sine of 12 degrees to find the offset components.

Working out the upper edge gives a center around (0.253, 0.162), with the ramp top reaching roughly z=0.224 at the upper end. Since the ramp will be floating in space, I need a support post beneath the upper end, but I'm wary of adding one at the lower end too since it might collide with the cup's outer wall.

Calculating the post geometry — figuring out heights so each post's top matches the ramp's underside at that x-position without poking through.

Now I'm placing the ball's starting position: computing a point 0.07 along the slope from the upper edge, then offsetting by the radius along the surface normal to get the ball center coordinates.

Checking the remaining travel distance to the ramp's lower edge, friction sufficiency, and the pivot behavior at the ramp exit, all seem fine. I'm now working out the cup geometry—cylinder bottom and wall dimensions, rim height—and confirming the ramp's lower end aligns properly near the cup wall position.

Computing the bottom corner of the ramp's end box in world coordinates to verify it clears the wall's interior edge without overlapping—this checks out, so no collision there before the ball even arrives.

Tracing the ball's path: it leaves the ramp clear of the near wall, lands inside, then rolls toward the far wall and bounces gently off it with residual speed. I'm considering tuning the rolling friction coefficient so the ball settles faster, checking that the deceleration stays consistent with the ramp's incline angle.

Verifying friction combination rules in MuJoCo — since condim is taken as the max between contacting geoms, the ball's friction values will dominate over the cup's defaults, so I'll set rolling friction to 0.002 for a stable, physically reasonable result. I'm now setting up the initial keyframe position for the ball in the qpos array.

I'm laying out the floor plane and octagonal walls geometrically — placing eight angled box walls at 45-degree increments around the center using trigonometry to compute their offset positions, with thin box dimensions and euler rotations matching each wall's angle.

