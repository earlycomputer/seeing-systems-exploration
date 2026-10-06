**What happens in the run**

The pusher sphere starts rolling. Its speed drops from 1.5 to about 1.07 m/s as it starts to spin. It reaches block1 at 0.92 s and shoves the whole stack about 5–6 cm along +x. The stack leans by only 2–3° and rocks back and forth. By 1.71 s all five blocks are at rest, upright and still stacked, and they stay that way to 6 s.

**Why it fails**

The bottom block is pushed, but the stack never topples. The 4 kg pusher arrives at about 1 m/s. That is too soft a hit: the whole stack slides together a few centimetres instead of being knocked over.

**The fix**

I made the pusher much heavier and faster: 10 kg, launched at 4 m/s, so it arrives at about 2.9 m/s. I also raised the friction on the blocks so the bottom block's motion drags block2 sideways. The expected result is that block1 gets knocked out from under the stack, and the four blocks above lose their support and fall over. I have not run this corrected version, so it needs a re-run to confirm the topple.

```xml
<mujoco model="stack_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="6 6 0.1" friction="0.6 0.005 0.0001"/>
    <body name="block1" pos="0 0 0.100">
      <freejoint/>
      <geom name="block1" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.8 0.005 0.0001"/>
    </body>
    <body name="block2" pos="0 0 0.300">
      <freejoint/>
      <geom name="block2" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.8 0.005 0.0001"/>
    </body>
    <body name="block3" pos="0 0 0.500">
      <freejoint/>
      <geom name="block3" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.8 0.005 0.0001"/>
    </body>
    <body name="block4" pos="0 0 0.700">
      <freejoint/>
      <geom name="block4" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.8 0.005 0.0001"/>
    </body>
    <body name="block5" pos="0 0 0.900">
      <freejoint/>
      <geom name="block5" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.8 0.005 0.0001"/>
    </body>
    <body name="pusher" pos="-1.2 0 0.1">
      <freejoint/>
      <geom name="pusher" type="sphere" size="0.1" mass="10.0" friction="0.3 0.005 0.0001"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0 0 0.100 1 0 0 0  0 0 0.300 1 0 0 0  0 0 0.500 1 0 0 0  0 0 0.700 1 0 0 0  0 0 0.900 1 0 0 0  -1.2 0 0.1 1 0 0 0" qvel="0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  4.0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```json
{"what_happens": "The pusher sphere rolls in, slowing to about 1.07 m/s as it starts to spin, and hits block1 at 0.92 s. The whole five-block stack slides about 5 cm along +x as a unit and wobbles 2-3 degrees. By 1.7 s it settles upright and stays stacked at rest until 6 s.", "works": false, "problem": "The push is too weak, so the stack only slides a few centimetres and rocks back upright instead of toppling."}
```

---
thinking (summarized):

The pusher slows from 1.5 to 1.07 as it rolls, then hits block1 at 0.92s, sliding it 6cm and making the stack wobble 2-3° before settling upright—so it doesn't topple, meaning this approach fails. I need to rethink the strategy, maybe by kicking the bottom block out faster to force a topple instead.

Hard to predict precisely without full simulation. I'm weighing whether a fast ejection of block1 reliably topples the upper stack versus just dropping it flat, and estimating friction forces between blocks to see if there's enough drag/torque to cause tipping rather than a clean slide of the whole stack together.

So the bottom interface tips first since a=2.45 m/s² is the lowest threshold, but I need to check friction can actually deliver that: mu must exceed 0.25, and with mu=0.6 that's fine. During an impulsive push, friction between block1 and block2 caps the force at mu*N≈11.8N, giving the upper stack 5.9 m/s² of acceleration, well above the 2.45 tipping threshold, while block1 itself slides out from underneath as block2 gets torqued over.

Now I'm working out the deceleration of block1 from floor and block2 friction, roughly 53 m/s², against the pusher's momentum of about 4.3 kg·m/s, estimating the pusher stops in roughly 0.1s during which the upper stack moves together with block1 without relative sliding.

This gives too small an acceleration (~5 m/s²) with only a 3° tilt that then rocks back, so I need a stronger, longer push. I'm reconsidering with a much heavier 20 kg pusher at 3 m/s so block1 gets driven hard enough that the upper stack's friction limit of 11.8N yields an acceleration around 5.9 m/s².

Tracking through the geometry: block1 slides clear of block2 in about 0.07s, giving block2 a velocity around 0.4 m/s and some torque, but the rotation dynamics get messy since friction only directly acts on block2 while blocks 3-5 get dragged along through inter-block friction, causing relative tipping between blocks as the stack falls.

The faster pusher (20 kg vs 0.5 kg) would actually keep moving after block1 slides away and could collide with block2 again once it's landed on the floor, essentially double-pushing the base and likely toppling everything like a bowling strike -- though I want a cleaner, more deterministic toppling mechanism rather than relying on this secondary collision. A simpler approach might be to just hit block1 with enough momentum directly.

I'm working through the collision timing: block1 slides out quickly after impact, and as blocks 2-5 start falling roughly 0.2s later, I need to check whether the still-moving pusher ends up positioned underneath block2 just as it drops, which would complicate the dynamics.

Given the mass mismatch (heavy pusher vs light blocks), this could fling blocks rather than produce a clean topple, but scattered blocks on the floor should still satisfy the "topple" requirement. I'll settle on a pusher around 8 kg to balance a convincing knock against not overly chaotic launching.

