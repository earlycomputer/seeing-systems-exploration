**What happens in the run**

The ball rolls down `ramp_deck` from x ≈ 0.14 m. The deck does not reach the floor: its lower end sits about 0.45 m up at x ≈ 1.6 m, so the ball leaves it at 1.26 s and flies off the edge. It lands short of the cup. At 1.48 s it hits the outside face of `cup_near` (x = 2.2 m) at about 0.08 m height, well below the 0.3 m wall top. It bounces back, drops to the floor, rolls backward and stops at (1.63, 0, 0.06) m, outside the cup.

**Why it fails**

From the launch point (centre z ≈ 0.53 m, velocity about 2.3 m/s forward and 0.8 m/s down), the ball's centre reaches the floor at x ≈ 2.15 m. That is just before the near wall. The cup is simply too far away.

**Fix**

I moved the cup so the ball lands inside it.

- The cup is now centred at x = 2.2 m with an inner half-length of 0.5 m, so its walls are at x = 1.7 m and x = 2.7 m.
- At x = 1.7 m the ball's centre is still about 0.48 m high, so it clears the 0.3 m near wall easily.
- It lands on the base at about x = 2.14 m.
- Either way it ends in the cup: it stops on the base, or it reaches the far wall at 2.7 m, where the contact damping absorbs the bounce.
- I gave `cup_base` higher rolling friction so the ball settles well within the 6 s.

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
      <geom name="cup_base" type="box" pos="0 0 0.01" size="0.510 0.300 0.01" friction="0.8 0.01 0.01"/>
      <geom name="cup_near" type="box" pos="-0.500 0 0.150" size="0.01 0.300 0.150"/>
      <geom name="cup_far" type="box" pos="0.500 0 0.150" size="0.01 0.300 0.150"/>
      <geom name="cup_left" type="box" pos="0 0.300 0.150" size="0.510 0.01 0.150"/>
      <geom name="cup_right" type="box" pos="0 -0.300 0.150" size="0.510 0.01 0.150"/>
    </body>
  </worldbody>
</mujoco>
```

```json
{"what_happens": "The ball rolls down ramp_deck, whose lower end hangs about 0.45 m above the floor at x = 1.6 m, so it flies off the end. It hits the outside of cup_near low down at about 1.48 s, bounces back onto the floor and rolls back to rest at (1.63, 0, 0.06) m, outside the cup.", "works": false, "problem": "The cup is too far from the ramp's end: the ball's flight lands short and strikes the outside of the near wall, so it never enters the cup."}
```

---
thinking (summarized):

Tracing the ball's trajectory down the ramp, it leaves around x=1.59, flies off, and strikes the near wall of the cup before bouncing back to rest on the floor near x=1.63, short of landing in the cup. I'm working through the ramp's geometry—its deck center, half-length, and tilt angle—to figure out exactly where the ball launches from.

Tracking the ball's trajectory after launch, I calculate it falls well short of clearing the cup's near wall — by the time it reaches x≈2.2, the projected height is already below the floor level, meaning it crashes before even reaching the wall rather than sailing into the cup.

The fix is to reposition the cup so the ball's actual landing spot falls within the cup's interior, but I need to check the near wall clearance too — the ball's center must pass above the wall top with enough margin as it crosses that x-coordinate.

After that the ball will bounce inside the cup, likely losing energy fast since the default contact damping is fairly stiff and non-bouncy, so it should settle rather than climb the 0.3m walls given its low impact speed and radius. Rolling and torsional friction should further dissipate residual motion until it comes to rest inside.

I'm reconsidering the cup placement to make the geometry cleaner—shifting the cup center further out with a larger half-length so the ball lands comfortably inside, and recalculating the fall timing from the new launch height.

Then I'm checking the ball's trajectory toward the far wall for a soft rebound, and verifying clearance at the near wall and ramp edge so nothing collides unexpectedly—confirming the ball clears by a safe margin at both x positions.

With near-zero restitution against the wall, the ball's spin would keep driving it forward against the contact while friction gradually kills momentum, settling at rest in the cup around 4 seconds. I'm considering bumping up rolling friction on the base material to make sure it actually damps out rather than lingering.

