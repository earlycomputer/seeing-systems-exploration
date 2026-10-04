Below is the corrected scene; only the `qvel` of the `shot` key changed.

**Why it missed:** the old launch of (3.60, 0, 10.42) m/s peaked about 2 m above the rim. The ball sailed over the rim, the board and the support.

**New launch:** (3.341, 0, 9.05) m/s.

**How I chose it:** I stepped the flight by hand at 0.1 s, using the scene's own air settings.
- **Drag:** the blunt-drag force is ρ·0.25·πr²·|v|v. With this ball that slows it by about 0.0217·|v|·v per second.
- **Air lift:** buoyancy reduces gravity by about 1.4%. I don't know for certain that MuJoCo applies buoyancy in this fluid model, so I aimed halfway between gravity with and without it.

**Predicted flight:**
- The ball peaks at about 3.9 m, near x ≈ 2.8 m.
- It reaches the rim's height while falling, at about x ≈ 4.00 m, around t ≈ 1.3 s.
- It enters at roughly 55° below horizontal.
- It clears the front rim by about 5–6 cm and the back rim by about 5 cm.

**Margin:** if my buoyancy assumption is wrong either way, the ball crosses the rim about 4 cm off centre and still clears the front rim.

**Caveat:** I have not run the simulation. These numbers come from a hand integration.

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
    <key name="shot" qvel="3.341 0 9.05 0 0 0"/>
    <!-- Changed shot qvel from "3.5952 0 10.416 0 0 0" to "3.341 0 9.05 0 0 0".
         The old launch peaked near 5 m, about 2 m above the rim, and flew long over the rim,
         the backboard and the support. The new launch, integrated by hand with this scene's
         air drag (rho*0.25*pi*r^2*|v|v, i.e. about 0.0217*|v|*v per second for this ball)
         and gravity taken halfway between with and without buoyancy, peaks at about 3.9 m
         near x = 2.8 m. It falls through rim height (z = 3.05 m) at about x = 4.00 m,
         t ~ 1.3 s, entering at about 55 degrees below horizontal. It clears the front rim
         by about 5-6 cm and the back rim by about 5 cm; y velocity stays zero, so it is
         centred left-right. Not checked by running the simulation. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to work out the velocity needed so the ball's center passes exactly through the rim center while descending, accounting for the rise of about 2.93 m over a 4 m horizontal distance. I'm thinking a descending angle near 45° with an apex around 4 m high makes sense, then I can solve for the initial vertical velocity.

Computing the actual numbers now: vz0 comes out to about 8.73 m/s with a rise time near 0.89s and a fall time of 0.44s for the remaining drop, giving a total flight time of 1.33s and a horizontal velocity of 3.0 m/s. That checks out to a reasonable ~55° entry angle with vz around -4.32 m/s at the rim.

Next I need to account for drag using MuJoCo's ellipsoid fluid model — computing the projected area of the sphere and the blunt drag coefficient to get an equivalent drag force formula, which works out to something like an effective Cd of 0.5 times density times area times velocity squared.

I'm also checking whether Kutta lift or Magnus effects matter here — since the ball has no spin, both should be negligible. Then I'm estimating buoyancy from the fluid density, which reduces effective gravity by about 1.4%, and trying to recall whether MuJoCo's ellipsoid fluid model actually applies buoyancy forces or just drag and lift terms.

Computing the drag coefficient k as 0.02167/m, I'm now trying to numerically integrate the trajectory by hand using a midpoint method with dt=0.1s, starting with a guess of vx0=3.3, vz0=9.0, and tracking position and velocity magnitude step by step to hit the target point at x=4, z=3.05.

Continuing the drag-adjusted integration, I update velocities and positions again with midpoint corrections, bringing x to about 0.6472 and z to about 0.9617 at this step.

Continuing the position updates at t=0.3, I compute the acceleration from drag and gravity, then do another midpoint step to get updated velocities around 3.09 and 4.6 for the x and z components.

Continuing the integration step, I update position and velocity using the midpoint drag values: x reaches 1.5811, z reaches 3.2515 at t=0.5, with velocity components around vx=3.0574, vz=3.6620. I then compute the next midpoint drag forces for t=0.5 to 0.6, getting ax≈-0.289, az≈-9.975.

Continuing the RK2 integration step, I update position and velocity to t=0.7, then begin computing the midpoint drag forces for the next step toward t=0.8.

Continuing the RK2 integration step, updating velocity and position at t=0.9 then computing midpoint drag forces for the next step.

Continuing the step integration: updating velocity and position at t=1.1, then computing drag acceleration for the next midpoint estimate at t=1.1-1.2.

Continuing the update, by t=1.3 the ball reaches x≈3.95, z≈3.05, just shy of x=4 where it needs to pass through the rim. I'm checking whether it clears the hoop opening given the rim's inner radius and the ball's radius, which leaves about 0.109 clearance for horizontal tolerance.

The offset of about -0.049m at the entry point is small but matters given the ~55° descent angle shrinks the effective opening. To correct for this, I'll scale vx up slightly (roughly by 4/3.951) so the trajectory centers better through x=4, while checking this doesn't create a backboard clearance issue near the apex.

Now I need to verify the ball clears the front rim: tracing the path from (3.66, 3.41) toward (3.95, 3.05), I'm checking the perpendicular distance from the front rim point (3.763, 3.05) to this line segment to confirm sufficient clearance.

Checking the bracket clearance too - distance comes out to 0.175, safely clear of the 0.119 threshold. Adjusting for the slightly higher drag coefficient, vx ends up about 1.24% larger, so recalculating the trajectory at t=1.3 gives x≈4.0 with minimal change to the vertical position.

That's too close for comfort, touching the front rim. I'm now trying to recall whether MuJoCo's ellipsoid fluid model actually includes a buoyancy term at all, since the box model clearly does but I'm uncertain whether the ellipsoid implementation applies the same force.

Given uncertainty about buoyancy effects, I'll hedge by aiming for a gravity value centered between estimates, around 9.74, since that keeps the crossing error small either way. Recomputing trajectory with this effective gravity, the vertical drop by t=1.3 shifts by roughly 0.057, bringing z to about 2.997 once I adjust x with the velocity bump.

Correcting for that drop means nudging vz0 up by about 0.047, so vz0≈9.05, giving qvel "3.341 0 9.05 0 0 0". Checking the crossing tolerance at both gravity extremes shows the clearance stays above 0.15, comfortably more than the 0.127 threshold, so I'm confident this setup works and ready to write up the comment.

