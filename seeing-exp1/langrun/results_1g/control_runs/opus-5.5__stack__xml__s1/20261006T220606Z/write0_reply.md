The bottom block is pushed by a ram on a slide joint. A velocity motor drives the ram at 1 m/s, and the keyframe sets that control. The ram starts 0.4 m away, so the stack stands for about 0.4 s before contact.

The bottom block has low friction (0.3) and the blocks above have high friction (0.8). So when `block1` is driven forward, it drags the base of the 4‑block column above it and tips that column backward. The column then falls off `block1` as `block1` slides out. The blocks are slender (8×8×12 cm), which makes tipping easier.

I haven't run this. My estimate says the push is strong enough to tip the column, but not by a large margin.

```xml
<mujoco model="five_block_stack_topple">
  <option timestep="0.002"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" friction="0.3 0.005 0.0001" rgba="0.8 0.8 0.8 1"/>

    <body name="block1" pos="0 0 0.06">
      <freejoint name="block1_free"/>
      <geom name="block1_geom" type="box" size="0.04 0.04 0.06" density="600" friction="0.3 0.005 0.0001" rgba="0.85 0.3 0.3 1"/>
    </body>

    <body name="block2" pos="0 0 0.18">
      <freejoint name="block2_free"/>
      <geom name="block2_geom" type="box" size="0.04 0.04 0.06" density="600" friction="0.8 0.005 0.0001" rgba="0.9 0.6 0.2 1"/>
    </body>

    <body name="block3" pos="0 0 0.30">
      <freejoint name="block3_free"/>
      <geom name="block3_geom" type="box" size="0.04 0.04 0.06" density="600" friction="0.8 0.005 0.0001" rgba="0.9 0.85 0.2 1"/>
    </body>

    <body name="block4" pos="0 0 0.42">
      <freejoint name="block4_free"/>
      <geom name="block4_geom" type="box" size="0.04 0.04 0.06" density="600" friction="0.8 0.005 0.0001" rgba="0.3 0.75 0.35 1"/>
    </body>

    <body name="block5" pos="0 0 0.54">
      <freejoint name="block5_free"/>
      <geom name="block5_geom" type="box" size="0.04 0.04 0.06" density="600" friction="0.8 0.005 0.0001" rgba="0.3 0.45 0.85 1"/>
    </body>

    <body name="ram" pos="-0.48 0 0.05">
      <joint name="ram_slide" type="slide" axis="1 0 0" range="0 0.65" limited="true"/>
      <geom name="ram_geom" type="box" size="0.04 0.06 0.04" mass="3" friction="0.3 0.005 0.0001" rgba="0.4 0.4 0.45 1"/>
    </body>
  </worldbody>

  <actuator>
    <velocity name="ram_motor" joint="ram_slide" kv="300" ctrlrange="0 2" ctrllimited="true" forcerange="-60 60" forcelimited="true"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0 0 0.06 1 0 0 0  0 0 0.18 1 0 0 0  0 0 0.30 1 0 0 0  0 0 0.42 1 0 0 0  0 0 0.54 1 0 0 0  0" ctrl="1"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm planning a scene with a stack of five cube blocks that stays stable until something pushes the bottom one, triggering a toppling cascade. I need the pusher to be driven by the scene itself, like a ram or ball with keyframed velocity, so I'm sketching out block dimensions and stacking positions before figuring out the push mechanism.

Pushing slowly risks the whole stack sliding together as one rigid unit rather than toppling, since friction forces balance out inertia at low speed. A fast, sharp impact on the bottom block seems more likely to actually knock it free and let the upper blocks tip over realistically.

Friction-matching tricks won't work since the stack would just move together, so I consider an impulsive approach: ram block1 at high speed so it shoots out from under the stack, leaving block2 to get only a brief frictional kick at its base as block1 slides free.

I'm estimating the friction impulse from the upper blocks' weight over the ~0.03s clearance time, then checking whether that's enough to rotate or slide the upper column before it drops back down—and whether block2 would slip relative to block3 if the drag exceeds their friction limit.

Each block above shares a decreasing fraction of the friction force, so the shear effect weakens going up the stack, more like a gradual offset than a clean topple—not a very convincing mechanism, so I'm reconsidering whether pushing the bottom block alone can reliably topple the stack or if I need some asymmetry elsewhere.

I'm checking whether the torque condition holds for a 4-block column: needing a > 0.25g to tip about the rear edge, which stays within the friction limit of μg since μ=1. But I realize an actual impulsive velocity step would mean infinite instantaneous acceleration, and the column may not behave as a single rigid body—each block interface could pivot somewhat independently rather than tipping as one unit.

Given that, I'm instead modeling it as a rotational impulse problem: the sudden base velocity v imparts angular momentum about the trailing bottom pivot edge, giving angular velocity ω ≈ 3.53v for this 0.1×0.4 column with moment of inertia about the pivot of 0.0567M. Tipping requires the rotational kinetic energy to exceed the potential energy barrier from raising the center of mass by Δh≈0.0062, so I'm setting up ½Iω² > Mg·Δh to solve for the critical v.

But I'm realizing this assumes the base continues at constant v via a motor-driven pusher, so I need to think about how the impulse actually transmits through friction at the block1-block2 contact, which is capped by μN — meaning if friction is insufficient, block2 will just slide instead of rotating, so I should set block-block friction high while considering how floor friction under the pusher block affects things separately.

After the column topples backward and scatters onto the floor behind the moving block1, the pusher needs to keep driving forward — I'm weighing a velocity actuator with a fixed ctrl value against a position actuator, since a velocity actuator avoids the huge acceleration spikes a high-gain position target would cause.

I'm setting up the joint limit so the pusher stops naturally once it travels its stroke, and giving it a short runway so the stack stands idle before contact, then reaches a smooth push velocity just before hitting block1. I'm also sizing the blocks and their density so the impact is enough to actually topple the stack realistically.

Actually, since the pusher approaches from -x, the column will likely tip back toward the pusher rather than away — that's physically fine, just means falling blocks might land on top of the pusher itself, which I'll allow since it keeps things simple.

I need to make sure block1's friction with block2 (μ=1) transmits enough force before tipping breaks contact to just the rear edge, and that the floor friction under block1 doesn't exceed what the motor can overcome — roughly 29N needed for the 3kg stack, so I'll tune block and floor friction coefficients around 0.6 to balance grip versus slide.

For the stroke, I'm planning the pusher to contact block1 after 0.3m and push it another 0.25m so it fully clears the column's base, causing the column to tip backward as the base shifts out from under it.

Once block1 leaves, the column should drop off the rear edge with rotation, landing tilted on the floor and likely toppling over the 0.6m total stroke. I'm also considering whether the impulsive contact might make block1 separate briefly ahead of the pusher, checking the friction impulse limits against the required momentum transfer to see if the contact can actually deliver that velocity change within a realistic contact duration.

Computing torque about the rear pivot edge gives roughly 1.08M, so with the moment of inertia about that pivot I get α≈19 rad/s², and over the ~0.1s slip phase ω reaches about 1.9 rad/s, just above the 1.47 needed to tip — marginal but plausible, though the column's rigidity across blocks is questionable. Pushing faster at 1.0 m/s extends the slip phase to 0.13s and boosts ω to ~2.5, which seems more robust, and then after the first block exits the column continues rotating as it falls.

I'm reconsidering block dimensions — slimmer blocks (8x8x12cm half-sizes 0.04/0.04/0.06) give a better tip-threshold ratio of a > 0.167g for a 4-block column, which should make toppling easier while still letting a 5-box stack remain stable in the simulator with standard solver settings.

Now I'm positioning the pusher so it stays below block1's height: half-height 0.04 centered at z=0.05 puts its bottom at 0.01 (clear of floor contact) and top at 0.09, leaving room for the stack to fall onto it without unwanted collisions.

After the pusher reaches its joint limit and stops, block1 continues sliding on 0.3 friction, decelerating from 1 m/s over roughly 0.17 m before resting. I'm setting up a velocity actuator for the ram with kv=300 and a force range of ±80N, limited and ctrlrange 0 to 2, then sizing the pusher mass (around 3) and checking the push force needed to overcome block1's friction against the floor.

Calculating block masses at 0.46 kg each with a total stack of about 2.3 kg, friction resistance comes to roughly 6.8 N, so the actuator force is sufficient. I'm positioning the pusher's starting gap from block1 at around 0.25-0.4 m so it reaches the block after a short approach time (~0.3-0.4s), then working out the slide joint's travel range to accommodate this.

As the pusher advances at 1 m/s while the column topples backward, I need to check whether the falling blocks might land on or collide with the pusher's body as it passes beneath the toppling stack, tracking where the pusher's front face ends up relative to the spreading blocks.

I'll give the pusher a heavy 3 kg mass so it reliably drives through the column without being deflected. Blocks are spaced 0.12 m apart starting at z=0.06, touching initially and letting MuJoCo's contacts settle them. For the keyframe, I'm working out the full qpos ordering — five free joints (7 values each) plus the slide joint, with blocks listed first and the ram last, all starting at rest so velocities can be omitted.

I'm setting up a velocity actuator for the pusher with kv=300 and a force range of ±60N, giving roughly 20 m/s² acceleration up to its 1 m/s target speed in about 0.05s. I'm also tracking the friction coefficients per the brief: block1 at 0.3, blocks 2-5 at 0.8, floor at 0.3, with contact pairs taking the max of the two surfaces' values.

For the solver options I'll keep the option tag minimal, just setting timestep to 0.002 as specified rather than adding extra attributes. I should note that the toppling behavior described isn't something I can verify without actually running the simulation, and I need to make sure every body, geom, and light in the XML has a proper name, including adding a visual light source.

