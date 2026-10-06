The door is a heavy slab on a vertical hinge. It starts open at 1.4 rad. A torsional spring, like a door closer, pulls it toward −0.3 rad, which is past shut. The joint limit at 0 stops it there, and the leftover spring torque holds it pressed against that stop. Damping takes the energy out of the swing so it settles instead of bouncing.

```xml
<mujoco model="closing_door">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0 0 4" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="4 4 0.1" rgba="0.8 0.8 0.8 1"/>
    <geom name="frame_hinge_post" type="box" pos="-0.04 0 1.03" size="0.03 0.05 1.03" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <geom name="frame_latch_post" type="box" pos="0.94 0 1.03" size="0.03 0.05 1.03" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <geom name="frame_header" type="box" pos="0.45 0 2.09" size="0.52 0.05 0.03" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <body name="door" pos="0 0 0.03">
      <joint name="hinge" type="hinge" axis="0 0 1" pos="0 0 0" limited="true" range="0 1.7" stiffness="20" springref="-0.3" damping="12" armature="0.1"/>
      <geom name="door_slab" type="box" pos="0.45 0 1.0" size="0.44 0.02 1.0" density="600" rgba="0.6 0.4 0.2 1"/>
      <geom name="door_knob" type="sphere" pos="0.8 0.05 1.0" size="0.03" density="600" rgba="0.9 0.8 0.2 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.4" qvel="0"/>
  </keyframe>
</mujoco>
```

```expect
door reaches its lower stop
```

---
thinking (summarized):

I'm thinking the door needs a hinge joint limited to a range (say 0 to 1.6 radians), with a spring pulling it toward the closed position so it swings shut and settles at the stop, starting from an open keyframe position.

Actually, I'll simplify by letting the jamb geom do the stopping with a slightly wider limit range instead, so the door rests against it near zero rotation with negligible penetration. I'll make the jamb non-colliding for looks only, and keep the joint limit as the real stop, giving frame posts contype 0 so they don't interfere with the door's collision geometry. For mass, I'm computing the door body from a wood-density box with half-sizes roughly 0.45 by 0.02 by 1.0.

Now I'm working out the dynamics: hinge inertia near 11.7 kg·m², spring stiffness 20 N·m/rad with a springref of -0.3, and comparing critical damping (~30) against a lower value like 12 so the door swings somewhat underdamped and slams shut realistically. I'm checking the oscillation frequency (~1.3 rad/s) to confirm the door closes from 1.4 rad to 0 in about 1.3 seconds, then stays pressed shut under a small torque, and adding a bit of armature for stability.

Since the hinge axis is vertical, gravity isn't a factor here. I'll describe the outcome as the door reaching its lower stop, setting the hinge as limited with a range of 0 to 1.7, and the keyframe qpos at 1.4.

