Contact happens, but the stack never topples.

**What the picture shows.** The sphere rolls from x ≈ -1.2 m along the floor and reaches the bottom block at about x ≈ -0.1 m. The five-block column stays upright the whole time. Its top stays near z ≈ 1.0 m, and it shifts only a few centimetres in +x. Nothing falls in the 1.91 s the residue covers.

**Why it fails.** The rolling ball's push is short and goes through the bottom block's centre. That either slides the stack a little or slips block1 under the blocks above, and neither tips the column.

**The fix.** I replaced the ball with a ram on a slide joint, driven by a constant 22 N motor force that the keyframe sets. The ram starts touching block1. These figures are hand estimates; I have not re-run the scene.

- **Push phase.** About 7.3 N is left after floor friction, so the whole stack speeds up together at about 1.6 m/s². That is below the roughly 2.45 m/s² at which the upper four blocks would tip backward, so the stack stays upright while it is pushed.
- **Stop.** The ram hits its joint limit after 0.5 m, at about 1.27 m/s. Block1 then slows on floor friction at up to about 5.9 m/s².
- **Topple.** That deceleration is well above the forward tipping threshold, so the stack should tip forward over block1's front edge.

```json
{"what_happens": "The pusher sphere rolls along the floor from x≈-1.2 and reaches the bottom block, but the five-block column only shifts a few centimetres in +x and stays upright with its top near z≈1.0 m; nothing topples during the run.", "works": false, "problem": "The rolling ball gives the bottom block only a brief push through its centre, which slides the stack slightly instead of making it topple."}
```

```xml
<mujoco model="stack_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="6 6 0.1" friction="0.6 0.005 0.0001"/>
    <body name="block1" pos="0 0 0.100">
      <freejoint/>
      <geom name="block1" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block2" pos="0 0 0.300">
      <freejoint/>
      <geom name="block2" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block3" pos="0 0 0.500">
      <freejoint/>
      <geom name="block3" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block4" pos="0 0 0.700">
      <freejoint/>
      <geom name="block4" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block5" pos="0 0 0.900">
      <freejoint/>
      <geom name="block5" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="pusher" pos="-0.151 0 0.1">
      <joint name="pusher_slide" type="slide" axis="1 0 0" limited="true" range="0 0.5" damping="0"/>
      <geom name="pusher" type="box" size="0.05 0.1 0.08" mass="2.0" friction="0.3 0.005 0.0001"/>
    </body>
  </worldbody>
  <actuator>
    <motor name="pusher_motor" joint="pusher_slide" gear="1" ctrllimited="true" ctrlrange="0 30"/>
  </actuator>
  <keyframe>
    <key name="start" qpos="0 0 0.100 1 0 0 0  0 0 0.300 1 0 0 0  0 0 0.500 1 0 0 0  0 0 0.700 1 0 0 0  0 0 0.900 1 0 0 0  0" qvel="0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0" ctrl="22"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm visualizing the scene: the pusher sphere rolls from x=-1.2 toward the stack, leaving a trail of copies in both the side and plan views, while the stack stays vertical and doesn't topple within the 1.91s window shown. I'm working out whether the sphere, starting 1.2m away and needing to cover roughly a meter at 1.5 m/s minus rolling friction, actually reaches the stack in that time.

The sphere's center sits at a height that matches the bottom block's center, so contact pushes the block sideways rather than tipping it — but since nothing topples, I need to rework the collision so the bottom block gets knocked out fast enough to collapse the upper stack.

I'm working through the physics: a slow push just slides the whole stack together due to friction, while a sharp kick out could pull the base away leaving the upper blocks to fall, though that might just drop them flat rather than toppling. I'm calculating the acceleration threshold where the base sliding out faster than the interface friction can hold causes the upper stack's center of mass to tip relative to the bottom block.

Maybe a more reliable approach is using a slide-joint ram with a position actuator that pushes block1 a fixed distance quickly and then stops. The sudden stop lets the upper stack's momentum carry it forward, tipping it over the front edge if there's enough kinetic energy to raise the COM past the tipping point — this seems more controllable than relying on friction-impulse transfer alone.

I'm working through the physics: pivoting about the front top edge of block1 requires raising the upper stack's COM by about 0.0123 m, computing the moment of inertia about that pivot, and checking whether the angular momentum from the sudden stop generates enough kinetic energy to clear that threshold.

But I'm reconsidering since the stack isn't rigid — block1 decelerates on the floor via friction while the upper blocks only feel friction transmitted from block1's top surface, so I'm comparing the required deceleration against what friction can actually provide to see if tipping occurs.

The impulse passes through block1's center, so block1 likely slips out from under while the upper blocks get a forward friction kick at their base, which would tend to tilt them backward. But the image still shows things roughly vertical, so maybe the contact just hasn't had time to topple anything by 1.91s—I'm trying to pin down exactly where the sphere's trail ends in the image to check this.

Working through the pixel-to-meter conversion, I'm figuring out the scale factor (around 60.4 px/m) to map the sphere trail's pixel positions back to real coordinates, since the column's expected position is x=-0.1 to 0.1 and I want to see how far things have shifted.

Checking the column top height, it seems the stack didn't topple over—it just slid a bit, which isn't what I wanted. I need a design fix to guarantee a toppling motion: pushing the bottom block hard enough that friction with the floor causes deceleration that tips the stack forward, while making sure the impact doesn't just cause slipping or backward tipping instead.

Checking tipping thresholds per block level: the top block alone slides rather than tips since its threshold exceeds floor friction, but the upper two blocks together have a lower threshold of 4.9, below the 5.9 deceleration, so they tip forward. The whole stack tilts and topples once moving fast enough, needing roughly v ≥ 1.5 m/s or so to tip over rigidly.

A simpler approach without an actuator: use a sliding-joint pusher with large mass hitting block1 at that velocity — but this creates a harsh impulse since contacts are soft with a short time constant, giving accelerations far too high. Instead I should drive the pusher with a velocity-controlled motor whose control signal is set by the keyframe, using a rigid ram body to apply a gentler push.

I'm working out that with a ram mass around 5 kg plus a 2.5 kg stack, I need roughly 11 N of force for the target acceleration, so a velocity servo with ctrl 1.5 and kv=8 gives an initial force near that, decaying with a time constant around 0.94 s as speed builds. The ram then hits a joint limit around 0.6 m of travel and stops abruptly, letting the block and stack continue forward at about 1.2 m/s while friction decelerates the base block, causing the stack to tip forward.

Wait, I realize floor friction of about 14.7 N opposes the push, so 12 N alone won't even start the block moving — I need the motor force to exceed roughly 26 N to overcome friction plus accelerate the mass. I consider keeping friction at μ=0.6 rather than lowering it, since that's what drives the tipping deceleration, and I think about switching to a constant-force actuator instead, computing net acceleration from a 28 N force minus the 14.7 N friction.

Testing different ram masses with F=24 N, settling on 2 kg giving about 2.07 m/s² acceleration, which seems reasonable. I'm also working out how the ram should move before contacting the block — floating on a slide joint without floor contact, starting nearly touching block1 with a tiny initial gap, and calculating the travel distance needed to reach the target velocity.

Now I'm figuring out the speed when the ram hits its travel limit (around 1.29 m/s at 0.4 m), then thinking through what happens after separation — how far block1 slides before stopping under deceleration, and whether that deceleration is enough to tip the stack forward, comparing the rigid sudden-stop case against a more gradual dynamic tipping analysis.

Checking the backward tilt during acceleration stays under threshold, and that block1 friction torque with the floor is fine given full weight. With force at 22N, acceleration comes out to 1.62 m/s², giving travel time around 0.78s, which seems workable — maybe I should add a small gap before the ram starts pushing.

Actually a 0.15m gap causes the ram to hit at 1.8 m/s, which is too fast and would cause an impact rather than a gentle push. I think starting the ram already in contact is simpler, even if it means the "stands until pushed" moment is brief — or I could use a velocity servo to make the ram cruise slowly toward the block for a gentler approach.

Setting up the joint limits and geometry now: defining the slide joint range, positioning the ram's box geometry so its face is flush against the stack without clipping into the floor, and making sure the body position and collision geometry stay consistent.

The ram's mass and friction need to interact properly with the blocks, so I'm setting a low friction coefficient and a motor actuator driving the slide joint with a bounded control range, then adding a keyframe control value. I also need to account for the extra slide joint's qpos and qvel entries in the overall state vector, appending one more value to each since this joint is added after the block bodies.

Thinking about the dynamics further, I expect the step-function motor force could cause some transient contact oscillation at t=0, but that's an acceptable risk given the toppling threshold margins are comfortable. Time to finalize and write the file.

