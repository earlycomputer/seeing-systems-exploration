The stack starts at rest. A heavy, frictionless ram on a slider coasts toward it at 1.2 m/s, hits the bottom block at about 0.46 s, and shoves it about 7 cm forward before a joint limit stops the ram. That leaves the upper four blocks mostly unsupported, so they tip backward off the bottom block's rear edge and fall. I haven't run this; the timing, shove distance and toppling are estimated by hand.

```xml
<mujoco model="five_block_topple">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" friction="0.3 0.005 0.0001" rgba="0.8 0.8 0.8 1"/>

    <body name="block1" pos="0 0 0.05">
      <freejoint name="block1_free"/>
      <geom name="block1_geom" type="box" size="0.05 0.05 0.05" mass="0.5" friction="0.3 0.005 0.0001" rgba="0.8 0.2 0.2 1"/>
    </body>
    <body name="block2" pos="0 0 0.15">
      <freejoint name="block2_free"/>
      <geom name="block2_geom" type="box" size="0.05 0.05 0.05" mass="0.5" friction="0.3 0.005 0.0001" rgba="0.9 0.6 0.2 1"/>
    </body>
    <body name="block3" pos="0 0 0.25">
      <freejoint name="block3_free"/>
      <geom name="block3_geom" type="box" size="0.05 0.05 0.05" mass="0.5" friction="0.3 0.005 0.0001" rgba="0.9 0.9 0.2 1"/>
    </body>
    <body name="block4" pos="0 0 0.35">
      <freejoint name="block4_free"/>
      <geom name="block4_geom" type="box" size="0.05 0.05 0.05" mass="0.5" friction="0.3 0.005 0.0001" rgba="0.2 0.8 0.3 1"/>
    </body>
    <body name="block5" pos="0 0 0.45">
      <freejoint name="block5_free"/>
      <geom name="block5_geom" type="box" size="0.05 0.05 0.05" mass="0.5" friction="0.3 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>

    <body name="ram" pos="-0.62 0 0.025">
      <joint name="ram_slide" type="slide" axis="1 0 0" limited="true" range="0 0.62" damping="0"/>
      <geom name="ram_head" type="box" size="0.02 0.08 0.02" mass="3" friction="0.3 0.005 0.0001" rgba="0.3 0.3 0.3 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 0 0.05 1 0 0 0  0 0 0.15 1 0 0 0  0 0 0.25 1 0 0 0  0 0 0.35 1 0 0 0  0 0 0.45 1 0 0 0  0" qvel="0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  1.2"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm planning a scene with a stack of five small cube blocks that stays upright until a pusher object, animated with a keyframed velocity, strikes the bottom block after a delay and knocks it out, causing the stack to topple. I'm working out the block dimensions (0.1m cubes) and their stacked positions along the vertical axis.

I'm reasoning through the pusher's physics: it needs to slide along a horizontal axis without touching the floor to avoid friction decelerating it, so I'm raising it slightly and considering a velocity actuator to maintain constant speed. I'm weighing whether a slow push would just drag the whole stack via friction versus a faster impact that would cleanly knock the bottom block out and let the upper blocks topple from the sudden instability.

I'm running through the physics numbers: if the bottom block gets shoved out fast enough, friction from the blocks above should be enough to drag block2 along before block1 fully clears, calculating masses and friction coefficients to see if the collision is energetic enough to actually destabilize the stack rather than just sliding it.

That outcome seems unlikely — it probably lands flat with only a slight tilt rather than toppling. For actual toppling, I need the pusher to shift block1 just enough that the upper stack's center of mass ends up outside its base of support, making it fall over sideways rather than just sliding along.

So block2's center ends up outside block1's support edge, meaning the upper stack topples backward toward the pusher side. I need to think about the pusher's geometry—if it's tall it would collide with the falling block2, so maybe shortening the pusher to a thin ram would avoid that collision, though the numbers still need checking.

Let me reconsider the dynamics instead: if block1 is driven out continuously rather than stopping, friction drags the upper stack along and tips it as block1 slides clear, with the tipping rate depending on push speed and the friction coefficient at the base of the stack.

Maybe a pendulum hammer works better: swing it down from a raised angle to strike block1 at the bottom of its arc, knocking it away while continuing its swing. But I need to check that the hammer's pivot and arm don't collide with block2 as it falls back toward where the hammer came from—the pivot would need to sit above the stack, which complicates the geometry.

Simpler idea: just use a sliding ball or ram along the floor to push block1 out, treating it like a sliding puck rather than worrying about arc geometry.

The upper blocks might end up resting on the ball as it rolls under the falling stack, which would just add to the chaos but still satisfy the basic "topple when pushed" requirement, since blocks stay stationary before impact. Maybe I should simplify by reconsidering where and how the pusher strikes block1 — perhaps a sustained, lower push would create a cleaner toppling motion than a sharp collision.

Now I'm working out the friction setup, since MuJoCo combines contact friction by taking the max of the two geoms involved, so I need matching low friction values on both the floor and blocks to avoid the bottom block sticking. I'm also sketching out the ram's physical setup — its size, mass, starting velocity, and slide joint range — so it delivers a controlled jolt to the stack without interacting with the floor itself.

Working through the deceleration: block1 slides another ~3cm after ram stops due to friction, bringing total shift to roughly 0.1. The upper stack (block2) drifts separately under its own friction, slipping maybe 1.5cm plus some rotation, leaving a relative offset where block2 overlaps block1 by only a small margin.

Checking whether block2's center of mass clears its support — it's largely outside the edge, so the upper stack starts to topple backward toward the ram, rotating about block1's rear edge before possibly striking the ram head.

Pushing low on block1 should avoid tipping issues since it's below the center of mass, and I don't need floor contact for the ram if I keep a small gap. For mass, I can just set mass="3" directly on the ram head geom rather than computing density, with no damping on the slide joint. For the blocks, I'll use 0.05 cube size with mass 0.5 and friction 0.3 matching the floor.

Blocks stacked exactly touching should settle slightly from soft contacts, which is fine. When the ram hits its limit at qpos 0.30, block1 shifts about 0.07 forward, which looks right. Checking timing, contact happens around 0.19s given the gap and speed, so I might want more standing time before impact by starting the ram farther back, like x=-0.6.

Setting ram start at -0.62 gives about 0.46s before contact, with travel range up to 0.62 for the slide joint. Now I need to work out the keyframe qpos array — 5 free joints at 7 values each plus the slide joint gives 36 total, ordered by body appearance in the XML with blocks first then the ram, and similarly 31 values for qvel.

I'm specifying each block's position with a slight height increase per block and zero rotation, ram starting at the origin, and qvel as all zeros except a constant 1.2 velocity for the ram until impact. I'm also considering whether the collision with block1 might cause it to bounce ahead of the ram given MuJoCo's contact dynamics.

