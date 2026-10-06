**Expected behaviour**

The ball starts resting on the high end of the ramp deck. The deck rises from x = 0 at z = 1.0 down to x = 1.6 at z = 0.45, tilted about 19°. The ball rolls about 1.57 m along it and drops about 0.51 m. Rolling resistance slows it a little, so it leaves the low edge at roughly 2.2–2.7 m/s, with its centre near (1.63, 0.53).

**The problem**

The cup's near wall runs from x = 2.19 to 2.21 and is 0.3 m tall. A projectile estimate puts the ball's centre at only about z ≈ 0.16 when its leading edge reaches x ≈ 2.13. To clear the wall, the centre would need to be above about 0.36. So the ball strikes the outside face of the near wall, bounces back, and ends up on the floor outside the cup.

**The fix**

Move the cup toward the ramp and lengthen it slightly. The new near wall sits at x ≈ 1.72, just past the deck's lip, which is at z ≈ 0.43. The ball's centre stays above about 0.41 while it passes over that wall. It then lands on the cup floor at x ≈ 2.1–2.2, well inside the new interior (1.73–2.71). The wall contacts are critically damped and rolling friction removes the remaining speed, so the ball settles inside the cup well before 6 s.

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
    <body name="cup" pos="2.2200 0 0">
      <geom name="cup_base" type="box" pos="0 0 0.01" size="0.500 0.300 0.01"/>
      <geom name="cup_near" type="box" pos="-0.500 0 0.150" size="0.01 0.300 0.150"/>
      <geom name="cup_far" type="box" pos="0.500 0 0.150" size="0.01 0.300 0.150"/>
      <geom name="cup_left" type="box" pos="0 0.300 0.150" size="0.500 0.01 0.150"/>
      <geom name="cup_right" type="box" pos="0 -0.300 0.150" size="0.500 0.01 0.150"/>
    </body>
  </worldbody>
</mujoco>
```

```json
{"what_happens": "The ball rolls down the 19-degree ramp and leaves its low edge at about 2.2-2.7 m/s from a height of about 0.53 m. It falls short of clearing the 0.3 m near wall of the cup at x=2.19, hitting the outside of that wall at about z=0.16. It bounces back and comes to rest on the floor outside the cup.", "works": false, "problem": "The cup is too far from the ramp, so the falling ball hits the outside of the cup's near wall below its rim instead of landing inside."}
```

---
thinking (summarized):

I'm working out the ramp deck geometry, calculating its tilt angle and endpoints based on rotating around the y-axis by about 19 degrees from its center point.

I'm checking whether the ball's position aligns with the deck's top surface by computing the offset along the surface normal, confirming it rests properly at around 0.14 along x. I'm also verifying the leg support near x=0 doesn't collide with the ball given their respective widths and positions, then computing where the deck's low end sits in world coordinates to see where the ball would roll off.

Now I'm calculating how far the ball still needs to travel along the ramp's axis to reach the low end, about 1.57 meters, which gives a drop height around 0.51 m. I'm applying the rolling-sphere energy equation (v² = 10/7 g h) to find the ball's exit velocity at the bottom of the ramp.

Then I'm setting up the projectile motion: the ball leaves the ramp edge with velocity components (2.53, -0.87), and I'm solving for when it falls to the cup's base height, getting a fall time around 0.226 seconds.

Checking the horizontal position at that time, the ball only reaches x=2.197, which is still inside the near wall at x=2.19-2.21. I check whether it clears the wall's top at z=0.3, but at that x position the ball's height is only about 0.158 — far too low, so it's going to strike the outer face of the near wall and bounce back rather than landing in the cup.

I need to fix this by either moving the cup closer to the ramp or lowering the wall height so the ball clears it — calculating what x-position gives z=0.36 for clearance.

Landing around x≈2.197 on the base, the ball then rolls toward the far wall at about 2.5 m/s, bounces, and needs to settle within 6 seconds. Estimating rolling resistance from the friction coefficients gives a deceleration around 0.47 m/s², which I can use to check whether it stops in time.

Checking the bounce dynamics against the far wall: the contact's critically-damped solref means very low restitution, so the vertical impact speed mostly gets absorbed rather than bounced back, while the horizontal speed transitions from sliding to pure rolling, cutting it down to roughly 1.8 m/s before the collision damps out most of the remaining energy.

I should instead reposition the cup near the far wall so it's wide enough to catch the ball safely. Placing the cup center around x=2.2 with a half-length of 0.45 puts the far wall at 2.65, leaving the ball's landing point at 2.197 comfortably inside with margin to spare, while the near wall still clears the deck edge.

Checking the clearance near the wall edge confirms the ball passes well above the wall height at that point, so it should clear fine. I'm also confirming the physics holds up: friction is sufficient for the ball to roll down the 19° ramp without slipping, and rolling friction will only slightly decelerate it during flight down the ramp, which shouldn't meaningfully affect the landing calculations.

Even at v=1.5, landing stays around 1.96, which is fine, though clearance near the wall gets a bit tight — still workable above v=2. My rolling friction model is an approximation of MuJoCo's soft constraint, which seems reasonable, but I'll give the cup more margin by moving the near wall to 1.72 with the cup's half-length at 0.5, putting its center at 2.22 and the far wall at 2.72, keeping the wall height as is.

The cup's base sits flush on the floor as a static body, which is fine. Checking the rest timing: after landing around 1.4s, with horizontal speed near 1.5 m/s and rolling deceleration of 0.47, it should stop within about 3 seconds and travel roughly 2.4m, which the walls will contain comfortably. I'll finalize the file with the cup positioned at 2.22 and half-length 0.5.

