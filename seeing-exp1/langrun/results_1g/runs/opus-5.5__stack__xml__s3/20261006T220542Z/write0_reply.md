The stack is five 10 cm cubes, `block1` to `block5`. A heavy 10 kg ram on a horizontal slide rail starts 0.7 m away, moving at 4 m/s, and hits the bottom block after about 0.18 s. The ram is lower than the bottom block's top face and reaches the end of its rail travel soon after impact. So it kicks `block1` out from under the stack, and the upper blocks lose their support and fall onto the floor. I haven't run this, so the speed and friction values may need tuning.

```xml
<mujoco model="toppling_stack">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" friction="0.5 0.005 0.0001" rgba="0.8 0.8 0.8 1"/>

    <body name="pusher" pos="-0.8 0 0.04">
      <joint name="pusher_slide" type="slide" axis="1 0 0" limited="true" range="0 0.74" damping="0"/>
      <geom name="pusher_geom" type="box" size="0.05 0.04 0.03" mass="10" friction="0.5 0.005 0.0001" rgba="0.8 0.2 0.2 1"/>
    </body>

    <body name="block1" pos="0 0 0.05">
      <freejoint name="block1_free"/>
      <geom name="block1_geom" type="box" size="0.05 0.05 0.05" density="500" friction="0.5 0.005 0.0001" rgba="0.2 0.4 0.8 1"/>
    </body>
    <body name="block2" pos="0 0 0.15">
      <freejoint name="block2_free"/>
      <geom name="block2_geom" type="box" size="0.05 0.05 0.05" density="500" friction="0.5 0.005 0.0001" rgba="0.2 0.7 0.3 1"/>
    </body>
    <body name="block3" pos="0 0 0.25">
      <freejoint name="block3_free"/>
      <geom name="block3_geom" type="box" size="0.05 0.05 0.05" density="500" friction="0.5 0.005 0.0001" rgba="0.9 0.7 0.1 1"/>
    </body>
    <body name="block4" pos="0 0 0.35">
      <freejoint name="block4_free"/>
      <geom name="block4_geom" type="box" size="0.05 0.05 0.05" density="500" friction="0.5 0.005 0.0001" rgba="0.6 0.3 0.8 1"/>
    </body>
    <body name="block5" pos="0 0 0.45">
      <freejoint name="block5_free"/>
      <geom name="block5_geom" type="box" size="0.05 0.05 0.05" density="500" friction="0.5 0.005 0.0001" rgba="0.9 0.4 0.1 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0  0 0 0.05 1 0 0 0  0 0 0.15 1 0 0 0  0 0 0.25 1 0 0 0  0 0 0.35 1 0 0 0  0 0 0.45 1 0 0 0" qvel="4  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
pusher touches block1
block5 touches floor
block4 touches floor
```

---
thinking (summarized):

I'm designing a scene with a stack of five 0.1m cube blocks and a pusher body on a slide joint that starts off to the side and gets a velocity to strike the bottom block, causing the stack to topple.

As block1 slides forward, block2 loses support progressively from its trailing edge, so once the contact point passes block2's center of mass, block2 tips backward and the stack falls to the floor — a clean topple. I'll make the pusher a heavy box sized to strike only block1's height (not block2), giving it a set velocity for a controlled shove rather than a continuous push.

Now I'm estimating the physics: friction between block1, the floor, and block2's weight pressing down creates significant deceleration, so I'm checking whether block1 can actually slide clear before friction kills its momentum. I may need to limit the pusher's travel range or give it enough initial speed to overcome this drag.

I'm checking whether friction drags the stack of blocks 2-5 along as a unit — with μg giving roughly 5 m/s² deceleration, the stack only shifts a few millimeters during the push, which is negligible. I'm considering whether to zero out inter-block friction instead of using the default values to keep things cleaner.

Now I'm worrying about geometry: once block1 is removed and block2 drops, it might partially land on the pusher itself since the pusher's top (0.075) sits below block1's top (0.1) and spans the same region the stack occupies. That overlap seems messy, so I'm thinking about making the pusher a thinner rod positioned lower to avoid colliding with the falling stack.

I'm considering shaping the pusher as a compact "ram" sized to strike block1 at its center height, then letting it stop short so block1 launches off from the impact velocity. Given MuJoCo's soft contact solver, block1 would pick up roughly the pusher's velocity during a brief impact, then decelerate from friction (μ=0.5, about 44 m/s² deceleration) as it slides — I'm estimating it needs to travel roughly 0.1 m to clear the stack.

Working through the numbers, a pusher speed of about 4 m/s gives block1 enough velocity to travel ~0.18 m, more than enough to escape, though I need to check that dragging block2's base briefly as block1 slides past doesn't just translate it rather than tip it — the friction-induced torque should still work in favor of toppling.

I'm also weighing a simpler alternative: instead of a fast impulsive push, slowly pushing the bottom block so the stack topples more predictably under quasi-static conditions.

For the pusher mechanism itself, I'm setting up a slide joint along x with a small gap to block1, limiting its travel so it only contributes a partial push before combining with the launch velocity, giving the heavy pusher a soft stop at the joint limit so it doesn't overshoot too much.

Now I'm sizing the pusher geometry so it sits just above the floor, relying on the slide joint to hold it in place against gravity since that's its only constrained direction, avoiding accidental floor contact. I'm also working out the keyframe's qpos and qvel ordering to cover the pusher plus all five blocks correctly.

For the gap between pusher and stack, a small 0.02m separation would only give about 5ms before impact at 4 m/s, too brief to visibly show the stack standing still first. I'm widening the gap to roughly 0.38m by repositioning the pusher body further back and extending its slide range so it takes about 0.1s to reach the stack, giving a clearer "stands until pushed" moment.

For validation, I want simple observable events like the pusher contacting block1 and block5 eventually touching the floor, since the top block hitting the ground is a clear signal the stack toppled rather than just settling.

I'm naming each geom block1_geom through the stack, giving the pusher its own geom, and adding a light. I'll set floor friction to 0.5 to match the blocks, since contact friction uses the max of the two surfaces.

For mass, blocks use density 500 giving roughly 0.5 kg each, while the pusher's box volume works out to about 4.8e-4 m³, so I'm explicitly setting its mass to 10 kg instead.

