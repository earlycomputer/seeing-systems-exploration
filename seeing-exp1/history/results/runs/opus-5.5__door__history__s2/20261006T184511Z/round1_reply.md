**What happens in the run:** the door does end up shut and stays there, but it never swings. Its range is written as `range="0 2.1"`, which looks like radians. MuJoCo's compiler defaults to degrees, so it applied the range as 0° to 2.1°. The keyframe sets qpos=1.2, which is in radians (68.8°), so the door starts far outside its range. The limit constraint then throws it back in about 0.06 s at roughly 1040°/s. It overshoots to −6.5°, past its lower stop, bounces between the stops, and settles at 0° by 0.75 s. That violent snap comes from the limit correcting the violation, not from a swing driven by the spring.

**Fix:** give the range in degrees, `range="0 120"`, so the starting 68.8° is legal. The hinge spring (stiffness 40) and damping (25) then swing the door shut. The door's moment of inertia about the hinge is about 5.4 kg·m², so the damping ratio is about 0.85. The door closes smoothly in about a second, and the lower stop at 0° holds it shut.

```xml
<mujoco model="door_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="5 5 0.1"/>
    <geom name="frame_post" type="box" pos="0 -0.12 1.05" size="0.04 0.04 1.05"/>
    <body name="door" pos="0 0 1.0">
      <joint name="hinge" type="hinge" axis="0 0 1" pos="0 0 0" stiffness="40" springref="0" damping="25" range="0 120" limited="true"/>
      <geom name="door_panel" type="box" pos="0 0.45 0" size="0.02 0.45 0.98" mass="20"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.2"/>
  </keyframe>
</mujoco>
```

```json
{"what_happens": "The door starts at 68.8°, far outside its applied 0°–2.1° range, so the joint limit throws it to 0° in 0.06 s at about 1040°/s. It overshoots to -6.5°, bounces between the stops, and settles shut at 0° by 0.75 s, staying there to 6 s.", "works": false, "problem": "The hinge range was written in radians but applied in degrees (0°–2.1°), so the door starts outside its range and is snapped shut by the limit constraint instead of swinging shut under its spring."}
```

---
thinking (summarized):

Since the range is in degrees but the keyframe qpos is in radians, the door starts well outside its limit and gets violently snapped shut by the constraint in 0.06s — over 1000°/s, which is really a snap rather than a natural swing, even though it technically ends up shut.

The fix is to either set compiler angle to radian or change the range to degrees like "0 120" — then with that spring/damping setup (zeta≈0.85) the door would settle smoothly with negligible overshoot, hitting the lower limit cleanly instead of being thrown.

Checking settle time: decay rate near 2.3/s means a 1.2 rad swing damps to about 0.001 rad within roughly 3 seconds, which is acceptable.

