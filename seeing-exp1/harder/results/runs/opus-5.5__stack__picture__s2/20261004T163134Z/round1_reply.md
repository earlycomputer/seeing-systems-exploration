**What happens:** The 4 kg sphere starts at x = −1.2 m and rolls right along the floor. Its copies get denser as it approaches the stack, and the darkest copy sits right against the left face of block1. The five-block column is drawn once, with no residue in either view. No block slid, tilted or fell during the 1.9 s shown. The push arrives, but the stack never topples, so the brief's main event doesn't happen.

**Fix:** I replaced the free-rolling ball with a driven pusher that can't lose its momentum. It is a low box on an x slide joint, held at 1.5 m/s by a velocity servo, and its top is below block2, so it strikes only block1.

Why this should topple the stack (rough estimate, not run):
- Block friction is raised to 0.8, so block1 drags the stack hard as it is shoved.
- That drag gives the four blocks above about 7.8 m/s² of base acceleration. This is well past the roughly 2.5 m/s² needed to tip a 0.2 m wide, 0.8 m tall column.
- Block1 keeps moving at 1.5 m/s, sliding out from under the stack, so the column tips back and falls.

```json
{"what_happens": "The heavy sphere rolls from x=-1.2 to the foot of the stack and comes to rest against block1; the five-block column is drawn once with no residue, so it stays upright and nothing topples.", "works": false, "problem": "The rolling ball reaches block1 but does not push it, so the stack never topples."}
```

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
    <body name="pusher" pos="-0.4 0 0.08">
      <joint name="pusher_x" type="slide" axis="1 0 0" limited="true" range="0 1.2" damping="0"/>
      <geom name="pusher" type="box" size="0.05 0.12 0.06" mass="5.0" friction="0.3 0.005 0.0001"/>
    </body>
  </worldbody>
  <actuator>
    <velocity name="push" joint="pusher_x" kv="500" ctrlrange="0 2" forcerange="-400 400"/>
  </actuator>
  <keyframe>
    <key name="start" qpos="0 0 0.100 1 0 0 0  0 0 0.300 1 0 0 0  0 0 0.500 1 0 0 0  0 0 0.700 1 0 0 0  0 0 0.900 1 0 0 0  0" qvel="0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  1.5" ctrl="1.5"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm examining the plan view to check whether the stack actually moved or just stayed static while the ball's residue trail approaches it near x=-0.2, trying to confirm the stack's column position is fixed rather than shifted.

Running the numbers: the 4 kg sphere slows from 1.5 m/s to about 1.07 m/s rolling, taking 0.73 s to reach the stack with momentum around 4.3. Comparing that against friction forces on the bottom block (from floor and from block2 above), it's unclear whether the impact would be enough to dislodge block1 — but since the stack column in the image looks uniform without any smearing to the right, it seems like the stack didn't get pushed.

Now I'm trying to cross-check the pixel scale against the ball's position: at 60.4 px/m over a 2.12 m range, the stack should land around pixel 24.5, but visually it looks closer to pixel 95, so something about my scale assumption seems off.

Pinning down x=0 at pixel 97.8 fits the stack location better, and the ball's starting point at x=-1.2 lines up with pixel 25. The ball's copies look too numerous for a simple constant-speed pass to the stack, suggesting it's slowing down or stalling right as it reaches it, with the final copy darkest right at the stack — meaning the ball hits and stops rather than the stack itself shifting.

But physically that's odd: a 4 kg ball at ~1.07 m/s hitting a 0.5 kg block should impart enough impulse to overcome the ~26.5 N friction resisting it, so block1 should get pushed. Since the residue trail only extends to 1.91 s and shows no displacement of block1, it seems like the push either hasn't visibly registered yet in that window or the contact stalled — toppling of the stack would unfold over several more seconds beyond what's shown.

I'm reconsidering the design: a cleaner approach is a non-rotating slider pusher with a strong, decisive velocity aimed low enough to strike only block1, so it's yanked out quickly like a tablecloth trick, letting the stack drop and potentially remain standing — or alternatively, a moderate push that drags block1 via friction so the upper blocks lag behind and topple that way.

I'm working out the physics of whether a sudden acceleration on block1 would actually tip the stack backward toward the pusher, given its 1m height and 0.2m width — checking if the tipping condition (acceleration exceeding g times width over center-of-mass height) is realistic to achieve.

Given the impulsive-contact uncertainty, I'm instead considering a simpler, more controllable approach: a kinematic pusher using a slide joint with a constant velocity actuator, pushing block1 steadily at something like 0.5 m/s rather than relying on an impulsive strike.

If block1 slides out more than half its width relative to block2, the upper stack's center of mass shifts past the edge of support and topples into the gap. I can engineer this by lowering friction specifically on block1's contacts using MuJoCo's priority setting, so block1 slides freely against both the floor and block2 while the upper blocks stay relatively still—creating the offset needed for toppling.

For the pusher, I'll use a slide joint along x rather than a freejoint so it can't tumble, positioned low enough to only contact block1 and avoid the floor, driven by a velocity actuator set to push block1 at a few meters per second.

Thinking through the physics: if block1 slides out cleanly before the stack falls, the upper blocks might just drop straight down and stay standing rather than toppling. For actual tipping to occur, I need the overlap between block1 and block2 to shrink until block2's center of mass extends past block1's support edge, causing the stack to tip backward toward the pusher side rather than falling flat.

Block1 needs another 0.33 s at 0.3 m/s to clear block2. There's also friction between the blocks at μ=0.1 dragging block2 slightly forward, and I need to check the pusher's position relative to block2 — since the pusher trails right behind block1, as block2 tilts backward its left edge might actually come down onto the pusher itself, which changes the geometry significantly.

This is getting messy, so I'm considering a cleaner setup instead: push block1 abruptly and let it stop against a stopper, so the stack above keeps moving via inertia and topples forward — a more robust classic approach. Alternatively, using a ball impact on block1 rather than a continuous pusher might simplify the dynamics.

Computing the max acceleration at 7.8 m/s² and checking the tipping threshold (2.45 m/s²), I confirm the stack does tip backward since it's exceeded—so it rotates about block2's left bottom edge once block1 reaches its target speed of 0.6 m/s after about 0.08 s, with the stack then carried along while rotating on that pivot edge.

Treating the upper four blocks as a rigid body (mass 2, dimensions 0.2×0.8) pivoting at the bottom-left corner, I compute torque from the pseudo-force (6.24 N·m) against gravity's restoring torque (1.96 N·m), giving a net torque of 4.3 N·m against a moment of inertia of 0.453, so angular acceleration comes out to about 9.5 rad/s². I'm now second-guessing whether friction stays saturated once the stack actually begins tipping, since that changes the force balance.

After the push ends, the angular velocity reaches roughly 0.76 rad/s at a tilt of 0.03 rad. Then I check the energy needed to reach the 14° critical angle—raising the center of mass by about 0.012 m requires 0.24 J, which I compare against the rotational kinetic energy built up during the push to see if the stack has enough momentum to actually topple.

It'll likely topple backward regardless, and faster pushes only make that worse given the high friction. I'm now reconsidering the setup: maybe the ball actually did move things and I misjudged it, so I'm sketching a pusher body with a sliding joint, a box geom sized appropriately starting close to the stack, and a velocity actuator with enough gain and force range to drive it forward convincingly.

Pusher contacts with toppling blocks should be fine since gravity's handled by the slide joint constraint. I'll set block friction to 0.8 and floor friction to 0.6, giving a total qpos of 36 and qvel of 31, with ctrl set to "1.5". Now I'm ready to write the final answer: the sphere rolls from x=-1.2 to the stack's base, stops against block1, and the stack stays upright throughout.

