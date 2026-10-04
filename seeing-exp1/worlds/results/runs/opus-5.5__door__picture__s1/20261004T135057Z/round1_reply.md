**What I see.** The door is drawn shut in both views for the whole recorded window.

- In the side elevation it shows as one full-width 0.9 m panel between the jambs.
- In the plan it shows as one thin strip along y ≈ 0.
- No fan of residue copies swings in from the open position (about 0.89 m toward +y), so the door never visibly swings.

**Why.** MJCF's default compiler angle unit is degrees. The hinge `range="0 1.6"` was read as 0–1.6°, and `springref="-0.2"` as −0.2°. The keyframe `qpos="1.4"` is always radians, so it started the door far outside its range. The limit snapped it back to about 0 within a few timesteps, before the first 0.03 s copy.

**Fix.** Declaring `<compiler angle="radian"/>` makes the range and spring reference mean what I intended. The door then starts at 1.4 rad and swings shut in about 1 s. It rests against the 0 limit, and the spring presses it there with about 8 N·m.

```json
{"what_happens": "The door appears shut (along x, at y≈0) throughout the recorded window with no visible swing; it never starts open because the joint range was read in degrees and the limit immediately clamped the radian keyframe angle back to ~0.", "works": false, "problem": "Without compiler angle=\"radian\" the hinge range and springref were interpreted in degrees, so the 1.4 rad open start was instantly snapped shut by the limit and no swing occurs."}
```

```xml
<mujoco model="self_closing_door">
  <compiler angle="radian"/>
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0 0 4" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.8 0.8 0.8 1"/>
    <geom name="jamb_hinge_side" type="box" pos="-0.04 0 1.05" size="0.03 0.06 1.05" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <geom name="jamb_latch_side" type="box" pos="0.94 0 1.05" size="0.03 0.06 1.05" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <geom name="lintel" type="box" pos="0.45 0 2.13" size="0.52 0.06 0.03" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <body name="door" pos="0 0 0">
      <joint name="hinge" type="hinge" axis="0 0 1" pos="0 0 0" limited="true" range="0 1.6" stiffness="40" springref="-0.2" damping="15"/>
      <geom name="door_panel" type="box" pos="0.45 0 1.03" size="0.45 0.02 1.0" density="1000" rgba="0.6 0.4 0.2 1"/>
      <geom name="door_knob" type="sphere" pos="0.8 0.05 1.0" size="0.03" density="500" rgba="0.9 0.8 0.2 1"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="1.4" qvel="0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

Checking the plan view, I only see a thin strip near y≈0 from x 0 to 0.9, which suggests the door is closed rather than rotated to 1.4 rad — if it were open at that angle, the plan should show it extending out to y≈0.89, well within the visible y range up to 1.16, but I don't see that.

The elevation rectangle also looks full-width rather than foreshortened, reinforcing that the door appears closed throughout. I'm trying to reconcile this with the physics: with k=40 and the computed inertia around 19.4, damping 15 should produce a close time of roughly 1 second, so I'd expect visible intermediate copies between 0 and 0.6s, but the plan only shows that single strip with maybe a few faint marks near x 0.5–0.8.

I'm checking the pixel geometry of the plan view — the y range runs from about −0.44 to 1.16 meters, mapping to roughly 48 pixels, which puts y=0 around row 115. A door opened to 1.4 rad should reach y≈0.89, landing around row 88, but there's nothing there, confirming the door never actually opened in the visible frames. This makes me question whether the keyframe is actually being applied, or whether something else — joint limits, floor geometry, knob placement — is interfering, though none of those seem like the actual culprit.

Looking at the elevation view, the rectangle spanning roughly rows 8 downward and columns 45–80 lines up with the frame and jambs plus the closed door itself, with no sign of a swinging leaf. The plan view confirms this too — that same strip near row 115 is just the jambs and closed door, no arc or fan shape indicating motion. So it really does look like the door is staying shut throughout the rendered sequence rather than swinging as intended.

I'm concluding the sim genuinely shows no swing — the door stays shut the whole time with no visible motion in the residue trail. For the fix, I'll make the test more robust by explicitly verifying qvel/motion rather than just trusting the keyframe reset, since something in the qpos or spring setup may be silently failing.

I realize I could instead write the door body geometry pre-rotated by 1.4 rad so it's drawn open, making qpos0=1.4 correspond to shut being a −1.4 rotation back — meaning a default reset would already start it open, with range and springref expressed in qpos units. I need to remember to set the compiler's angle mode to radians rather than the default degrees, since I'm specifying the euler rotation in radians.

Actually, I just realized the bug: the compiler's default angle unit is degrees, so my range="0 1.6" was being interpreted as 0 to 1.6 degrees, not radians, while my keyframe qpos=1.4 was in radians — way outside that range, so the joint limit immediately clamped the door almost shut. Springref for hinge joints is converted the same way, so it's affected too. The fix is simply adding `<compiler angle="radian"/>` and keeping the keyframe as is; I should verify afterward that the door still closes within 6 seconds given the damping.

With ζ ≈ 0.27, it's underdamped and reaches the stop around 1.2 s, with the limit absorbing a bit of impact and some minor bounce before settling — that all looks fine.

