The ball ends up in the bucket, but only after striking the top of the near wall. It is not a clean throw.

**What happens in the run**
- The stiffer spring swings the arm to its 55° stop in 0.37 s, arriving at 270°/s.
- The ball is released at about (−0.46, 1.22) m with a velocity of about (3.75, 1.37) m/s.
- It peaks at 1.32 m at x = 0.06 m.
- At 0.93 s it hits the top edge of `bucket_near`, which spans x = 1.67–1.69 m and reaches z = 0.4 m. At 1.00 s the ball is at (1.67, 0.46) m, sitting on the rim. It bounces there twice.
- It then drops inside, rolls across `bucket_base`, and comes to rest at (2.18, 0, 0.08) m, inside the bucket.

**Why I'm not calling it working**
The landing depends on a rim bounce, so a tiny change in launch speed would put the ball outside. The ball needs about 7% more speed so its path clears the near wall and lands near the bucket's centre.

**Fix (estimated, not re-run)**
- **Target:** keep the same launch angle and land at about x = 2.15 m.
- **Needed speed:** that takes a speed factor of about 1.07, or about 14% more energy, roughly +0.4 J. With that, the ball centre is at z ≈ 0.52 m when it passes x = 1.75 m, so its bottom is about 0.06 m above the rim. It stays well short of the far wall, at x = 2.48 m.
- **Stiffness change:** the spring delivers about 2.05 J per N·m/rad of stiffness over the stroke. So I raise the stiffness from 2.8 to 3.0 N·m/rad.

```xml
<mujoco model="catapult_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="8 8 0.1"/>
    <geom name="catapult_base" type="box" pos="0 0 0.170" size="0.08 0.12 0.170"/>
    <body name="catapult_arm" pos="0 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 55" stiffness="3.0" springref="150" damping="0.05" armature="0.01"/>
      <geom name="catapult_beam" type="box" pos="-0.500 0 0" size="0.500 0.03 0.02" mass="0.3"/>
      <geom name="catapult_cup_floor" type="box" pos="-0.920 0 0.025" size="0.08 0.08 0.005" mass="0.02"/>
      <geom name="catapult_cup_back" type="box" pos="-1.005 0 0.07" size="0.005 0.08 0.05" mass="0.01"/>
    </body>
    <body name="ball" pos="-0.920 0 0.4895">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.06" mass="0.15" condim="6" friction="0.8 0.01 0.004" solref="0.01 1"/>
    </body>
    <body name="bucket" pos="2.08 0 0">
      <geom name="bucket_base" type="box" pos="0 0 0.01" size="0.4 0.4 0.01"/>
      <geom name="bucket_near" type="box" pos="-0.4 0 0.2" size="0.01 0.4 0.2"/>
      <geom name="bucket_far" type="box" pos="0.4 0 0.2" size="0.01 0.4 0.2"/>
      <geom name="bucket_left" type="box" pos="0 0.4 0.2" size="0.4 0.01 0.2"/>
      <geom name="bucket_right" type="box" pos="0 -0.4 0.2" size="0.4 0.01 0.2"/>
    </body>
  </worldbody>
</mujoco>
```

```json
{"what_happens": "The spring arm hits its 55° stop at 270°/s and releases the ball at about (3.75, 1.37) m/s from (-0.46, 1.22) m. The ball peaks at 1.32 m, comes down onto the top edge of the bucket's near wall at x = 1.67 m, bounces on the rim twice, then drops inside and rolls to rest on the bucket base at x = 2.18 m.", "works": false, "problem": "The ball only gets into the bucket by bouncing off the near wall's rim, so the result hinges on a marginal rim strike rather than a clean throw that clears the wall."}
```

---
thinking (summarized):

Tracking the trajectory, the ball clips the top rim of the near bucket wall around 0.93s before tumbling inside and settling near the base — technically landing in, but only via a risky rim bounce, so I want to check if a faster release gives a cleaner shot instead.

I'm recalculating: scaling up the release speed at the same angle increases horizontal range by the square of the scaling factor, so I'm solving for the right speed multiplier that lands the ball closer to the bucket's center (around x=2.05) rather than skimming the near wall at x=1.62.

I find that a scale factor of about 1.035 gets the drop to z=0.08 at the target x, then I'm double-checking the trajectory still clears the wall height at x=1.74 so it doesn't clip the rim on the way in.

Marginal clearance, so I try retargeting with a steeper trajectory landing further at x=2.15, solving for f to clear the floor with some margin. Testing f=1.067 at x=1.75 gives z=0.525, clearing the wall by 0.065 — better. Now I need to check the far wall at 2.47, making sure the ball's center stays under 2.41 while descending below z=0.46.

Checking the energy numbers: needed extra kinetic energy is about 0.41 J, corresponding to a stiffness increase of roughly 0.2 units given 2.05 J per unit. The ball lands and rolls toward the far wall at about 0.4 m/s, which seems fine. I'm weighing whether this run should count as a success — it does end in the bucket, but the rim strike feels like a fluke rather than a reliable result.

Given the trajectory depends on a bounce off the rim, I don't think this counts as robust, so I'll mark it as not working and continue tuning rather than accept a fragile outcome.

