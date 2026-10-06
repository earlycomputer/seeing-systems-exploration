```xml
<mujoco model="drop_weight_seesaw">
  <compiler angle="degree" inertiafromgeom="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicit" solver="Newton" cone="elliptic" iterations="100" tolerance="1e-10"/>

  <visual>
    <global azimuth="135" elevation="-20"/>
  </visual>

  <worldbody>
    <light name="overhead" pos="0 -2 5" dir="0 0 -1"/>
    <camera name="overview" pos="3 -6 3" xyaxes="0.894427 0.447214 0 -0.182574 0.365148 0.912871"/>

    <geom name="floor" type="plane" pos="0 0 0" size="5 5 0.1" rgba="0.75 0.78 0.80 1" friction="0.8 0.005 0.0001" solref="0.004 1" solimp="0.99 0.999 0.001"/>

    <body name="pedestal" pos="0 0 0">
      <geom name="pedestal_base" type="box" pos="0 0 0.04" size="0.25 0.25 0.04" rgba="0.25 0.28 0.32 1"/>
      <geom name="pedestal_column" type="box" pos="0 0 0.23" size="0.09 0.19 0.15" rgba="0.35 0.38 0.42 1"/>
      <geom name="pivot_axle" type="cylinder" pos="0 0 0.45" quat="0.7071067812 0.7071067812 0 0" size="0.035 0.18" contype="0" conaffinity="0" rgba="0.15 0.17 0.20 1"/>
    </body>

    <!-- The upper hinge stop supports the resting ball before impact.
         Negative hinge rotation lowers the weight end and raises the ball end. -->
    <body name="seesaw" pos="0 0 0.45">
      <joint name="seesaw_hinge" type="hinge" axis="0 1 0" limited="true" range="-22 0" damping="0.005" solreflimit="0.004 1" solimplimit="0.99 0.999 0.001"/>
      <geom name="seesaw_plank" type="box" size="1 0.13 0.025" mass="0.25" rgba="0.12 0.40 0.70 1" friction="0.8 0.005 0.0001" solref="0.004 1" solimp="0.99 0.999 0.001"/>
    </body>

    <body name="weight" pos="-0.85 0 3">
      <freejoint name="weight_free"/>
      <geom name="weight_sphere" type="sphere" size="0.1" mass="1" rgba="0.25 0.27 0.30 1" friction="0.8 0.005 0.0001" solref="0.004 1" solimp="0.99 0.999 0.001"/>
    </body>

    <body name="ball" pos="0.85 0 0.525">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.05" mass="0.1" rgba="1 0.35 0.05 1" friction="0.8 0.005 0.0001" solref="0.004 1" solimp="0.99 0.999 0.001"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 -0.85 0 3 1 0 0 0 0.85 0 0.525 1 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Considering integrators and solvers**

I'm looking into using the cone elliptic solver with Newton's method, which seems to be an accepted option. The modern implicitfast integrator is the safest choice, and it typically supports certain functionalities. I can set options like `integrator="implicit"` for long-term support. 

I’ll also be mindful of the gravity effects, especially with ballistic weights after impact; bounces and launches need to be carefully coded. Time to provide that code!