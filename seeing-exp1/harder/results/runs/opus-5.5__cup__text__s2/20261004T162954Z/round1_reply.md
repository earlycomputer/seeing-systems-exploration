**What I expect to happen**

The ball starts resting on the upper end of an 19° ramp at about z ≈ 1.04. It rolls down and leaves the low end of the ramp at about x ≈ 1.63, z ≈ 0.53. It is moving at roughly 2.4–2.7 m/s, mostly horizontally.

The cup's near wall is at x ≈ 2.19–2.21 and reaches up to z = 0.30. The ball's fall puts its centre at about z ≈ 0.10–0.16 by the time it reaches that x. So it hits the outside face of the near wall, below the rim, and bounces back onto the floor. It never gets into the cup, and the scene does not match the brief.

**Fix**

I moved the cup closer, so its near wall sits just beyond and below the ramp's end, at x = 1.75. The wall tops at 0.30 are well below the deck end at ~0.45, so the cup does not overlap the ramp. The ball clears that rim with its centre near z ≈ 0.48, and lands on the cup floor at about x ≈ 2.15–2.2. The cup interior now runs from x = 1.75 to 2.75.

I also gave the cup base more rolling and torsional friction. The ramp contact is unchanged, so the descent behaves the same. Inside the cup, the ball now loses its speed quickly, and after a bounce off the far wall it comes to rest well within the 6 s.

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
    <body name="cup" pos="2.2500 0 0">
      <geom name="cup_base" type="box" pos="0 0 0.01" size="0.510 0.310 0.01" friction="1 0.03 0.03"/>
      <geom name="cup_near" type="box" pos="-0.500 0 0.150" size="0.01 0.310 0.150"/>
      <geom name="cup_far" type="box" pos="0.500 0 0.150" size="0.01 0.310 0.150"/>
      <geom name="cup_left" type="box" pos="0 0.300 0.150" size="0.510 0.01 0.150"/>
      <geom name="cup_right" type="box" pos="0 -0.300 0.150" size="0.510 0.01 0.150"/>
    </body>
  </worldbody>
</mujoco>
```

```json
{"what_happens": "The ball rolls down the ramp and leaves its low end at about x=1.63, z=0.53, moving at roughly 2.5 m/s. It flies toward the cup but is still below the 0.30 m rim when it reaches the near wall at x≈2.2, so it hits the wall's outer face, bounces back, and ends up on the floor outside the cup.", "works": false, "problem": "The cup is too far from the ramp end, so the ball's trajectory drops below the rim before reaching the cup and it strikes the outside of the near wall instead of landing inside."}
```

---
thinking (summarized):

I'm working out the ramp deck's geometry, using its pitch angle and center position to find where each end sits in z, since the rotation about y tilts the +x end downward.

With the surface normal computed, I'm placing the ball's center offset above the deck surface by its radius plus the deck thickness, then checking at the ball's starting x-position whether it sits properly on the ramp (it lands about a millimeter above, which is fine). I'm also checking whether the ramp's leg geometry at the lower end overlaps with the deck or ball, since the leg sits right where the deck terminates.

Now I'm computing the ball's exit conditions as it rolls off the end of the ramp: using the drop height from start to end (~0.512m) with rolling sphere energy conservation to get exit speed (~2.68 m/s), then resolving that into velocity components along the slope direction.

I'm then setting up the projectile trajectory from the exit point toward the cup, checking the cup's geometry (base, walls, inner opening around x=2.21 to 3.09) to figure out if the ball will clear the near wall at x≈2.19-2.21 before descending into the cup.

Solving confirms the ball still hits the wall around z≈0.158 before clearing it, so this setup fails. I need to reposition the cup so the ball clears the wall top at 0.30 — that means the ball's center must exceed 0.36 when passing over, so I should recompute the timing for that threshold instead.

Checking if placing the near wall around x=1.70 keeps it clear of the ramp since the ball is still well above the wall height there. Working out the landing point on the cup floor, I get the ball touching down near x≈2.2 with forward velocity still around 2.53, so it'll keep moving toward the far wall afterward.

Now I'm thinking through how the bounce off the far wall behaves given the contact damping and friction settings — the collision is fairly inelastic but not perfectly so, and the sliding friction should convert the slide into rolling fairly quickly, bringing the horizontal speed down toward roughly 1.8, factoring in the spin the ball already carries from rolling down the ramp.

When it bounces off the far wall at that speed, the critically damped soft contact should keep restitution small but not zero, so there's some energy loss but a slight bounce. With the near wall only 0.30 high and the ball's diameter at 0.12, it shouldn't escape unless the bounce is unusually strong, but settling within the 6 second window still feels uncertain given the combination of rolling friction and floor contact parameters.

Bumping up rolling friction to curb that uncertainty seems tempting, but I realize it would also fight against the ball's descent on the ramp—too much rolling resistance there could nearly cancel out gravity's pull down the slope, which would break the whole setup. I should either pick a smaller rolling friction value or consider shortening the cup instead so wall impacts matter less.

I could instead raise the rolling/torsional friction specifically on the cup's base contact, since it only engages once the ball lands inside—leaving ramp dynamics untouched while giving settling in the cup a boost. Checking the landing velocity confirms the vertical speed at impact is reasonable for the bounce stiffness I've set.

Now I'm laying out the cup geometry itself: centering it around x=2.25 with inner walls near x=1.75 and 2.75, checking that the near wall doesn't collide with the end of the ramp deck, and confirming the ball clears the near wall's corner with plenty of margin before landing around x=2.2, well inside the cup before the far wall.

I'm then working through the rolling friction math on the ramp itself — with the ball's rolling friction coefficient lower than the ramp's static friction, deceleration from friction is much smaller than the gravity component pulling it downhill, so the ball still accelerates down the ramp but slightly slower than a frictionless case, and after reaching the floor it decelerates further, bounces softly off the far wall, and eventually settles back toward the near wall.

Either way it still hits the outer near wall, so the original setup fails. Checking the cup's base dimensions to confirm it's sized to catch the ball, and whether a small vertical bounce could carry it over the far wall - seems fine, so I'm ready to write the final answer.

