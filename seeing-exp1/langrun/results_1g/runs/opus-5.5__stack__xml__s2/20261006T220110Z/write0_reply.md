The pusher is a low paddle on a slide joint. A velocity motor drives it at 0.5 m/s, and the keyframe sets its control. It starts 0.5 m behind the stack, so the stack stands for about a second before the paddle reaches the bottom block. The bottom block has low friction and wins the friction choice through `priority`. That lets the paddle shove it out from under the stack without dragging the stack along. Once the block has moved about half its width, the four blocks above it lose support and topple backward onto the floor. I haven't run this, so the expectations below are predictions.

```xml
<mujoco model="block_stack_topple">
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="3 3 0.1" friction="0.6 0.005 0.0001" rgba="0.8 0.8 0.8 1"/>

    <body name="pusher" pos="-0.6 0 0.025">
      <joint name="pusher_slide" type="slide" axis="1 0 0" damping="0"/>
      <geom name="pusher_paddle" type="box" size="0.05 0.08 0.02" mass="2" friction="0.6 0.005 0.0001" rgba="0.2 0.3 0.8 1"/>
    </body>

    <body name="block1" pos="0 0 0.05">
      <freejoint name="block1_free"/>
      <geom name="block1_geom" type="box" size="0.05 0.05 0.05" mass="0.3" friction="0.05 0.005 0.0001" priority="1" rgba="0.9 0.2 0.2 1"/>
    </body>
    <body name="block2" pos="0 0 0.15">
      <freejoint name="block2_free"/>
      <geom name="block2_geom" type="box" size="0.05 0.05 0.05" mass="0.3" friction="0.6 0.005 0.0001" rgba="0.9 0.6 0.2 1"/>
    </body>
    <body name="block3" pos="0 0 0.25">
      <freejoint name="block3_free"/>
      <geom name="block3_geom" type="box" size="0.05 0.05 0.05" mass="0.3" friction="0.6 0.005 0.0001" rgba="0.9 0.9 0.2 1"/>
    </body>
    <body name="block4" pos="0 0 0.35">
      <freejoint name="block4_free"/>
      <geom name="block4_geom" type="box" size="0.05 0.05 0.05" mass="0.3" friction="0.6 0.005 0.0001" rgba="0.2 0.8 0.3 1"/>
    </body>
    <body name="block5" pos="0 0 0.45">
      <freejoint name="block5_free"/>
      <geom name="block5_geom" type="box" size="0.05 0.05 0.05" mass="0.3" friction="0.6 0.005 0.0001" rgba="0.6 0.3 0.9 1"/>
    </body>
  </worldbody>

  <actuator>
    <velocity name="pusher_drive" joint="pusher_slide" kv="200" ctrlrange="-1 1" ctrllimited="true"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0  0 0 0.05 1 0 0 0  0 0 0.15 1 0 0 0  0 0 0.25 1 0 0 0  0 0 0.35 1 0 0 0  0 0 0.45 1 0 0 0" qvel="0.5  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0" ctrl="0.5"/>
  </keyframe>
</mujoco>
```

```expect
pusher touches block1
block5 touches floor
block4 touches floor
block5 comes to rest
```

---
thinking (summarized):

I'm planning a scene with a stack of five 0.1m cube blocks that stands until a pusher body, starting about 0.3m away, moves in and strikes the bottom block, causing the stack to topple as the lower block gets knocked out from under the upper ones.

I'm weighing options for the pusher: using a slide joint along x so it doesn't interact vertically with the floor, giving it decent mass and a moderate velocity so it knocks the bottom block out convincingly rather than just dragging the whole stack together via friction, which would prevent a proper toppling effect.

Actually a cleaner topple: if the pusher moves block1 just partway, say 0.06 m, the support under the stack above shifts enough that the combined center of mass falls outside block1's footprint, tipping the stack toward -x and causing a clean fall rather than a slow slide. I need to watch out for friction dragging block2 along with block1, which would undermine this effect, so maybe lower friction between block1 and block2 helps preserve the toppling motion.

Working through the physics: block1 slides roughly 0.16m before it's fully clear, at which point the stack above starts to lose support. The remaining blocks get dragged a bit by friction but at low acceleration, so the key question becomes whether block1 moves out far enough relative to the support edge for the stack to start tipping before momentum from the drag settles out.

I'm not fully certain it'll topple cleanly, so I'm considering tweaking block dimensions to make the stack narrower and less stable, or trying a slow sustained push instead—using a velocity actuator on block1 with low friction against block2 so the upper blocks barely get dragged along while block1 slides out from under them.

Let me try concrete numbers: blocks as 0.1 cube, density 300 giving mass 0.3 kg each, pusher mass 3 kg moving at 1.0 m/s with no damping so it keeps shoving block1 forward. That drags the upper stack via friction, giving block2's base a horizontal kick while the top lags behind, producing a tilt before the stack goes into free fall off the edge — I'm weighing whether this geometry actually causes toppling once it lands.

Actually since friction scales with weight above, the whole stack moves rigidly at mu*g rather than slipping internally. But that base friction also creates a torque about the stack's center of mass, and with mu=0.5 the torque exceeds the stabilizing moment from the stack's width (threshold mu>0.25), so the stack tips backward during the push, falling toward the pusher's original side after about 0.1 m of displacement.

I'm reconsidering the pusher geometry instead — positioning it so its slide joint range only allows block1 to be shoved about 0.1 m, just enough to clear it fully out from under the upper blocks, rather than relying on toppling dynamics.

I'll set the limit so the pusher clears block1 fully, keeping it low and thin so the toppling stack tumbles over it rather than resting on it. For the test expectations, I need contacts like block1-pusher and eventually block5 hitting the floor and coming to rest, with floor friction bringing the fallen blocks to a stop fairly quickly.

Checking the timing: with the pusher moving at 0.8 m/s and the stack accelerating at 5 due to the push, the relative displacement needed to clear block1 (0.1 m) works out to about t=0.16s.

I'm realizing that at this exact time the velocities actually equalize, which means slip stops and the stack just rides along with no torque to tip it — not what I want. So I need a faster pusher speed, like 2 m/s, which gives a shorter contact time (~0.056s) and leaves the upper stack still slower than the pusher, preserving relative sliding and the torque needed for tipping about the rear bottom edge of block2.

Trying an intermediate speed around 1.2 m/s instead, solving for when relative displacement hits the critical 0.1m threshold gives t≈0.107s and upper velocity ≈0.54 m/s. I'm now setting up the rigid-body tipping condition: treating the four-block stack as a rigid box of dimensions 0.1×0.1×0.4, computing its moment of inertia about the center of mass to relate the friction-driven torque to angular acceleration.

Working through the torque balance, the normal force shifts toward the trailing edge, giving a restoring moment, and the net tipping torque comes out to roughly 0.05Mg once the edge becomes the pivot. Using parallel-axis corrections I get α≈8.6 rad/s², which after 0.1s yields ω≈0.86 rad/s and a tilt of about 0.043 rad, growing further during the fall phase under gravity's own torque to around 0.16 rad by landing — with the stack rotating backward while its base still carries forward momentum from the push.

But now landing complicates things: friction suddenly stops the base's horizontal motion, while the upper blocks still carry forward momentum, so instead of tipping backward it may actually tip forward at impact. Since each block is loose rather than rigidly attached, I need to think about this as individual blocks sliding relative to each other under their own friction limits rather than one rigid body, which changes the whole tipping analysis.

Maybe a cleaner design: have the pusher move slowly with low friction so block1 gradually slides out from under the stack, letting the upper blocks start tipping backward over the edge of block1 as it keeps moving forward.

I'm working out the pusher geometry and motion—keeping it short in length and driven at constant velocity, so the timing of when it reaches block1 lines up with where the falling stack lands around x≈-0.4. I'm also thinking through the friction priority system: since block1 has higher priority with friction 0.1, that value governs contact with the floor, block2, and the pusher, which determines the resisting force the pusher must overcome.

I'm checking whether the upper stack's friction-driven drag will cause it to catch up with the lower blocks too soon, and testing lower friction values to make sure the relative displacement timing works out correctly before contact occurs.

Switching to a faster pusher speed of 0.5 m/s with block1 friction at 0.05 gives a sufficient relative displacement margin, and this direction also helps tilt the stack backward consistently. I'll set the pusher starting 0.5 m away so contact happens at 1 s, then keep it moving afterward to see how block1 behaves once pushed, given the floor is nearly frictionless.

I should check whether the falling stack lands on the pusher itself, since the pusher sits low and moves forward while the stack falls backward — but with block5 landing around x≈-0.4 and the pusher occupying a region near x≈0 to 0.1 at that time, they shouldn't actually collide.

For the pusher-block1 contact, since the push force is applied below block1's center of mass, it shouldn't create a forward tipping moment, so friction at the floor stays negligible. I'm also setting up a velocity actuator for the pusher joint with kv=200, giving a fast time constant relative to the small load force, and considering giving the pusher an initial velocity to start the motion.

Now I'm working out the keyframe layout: 36 qpos values (five freejoint blocks at 7 each plus one slide joint), 31 qvel values, and a single ctrl value of 0.5. I'm stacking the blocks vertically with z-positions spaced 0.1 apart starting at 0.05, letting them rest exactly touching since zero initial penetration settles fine in MuJoCo, and placing the pusher body off to the side with its box geometry.

With the pusher at -0.6 and its front face at -0.55, there's a 0.5 gap to block1's rear face, so contact happens around t=1s given the slide axis along x. I'm checking that the pusher stays purely horizontal (no vertical motion from gravity since it's a slide joint), and that after it strikes block1, the stack's center of mass shifts past the rear edge causing block2 to tip backward — with low friction at the contact edge, block2's base should slip forward as the top falls, eventually sliding off the back edge of block1 onto the floor.

I expect the upper blocks (2-5) to topple and eventually settle on the floor, with contacts like "pusher touches block1" and "block5 comes to rest" worth noting, while making sure block1 itself (still being pushed) doesn't count as "at rest" since it keeps moving with the pusher. Now I'm writing the MJCF XML, making sure every body, geom, and other element has a unique name, with attributes kept on a single line per the formatting requirement.

Setting block1's friction very low with high priority so it slides easily under the pusher, while giving the other blocks, floor, and pusher higher friction (0.6) so they interact normally and block1 dominates only in its direct contact with the pusher. I'm also setting a reasonable mass for the block geoms and leaving the solver settings at their defaults.

