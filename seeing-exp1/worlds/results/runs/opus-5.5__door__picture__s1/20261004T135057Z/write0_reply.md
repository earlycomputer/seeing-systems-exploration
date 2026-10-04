The door is a 0.9 m × 2 m slab on a vertical hinge. The `start` keyframe opens it to 1.4 rad. A joint spring pulls it shut, and the spring's rest angle is set slightly past closed (−0.2 rad). The hinge range stops at 0, so the spring keeps pressing the door against that stop with about 8 N·m. Damping absorbs the swing and the impact, so the door comes to rest closed and stays there.

```xml
<mujoco model="self_closing_door">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0 0 4" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>
    <geom name="jamb_hinge_side" type="box" pos="-0.04 0 1.05" size="0.03 0.06 1.05" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <geom name="jamb_latch_side" type="box" pos="0.94 0 1.05" size="0.03 0.06 1.05" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <geom name="lintel" type="box" pos="0.45 0 2.13" size="0.52 0.06 0.03" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <body name="door" pos="0 0 0">
      <joint name="hinge" type="hinge" axis="0 0 1" pos="0 0 0" limited="true" range="0 1.6" stiffness="40" springref="-0.2" damping="15"/>
      <geom name="door_panel" type="box" pos="0.45 0 1.03" size="0.45 0.02 1.0" density="1000" rgba="0.6 0.4 0.2 1"/>
      <geom name="door_knob" type="sphere" pos="0.8 0.05 1.0" size="0.03" density="500" rgba="0.9 0.8 0.2 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.4" qvel="0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm thinking through how to make a door swing shut and stay closed — using a hinge joint with a spring pulling it toward closed, combined with a range limit so it can't swing past zero and oscillate, plus damping to prevent bouncing against the stop.

Now I'm sizing the door (0.9m wide, 2m tall, 0.04m thick, ~72kg) and computing its rotational inertia about the hinge axis to pick a spring stiffness that closes it from an open angle of about 1.4 rad in roughly 1.5 seconds, landing on a stiffness around 40 for the needed natural frequency.

I'm then checking damping: critical damping would be around 56, so I'm choosing a lighter value of 15 to keep it underdamped, letting the door swing and strike the limit stop with some residual velocity before settling shut, with the spring torque at rest confirming it stays closed against the stop. Now I'm positioning the door body and its hinge, making sure the geometry sits just above the floor to avoid unwanted contact.

I'm finalizing the door geometry placement and adding non-colliding jamb geoms just to mark where it closes, setting the hinge axis so the door swings from closed toward open, and setting the initial keyframe angle. Then I'm adding joint damping/stiffness/limit attributes, a light, and names for all bodies and geoms before writing out the file.

