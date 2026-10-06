The door hangs on a vertical hinge and starts swung open about 75°. A damped hinge spring with its rest angle set slightly past shut (`springref="-0.3"`) swings it closed. The joint's lower limit at 0, matching the door jamb, stops it. Because the spring's rest angle lies beyond that limit, the spring keeps the door pressed against the stop, so it stays shut.

```xml
<mujoco model="closing_door">
  <option timestep="0.002"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="1 -2 4" dir="-0.3 0.5 -1" diffuse="0.8 0.8 0.8"/>
    <camera name="view" pos="2.2 -2.6 1.8" xyaxes="0.76 0.65 0 -0.3 0.35 0.89"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.6 0.6 0.6 1"/>
    <body name="frame" pos="0 0 0">
      <geom name="frame_hingepost" type="box" pos="-0.03 0 1.05" size="0.02 0.05 1.05" rgba="0.4 0.3 0.2 1"/>
      <geom name="frame_jamb" type="box" pos="0.95 -0.031 1.05" size="0.05 0.01 1.05" rgba="0.4 0.3 0.2 1" contype="0" conaffinity="0"/>
      <geom name="frame_latchpost" type="box" pos="0.97 0.02 1.05" size="0.03 0.04 1.05" rgba="0.4 0.3 0.2 1" contype="0" conaffinity="0"/>
      <geom name="frame_lintel" type="box" pos="0.47 0 2.13" size="0.53 0.05 0.03" rgba="0.4 0.3 0.2 1"/>
    </body>
    <body name="door" pos="0 0 0">
      <joint name="hinge" type="hinge" axis="0 0 1" pos="0 0 0" limited="true" range="0 1.7" stiffness="40" springref="-0.3" damping="15" solreflimit="0.01 1"/>
      <geom name="door_panel" type="box" pos="0.45 0 1.02" size="0.45 0.02 1.0" density="500" rgba="0.7 0.5 0.3 1"/>
      <geom name="door_knob" type="sphere" pos="0.82 0.06 1.0" size="0.03" density="500" rgba="0.9 0.8 0.2 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.3" qvel="0"/>
  </keyframe>
</mujoco>
```

```expect
door reaches its lower stop
```

---
thinking (summarized):

I'm picturing a door on a vertical hinge with a door frame acting as a stop — it starts open with a spring (springref=0) pulling it closed, using damping and a joint range limit so it settles at the lower stop without bouncing back open.

I'll set the hinge range to something like 0 to 1.7, with a slightly negative springref (-0.2) so the spring presses the door firmly against the stop rather than resting loosely at contact. I'm weighing whether to add an actual jamb geom for visual contact, but worry it might conflict with the joint limit, so I'll keep both colliding but positioned so the limit engages right at the stop point.

Now I'm working out the door and jamb geometry: setting the jamb to non-colliding (contype/conaffinity 0) to avoid overlap issues, sizing the door box with mass and inertia estimates (~36 kg, ~9.7 kg·m² about the hinge), and positioning the jamb on the closing side so it aligns with the hinge stop at q=0. I'm also picking spring stiffness (k=40) to get a natural frequency around 2 rad/s, balancing a door that swings freely but settles back firmly against the stop.

Choosing damping (c=15, underdamped ζ≈0.38) so the door swings and oscillates a bit before settling against the lower limit rather than snapping immediately. Checking that gravity doesn't affect the vertical hinge, confirming the door stays clear of the floor with no unwanted contact, and setting the keyframe to start the door open at q=1.3 before it swings closed and rests at its stop.

