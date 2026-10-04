```xml
<mujoco model="self_closing_door">
  <compiler angle="degree" inertiafromgeom="auto"/>
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast"/>

  <asset>
    <material name="floor_material" rgba="0.32 0.35 0.38 1"/>
    <material name="frame_material" rgba="0.72 0.74 0.77 1"/>
    <material name="door_material" rgba="0.48 0.25 0.11 1"/>
    <material name="metal_material" rgba="0.18 0.20 0.23 1"/>
  </asset>

  <worldbody>
    <light name="main_light" pos="0 -3 5" dir="0 0.5 -1"/>
    <camera name="overview" pos="3 -4 2.8" xyaxes="0.8 0.6 0 -0.27 0.36 0.89"/>

    <geom name="floor" type="plane" size="5 5 0.1" material="floor_material"/>

    <body name="frame" pos="0 0 0">
      <geom name="left_jamb" type="box" pos="-0.555 0 1.06" size="0.04 0.075 1.06" material="frame_material"/>
      <geom name="right_jamb" type="box" pos="0.50 0 1.06" size="0.04 0.075 1.06" material="frame_material"/>
      <geom name="header" type="box" pos="-0.0275 0 2.12" size="0.5675 0.075 0.04" material="frame_material"/>

      <!-- The leaf meets this stop at hinge angle zero. -->
      <geom name="closing_stop" type="box" pos="0.435 -0.0475 1.04" size="0.025 0.02 0.99" material="frame_material" friction="0.6 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001"/>

      <geom name="lower_hinge_barrel" type="cylinder" pos="-0.48 0 0.30" size="0.023 0.07" material="metal_material"/>
      <geom name="upper_hinge_barrel" type="cylinder" pos="-0.48 0 1.78" size="0.023 0.07" material="metal_material"/>
    </body>

    <body name="door" pos="-0.48 0 1.04">
      <!-- A preloaded torsion spring closes the door and holds it against the stop. -->
      <joint name="hinge" type="hinge" pos="0 0 0" axis="0 0 1" limited="true" range="0 100" stiffness="18" springref="-5" damping="12" armature="0.02" solreflimit="0.008 1" solimplimit="0.95 0.99 0.001"/>

      <geom name="door_leaf" type="box" pos="0.48 0 0" size="0.45 0.0275 1.0" mass="12" material="door_material" friction="0.6 0.005 0.0001" solref="0.008 1" solimp="0.95 0.99 0.001"/>
      <geom name="front_handle" type="capsule" fromto="0.83 -0.065 -0.08 0.83 -0.065 0.08" size="0.015" mass="0.12" material="metal_material"/>
      <geom name="rear_handle" type="capsule" fromto="0.83 0.065 -0.08 0.83 0.065 0.08" size="0.015" mass="0.12" material="metal_material"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="1.2217304764" qvel="0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

**Designing door mechanics**

I need to design a robust MJCF door that closes and stays shut. I want the hinge spring damping to allow for an initial open angle, with damped convergence taking about six seconds. The hinge range should go from 0 to 100 degrees. Additionally, it needs to visually satisfy by swinging shut and settling within about two seconds. I’ll explore a torque motor for controlled closure, ensuring no collision issues with the frame. The door dimensions need careful consideration too.

**Determining door and frame specifications**

I’m figuring out the frame columns at x=-0.525, considering potential contacts between the hinge panel when closed. The left post's inner face is at -0.49, while the right post is at .505, meaning I have a clearance of .045. I need exact dimensions for the doorway from hinge to the right side. I also want fixed rear stops to ensure a small gap when the door shuts, aiming for realistic physical interaction. Balancing the closer torque and damping is also essential.

**Calculating door dynamics**

I’m figuring out the mass of the door, which is 16 kg, and the hinge moment of inertia is 4.32 kgm². I have torque values of -5 or -8, and the damping is set at 7. The door will open to 75 degrees and should close in about 2.3 seconds. When it impacts the stop, the velocity will be -0.8 rad/s, but I need to ensure there's no restitution at contact; damping should hold everything in place.

**Finalizing scene materials**

I'm working with geometry using wood and frame, and setting the floor with rgba. I’m considering that the scene needs assets, and while no textures are allowed, materials can be used. I'm trying to keep things simple, so there’s no need to overcomplicate. The final output should be a complete file without any claims for testing. Let's make sure everything is in order for a smooth finish!