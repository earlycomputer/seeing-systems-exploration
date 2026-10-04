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
    <key name="shot" qvel="3.1424 0 9.4272 0 0 0"/>
    <!-- Increased +x launch velocity from 2.9532 to 3.1424 m/s and +z from 8.556 to 9.4272 m/s to compensate for air drag and target the rim center on descent; the starting position is unchanged. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Figuring out air dynamics**

I need to solve for accurate air dynamics related to the hoop, but I don't have any tools right now. I'm planning to derive the drag for MuJoCo and then numerically optimize it by carefully considering clearance and trajectory angle. I might calculate it by numerical integration, but there's some uncertainty involved. I'm realizing I need the correct force formulas and to recall the implementation details from GitHub. I'll need to look into the exact equations for ellipsoid drag.

**Recalling MuJoCo formulas**

I'm revisiting the MuJoCo documentation about drag calculations. I remember that blunt drag is proportional to the square of the linear velocity and acts opposite to that velocity. Slender drag refers to resistance parallel to the ellipsoid's surface. There's a combined drag coefficient that seems to remain constant at .25, regardless of the cross-sectional area. I can also recall the fluid damping code from previous tasks and there's some memory about ellipsoid drag formulas, which define projected areas based on the ellipsoid's dimensions.

**Clarifying slender drag**

I'm looking at the formula for slender drag, which is expressed as -ρ C_slender (Amax - Aproj)||v|| v. I notice for a sphere, the difference is negligible, so the constant k is .02167, which seems reasonable to me. However, I realize I need to confirm if the slender term scales based on the total surface area minus the projected area, rather than maximum differences. I definitely need to check this for accuracy.

**Analyzing drag coefficient options**

I'm looking at the default value for the "blunt drag coeff," which is .5, and I wonder if the supplied coeff of .25 might effectively reflect that in physical terms, like with basketball. If the coefficient factor is uncertain, I could explore trajectories where drag impact is small. I should ensure robustness for the drag coefficient variation, ideally within [0.0108, .0433]. Ultimately, there’s a risk in manipulating the collision with backboard for range uncertainties.

**Calculating ratios and parameters**

I’m determining specific values for p_end and p0 in relation to ratios of integrals. For k equals 0, I find the average of p0 and p_end, which leads me to p0 being about 3.2153. I think I need to adjust p0 upwards, maybe around 3.0, to positively impact mean p. Then I can derive vx from x4. It's a bit complex, but I'm working through it!

**Evaluating launch parameters and fluid dynamics**

I’m considering using a safer launch steepness, maybe adjusting p_end to -1.745 for ball geometric clearance. At rim center, I have a velocity angle of -60.2 degrees and tweaking my opening apothem gives a margin of .0865. I wonder if the modeled air mass and fluid dynamics could impact vertical acceleration? After reviewing the MuJoCo documentation, it mentions added mass and drag effects, which might modify effective mass but won't change the mass matrix directly. I need to check the drag for a sphere next.

**Clarifying projected area formulas**

I’m exploring whether the formula for blunt area, like `Aproj = π(ry² rz² vx² + ...) / sqrt((ry rz vx)² + ...)`, holds up. For a sphere, it simplifies to πr², which is great. I’m considering if the slender drag area includes `Aproj` and if skin drag could be represented as `π(ry² + rz²)` in an independent direction. 

I'm also thinking about how blunt and slender drag applies to ellipsoids versus spheres and how they might relate as isotropic forces. I’ll need to find the MuJoCo ellipsoid drag calculations next.

**Calculating values and derivatives**

I'm working with the calculation s = 0.0022091187 / 0.126243824, which gives me s = 0.017498822. Now I want to double-check my work by calculating derivatives to make sure that s = 0.017498822 isn’t causing any greater issues. I need to ensure that my maximum errors are within 0.0005. It's always good to verify calculations to avoid potential mistakes!

**Clarifying changes in measurements**

I think it's important to comment precisely about the increase in values, like stating, "Increased from 2.9532 to 3.1424 and from 8.556 to 9.4272 m/s to account for drag and the center descending rim passage, while the rest-state position remains unchanged." This helps clarify the reasoning behind the adjustments. I'm also considering if the physics model is robust enough for these measurements, and for now, it seems like it is!