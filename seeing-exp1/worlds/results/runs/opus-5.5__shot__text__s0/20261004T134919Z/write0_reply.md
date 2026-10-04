The ball starts resting on the floor with its center at z = 0.12 m. It is launched at v = (2.865, 0, 8.947) m/s, which gives an apex of about 4.2 m. It then descends at roughly 59° and crosses z = 3.05 m at x = 4.00 m, the center of the 0.457 m rim, at t ≈ 1.40 s.

At that moment the ball's center passes about 0.20 m from the front and back rim tubes. Clearing them only needs 0.128 m (ball radius 0.119 m plus tube radius 0.008 m). The ball passes 2.70 m at its lowest point, so it stays under the backboard's bottom edge at 2.90 m.

Air drag is off: the MuJoCo default air density is zero, so the flight is purely ballistic.

```xml
<mujoco model="basketball_shot">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="2 -3 8" dir="0 0.3 -1" directional="true" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="10 10 0.1" pos="0 0 0" rgba="0.75 0.6 0.4 1"/>

    <!-- Ball: regulation size 7 (circumference ~0.749 m, r = 0.119 m, 0.62 kg), hollow-shell inertia -->
    <body name="ball" pos="0 0 0.12">
      <freejoint name="ball_free"/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.00585 0.00585 0.00585"/>
      <geom name="ball" type="sphere" size="0.119" rgba="0.9 0.45 0.1 1" friction="0.8 0.01 0.001"/>
    </body>

    <!-- Hoop: origin at rim center, 4 m downrange, 3.05 m high. Rim inner radius 0.2286 m, tube radius 0.008 m -->
    <body name="hoop" pos="4 0 3.05">
      <geom name="rim00" type="capsule" size="0.008" fromto="0.2366 0 0 0.2186 0.0905 0" rgba="0.9 0.2 0.1 1"/>
      <geom name="rim01" type="capsule" size="0.008" fromto="0.2186 0.0905 0 0.1673 0.1673 0" rgba="0.9 0.2 0.1 1"/>
      <geom name="rim02" type="capsule" size="0.008" fromto="0.1673 0.1673 0 0.0905 0.2186 0" rgba="0.9 0.2 0.1 1"/>
      <geom name="rim03" type="capsule" size="0.008" fromto="0.0905 0.2186 0 0 0.2366 0" rgba="0.9 0.2 0.1 1"/>
      <geom name="rim04" type="capsule" size="0.008" fromto="0 0.2366 0 -0.0905 0.2186 0" rgba="0.9 0.2 0.1 1"/>
      <geom name="rim05" type="capsule" size="0.008" fromto="-0.0905 0.2186 0 -0.1673 0.1673 0" rgba="0.9 0.2 0.1 1"/>
      <geom name="rim06" type="capsule" size="0.008" fromto="-0.1673 0.1673 0 -0.2186 0.0905 0" rgba="0.9 0.2 0.1 1"/>
      <geom name="rim07" type="capsule" size="0.008" fromto="-0.2186 0.0905 0 -0.2366 0 0" rgba="0.9 0.2 0.1 1"/>
      <geom name="rim08" type="capsule" size="0.008" fromto="-0.2366 0 0 -0.2186 -0.0905 0" rgba="0.9 0.2 0.1 1"/>
      <geom name="rim09" type="capsule" size="0.008" fromto="-0.2186 -0.0905 0 -0.1673 -0.1673 0" rgba="0.9 0.2 0.1 1"/>
      <geom name="rim10" type="capsule" size="0.008" fromto="-0.1673 -0.1673 0 -0.0905 -0.2186 0" rgba="0.9 0.2 0.1 1"/>
      <geom name="rim11" type="capsule" size="0.008" fromto="-0.0905 -0.2186 0 0 -0.2366 0" rgba="0.9 0.2 0.1 1"/>
      <geom name="rim12" type="capsule" size="0.008" fromto="0 -0.2366 0 0.0905 -0.2186 0" rgba="0.9 0.2 0.1 1"/>
      <geom name="rim13" type="capsule" size="0.008" fromto="0.0905 -0.2186 0 0.1673 -0.1673 0" rgba="0.9 0.2 0.1 1"/>
      <geom name="rim14" type="capsule" size="0.008" fromto="0.1673 -0.1673 0 0.2186 -0.0905 0" rgba="0.9 0.2 0.1 1"/>
      <geom name="rim15" type="capsule" size="0.008" fromto="0.2186 -0.0905 0 0.2366 0 0" rgba="0.9 0.2 0.1 1"/>
      <!-- bracket from back of rim to backboard face -->
      <geom name="bracket" type="box" size="0.0675 0.05 0.01" pos="0.3125 0 0" rgba="0.3 0.3 0.3 1"/>
    </body>

    <!-- Backboard (1.83 x 1.07 m), front face 0.15 m behind rim, bottom edge at 2.90 m -->
    <body name="backboard" pos="4.405 0 3.435">
      <geom name="backboard" type="box" size="0.025 0.915 0.535" rgba="0.95 0.95 0.95 0.6"/>
    </body>

    <!-- Support: arm and pole well behind the hoop -->
    <body name="support" pos="0 0 0">
      <geom name="arm" type="box" size="0.8 0.05 0.05" pos="5.23 0 3.6" rgba="0.2 0.2 0.25 1"/>
      <geom name="pole" type="cylinder" size="0.08" fromto="6.1 0 0 6.1 0 3.65" rgba="0.2 0.2 0.25 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 0 0.12 1 0 0 0" qvel="2.865 0 8.947 0 -6 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out the physical parameters for a basketball shot: ball radius ~0.119m, mass 0.62kg, hoop center at 3.05m height and 4m away, with rim inner radius 0.2286m and tube radius ~0.008m. I need the ball to be descending as it passes through the hoop plane so it drops in cleanly rather than bouncing off the rim.

I'm calculating a trajectory with apex around 4.2m: solving for initial vertical velocity (~8.95 m/s) and horizontal velocity (~2.87 m/s) using projectile motion equations, giving a steep descent angle of about 59° at the hoop, which should let the ball pass through the rim opening comfortably given its clearance.

That clearance of 0.196 beats the 0.128 threshold comfortably on both rims, so the trajectory clears fine. I don't think a net is necessary, but I could add a backboard positioned safely behind the rim at x≈4.38 so it stays clear of the ball's path; then I'm working out the remaining fall time after the ball passes through the hoop, solving the quadratic for when it drops the final 2.93 m.

Checking where the ball lands, it comes down around x=5.23, which means it would actually clear the backboard since the ball's height at that point stays below the backboard's bottom edge near 2.9 m. Now I'm figuring out where to place the support pole further back so it's out of the way of the ball's landing and bounce.

Adding a small bracket connecting the rim to the backboard, keeping it clear of the ball's trajectory, then building the rim itself from 16 capsule segments arranged around the ring at a tube radius of about 0.2366, computed via angle steps of 22.5 degrees.

I finish computing all 16 points around the circle, then check the inward chord midpoint distance for the polygon tube, accounting for wall thickness to get the inner radius. Now I'm figuring out where the bracket should attach.

I'm placing the backboard using NBA dimensions, calculating its center position and half-extents in x, y, and z. Then I size a small bracket box connecting the rim to the board, noting that since these are separate static bodies, contacts between them may not actually be computed by the physics engine.

I'm also laying out the support arm and pole geometry, checking whether the ball's trajectory after bouncing could intersect the pole given its landing position and velocity — it looks fine since the floor collision handles things adequately.

For the ball's physical properties, I'm computing inertia for a hollow shell instead of relying on default solid-sphere inertia, giving it an explicit diagonal inertia value matching a hollow sphere formula. I'm leaving air density at zero for pure ballistic motion and setting up contact restitution so the basketball bounces realistically off the floor.

I'm placing the ball just above the floor with a small gap to avoid initial contact, then verifying the launch velocity produces an apex height around 4.2 units by working through the projectile motion equations.

Checking the trajectory at the moment it crosses the rim plane (x=4), I get z≈3.05, which confirms the arc is correct. I'm also estimating the small positional error introduced by the semi-implicit Euler integration (roughly 0.014m lower than ideal), which translates to a negligible horizontal offset of about 0.008m — well within tolerance.

I'll set the freejoint keyframe with qpos and qvel for the shot, and consider adding a slight backspin (negative angular velocity about y) for realism since it's harmless to the trajectory. I'll skip adding a net and move on to writing the file.

