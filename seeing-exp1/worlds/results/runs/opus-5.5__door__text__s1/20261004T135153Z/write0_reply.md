The door hangs on a vertical hinge, and the keyframe starts it open at 1.3 rad. A damped closer spring pulls it shut. The spring's rest angle is set slightly past closed (−0.1 rad), and the hinge range stops at 0. That leaves a small constant torque holding the door against the stop, so it stays shut instead of drifting.

From rough estimates (not run), it should reach 0 in under a second and stay there for the rest of the 6 s, sitting a hair past 0 because the joint limit is soft. The frame and door-stop geoms are only visual: they have contacts off, and the joint limit does the actual stopping.

```xml
<mujoco model="door_swings_shut">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0 -2 4" dir="0 0.4 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" pos="0 0 0" size="5 5 0.1" rgba="0.6 0.6 0.6 1"/>
    <geom name="jamb_hinge" type="box" pos="-0.03 0 1.05" size="0.02 0.05 1.05" rgba="0.5 0.35 0.2 1" contype="0" conaffinity="0"/>
    <geom name="jamb_latch" type="box" pos="0.95 0 1.05" size="0.02 0.05 1.05" rgba="0.5 0.35 0.2 1" contype="0" conaffinity="0"/>
    <geom name="header" type="box" pos="0.46 0 2.12" size="0.51 0.05 0.03" rgba="0.5 0.35 0.2 1" contype="0" conaffinity="0"/>
    <geom name="door_stop" type="box" pos="0.9 -0.03 1.05" size="0.03 0.01 1.0" rgba="0.4 0.25 0.15 1" contype="0" conaffinity="0"/>
    <body name="door" pos="0 0 0">
      <joint name="hinge" type="hinge" axis="0 0 1" pos="0 0 0" limited="true" range="0 1.6" stiffness="20" springref="-0.1" damping="12"/>
      <geom name="door_panel" type="box" pos="0.46 0 1.03" size="0.45 0.02 1.0" mass="20" rgba="0.75 0.55 0.3 1" contype="0" conaffinity="0"/>
      <geom name="handle" type="sphere" pos="0.82 0.05 1.0" size="0.03" mass="0.2" rgba="0.8 0.8 0.2 1" contype="0" conaffinity="0"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.3" qvel="0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need a door that swings shut and stays shut — I'll add a spring on the hinge biased so it presses against a stop at the closed position, with the joint limited and a slightly negative springref so it acts like a door closer. I'll set the starting keyframe with the door open, like 1.2 rad.

Working through the physics: with a door mass around 20 kg and width 0.9m, the moment of inertia about the hinge comes out to roughly 5.4 kg·m², so with stiffness 20 and damping 8 it's underdamped enough to swing shut and settle against the limit at 0 without bouncing too much. I also want to make sure the door geometry doesn't collide awkwardly with the floor or frame posts, so I'm placing the door slightly above the ground and working out the jamb post position so it clears the door when closed.

For the latch, I'm deciding to use the joint limit itself as the stop rather than a separate contact geometry, with maybe a decorative strip (contype 0) for visual realism. Since the hinge axis is vertical, gravity won't add torque, so I just need to set a small frictionloss and define the door's box geometry (positioned and sized appropriately) along with a handle and arm detail.

I'm bumping damping up to around 12 to minimize bounce when it hits the limit, checking that a 1.3 rad swing settles in under a second. I still need the floor, lighting, a keyframe at qpos="1.3", and named bodies/geoms for the frame posts (hinge-side and latch-side jambs plus header), all set to contype=0/conaffinity=0 so they don't interfere with the door's swing.

