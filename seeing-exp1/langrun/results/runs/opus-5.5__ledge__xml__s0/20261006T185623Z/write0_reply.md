The table top is at 0.75 m with its edge at x = 0. The bucket is centred at x = 0.6 m, has an inner radius of 15 cm and walls 25 cm high. The ball starts rolling (spin matched to speed, so no sliding) at 1.6 m/s.

These numbers are hand calculations, not simulation results:
- **Rim clearance:** when the ball's lower edge falls to rim height, its centre is at about x ≈ 0.51 m. That is already about 6 cm inside the near wall's inner face at x = 0.45 m.
- **Landing point:** the ball reaches the bucket floor at about x ≈ 0.62 m, about 13 cm short of the far wall.

```xml
<mujoco model="ball_table_bucket">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="table" pos="0 0 0">
      <geom name="table_top" type="box" pos="-0.4 0 0.73" size="0.4 0.3 0.02" rgba="0.6 0.4 0.2 1"/>
      <geom name="table_leg1" type="box" pos="-0.05 0.25 0.355" size="0.02 0.02 0.355" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg2" type="box" pos="-0.05 -0.25 0.355" size="0.02 0.02 0.355" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg3" type="box" pos="-0.75 0.25 0.355" size="0.02 0.02 0.355" rgba="0.5 0.3 0.15 1"/>
      <geom name="table_leg4" type="box" pos="-0.75 -0.25 0.355" size="0.02 0.02 0.355" rgba="0.5 0.3 0.15 1"/>
    </body>

    <body name="bucket" pos="0.6 0 0">
      <geom name="bucket_bottom" type="cylinder" pos="0 0 0.005" size="0.17 0.005" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall0" type="box" pos="0.155 0 0.135" euler="0 0 0" size="0.005 0.068 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall1" type="box" pos="0.1096 0.1096 0.135" euler="0 0 45" size="0.005 0.068 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall2" type="box" pos="0 0.155 0.135" euler="0 0 90" size="0.005 0.068 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall3" type="box" pos="-0.1096 0.1096 0.135" euler="0 0 135" size="0.005 0.068 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall4" type="box" pos="-0.155 0 0.135" euler="0 0 180" size="0.005 0.068 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall5" type="box" pos="-0.1096 -0.1096 0.135" euler="0 0 225" size="0.005 0.068 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall6" type="box" pos="0 -0.155 0.135" euler="0 0 270" size="0.005 0.068 0.125" rgba="0.2 0.4 0.8 1"/>
      <geom name="bucket_wall7" type="box" pos="0.1096 -0.1096 0.135" euler="0 0 315" size="0.005 0.068 0.125" rgba="0.2 0.4 0.8 1"/>
    </body>

    <body name="ball" pos="-0.5 0 0.78">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" mass="0.1" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-0.5 0 0.78 1 0 0 0" qvel="1.6 0 0 0 53.333 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out the physics so the ball's trajectory off the table edge actually lands inside the bucket—setting a table height, edge position, bucket placement, and ensuring the ball clears the near wall before falling in.

I confirm the angular velocity relation for rolling contact, then check the edge transition: with v²/(g·r) way above 1, the ball leaves the edge almost immediately rather than pivoting around it, so the trajectory stays simple. I'll start the ball at x=-0.5 on the table so it has 0.5 m of free rolling before reaching the edge.

Positioning the table and legs so they stay clear of the ball's path, then setting up a static bucket body at (0.6,0,0), building its base and walls from cylinder and box geoms to approximate a circular container.

Checking the trajectory against the rim: when the ball's bottom edge reaches the rim height, its center is still about 1.6 cm clear of the wall's inner face, so it should pass over without clipping, though it's tight enough that I might want to bump the speed slightly to land more centered.

I'll keep bucket walls at 0.25 height, since default restitution settings should contain the ball fine once it lands. With no rolling friction the ball stays at constant speed, so it spends about 0.31s crossing the table. Now I'm computing the octagon wall positions and orientations, placing each box wall at its angle around the ring with corresponding rotation.

Checking the corner gaps between adjacent walls, I find the half-width of 0.066 leaves a slight overlap on the inner edge but nearly zero gap outward, so I'll bump it up to 0.068 to ensure the 6cm ball can't slip through. The bottom will be a cylinder with radius 0.17 to fully cover the octagon's footprint.

Now I'm setting up the keyframe: the ball starts at position (-0.5, 0, 0.78) with identity orientation, and its linear velocity is 1.6 m/s in x with angular velocity 53.33 rad/s in y (computed as v/r for the 3cm radius ball, since MuJoCo's free joint angular velocity is in the local frame which matches global here). I'm finalizing the ball's mass and friction defaults, adding the floor plane and lighting, and checking the ball's starting height clears the setup properly.

I'm adding the four table legs as thin boxes positioned at the corners, and the tabletop as a flat box, then verifying the ball's trajectory doesn't clip the bucket wall before settling with a small bounce. This all looks good, so I'll write out the final model.

