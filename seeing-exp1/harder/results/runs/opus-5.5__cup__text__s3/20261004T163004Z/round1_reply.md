**Expected behaviour:** the ball rolls down the 19° ramp, flies off the end, and hits the outside of the cup's near wall. It never reaches the cup.

**Geometry check.** The ball starts resting on the high end of the ramp deck. Its centre is about 1 mm above the surface, which is fine.

The deck's lower end is not on the floor. It stops in mid-air at about x = 1.6 m, z = 0.45 m.

**Speed at the ramp end.**
- The ball drops about 0.51 m along the ramp.
- Rolling, with a little rolling resistance, gives it about 2.5–2.7 m/s.
- It leaves the ramp moving forward at about 2.4–2.5 m/s and downward at about 0.85 m/s, with its centre near (1.63, 0.53).

**Flight to the cup.**
- The near wall's outer face is at x = 2.19 and its top is at z = 0.30.
- The ball's leading edge reaches x = 2.19 about 0.2 s after launch.
- By then its centre has fallen to roughly z = 0.16, well below the wall top.
- So it strikes the outside of the near wall, drops to the floor and rolls around outside the cup.

**Fix.** Move the cup toward the ramp and lengthen it.
- New cup centre: x = 2.4. New half-length: 0.6.
- The near wall sits at x = 1.8. When the ball's leading edge reaches it, the ball's bottom is at about z ≈ 0.38, clearing the 0.30 m wall by about 8 cm.
- The ball lands on the cup base at about x ≈ 2.2. That is well before the far wall at x = 3.0.
- The landing is critically damped (solref 0.01 1), so there is almost no bounce.
- The ball then rolls into the far wall, loses most of its speed there, and settles inside the cup well within 6 s.

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
    <body name="cup" pos="2.4000 0 0">
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
{"what_happens": "The ball rolls down the ramp, launches off its raised lower end at about 2.5 m/s from a height of about 0.5 m, and strikes the outside of the cup's near wall at about z=0.16 (below the 0.30 m wall top). It then falls to the floor and rolls about outside the cup.", "works": false, "problem": "The cup sits too far from the ramp end, so the ball's flight arc drops below the near wall's top before reaching it and the ball hits the cup's outer wall instead of landing inside."}
```

---
thinking (summarized):

I'm working out the ramp deck's orientation from its pitch rotation about the y-axis, calculating how its endpoints shift in x and z based on the tilt angle.

Checking the ball's position against the deck's top surface, offset by the normal vector, and it lines up closely—about a millimeter above where expected, which is fine. But I notice the low end of the ramp actually ends up floating in the air rather than meeting the ground, meaning the ball would launch off the end at that height and fall rather than smoothly rolling down to the floor.

I'm calculating the fall height from the ramp's exit point and using energy conservation with rolling resistance to find the ball's exit speed, splitting it into horizontal and vertical components based on the ramp's angle. Then I'm checking where the ball lands relative to the cup's walls, making sure its trajectory clears the near wall of the cup before landing inside.

Actually the ball hits the near wall's outer face before reaching the cup, at z=0.159 which is below the wall top—so it bounces back instead of landing inside. This setup fails, so I need to fix it, either by extending the ramp closer to the floor or repositioning the cup so the ball actually lands inside.

Working backward, the near wall needs to sit around x≤1.80 to let the ball clear it safely, with landing around x≈2.2. After that the ball rolls forward near 2.5 m/s and could strike the far wall at 2.70 given a 0.9m cup, though critical damping in the contact solver should keep the bounce minimal.

Estimating rolling friction deceleration at roughly 1.17 m/s², the ball should bleed off speed and settle within a couple seconds after accounting for wall rebounds, though I still need to check whether the impact could launch it over the far wall entirely.

Rather than tweak the ramp, I think repositioning the cup is cleaner — placing its center near x=2.30 with a 0.45 half-length gives walls at roughly 1.85 and the ball trajectory clears the near wall top by about 5 cm margin, which should be enough once I account for ball radius.

No overlap there, that's fine. I should also account for rolling friction decelerating the ball slightly along the ramp — checking MuJoCo's friction mixing (which takes the max across contacting geoms) gives a small rolling resistance coefficient around 0.004, producing a modest deceleration of roughly 0.44 m/s², which would make the ball land a bit earlier and slightly reduce clearance margins.

Working through the reduced speed, I get v≈2.52 m/s at landing, giving clearance of about 0.44 m at x=1.80, which still looks fine. I'm now wondering whether the persisting rolling deceleration in the cup (~0.44 m/s²) plus wall/landing impacts would actually bring the ball to rest within the 6-second window, or whether horizontal velocity carries over after landing due to the ball's spin matching its rolling motion.

The critically damped wall contact should produce minimal rebound, but the ball's forward spin will keep pressing it against the far wall through floor friction, likely settling it near-rest there within the time limit -- close enough to count as "resting in a cup," though I could tighten this by increasing rolling friction if needed.

