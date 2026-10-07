This is designed by hand and has not been run, so the energy and trajectory figures are estimates.

How the chain works:
- **Pendulum to cart:** the bob starts 0.6 m above its lowest point. It reaches the bottom at about 3.4 m/s and hits the cart there.
- **Cart to weight:** the cart slides and pushes the 1 kg weight completely off the shelf. The cart's joint range is set to make sure of this.
- **Weight to seesaw:** the weight strikes a stop wall and drops onto the raised left arm of the seesaw. This drives the seesaw onto its lower joint stop at q = 0.
- **Seesaw to ball:** the ball sits in a small cradle at the end of a bent arm. When the seesaw stops, the ball is thrown at about 50° elevation.
- **Ball to cup:** the cup is a wide box with a 1.5 m backboard. By hand calculation, launch speeds from about 1.2 m/s up to about 5 m/s land the ball inside the cup. Rolling friction on the ball (`condim="6"`) should bring it to rest.

```xml
<mujoco model="pendulum_cart_seesaw_cup">
  <compiler angle="radian"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="1 -2 4" dir="0 0.5 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- pendulum support (visual only) -->
    <geom name="pend_post" type="box" pos="0 0.15 1.1" size="0.02 0.02 1.1" contype="0" conaffinity="0" rgba="0.4 0.4 0.4 1"/>
    <geom name="pend_beam" type="box" pos="0 0.075 2.2" size="0.02 0.075 0.02" contype="0" conaffinity="0" rgba="0.4 0.4 0.4 1"/>

    <!-- shelf holding the weight -->
    <geom name="shelf" type="box" pos="0.39 0 1.275" size="0.14 0.12 0.025" friction="0.5 0.005 0.0001" rgba="0.6 0.45 0.3 1"/>
    <geom name="shelf_post" type="box" pos="0.30 0 0.625" size="0.02 0.02 0.625" contype="0" conaffinity="0" rgba="0.5 0.4 0.3 1"/>

    <!-- wall that stops the weight so it drops onto the seesaw -->
    <geom name="weight_stop" type="box" pos="0.785 0 1.21" size="0.025 0.15 0.39" rgba="0.5 0.5 0.6 1"/>

    <!-- seesaw pivot support (visual only) -->
    <geom name="seesaw_post" type="box" pos="1.0 0.13 0.275" size="0.02 0.02 0.275" contype="0" conaffinity="0" rgba="0.4 0.4 0.4 1"/>

    <body name="pendulum" pos="0 0 2.2">
      <joint name="pendulum_hinge" type="hinge" pos="0 0 0" axis="0 1 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.75" size="0.012" mass="0.05" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.8" size="0.05" mass="1.0" rgba="0.8 0.2 0.2 1"/>
    </body>

    <body name="cart" pos="0.13 0 1.4">
      <joint name="cart_slide" type="slide" axis="1 0 0" limited="true" range="0 0.34" solreflimit="0.005 1"/>
      <geom name="cart_box" type="box" size="0.08 0.06 0.06" mass="1.0" rgba="0.2 0.4 0.8 1"/>
    </body>

    <body name="weight" pos="0.5 0 1.36">
      <freejoint name="weight_free"/>
      <geom name="weight_box" type="box" size="0.06 0.06 0.06" mass="1.0" friction="0.5 0.005 0.0001" rgba="0.3 0.3 0.3 1"/>
    </body>

    <body name="seesaw" pos="1.0 0 0.55">
      <joint name="seesaw_hinge" type="hinge" pos="0 0 0" axis="0 1 0" limited="true" range="0 0.35" solreflimit="0.005 1"/>
      <geom name="seesaw_plank" type="box" pos="-0.325 0 0" size="0.325 0.08 0.01" mass="0.06" rgba="0.7 0.6 0.2 1"/>
      <geom name="seesaw_bump" type="box" pos="-0.04 0 0.035" size="0.02 0.08 0.025" mass="0.01" rgba="0.6 0.5 0.2 1"/>
      <geom name="seesaw_arm" type="box" pos="0.17236 0 -0.144627" size="0.225 0.05 0.01" euler="0 0.698132 0" mass="0.12" rgba="0.7 0.6 0.2 1"/>
      <geom name="seesaw_endwall" type="box" pos="0.362771 0 -0.252185" size="0.01 0.05 0.05" euler="0 0.698132 0" mass="0.02" rgba="0.6 0.5 0.2 1"/>
      <geom name="seesaw_rail_l" type="box" pos="0.29889 0.045 -0.211637" size="0.065 0.005 0.02" euler="0 0.698132 0" mass="0.01" rgba="0.6 0.5 0.2 1"/>
      <geom name="seesaw_rail_r" type="box" pos="0.29889 -0.045 -0.211637" size="0.065 0.005 0.02" euler="0 0.698132 0" mass="0.01" rgba="0.6 0.5 0.2 1"/>
      <geom name="seesaw_axle" type="cylinder" pos="0 0 0" size="0.015 0.1" euler="1.5708 0 0" mass="0.01" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
    </body>

    <body name="ball" pos="1.2351 0 0.2261">
      <freejoint name="ball_free"/>
      <geom name="ball_geom" type="sphere" size="0.03" mass="0.03" condim="6" friction="0.8 0.01 0.005" rgba="0.9 0.5 0.1 1"/>
    </body>

    <body name="cup" pos="1.75 0 0">
      <geom name="cup_floor" type="box" pos="0 0 0.01" size="0.27 0.22 0.01" rgba="0.2 0.6 0.3 1"/>
      <geom name="cup_front" type="box" pos="-0.26 0 0.09" size="0.01 0.22 0.09" rgba="0.2 0.6 0.3 1"/>
      <geom name="cup_back" type="box" pos="0.26 0 0.75" size="0.01 0.22 0.75" rgba="0.2 0.6 0.3 0.6"/>
      <geom name="cup_side_l" type="box" pos="0 0.21 0.10" size="0.25 0.01 0.08" rgba="0.2 0.6 0.3 1"/>
      <geom name="cup_side_r" type="box" pos="0 -0.21 0.10" size="0.25 0.01 0.08" rgba="0.2 0.6 0.3 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="1.3181 0 0.5 0 1.36 1 0 0 0 0.35 1.2351 0 0.2261 1 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

Setting up the cup geometry with floor, walls, and positioning for the scene layout...

Working out the keyframe initial positions for pendulum, cart, weight, seesaw, and ball, then defining the cart's slide joint, pendulum's hinge joint, the weight-stop wall, and seesaw geometry with its rail placements. Time to write the complete file now.

