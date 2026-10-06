**What happens in the run.** The door's range is written as `0 2.1`, presumably meant as radians. MuJoCo reads joint ranges in degrees by default, so it applies 0° to 2.1°. The keyframe `qpos="1.2"` is always in radians, so the door starts at 68.8°, far outside that range.

The joint limit then throws the door shut in about 0.06 s, at over 1000°/s. It bounces to −6.5° and rattles between the two stops for about half a second. From about 0.75 s it rests at 0°. The door does end shut and stays shut, but it never swings: the limit snaps it shut, not the spring.

**Does the spring work?** The spring and damper are reasonable on their own:
- The door's inertia about the hinge is about 20·0.9²/3 ≈ 5.4 kg·m².
- With k = 40 the natural frequency is about 2.7 rad/s.
- c = 25 gives a damping ratio of about 0.85.

From 68.8° that is a smooth close over roughly 2 s, with an overshoot of under 0.5°. The lower stop at 0° catches that overshoot gently, like the door meeting its frame.

**Fix.** Write the range in degrees as `0 120`. The 68.8° start is then inside the range and the spring does the closing.

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
{"what_happens": "The door starts at 68.8°, far outside its applied range of 0° to 2.1°, so the joint limit snaps it shut in about 0.06 s at over 1000°/s. It overshoots to -6.5°, rattles between the two stops for about half a second, and rests at 0° from about 0.75 s to the end.", "works": false, "problem": "The hinge range '0 2.1' is read as degrees while the keyframe is in radians, so the door starts outside its range and the limit violently snaps it shut instead of the spring swinging it closed."}
```

---
thinking (summarized):

Since the range defaults to degrees, that's 0–2.1° while qpos is 1.2 rad (68.8°), so the door starts way outside range and slams to the limit at over 1000°/s in just 0.06s — that's the limit violently yanking it shut, not a natural swing. There's also overshoot past the limit to consider.

The real fix is range="0 120" in degrees since qpos is always in radians and 1.2 rad = 68.75° fits that range fine. Checking the dynamics: with inertia about the hinge ~5.4, stiffness 40, damping 25, the critical damping would be ~29.4, so this is underdamped with zeta≈0.85, giving a tiny overshoot (~0.44°) that the lower limit at 0 would absorb — natural frequency comes out to about 2.72 rad/s.

Settling from 1.2 rad to near zero takes roughly 2 seconds, well within a 6-second window, so damping of 25 is fine — overdamping it to 30 would just slow the approach and isn't necessary. I'm also confirming the door panel and hinge-side door post don't geometrically overlap at rest, since the post sits outside the door's shut-position span.

The hinge rotation direction is confirmed correct, and checking the floor clearance shows the door bottom stays just above the ground. I'll finalize the fix as simply setting the joint range to 0–120 degrees, no extra compiler attributes needed.

