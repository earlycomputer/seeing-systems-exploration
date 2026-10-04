The five blocks start stacked and resting. A heavy pusher on a horizontal slide joint starts with a keyframe velocity of 1.5 m/s and reaches the bottom block at about 0.6 s. It drives that block out about 0.15 m, which is more than the block's width, and the upper four blocks fall back over toward the pusher. I haven't simulated it; the timing and the topple come from hand estimates.

```xml
<mujoco model="five_block_stack_topple">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="3 3 0.1" pos="0 0 0" friction="0.8 0.005 0.0001" rgba="0.8 0.8 0.8 1"/>

    <body name="block1" pos="0 0 0.05">
      <freejoint name="block1_free"/>
      <geom name="block1_geom" type="box" size="0.05 0.05 0.05" mass="0.5" friction="0.8 0.005 0.0001" rgba="0.8 0.2 0.2 1"/>
    </body>
    <body name="block2" pos="0 0 0.15">
      <freejoint name="block2_free"/>
      <geom name="block2_geom" type="box" size="0.05 0.05 0.05" mass="0.5" friction="0.8 0.005 0.0001" rgba="0.9 0.6 0.2 1"/>
    </body>
    <body name="block3" pos="0 0 0.25">
      <freejoint name="block3_free"/>
      <geom name="block3_geom" type="box" size="0.05 0.05 0.05" mass="0.5" friction="0.8 0.005 0.0001" rgba="0.9 0.9 0.2 1"/>
    </body>
    <body name="block4" pos="0 0 0.35">
      <freejoint name="block4_free"/>
      <geom name="block4_geom" type="box" size="0.05 0.05 0.05" mass="0.5" friction="0.8 0.005 0.0001" rgba="0.2 0.8 0.3 1"/>
    </body>
    <body name="block5" pos="0 0 0.45">
      <freejoint name="block5_free"/>
      <geom name="block5_geom" type="box" size="0.05 0.05 0.05" mass="0.5" friction="0.8 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>

    <body name="pusher" pos="-1.0 0 0.05">
      <joint name="pusher_slide" type="slide" axis="1 0 0" limited="true" range="0 1.05" damping="0"/>
      <geom name="pusher_geom" type="box" size="0.05 0.08 0.04" mass="3" friction="0.8 0.005 0.0001" rgba="0.3 0.3 0.3 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 0 0.05 1 0 0 0  0 0 0.15 1 0 0 0  0 0 0.25 1 0 0 0  0 0 0.35 1 0 0 0  0 0 0.45 1 0 0 0  0" qvel="0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  1.5"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm planning the scene setup: five stacked cube blocks that stay stable until a pusher mechanism, like a prismatic-jointed slider or pendulum hammer, strikes the bottom block after a delay, knocking it loose so the stack topples. I'm sizing the blocks as small cubes centered on the origin.

The pusher needs to be positioned and shaped so it only contacts the bottom block, not the floor, and timed to strike around half a second in so the stack settles first. I'm considering what happens physically when the bottom block is removed quickly—whether the upper four blocks fall straight down and stay stacked, or whether friction drags them enough to topple.

Pushing with acceleration rather than constant velocity matters: the inertial force on the stack above scales with acceleration, and it should tip once that acceleration exceeds roughly g/4 given the stack's height-to-width ratio, as long as friction (μ≈0.8) is high enough to prevent pure sliding instead of tipping. I'm now checking that the friction force available between blocks is actually sufficient to transmit that acceleration to the upper blocks rather than just letting the bottom slide out from under them.

Friction force on block1 from the stack above comes out to roughly 19.6N, so after impact block1 accelerates quickly while the stack tips from the 7.8 m/s² friction acceleration. I should limit the pusher's travel so it doesn't slide indefinitely at 1.5 m/s — I'll constrain its slide joint range so it only pushes block1 a short distance before stopping.

Tipping depends on whether the friction-driven acceleration exceeds g*w/h; since μg (~7.8) is well above the ~2.45 threshold, the stack should tip, as long as block1 keeps slipping against block2 long enough — checking that slip duration against the 1.5 m/s relative velocity.

For the model setup, I need to account for all freejoints plus the slide joint when ordering qpos/qvel, so I'm putting the blocks before the pusher in the body order to keep things straightforward.

I'm stacking blocks at increasing heights with identity orientation, then setting up the pusher dimensions and mass so it stays clear of the floor while sliding freely, and tuning friction values so the pusher-block contact behaves realistically even if the stack tips backward onto it.

Now I'm widening the pusher's y-dimension for a squarer hit, setting initial velocities with zero for the blocks and a push speed for the pusher, and adding a named light plus ensuring every body, geom, and the floor all have proper names.

