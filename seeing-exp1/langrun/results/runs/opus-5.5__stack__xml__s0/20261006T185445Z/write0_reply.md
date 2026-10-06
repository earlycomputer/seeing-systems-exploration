A slider-mounted pusher creeps toward the stack under a velocity motor. It reaches the bottom block at about t = 1.0 s and pushes it near its top edge. The floor's high friction keeps the base from simply sliding out, so the whole column tips about the bottom block's front edge and falls away from the pusher. The pusher–block contact is nearly frictionless so it doesn't hold the block down.

```xml
<mujoco model="toppling_stack">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <camera name="side" pos="0.2 -1.6 0.4" xyaxes="1 0 0 0 0.25 1"/>
    <geom name="floor" type="plane" size="3 3 0.1" friction="1 0.005 0.0001" rgba="0.8 0.8 0.8 1"/>

    <body name="pusher" pos="-0.32 0 0.08">
      <joint name="push_slide" type="slide" axis="1 0 0" limited="true" range="0 0.35" damping="0"/>
      <geom name="pusher_head" type="box" size="0.02 0.06 0.015" mass="1" contype="0" conaffinity="0" rgba="0.8 0.2 0.2 1"/>
    </body>

    <body name="block1" pos="0 0 0.05">
      <freejoint name="block1_free"/>
      <geom name="block1_geom" type="box" size="0.05 0.05 0.05" density="500" friction="1 0.005 0.0001" rgba="0.2 0.4 0.8 1"/>
    </body>
    <body name="block2" pos="0 0 0.15">
      <freejoint name="block2_free"/>
      <geom name="block2_geom" type="box" size="0.05 0.05 0.05" density="500" friction="1 0.005 0.0001" rgba="0.2 0.7 0.4 1"/>
    </body>
    <body name="block3" pos="0 0 0.25">
      <freejoint name="block3_free"/>
      <geom name="block3_geom" type="box" size="0.05 0.05 0.05" density="500" friction="1 0.005 0.0001" rgba="0.9 0.7 0.2 1"/>
    </body>
    <body name="block4" pos="0 0 0.35">
      <freejoint name="block4_free"/>
      <geom name="block4_geom" type="box" size="0.05 0.05 0.05" density="500" friction="1 0.005 0.0001" rgba="0.6 0.3 0.7 1"/>
    </body>
    <body name="block5" pos="0 0 0.45">
      <freejoint name="block5_free"/>
      <geom name="block5_geom" type="box" size="0.05 0.05 0.05" density="500" friction="1 0.005 0.0001" rgba="0.9 0.4 0.3 1"/>
    </body>
  </worldbody>

  <contact>
    <pair name="pusher_block1" geom1="pusher_head" geom2="block1_geom" condim="3" friction="0.02 0.02 0.005 0.0001 0.0001"/>
  </contact>

  <actuator>
    <velocity name="push_motor" joint="push_slide" kv="200" forcelimited="true" forcerange="-100 100"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0  0 0 0.05 1 0 0 0  0 0 0.15 1 0 0 0  0 0 0.25 1 0 0 0  0 0 0.35 1 0 0 0  0 0 0.45 1 0 0 0" qvel="0.25  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0" ctrl="0.25"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need to design a toppling scene: a stack of five blocks standing, then something pushes the bottom one to start the chain reaction. I'm weighing options — a slider pusher with keyframed velocity starting after the stack settles, versus a pendulum or hammer released by gravity to strike the stack.

The trickier physics question is whether pushing the bottom block actually topples the stack rather than just shooting it free while the upper blocks drop cleanly back down. I'm reasoning through friction at each block interface — a fast push might just eject the bottom block without tipping the rest, while a moderate push creates enough lag in the upper blocks' inertia to make them tilt backward and fall, which is the toppling behavior I actually want.

Once steady pushing begins at constant velocity, there's no more acceleration to topple anything, so the stack just rides along with a slight wobble rather than falling. I'm reconsidering the approach — maybe pushing the bottom block in a way that induces rotation, or pushing partway through so the stack loses support, would be more effective at causing an actual fall.

If d exceeds half the block width, the upper stack would pivot off the trailing edge and topple back toward the pusher, which gets messy since the pusher sits at floor level. Really what's needed is for the bottom block to slide out fast enough that friction can't drag the upper blocks along with it — but since MuJoCo contact friction takes the max of the two geoms' coefficients by default, I can't just lower friction between the blocks without also affecting the floor contact.

So maybe a cleaner approach: use a pendulum hammer to strike block1 hard, letting it shoot out and the stack drop the 0.1m gap — though it's unclear whether block2 picks up backward rotation from the friction impulse at its base. Alternatively, I could use a position actuator for the pusher with a limited stroke, setting a keyframe control target so block1 ends up displaced exactly 0.08m.

I'm weighing damped position control versus a velocity actuator with a joint range limit — the velocity approach seems cleaner: pusher creeps at a constant 0.2 m/s until contact at t=1s, nudges block1 forward 0.08m over 0.4s, then stops at the joint limit, giving a clean delayed push without overshoot.

Checking the faster push case: at 1 m/s stroke, the upper stack barely moves while block1 slides out 0.077 m relative, exceeding the 0.05 half-width — so the stack's COM passes the trailing edge and it topples backward off block1. Then I need to consider what happens after the pusher stops, since block1 keeps sliding on the floor under friction deceleration.

I'm also questioning whether a different push location — contacting block1 higher up rather than at floor level — would produce a forward toppling instead, which feels more like the classic setup for this kind of problem.

Once tilted past about 11 degrees, the center of mass passes the pivot and gravity takes over to topple it, so I just need tipping to dominate over sliding — with floor friction around 1, the tipping threshold of roughly 0.625·mg is comfortably lower than the sliding threshold, so the block tips rather than slides. I'll position the pusher's contact face to span the upper portion of block1's height, around z=0.06 to 0.10, to apply the push near the top for better leverage.

I'll keep the pusher off the ground via its slide joint (gravity resisted by the joint, no floor collision since it sits above z=0.065), moving at a steady 0.4 m/s with a stroke range limiting how far it travels so it doesn't push indefinitely.

Working through the geometry, tilting the tower by roughly 11° only requires about 0.017 m of horizontal displacement at the contact height, since the rotation happens about the front edge — so a 0.06 m stroke after contact gives plenty of margin even as the contact point slides along the back face during rotation.

I'm also considering whether block1 might just slide instead of tip: with an impulsive impact from the pusher at 0.4 m/s, the momentary force at the floor could exceed the friction limit even with mu=1, so some sliding is plausible alongside tipping. I think dialing back to a gentler speed like 0.25 m/s and checking the torque balance about the front edge would clarify whether tipping still dominates despite the floor friction being momentarily overwhelmed.

So it topples away from the pusher direction. I need to check whether the pusher, which only spans the lower height range and acts on block1, might also end up contacting block2 as the tower rotates — since block2's back face is coplanar with block1's, a point on that shared face at the pusher's height stays on block1 initially, but I should verify the geometry doesn't let the pusher catch block2's edge once rotation begins.

I'll cap the pusher's force using forcerange, something like ±50 N, since the tower's weight is roughly 24.5 N and the force needed to tip it is only around 15 N given the geometry.

For the velocity actuator, I'm picking a gain so the pusher reaches its target speed almost instantly, around a 5 ms time constant with a 1 kg pusher mass, making sure it doesn't collide with the floor but does collide with the blocks.

I'm positioning the pusher's starting gap so it begins about 0.32 m back from the block, which at 0.25 m/s means contact happens roughly one second into the simulation.

For the joint range, I'm capping travel around 0.33-0.35 m — enough to tip the tower after contact and let it fall forward, while checking that the pusher's final position doesn't collide with the fallen blocks, which end up rotated and offset further in x.

Now I'm setting up the stack geometry with blocks centered at 0.1 m intervals, relying on default friction and contact solver settings so the stack stays stable at rest. I'm working out the keyframe's qpos/qvel vectors — accounting for the pusher's one slide DOF plus each block's seven-dimensional free joint — and giving the pusher an initial velocity via ctrl to kick off the motion.

I want to confirm the tipping check holds: contact height around 0.08 against a block face spanning roughly 0.065–0.095 gives an effective torque ratio near 0.625, well under the friction coefficient of 1, so sliding shouldn't dominate over tipping. I'm also considering lowering the pusher's friction so it doesn't drag the block vertically during contact, since MuJoCo takes the max of geom frictions for a given contact pair.

Actually I realize the friction coupling could backfire: if the pusher can't move vertically, friction at the back contact point as the block tips would create a downward force that opposes the tipping torque, potentially canceling the push entirely. So I need the pusher-block friction to be very low, which means using an explicit contact pair override rather than relying on the default max-friction rule.

I should set pusher's contype/conaffinity to 0 so it only interacts via explicit pairs, avoiding duplicate dynamic contacts. That means I'd need a separate explicit pair for each geom the pusher should still collide with, though since this is just about pushing the bottom block, a single pair for block1 should suffice.

For the pusher body, I'll use a slide joint along the x-axis with limited range, a small box geom with mass, and skip adding a visual rail since it's unnecessary. Now I just need to finish with lighting, camera setup, and write out the full file.

