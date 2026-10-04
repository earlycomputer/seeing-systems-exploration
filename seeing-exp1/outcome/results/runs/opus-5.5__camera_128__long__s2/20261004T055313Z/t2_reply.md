The original shot (vx = 3.60, vz = 10.42 m/s) peaks near 5.6 m and is still about 2.6 m above the rim when it reaches the hoop's x position, so it sails long over the backboard. I replaced it with a flatter, slower shot, worked out by integrating the trajectory by hand rather than running the simulation.

- **Drag model:** I included the fluid drag, about 0.0217·|v|·v per unit mass for the ball's blunt-drag coefficient of 0.25 and air density of 1.2.
- **Path through the rim:** with qvel = (3.41, 0, 9.0), the apex is about 3.9 m at x ≈ 2.7 m. The ball centre reaches z = 3.05 m at x ≈ 4.0 m, about 1.28 s after launch.
- **Entry:** the ball is falling at about 4.0 m/s with about 2.9 m/s forward speed, so it enters roughly 55° below horizontal. At that angle the rim allows about ±8 cm of horizontal error before the ball touches it.
- **Clearances:** the ball clears the bracket and the backboard's bottom edge after passing through.
- **After the hoop:** below the rim it will most likely strike the support pole, around z ≈ 1 m, before reaching the floor. That happens after the basket.

```xml
<mujoco model="basketball_hoop">
  <option timestep="0.002" density="1.2"/>

  <visual>
    <headlight ambient="0.15 0.15 0.15" diffuse="0.3 0.3 0.3" specular="0 0 0"/>
  </visual>

  <worldbody>
    <!-- Lighting: main overhead directional light plus a softer fill spot above the hoop -->
    <light name="overhead_sun" directional="true" pos="2 0 10" dir="0 0 -1" diffuse="0.8 0.8 0.8" specular="0.2 0.2 0.2" castshadow="true"/>
    <light name="overhead_fill" pos="4 0 8" dir="0 0 -1" diffuse="0.3 0.3 0.3" specular="0 0 0" castshadow="false"/>

    <!-- Floor: top surface at z = 0 -->
    <geom name="floor" type="plane" pos="0 0 0" size="10 10 0.1" rgba="0.72 0.52 0.32 1" friction="0.8 0.005 0.0001"/>

    <!-- Regulation size-7 basketball: circumference 0.75 m -> radius 0.1194 m, mass ~0.62 kg (hollow shell inertia 2/3 m r^2) -->
    <body name="ball" pos="0 0 0.1194">
      <freejoint name="ball_free"/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.005893 0.005893 0.005893"/>
      <geom name="ball" type="sphere" size="0.1194" rgba="0.85 0.40 0.10 1" friction="0.9 0.01 0.001" solref="0.01 0.2" fluidshape="ellipsoid" fluidcoef="0.25 0.25 1.5 1.0 1.0"/>
    </body>

    <!-- Hoop: origin at rim center, 4 m along +x, rim at 3.05 m. Fixed to the world (no joint). -->
    <body name="hoop" pos="4 0 3.05">
      <!-- Rim: 16 capsule segments, inner diameter 0.4572 m (18 in), tube radius 0.008 m, tube-center radius 0.2366 m -->
      <geom name="rim_00" type="capsule" size="0.008" fromto="0.2366 0 0 0.2186 0.0905 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_01" type="capsule" size="0.008" fromto="0.2186 0.0905 0 0.1673 0.1673 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_02" type="capsule" size="0.008" fromto="0.1673 0.1673 0 0.0905 0.2186 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_03" type="capsule" size="0.008" fromto="0.0905 0.2186 0 0 0.2366 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_04" type="capsule" size="0.008" fromto="0 0.2366 0 -0.0905 0.2186 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_05" type="capsule" size="0.008" fromto="-0.0905 0.2186 0 -0.1673 0.1673 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_06" type="capsule" size="0.008" fromto="-0.1673 0.1673 0 -0.2186 0.0905 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_07" type="capsule" size="0.008" fromto="-0.2186 0.0905 0 -0.2366 0 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_08" type="capsule" size="0.008" fromto="-0.2366 0 0 -0.2186 -0.0905 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_09" type="capsule" size="0.008" fromto="-0.2186 -0.0905 0 -0.1673 -0.1673 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_10" type="capsule" size="0.008" fromto="-0.1673 -0.1673 0 -0.0905 -0.2186 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_11" type="capsule" size="0.008" fromto="-0.0905 -0.2186 0 0 -0.2366 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_12" type="capsule" size="0.008" fromto="0 -0.2366 0 0.0905 -0.2186 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_13" type="capsule" size="0.008" fromto="0.0905 -0.2186 0 0.1673 -0.1673 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_14" type="capsule" size="0.008" fromto="0.1673 -0.1673 0 0.2186 -0.0905 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_15" type="capsule" size="0.008" fromto="0.2186 -0.0905 0 0.2366 0 0" rgba="0.9 0.3 0.05 1"/>

      <!-- Bracket joining the back of the rim to the backboard face -->
      <geom name="hoop_bracket" type="box" pos="0.3105 0 -0.01" size="0.0705 0.05 0.012" rgba="0.9 0.3 0.05 1"/>

      <!-- Backboard: 1.80 x 1.05 m, 0.03 m thick; front face 0.15 m behind the rim's inner edge (x = 0.381); bottom edge 0.15 m below rim -->
      <geom name="backboard" type="box" pos="0.396 0 0.375" size="0.015 0.9 0.525" rgba="0.92 0.95 0.98 0.85"/>
      <!-- Target square painted on the backboard front (thin, visual only) -->
      <geom name="backboard_square" type="box" pos="0.3805 0 0.145" size="0.0005 0.295 0.225" rgba="0.1 0.1 0.1 1" contype="0" conaffinity="0"/>
    </body>

    <!-- Support: floor plate, vertical pole behind the backboard, and horizontal arm to the backboard's back face (x = 4.411) -->
    <body name="hoop_support" pos="5.2 0 0">
      <geom name="support_base" type="box" pos="0 0 0.025" size="0.4 0.4 0.025" rgba="0.2 0.2 0.25 1"/>
      <geom name="support_pole" type="box" pos="0 0 1.7" size="0.1 0.1 1.7" rgba="0.25 0.25 0.3 1"/>
      <geom name="support_arm" type="box" pos="-0.4445 0 3.3" size="0.3445 0.06 0.06" rgba="0.25 0.25 0.3 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="shot" qvel="3.41 0 9.0 0 0 0"/>
    <!-- Changed qvel from (3.5952, 0, 10.416) to (3.41, 0, 9.0). The old launch peaked near 5.6 m and was
         still ~2.6 m above the rim at x = 4 m, so it flew long over the backboard. Integrating gravity plus
         the ellipsoid blunt drag (0.25 * 1.2 * pi r^2 |v| v, i.e. ~0.0217 |v| v per kg), the new launch
         (~69 deg, 9.6 m/s) peaks at ~3.9 m and brings the ball centre down through z = 3.05 m at x ~= 4.0 m,
         y = 0, about 1.28 s after launch, descending at ~55 deg. That leaves ~+/-8 cm of horizontal margin
         to the rim and clears the bracket and backboard bottom edge on the way through. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to work out the initial velocity so the ball arcs from the start point through the hoop center while accounting for MuJoCo's ellipsoid drag model, which applies a blunt drag force proportional to velocity squared and projected area.

For a sphere there's no slender drag or Magnus lift since there's no spin, so the equation of motion is just gravity plus this quadratic drag term. Computing the drag coefficient from the ball's radius and mass gives roughly k=0.02167 per meter, and now I'm trying to pick a launch angle (around 55°) and solve for the speed that makes the trajectory pass through the hoop with the right descending angle, which will require some rough numerical integration since drag makes this non-trivial analytically.

Trying 65°: vx=3.728, vz=7.994, giving entry angle around 34° at the hoop, which checks out against the rim's effective opening relative to ball diameter — roughly marginal but workable.

Checking the actual clearance: the ball's path must clear the front rim point by more than its radius plus tube thickness, and at 34° the margin is only barely positive (0.132 vs 0.1274 needed). A steeper 45° entry would give better clearance, so I should favor a higher launch angle to make the shot safely clean.

Trying a 70° launch angle instead: working through the velocity components gives vx around 3.12 m/s and vz around 8.57 m/s, landing at the hoop with roughly a 52° entry angle, which clears comfortably. Now I need to account for air drag using numerical integration with small time steps, iterating on initial velocities to converge on the right trajectory.

Continuing the step, I get x=0.327, z=0.961, vx=3.236, vz=7.854 at t=0.1. Moving to t=0.1, I recompute the speed magnitude and drag accelerations for the next midpoint estimate, finding ax≈-0.596 and az≈-11.256 with the midpoint velocities settling near vx=3.206, vz=7.292.

Continuing the numerical integration, I update position and velocity to t=0.3 (x≈0.963, z≈2.311, vx≈3.133, vz≈5.673), then begin computing the drag forces for the next step at t=0.3 with speed magnitude around 6.48.

Continuing the midpoint integration through t=0.5, updating position to roughly x=1.58, z=3.24 with velocity components settling around vx=3.06, vz=3.60.

Continuing the RK2 integration step at t=0.6, computing velocity magnitude and drag-adjusted accelerations for the midpoint, then updating position and velocity values.

Continuing the step integration, updating position and velocity through t=0.8, with drag and gravity still pulling vz down toward zero and x,z steadily increasing.

Continuing the drag integration into t=1.0, updating position and velocity with the new acceleration values, then starting the next midpoint step toward t=1.0's correction.

Continuing the drag-adjusted numerical integration, advancing position and velocity to t=1.2 with updated acceleration values from air resistance.

At t=1.3, position is x=3.953, z=2.947, but the target is x=4, z=3.05 — I'm about 0.117 m short at the required height, with a descent angle near 55.7°, which looks reasonable. I need to scale up the horizontal velocity slightly so the trajectory reaches x=4 right when z=3.05, around t≈1.276.

Correcting the horizontal speed by roughly 3% gives vx0≈3.399, and I'm checking whether the small added drag from the higher speed meaningfully shifts the vertical timing — estimating it's a minor coupling effect that shouldn't change the descent time much.

Working through the extra drag correction more precisely, the vertical effect roughly cancels out while the horizontal drag trims a small amount off x, so I'm nudging vx0 up to about 3.41 to compensate. Now I need to verify the ball's clearance past the front rim using this corrected horizontal offset.

After the rim, the ball continues descending past x=4, and I need to check whether it clears the backboard's bottom edge at z=2.9, x≥4.381 — tracing the trajectory shows it might dip below that edge right around where the backboard begins, so I'm checking the clearance distance there.

Checking whether the ball's trajectory after the hoop clears the support pole—tracing the fall time and horizontal distance, it looks like the ball could actually strike the pole near its base since the landing x-position falls right within the pole's width range.

Still, since the core requirement is just that the ball drops through the hoop, the post-hoop collision with the pole isn't really a problem, and since there's no net modeled on the rim, nothing blocks the ball's pass-through. I'll accept this trajectory as satisfying the task.

Doing a sanity check on the final velocity values confirms the horizontal distance works out close enough to put the ball through the hoop at the right height, so I'm settling on these numbers.

