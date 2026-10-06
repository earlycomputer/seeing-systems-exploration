**What happened:** The stack stood for 0.6 s while the pusher coasted in. The pusher hit `block1` at 0.60 s, but `block1` moved only about 1 cm before stopping. The pusher then drifted slowly backward for the rest of the run. All five blocks stayed stacked upright and nothing fell.

**Why:** A coasting 1.9 kg paddle at 1 m/s did not carry enough momentum to drag `block1`. That block is pinned to the floor by the friction of the whole stack's weight, so the shove ended well short of the joint limit.

**The fix:**
- **A strong velocity motor instead of coasting.** The paddle is driven at 0.6 m/s with up to 200 N of force, far above the roughly 20 N of floor friction on `block1`. It holds that speed until the joint limit stops it, with `block1` shifted about 7.5 cm.
- **The upper stack is left behind.** The friction between `block1` and `block2` is only 0.1, so blocks 2 to 5 drift just a few millimetres in that short shove. Their centre of mass should end up behind `block1`'s rear edge, and they should topple backward.
- **The arm no longer touches the blocks.** It now starts beside the stack instead of overlapping the rear face of `block1`.

```json
{"what_happens": "The stack stands for 0.6 s; the coasting pusher hits block1 at 0.60 s but only nudges it about 1 cm, then drifts slowly backward; all five blocks remain stacked upright at rest and nothing falls.", "works": false, "problem": "The unpowered pusher has too little momentum to overcome block1's floor friction under the stack's weight, so block1 barely moves and the stack never topples."}
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
      <joint name="pusher_slide" type="slide" axis="1 0 0" limited="true" range="-0.1 0.675" damping="0"/>
      <geom name="pusher_paddle" type="box" size="0.01 0.03 0.015" density="2000" rgba="0.8 0.2 0.2 1"/>
      <geom name="pusher_arm" type="box" pos="0 0.215 0" size="0.01 0.155 0.015" density="2000" rgba="0.8 0.2 0.2 1"/>
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

  <actuator>
    <velocity name="pusher_motor" joint="pusher_slide" kv="300" forcelimited="true" forcerange="-200 200"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0  0 0 0.05 1 0 0 0  0 0 0.15 1 0 0 0  0 0 0.25 1 0 0 0  0 0 0.35 1 0 0 0  0 0 0.45 1 0 0 0" qvel="0.6  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0" ctrl="0.6"/>
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

I'm puzzled why the pusher only reached 0.6 m and block1 moved just 1 cm despite the collision geometry lining up at that position—trying to figure out what stopped the pusher's momentum transfer so short given its mass and initial speed.

I think I need a stronger approach: drive the pusher with a velocity motor at higher speed and force, with a limit stop at 0.68, so it reliably shoves block1 the needed 8 cm against floor friction rather than relying on a soft inelastic collision that's underperforming.

But then I worry the total displacement could overshoot past block1's width, causing it to slide completely out from under the stack rather than just the intended partial shift — so I should dial the speed down to something like 0.6 m/s and recompute how far the stack itself drags along in that time.

At that rate, growing a 0.05 rad tilt to roughly 1 rad takes about 0.5 seconds, so I'll set block1's shift to 0.075 via the pusher to get a final offset near 0.065, which works. The minor details—pusher drift, block2 staying put, motor velocity actuator settings—don't really affect the outcome, so I won't worry about them further.

I'm setting the pusher start about 0.6 m behind block1, giving roughly 1 second of standing time before contact, with the position limit at 0.675 m so the velocity motor pushes firmly against it. The motor force (kv times velocity error, around 180N) easily dominates friction, so the pusher holds its 0.6 m/s speed reliably through the push and into the tipping phase.

I'm checking whether block2 might brush against the arm or paddle during tipping — the paddle top sits at 0.04 and the arm spans roughly y=0.03 to 0.37, while block2's rear overhang spans y±0.05, so there's a slight risk of contact. To avoid this I'm shifting the arm's start to y=0.06 (center 0.215, half-height 0.155), which clears both block1 and the paddle cleanly.

