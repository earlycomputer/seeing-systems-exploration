**What happens in the run**

The ball starts at rest near the top of the ramp and rolls down `ramp_deck`. The deck is tilted 19° and runs from (0, 1.0) down to (1.6, 0.45), so its low end hangs 0.45 m above the floor.

At 1.26 s the ball leaves the end of the deck at about 2.4 m/s and flies through the air. At 1.48 s, at x ≈ 2.14 and z ≈ 0.08, it hits the outside face of `cup_near`. The cup's near wall sits at x = 2.20, which is past where the ball lands. The ball bounces back onto the floor and rolls back toward the ramp. It comes to rest on the floor at (1.63, 0, 0.06), well outside the cup.

**Fix**

I moved the cup back along the ball's actual flight path so the ball drops inside it.

- At 1.25 s the ball is at (1.59, 0.54) moving at (+2.30, −0.78) m/s.
- Projecting that path, the ball's centre is about 0.50 m high when it reaches x ≈ 1.68. Its bottom is then at about 0.44 m, clear of the 0.30 m wall top.
- The ball should reach the cup floor at about x = 2.14.

With the cup centred at x = 2.20:

- The near wall is at 1.75, below and past the deck's low end, so it doesn't touch the ramp.
- The interior runs from x = 1.76 to 2.64, so the landing point is inside.
- The ball's remaining speed is mostly lost when it hits the critically damped far wall, as happened at the near wall in this run.
- After that it rolls slowly and should stop between the walls.

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
    <body name="cup" pos="2.2000 0 0">
      <geom name="cup_base" type="box" pos="0 0 0.01" size="0.450 0.300 0.01"/>
      <geom name="cup_near" type="box" pos="-0.450 0 0.150" size="0.01 0.300 0.150"/>
      <geom name="cup_far" type="box" pos="0.450 0 0.150" size="0.01 0.300 0.150"/>
      <geom name="cup_left" type="box" pos="0 0.300 0.150" size="0.450 0.01 0.150"/>
      <geom name="cup_right" type="box" pos="0 -0.300 0.150" size="0.450 0.01 0.150"/>
    </body>
  </worldbody>
</mujoco>
```

```json
{"what_happens": "The ball rolls down ramp_deck and leaves its raised low end (z≈0.45 m at x=1.6) at about 2.4 m/s. It flies into the outside face of cup_near at x≈2.14, bounces back onto the floor, rolls back toward the ramp and comes to rest on the floor at (1.63, 0, 0.06), outside the cup.", "works": false, "problem": "The cup sits too far away, so the airborne ball hits the outside of the cup's near wall and settles on the floor instead of landing inside the cup."}
```

---
thinking (summarized):

The ball hits the cup's near wall and bounces out instead of landing inside, so it fails the test. I need to recompute the ramp and cup geometry more precisely to fix the trajectory, working out the ramp deck's endpoint positions based on its center, pitch angle, and half-length.

The ramp's low end actually sits above the floor at around z=0.45 rather than reaching ground level, meaning the ball launches into the air before reaching the cup. Since the cup walls are 0.3 tall and the ball can't roll over them, I need the ramp to end directly above the cup interior so the ball drops in cleanly, accounting for the ball's exit velocity, rolling friction, and how it settles after bouncing off the far wall.

Calculating velocities for different drop heights to keep the ball slow enough to settle quickly — a 0.3m drop gives about 2.05 m/s which seems too fast, while a 0.15m drop gives roughly 1.45 m/s, which combined with the ~0.3m fall into the cup might work better for settling within a reasonable time.

Actually, looking at the run data, wall impacts with critical damping absorb most of the horizontal velocity — the ball hit the near wall at ~2.3 m/s and bounced back at only -0.24 m/s, so the walls are doing the heavy lifting on energy dissipation. That means the ball should decelerate quickly once inside the cup regardless of entry speed, settling well within the 0.88m interior length. The simplest fix now is just repositioning the cup so the ball actually lands inside its catch zone.

Solving for when z reaches 0.36, I get t≈0.123s giving x≈1.90, so the near wall must sit at an x-position where the ball is still clearing it with margin above 0.3 — meaning the wall's placement needs to be closer than this crossing point to guarantee clearance.

Checking x=1.75 gives z≈0.47, well clear of the ramp's low end at z≈0.43, so no collision there. This lets me place the near wall around x=1.72, putting the cup center near x=2.17 with the ball landing around x=2.16 — right in the interior zone spanning roughly 1.73 to 2.61, though I still need to check whether the ball clears the far wall given its landing velocity components.

With soft contact (solref 0.01 1) the bounce on the base should be minimal, and the ball should mostly slide forward converting its horizontal velocity through friction. The 0.39m gap to the far wall means it'll hit that wall, lose most speed, and likely roll back just enough to settle inside without escaping past the near wall — so the ball should come to rest within the cup area.

Checking ball clearance against the near wall confirms good margin above it. I'll place the cup around x=2.20 so the ball lands comfortably inside, clearing both the near wall and leaving buffer before the far wall.

No conflicts show up between the ramp's deck underside and the cup wall heights, and the landing dynamics look critically damped with no bounce-out risk off the far wall. This configuration works.

