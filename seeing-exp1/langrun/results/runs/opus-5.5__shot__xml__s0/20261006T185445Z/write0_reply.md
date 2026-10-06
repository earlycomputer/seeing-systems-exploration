The ball starts resting on the floor and is launched at about 9.2 m/s at 71° above horizontal (vx = 3.009, vz = 8.725 m/s), with a little backspin. It peaks at about 4.0 m and comes down through the rim centre at 3.05 m, 1.33 s after launch, at roughly 55° below horizontal.

**Hand checks**
- **Ball:** size-7, radius 0.1193 m, mass 0.62 kg, with hollow-shell inertia.
- **Rim:** 18″ inner diameter, built from 16 capsule segments.
- **Clearance at the rim:** with the 55° entry, the ball centre comes no closer than about 0.19 m to the front or back rim tube. A collision needs 0.127 m (ball radius plus tube radius).
- **Backboard:** the falling ball passes beneath its lower edge (2.90 m).

```xml
<mujoco model="basketball_shot">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="2 -3 8" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="10 10 0.1" rgba="0.75 0.6 0.4 1" friction="0.8 0.005 0.0001"/>

    <!-- Backboard (1.83 m x 1.07 m), front face at x = 4.38, bottom edge at 2.90 m -->
    <geom name="backboard" type="box" pos="4.395 0 3.435" size="0.015 0.915 0.535" rgba="0.95 0.95 0.95 0.6"/>
    <geom name="backboard_square" type="box" pos="4.378 0 3.30" size="0.002 0.30 0.225" rgba="0.9 0.2 0.1 1" contype="0" conaffinity="0"/>
    <!-- Support arm and padded pole -->
    <geom name="support_arm" type="box" pos="5.105 0 3.30" size="0.695 0.05 0.05" rgba="0.2 0.2 0.25 1"/>
    <geom name="pole" type="cylinder" fromto="5.8 0 0 5.8 0 3.35" size="0.1" rgba="0.2 0.2 0.25 1"/>

    <!-- Hoop: origin is rim centre, 3.05 m high, 4 m from launch point -->
    <body name="hoop" pos="4 0 3.05">
      <geom name="rim_00" type="capsule" fromto="0.23660 0 0 0.21859 0.09054 0" size="0.008" rgba="1 0.35 0 1"/>
      <geom name="rim_01" type="capsule" fromto="0.21859 0.09054 0 0.16730 0.16730 0" size="0.008" rgba="1 0.35 0 1"/>
      <geom name="rim_02" type="capsule" fromto="0.16730 0.16730 0 0.09054 0.21859 0" size="0.008" rgba="1 0.35 0 1"/>
      <geom name="rim_03" type="capsule" fromto="0.09054 0.21859 0 0 0.23660 0" size="0.008" rgba="1 0.35 0 1"/>
      <geom name="rim_04" type="capsule" fromto="0 0.23660 0 -0.09054 0.21859 0" size="0.008" rgba="1 0.35 0 1"/>
      <geom name="rim_05" type="capsule" fromto="-0.09054 0.21859 0 -0.16730 0.16730 0" size="0.008" rgba="1 0.35 0 1"/>
      <geom name="rim_06" type="capsule" fromto="-0.16730 0.16730 0 -0.21859 0.09054 0" size="0.008" rgba="1 0.35 0 1"/>
      <geom name="rim_07" type="capsule" fromto="-0.21859 0.09054 0 -0.23660 0 0" size="0.008" rgba="1 0.35 0 1"/>
      <geom name="rim_08" type="capsule" fromto="-0.23660 0 0 -0.21859 -0.09054 0" size="0.008" rgba="1 0.35 0 1"/>
      <geom name="rim_09" type="capsule" fromto="-0.21859 -0.09054 0 -0.16730 -0.16730 0" size="0.008" rgba="1 0.35 0 1"/>
      <geom name="rim_10" type="capsule" fromto="-0.16730 -0.16730 0 -0.09054 -0.21859 0" size="0.008" rgba="1 0.35 0 1"/>
      <geom name="rim_11" type="capsule" fromto="-0.09054 -0.21859 0 0 -0.23660 0" size="0.008" rgba="1 0.35 0 1"/>
      <geom name="rim_12" type="capsule" fromto="0 -0.23660 0 0.09054 -0.21859 0" size="0.008" rgba="1 0.35 0 1"/>
      <geom name="rim_13" type="capsule" fromto="0.09054 -0.21859 0 0.16730 -0.16730 0" size="0.008" rgba="1 0.35 0 1"/>
      <geom name="rim_14" type="capsule" fromto="0.16730 -0.16730 0 0.21859 -0.09054 0" size="0.008" rgba="1 0.35 0 1"/>
      <geom name="rim_15" type="capsule" fromto="0.21859 -0.09054 0 0.23660 0 0" size="0.008" rgba="1 0.35 0 1"/>
      <!-- Bracket joining the rim to the backboard -->
      <geom name="bracket" type="box" pos="0.3083 0 -0.01" size="0.0717 0.04 0.01" rgba="1 0.35 0 1"/>
      <!-- Visual-only net -->
      <geom name="net_0" type="capsule" fromto="0.230 0 0 0.140 0 -0.40" size="0.003" rgba="1 1 1 0.7" contype="0" conaffinity="0"/>
      <geom name="net_1" type="capsule" fromto="0.1626 0.1626 0 0.0990 0.0990 -0.40" size="0.003" rgba="1 1 1 0.7" contype="0" conaffinity="0"/>
      <geom name="net_2" type="capsule" fromto="0 0.230 0 0 0.140 -0.40" size="0.003" rgba="1 1 1 0.7" contype="0" conaffinity="0"/>
      <geom name="net_3" type="capsule" fromto="-0.1626 0.1626 0 -0.0990 0.0990 -0.40" size="0.003" rgba="1 1 1 0.7" contype="0" conaffinity="0"/>
      <geom name="net_4" type="capsule" fromto="-0.230 0 0 -0.140 0 -0.40" size="0.003" rgba="1 1 1 0.7" contype="0" conaffinity="0"/>
      <geom name="net_5" type="capsule" fromto="-0.1626 -0.1626 0 -0.0990 -0.0990 -0.40" size="0.003" rgba="1 1 1 0.7" contype="0" conaffinity="0"/>
      <geom name="net_6" type="capsule" fromto="0 -0.230 0 0 -0.140 -0.40" size="0.003" rgba="1 1 1 0.7" contype="0" conaffinity="0"/>
      <geom name="net_7" type="capsule" fromto="0.1626 -0.1626 0 0.0990 -0.0990 -0.40" size="0.003" rgba="1 1 1 0.7" contype="0" conaffinity="0"/>
    </body>

    <!-- Regulation size-7 basketball: r = 0.1193 m, m = 0.62 kg, hollow-shell inertia 2/3 m r^2 -->
    <body name="ball" pos="0 0 0.12">
      <freejoint name="ball_free"/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.00588 0.00588 0.00588"/>
      <geom name="ball" type="sphere" size="0.1193" rgba="0.85 0.4 0.1 1" friction="0.8 0.005 0.0001"/>
    </body>
  </worldbody>

  <keyframe>
    <!-- Apex ~4.0 m; passes rim centre (4, 0, 3.05) descending at ~55 deg after 1.33 s -->
    <key name="start" qpos="0 0 0.12 1 0 0 0" qvel="3.009 0 8.725 0 -6 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out the physical parameters for a basketball shot animation—ball needs to arc from the floor through a hoop set 3.05 m high and 4 m away, so I'm referencing regulation sizes for the ball and rim to get the geometry right.

Picking a steep 55° entry angle with an apex around 4 m, I calculate the launch velocity components using kinematics: vz0 ≈ 8.73 m/s, vx ≈ 3.01 m/s, giving a total flight time near 1.33 s. I verify the ball's diameter fits well within the rim's effective opening at that entry angle, confirming clean clearance.

Now I'm checking whether the ball's trajectory clips the front rim tube before reaching center — treating the trajectory as a line near the rim and computing the perpendicular distance from the near-side rim tube center to that line, which needs to exceed the combined ball and tube radii (~0.127 m) to avoid collision.

The computed margin comes out to about 0.194 for the front rim, well clear. I check the back rim similarly, getting a comparable margin despite the path curving slightly as it descends, leaving roughly 0.067 clearance. I should also add a backboard behind the hoop, since regulation specifies a set distance between the rim's inner edge and the backboard.

So the backboard plane sits at x ≈ 4.38, with standard 1.83×1.07 m dimensions. I trace the ball's trajectory past the rim to check whether it'd strike the backboard before hitting the floor, solving for when it falls from 3.05 m down to 0.12 m — giving roughly 0.449 s and a horizontal position around x = 5.35, well past the backboard, so no collision.

Checking the backboard's lower edge at about 2.9 m, I compute the ball's height when it's directly beneath that edge and find it clears with room to spare (around 2.64 m, below the 2.9 m threshold). Now I need to figure out where to put the support pole so it doesn't interfere with the ball's landing spot near x = 5.35 — maybe mounting it via a bracket from the board itself is simpler than placing a freestanding pole.

I'll make the net non-colliding geoms with contype/conaffinity set to 0 so they're purely visual, or skip the net entirely for simplicity. For the rim, I'm approximating the torus shape using 16 capsule segments arranged around the circle, calculating the centerline radius and checking that the chord clearance still keeps the rim diameter close to the real 0.2286 m spec.

Computing coordinates...

Now checking whether the rim bracket connecting to the backboard could interfere with the ball's path, estimating the ball's z-height near that x-region to confirm it stays clear.

Checking the minimum distance to the front rim as well, computing the same trajectory calculation before the rim crossing point — minimum comes out around 0.19, comfortably clearing the 0.127 threshold too.

I'm also thinking about physics realism: whether to add damping or special bounce properties to the ball contact, but default friction and solver settings should let the ball roll naturally without extra tuning. For the initial gap, I'll set the ball's starting height to just above the ground radius so there's a small clearance at spawn.

For mass properties, since a basketball is really a hollow shell rather than a solid sphere, I'm setting an explicit inertial element with mass 0.62 and diagonal inertia computed from the hollow-sphere formula (2/3 m r²) rather than letting the solver infer it from geometry, which would assume a solid ball and give the wrong rotational dynamics.

For the keyframe initial conditions, I'm giving the ball its launch position and velocity, and considering whether to add backspin by assigning an angular velocity about the y-axis — working out the sign convention so the top of the ball rotates backward relative to its forward motion. Since MuJoCo's default setup has no fluid dynamics, there's no Magnus effect to worry about, so the spin is mostly cosmetic for this setup, but I'll still add a small backspin value for realism.

Double-checking the numbers more precisely: solving for fall time and apex velocity gives t_a≈0.8894s, fall time for the 0.95m drop ≈0.4401s, total time of flight ≈1.3295s, horizontal velocity ≈3.00867, and vertical velocity at the rim ≈4.31729 — confirming the values I'll plug into the keyframe.

Now I'm working out the floor and backboard geometry — the plane dimensions, where the ball lands after bouncing near the pole, and placing the backboard box so its center sits at z=3.435 with the bottom edge just below the rim at 2.90, consistent with regulation dimensions. I'm also calculating the bracket offset so the backboard face aligns correctly relative to the rim position.

I'm now positioning the support pole so the ball doesn't collide with it after bouncing — checking the ball's landing position and velocity against the pole's radius and location, and adjusting the pole placement outward to roughly 1.2m behind the baseline per regulation overhang distance.

For the net, I'm adding a ring of thin capsules from the rim down to a smaller ring below it, using alternating angles for a basketweave look, all non-colliding so the ball passes through visually but not physically.

