The door starts 1.4 rad open. A hinge spring with damping pulls it toward a jamb on the world frame, and the door makes contact with the jamb at `hinge` = 0. The spring's rest angle is slightly past the jamb (-0.15 rad), so it keeps pressing the door against the stop and the door stays shut after it settles.

```xml
<mujoco model="self_closing_door">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="1 -2 4" dir="-0.2 0.4 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.6 0.6 0.6 1"/>
    <body name="frame" pos="0 0 0">
      <geom name="hinge_post" type="cylinder" pos="-0.03 0 1.05" size="0.02 1.05" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>
      <geom name="jamb_stop" type="box" pos="0.85 -0.04 1.0" size="0.03 0.02 0.95" rgba="0.4 0.25 0.1 1"/>
      <geom name="jamb_post" type="box" pos="0.95 -0.04 1.05" size="0.04 0.04 1.05" contype="0" conaffinity="0" rgba="0.4 0.25 0.1 1"/>
    </body>
    <body name="door" pos="0 0 0">
      <joint name="hinge" type="hinge" pos="0 0 0" axis="0 0 1" stiffness="20" springref="-0.15" damping="8" armature="0.01"/>
      <geom name="door_panel" type="box" pos="0.45 0 1.02" size="0.44 0.02 1.0" mass="20" rgba="0.7 0.5 0.3 1"/>
      <geom name="door_handle" type="capsule" fromto="0.8 0.02 1.0 0.8 0.08 1.0" size="0.015" mass="0.2" contype="0" conaffinity="0" rgba="0.8 0.8 0.2 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.4" qvel="0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm thinking through a hinged door mechanism that swings shut and stays closed—using a vertical hinge joint starting open, with a spring pulling it toward the closed position plus damping, and a physical stop to prevent it from swinging past shut, possibly biasing the spring reference slightly so it presses against the stop.

I'm now sizing the actual door panel geometry (a thin tall box offset from the hinge axis) and positioning a jamb stop geometry on the correct side so the door collides with it exactly when the hinge angle returns to zero.

I'm also double-checking MuJoCo's parent-child contact filtering rule — since the door's parent body is the world, contacts between them aren't automatically excluded, which is good because I need the door to physically collide with the world-attached jamb stop rather than passing through it.

To be safe, I'll put the jamb in its own static "frame" body welded to world rather than directly in worldbody, since the frame isn't the door's parent, so normal collision filtering applies cleanly between them. I should also make sure the floor clears the door bottom and that the hinge post geom has contype=0 so it doesn't collide with the door itself, while estimating the door's mass from its density and dimensions for reasonable dynamics.

Setting door mass to 20 kg gives hinge inertia around 5.4 kg·m², and with spring stiffness 20 Nm/rad starting at 1.4 rad, the restoring torque near 1.5 rad is about 30 Nm, yielding an undamped frequency near 1.92 rad/s and a period around 3.3 s. I'm picking damping 6 for a critical ratio of about 0.29, aiming for the door to close in roughly 2-3 seconds without slamming too hard, and expecting it to hit the stop around 2 rad/s with some bounce governed by the default contact solver parameters.

I'm settling on stiffness 20, damping 8, and springref -0.15, confirming the door stays shut with the spring pressing at about 2 Nm once closed. There's no gravity torque since the hinge is vertical. I'm adding a handle geom for visuals with contype 0, plus a floor plane and light, using explicit geom mass instead of separate inertial elements, and setting a keyframe at qpos 1.4.

Checking the geometry at that opening angle, I confirm the panel swings clear of the jamb and hinge post without interference, with the hinge post cylinder set to contype 0 so it doesn't collide. Default condim and friction settings are fine, so I'm ready to write the full model.

