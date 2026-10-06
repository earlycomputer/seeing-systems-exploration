The door starts swung open about 80° (`hinge` = 1.4 rad, set by the keyframe). A damped spring on the hinge with its rest angle at 0 pulls it back. The door closes against a fixed stop strip on the latch side, and both the spring and the stop hold it at `hinge` = 0.

```xml
<mujoco model="self_closing_door">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="1 -3 4" dir="-0.2 0.6 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.6 0.6 0.6 1"/>
    <geom name="hinge_post" type="box" pos="-0.12 0 1.05" size="0.05 0.06 1.05" contype="0" conaffinity="0" rgba="0.5 0.35 0.2 1"/>
    <geom name="latch_post" type="box" pos="1.0 0 1.05" size="0.05 0.06 1.05" contype="0" conaffinity="0" rgba="0.5 0.35 0.2 1"/>
    <geom name="lintel" type="box" pos="0.44 0 2.15" size="0.61 0.06 0.05" contype="0" conaffinity="0" rgba="0.5 0.35 0.2 1"/>
    <geom name="door_stop" type="box" pos="0.89 -0.03 1.02" size="0.06 0.01 0.9" rgba="0.3 0.2 0.1 1"/>
    <body name="door" pos="0 0 1.02">
      <joint name="hinge" type="hinge" axis="0 0 1" pos="0 0 0" stiffness="20" springref="0" damping="18" limited="true" range="-0.3 1.7"/>
      <geom name="door_panel" type="box" pos="0.47 0 0" size="0.45 0.02 1.0" mass="36" rgba="0.8 0.6 0.4 1"/>
      <geom name="door_handle" type="sphere" pos="0.75 0.05 0" size="0.03" contype="0" conaffinity="0" mass="0.2" rgba="0.8 0.8 0.2 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.4" qvel="0"/>
  </keyframe>
</mujoco>
```

These numbers are hand estimates. I have not run the file. The door has mass 36 kg and moment of inertia about the hinge of about 9.7 kg·m². With a spring stiffness of 20 N·m/rad and damping of 18 N·m·s/rad, it is underdamped at a damping ratio of about 0.54. It should reach the closed position in about 1.8 s, meet the stop at moderate speed, and settle at about 0 well before the 6 s run ends. The door bottom sits 2 cm above the floor. Only the door panel and the stop strip can collide. The door opens toward +y, away from the stop.

---
thinking (summarized):

I'm planning a door that starts open and swings shut under a spring force pulling it toward hinge=0, with damping to prevent oscillation and a stop so it stays closed once it latches.

I'm sizing the door panel and computing its mass and inertia to estimate a reasonable hinge stiffness and damping value so the swing looks physically plausible and settles against the limit without excessive bouncing.

I'll start the door open at around 80 degrees with moderate underdamping so it swings shut over a couple seconds and gets caught by the joint limit at zero. I'm also thinking through adding a jamb geometry near the door's far edge to act as a visual and physical stop, positioned so it catches the door as it rotates closed.

Since the hinge axis is vertical there's no gravity torque to worry about, but I need to keep the door clear of the floor and the hinge-side jamb geometrically — checking that the bottom clears z=0.02 and that the door's near corner, swinging at radius ~0.028 around the hinge, doesn't clip into the post positioned near x=-0.01 to -0.09.

I realize at a ~80° open angle the swept corner moves to roughly x=-0.016, which does collide with the post, so I'll either make the jamb non-colliding or shift it further out to x=-0.08, treating the frame as mostly decorative except for the door stop. I'm placing the stop on the opposite side near x 0.8-0.95, aligning its face with the door's closed position so it doesn't interfere as the door swings outward and away from it.

Now I'm checking the underdamped settling dynamics — with ζ≈0.54, ωn≈1.43, ωd≈1.2 — to estimate when the door's velocity first crosses zero after contact, since any bounce off the stop should damp out well before the 6s mark.

I'll bump the damping coefficient up to 18 to keep the impact from feeling too abrupt, then move on to setting up the keyframe at qpos 1.4 since it's a single-DOF hinge, and start adding the floor, lighting, and mass properties computed from a reasonable density for the door panel.

