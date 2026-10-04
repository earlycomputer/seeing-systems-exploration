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
    <key name="shot" qvel="2.88 0 10 0 0 0"/>
    <!-- Changed forward speed from 3.5952 to 2.88 m/s and upward speed from 10.416 to 10 m/s to target the hoop on descent with air drag, instead of overshooting. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Calculating drag coefficients and trajectories**

I'm working through some physics calculations related to drag and trajectory. I’m looking at linear drag coefficients and trying to solve for horizontal velocity and other factors. As I break it down, I see the effects of drag leading to some vertical loss. I’m trying to target specific speeds and account for how fluid dynamics might play into the results. I need to be careful about drag sensitivity near the hoop to avoid risks when the ball approaches at a shallow angle.

**Determining trajectory clearance**

I need to ensure a clean, steep downward trajectory to avoid hitting the front rim. For a sphere at the rim, with specific dimensions for the ball and clearance, I’m calculating the needed slope. I’m checking if the effective horizontal clearance is below the specified radius. This requires a particular slope greater than 1.3. I'm targeting a vertical speed of 10 with a horizontal speed of 2.6, ensuring the ball can avoid hitting the rim by passing within a certain range.

**Reviewing Mujoco formulas**

I'm looking at the Mujoco documentation and noticing a formula for calculating a force related to drag and projection area. It seems to represent a quadratic function, but I'm questioning if there's a need for a “half” factor in this context. The components like drag coefficient and area make sense, but I should double-check how they’re applied. I want to ensure I have the correct understanding of this formula.

**Analyzing flight trajectory**

I’m trying to figure out the trajectory for a flight, specifically with varying parameters. I need to solve an ordinary differential equation related to quadratic drag, which means considering factors like drag coefficient and mass. By calibrating and integrating manually for constant values, I’m looking to achieve precise results within specific tolerances. I’ll also need to balance launch angles and horizontal speed to maximize my chances of success while keeping errors controlled. Let's see how it goes!

**Calculating shot trajectory**

I'm analyzing the shot trajectory towards the hoop, aiming to decrease the horizontal velocity to ensure the center of the shot reaches the target later while maintaining the original vertical velocity. I'll investigate the rendered image of the trajectory, noting important coordinates, particularly where the ball seems to intersect with the backboard. I want to check if the trajectory is near vertical, as that might lead to hitting the backboard. Balancing these aspects is crucial for accuracy!

**Inspecting low-resolution image**

I need to closely examine the image described by the user. Since it’s low-resolution, I’ll have to mentally magnify the details to get a better understanding, even without any additional tools. It seems I’ll rely on my ability to visualize and interpret the details from that description to provide useful insights. Let’s see what I can gather from it and how I can help the user!

**Considering analytical quadrature**

I’m looking into analytical quadrature using the s velocities formula. I have to choose a descending slope of u = -2, where I’ve got vxcenter around 2.33 and vz at -4.66. It's quite a specific setup, but I'm curious about how these parameters will interact with one another. I'll keep these values in mind as I explore the implications in my calculations. Let's see where this leads!

**Calculating integrals**

I’m working on a calculation involving an integral. I'm calculating .5/6 multiplied by the sum of 22.764, 4 times 26.388, and 30.333. That leads me to .083333 multiplied by 158.649. After doing the math, I get a result of 13.2208. It's interesting to see how these figures come together, but I want to make sure I double-check everything to ensure accuracy!

**Calculating launch parameters**

I need to ensure the fluid coefficient k is quadratic without any strange added mass influences. The prediction matches the apex exactly, which is good. I can choose between 2.88 and 2.89 for qvel. The launch allows for clearance at the front rim, with the center positioned at x3.78. I’ll derive C for vx2.88 to adjust the center. All velocities are about 1.3% lower, and I'll look into Ix with the extension adjustments.