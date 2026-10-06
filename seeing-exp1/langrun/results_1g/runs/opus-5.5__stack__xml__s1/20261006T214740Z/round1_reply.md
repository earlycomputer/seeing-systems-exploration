**What happened:** The pusher reached `block1` at 1.00 s and then drove at about 0.3 m/s to the end of the run. All five blocks slid along together as one upright column, about 1.1 m in total. Nothing tipped, and `block2` and `block5` never touched the floor.

**Why:** The push was slow and steady, so the stack barely had to accelerate. The block-to-block friction (1.0) held it on `block1`, and it rode along instead of falling.

**The fix:**
- **A sudden, short shove instead of a steady drive.**
  - The paddle is now heavy and starts with 1 m/s of keyframe velocity, so it shoves `block1` at about 0.6 s.
  - A joint limit then stops the paddle, so `block1` is shifted only about 8 cm.
- **Low friction between `block1` and `block2`.**
  - Now 0.1 instead of 1.0, so the upper four blocks stay nearly where they were while `block1` slides out.
  - With `block1` shifted that far, their centre of mass ends up behind `block1`'s rear edge, and the column should tip backward over that edge.
- **A low paddle with its arm off to the side.**
  - The paddle top is at 4 cm and its arm extends sideways, so the paddle and arm should stay below the tipping blocks.

These changes are untested; the corrected file below needs another run to confirm the stack topples.

```json
{"what_happens": "The pusher reaches block1 at 1.0 s and keeps driving it at ~0.3 m/s; all five blocks slide together as an upright stack about 1.1 m across the floor and never tip; no upper block touches the floor.", "works": false, "problem": "The slow constant-velocity push plus high block-to-block friction carries the whole stack along instead of knocking the bottom block out from under it, so nothing topples."}
```

```xml
<mujoco model="toppling_stack">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <camera name="side" pos="-0.2 -1.8 0.5" xyaxes="1 0 0 0 0.3 1"/>
    <geom name="floor" type="plane" size="3 3 0.1" friction="0.8 0.005 0.0001" rgba="0.8 0.8 0.8 1"/>

    <body name="pusher" pos="-0.66 0 0.025">
      <joint name="pusher_slide" type="slide" axis="1 0 0" limited="true" range="-0.1 0.68" damping="0"/>
      <geom name="pusher_paddle" type="box" size="0.01 0.03 0.015" density="8000" rgba="0.8 0.2 0.2 1"/>
      <geom name="pusher_arm" type="box" pos="0 0.2 0" size="0.01 0.17 0.015" density="8000" rgba="0.8 0.2 0.2 1"/>
    </body>

    <body name="block1" pos="0 0 0.05">
      <freejoint name="block1_free"/>
      <geom name="block1_geom" type="box" size="0.05 0.05 0.05" density="500" friction="0.1 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>
    <body name="block2" pos="0 0 0.15">
      <freejoint name="block2_free"/>
      <geom name="block2_geom" type="box" size="0.05 0.05 0.05" density="500" friction="0.1 0.005 0.0001" rgba="0.2 0.8 0.3 1"/>
    </body>
    <body name="block3" pos="0 0 0.25">
      <freejoint name="block3_free"/>
      <geom name="block3_geom" type="box" size="0.05 0.05 0.05" density="500" friction="0.6 0.005 0.0001" rgba="0.9 0.8 0.2 1"/>
    </body>
    <body name="block4" pos="0 0 0.35">
      <freejoint name="block4_free"/>
      <geom name="block4_geom" type="box" size="0.05 0.05 0.05" density="500" friction="0.6 0.005 0.0001" rgba="0.9 0.5 0.1 1"/>
    </body>
    <body name="block5" pos="0 0 0.45">
      <freejoint name="block5_free"/>
      <geom name="block5_geom" type="box" size="0.05 0.05 0.05" density="500" friction="0.6 0.005 0.0001" rgba="0.6 0.2 0.8 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0  0 0 0.05 1 0 0 0  0 0 0.15 1 0 0 0  0 0 0.25 1 0 0 0  0 0 0.35 1 0 0 0  0 0 0.45 1 0 0 0" qvel="1.0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
pusher touches block1
block2 touches floor
block5 touches floor
```

---
thinking (summarized):

The stack moved together since block-block friction exceeded floor friction, so I need to lower that friction so the bottom block slides out while the upper ones tip off the offset edge. A tablecloth-style pull might leave the stack upright instead, so I'm reconsidering whether block2's base would slide over block1's trailing edge.

Tracing block1 sliding forward while block2 lags behind, once block1 moves past half its length, block2's center of mass clears block1's rear edge and the upper stack topples backward around that pivot. But the pusher paddle sits right behind block1 at a height below block2's bottom, so the falling stack could land on the moving pusher instead of the floor cleanly — I need a different push approach, maybe pushing from the side instead.

I'm considering alternatives: a fast tablecloth-style impact so block1 shoots out and the stack drops vertically without toppling, or a low thin rod/stick pusher under the stack, but that still risks the tipping block2 catching on the stick near block1's rear top edge.

As the stack falls, block5 may land near the stick lying horizontally underneath, risking the blocks partly resting on it instead of the floor — I should think about bounding the pusher's motion so it stops after pushing block1 a fixed amount, maybe by limiting joint range or using a position actuator, rather than letting it keep pushing into the falling stack.

I'm tracing the paddle's position as it advances, checking whether block2's overhanging rear edge stays above it as the stack tips, working out the pivot geometry so the falling corner sweeps back and down in an arc relative to the paddle's top surface.

I'm also checking that the arm extending in the +y direction stays clear of the falling stack near y≈0, and thinking through whether low inter-block and block-floor friction will let block1 slide forward without dragging block2 along with it.

Realizing a slow constant-velocity push always drags the upper stack along since zero acceleration means static friction carries everything — sliding only occurs with a sudden velocity jump where the needed acceleration exceeds μg. I'm working out the relative displacement during that slip: with kinetic friction decelerating the stack at μg while block1 jumps to speed v, the slip distance is v²/(2μg), and I need that to exceed roughly 0.08 for a clean separation.

But MuJoCo takes the max friction coefficient between two contacting geoms, so I can't just lower block2's friction without affecting its contact with block3 too — I need to think about how setting block1 and block2 to low friction (0.1) propagates through all their contacts, including potentially letting the upper blocks slide apart from each other.

Working through the dynamics: with μ=0.1 between block1 and the stack above, the stack only accelerates slowly while block1 is driven fast by the floor friction and motor, so block1 slips out from under the stack almost immediately, and the stack begins tipping over its rear edge as block1's displacement quickly outpaces it.

Checking whether slower pushing could cause genuine tipping instead of a tablecloth-pull effect, I'm estimating that the push velocity needs to exceed roughly 0.3 m/s given the stack's geometry and friction, otherwise block1 clears too fast for meaningful rotation. At moderate velocities the stack experiences partial tipping with its base landing back on the floor while rotating, likely causing the stack to fall backward rather than forward.

Now I'm considering a cleaner mechanism: a pusher with a limited stroke that nudges block1 just enough (~0.06 m) before stopping, shifting the stack's center of mass behind the base's rear edge so it topples backward slowly, with the paddle positioned so it doesn't interfere with the fall.

I'm also tracing through how block2 behaves as the whole stack rotates about that rear pivot edge—checking whether it swings clear of the paddle and where its bottom face ultimately lands on the floor.

For the pusher mechanism, I'm leaning toward driving it with a scripted velocity keyframe rather than an actuator, so it travels a fixed 0.3m gap and strikes block1 at roughly 0.3 seconds, giving a clean "stands then gets pushed" motion.

Working through the deceleration: once block1 decelerates sharply under the stack's weight, it stops within about a centimeter, while the stack itself keeps sliding forward on block1 at low friction, dragging a bit further before settling—netting a total relative offset of roughly 7 cm with the combined COM trailing slightly behind.

I'm also laying out the paddle and arm geometry: the paddle sits right behind block1's rear edge after the gap opens, and I'm positioning the arm as a thin box extending outward in y from the paddle, aligned in x and z, checking it clears block1's own footprint along y.

The geoms don't need to physically connect since they're part of the same rigid body, so I can place the arm offset slightly without worrying about visual continuity—acceptable even if a bit odd-looking. I'm also noting the joint limit and impact dynamics for the pusher at roughly 2 kg moving at 1 m/s, figuring default solver parameters should handle it fine.

The paddle only strikes block1, since block2's overhang sits well above the paddle's top (0.04 vs 0.1), so contact stays low and clean. With a small COM offset behind the support edge, the stack should tip as a rigid unit, with angular acceleration low enough that the tipping unfolds gradually over roughly half a second to a second.

I'm estimating the pusher's mass from its paddle and arm volumes times steel-like density, landing around 1.9 kg, which seems reasonable. Checking friction interactions during tipping — block1-floor contact resolves to 0.8, block2-block3 to 0.6 — these all look consistent for a stable topple rather than a slide. I'm now setting the pusher's initial keyframe position and velocity, and computing the paddle's centerline position relative to the arm's front offset.

I'm setting the travel range so the paddle front reaches just past block1's shifted position, giving a range of roughly -0.1 to 0.68 with the joint limited, and a stand time of 0.6 seconds. I'll keep the success expectations limited to three conditions: pusher contacting block1, block2 resting on the floor, and block5 resting on the floor.

