```xml
<mujoco model="gravity_seesaw_launcher">
  <compiler angle="degree" inertiafromgeom="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="80" cone="elliptic"/>
  <size njmax="200" nconmax="100"/>

  <visual>
    <global azimuth="135" elevation="-20"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="0 -3 5" dir="0 0.5 -1" directional="true"/>

    <geom name="floor" type="plane" pos="0 0 0" size="10 10 0.1" condim="6" friction="0.9 0.03 0.01" solref="0.004 1" solimp="0.99 0.999 0.001" rgba="0.75 0.78 0.82 1"/>

    <geom name="pedestal" type="box" pos="0 0 0.20" size="0.07 0.18 0.20" contype="0" conaffinity="0" rgba="0.25 0.28 0.32 1"/>
    <geom name="pivot_axle" type="cylinder" pos="0 0 0.45" quat="0.70710678 0.70710678 0 0" size="0.035 0.19" contype="0" conaffinity="0" rgba="0.18 0.20 0.23 1"/>

    <body name="seesaw" pos="0 0 0.45">
      <joint name="seesaw_hinge" type="hinge" axis="0 1 0" limited="true" range="-18 0" damping="0.015" armature="0.001" solreflimit="0.004 1" solimplimit="0.99 0.999 0.001"/>
      <geom name="seesaw_plank" type="box" size="1 0.14 0.025" mass="0.18" condim="6" friction="0.9 0.03 0.01" solref="0.004 1" solimp="0.99 0.999 0.001" rgba="0.72 0.45 0.20 1"/>
    </body>

    <body name="weight" pos="-0.8 0 2.5">
      <freejoint name="weight_free"/>
      <geom name="weight_sphere" type="sphere" size="0.09" mass="1" condim="6" friction="0.9 0.03 0.01" solref="0.004 1" solimp="0.99 0.999 0.001" rgba="0.22 0.28 0.36 1"/>
    </body>

    <body name="ball" pos="0.8 0 0.525">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.05" mass="0.1" condim="6" friction="0.9 0.03 0.01" solref="0.004 1" solimp="0.99 0.999 0.001" rgba="0.95 0.25 0.12 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 -0.8 0 2.5 1 0 0 0 0.8 0 0.525 1 0 0 0" qvel="0 0 0 0 0 0 0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Exploring reaction forces**

I'm considering how reaction separation occurs, especially when it comes to impact impulses versus gravity. For instance, when a seesaw hits something, it’s similar to how light pushes; both showcase contact forces acting quickly for a brief moment, leading to similar velocities. I wonder about the dynamics at play here and how these forces interact in different situations. It’s intriguing to think about the physics behind it!

**Evaluating cylinder support orientation**

I'm considering the static orientation of the cylinder, which defaults to having its vertical axis aligned with the z-axis. The cylinder's position is set to (0, 0, 0.22) with a size of (0.07, 0.22) and a height of 0.44. The pivot is at 0.45, creating a seesaw effect. It looks like the support collides initially with the plank at the top edge of 0.44 versus the bottom of 0.425, leading to an overlap of 0.015.

**Evaluating rolling friction and torque**

I'm thinking about whether rolling high-friction spheres on a beam could torque constraints. The rolling friction torque is bounded by the normal force, which could lead to very large moments. Yet, there's potential for absorbing angular momentum through effective rolling, possibly adding inertia to the ball. After considering various components including inertia and friction coefficients, I should confirm that all parts are working fine. It seems that understanding these mechanics is crucial for a successful setup.

**Analyzing the ball's movement**

I'm noting that the ball hits the floor after 1.9 seconds, which is when it makes contact. I'll also consider that it takes about 6 seconds to settle completely. This suggests that the movement involves initial dynamics followed by a period of rest. It’s fascinating to think about how gravity and motion play a role in this process! There’s a lot happening in those seconds, and I should consider the implications for any further analysis.