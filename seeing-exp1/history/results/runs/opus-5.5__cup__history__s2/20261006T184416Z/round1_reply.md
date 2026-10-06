**What happens in the run:** The ball starts on the upper end of the ramp and rolls down `ramp_deck`. It leaves the low end at x ≈ 1.6 m, about 0.5 m up, at roughly 2.4 m/s, and flies forward. The cup's near wall stands at x = 2.2 m. The ball lands just short of it and strikes the outside of `cup_near` at 1.48 s. It bounces back onto the floor and rolls away from the cup. It comes to rest on the floor at x ≈ 1.63 m, outside the cup.

**Why it fails:** From where the ball leaves the ramp, it lands at about x ≈ 2.15 m. That is short of the cup, so it hits the outside wall instead of dropping in.

**The fix:**
- **Move the cup back toward the ramp.** I moved its centre from x = 2.65 m to x = 2.1 m, so the near wall sits at x ≈ 1.65 m, just past the ramp's end.
- **Lower the near wall to 0.35 m.** As the ball passes over the near wall, its bottom is about 0.47 m up, so it clears the wall. It then lands at x ≈ 2.15 m, well inside the cup.
- **Raise the far and side walls to 0.6 m.** The ball keeps rolling forward at about 2.3 m/s with its spin. Its energy could carry it up a wall to a height of about 0.38 m, so 0.6 m walls keep it from climbing out.

After it hits the far wall, the contacts damp most of its speed, and it should settle on the cup base by 6 s. I have not re-run the corrected file.

```xml
<mujoco model="cup_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="6 6 0.1" friction="0.8 0.005 0.002"/>
    <geom name="ramp_deck" type="box" pos="0.8000 0 0.7250" euler="0 18.9704 0" size="0.8459 0.2 0.02"/>
    <geom name="ramp_leg" type="box" pos="0.0000 0 0.5000" size="0.03 0.03 0.5000"/>
    <body name="ball" pos="0.1398 0 1.0376">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.06" mass="0.2" condim="6" friction="0.8 0.01 0.004" solref="0.01 1"/>
    </body>
    <body name="cup" pos="2.1000 0 0">
      <geom name="cup_base" type="box" pos="0 0 0.01" size="0.450 0.300 0.01" friction="1.0 0.01 0.004"/>
      <geom name="cup_near" type="box" pos="-0.450 0 0.175" size="0.01 0.300 0.175"/>
      <geom name="cup_far" type="box" pos="0.450 0 0.300" size="0.01 0.300 0.300"/>
      <geom name="cup_left" type="box" pos="0 0.300 0.300" size="0.450 0.01 0.300"/>
      <geom name="cup_right" type="box" pos="0 -0.300 0.300" size="0.450 0.01 0.300"/>
    </body>
  </worldbody>
</mujoco>
```

```json
{"what_happens": "The ball rolls down ramp_deck and leaves its low end at x≈1.6 m, about 0.5 m up, at ~2.4 m/s. It flies forward and strikes the outside of cup_near (x≈2.2 m) at 1.48 s, bounces back onto the floor, and rolls to rest at x≈1.63 m, outside the cup.", "works": false, "problem": "The cup is too far from the ramp end, so the ball lands short and hits the outside of the cup's near wall, then rests on the floor instead of in the cup."}
```

---
thinking (summarized):

The ball rolls off the ramp but clips the outside wall of the near cup and bounces away, landing short on the floor instead of going in — so the trajectory fails. I need to recheck the ramp's geometry more carefully, recalculating where the deck's edges actually fall given its center position and angle.

Reworking the exit conditions: the ball leaves the ramp around x=1.6 at a height near 0.54 with velocity components roughly vx=2.3, vz=-0.78, and falling under gravity it would land around x=2.15 on the floor — right where the near cup wall sits, so it gets blocked. For it to actually drop into the cup, its center needs to stay above the wall's top (z=0.3, so center above 0.36) while crossing that x position, which means I need to recompute the timing of when the ball's height passes that threshold relative to its horizontal position.

Let me reconsider the geometry: friction will settle the ball once it rattles inside the cup. If I center the cup at x=2.1 with half-length 0.45, the near wall sits at 1.65 (clearing the ball as it exits the ramp around x=1.6 at height ~0.54) while the far wall at 2.55 keeps the ball contained after it lands around x=2.15 and rolls forward.

But I need to check the ball's horizontal speed after landing, roughly 2.3 m/s, against the far wall — with default contact damping there's little bounce, but if the ball has topspin, friction at the wall could actually cause it to climb up and potentially jump out. Doing the energy math, a rise of about 0.28 m is close to the 0.3 m wall height, so I should probably increase the wall height to around 0.4 m to keep enough margin for the ball not to escape.

No overlap there since the cup body is static anyway. I'm thinking about damping: ball has rolling friction so it'll decelerate, and bouncing between the cup walls loses energy at each contact, so it should settle well before 6 seconds. To be extra safe I might add solver damping to the cup walls.

For the landing itself, with vz around -1.0 and the ball's solref tuned low, there's no real bounce. I'm also checking whether topspin could make the ball climb the far wall of the cup — working through the surface velocity at the contact point for a rolling ball (top moving forward at 2v, bottom stationary) to see which direction friction would push it at the wall.

I confirm the friction direction is upward, so the ball does climb slightly, but I compute the required rise to clear a 0.4 wall (from 0.08 to 0.46) and find the total kinetic energy, including rotational, only converts to about 0.38 m of height — borderline but still short, so I think it's fine. I should double check how this interacts with the landing dynamics and horizontal speed once it comes back down around x≈2.3.

I realize the near wall creates a conflict since the ball's bottom is higher than the wall top at crossing. I'll make the walls asymmetric instead: a shorter near wall at 0.35 and a taller far wall at 0.6, with tall side walls too, so the ball clears the near wall but gets properly captured by the far wall after rising enough. I'm positioning the cup at x=2.1 with a base size around 0.45.

Setting precise positions and sizes for each wall segment, then verifying the ball's trajectory doesn't clip the near wall on entry, properly hits the far wall around x≈2.48, bounces back without escaping over the now-fine near wall, and settles at rest on the base.

