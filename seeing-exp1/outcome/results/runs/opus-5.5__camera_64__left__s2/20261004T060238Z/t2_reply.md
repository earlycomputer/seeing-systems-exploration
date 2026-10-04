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
    <key name="shot" qvel="3.26 0 9.3 0 0 0"/>
    <!-- Changed qvel from "3.19778 0.27977 9.3 0 0 0" to "3.26 0 9.3 0 0 0".
         Why: the sideways velocity of 0.28 m/s carried the ball about 0.35 m toward +y (shooter's left)
         by the time it reached the hoop. The rim's inner radius is 0.229 m and the ball's radius is 0.119 m,
         so the ball's centre must stay within about 0.11 m of the rim axis; with that drift it could not drop
         through. Setting vy = 0 keeps the flight in the hoop's plane (y = 0).
         The forward speed is also raised slightly, from 3.198 to 3.26 m/s. This is based on my estimate
         of air drag (density 1.2, blunt coefficient 0.25), which takes roughly 0.4 m off the range and
         0.7 m off the height. With that drag, the old forward speed would have brought the ball down
         through the rim plane at about x = 3.92 m, grazing the front of the rim. The extra 0.06 m/s moves
         that crossing to about x = 4.0 m, the rim centre, with the ball descending at roughly 55 degrees.
         Caveat: this rests on reading MuJoCo's drag formula as having no factor of one half. If it does
         include one half, the drag is half as strong, the ball carries much farther, and it would likely
         hit the back of the rim or the backboard instead. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to set vy=0 and pick vx, vz so the ball descends through the rim center, accounting for drag—previously vx=3.2, vz=9.3 overshot the rim height slightly, so I need to lower the trajectory at x=4. I'm working through the drag force model MuJoCo uses for ellipsoids to estimate how much it'll pull the trajectory down.

Given the uncertainty in the exact drag coefficient (whether there's a factor of ½), I'll estimate k somewhere between 0.011 and 0.0217 and try to pick a shot trajectory that's robust to that uncertainty, favoring a steeper entry angle for more tolerance.

I'm thinking through the geometry: with rim clearance around 0.109m and a steep descent angle, I need the drag uncertainty's effect on horizontal position to stay within roughly ±0.05m for the shot to reliably go in.

I'm trying out specific launch angles by hand, testing vx=3.6 and vz=8.087 for a trajectory reaching the rim at x=4m, but that gives a shallow 38° entry angle. I'm adjusting to vx=3.0 instead, aiming for a steeper, more forgiving entry.

Now I'm estimating how drag would perturb this vacuum trajectory, tracking speed at several time steps along the path to approximate the horizontal deceleration and resulting displacement loss.

Finishing the remaining segments gives a total around 15.87, so Δx comes to about -15.9k, roughly -0.34 m or -0.17 m depending on the k value used. For the vertical component, I'm computing the same weighted integral using vz instead, getting large early contributions that taper off and go slightly negative near the end.

The integral sums to roughly 30, so Δz is approximately -28k, putting it around -0.61 m or -0.30 m depending on k. These drop values seem quite large, which makes me want to pin down the correct k by going back to the MuJoCo documentation's ellipsoid fluid model formula for the drag force.

So there's no ½ factor in the formula, which fits with the 0.25 coefficient effectively representing half of a drag coefficient of 0.5, matching a sphere. I'll go with k=0.0217, and note that rotational drag doesn't apply here since there's no spin, but there could be a Kutta lift term proportional to the difference between max and projected area.

With k=0.0217 fixed, I need to work out the correction to the launch velocity so the trajectory, now with drag, still passes through the target point at the right time — essentially adjusting vx and vz by small increments to offset the drag-induced undershoot, using a linear perturbation approach rather than solving exactly.

Rechecking the original trajectory with drag, it seems plausible it actually lands near center if vy=0, suggesting vy may be the only erroneous parameter in the scene. I want to redo the perturbation calculation more carefully to confirm whether the original trajectory truly hits center once vy is zeroed out.

Continuing the remaining points and summing via trapezoid gives roughly 19.97, but since the first segment is convex I refine it with a midpoint check at t=0.15, applying Simpson's rule there to get about 10.21 instead, bringing the total integral closer to 19.8.

Using that, the drag-induced position shift works out to about -0.43, though since drag also reduces velocity over time (a second-order effect I'm approximating), the true shift is smaller, say -0.40, putting x at t=1.4 around 4.08. Now I'm computing the vertical force values at each time point to set up a similar Simpson's integration for the z-direction, getting 128.0, 82.8, 49.8, 12.78, 0, -2.0, and 0 across the sequence, and starting the 0-0.3 Simpson segment which comes out to 25.45.

Continuing the integration from 0.3 onward, the pieces sum to about 35.5, giving a drag-induced vertical shift of roughly -0.77, adjusted down to about -0.72 for the second-order effect, so z at t=1.4 lands around 2.80 — meaning the object is already below the rim by then, so I need to find where it actually crosses the rim plane slightly earlier, accounting for the vertical speed now being around -4.6 due to drag.

Backing up about 0.055 seconds puts the crossing near t≈1.345 with z=3.05 and x≈3.92, which is about 0.08 short of center. Checking clearance, I need the ball's center to stay more than 0.1274 from the rim tube center (located at x≈3.7634 with radius 0.008) at the moment of crossing, given the steep ~57° descent angle.

Computing the perpendicular distance from the trajectory line to the rim point, I get roughly 0.132, which is just barely above the 0.1274 threshold — a very marginal clearance given my ±0.05 uncertainty. I think it's safer to nudge the horizontal velocity slightly so the crossing lands closer to x≈4.0, giving more margin from the rim.

Trying to recall MuJoCo's exact drag formula — it uses blunt and slender drag coefficients applied to projected areas without an explicit ½ factor, which matches my no-½ assumption, and the scene author likely set 0.25 as half of a standard sphere Cd of 0.5 to align with that convention.

Estimating the second-order correction more carefully: drag reduces velocity enough that the force weakens by roughly 5-7% over the trajectory, so I'll settle on a horizontal shift of about -0.40 as a reasonable approximation.

No rotation or Magnus effects apply here, and the ball starts at rest right at floor level, so the launch is clean. I'll settle on qvel="3.26 0 9.3 0 0 0", giving a small horizontal shift that puts the crossing point near x≈4.0.

