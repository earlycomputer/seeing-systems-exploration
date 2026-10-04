The stack stands still for about 1 s. Then a ram on a horizontal slide joint, started by the keyframe velocity, hits the bottom block. The ram keeps shoving the block until a joint limit stops it, which knocks the block out from under the stack. The friction kick and the 0.1 m drop should make the four blocks above tip over, back toward the ram. I haven't run this, so how far each block ends up is my estimate, not a measured result.

```xml
<mujoco model="toppling_stack">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="3 3 0.1" friction="0.8 0.005 0.0001" rgba="0.8 0.8 0.8 1"/>

    <!-- Pusher (ram): slides along +x, starts 1 m from the stack, hits block1 at about t = 1 s, stops at the joint limit -->
    <body name="pusher" pos="-1.08 0 0.05">
      <joint name="pusher_slide" type="slide" axis="1 0 0" limited="true" range="0 1.2" damping="0"/>
      <geom name="pusher_geom" type="box" size="0.04 0.1 0.04" mass="3" friction="0.3 0.005 0.0001" rgba="0.8 0.2 0.2 1"/>
    </body>

    <!-- Stack of five 0.08 x 0.08 x 0.10 m blocks -->
    <body name="block1" pos="0 0 0.05">
      <freejoint name="block1_free"/>
      <geom name="block1_geom" type="box" size="0.04 0.04 0.05" density="600" friction="0.8 0.005 0.0001" rgba="0.2 0.4 0.8 1"/>
    </body>
    <body name="block2" pos="0 0 0.15">
      <freejoint name="block2_free"/>
      <geom name="block2_geom" type="box" size="0.04 0.04 0.05" density="600" friction="0.8 0.005 0.0001" rgba="0.2 0.7 0.3 1"/>
    </body>
    <body name="block3" pos="0 0 0.25">
      <freejoint name="block3_free"/>
      <geom name="block3_geom" type="box" size="0.04 0.04 0.05" density="600" friction="0.8 0.005 0.0001" rgba="0.9 0.7 0.2 1"/>
    </body>
    <body name="block4" pos="0 0 0.35">
      <freejoint name="block4_free"/>
      <geom name="block4_geom" type="box" size="0.04 0.04 0.05" density="600" friction="0.8 0.005 0.0001" rgba="0.6 0.3 0.7 1"/>
    </body>
    <body name="block5" pos="0 0 0.45">
      <freejoint name="block5_free"/>
      <geom name="block5_geom" type="box" size="0.04 0.04 0.05" density="600" friction="0.8 0.005 0.0001" rgba="0.3 0.8 0.8 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0  0 0 0.05 1 0 0 0  0 0 0.15 1 0 0 0  0 0 0.25 1 0 0 0  0 0 0.35 1 0 0 0  0 0 0.45 1 0 0 0" qvel="1.0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm thinking through how to make the toppling happen without external control — maybe a pendulum hammer swinging from a height to strike the bottom block, or a frictionless slider given initial velocity so it coasts into the stack on its own.

I decide on a pusher block on a slide joint with keyframed velocity, floating just above the floor so it doesn't pick up friction, timed to strike the bottom cube around one second in. I'm checking that the block heights line up so the pusher contacts within the bottom block's vertical range, and reasoning about whether a fast strike will actually knock the bottom block free while friction drags the block above into toppling rather than just sliding along with it.

I'm roughing out masses and forces: giving blocks moderate density for about 0.5 kg each, picking pusher mass and speed, and estimating the friction force from the blocks above pressing down to see if it's enough to resist the bottom block's sudden acceleration, which determines whether the stack actually tips over.

After the bottom block drops away, the stack likely tilts and could topple given its slender aspect ratio, though a slow push instead would just slide the whole stack without toppling since it rides along as a unit. I'm leaning toward the fast knockout being the reliable way to induce toppling, since the angular kick would tip the upper stack backward as it falls.

Lower pusher speed actually increases contact time and impulse, but if the pusher keeps pushing steadily, the stack could just accelerate together at μg and ride along with minimal relative slip — meaning the toppling effect might vanish entirely rather than intensify at low speed.

Actually, checking tipping: with a=μg=9.8, that's way above the threshold of g/4 needed to tip the stack backward about the base interface, so the stack would topple. But individual block-to-block interfaces matter too since the column isn't rigid — I need to check each interface separately, since blocks can hinge relative to each other at any contact face, not just at the base.

To be safe I should make the impact decisive, maybe limit the pusher's travel so it stops while the bottom block flies free — the bottom block would then decelerate at μg on the floor, stopping fairly quickly given its initial speed.

I'm working out the geometry so the stack stands undisturbed for about a second before the pusher reaches it: sizing the blocks and pusher box, setting the starting gap at roughly 1 meter with a 1 m/s approach speed, and figuring the slide joint's starting position and contact point accordingly.

I'm adding a travel limit on the slide joint so it pushes the block about 0.2 m before stopping, and setting the pusher mass to 3 kg. I'm also checking that the pusher geometry stays clear of the floor so gravity and extra contacts don't interfere, and confirming the keyframe qpos layout covers the slide joint plus the block free joints.

Now I'm working out the keyframe's qvel ordering, giving the pusher an initial velocity of 1.0 m/s and zeroing the rest, and tuning friction values so the pusher slides smoothly into block 1 without lifting it. I'm estimating the resulting velocities after impact given the pusher's 3 kg mass versus the roughly 0.5 kg block, and checking the pusher travels far enough to shove the block about 0.2 m total before hitting its limit.

I'm also considering whether the upper stack will actually topple from the kick rather than just dropping flat, and thinking about adjusting block dimensions from cubes to a slightly taller shape to make the stack more prone to tipping over during the impact.

