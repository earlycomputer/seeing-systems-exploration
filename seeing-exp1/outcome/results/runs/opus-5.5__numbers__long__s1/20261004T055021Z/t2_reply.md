The original launch, `qvel="3.5952 0 10.416 0 0 0"`, peaks near 5.0 m and passes over the hoop about 1.65 m too high, so it lands long. I lowered both components so the ball arcs to about 4.4 m and comes down steeply onto the rim.

**How I chose the new velocity.** I hand-integrated a model of gravity plus quadratic drag (deceleration of about 0.016·|v|·v, which matched the previous run's numbers) for the new launch of vx = 3.0 m/s and vz = 9.7 m/s. Under that model:

- The ball peaks at about 4.4 m, near x ≈ 2.8 m.
- It reaches x = 4.0 m at about z ≈ 3.05 m, falling at about 5 m/s against about 2.6 m/s forward, an entry angle of roughly 60°.
- At that angle the rim's opening is about 0.41 m wide as the ball sees it, against the ball's 0.24 m diameter. That leaves roughly ±0.09 m of horizontal margin at the rim plane.
- The ball stays clear of the front rim, the bracket and the backboard.

**What I can't confirm.** These figures come from my estimate, not from a new MuJoCo run. The drag model and the small speed loss when the ball leaves the floor are approximations, so the shot should be re-run to confirm it drops through the hoop.

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
    <key name="shot" qvel="3.0 0 9.7 0 0 0"/>
    <!-- Changed shot qvel from "3.5952 0 10.416 0 0 0" to "3.0 0 9.7 0 0 0". The old launch peaked near
         5.0 m and crossed x = 4 m at z ~ 4.7 m, sailing over the rim and backboard and landing long at
         x ~ 6.1 m. A hand-integrated gravity + quadratic-drag model (fit to the old run) puts the new launch
         at a ~4.4 m apex, crossing the rim plane (z = 3.05 m) at x ~ 4.0 m while descending at roughly
         60 degrees, which leaves about +/-0.09 m of clearance inside the 0.457 m rim for the 0.239 m ball.
         Lateral velocity stays 0, so y stays centred. This is an estimate, not a simulated result: re-run to
         confirm the ball drops through. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to account for air drag affecting the trajectory from (0,0,0.119) to (4,0,3.05). Comparing the no-drag estimate of peak height against the observed value shows drag is reducing the ball's rise significantly, so I need to adjust the initial velocity components to compensate.

Let me try a new approach: picking T=1.0 second, solving for vx=4 and vz=7.836 to hit the target, then checking what apex height this produces without drag before factoring drag back in.

With T=1.2 instead, I get vx=3.333 and vz=8.329, giving a steeper 46° entry angle at the hoop — much better for clearing the rim. Now I need to go back and recalibrate the drag coefficient more precisely from the original trajectory data, since the initial speed was about 11.02 m/s.

Checking the first time step, the x-position comes out oddly short compared to the no-drag estimate, which seems too large a deficit for simple air drag alone — I'm wondering if the floor contact at the very start, with the ball resting exactly at its initial height, is introducing a friction impulse that bleeds off some initial horizontal velocity before the ball actually leaves the ground.

Checking the z-velocity differences across intervals, I get roughly 11.6 m/s² effective deceleration, consistent with gravity plus drag at that speed. Extrapolating back to the midpoint of the first interval gives a velocity close to the expected launch value minus drag losses, so the numbers line up reasonably well.

There's a small discrepancy though: observed displacement (0.486) is slightly less than predicted (0.505), suggesting a tiny initial loss, maybe from contact penetration. Similarly the horizontal velocity drops about 3% in the first step, which is odd since the ball is moving away from the floor — I suspect the contact constraint is still active at zero distance and friction is removing some momentum even though the normal force shouldn't affect vz directly.

Looking at the vx sequence over time, I'm trying to fit a drag model where deceleration scales with speed times vx, estimating a drag coefficient k from the early steps versus near the peak, but the numbers aren't quite consistent between the two regions.

I'll just go empirical instead: use k≈0.016 for quadratic drag, apply a roughly 3% initial velocity loss, and crudely integrate the trajectory step by step with dt=0.1 to find launch velocities that land at x=4, z=3.05 while descending, starting from a guess of vx≈3.6 and vz≈8.7 adjusted for the loss.

Continuing the numerical integration through more time steps, tracking velocity decay from drag and position updates, with horizontal distance approaching about 1.36 and height still climbing before it will eventually peak and fall.

Continuing the step-by-step velocity and position integration, I see the projectile's height peak and begin descending around t=0.7-0.8s, with vertical velocity turning negative while horizontal position keeps advancing steadily past x=3.

This trajectory falls short, landing too low around z=3.05 near x=3.68. I need to boost both horizontal and vertical velocity—trying vx=3.75, vz=8.7 as new targets and re-running the integration from scratch to check if this gets closer to the goal.

Continuing the simulation, drag keeps decreasing as velocity drops while gravity's effect stays near constant, with position creeping forward to about x=1.8-2.1 and height climbing past 3 meters by t=0.5s, velocity settling around 4.9 m/s.

Continuing the trajectory, at t1.0 velocity drops to about (3.398,-2.540) with x near 3.89, z near 3.36, and by t1.1 x reaches the target 4 while z keeps falling, so I'm solving for the exact time fraction where x crosses 4 to get the corresponding z value.

I find z is still about 0.22 too high there. Since dz/dx is roughly -0.85 near that point, I estimate the first trial lands z=3.05 around x≈3.69 while this trial reaches it around x≈4.25, so I need to interpolate between the two trials to find the launch condition that gives z=3.05 exactly at x=4.

I'm cross-checking my drag coefficient guess by looking at the original trajectory's peak height and estimating whether k=0.016 reproduces the observed peak around x≈3.25, z≈5.01.

The match is close with k maybe slightly lower around 0.013, and the velocity decay over the first second lines up reasonably with the observed values, so I'm now verifying the early loss ratio assumption against the recorded position after the first short time step.

Vz loss is similarly small, around 0.4%, so I'm adjusting my launch estimate upward by about 1% with a small lag of roughly 0.01s in the integration. Now I'm checking the tolerance window: with the ball's radius and rim's inner radius, the center has roughly ±0.109 m of margin to clear the hoop.

But accounting for the entry angle changes things — the effective opening through the rim narrows to roughly 2R sinθ, and comparing that against the ball's diameter gives a minimum angle requirement near 31.5°. At the actual 40° entry angle, the margin is only about ±0.027 m, which is quite tight.

Going steeper, like 50°, widens that margin to roughly ±0.07 m along x, which is much safer, so I should aim for a higher arc with an apex around 4.3 m and target the center of the rim at x=4, z=3.05.

Now I'm running a new trajectory simulation with drag coefficient k=0.016, stepping through velocity and position updates over small time increments to see where the ball lands relative to the rim.

Continuing the trajectory simulation, velocity and drag are decaying steadily as the projectile approaches around t=0.7s, with horizontal position nearing 2.5 and height dropping toward 4.2.

Continuing the trajectory simulation, drag is reducing horizontal velocity while gravity pulls the projectile downward, tracking position through each timestep as it arcs forward and descends.

At x=4.0m the height overshoots the target of 3.05m by about 0.67m, so I keep stepping forward and find the trajectory crosses z=3.05 near x≈4.44, meaning the range needs to shrink by roughly 0.44m — I need to reduce the launch velocity's horizontal component to pull the landing point back.

Scaling vx down by a factor of about 0.90 (to 2.97) and recomputing, I find the trajectory now crosses z=3.05 almost exactly at x=4.0, with the velocity there giving a steep entry angle around 63°, which is a nice steep approach into the hoop. I also check that the apex height and the arc near the backboard stay clear of the rim structure.

With this entry angle, I estimate the tolerance window for error: given the drag coefficient uncertainty (k between 0.013–0.016), the resulting vertical error at the hoop plane translates to roughly a small fraction of a meter, well within the acceptable margin for the shot to still fall through.

Running the step-by-step numerical integration with k=0.016, tracking velocity, drag, and position updates across each timestep to see how closely it tracks the observed trajectory values.

The model consistently overshoots z by a small, slowly growing margin (0.017 at t=0.1, 0.035 at t=0.5), while x-tracking stays tight against observed values. This suggests the drag coefficient is roughly right but maybe slightly underestimated, so the actual trajectory might land a touch shorter than my prediction in the new shot.

For the launch I'll settle on qvel="3.0 0 9.7 0 0 0", applying the lag correction to get effective values around vx 2.97, vz 9.6. Checking clearance against the rim: the ball passes well above the front edge near x≈3.77, and at the back rim around x 4.24-4.38 the trajectory still clears comfortably as it descends through the bracket zone.

