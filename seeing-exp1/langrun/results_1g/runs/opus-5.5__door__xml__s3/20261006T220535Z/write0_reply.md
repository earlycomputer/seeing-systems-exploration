The door starts open at 1.4 rad. A hinge spring with its rest angle just past shut (−0.1 rad) swings it closed. The hinge's lower limit at 0 and a matching jamb strip stop it there. Because the spring keeps pushing against that stop, damping settles the door and it stays shut.

```xml
<mujoco model="swinging_door">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0 0 4" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>
    <geom name="wall_left" type="box" pos="-0.15 -0.04 1.1" size="0.12 0.02 1.1" rgba="0.6 0.55 0.5 1"/>
    <geom name="wall_right" type="box" pos="1.05 -0.04 1.1" size="0.12 0.02 1.1" rgba="0.6 0.55 0.5 1"/>
    <geom name="jamb" type="box" pos="0.88 -0.04 1.01" size="0.04 0.02 0.95" rgba="0.4 0.3 0.2 1"/>
    <body name="door" pos="0 0 0">
      <joint name="hinge" type="hinge" axis="0 0 1" pos="0 0 0" limited="true" range="0 1.7" stiffness="20" springref="-0.1" damping="6" solreflimit="0.01 1"/>
      <geom name="door_panel" type="box" pos="0.46 0 1.02" size="0.44 0.02 1.0" mass="20" rgba="0.7 0.45 0.25 1"/>
      <geom name="door_knob" type="sphere" pos="0.82 0.05 1.0" size="0.03" mass="0.2" rgba="0.9 0.8 0.2 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.4" qvel="0"/>
  </keyframe>
</mujoco>
```

```expect
door reaches its lower stop
door touches jamb
```

---
thinking (summarized):

I want the door to swing shut and actually stay closed, not drift back open. I'm thinking a hinge joint starting open with a spring (springref 0) pulling it toward closed, enough damping to prevent oscillation, and a limited range like "0 1.6" so it stops cleanly at the closed position rather than overshooting.

With damping 5, the system is underdamped (zeta≈0.24), so it'll swing closed and hit the jamb with some velocity, likely bouncing slightly before the spring settles it against the stop—using small restitution in solref should handle that. Gravity doesn't matter since the hinge axis is vertical, and I need to make sure the door's bottom clears the floor and that wall geoms near the hinge don't cause unwanted collisions.

For naming, I'll call the stop geom "jamb" so I can describe the outcome as "door touches jamb." I'm debating whether to also rely on the joint's range limit as a stop or just let the jamb geom alone define the stop, placing it with a small gap so the geometric contact and the range limit don't conflict.

I'll set the jamb geom so its face sits exactly at the contact distance of zero, which should register as touching once the spring pushes slightly into it, so both the lower-stop and jamb-touch expectations hold. Then I'll finalize the keyframe with qpos 1.4 and qvel 0 for the single joint and write out the XML.

