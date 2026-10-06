**What happens in the run.** The hinge range was written as `0 2.1`, meaning radians. MuJoCo reads angles in degrees by default, so it applied the range as 0° to 2.1°. The keyframe's `qpos="1.2"` is in radians, which puts the door at 68.8°, far outside that range.

At 0 s the joint-limit constraint snaps the door back almost at once. It reaches the stops by 0.06 s, moving at about −1040°/s. It overshoots to −6.5°, bounces between the 0° and 2.1° stops, and has settled at 0° by 0.75 s. It stays there until 6 s.

So the door does end shut. But the spring and damper are not swinging it closed. The out-of-range start is corrected by the limit constraint in a 60 ms slam, and the door then rattles inside a 2° window.

**The fix.** Give the range in degrees, `0 120`, so the 68.8° start is inside it.

Checking the swing with that range:
- The door's moment of inertia about the hinge is about 5.4 kg·m².
- With stiffness 40 N·m/rad and damping 25 N·m·s/rad, the damping ratio is about 0.85.
- The door should swing closed over roughly 1.5–2 s.
- Its tiny overshoot of under 1° is caught by the 0° stop, and it then stays shut for the rest of the 6 s.

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
{"what_happens": "The door starts at 68.8°, far outside its applied hinge range of 0° to 2.1°. The limit constraint slams it to the stops in 0.06 s at about 1040°/s, it overshoots to -6.5°, rattles between 0° and 2.1°, and sits still at 0° from 0.75 s to 6 s.", "works": false, "problem": "The hinge range was written in radians but MuJoCo applies it in degrees (0° to 2.1°), so the door starts outside its range and is snapped shut by the limit constraint instead of being swung shut by its spring."}
```

---
thinking (summarized):

I realize the range is actually in degrees, so the hinge limit is just 0 to 2.1°, meaning the starting position at 1.2 rad (68.8°) is already way outside the allowed range. That explains the violent slam—it's snapping back into range at roughly 1000°/s, overshooting to -6.5° before settling, which is physically implausible even though it technically ends up shut.

The fix is to change the range to something like "0 120" in degrees, since qpos is always stored in radians (1.2 rad ≈ 68.8°, which would sit comfortably within that range). I should also double check the door never actually contacts the frame post—it's purely the joint limit stopping it, not a collision.

Settling within 6 seconds seems fine with damping at 25, landing on the lower stop as if closing shut. I'm checking clearances too—the frame post doesn't intersect the rotated panel, and the panel bottom stays clear of the floor.

