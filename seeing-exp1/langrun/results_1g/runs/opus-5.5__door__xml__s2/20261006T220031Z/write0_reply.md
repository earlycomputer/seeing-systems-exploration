The door starts open at 1.2 rad. A damped spring on the hinge pulls it toward a point slightly past shut (springref −0.3). So it swings closed, hits the hinge's lower limit at 0, presses against a jamb strip, and the spring holds it there.

```xml
<mujoco model="self_closing_door">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0 0 5" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>
    <body name="frame" pos="0 0 0">
      <geom name="frame_hinge_post" type="box" pos="-0.04 0 1.0" size="0.02 0.05 1.0" rgba="0.5 0.35 0.2 1"/>
      <geom name="frame_latch_post" type="box" pos="0.86 0 1.0" size="0.02 0.05 1.0" rgba="0.5 0.35 0.2 1"/>
      <geom name="frame_lintel" type="box" pos="0.41 0 2.04" size="0.47 0.05 0.02" rgba="0.5 0.35 0.2 1"/>
    </body>
    <body name="jamb" pos="0 0 0">
      <geom name="jamb" type="box" pos="0.78 -0.035 1.0" size="0.04 0.015 0.95" rgba="0.3 0.2 0.1 1"/>
    </body>
    <body name="door" pos="0 0 0">
      <joint name="hinge" type="hinge" axis="0 0 1" pos="0 0 0" limited="true" range="0 1.6" stiffness="20" springref="-0.3" damping="8" solreflimit="0.01 1"/>
      <geom name="door_panel" type="box" pos="0.42 0 1.01" size="0.4 0.02 1.0" density="500" rgba="0.6 0.4 0.25 1"/>
      <geom name="door_knob" type="sphere" pos="0.74 0.05 1.0" size="0.025" density="500" rgba="0.9 0.8 0.2 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.2" qvel="0"/>
  </keyframe>
</mujoco>
```

```expect
door reaches its lower stop
door touches jamb
```

---
thinking (summarized):

I'm designing the door hinge so it has a limited range with a stop at shut, using a spring that pushes slightly past the stop (negative spring reference) combined with damping so it settles against the frame without bouncing.

I'm also adding a physical jamb body for the door to contact near the free end, positioning it with a tiny gap so the joint limit engages first and the contact geometry confirms it, keeping the margin tight enough to avoid visible overlap.

Working out the door's physical parameters: computing mass from density giving about 32kg, deriving rotational inertia around the hinge axis, then picking spring stiffness (~20) and damping (~8) so the door swings shut in roughly 1.5 seconds with enough speed to reach the stop realistically.

I'm checking collision geometry so the door doesn't clip into the frame post during rotation, keeping a small gap above the floor to avoid unwanted contact, and setting the initial keyframe angle to 1.2 radians open.

Now I want to make sure the expected outcomes are testable—phrases like "door reaches its lower stop" or "door touches jamb" work, but something vague like "door comes to rest" needs a clear target object, so I'll skip that one.

