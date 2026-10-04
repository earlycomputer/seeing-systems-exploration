The shot now enters the hoop in my calculation, with about 5 cm of clearance from the rim. I could not run MuJoCo here, so this rests on hand integration rather than a simulation.

**Why the original falls short.** Using the scene's own drag (air density 1.2, blunt-drag coefficient 0.25 on the ball's cross-section), the old launch speed brings the ball back down to rim height at x ≈ 3.86 m. That is about 0.14 m short of the hoop centre and onto the front of the rim.

**The fix.** Only the `shot` key changes, from `qvel="2.9532 0 8.556"` to `qvel="3.33 0 8.7"`:
- **Forward speed** goes from 2.95 to 3.33 m/s. This makes up the horizontal distance lost to drag, so the ball comes down at the hoop centre.
- **Upward speed** goes from 8.556 to 8.7 m/s. This keeps a high arc, peaking about 0.7 m above the rim, so the ball drops in steeply.

**Predicted path.**
- The ball's centre falls through rim height (z = 3.05) at x ≈ 4.00 m, about 1.25 s after launch.
- It is moving roughly 3.0 m/s forward and 3.5 m/s downward, so it enters at about 49° below horizontal.
- At that angle it clears both the front and back of the rim by about 5 cm.
- The ball's top is still below the bottom of the backboard (z = 2.9) when it reaches the backboard's position, so it does not hit the board.
- After passing through, it probably strikes the support pole at about 1 m height before it reaches the floor. That happens after it has gone in, so it does not affect the result.

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
    <key name="shot" qvel="3.33 0 8.7 0 0 0"/>
    <!-- Changed shot qvel from "2.9532 0 8.556 0 0 0" to "3.33 0 8.7 0 0 0".
         Why: with the scene's air drag (density 1.2, blunt-drag coefficient 0.25 on the
         ball's cross-section) the old launch brought the ball back down to rim height
         (z = 3.05) at x ~ 3.86 m, about 0.14 m short of the hoop centre and onto the
         front rim. Raising forward speed to 3.33 m/s makes up that distance; raising
         upward speed to 8.7 m/s keeps a high arc (peak ~3.8 m), so the ball enters
         steeply. Hand integration with drag (not checked by running MuJoCo) puts the
         ball's centre through rim height at x ~ 4.00 m about 1.25 s after launch,
         descending at ~49 deg, clearing the front and back rim by ~5 cm and passing
         under the backboard's bottom edge. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to account for drag when estimating velocity, so I'm working through MuJoCo's fluid model for an ellipsoid shape, considering blunt and slender drag coefficients plus angular drag to get a realistic force estimate.

Running the numbers gives a drag deceleration of roughly 0.01 per v², modest at shooting speeds (~0.9 m/s² at 9 m/s). I'm now thinking about the trajectory needed for the ball to pass through the hoop center while clearing the rim with enough margin, aiming for a steep descent angle around 55° with sufficient apex height, then I'll solve the no-drag case first and apply a correction for the small horizontal deceleration drag introduces.

Let me just set up a numerical midpoint integration with candidate velocities vx=3.2, vz=8.7, stepping through drag and gravity accelerations each 0.1s to see where it lands, targeting a point around x=4, z=3.05 on the way down.

Continuing the next integration step: computing drag speed and acceleration terms, then updating position to roughly x=0.634, z=1.648 and velocity vx≈3.143, vz≈6.6 at this timestep.

Continuing the drag integration through t=0.3 and t=0.4, updating position and velocity each step as drag force decreases with speed.

Continuing the RK2 integration step: updating drag forces, velocities, and positions at t=0.6, getting x=1.87447, z=3.4741 with vx=3.0683, vz=2.5620, then starting the next half-step calculation.

Continuing the drag integration step by step, advancing velocity and position to t=0.8 with updated speed and drag coefficient calculations.

Continuing the midpoint integration step, updating velocity and position at t=1.0 with drag-adjusted acceleration, then starting the next timestep's calculations.

Continuing the numerical integration, I'm advancing velocity and position through t=1.2, recalculating drag forces and accelerations at each half-step of this RK2-style simulation.

By x=4.0, z has dropped to about 2.86, below the 3.05 target height. Interpolating, the trajectory crosses z=3.05 around t≈1.254 at x≈3.856, so I need roughly 0.14 m more horizontal reach — meaning I should slightly increase the initial horizontal velocity.

Bumping vx to around 3.32-3.33 (accounting for extra drag at higher speed) should put x at roughly 4.0 when z=3.05, while the descent angle at that point works out to about dz/dx ≈ -1.17.

Checking the backboard clearance now: by the time the ball's front edge reaches the backboard face at x=4.381, the center has dropped enough that its top sits around z=2.83, just under the 2.9 bottom edge of the backboard—a tight but workable margin.

I also verify the shot clears both the near and far rim edges by computing the perpendicular distance from each rim point to the ball's descending trajectory line (at a 49° angle), finding about 0.179 on both sides versus the required 0.127, giving a comfortable 0.05 margin. The support bracket near x=4.24–4.381 sits below rim height, so the ball passes over it safely too.

Now I'm tracing where the ball lands after falling through: starting around x=4, z=2.86, with velocity components vx≈3, vz≈-3.8, I solve the fall time to ground level and get roughly x≈5.3, which could put the ball on a collision course with the hoop's support pole located between x=5.1 and 5.3.

Since the task only cares about whether the shot goes in, hitting the pole afterward doesn't matter—the ball already passed through the hoop. I'm also double-checking how drag affects the vertical velocity as horizontal speed increases slightly, since that could trim a bit off the arc height.

Working through the horizontal drag loss similarly, scaling by the increased speed, I get x landing around 4.0 at crossing time near 1.253, so settling on qvel values of 3.33, 0, 8.7, 0, 0, 0 seems right. I'm a little uncertain whether MuJoCo's ellipsoid fluid model also accounts for added mass effects beyond simple drag.

Magnus vanishes with zero spin, viscous drag vanishes with zero viscosity, and blunt drag uses the projected area of a sphere, πr². That covers the relevant terms, so I'll note this in a comment.

