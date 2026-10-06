The first domino starts leaning forward with a small tipping velocity; gravity and contact drive the rest of the chain.

```xml
<mujoco model="ten_domino_chain">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast" solver="Newton" iterations="100"/>
  <size nconmax="200" njmax="1000"/>

  <worldbody>
    <light name="overhead_light" pos="0.5 -1 3" dir="0 0 -1"/>
    <camera name="overview" pos="0.54 -2.2 1.3" xyaxes="1 0 0 0 0.5 0.8660254"/>
    <geom name="floor" type="plane" pos="0 0 0" size="3 2 0.1" friction="0.9 0.005 0.0001" solref="0.006 1" solimp="0.95 0.99 0.001" rgba="0.3 0.33 0.36 1"/>

    <body name="domino1" pos="0 0 0.147794296" quat="0.984807753 0 0.173648178 0">
      <freejoint/>
      <geom name="domino1_geom" type="box" size="0.02 0.06 0.15" mass="0.25" friction="0.9 0.005 0.0001" solref="0.006 1" solimp="0.95 0.99 0.001" rgba="0.9 0.25 0.15 1"/>
    </body>

    <body name="domino2" pos="0.12 0 0.15">
      <freejoint/>
      <geom name="domino2_geom" type="box" size="0.02 0.06 0.15" mass="0.25" friction="0.9 0.005 0.0001" solref="0.006 1" solimp="0.95 0.99 0.001" rgba="0.95 0.45 0.15 1"/>
    </body>

    <body name="domino3" pos="0.24 0 0.15">
      <freejoint/>
      <geom name="domino3_geom" type="box" size="0.02 0.06 0.15" mass="0.25" friction="0.9 0.005 0.0001" solref="0.006 1" solimp="0.95 0.99 0.001" rgba="0.95 0.65 0.15 1"/>
    </body>

    <body name="domino4" pos="0.36 0 0.15">
      <freejoint/>
      <geom name="domino4_geom" type="box" size="0.02 0.06 0.15" mass="0.25" friction="0.9 0.005 0.0001" solref="0.006 1" solimp="0.95 0.99 0.001" rgba="0.75 0.8 0.2 1"/>
    </body>

    <body name="domino5" pos="0.48 0 0.15">
      <freejoint/>
      <geom name="domino5_geom" type="box" size="0.02 0.06 0.15" mass="0.25" friction="0.9 0.005 0.0001" solref="0.006 1" solimp="0.95 0.99 0.001" rgba="0.3 0.75 0.35 1"/>
    </body>

    <body name="domino6" pos="0.60 0 0.15">
      <freejoint/>
      <geom name="domino6_geom" type="box" size="0.02 0.06 0.15" mass="0.25" friction="0.9 0.005 0.0001" solref="0.006 1" solimp="0.95 0.99 0.001" rgba="0.2 0.75 0.65 1"/>
    </body>

    <body name="domino7" pos="0.72 0 0.15">
      <freejoint/>
      <geom name="domino7_geom" type="box" size="0.02 0.06 0.15" mass="0.25" friction="0.9 0.005 0.0001" solref="0.006 1" solimp="0.95 0.99 0.001" rgba="0.2 0.6 0.9 1"/>
    </body>

    <body name="domino8" pos="0.84 0 0.15">
      <freejoint/>
      <geom name="domino8_geom" type="box" size="0.02 0.06 0.15" mass="0.25" friction="0.9 0.005 0.0001" solref="0.006 1" solimp="0.95 0.99 0.001" rgba="0.3 0.4 0.9 1"/>
    </body>

    <body name="domino9" pos="0.96 0 0.15">
      <freejoint/>
      <geom name="domino9_geom" type="box" size="0.02 0.06 0.15" mass="0.25" friction="0.9 0.005 0.0001" solref="0.006 1" solimp="0.95 0.99 0.001" rgba="0.6 0.35 0.85 1"/>
    </body>

    <body name="domino10" pos="1.08 0 0.15">
      <freejoint/>
      <geom name="domino10_geom" type="box" size="0.02 0.06 0.15" mass="0.25" friction="0.9 0.005 0.0001" solref="0.006 1" solimp="0.95 0.99 0.001" rgba="0.85 0.3 0.65 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qvel="0.295588592 0 -0.065018338 0 2 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
domino1 touches domino2
domino2 touches domino3
domino3 touches domino4
domino4 touches domino5
domino5 touches domino6
domino6 touches domino7
domino7 touches domino8
domino8 touches domino9
domino9 touches domino10
domino1 ends tilted at least 15 degrees from upright
domino2 ends tilted at least 15 degrees from upright
domino3 ends tilted at least 15 degrees from upright
domino4 ends tilted at least 15 degrees from upright
domino5 ends tilted at least 15 degrees from upright
domino6 ends tilted at least 15 degrees from upright
domino7 ends tilted at least 15 degrees from upright
domino8 ends tilted at least 15 degrees from upright
domino9 ends tilted at least 15 degrees from upright
domino10 ends tilted at least 15 degrees from upright
```

---
thinking (summarized):

**Designing a domino chain**

I need to create a reliable domino chain with ten free bodies, using XML for naming conventions like "domino1... tilted." I'll check everything honestly without specific tools, reasoning through the physical aspects instead. It seems I need to ensure the spacing and velocities are robust, starting with a first domino tilted at 15° and adjusting its position accordingly. Domino dimensions will be around .2 in height, .03 in thickness, and .10 in width, with appropriate spacing between them.

**Calculating pivot angles and positions**

I'm working on setting the first body's quaternion angle, starting with 12/20 for the z-coordinate. I’ll calculate positions based on angles, particularly focusing on the lower supports and their shift in relation to the x-axis. It seems I need to ensure that the initial positions of the pivots are consistent and take into account angular velocities. If I adjust the positions properly, it could lead to a successful launch, but I need to verify everything according to gravity and pivot mechanisms.

**Evaluating stability at tilt angles**

I'm considering whether I can rely on the first domino being tipped at 20° for stability, given that gravity will play a significant role. I need to check if the center of mass right of the pivot creates a stable situation. If the angle exceeds the arctangent of the ratio of dimensions, around 7.125°, it might cause an automatic fall. I’ll need to ensure that I account for torque and gravitational forces properly to maintain stability.