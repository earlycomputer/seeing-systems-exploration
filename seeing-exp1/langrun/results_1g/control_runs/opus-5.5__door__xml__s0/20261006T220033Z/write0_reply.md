The door hangs on a vertical hinge and starts 80° open. A torsional spring with damping, acting like a door closer, pulls it shut. A joint limit at 0 acts as the jamb, so the door stops at the frame and stays there.

```xml
<mujoco model="self_closing_door">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0 -3 4" dir="0 0.6 -0.8" directional="true"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>
    <body name="frame" pos="0 0 0">
      <geom name="post_hinge" type="box" pos="-0.06 0 1.03" size="0.04 0.06 1.03" rgba="0.4 0.3 0.2 1"/>
      <geom name="post_latch" type="box" pos="0.96 0 1.03" size="0.04 0.06 1.03" rgba="0.4 0.3 0.2 1"/>
      <geom name="lintel" type="box" pos="0.45 0 2.1" size="0.55 0.06 0.04" rgba="0.4 0.3 0.2 1"/>
      <geom name="stop_strip" type="box" pos="0.45 -0.04 1.03" size="0.47 0.015 0.01" contype="0" conaffinity="0" rgba="0.3 0.2 0.1 1"/>
    </body>
    <body name="door" pos="0 0 0">
      <joint name="hinge" type="hinge" axis="0 0 1" pos="0 0 0" limited="true" range="0 1.6" stiffness="60" springref="0" damping="55" armature="0.1"/>
      <geom name="door_panel" type="box" pos="0.45 0 1.01" size="0.45 0.02 1.0" density="1000" contype="0" conaffinity="0" rgba="0.6 0.4 0.2 1"/>
      <geom name="door_knob" type="sphere" pos="0.8 0.05 1.0" size="0.03" contype="0" conaffinity="0" rgba="0.9 0.8 0.2 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.4" qvel="0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need a door that swings shut and stays closed, so I'm thinking of a vertical hinge joint starting open, with a spring pulling it toward the closed position (springref 0) and damping so it settles rather than oscillating, plus a joint range limit of [0, 1.6] acting like a door frame stop to prevent it from swinging past closed.

I'm sizing the door as a 0.9×0.04×2.0 box hinged at x=0, computing its mass and moment of inertia, then picking spring stiffness and damping values that give a reasonably fast but not too bouncy closing motion (ζ≈0.8), so it swings from 1.4 rad down to the stop and settles within a few seconds. I'm also considering adding simple static jamb/post geoms near the hinge and latch sides as a visual door frame, positioned so they don't intersect the door itself.

I'll keep the stop strip decorative rather than functional, relying on the hinge joint limits instead. The door bottom clears the floor with no contact, so I'll set the keyframe qpos to 1.4, add frictionloss to the latch, name all the parts, use default solreflimit for the hinge, and add a light to the scene.

