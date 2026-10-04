I expect the original scene to fail. The stack stands at first and the pusher reaches `block1` at about 0.6 s. Shoving the loaded bottom block costs about 35 N of friction: about 19.6 N from the floor under the full stack and about 15.7 N from `block2` above it. Against that, the 3 kg pusher's 3.4 J of kinetic energy carries it only about 0.11 m. That is barely more than the block's 0.1 m width, so the push may stall with the stack still largely supported. Even if it gets the full 0.15 m, the pusher stops directly under where the stack stood. Its top is only 1 cm below the old support height, so the upper blocks can land on it. Its sudden stop then cancels the backward tilt the push gave them, and the stack could end up standing on the pusher.

The corrected file replaces the passive slider with a horizontal sweeping arm on a vertical hinge. A velocity motor drives it, and the keyframe sets its control and initial speed so it doesn't slow down under load. The stack settles for about 0.5 s. The head then hits the bottom block at about 1.5 m/s and carries it well out from under the stack. The arm stops at a joint limit away from the stack's footprint, so nothing is left under the falling blocks.

```json
{"what_happens": "The five-block stack stands for about 0.6 s. The 3 kg pusher hits block1 at 1.5 m/s, but about 35 N of friction from the floor and the stack above may stall it after only about 0.1 m, leaving the stack partly supported. If the pusher does reach its limit, it stops directly under the stack's footprint 1 cm below the old support height, so the upper blocks can land on it and stay upright.", "works": false, "problem": "The pusher has too little energy to reliably clear the loaded bottom block, and it ends up as a pedestal right where the stack falls."}
```

```xml
<mujoco model="five_block_stack_topple">
  <option timestep="0.002" gravity="0 0 -9.81" integrator="implicitfast"/>

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

    <body name="sweeper" pos="0 0.6 0.05">
      <joint name="sweep" type="hinge" axis="0 0 1" limited="true" range="-1.45 0.9" damping="0"/>
      <geom name="sweeper_arm" type="capsule" fromto="0 0 0 0 -0.55 0" size="0.02" mass="0.5" rgba="0.3 0.3 0.3 1"/>
      <geom name="sweeper_head" type="box" pos="0 -0.6 0" size="0.05 0.05 0.04" mass="2" friction="0.8 0.005 0.0001" rgba="0.2 0.2 0.2 1"/>
    </body>
  </worldbody>

  <actuator>
    <velocity name="sweep_motor" joint="sweep" kv="200" ctrllimited="true" ctrlrange="-5 5" forcelimited="true" forcerange="-80 80"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0 0 0.05 1 0 0 0  0 0 0.15 1 0 0 0  0 0 0.25 1 0 0 0  0 0 0.35 1 0 0 0  0 0 0.45 1 0 0 0  -1.4" qvel="0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  2.5" ctrl="2.5"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

Let me verify the geometry: pusher's front face travels from -0.95 to -0.95+1.05=0.10 at full range, pushing block1's back face from -0.05 to 0.10 — a 0.15 m displacement, which exceeds the block's own 0.1 m width.

Working through the dynamics, friction from the floor and from block2 resting on block1 decelerates the pusher+block1 system at roughly 10 m/s², so by the time it hits the travel limit the pusher is still moving around 1 m/s. After that, block1 keeps sliding ahead on its own, decelerating under floor friction while dragging block2 forward via friction at their interface, which is strong enough to exceed block2's tipping threshold — meaning the stack above would tip backward as its base gets pulled forward faster than its top.

Checking the tipping condition more carefully with sliding friction: since μ (0.8) is much greater than the width-to-height ratio (0.25), the friction force is enough to tip the stack regardless of the exact acceleration value.

The real sequence is that block1 sliding out from underneath means block2 loses support once the relative displacement exceeds about 0.1 m, so the upper stack likely drops and tumbles backward toward the pusher rather than cleanly tipping in place. I'm now working out where the pusher sits at its stroke limit to see if the falling blocks would land on or near it.

I'm tracing through the geometry over time: as block1 slides out from under block2, the support region shrinks, dragging block2 forward via friction while it starts tipping backward about its rear edge. It's getting complicated figuring out exactly how the contact area shifts as block1's trailing edge passes under block2.

I'm trying to work out whether the friction torque tips block2 forward or backward—when the pusher stops abruptly, the deceleration at the base could counteract the backward tipping tendency. Estimating the sliding friction impulse (~1.57 N·s over 0.1s) gives block2 a velocity around 0.78 m/s, and I'm now computing the angular impulse this produces about its center of mass to see which way it tips.

Comparing that angular impulse against gravity's restoring torque, the net effect seems small, giving a rotation of maybe a couple rad/s about the pivoting edge, and I'm checking this against the critical tipping angle of about 14 degrees.

Working through energy: the kinetic energy at that rotation rate about the edge exceeds the gravitational potential barrier to tip, so the toppling likely succeeds. But the upper blocks aren't glued together, so they'd slide and separate during this disturbance rather than staying rigid — meaning even if the bottom structure doesn't fully topple backward, the removal of block1 and the resulting tilt would still disrupt the stack significantly, with the top blocks likely falling or shifting out of alignment.

Since block1 slides faster than block2 after the pusher stops, their relative positions get messier, but the overall picture still points toward the stack toppling since the base support essentially vanishes. The pusher ending up under the stack feels like a design flaw that could accidentally prop things up—maybe a better design would give the pusher enough stroke to clear the block entirely before stopping.

Actually I'm reconsidering the landing position: with pusher stopped at [0,0.1] and block2 drifting forward roughly 4 cm from momentum, it could end up nearly centered on the pusher top rather than overhanging as I assumed, which complicates the toppling outcome I expected.

Given this uncertainty about whether the stack actually falls or stays balanced, I think the safer design choice is to make sure the pusher geometry doesn't end up directly under the stack at all, perhaps by changing the pusher's shape or sliding axis so it clears out from underneath after impact.

Maybe a pendulum still lands under the stack and drags it forward. I consider instead a horizontal rotating arm hinged about a vertical axis, sweeping sideways through block1 and continuing past quickly rather than lingering under the stack, so it knocks the block away without getting trapped beneath the falling pieces.

Maybe a spring-loaded pusher works better: a slide joint with stiffness and a springref sets it up like a ram that shoots forward, decelerates against the spring, reaches a peak excursion, then retracts automatically. I'm working out the amplitude needed so it travels roughly 0.2 into the stack before springing back.

Maybe a horizontal sweeping hinge works better — pivoting about the vertical axis at a fixed low height so the arm never rises into the stack, just sweeps through block1's position. I'd need a joint limit or damping so it stops after one pass instead of spinning forever.

Checking that line clears the stack footprint — looks okay but the geometry is getting messy since the arm capsule itself sweeps through the block area. I'm reconsidering a simpler linear pusher with spring retraction, but realize the timing still causes it to drag the stack forward then backward during retraction, which is counterproductive. I need the pusher's resting position to not sit under the stack at all.

Thinking about whether a short, hard strike (0.06m stroke at 1.5 m/s, ~0.04s duration) could topple the stack via friction alone — probably not enough time even with high friction (μ=1.0, ~19.6N), since tipping requires sustained acceleration, not just a brief impulse.

Instead I'm pivoting to a different design: a hinged sweeping arm ("hammer") rotating about the z-axis, with a capsule geometry forming the arm and head, positioned so the head starts offset from the stack and swings into it — I'm working out the pivot position and initial rotation angle needed for the head to strike correctly.

I'm tracing the arm's sweep path more carefully: the head crosses the stack's footprint right at θ=0, but as it continues to larger angles it moves away from the origin region, so I'm checking the closest approach distance from the swept line to the stack to see whether contact actually occurs beyond that initial pass.

I should also set the hinge joint limits to roughly -0.8 to 0.9 radians, with the starting position near the lower edge, and estimate timing: at an angular velocity of about 2.5 rad/s, the head would take roughly 0.23 seconds to swing from its start to first make contact with block1.

To give the stack time to settle before impact, I'm widening the sweep further back, say to around -1.4 to -1.5 radians, which pushes contact time out to about 0.5 seconds. I'm also checking the direction block1 gets pushed—since the head's tangential motion near the contact angle points mostly in the +x direction with a slight +y component, that should knock block1 out from under the stack rather than straight up into it.

Working through the torque, though, a 3 kg head at 0.6 m radius with angular velocity 2.5 rad/s gives decent momentum, but if the resistance from the stack creates too much angular deceleration, the hammer could lose most of its speed before even completing the swing—so I need to make sure the head is heavy enough to punch through.

Working through the stall calculation, block1 likely only moves about 0.11 m before stopping, which confirms the original pusher design is unreliable. I should mark it as not working and switch to a more robust approach: a velocity-controlled motor actuator on the slide that maintains constant speed regardless of load, rather than relying on a passive linear pusher.

For the hinge sweeper alternative, a constant angular velocity actuator would keep rotating and sweep back through fallen debris every rotation period, which is messy but could be stopped using a hinge range limit with force-limited control so the motor pushes against the stop safely.

A heavy hammer at 20 kg gives plenty of kinetic energy to slam block1 forward on impact, which works fine passively. Still, I lean toward a velocity-actuated sweeper for determinism, so I'm defining a velocity actuator on the sweep joint with gain and force range limits.

I'm checking torque requirements against the actuator's force range and confirming the gain-to-inertia ratio stays stable at the chosen timestep, and I'll switch to the implicitfast integrator to be extra safe given the velocity actuator's stiffness.

Now I'm questioning whether a joint limit is even needed — if the arm sweeps freely through a full rotation, I need to trace where the head ends up at various angles to make sure it doesn't collide with anything unexpected along the way.

I'm checking the geometry clearances: the head box sits above the floor and below block2's bottom, so it clears both. I'm defining the hammer body's arm capsule and head box dimensions relative to the pivot to make sure the sizes and offsets line up correctly.

Then I'm verifying the pivot hinge is correctly anchored to the world and that the swinging head's front face strikes block1's side squarely as it sweeps through its arc, checking the alignment at the contact angle.

As the head rotates, its face normal shifts from +x toward +y, carrying block1 along the swing via friction until the sweeper halts near θ=0.9, by which point block1 has been pushed roughly 0.6 m clear of the stack—well off its original footprint within about 0.43 seconds of contact.

Checking whether the arm itself stays clear of the stack region as it sweeps through, I'm tracking the capsule's position at small angles against the stack's x-span, accounting for a few centimeters of forward drift on block2.

Then I turn to the real question — whether the upper stack topples sideways or drops straight down and stays standing once block1 is yanked out fast enough, essentially testing a tablecloth-pull scenario.

As block1's rear edge slides beneath block2's COM, block2 starts pivoting backward on that moving edge, with gravity torque adding to the tilt while its rear is unsupported. Given this backward rotation building up against the forward-sliding tendency, and the stack's tall 4:1 aspect ratio falling 0.1 m, it seems more likely than not that the tower topples backward on landing, though the competing forward slip makes this uncertain.

I'm also second-guessing the push speed: a slow constant-velocity pull would just drag block1 along with the rest via static friction, causing the whole stack to slide together without tipping — so the removal needs to be fast enough, more like a tablecloth-trick impulse, to actually induce the toppling I'm predicting.

Trying to pin down the net tipping direction: during the brief contact, friction torque about the center of mass tends to tip the stack backward (requiring μ above roughly 0.25), and the loss of support underneath also tips it backward, while the forward slide on landing afterward tends to tip it forward. I'm roughly estimating the angular impulse from friction versus the counteracting gravity torque to see which effect wins and get a rough angular velocity for the stack.

Recovering from that tilt would need a strong forward angular velocity, which isn't there, so it topples—and since the stack isn't rigid, the upper blocks lag behind and lean back even further, reinforcing that conclusion. The sweeper arm has already moved away from that region by the time the stack falls, so it's not a factor.

Checking the impact dynamics: the motor's force limit and hammer inertia are sufficient to accelerate block1 to the needed velocity, and floor friction alone would be enough to keep pushing it afterward. The stack settles within half a second initially, and I'm tracking the sweeper head's position starting from its initial angle.

I'm also verifying the joint range, velocity limits, and actuator ctrl range for the sweep motor, confirming qpos/qvel ordering with blocks before the hammer hinge, and checking that the hammer head and arm geoms sit high enough off the floor to avoid unwanted contact.

Since the hammer's parent body is the world, MuJoCo automatically filters out parent-child contacts, so the floor-hammer collision is excluded regardless. I'll finalize the integrator as implicitfast, name the light, and write out the file.

