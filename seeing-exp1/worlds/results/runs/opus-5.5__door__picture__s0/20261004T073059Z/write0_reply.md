The door starts 1.3 rad open and is pulled shut by a moderately damped hinge spring. The spring's rest angle is slightly past closed (`springref=-0.1`), so it keeps the door pressed against a stiff hinge limit at 0, which acts as the door stop. That holds it shut.

```xml
<mujoco model="self_closing_door">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0 -3 5" dir="0 0.5 -1" directional="true"/>
    <geom name="floor" type="plane" size="5 5 0.1" pos="0 0 0" rgba="0.8 0.8 0.8 1"/>
    <body name="frame" pos="0 0 0">
      <geom name="jamb_hinge" type="box" size="0.03 0.06 1.04" pos="-0.035 0 1.04" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
      <geom name="jamb_latch" type="box" size="0.03 0.06 1.04" pos="0.935 0 1.04" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
      <geom name="header" type="box" size="0.5 0.06 0.03" pos="0.45 0 2.11" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
      <geom name="stop_strip" type="box" size="0.45 0.01 1.0" pos="0.45 -0.035 1.01" contype="0" conaffinity="0" rgba="0.3 0.2 0.1 1"/>
    </body>
    <body name="door" pos="0 0 0">
      <joint name="hinge" type="hinge" axis="0 0 1" pos="0 0 0" limited="true" range="0 1.7" stiffness="30" springref="-0.1" damping="15" solreflimit="0.005 1"/>
      <geom name="door_panel" type="box" size="0.45 0.02 1.0" pos="0.45 0 1.02" mass="30" rgba="0.6 0.4 0.25 1"/>
      <geom name="door_knob" type="sphere" size="0.03" pos="0.8 0.05 1.0" mass="0.2" rgba="0.9 0.8 0.3 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.3" qvel="0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need a door that swings shut and stays closed, so I'll give it a vertical hinge with spring return to zero plus damping so it settles without overshooting, and add a limited joint range so it can't swing past the frame in either direction.

Working through the physics: sizing the door as a 0.9m wide, 0.04m thick, 2m tall box gives roughly 36kg mass and about 9.72 kg·m² of rotational inertia about the hinge. I'm calculating spring stiffness and damping coefficients to get a reasonable closing time—testing critical damping first (settles too slowly, taking many seconds to fully close) then trying a slightly underdamped setup (k=30, c=15, ζ≈0.44) so the door swings shut with a bit of momentum and catches against the frame limit like a real door closing.

I'm settling on a small negative springref (-0.1) so the spring preloads the door against the stop, keeping it held shut at the limit rather than resting with zero force at zero displacement — the limit's soft contact absorbs the impact with minor penetration, and the damping keeps any bounce-back small. I'm also considering adding a visible doorframe geom, but need to be careful it doesn't conflict with the joint limit itself.

For the frame, I'll make jamb posts and header geoms purely visual by setting contype and conaffinity to zero, so they don't physically collide with the door — the limit joint alone handles the physical stop. Since the hinge axis is vertical, gravity doesn't affect swing, and I'll keep the door's bottom just above the floor with a slight gap to avoid any floor contact. The hinge sits at the origin with the door extending along x, swinging toward positive y, with jamb posts placed just outside the door edges and a limited rotation range.

I'm working through the door-slam dynamics: with a damping ratio around 0.44 and natural frequency near 1.76 rad/s, the damped frequency comes out to roughly 1.58 rad/s, giving a first zero-crossing time near 1.1 seconds from rest, with impact velocity around 1.3 rad/s. For the limit itself, I want it closer to critically damped so the stop doesn't bounce noticeably.

No need for added armature or friction loss, and rather than letting the solver auto-compute inertia from geometry and density, I should just set an explicit mass on the geom, something like 30, to keep the dynamics predictable.

