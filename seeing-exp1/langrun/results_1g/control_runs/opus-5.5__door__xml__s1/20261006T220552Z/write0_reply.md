The door hangs on a vertical hinge. The keyframe starts it about 80° open. A torsional spring with a slight negative rest angle swings it shut against the joint limit at 0, and that small preload holds it there. Moderate damping lets it settle well within the 6 s run.

```xml
<mujoco model="door_swings_shut">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="1 -2 4" dir="-0.2 0.4 -1"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>
    <geom name="hinge_post" type="box" pos="-0.04 0 1.02" size="0.03 0.05 1.02" rgba="0.5 0.35 0.2 1" contype="0" conaffinity="0"/>
    <geom name="latch_post" type="box" pos="0.94 0 1.02" size="0.03 0.05 1.02" rgba="0.5 0.35 0.2 1" contype="0" conaffinity="0"/>
    <geom name="door_stop" type="box" pos="0.905 -0.035 1.02" size="0.006 0.012 1.0" rgba="0.4 0.25 0.15 1" contype="0" conaffinity="0"/>
    <body name="door" pos="0 0 0.02">
      <joint name="hinge" type="hinge" axis="0 0 1" pos="0 0 0" limited="true" range="0 1.7" stiffness="20" springref="-0.2" damping="6" frictionloss="0.5"/>
      <geom name="door_panel" type="box" pos="0.45 0 1.0" size="0.45 0.02 1.0" mass="20" rgba="0.7 0.5 0.3 1" contype="0" conaffinity="0"/>
      <geom name="door_handle" type="capsule" fromto="0.8 0.04 1.0 0.8 0.08 1.0" size="0.015" mass="0.2" rgba="0.9 0.85 0.3 1" contype="0" conaffinity="0"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.4" qvel="0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

For the door, I'm thinking a hinge joint about the z-axis starting open with a keyframe qpos, using a spring toward springref 0 plus damping so it swings shut, and limiting the range so 0 acts as the closed stop against the frame. I could also add a door frame post geom for visual collision.

Working through the physics: a 0.9 wide, 0.04 thick, 2.0 tall door at 20 kg mass gives rotational inertia about the hinge around 5.4 kg·m², so with stiffness ~20 Nm/rad the natural frequency is close to 2 rad/s. I'm setting a slightly negative springref so the spring preloads the door into the closed stop, using moderate damping (well under critical) so it swings from its open angle, overshoots slightly past zero, and settles held shut by the preload torque against the limit.

I also want to avoid unwanted collisions: I'll raise the door slightly off the floor, disable collision between the door and the frame/jamb geoms (contype/conaffinity 0 on the frame), and add a small frictionloss at the hinge that stays below the preload torque so it doesn't prevent closing.

Now I'm setting the door's initial open angle in the keyframe, giving the hinge a joint limit instead of relying on contact stops, and assigning the door and handle geoms plausible masses so the swing dynamics feel right.

