**What the file does.** The ball starts on the floor at x = 0 with velocity (3.21, 0, 9.3) m/s and a backspin of −30 rad/s about y. `density="1.2"` and `fluidshape="ellipsoid"` turn on MuJoCo's ellipsoid fluid model. The fifth `fluidcoef` is the Magnus coefficient, set to 1.0. That gives a Magnus force ρV·ω×v of about 0.0086 × 30 × 9.8 ≈ 2.5 N, which is several times larger than the real lift on a basketball. At launch it pulls the ball back with about −3.9 m/s² horizontally. Drag (C = 0.25) removes about 1 m/s² more, and angular drag only slowly bleeds off the spin.

**Expected trajectory.** I integrated it by hand. Horizontal speed falls from 3.2 to about 1.4 m/s by the apex, which is near (x ≈ 1.95 m, z ≈ 4.7 m) at t ≈ 1 s. On the way down the backspin adds only a little forward push. The ball comes back down through 3.05 m at roughly x ≈ 2.9 m, about a metre short of the rim. It then lands on the floor around x ≈ 3.3 m without touching the hoop.

Without any air at all the same launch would overshoot to x ≈ 4.8 m and hit the backboard. So the launch matches neither the air model in the file nor a vacuum.

**Fix.** I removed the air model by dropping `density` and the fluid attributes, and re-solved the launch as a ballistic shot:
- Apex at about 4.6 m, so vz = 9.38 m/s.
- The ball descends through z = 3.05 at t = 1.519 s.
- vx = 4 / 1.519 = 2.633 m/s puts the centre at x = 4.00 m at that moment.
- The descent angle is about 64°.
- MuJoCo's semi-implicit Euler shifts the crossing by only about 7 mm, well inside the ±0.109 m clearance between the ball and the rim.
- Clearance to the front and back rim tubes stays at least 0.21 m against the 0.127 m needed.
- The ball passes under the bracket and backboard, then drops to the floor and bounces off the base of the support pole.
- I kept a mild backspin. It only matters on contact.

```xml
<mujoco model="basketball_hoop">
  <option timestep="0.002"/>

  <visual>
    <headlight ambient="0.15 0.15 0.15" diffuse="0.3 0.3 0.3" specular="0 0 0"/>
  </visual>

  <worldbody>
    <light name="overhead_sun" directional="true" pos="2 0 10" dir="0 0 -1" diffuse="0.8 0.8 0.8" specular="0.2 0.2 0.2" castshadow="true"/>
    <light name="overhead_fill" pos="4 0 8" dir="0 0 -1" diffuse="0.3 0.3 0.3" specular="0 0 0" castshadow="false"/>

    <!-- Floor: top surface at z = 0 -->
    <geom name="floor" type="plane" pos="0 0 0" size="10 10 0.1" rgba="0.72 0.52 0.32 1" friction="0.8 0.005 0.0001"/>

    <!-- Regulation size-7 basketball: radius 0.1194 m, mass 0.62 kg (hollow shell inertia 2/3 m r^2) -->
    <body name="ball" pos="0 0 0.1194">
      <freejoint name="ball_free"/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.005893 0.005893 0.005893"/>
      <geom name="ball" type="sphere" size="0.1194" rgba="0.85 0.40 0.10 1" friction="0.9 0.01 0.001" solref="0.01 0.2"/>
    </body>

    <!-- Hoop: origin at rim center, 4 m along +x, rim at 3.05 m. Fixed to the world. -->
    <body name="hoop" pos="4 0 3.05">
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

      <geom name="hoop_bracket" type="box" pos="0.3105 0 -0.01" size="0.0705 0.05 0.012" rgba="0.9 0.3 0.05 1"/>
      <geom name="backboard" type="box" pos="0.396 0 0.375" size="0.015 0.9 0.525" rgba="0.92 0.95 0.98 0.85"/>
      <geom name="backboard_square" type="box" pos="0.3805 0 0.145" size="0.0005 0.295 0.225" rgba="0.1 0.1 0.1 1" contype="0" conaffinity="0"/>
    </body>

    <body name="hoop_support" pos="5.2 0 0">
      <geom name="support_base" type="box" pos="0 0 0.025" size="0.4 0.4 0.025" rgba="0.2 0.2 0.25 1"/>
      <geom name="support_pole" type="box" pos="0 0 1.7" size="0.1 0.1 1.7" rgba="0.25 0.25 0.3 1"/>
      <geom name="support_arm" type="box" pos="-0.4445 0 3.3" size="0.3445 0.06 0.06" rgba="0.25 0.25 0.3 1"/>
    </body>
  </worldbody>

  <keyframe>
    <!-- Ballistic shot (no air): apex ~4.6 m, centre crosses z = 3.05 descending at t = 1.519 s, x = 4.00 m, ~64 deg descent -->
    <key name="start" qvel="2.633 0 9.38 0 -10 0"/>
  </keyframe>
</mujoco>
```

```json
{"what_happens": "In the original file, the strong Magnus force from the -30 rad/s backspin (MuJoCo's C_M = 1 is several times too large for a basketball) plus drag slows the ball's forward speed from 3.2 to about 1.4 m/s by the apex. The ball comes back down through rim height near x = 2.9 m, about a metre short of the hoop, and lands on the floor without touching it. In the corrected file there is no air; the ball arcs to about 4.6 m, falls through the rim centre at about 64 degrees with clearance, passes under the backboard and lands behind the hoop.", "works": false, "problem": "The enabled fluid model (density 1.2, Magnus coefficient 1.0, 30 rad/s backspin) pulls the ball back so hard that it comes down through 3.05 m about 1.1 m short of the hoop."}
```

---
thinking (summarized):

I'm tracing the ball's trajectory starting at its initial position with given velocity and angular velocity, noting the negative spin suggests backspin, and considering how MuJoCo's fluid model with Magnus lift coefficients would affect its flight path.

Ignoring drag, I calculate the time to reach hoop height works out to about 1.497 s, putting the ball's x-position around 4.8 m—overshooting the hoop and possibly hitting the backboard. But I realize drag forces matter here, so I'm estimating the drag coefficient effect using the ball's mass and cross-sectional area, finding the deceleration is significant enough to meaningfully shift the landing point, and now I'm working out the Magnus force contribution as well.

Plugging in the initial velocity gives Fx ≈ -2.39 N and Fz ≈ 0.825 N, which seems surprisingly large — that backspin of 30 rad/s is nearly 5 rev/s, quite high. I'm also wondering whether angular drag matters here, recalling that MuJoCo models a damping torque on spin proportional to angular velocity squared, scaled by an inertia-like factor for the sphere's geometry.

Computing that moment of inertia term for the sphere gives roughly 8.13e-5, leading to a damping torque around 0.066 N·m and angular deceleration near 11 rad/s² initially — so the spin decays over the 1.5 second flight following a hyperbolic falloff rather than staying constant at 30 rad/s.

I'm also confirming the Magnus force formula uses the cross product of angular velocity and velocity scaled by the Magnus coefficient, density, and volume, and that MuJoCo's Kutta lift term vanishes for a sphere due to symmetry while viscosity defaults to zero. Now I need to check whether the ball's trajectory passes cleanly through the rim near x=4 at z=3.05, accounting for the radius tolerance between the rim and ball, which requires working through the numerical integration of the trajectory by hand.

Setting up the initial state with x=0, z at the ball's radius, and the given velocity and spin components, I'm deriving the acceleration equations incorporating drag and Magnus effects, then computing the drag coefficient per unit mass and the Magnus coefficient per unit mass using the ball's volume and air density.

Computing the Magnus coefficient over time, since spin decays following ω(t)=30/(1+0.3726t), and recalling the angular drag torque formula from MuJoCo's documentation involving the moment of inertia tensor. Now I'm setting up the numerical integration step with dt=0.1.

At t=0, with vx=3.21 and vz=9.3, I compute the accelerations: ax comes out around -4.19 and az around -9.47, combining gravity, linear drag, and the Magnus effect. That's a large deceleration in x, so vx will drop toward zero quickly, and I need to track how the Magnus force in x shrinks as vz decreases and eventually flips sign once vz goes negative.

Using Heun's method with dt=0.1, I predict vx≈2.79 and vz≈8.35 after the first step, then recompute the speed and forces at that predicted state—getting ax≈-3.60 and az≈-9.49—so the averaged accelerations over the step land around -3.90 for x and -9.4 for z.

Averaging gives vx1≈2.820, vz1≈8.352, updating position to x1≈0.3015, z1≈1.002. Now I'm recomputing the accelerations at t=0.1 using these new velocities, finding |v|≈8.815 and working out ax≈-3.603 before continuing to az.

Working through to az≈-9.482, I predict the next velocities (vx≈2.460, vz≈7.404) and step to t=0.2, recalculating ω, kM, and |v|≈7.802 to get ax≈-3.061 and az≈-9.488. Averaging these gives vx2≈2.487, vz2≈7.4035, and I start updating x2.

Continuing to integrate position and velocity: I compute x2≈0.567 and z2≈1.790 from the averaged velocities. Moving into step 3 at t=0.2, I recompute |v|≈7.810 with the current vx and vz, derive ax≈-3.063 and az≈-9.478, then predict vx≈2.181 and vz≈6.456 heading into the next timestep at t=0.3.

z3=2.483, continuing the integration into step 4 with t=0.3, updating velocities to vx=2.2056, vz=6.4558, recomputing drag and Magnus accelerations giving ax≈-2.567, az≈-9.466, then predicting vx=1.9489, vz=5.5092 for the next step and starting to recompute ω and kM at t=0.4.

Now I'm averaging accelerations to get ax=-2.3375, az=-9.4615, updating velocities to vx4=1.9718, vz4=5.5096, and integrating positions to x4=1.0104, z4=3.081 before moving into step 5 at t=0.4.

Continuing the RK-style integration, I compute drag-adjusted accelerations at the predicted velocity (vx=1.9718, vz=5.5096), getting ax=-2.110, az=-9.449, then predict vx=1.7608, vz=4.5647 for the next half-step, updating the spin-dependent magnus coefficient (ω=25.29, kM=0.349) and recomputing ax=-1.686 at t=0.5.

Averaging gives ax=-1.898, az=-9.443, updating vx5=1.782, vz5=4.5653, x5=1.198, z5=3.585. I notice x is only reaching about 1.2 m at t=0.5 while vx keeps shrinking, so horizontal distance will fall well short of 4 m unless I'm miscalculating something — I'll keep stepping forward to see where vz hits zero around t≈0.98 and check the total range.

Continuing to t=0.5-0.6, I recompute ax and az using updated speed and spin-dependent magnus terms, getting vx≈1.613, vz≈3.622 at the predictor step, then refining with ω and kM at t=0.6 to get ax≈-1.295 and az dropping further toward -9.81 adjusted by drag and magnus contributions.

Averaging the predictor-corrector values gives vx6≈1.633, vz6≈3.623, updating position to x6≈1.369, z6≈3.994. Moving to step 7 at t=0.6, I recompute the magnus coefficient and accelerations again, getting ax≈-1.296, az≈-9.414, then predict vx≈1.503, vz≈2.681 heading into t=0.7.

Continuing the RK2 integration, I compute acceleration and velocity updates for steps 8 and 9, getting vx8=1.4455, vz8=1.742, with position x8=1.6749, z8=4.530, then begin step9 at t=0.8.

Continuing the integration step, I compute drag and gravity accelerations for step 10, average the predictor-corrector values, and update velocity and position to get vx10=1.3897, vz10=-0.1364, x10=1.9569, with z10 still being finalized using the average vertical velocity.

Now looking at the descent phase from 4.69m down to the hoop at 3.05m, roughly a 1.64m drop that takes about 0.59s with effective gravity reduced by Magnus lift. The horizontal velocity grows modestly from Magnus effects but the resulting x position at hoop height comes out around 2.9m, well short of the 4m target distance.

Let me double check the Magnus force formula used by MuJoCo - the default fluidcoef sets drag at 0.25 but keeps the Magnus coefficient at 1.0, which seems unusually strong compared to a real ball's lift coefficient of roughly 0.2-0.3.

Computing the realistic Magnus force for this spin ratio gives about 0.77 N, but MuJoCo's formula yields roughly 2.5 N - nearly 3x stronger. Checking the vacuum trajectory, the launch velocity doesn't seem tuned for either a no-air scenario or a drag-only scenario, suggesting the scene creators accounted for drag but overlooked the Magnus effect's outsized influence.

I'm confirming the fluid forces are indeed active since density and fluidshape are set. The simplest fix would be removing spin and air resistance entirely, then designing the trajectory analytically for a vacuum - though I need to remember the rim clearance constraint, where the ball's center must stay within about 0.109 units of the rim center to pass through cleanly.

I realize default fluidshape uses the legacy inertia-box drag model when density>0, so for exact analytic trajectory I should set density=0 and drop the fluid attributes entirely. Spin only matters on contact, so I don't need to worry about it for a clean swish — I'll just leave angular velocity small or zero rather than overthinking backspin realism.

Now working through the trajectory math: starting at height 0.1194, I pick an apex of 4.6m giving rise height 4.4806m, solve for initial vertical velocity (~9.376 m/s), then compute time up (0.9558s) and time falling from apex to rim height 3.05m (0.5622s) for a total flight time of 1.518s. With horizontal distance 4.0m, that gives vx=2.635 m/s, and checking the descent angle at the hoop (~64° from horizontal) confirms a nice steep, realistic approach.

I'm also accounting for MuJoCo's semi-implicit Euler integration at dt=0.002, which introduces a small positional error (~0.0147m low in z) since velocity updates before position each step — I need to factor that into my initial velocity choices to hit the target accurately.

Checking that the ball's descending trajectory clears the rim: when the center passes near z=3.17 (rim height plus ball radius), the crossing happens about 0.022s earlier than the ideal trajectory, shifting x to roughly 3.942 — still within the margin needed to clear the rim safely.

Computing distances to both the near and far rim points as the ball descends past z=3.05, each time confirming the gap stays above the 0.1274 radius threshold (around 0.21-0.22), so the trajectory passes clean through without contact.

Clear past the bracket, so I track the ball falling to the floor—solving for landing time gives x≈5.04, but checking the support pole at x 5.1-5.3 reveals the ball's edge at 5.16 actually collides with the pole before reaching the floor.

Ball bounces off the pole near the bottom, which is fine for realism since it already passed through the hoop. I also check the support arm's position (x 4.411-5.1, z 3.24-3.36) and confirm the ball's trajectory apex at x≈2.52 never reaches it, so no interference there.

Backboard top sits at z=3.95 near x=4.381, well past the ball's path, so nothing obstructs it on the way up either. The inertia and ball contact bounciness settings look fine as is, so I just need to remove density from the options block, keeping only the timestep, before writing the final file.

