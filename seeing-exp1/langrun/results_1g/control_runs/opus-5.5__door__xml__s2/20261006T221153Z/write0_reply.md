The door starts about 80° open. A hinge spring with a slightly negative rest angle pulls it shut, and damping slows it so it doesn't slam. The joint limit at 0 acts as the door frame, with a stop strip as the visible frame stop. Because the spring rest angle (-0.1 rad) lies beyond the closed position, the spring keeps pressing the door against the limit, so `hinge` stays at about 0.

```xml
<mujoco model="door_swings_shut">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0 -3 4" dir="0 0.6 -0.8" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" pos="0 0 0" size="5 5 0.1" rgba="0.6 0.6 0.6 1"/>
    <geom name="wall_hinge_side" type="box" pos="-0.55 0 1.1" size="0.5 0.05 1.1" rgba="0.85 0.82 0.75 1"/>
    <geom name="wall_latch_side" type="box" pos="1.45 0 1.1" size="0.5 0.05 1.1" rgba="0.85 0.82 0.75 1"/>
    <geom name="lintel" type="box" pos="0.45 0 2.15" size="0.5 0.05 0.05" rgba="0.85 0.82 0.75 1"/>
    <geom name="door_stop" type="box" pos="0.87 -0.036 1.01" size="0.03 0.015 0.95" rgba="0.4 0.3 0.2 1"/>
    <body name="door" pos="0 0 0">
      <joint name="hinge" type="hinge" pos="0 0 0" axis="0 0 1" limited="true" range="0 1.7" stiffness="20" springref="-0.1" damping="12"/>
      <geom name="door_panel" type="box" pos="0.45 0 1.01" size="0.45 0.02 1.0" mass="30" rgba="0.55 0.35 0.2 1"/>
      <geom name="door_knob" type="sphere" pos="0.8 0.05 1.0" size="0.03" mass="0.2" rgba="0.9 0.8 0.3 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.4" qvel="0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need a door that swings shut and stays closed — starting open on a hinge, with a spring (springref 0) pulling it back and damping to prevent overshoot, plus a frame or jamb geom acting as a stop so it doesn't swing past closed. Critical damping plus a physical stop should keep it settled shut without needing a separate latch mechanism.

I'm working out the joint limits and geometry: a hinge limited to roughly [0, 1.6] radians, with the limit at 0 acting as the stop, slightly negative springref so the spring presses the door firmly against that limit. I'm sizing the door box, placing the hinge axis, and positioning a small stop strip near the jamb with a tiny gap to avoid overlap while still touching when closed.

For dynamics, I'm computing mass (~30 kg) and inertia about the hinge (~8.1 kg·m²) from the door's dimensions, then picking spring stiffness (20 Nm/rad) and damping (12, giving mild underdamping around zeta 0.47) so the door swings shut visibly from 1.4 rad and settles against the stop in under a second.

Default limit solref should keep bounce minimal when it hits the stop, with the spring continuing to press it at a -0.1 rad offset held by the limit at steady state. I'm now writing the hinge joint definition with range, stiffness, springref, and damping, plus a keyframe setting the initial angle, and adding a hinge-side post at x=-0.05 for the wall geometry.

Checking the door's rotation sweep at x=0, with the left wall ending near x=-0.03 and right wall starting at x=0.93, there's enough clearance for the door tip's circular path, and since the door only rotates toward +y, it stays clear of the stop strip positioned at negative y. Adding a lintel above the door and a light fixture to finish the scene.

