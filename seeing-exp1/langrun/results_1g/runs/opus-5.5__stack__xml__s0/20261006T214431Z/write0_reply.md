A motor-driven pusher waits 0.5 s, then shoves the bottom block forward at 0.6 m/s. Friction drags the four blocks above forward faster than they can follow, so the column tips backward and topples.

```xml
<mujoco model="block_stack_topple">
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast"/>

  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" friction="0.8 0.005 0.0001" rgba="0.8 0.8 0.8 1"/>

    <body name="pusher" pos="-0.4 0 0.045">
      <joint name="pusher_slide" type="slide" axis="1 0 0" limited="true" range="-0.1 0.8" damping="0"/>
      <geom name="pusher_geom" type="box" size="0.05 0.1 0.035" mass="2" friction="0.8 0.005 0.0001" rgba="0.8 0.2 0.2 1"/>
    </body>

    <body name="block1" pos="0 0 0.05">
      <freejoint name="block1_free"/>
      <geom name="block1_geom" type="box" size="0.05 0.05 0.05" density="1000" friction="0.8 0.005 0.0001" rgba="0.2 0.4 0.8 1"/>
    </body>
    <body name="block2" pos="0 0 0.15">
      <freejoint name="block2_free"/>
      <geom name="block2_geom" type="box" size="0.05 0.05 0.05" density="1000" friction="0.8 0.005 0.0001" rgba="0.2 0.7 0.3 1"/>
    </body>
    <body name="block3" pos="0 0 0.25">
      <freejoint name="block3_free"/>
      <geom name="block3_geom" type="box" size="0.05 0.05 0.05" density="1000" friction="0.8 0.005 0.0001" rgba="0.9 0.7 0.1 1"/>
    </body>
    <body name="block4" pos="0 0 0.35">
      <freejoint name="block4_free"/>
      <geom name="block4_geom" type="box" size="0.05 0.05 0.05" density="1000" friction="0.8 0.005 0.0001" rgba="0.6 0.2 0.7 1"/>
    </body>
    <body name="block5" pos="0 0 0.45">
      <freejoint name="block5_free"/>
      <geom name="block5_geom" type="box" size="0.05 0.05 0.05" density="1000" friction="0.8 0.005 0.0001" rgba="0.1 0.7 0.8 1"/>
    </body>
  </worldbody>

  <actuator>
    <velocity name="pusher_motor" joint="pusher_slide" kv="300" forcelimited="true" forcerange="-200 200"/>
  </actuator>

  <keyframe>
    <key name="start" ctrl="0.6"/>
  </keyframe>
</mujoco>
```

```expect
pusher touches block1
block5 touches floor
block5 comes to rest
```

---
thinking (summarized):

I'm planning a scene with a stack of five 0.1m cube blocks positioned vertically, plus some kind of pusher object that strikes the bottom block to topple the stack—considering whether to use a sliding box with initial velocity or a swinging pendulum hammer as the impact mechanism.

I'm weighing the physics: if the pusher hits the bottom block too fast, the blocks above might just fall straight down rather than topple, while friction between blocks could drag the whole stack along as a unit if the push is too slow, so I need to tune the pusher's speed and mass to get a convincing toppling effect.

Constant velocity pushing won't cause toppling since the whole stack just slides uniformly. I'm now considering that pushing at the base could actually tip the stack backward due to inertia—like pushing a tall object quickly causes the top to lag behind. Checking whether acceleration needed to tip exceeds what inter-block friction can transmit, given the stack's height-to-width ratio.

Making the pusher effectively massive so block1 snaps to its speed on contact and holds a steady 0.6 m/s, I'm checking whether friction (μ=1) can drag the upper stack along fast enough. Since matching block1's velocity instantly would need infinite force, the stack slips relative to block1, with friction producing acceleration 9.8 m/s² — well above the 2.45 m/s² needed to tip it backward.

So the upper stack topples backward around its rear edge as block1 slides forward out from under it, and I expect it falls toward the pusher, landing somewhere near the pusher arm at height 0.045, while the pusher itself just keeps moving steadily forward.

To keep the pusher from traveling forever, I'll limit its joint range to something like 0.8 m and drive it with a velocity actuator (kv≈200, forcerange ±100) so it pushes against the limit and stops rather than sliding 3.6 m. I'm also checking timing: with the pusher starting at x=-0.4 and block1's rear face at -0.05, there's a 0.3 m gap, giving about 0.5 s where the stack stands untouched before contact at 0.6 m/s — which matches the "stands until pushed" requirement.

Now I'm working out the physical setup: keeping the pusher just clear of the floor (bottom around z=0.01), stacking the 0.1 m cube blocks at z=0.05+0.1*i with negligible gaps, and using default density so each block is 1 kg. The pusher at 2 kg needs enough force to overcome friction (~49 N) plus acceleration, so I'm setting forcerange to 200 and reconsidering kv around 500 for the velocity actuator.

I'm checking the velocity actuator's response time with kv=300, mass 2 kg, giving a time constant of about 0.007s, and verifying stability with dt=0.002 using the implicitfast integrator. With floor and block friction at 0.8, the resulting friction acceleration (~7.8 m/s²) comfortably exceeds the stack's needed acceleration, and since the pusher contacts below the block's center of mass, tipping shouldn't be an issue — though I'm now considering whether the pusher's contact height could catch a block as it tilts backward during the push.

As the column tips back, it rotates around block1's rear top edge near the pusher's front face at height 0.1, with the pusher top at 0.08, meaning the falling column could land partly on the pusher itself. Blocks further up the stack (like block5) fall further back relative to the pusher's footprint, so most land on the floor behind the pusher rather than on it, and since the pusher continues moving forward while fallen blocks stay behind, there shouldn't be direct interference — though I need to double check the case where the tipping column rests partly on the pusher.

The pusher keeps advancing until it hits its joint limit around x=0.4 (range -0.1 to 0.8), pushing block1 to around x=0.5, at which point the velocity actuator holds it there. Based on this, I'd expect contacts like "block5 touches floor" and "block1 touches pusher" to be the key events to report, with blocks further up the stack following similarly once they collapse.

Now I'm setting up the keyframe, ordering the pusher's slide joint first and then the five freejoints for the blocks, computing the full qpos array (36 values: 1 slide + 5×7 for position/orientation).

