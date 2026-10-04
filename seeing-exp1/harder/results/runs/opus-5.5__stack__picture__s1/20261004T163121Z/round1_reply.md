**What happens.** The 4 kg sphere rolls in from x = −1.2 m. Its fading copies march right along the floor and stop against the left face of the bottom block. The five-block column is drawn once, crisp and dark, in both the side view and the plan view. So the stack never moved. Nothing topples.

**Why it fails.** The sphere arrives at about 1.5 m/s, gives the bottom block a short shove, and stops. All the blocks share friction 0.6. Under that shove, block 1 either barely moves or carries the whole stack with it, so the tower stays upright.

**The fix.** Toppling needs the bottom block driven partway out from under the stack and then stopped. If it moves more than half its width (0.1 m) but less than its full width (0.2 m), the centre of mass of the four blocks above sits past block 1's trailing edge. They then tip over that edge and fall.

Changes in the corrected file:
- **Pusher.** It is now a ram on a slide joint, driven by a heavily damped position servo whose target the keyframe sets. It approaches slowly, so the impact cannot fling block 1. The servo is meant to stall at about 30 N, against roughly 27 N of friction, leaving block 1 displaced about 0.13 m. That figure comes from hand calculation; I have not simulated it.
- **Friction.** The floor is set to 1.0, so block 1 stops as soon as the ram stops. The blocks are set to 0.1, so block 1 slides out without dragging block 2 along.
- **Ram height.** It is low enough to touch only block 1.

```json
{"what_happens": "The pusher sphere rolls from x=-1.2 to the bottom block and stops against it; the five-block stack stays standing, drawn unmoved in both views. Nothing topples.", "works": false, "problem": "The sphere's push neither drives the bottom block out from under the stack nor tilts it, so the stack stays standing instead of toppling."}
```

```xml
<mujoco model="stack_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="6 6 0.1" friction="1.0 0.005 0.0001"/>
    <body name="block1" pos="0 0 0.100">
      <freejoint/>
      <geom name="block1" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.1 0.005 0.0001"/>
    </body>
    <body name="block2" pos="0 0 0.300">
      <freejoint/>
      <geom name="block2" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.1 0.005 0.0001"/>
    </body>
    <body name="block3" pos="0 0 0.500">
      <freejoint/>
      <geom name="block3" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.1 0.005 0.0001"/>
    </body>
    <body name="block4" pos="0 0 0.700">
      <freejoint/>
      <geom name="block4" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.1 0.005 0.0001"/>
    </body>
    <body name="block5" pos="0 0 0.900">
      <freejoint/>
      <geom name="block5" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.1 0.005 0.0001"/>
    </body>
    <body name="pusher" pos="-0.55 0 0.08">
      <joint name="ram_slide" type="slide" axis="1 0 0" damping="400"/>
      <geom name="pusher" type="box" size="0.05 0.15 0.05" mass="3.0" friction="0.1 0.005 0.0001"/>
    </body>
  </worldbody>
  <actuator>
    <position name="ram_drive" joint="ram_slide" kp="1000" ctrlrange="0 0.7"/>
  </actuator>
  <keyframe>
    <key name="start" qpos="0 0 0.100 1 0 0 0  0 0 0.300 1 0 0 0  0 0 0.500 1 0 0 0  0 0 0.700 1 0 0 0  0 0 0.900 1 0 0 0  0" ctrl="0.56"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm picturing the pusher sphere rolling from -1.2 toward the stack, leaving residue copies up to about x=-0.1 where it touches block1, while the stack itself stays standing and unchanged throughout — at least through 1.91s, with a residue copy drawn every 0.08s over that span.

Working through the physics: the sphere moving at 1.5 m/s reaches block1 around 0.73s, contacting it near its base. With the stack's weight pressing down (roughly 4 blocks above adding ~19.6N normal force and ~11.8N friction on block1), it seems unlikely the sphere would topple the stack outright — more plausible it'd just slide block1 slightly or stall against it, consistent with the image showing the column unchanged and the residue stopping right at the block's face.

For a real topple, I need to reconsider the mechanism — knocking the bottom block out fast enough that inertia makes the upper blocks lean and fall, rather than just sliding the whole stack together, since high block-to-block friction would otherwise drag the base along with everything stacked on it.

I'm working out a more targeted approach: give block1 high floor friction so it only slides a small distance (0.1-0.15 m) before stopping, while high inter-block friction drags the stack above along with it, shifting block1's support out from under block2's center of mass until it overhangs the edge enough to topple.

Now I need the displacement to land in a narrow window (roughly 0.12-0.18 m) so the four-block upper stack tips over its pivot edge rather than just sliding or dropping cleanly—controlling that precisely is the tricky part, and I'm thinking through how the pusher's kinetic energy converts into block1's sliding motion to hit that range.

Since MuJoCo combines friction by taking the max between contacting geoms, I need floor friction high and block-to-block friction low, but block1 touches both the floor and block2, so its own friction value affects both contacts. Setting floor friction to 1.0 and block material friction to 0.1 gives floor-block1 friction of 1.0 and block1-block2 friction of 0.1, which should let the upper stack slide relative to block1 instead of locking together.

For the pusher, I'm thinking a box on a slide joint is the cleanest way to get deterministic motion — give it a velocity via keyframe, a joint range to limit travel, and let it ram into block1 until it stops at its limit, after which block1 continues sliding and decelerating from floor friction alone, with a quick calculation showing it would nearly stop almost immediately given the high friction coefficient.

I need to tune the servo gains carefully—too high and the ram slams too violently, launching block1 on impact. Dialing down to kp=300 with damping=60 and mass 3kg gives a gentler initial force and capped velocity, which should produce a more controlled, realistic strike.

With d=0.13 the COM shifts 0.03 past the edge so toppling should still happen, and even with overshoot up to d=0.19 it stays under 0.2 so the stack still tips. I'm checking that floor friction under block1 (24.5N) is overcome by the 150N ram force, and that the weak block1-block2 friction (2N) won't meaningfully drag block2 during the brief impact. Now I just need to make sure the ram doesn't accidentally strike block2 itself.

Working through velocity dynamics: steady-state speed scales as kp*error/damping, giving ~2.4 m/s with kp=300, but at low kp the force near the target position is too weak to overcome the 26N static friction needed to actually push block1. This means I need a much higher kp (over 500, maybe 1000) to generate sufficient force near contact while still keeping approach speed reasonable.

I'm working out the ram's starting position and slide joint setup so the front face travels from -0.5 to around 0.03-0.06, giving the right stall distance of about 0.13. I'm also checking the ram's box geometry sits above the floor without gravity interference since it's a slide joint fixed in z.

Still writing the actuator and keyframe setup...

The stack of blocks with 0.1 friction should remain stable on its own, with the floor set to 1.0 friction and the geoms touching exactly at rest. I'm picturing the final scene: a sphere rolling rightward toward the block stack.

