**What happens.** The ram slides in from the left and pushes the bottom block. The column stays upright in both views. All motion ends by about 1.4 s, and nothing tips.

**Why it fails.** The damped servo pushed too gently. Block 1 accelerated well under μg = 0.98 m/s², the limit that the 0.1 friction on block 1's top face can transmit. Static friction therefore carried the four upper blocks along with it. The base never moved out from under the stack's centre of mass.

**The fix.** Block 1 has to be jerked out quickly, so the blocks above slip on it, and then stopped at a set distance.

- **Ram.** It is now a heavy 20 kg ram on a slide joint with a hard range limit. Its keyframe velocity is 1 m/s.
- **Strike.** It hits block 1 at nearly constant speed. That jerk is far above 1 m/s², so the upper blocks stay roughly in place while block 1 is driven about 0.13 m.
- **Stop.** The ram halts at its joint limit. The floor friction of 1.0 under the full stack weight stops block 1 within about a centimetre.
- **Topple.** The upper stack's centre of mass then lies outside block 1's top face, so it tips back over block 1's trailing edge and falls.

The distances are hand estimates; I have not run this version.

```json
{"what_happens": "The ram slides in and pushes the bottom block slowly; the whole five-block column stays upright, carried along by friction, and motion ends by about 1.4 s without any toppling.", "works": false, "problem": "The slow servo push let static friction carry the upper blocks along with the bottom block, so the stack never lost its support and did not topple."}
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
    <body name="pusher" pos="-0.35 0 0.08">
      <joint name="ram_slide" type="slide" axis="1 0 0" limited="true" range="0 0.33"/>
      <geom name="pusher" type="box" size="0.05 0.15 0.05" mass="20.0" friction="0.1 0.005 0.0001"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0 0 0.100 1 0 0 0  0 0 0.300 1 0 0 0  0 0 0.500 1 0 0 0  0 0 0.700 1 0 0 0  0 0 0.900 1 0 0 0  0" qvel="0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  1.0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

Looking at the image, the ram moves toward the block while the stack column stays standing upright with only slight blur near the top, and the residue trace stops by 1.42 s, suggesting the motion halted without the stack toppling—likely the displacement was too small to cause collapse.

Thinking through why: the friction math matters here. Block1-floor friction with mu=1.0 gives 24.5N, while block1-block2 friction at mu=0.1 gives only 2N, and the servo stalls around a small position error. If block1 shifted enough that the upper stack's COM fell outside its support base, it should've tipped—unless the upper stack got dragged along with block1 due to static friction holding them together during the slow push, since the required acceleration stays below the static friction threshold.

So the fix is to make the push a sharp, fast jerk rather than a slow one, so block1 accelerates faster than mu*g and slides out from under the stack—while still needing a controlled stop so the ram doesn't overshoot. I'm considering a limited slide joint with a range so the ram halts abruptly at its limit, letting block1 decelerate quickly via floor friction (now amplified by the full stack weight pressing down) while the upper stack's inertia keeps it in place.

I'm working out numbers: if the ram delivers roughly 1 m/s, block1 travels about 0.13 m before the ram stops, during which the stack above only creeps a few millimeters due to the low friction-driven acceleration—enough for noticeable relative slip. To keep the ram moving at a near-constant velocity against the ~26.5N friction resisting it, I'm giving the ram a larger mass (around 20 kg) so its kinetic energy dominates the frictional work done over the short travel distance, keeping its speed roughly steady until impact.

Then the ram hits its joint limit and stops within a few millimeters, after which block1's own momentum carries it slightly further to about 0.14 m displacement. With the stack's center of mass at 0 and its support base spanning roughly 0.04 to 0.1, this shift is enough to tip the whole stack toward the ram, causing it to topple onto the ram's top surface. I'm tuning joint damping to zero and adjusting the ram's starting position and range limits so the timing and displacement work out—placing the ram's body closer, around -0.35, to shorten the travel time before contact.

Checking the collision physics now: even with some elastic bounce giving block1 up to 2.4 m/s after impact, it decelerates quickly enough that the ram, still moving forward to its stop position, catches up to it—so the ram ends up in contact with block1 regardless of the bounce speed.

Lowering the ram's initial speed to 1.0 m/s should reduce bounce further. I'm dropping the actuator entirely and just setting the initial velocity directly through qvel, padding zeros for the other joints before the ram's slide velocity. Gravity acting on the ram only matters for the slide axis here, so that's fine.

