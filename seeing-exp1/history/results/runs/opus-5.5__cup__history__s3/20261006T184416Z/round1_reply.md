**What happens in the run**

The ball starts at rest near the top of the ramp and rolls down `ramp_deck`, speeding up steadily. At 1.26 s it leaves the deck's lower end at about 2.4 m/s. That end sits about 0.45 m above the floor at x ≈ 1.6 and is unsupported.

The ball flies through the air and at 1.48 s strikes the outside face of `cup_near`, the cup's near wall at x ≈ 2.2. It bounces back onto the floor, rolls backward toward the ramp, and comes to rest on the floor at x ≈ 1.63, outside the cup.

**Why it fails**

The cup is too far downrange. The ball's flight from the end of the ramp lands it at about x = 2.14, which is right where the cup's near wall stands. So the ball hits the wall from outside and never gets in.

**The fix**

I moved the cup back toward the ramp and lengthened it:
- **Near wall:** its inner face is now at x ≈ 1.72. It is 0.30 m tall and sits under the falling ball. The ball's centre is still about 0.45 m high when it passes over, so it clears the wall.
- **Landing:** the ball should land near x ≈ 2.1 on the cup base, well inside the cup.
- **Far wall:** it is now at x ≈ 2.9. The ball rolls into it fairly inelastically (the ball's contact is critically damped), then settles against it under rolling friction.

I also added a second leg, `ramp_leg2`, under the low end of the ramp so the deck is not floating. It stays clear of the cup and of the ball's path.

```xml
<mujoco model="cup_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="6 6 0.1" friction="0.8 0.005 0.002"/>
    <geom name="ramp_deck" type="box" pos="0.8000 0 0.7250" euler="0 18.9704 0" size="0.8459 0.2 0.02"/>
    <geom name="ramp_leg" type="box" pos="0.0000 0 0.5000" size="0.03 0.03 0.5000"/>
    <geom name="ramp_leg2" type="box" pos="1.5500 0 0.2200" size="0.03 0.03 0.2200"/>
    <body name="ball" pos="0.1398 0 1.0376">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.06" mass="0.2" condim="6" friction="0.8 0.01 0.004" solref="0.01 1"/>
    </body>
    <body name="cup" pos="2.3100 0 0">
      <geom name="cup_base" type="box" pos="0 0 0.01" size="0.600 0.300 0.01"/>
      <geom name="cup_near" type="box" pos="-0.600 0 0.150" size="0.01 0.300 0.150"/>
      <geom name="cup_far" type="box" pos="0.600 0 0.150" size="0.01 0.300 0.150"/>
      <geom name="cup_left" type="box" pos="0 0.300 0.150" size="0.600 0.01 0.150"/>
      <geom name="cup_right" type="box" pos="0 -0.300 0.150" size="0.600 0.01 0.150"/>
    </body>
  </worldbody>
</mujoco>
```

```json
{"what_happens": "The ball rolls down ramp_deck, launches off its raised lower end at about 2.4 m/s, flies through the air and hits the outside of the cup's near wall (cup_near) at x≈2.2, bounces back onto the floor and rolls to rest on the floor at x≈1.63, outside the cup.", "works": false, "problem": "The cup is placed too far downrange, so the ball's flight off the end of the ramp lands it on the outside of the cup's near wall instead of inside the cup."}
```

---
thinking (summarized):

I'm checking the trajectory - the ball leaves the ramp and clips the cup's outer wall instead of landing inside, bounces back, and rolls to a stop short of the cup at x=1.63, so this attempt fails. I'm recalculating the ramp's endpoint geometry using its center position, half-length, and pitch angle to verify where exactly the ball launches from.

With the rotation convention, the low end sits at x=1.6, z=0.45 — meaning the ramp is floating above the floor rather than meeting it. The ball exits around 1.26s at roughly 2.4 m/s and sails past the cup's near wall entirely, so I need to redesign the ramp or cup position so the trajectory actually drops the ball inside the cup, perhaps by extending the ramp over the cup's opening or adjusting launch height relative to the cup's 0.3m walls.

Thinking through the physics: a ball rolling onto the floor can't simply enter a walled cup without clearing the wall height, so the ramp needs to end above 0.3m over the cup opening so the ball falls in and stays there without bouncing out — relying on the ball's damped contact properties and rolling friction to kill momentum once it lands inside.

The spinning ball could climb the wall on impact since the wall height of 0.3 is manageable relative to the ball radius. To tame the speed, I should make the ramp gentler and position its low end to drop the ball directly into the cup, with the deck ending around x=2.4 at height 0.36 so the ball clears the wall top at 0.30 before falling in.

I also need to verify the deck doesn't collide with the cup walls as it passes over, and double-check whether repositioning the cup under the actual landing trajectory (ball leaving the deck near x≈1.6, z≈0.53, with vx~2.3, vz~-0.78) would be simpler than adjusting ramp geometry further.

Checking the wall placement against the deck end to make sure they don't collide, then positioning the near wall around x=1.71 and confirming the ball clears it with margin. From there I'm sizing the cup so its near wall sits at x≈2.16, giving an interior span from 1.72 to 2.60 that comfortably contains the landing point near x=2.14.

Now I'm thinking about what happens once the ball enters the cup: with vx≈2.3 it only has 0.4 m to travel before hitting the far wall at a relatively mild ~2 m/s. Given the critically-damped contact model there should be minimal rebound, but I need to check whether the ball's forward spin could let it climb over the far wall on impact, since the contact point's surface velocity from rolling spin points upward at the front of the ball.

So the ball might hop slightly upward as friction resists slipping. Working out the impulse-momentum relation for a solid sphere, the friction impulse needed to stop slipping is J = mv/3.5, giving an upward velocity of only about v/3.5 — at 2 m/s that's roughly 0.57 m/s, corresponding to a bounce height around 1.7 cm, so essentially negligible.

I'm thinking the far-wall collision will kill the forward velocity near-inelastically, but residual forward spin will roll the ball back toward that wall, letting it settle there — which is exactly what I want for it to rest in the cup. The landing impact (about -2.4 m/s vertical) should be critically damped with little rebound, but since the landing x-position is a prediction with some uncertainty, I should widen the cup for margin — maybe extending the far wall out to a half-length of 0.6, placing the near wall's inner edge around 1.72.

I'm also reconsidering the ramp's support: the low end currently floats unsupported, so I'll add a second leg underneath to fix that, calculating its height from the deck's slope so it reaches up to meet the deck bottom without interfering with the cup.

Checking the impact history confirms my earlier landing estimate was accurate — the ball first hits cup_near near x≈2.14, matching my projection almost exactly. I'll finalize the file with the base size set at 0.6 by 0.3.

