The ball starts on the floor 4 m from the rim and is launched at about 3.01 m/s forward and 8.73 m/s up. Its arc peaks near 4.0 m and comes down through the rim center at about 55° below horizontal, so it should clear the 0.45 m rim on both sides. After the rim it passes under the backboard and lands near x ≈ 5.35 m.

```xml
<mujoco model="basketball_shot">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="2 -3 8" dir="0 0.3 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="10 10 0.1" rgba="0.75 0.6 0.4 1"/>

    <body name="ball" pos="0 0 0.121">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.12" mass="0.62" rgba="0.9 0.45 0.1 1" solref="0.01 0.3"/>
    </body>

    <body name="hoop" pos="4 0 3.05">
      <geom name="rim_00" type="capsule" size="0.008" fromto="0.237 0 0 0.2190 0.0907 0" rgba="1 0.3 0 1"/>
      <geom name="rim_01" type="capsule" size="0.008" fromto="0.2190 0.0907 0 0.1676 0.1676 0" rgba="1 0.3 0 1"/>
      <geom name="rim_02" type="capsule" size="0.008" fromto="0.1676 0.1676 0 0.0907 0.2190 0" rgba="1 0.3 0 1"/>
      <geom name="rim_03" type="capsule" size="0.008" fromto="0.0907 0.2190 0 0 0.237 0" rgba="1 0.3 0 1"/>
      <geom name="rim_04" type="capsule" size="0.008" fromto="0 0.237 0 -0.0907 0.2190 0" rgba="1 0.3 0 1"/>
      <geom name="rim_05" type="capsule" size="0.008" fromto="-0.0907 0.2190 0 -0.1676 0.1676 0" rgba="1 0.3 0 1"/>
      <geom name="rim_06" type="capsule" size="0.008" fromto="-0.1676 0.1676 0 -0.2190 0.0907 0" rgba="1 0.3 0 1"/>
      <geom name="rim_07" type="capsule" size="0.008" fromto="-0.2190 0.0907 0 -0.237 0 0" rgba="1 0.3 0 1"/>
      <geom name="rim_08" type="capsule" size="0.008" fromto="-0.237 0 0 -0.2190 -0.0907 0" rgba="1 0.3 0 1"/>
      <geom name="rim_09" type="capsule" size="0.008" fromto="-0.2190 -0.0907 0 -0.1676 -0.1676 0" rgba="1 0.3 0 1"/>
      <geom name="rim_10" type="capsule" size="0.008" fromto="-0.1676 -0.1676 0 -0.0907 -0.2190 0" rgba="1 0.3 0 1"/>
      <geom name="rim_11" type="capsule" size="0.008" fromto="-0.0907 -0.2190 0 0 -0.237 0" rgba="1 0.3 0 1"/>
      <geom name="rim_12" type="capsule" size="0.008" fromto="0 -0.237 0 0.0907 -0.2190 0" rgba="1 0.3 0 1"/>
      <geom name="rim_13" type="capsule" size="0.008" fromto="0.0907 -0.2190 0 0.1676 -0.1676 0" rgba="1 0.3 0 1"/>
      <geom name="rim_14" type="capsule" size="0.008" fromto="0.1676 -0.1676 0 0.2190 -0.0907 0" rgba="1 0.3 0 1"/>
      <geom name="rim_15" type="capsule" size="0.008" fromto="0.2190 -0.0907 0 0.237 0 0" rgba="1 0.3 0 1"/>
      <geom name="rim_bracket" type="box" size="0.07 0.06 0.01" pos="0.31 0 -0.01" rgba="1 0.3 0 1"/>
    </body>

    <body name="backboard" pos="4.395 0 3.435">
      <geom name="backboard" type="box" size="0.015 0.915 0.535" rgba="0.95 0.95 1 0.6"/>
    </body>

    <body name="support" pos="5.8 0 0">
      <geom name="pole" type="cylinder" size="0.1 1.75" pos="0 0 1.75" rgba="0.3 0.3 0.35 1"/>
      <geom name="arm" type="box" size="0.7 0.06 0.06" pos="-0.69 0 3.45" rgba="0.3 0.3 0.35 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 0 0.121 1 0 0 0" qvel="3.0087 0 8.725 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
ball drops through hoop
ball touches floor
```

---
thinking (summarized):

I'm working out the physical parameters for the trajectory: a regulation basketball with radius around 0.12 m and mass 0.62 kg, a rim of inner radius 0.225 m positioned at height 3.05 m and 4 m horizontally from the launch point, setting up the ball's starting position on the floor before launch.

I'm computing the launch kinematics by picking an apex height above the rim and solving for vertical and horizontal velocities using basic projectile equations, checking that the resulting ~55° descent angle gives enough clearance through the rim opening relative to the ball's diameter. I'm also considering integration details in MuJoCo, like the small timestep error from semi-implicit Euler and the fact that air drag is negligible with default zero air density, then moving to model the rim itself as a torus approximated by a ring of capsules with a thin tube radius and the correct inner radius.

Computing capsule endpoint coordinates around the ring...

Now I'm positioning the backboard relative to the rim, placing it at the appropriate plane with correct height and dimensions, then working through the ball's trajectory after passing the rim to see where it would hit the backboard.

I'm also deciding whether to add a support pole around x=5.6 for realism, and computing roughly where the ball would land on the floor after falling from rim height.

I'll leave bounce physics at default since floor contact doesn't matter here. Checking whether the ball clips the front rim tube, I'm computing the perpendicular distance from the ball's trajectory line to the rim front point, getting about 0.194, which needs to exceed the rim tube radius for clearance.

Setting the initial velocity vector at roughly (3.0087, 0, 8.725) with the ball starting just touching the floor, I note the semi-implicit Euler integration will cause a tiny downward offset (about 1.3cm) in actual trajectory versus continuous-time math, which is negligible. The ball's mass and inertia look fine for this setup.

Hollow shell inertia doesn't matter much here, so I'll skip that detail and just write the file, making sure it satisfies the ball dropping through the hoop and touching the floor.

