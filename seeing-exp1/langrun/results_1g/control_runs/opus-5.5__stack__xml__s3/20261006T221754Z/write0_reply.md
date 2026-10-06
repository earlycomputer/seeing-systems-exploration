The pusher is a slider driven by a velocity servo. The keyframe sets its speed to 0.8 m/s. It closes a 0.30 m gap, so the five-block stack stands untouched for about 0.4 s. The pusher then shoves `block1` 0.30 m further and stops at its joint limit.

I have not run this file. That the stack topples rests on a rough hand calculation:

- With friction 0.6 between blocks, the four upper blocks should take about 0.14 s to reach the bottom block's speed.
- In that time `block1` should slide about 5 cm out from under them. That is roughly as far as the stack's centre of mass can shift before passing the support edge.
- The sudden drag on their base should also start the upper stack tipping backward.

The margins are moderate, so the direction and timing of the fall may differ from this estimate. The likely failure is the upper stack riding along on `block1` and staying upright. In that case, raising the block-on-block friction or the push speed should help.

```xml
<mujoco model="toppling_stack">
  <option timestep="0.002" integrator="implicitfast" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" friction="0.6 0.005 0.0001" rgba="0.8 0.8 0.8 1"/>

    <body name="block1" pos="0 0 0.05">
      <freejoint name="block1_free"/>
      <geom name="block1_geom" type="box" size="0.05 0.05 0.05" density="500" friction="0.6 0.005 0.0001" rgba="0.8 0.2 0.2 1"/>
    </body>
    <body name="block2" pos="0 0 0.15">
      <freejoint name="block2_free"/>
      <geom name="block2_geom" type="box" size="0.05 0.05 0.05" density="500" friction="0.6 0.005 0.0001" rgba="0.9 0.6 0.1 1"/>
    </body>
    <body name="block3" pos="0 0 0.25">
      <freejoint name="block3_free"/>
      <geom name="block3_geom" type="box" size="0.05 0.05 0.05" density="500" friction="0.6 0.005 0.0001" rgba="0.9 0.9 0.2 1"/>
    </body>
    <body name="block4" pos="0 0 0.35">
      <freejoint name="block4_free"/>
      <geom name="block4_geom" type="box" size="0.05 0.05 0.05" density="500" friction="0.6 0.005 0.0001" rgba="0.2 0.7 0.3 1"/>
    </body>
    <body name="block5" pos="0 0 0.45">
      <freejoint name="block5_free"/>
      <geom name="block5_geom" type="box" size="0.05 0.05 0.05" density="500" friction="0.6 0.005 0.0001" rgba="0.2 0.4 0.9 1"/>
    </body>

    <body name="pusher" pos="-0.34 0 0.045">
      <joint name="pusher_slide" type="slide" axis="1 0 0" range="0 0.6" limited="true"/>
      <geom name="pusher_geom" type="box" size="0.04 0.1 0.035" mass="3" friction="0.3 0.005 0.0001" rgba="0.3 0.3 0.3 1"/>
    </body>
  </worldbody>

  <actuator>
    <velocity name="push" joint="pusher_slide" kv="400" ctrlrange="0 2" ctrllimited="true" forcerange="-300 300" forcelimited="true"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0 0 0.05 1 0 0 0  0 0 0.15 1 0 0 0  0 0 0.25 1 0 0 0  0 0 0.35 1 0 0 0  0 0 0.45 1 0 0 0  0" ctrl="0.8"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm planning a scene with a stack of five blocks that stays stable until a pusher body, driven by a slide joint with constant velocity, knocks out the bottom block and topples the stack.

For the toppling physics, I need the pusher to strike the bottom block abruptly enough that its sudden acceleration lags the upper blocks' inertia, causing the tower to tip toward the pusher rather than sliding as a unit.

I'm weighing whether a slow push just slides the whole stack together without toppling, versus a fast knockout that risks the "tablecloth trick" where the tower drops but stays upright. A moderate speed around 0.8 m/s combined with higher block-to-block friction seems like the better balance to actually produce a topple.

Thinking through the dynamics: the pusher forces block1 to nearly instantly match its velocity, and friction from block1 transmits a force into the upper four-block stack, which can accelerate as a unit up to μg. Since the upper stack's center of mass sits at roughly 0.2 m above its base, tipping happens when the horizontal friction force times that height exceeds the weight times half the stack's width — so I need to check that torque balance against μ to see if toppling is geometrically favored.

Once block1 slides clear (~0.2s at that speed), the tower tips toward the pusher side and falls, and the pusher itself keeps moving forward into the debris, which is messy. I should avoid that by changing the actuation — maybe swap the velocity-driven pusher for a position actuator, though that risks spring-like overshoot, so perhaps a slide joint with a controlled stop is cleaner.

Switching to a slide joint with a limited travel range paired with a force-limited velocity actuator should make the pusher stop naturally once it hits its joint limit after pushing block1 about 0.15 m. I'm also reconsidering timing — with v=0.5 m/s and a gap of 0.15–0.25 m, contact happens somewhere around 0.3–0.5 s, which matches the "stands until pushed" framing. I'm also thinking about whether the tower actually tips or slides given the 0.8 block-to-block friction, since floor friction on block1 barely matters once the pusher overpowers it, and the sudden jerk in velocity could affect how block2 responds at its base.

Working through the tipping condition: toppling the whole 4-block stack needs a friction force exceeding mg, and since max friction is 3.2mg, sliding friction saturates and actually drives tipping, giving the center of mass an acceleration of 0.8g. I'm tracing through how this creates rotation — block1 slides out from under the stack, the tilted stack keeps rotating as it falls, and it should topple toward -x, though I'm still working out whether it rotates as one rigid body or if the individual blocks slip against each other as friction forces propagate upward.

Regardless of the exact mechanism, the blocks end up scattered on the floor with the top block landing low, which satisfies the toppling condition. The pusher stops at its range limit, block1 coasts briefly on momentum before friction halts it, and everything should settle within the 6-second window. I'm now double-checking the pusher's geometry and position to make sure the setup is physically consistent.

I'll position the pusher slightly above the floor so it doesn't clip, with a velocity actuator (kv=500, force-limited to ±200) driving the slide joint, and estimate masses from default density: pusher around 0.9 kg and blocks around 1 kg each.

Adjusting density to tune mass, I'm lowering gain to kv=200 for stability with implicitfast integration at dt=0.002, checking that the joint range limit safely stops the pusher under full force. For the keyframe I need all 36 qpos values (1 pusher slide + 5 free joints × 7) with ctrl set to zero.

I realize qpos can simply default to qpos0 in MJCF if unspecified in the keyframe, so I only need to set ctrl explicitly there, which simplifies things since the block stack is already defined to be touching.

With friction set to 0.8 for both blocks and floor, the sliding force needed (~20N) stays comfortably under the 200N actuator limit. But checking the dynamics, the required acceleration for the stack to follow the pushed block (60 m/s²) far exceeds what friction alone (0.8g) can sustain, meaning the stack likely won't move together smoothly as a rigid group.

Thinking through the rotational physics now: with friction force acting at a height offset from the center of mass, and the four-block stack's moment of inertia around 0.0142M, I need to balance the torque from friction against the counteracting torque from the shifted normal force at the trailing edge to determine whether the stack actually tips over.

After that, once the block matches speed, the tower keeps rotating at 1.5 rad/s with no more forcing, so I check whether it tips past the critical angle of 0.245 rad given its geometry. Comparing rotational kinetic energy (~0.064M) against the potential energy needed to lift the center of mass over the pivot (height gain of only ~0.0035 at this angle) suggests it has more than enough energy to tip.

But then I worry about the pusher stopping — once block1 hits its range limit and decelerates due to friction, the tower's relative motion could reverse and tip the other way, forward instead of backward. To avoid this ambiguity, I consider using a higher pusher speed, like 1.5 m/s, so block1 slides out more decisively before any deceleration becomes an issue.

Landing is messy — base friction could stop the bottom while the top keeps moving, creating a forward tipping torque that might cancel the backward rotation, possibly stabilizing like a tablecloth trick. Rather than rely on that chaotic landing, I'm considering a cleaner alternative: let friction decelerate the whole stack together while sliding, then check the tip criterion based on deceleration and the combined center-of-mass height.

Checking the tipping math: the stack's half-width is 0.05 and COM height 0.25, so tipping needs deceleration a > 0.2g. With floor friction μ=0.8, deceleration is 0.8g, which comfortably exceeds the threshold, so the tower would indeed tip forward as it's brought to a stop by friction — consistent with how tall towers behave when slid and halted on a high-friction surface. I'm now working out the timing of this deceleration phase, starting from some initial velocity down to zero.

I realize the block-to-block dynamics complicate this since each cube interacts with its neighbors through friction, not as one rigid body, so I'm reconsidering the setup. I'm thinking about whether a quasi-static push on the bottom block would just drag the whole stack along without toppling it, versus using differing friction coefficients between the floor and the inter-block surfaces to engineer a cleaner tipping failure.

Let me try constant-force pushing instead: if the pusher applies a steady acceleration above the floor-friction threshold but below the block-block slip threshold, block1 and the stack could move together without slipping at all, which defeats the purpose — so I need to reconsider whether a brief impulsive push followed by release is cleaner than a continuous-force motor.

Takes roughly 0.3-0.4s, covering about 0.5m, well within a 1m pusher travel range. Slipping between block1 and block2 might occur if friction can't sustain that acceleration, but that's fine since the tower topples regardless. I'm now checking the total force needed, accounting for the pusher mass plus all five blocks and the floor friction acting on block1.

That gives around 33 N total. But I realize there's an issue: if the pusher starts with a gap before contacting block1, it would accelerate freely and hit with significant speed—around 3.6 m/s—which could knock block1 out rather than push it cleanly. I need to reconsider the setup so the pusher starts already in contact with block1 at t=0, avoiding that impact problem.

I'm now considering slower approach speeds or damped actuation so the pusher reaches a terminal velocity instead of accelerating unbounded, which would prevent a jarring collision while still maintaining enough sustained force to move the stack once contact is made.

I'm realizing constant force gives impact speed proportional to time and gap, so getting low impact velocity while reaching contact quickly is contradictory, and trying a delayed/reversing velocity profile doesn't help since contact speed ends up matching the initial speed anyway. I'm considering instead a heavy pusher with a modest constant force, so the pusher's standalone acceleration is small but once in contact the combined system behaves differently.

Testing numbers: with pusher mass 20 kg, the computed contact speed still comes out around 3 m/s, which is too abrupt — the sudden jerk at impact would cause the first block to slip out instead of pushing smoothly. I'm concluding this approach isn't working and need to rethink the simplest way to start the pusher.

Maybe instead the pusher should begin touching block1 with essentially zero gap, so contact happens immediately — but that conflicts with wanting the stack to visibly stand for a moment before being pushed, so I should add a delay. One option is a velocity-controlled approach at a slow, steady speed before contact, then using a force-limited servo so the stack only needs to match that gentle velocity rather than absorb a sudden impulse on impact.

I'm also considering whether an overdamped spring-driven slide could work, but that doesn't quite produce a clean toppling event since the force actually decreases as it nears the target rather than building up. So the better approach seems to be: pusher advances slowly, stack slides together under static friction with little slip, and then stopping the pusher at the end of its range causes block1 to keep moving and topple forward off the stack.

Treating this like a block hitting a stop, I estimate the angular velocity imparted to the upper stack and compare rotational kinetic energy to the potential energy barrier needed to topple it, getting a threshold velocity around 0.41 m/s. Since the floor friction stop isn't instantaneous but still nearly impulsive, I'm checking whether the torque balance about the pivot, including gravity, still supports toppling under these conditions.

Good, the increased tilt helps too. Now I'm worried about direction: since the stack tips forward, away from the pusher, that's favorable since it falls clear rather than onto the pushing mechanism. But I realize the initial impact could first induce a backward rotation as the pusher catches up to speed before the forward tipping torque dominates — for v=1 m/s, estimating a catch-up slip time of about 0.13s giving backward ω≈2.5 rad/s and tilt ~0.16 rad, which complicates whether the stack actually falls backward before the forward phase takes over.

Checking energetics, it seems like the stack falls backward during the push itself. Looking at the slip more carefully, block1 slides about 0.065 m, and since that exceeds the half-width of 0.05, the upper stack's center of mass ends up past block1's rear edge — so it topples off the back regardless. Either way, toppling seems inevitable; I just need to pin down which direction it falls.

Setting block1's push distance to 0.3 m and v=0.8, I recompute the slip between block1 and the upper stack during catch-up: roughly 0.054 m, which exceeds the 0.05 m edge margin, so the upper stack tips backward with some angular momentum. Though I should double check this assuming block2 shares friction load with blocks 3-5 rather than treating it as a single accelerating unit.

Checking the numbers, the friction force needed to accelerate blocks 3-5 through block2 is ≤0.6×3mg — exactly matching 0.6g acceleration, so the assumption holds. I'm also accounting for the gap before the pusher makes contact: roughly 0.3 m at 0.8 m/s plus actuator ramp-up time (τ≈0.02 s, reaching speed within ~0.1 s), giving contact around t≈0.4 s, after which the pusher begins driving block1 forward against its friction.

I'm calculating total resisting friction on block1 (~27 N from floor and block2 contact) against the velocity servo — with kv=100 the steady-state speed error is too large, so I bump kv to 400 using implicitfast integration for stability, with forcerange ±300, bringing the error down to about 0.07 m/s. I'm settling on a pusher mass of 3 kg and setting the slide joint range to "0 0.6" with the pusher body positioned so its front face starts at -0.30 and travels to +0.30 at full extension.

At the range limit, the joint stops the pusher while the actuator still pushes up to 300 N against it, which should be fine since the limit constraint holds — I'll set the ctrlrange for the velocity actuator with ctrl 0.8. I'm sizing the pusher geom as a box spanning roughly z=0.01 to 0.08, positioned low enough that blocks might land on top of it, and confirming the pusher's slide joint means no gravity concerns and no floor contact since it floats 1 cm above. Now I'm checking the initial stack so blocks start exactly touching without overlap.

Soft contacts should allow small millimeter-level penetration which is fine, and by 6 seconds everything should settle with blocks on the floor and the pusher held at its limit with zero velocity. I'm writing the XML now, including a keyframe with ctrl="0.8" and deciding whether to specify explicit qpos values for each block's position plus the pusher's slide joint — going with explicit qpos listing each block stacked vertically followed by the pusher.

For friction, floor and blocks use 0.6 while the pusher uses 0.3, so contact pairs resolve to max friction of 0.6, which works fine. I'm adding a single option element setting timestep to 0.002 with the implicitfast integrator, keeping everything else at defaults, then finalizing the lighting and visual extras before writing out the complete file.

