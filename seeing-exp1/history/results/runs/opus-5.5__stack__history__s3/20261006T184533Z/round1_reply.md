**What happened in the run:** the stack stood still until 0.92 s, when the rolling sphere reached `block1`. By then it had slowed to 1.07 m/s. Its hit slid the whole column about 5 cm in +x. Each block tilted 2–3°, rocked back, and by 1.71 s all five blocks were upright again at x ≈ 0.05, stacked as before. Nothing toppled.

**Why:** a 4 kg ball at about 1 m/s shoves the bottom block. With equal friction everywhere, the blocks above are dragged along as one unit. The column is 1 m tall on a 0.2 m base, so it only tips past about 14°. It only reached 3°.

**What the corrected file changes:**
- **Slenderer column.** The blocks are now 0.1 m thick along the push direction, so the column tips past about 7°.
- **Slipperier block-to-block contact.** Friction between blocks is 0.25. The floor stays at 0.6, and MuJoCo uses the larger value for each contact pair.
- **A ram instead of a ball.** It is a 5 kg box on an x-slide joint at bottom-block height, starting at 1.2 m/s and hitting at about 0.37 s. A joint limit stops it after it has driven `block1` about 0.08 m forward. That is most of the way out from under the column.

The blocks above then lose their footing and tip back over the ram, so the stack topples. I have not run the corrected file. How much more `block1` slides after the ram stops is a guess.

```json
{"what_happens": "The stack stands until the rolling sphere reaches block1 at 0.92 s, moving at about 1.07 m/s. The hit slides the whole column about 5 cm in +x with 2-3 degrees of tilt. The blocks rock back and by 1.71 s all five are upright and at rest, still stacked. Nothing topples.", "works": false, "problem": "The push only slides the whole stack a few centimetres as a unit and the blocks resettle upright, so the stack never topples."}
```

```xml
<mujoco model="stack_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="6 6 0.1" friction="0.6 0.005 0.0001"/>
    <body name="block1" pos="0 0 0.100">
      <freejoint/>
      <geom name="block1" type="box" size="0.05 0.1 0.1" mass="0.5" friction="0.25 0.005 0.0001"/>
    </body>
    <body name="block2" pos="0 0 0.300">
      <freejoint/>
      <geom name="block2" type="box" size="0.05 0.1 0.1" mass="0.5" friction="0.25 0.005 0.0001"/>
    </body>
    <body name="block3" pos="0 0 0.500">
      <freejoint/>
      <geom name="block3" type="box" size="0.05 0.1 0.1" mass="0.5" friction="0.25 0.005 0.0001"/>
    </body>
    <body name="block4" pos="0 0 0.700">
      <freejoint/>
      <geom name="block4" type="box" size="0.05 0.1 0.1" mass="0.5" friction="0.25 0.005 0.0001"/>
    </body>
    <body name="block5" pos="0 0 0.900">
      <freejoint/>
      <geom name="block5" type="box" size="0.05 0.1 0.1" mass="0.5" friction="0.25 0.005 0.0001"/>
    </body>
    <body name="pusher" pos="-0.6 0 0.1">
      <joint name="pusher_slide" type="slide" axis="1 0 0" limited="true" range="-0.1 0.53"/>
      <geom name="pusher" type="box" size="0.1 0.08 0.05" mass="5.0" friction="0.3 0.005 0.0001"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0 0 0.100 1 0 0 0  0 0 0.300 1 0 0 0  0 0 0.500 1 0 0 0  0 0 0.700 1 0 0 0  0 0 0.900 1 0 0 0  0" qvel="0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  1.2"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

The simulation shows the pusher hitting block1 at 0.92s, causing the stack to shift about 5cm and tilt slightly before settling upright without toppling, so this configuration fails. I need to account for the pusher's rolling velocity decaying from 1.5 to 1.07 m/s due to translational-to-rotational energy conversion before it strikes the block.

To actually topple the stack, I need the bottom block to be pushed far enough or fast enough that the base slides out from under the upper blocks before friction drags them along, essentially needing a larger relative displacement between block1 and block2 than what a moderate tilt-and-recover produces.

I'm now thinking about achieving this with low friction between block1 and block2 so the push slides block1 cleanly out, but then I realize friction contacts take the maximum of the two geoms' friction values in MuJoCo, so just lowering the pusher's own friction with the floor won't matter—the floor's friction coefficient will dominate anyway.

Instead, I'm considering mounting the pusher on a slide joint, raised above floor contact entirely so it never touches the ground, acting like a ram. I'd position it at the right height to strike only block1, not the stack above, and give it enough mass for momentum.

Once it hits block1, friction between block1 and block2 above would drag the upper stack forward too—I need to work out whether that friction force is enough to topple or just translate the column, since the force acts at the base and could induce tipping of the stack rather than clean sliding.

Thinking it through, block1 shoots out at ram speed, moving about 0.3 m in 0.1 s, leaving the upper stack unsupported; it drops roughly 0.2 m onto the floor with some backward tilt and horizontal drift. It's unclear if it topples cleanly or just lands as a standing stack, and there's also the question of whether the ram collides with the falling stack on its way through.

I'm considering a more controlled approach: limiting the ram's travel with a slide joint range so it pushes block1 only a short distance (around 0.15 m) before stopping, letting friction and the resulting displacement induce a cleaner tip in the stack above.

Checking the geometry, after block1 shifts the upper stack's center of mass ends up outside the overlap region, so it would pivot and topple over block1's left edge rather than staying balanced. I need to figure out whether block1's floor friction decelerates it enough to still reach the required 0.15 m displacement, and whether the ram's limit constraint actually halts its motion in time.

I'm trying to figure out how far block1 needs to slide out before the stack above it loses support and tips, estimating maybe 0.15-0.3m depending on when contact overlap vanishes. Maybe a quasi-static push with high friction would be cleaner, since then the whole column just slides together rather than needing precise timing.

I'll set the ram with large mass and moderate velocity, letting a joint limit stop it once block1 has been pushed far enough, then let block1 continue sliding and decelerating from floor friction until the upper blocks lose support and topple.

Estimating the slide distance under varying friction loads, block1 likely clears out entirely before the stack above falls about 0.2 m. The tilt comes from the friction impulse acting briefly at block2's base while block1 slides beneath it, which I'm now working through as an angular momentum calculation to see how much rotation that imparts to the upper column.

Checking whether a 16° tilt plus that rotational velocity is enough to topple the column, given its height-to-width ratio puts the tipping threshold around 14°—it's borderline, so I'm now considering whether adjusting the ram velocity or the stack's proportions could make the outcome more reliably one way or the other.

A sudden base impulse gives a tall rod large angular velocity, so even a modest ram speed should tip it convincingly. I'll settle on thin blocks with half-x 0.05, block friction 0.5, and a slide-joint ram that strikes only block1, stopping after about 0.08 m of travel — then block1 keeps sliding slightly while the stack above either gets dragged and tips backward or loses support and falls.

Given the slenderness, any decent tilt should cause toppling rather than the column landing upright, so I'll use a moderate ram speed around 1 m/s with mass 5 kg, positioned to the side with a timed delay before impact so the stack visibly stands before the hit occurs — working out the ram's starting position and geometry so it clears the floor and reaches block1's back face after crossing the gap.

I'm defining the slide joint's range so the ram face reaches just past block1's position, confirming gravity doesn't affect it since it only moves along x. After impact, the stopped ram becomes a resting surface, and block2 tipping backward over its pivot would land on top of it, which is consistent with the toppling outcome.

Now I'm setting friction coefficients between blocks and the ram, keeping block widths and masses consistent, and tallying up the keyframe's qpos and qvel sizes across the five free-jointed blocks plus the ram's slide joint. I'm deciding to name the ram's joint for clarity, even though freejoints don't require names, and noting that block5 might not be in exact contact with block4 initially, allowing for a touch of settling motion.

