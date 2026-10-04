The shot was short, so I raised the launch speed and kept its steep angle (vx 2.953 → 3.336 m/s, vz 8.556 → 9.10 m/s). I worked the new values out by hand, including the scene's air drag, and did not run the simulation.

- **Path:** the ball now peaks at about 3.95 m. It comes back down to rim height (3.05 m) at x ≈ 4.0 m, the centre of the hoop, about 1.3 s after launch.
- **Entry:** it falls at roughly 55° from horizontal. Along that path it passes about 0.19 m from both the front and back of the rim, where the minimum is 0.127 m (ball radius plus rim tube). That leaves about 6–7 cm of margin either way.
- **Backboard and bracket:** it clears both.
- **Main risk:** the drag force is my estimate of MuJoCo's ellipsoid model (about 0.013·v² N). If MuJoCo's actual drag differs a lot from this, the ball could land a few centimetres off.

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
    <key name="shot" qvel="3.336 0 9.10 0 0 0"/>
    <!-- Changed qvel from "2.9532 0 8.556 0 0 0" to "3.336 0 9.10 0 0 0".
         Why: the old launch was short. Even without drag its centre came down to rim height (3.05 m)
         at x = 3.77 m, right on the front rim, and the scene's air drag (density 1.2, ellipsoid
         fluid model) shortened it further.
         New values come from hand integration that includes the blunt drag
         (about 0.25*rho*pi*r^2*v^2, roughly 0.013 v^2 N). The ball peaks near 3.95 m and descends
         through z = 3.05 m at x of about 4.0 m (hoop centre) at t of about 1.3 s, falling at
         roughly 55 degrees (vx about 2.9, vz about -4.1 m/s).
         Clearance: about 0.19 m from the front and back rim versus 0.127 m needed (ball radius
         plus rim tube); the backboard and bracket are also clear. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to account for drag so the ball's center passes through the hoop at z=3.05 near x=4.0 while descending, and I should double-check it clears the backboard front face given the ball's radius. I'm estimating the drag coefficient from MuJoCo's ellipsoid fluid model to figure out how much velocity to add for the trajectory to land correctly.

Working through the physics: using C_D,blunt=0.25, ball radius 0.119m giving projected area ~0.0448 m², mass 0.62kg, I get a drag deceleration constant k≈0.0217/m, with magnus/kutta lift negligible since there's no spin. Now I'm setting up a rough numerical integration at a launch angle around 55° to see how much initial speed is needed to overcome drag losses over the ~7m path.

Trying 55° without drag first: solving for v0 gives about 9.26 m/s with vx=5.31, vz=7.59. But checking the timing, the ball is still ascending when it reaches the target x-distance (peak time 0.773s vs arrival time 0.753s) — meaning this angle is too shallow and I need to steepen it so the ball is descending into the target.

At 60°, v0 comes out to about 8.86 m/s with vx=4.43, vz=7.68, and now the ball is descending at arrival with a downward velocity around -1.18 m/s, giving a shallow entry angle of roughly 15°. But given the ball's diameter relative to the rim, I need an entry angle steeper than about 32° (ideally closer to 45°) for a clean shot through the hoop, so 60° still isn't steep enough — I should stick closer to the original 71° launch angle, which naturally produces a much steeper, more reliable entry.

Trying t=1.3s without drag: vx=3.08, vz=8.63, giving a descent velocity at the hoop of -4.12 m/s and an entry angle around 53°, which looks good. Now I need to account for drag using a numerical simulation with k≈0.02168, stepping through velocity and position over small time intervals to correct the ideal trajectory.

Continuing to compute speed magnitude |v(t)| at each 0.1s step from 0.1 through 1.0, tracking how it decreases then starts rising again as vz goes negative near t=0.9-1.0.

Now I'm computing the drag deceleration ax_d = -k|v|*vx component at each time step, using the drag coefficient times the speed magnitude to get instantaneous horizontal deceleration values.

I'm then weighting each deceleration value by its remaining time (T-t) and setting up a trapezoidal integration to sum the contribution over the full time interval, halving the endpoint terms.

Finishing that integral gives a total horizontal displacement of about -0.289 m. Now I'm computing the drag-induced vertical deceleration term using k|v|vz at each time step, building toward another similar integration for vertical displacement.

Summing up all these weighted terms gives approximately 5.734, and multiplying by the step size of 0.1 yields a correction factor of about 0.573, suggesting a displacement change of roughly -0.573 meters.

Now I need a second Newton iteration since increasing speed increases drag quadratically. I estimate the velocity corrections (Δvx≈0.222, Δvz≈0.441 per unit time) and scale the drag deficit by the squared velocity ratio, giving a refined deficit of about 0.318 in x, with the z deficit still to be worked out.

The horizontal tolerance is roughly 0.10 m, which given the angled trajectory should still work if I aim near center. I'm also second-guessing the exact drag formula MuJoCo uses—whether it's the blunt drag coefficient times density times projected area times velocity squared, with no viscous or spin effects since viscosity is zero and there's no rotation. If my drag model is off by even a factor of 0.5, the resulting position error could be around 0.15 m, but a steeper entry angle gives more margin, so I'll accept the approximation and move toward a quick numeric check.

I'm running through a midpoint (RK2) integration by hand with initial velocity components and position, computing the speed magnitude and drag deceleration term step by step to see where the trajectory lands.

Continuing the integration through steps 3 and 4, updating velocity and position with drag and gravity each time: at step 3 the velocity settles near (3.150, 5.763) giving position (0.968, 2.339), then I move into step 4 starting from that same velocity to compute the next midpoint.

Continuing the RK2 integration, I get new velocity (3.074,3.685) at x=1.5901, z=3.2812, then step 6 gives v=(3.045,2.674) at x=1.8959, z=3.5987, and I'm starting step 7 with speed s=4.052.

Continuing the step-by-step integration, I'm tracking position and velocity through steps 9 and 10, applying drag deceleration with midpoint corrections to get x around 2.8-2.97 and z approaching 3.95 as velocity slows and turns negative in the z-component.

Continuing the step-by-step integration, updating velocity, drag acceleration, and position through steps 12 and 13, with the trajectory now dropping to about z=3.0 and x nearing 3.97.

At t=1.3 the ball reaches roughly x=3.973, z=3.059, just 0.021 short of the rim center at x=4.0, so I nudge vx up slightly to 3.336 to correct this with minimal effect on z. I set the velocity accordingly and check the backboard clearance—after crossing the rim plane the ball moves to about x=4.23, z=2.72, which I compare against the backboard's bottom edge and front face to confirm it clears.

Checking the back rim position (4.2366, 3.05) against the ball's path near x=4.11, the distance comes out to about 0.204, safely clearing the 0.127 rim radius. I now move on to check clearance against the front rim at (3.7634, 3.05) using the ball's position near x=3.85.

Checking where the ball lands after the floor path — it travels to roughly x≈5.4, near the support base and pole region, but since we only care about where it first lands, anything after that point doesn't matter. The backboard's bottom edge also clears the trajectory with margin. Good, I can write the final comment now.

