A spring-loaded hinge swings the door closed against a fixed stop, then keeps it pressed shut.

```xml
<mujoco model="self_closing_door">
  <compiler angle="radian" autolimits="true"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast"/>

  <visual>
    <headlight ambient="0.35 0.35 0.35" diffuse="0.7 0.7 0.7" specular="0.2 0.2 0.2"/>
  </visual>

  <worldbody>
    <light name="overhead_light" pos="0 -2 4" dir="0 0.4 -1"/>
    <camera name="overview" pos="3 -4 3" xyaxes="0.8 0.6 0 -0.3 0.4 0.866"/>

    <geom name="floor" type="plane" pos="0 0 0" size="4 4 0.1" rgba="0.65 0.67 0.69 1" friction="0.8 0.005 0.0001"/>

    <body name="frame" pos="0 0 0">
      <geom name="hinge_jamb" type="box" pos="-0.075 0 1.1" size="0.05 0.09 1.1" rgba="0.34 0.23 0.14 1"/>
      <geom name="latch_jamb" type="box" pos="1.075 0 1.1" size="0.05 0.09 1.1" rgba="0.34 0.23 0.14 1"/>
      <geom name="header" type="box" pos="0.5 0 2.17" size="0.625 0.09 0.05" rgba="0.34 0.23 0.14 1"/>
      <geom name="closing_stop" type="box" pos="0.96 -0.065 1.1" size="0.045 0.03 0.95" rgba="0.26 0.18 0.11 1" friction="0.8 0.005 0.0001" solref="0.01 1" solimp="0.99 0.99 0.001"/>
      <geom name="hinge_pin" type="cylinder" pos="0 0 1.1" size="0.018 1" rgba="0.3 0.3 0.32 1" contype="0" conaffinity="0"/>
    </body>

    <body name="door" pos="0 0 0.1">
      <joint name="hinge" type="hinge" pos="0 0 0" axis="0 0 1" limited="true" range="0 1.6" stiffness="40" springref="-0.08" damping="24" armature="0.02" solreflimit="0.01 1" solimplimit="0.99 0.99 0.001"/>
      <geom name="door_panel" type="box" pos="0.5 0 1" size="0.5 0.035 1" mass="12" rgba="0.18 0.36 0.55 1" friction="0.8 0.005 0.0001" solref="0.01 1" solimp="0.99 0.99 0.001"/>
      <geom name="door_handle" type="box" pos="0.83 0.065 1.05" size="0.08 0.03 0.015" mass="0.1" rgba="0.75 0.75 0.78 1" contype="0" conaffinity="0"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="1.3" qvel="0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Designing door dynamics**

I'm thinking about designing a door that smoothly swings shut and stays closed for about 6 seconds. I'll use hinge spring damping and contact stops with an optional latch. I must provide complete XML names, including all bodies and geometries, while avoiding defaults. It’s essential to check everything honestly since I won't be using any tools for testing. The door's mass and dimensions will also play a big part, and I suspect I'll end up needing some specific parameters for spring stiffness and damping.

**Evaluating door mechanics**

I’m figuring out the equilibrium for the door design, noticing it slightly negative at around - preload, which is very small. The geometry needs to make sure the frame and shutter contact stabilize. For the actuator position, I’ll use a control factor and a negative spring reference. I need to carefully position the door and ensure it swings and stays shut properly while avoiding collisions with the frame edges. The latch and stopping mechanics also require precise placement to function correctly without touching anything when fully open.

**Clarifying mass specifications**

I'm thinking about specifying inertial mass, particularly focusing on the full inertia of the door slab. It seems like the handle will have a mass of around 0.08, and the door panel's mass will be about 0.1. I’m also considering the mass of the hinge—should it be factorized in? My initial calculation seems to start with q1.25, but I won’t include any velocity for now. It's all a bit technical!