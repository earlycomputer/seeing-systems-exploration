Gravity powers the launch. The upper hinge stop holds the seesaw level until impact; the lower stop abruptly halts the seesaw, letting the light ball continue upward.

```xml
<mujoco model="gravity_seesaw_launcher">
  <compiler angle="degree" autolimits="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" iterations="100" tolerance="1e-10"/>

  <worldbody>
    <light name="overhead_light" pos="0 -2 4" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.35 0.38 0.42 1" friction="0.8 0.005 0.0001" solref="0.004 1" solimp="0.95 0.99 0.001"/>

    <body name="fulcrum" pos="0 0 0.215">
      <geom name="fulcrum_support" type="box" size="0.045 0.12 0.215" rgba="0.25 0.28 0.32 1" contype="0" conaffinity="0"/>
      <geom name="fulcrum_axle" type="cylinder" pos="0 0 0.235" euler="90 0 0" size="0.035 0.14" rgba="0.6 0.62 0.65 1" contype="0" conaffinity="0"/>
    </body>

    <body name="seesaw" pos="0 0 0.45">
      <joint name="seesaw_hinge" type="hinge" axis="0 1 0" range="-28 0" damping="0.015" solreflimit="0.004 1" solimplimit="0.99 0.999 0.001"/>
      <geom name="seesaw_deck" type="box" size="0.8 0.11 0.015" mass="0.2" rgba="0.75 0.48 0.18 1" friction="0.7 0.005 0.0001" solref="0.004 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="weight" pos="-0.62 0 1.60">
      <freejoint name="weight_free"/>
      <geom name="weight_sphere" type="sphere" size="0.09" mass="1" rgba="0.25 0.3 0.8 1" friction="0.7 0.005 0.0001" solref="0.004 1" solimp="0.95 0.99 0.001"/>
    </body>

    <body name="ball" pos="0.62 0 0.52">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.055" mass="0.1" rgba="0.9 0.18 0.12 1" friction="0.7 0.005 0.0001" solref="0.004 1" solimp="0.95 0.99 0.001"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 -0.62 0 1.60 1 0 0 0 0.62 0 0.52 1 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
weight touches seesaw
ball touches seesaw
seesaw reaches its lower stop
```

---
thinking (summarized):

**Analyzing ball movement on an inclined board**

As the angle progresses, I’m considering the acceleration in relation to centripetal forces—a mix of downward acceleration and radial components, but not normal. The angular acceleration seems to decelerate due to weight. A heavy weight on the left causes a negative gravitational torque, resulting in upward acceleration for the ball. I expect it might slide or roll toward the pivot on the inclined board and centrifugal force could push it outward. It may help to add walls for guidance.

**Examining weighs impacts on a seesaw**

I'm considering the way a weight on a seesaw plank creates a downward rotation after the collision. When a small ball contacts at x = -0.6, it sets the plank level. If the weight is large, it imposes a negative torque. The weight might exert a horizontal impulse due to tilt. If the configuration reaches q = -0.49, the left plate may rise outward, but I lack the ability to simulate the effects. I need to ensure my expectations are realistic, like expecting the ball to rise at least 0.5 when touching the seesaw.

**Understanding motion dynamics**

I’m examining how a ball interacts with a seesaw and its surroundings. When the ball touches the floor, it may slide left, eventually resting on either the board or the floor. There's an interesting interplay between weight on the seesaw, which reaches a lower stop. The damping and friction loss affect its behavior considerably. The weight rolls left, potentially falling off before it truly stops. The dynamics become fascinating as the weight leaves the beam, and the ball becomes airborne, influenced by gravity and inertia.

**Considering support structures**

I'm thinking about creating a pivot for support, possibly named support_geom or support body. I need to add a static pedestal with a vertical cylinder to stabilize it. The cylinder's dimensions would be critical, as it intersects the beam pivot area at the plank center, which could limit the seesaw's rotation. Setting the right configurations for contact type and affinity is essential for structural integrity. I might also want to consider a box geometry for the fulcrum, ensuring it fits correctly without interfering with other components. Users likely don't need decorative cylinders, so I'll keep it functional.

**Creating support structures**

I’m adding a pedestal body named fulcrum with specific dimensions for support, ensuring non-collision properties. The axle will be a static cylinder positioned accurately and configured for correct contact type and affinity. It’s essential to keep in mind the model's inertia, especially if the arm is too light. I need to set the proper mass for both the axle and the arm to ensure stability. The arm's size and mass are critical for the overall balance and function of the system.