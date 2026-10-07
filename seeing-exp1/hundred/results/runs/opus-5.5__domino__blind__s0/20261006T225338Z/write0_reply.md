The ramp is tilted 15° and descends toward +x, ending flush with the floor at x = 0. I took "1 m up ramp" to mean ball1 starts 1 m along the ramp surface from its foot, which is about 0.26 m of height.

Intended sequence:
- **Ball1 into d1:** ball1 has a 6 cm radius, so it strikes d1 at 6 cm height. That is above d1's centre of mass (5 cm), so d1 tips forward.
- **Ball1 stays out of the way:** ball1 has about the same mass as a domino and some rolling friction. It gives up most of its momentum in the hit and stalls behind the fallen dominoes, so it can't reach ball2 itself.
- **Domino chain:** each 10 cm domino falls into the next at 7 cm spacing.
- **D3 into ball2:** d3's face hits ball2 at about 26° of fall. Ball2 is a light ball sitting on a low step.
- **Into the cup:** ball2 rolls or flies off the step into the cup. The step and the cup's low near wall together block its way back.
- **Ball2 comes to rest:** ball2 has rolling friction (condim 6), so it slows down and stops inside the walls well before 6 s.

I worked this out by hand and have not run it.

```xml
<mujoco model="ramp_domino_cup">
  <option timestep="0.002"/>
  <worldbody>
    <light name="main_light" pos="0 0 2" dir="0 0 -1"/>
    <geom name="floor" type="plane" pos="0 0 0" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="ramp" pos="-0.6813 0 0.1619" euler="0 15 0">
      <geom name="ramp_plank" type="box" size="0.7 0.15 0.02" rgba="0.6 0.4 0.2 1"/>
    </body>

    <body name="ball1" pos="-0.9504 0 0.3170">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.06" density="150" condim="6" friction="0.8 0.005 0.005" rgba="0.9 0.1 0.1 1"/>
    </body>

    <body name="d1" pos="0.25 0 0.05">
      <freejoint name="d1_free"/>
      <geom name="d1_geom" type="box" size="0.01 0.04 0.05" density="600" rgba="0.1 0.3 0.9 1"/>
    </body>

    <body name="d2" pos="0.32 0 0.05">
      <freejoint name="d2_free"/>
      <geom name="d2_geom" type="box" size="0.01 0.04 0.05" density="600" rgba="0.1 0.5 0.9 1"/>
    </body>

    <body name="d3" pos="0.39 0 0.05">
      <freejoint name="d3_free"/>
      <geom name="d3_geom" type="box" size="0.01 0.04 0.05" density="600" rgba="0.1 0.7 0.9 1"/>
    </body>

    <body name="step" pos="0.46 0 0.02">
      <geom name="step_block" type="box" size="0.015 0.07 0.02" rgba="0.5 0.5 0.5 1"/>
    </body>

    <body name="ball2" pos="0.46 0 0.0651">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.025" density="300" condim="6" friction="0.8 0.005 0.002" rgba="0.1 0.8 0.1 1"/>
    </body>

    <body name="cup" pos="0 0 0">
      <geom name="cup_base" type="box" pos="0.605 0 0.002" size="0.12 0.07 0.002" rgba="0.9 0.8 0.2 1"/>
      <geom name="cup_near_wall" type="box" pos="0.48 0 0.01" size="0.005 0.08 0.01" rgba="0.9 0.8 0.2 1"/>
      <geom name="cup_far_wall" type="box" pos="0.73 0 0.035" size="0.005 0.08 0.035" rgba="0.9 0.8 0.2 1"/>
      <geom name="cup_left_wall" type="box" pos="0.605 0.075 0.035" size="0.12 0.005 0.035" rgba="0.9 0.8 0.2 1"/>
      <geom name="cup_right_wall" type="box" pos="0.605 -0.075 0.035" size="0.12 0.005 0.035" rgba="0.9 0.8 0.2 1"/>
    </body>
  </worldbody>
</mujoco>
```

---
thinking (summarized):

I need to pin down the geometry here, specifically what "1 m up ramp" means for ball1's starting position — whether that's measured along the slope surface or as vertical height. I'll go with placing it 1 meter along the ramp's incline from the bottom.

I'm settling on a 20° ramp angle with the ball starting 1 m up the slope, computing the resulting rolling speed at the bottom using the energy equation for a sphere, which comes out around 2.19 m/s — plenty to knock over a domino. I'm also working out how to orient the ramp as a rotated box so its downhill end meets the floor near the origin, using a y-axis rotation and figuring out the low-end corner position from the box's half-length and rotation angle.

Let me reduce the kink by using a 15° angle instead: that gives a drop height of 0.2588 m and an estimated speed of about 1.90 m/s down the slope, with acceptable minor energy loss at the junction. Recomputing the geometry: center z comes out to 0.1619 and cx to -0.6813, and now I'm positioning the first ball one meter along the slope from the low end.

For ball 1's radius of 0.04, the surface point one meter up translates to roughly (-0.9659, 0, 0.2588), and adding the normal offset gives a ball center around (-0.9556, 0, 0.2975), which fits comfortably within the 1.4 m ramp length. I'm second-guessing whether "1 m up the ramp" should mean distance along the slope versus vertical height, but I'll settle on measuring it as distance along the ramp since that's the more natural reading.

Now checking the domino setup: with half-sizes giving a 2cm thick, 10cm wide, 20cm tall box and 0.12 m spacing between them, the ball striking at 4cm height hits quite low on the 20cm domino. Hitting that low worries me since it might just slide the domino at its base rather than tip it over, but computing the torque balance—impulsive force times the 4cm height versus gravity times the 1cm half-thickness—suggests the force is large enough that it should still tip rather than slide.

Working through the mass estimate, the heavy ball will likely shove the domino violently, both sliding and tipping it. But hitting below the domino's center of mass could actually cause backward rotation rather than clean tipping, so I need the ball's contact point to land above the domino's COM — meaning the ball radius should exceed the domino's half-height, which constrains how short I can make the dominoes while still reaching the next one in the chain.

Let me try ball radius 0.06 with dominoes height 0.1, heavier ball (~1.8kg) versus light dominoes (~0.063kg) so it plows through the whole chain rather than stopping — but then ball1 might keep rolling and interfere with ball2 or the cup itself, so I need to think about whether d3 can still knock ball2 before ball1 catches up.

I'm wondering if a plain-walled cup even works since ball2 can't roll over a wall to get in. Maybe I need ball2 perched on an elevated edge that gets knocked off into the cup below, or a cup design with one lowered/ramped wall so the ball can enter from the side after being pushed.

I'm working out the cup geometry with back wall, side walls, and a low front lip around 1.2 cm tall. Checking whether a rolling ball with radius 2.5 cm and typical speed can actually climb over that lip, since the step height relative to radius is fairly large—rough energy estimates suggest it needs around 0.5 m/s or more to clear it.

I'm also considering alternatives, like whether the cup needs to be raised with ball2 dropping into it from a shelf, since pushing the ball over a wedge or lip might be unreliable depending on how hard the domino chain knocks it.

Actually, a pedestal could work: ball2 rests on a short post, and the falling domino knocks it sideways into a floor-level cup. I'm roughly calculating the fall trajectory from pedestal height to estimate how wide the cup opening needs to be given the horizontal velocity imparted.

Once inside, though, the ball might just keep rolling and bouncing off the cup walls without settling since MuJoCo doesn't add rolling friction by default. I'm considering giving ball2 condim 6 with rolling friction parameters, or shaping the cup bottom like a shallow bowl or V-shape so it naturally settles at the center.

Working through the physics: with rolling friction coefficient around 0.002 and radius 0.025m, deceleration comes out to roughly 0.56 m/s², which would stop a 1 m/s ball in about 2 seconds — good enough. I need to remember that MuJoCo contacts use the max condim and friction values between the two geoms, so setting ball2 to condim 6 with friction "0.8 0.005 0.002" against the floor's default friction will give the rolling resistance I want.

If I attach the pedestal as a geom on the cup body, that risks making the cup's bounding box include the pedestal location, which could falsely register ball2 as "in cup" from the start — so I should make a separate fixed "stand" body instead. I also need to account for ball1 continuing to roll after knocking over dominoes and potentially colliding with the pedestal or cup setup.

Computing the actual distance, it's just barely over the contact threshold, so no collision there. I'm now considering ways to slow ball1 down more reliably, like reducing its mass or adding rolling friction with a different contact dimension so it decelerates naturally before reaching ball2.

Estimating domino mass around 0.16 kg and ball mass around 0.45 kg, the ball hits around 1.6 m/s and tips the first domino forward hard, continuing at roughly 1 m/s to chase the falling chain since dominoes are spaced closer than their height. I'm now trying to lay out actual x-positions starting from the ramp's base at x=0.

Placing ball1's landing near x≈0, with dominoes d1, d2, d3 spaced roughly 0.07 apart starting around x=0.25, and working out the arc d3's top sweeps as it pivots forward to figure out where it might strike ball2, which sits on a pedestal at some height hp.

Checking the geometry, I find the top corner of the domino reaches the ball first rather than the face, at roughly φ≈31°, since the computed contact height exceeds the domino's own length. So I need to redo the collision condition using the corner point instead of the face line, solving for where the distance from that corner to the ball center equals the ball's radius.

Checking the pedestal won't interfere with d3's resting position or the domino's swing path — the corner clearance works out fine at φ≈48° after the ball hit. Also confirming d3's front bottom edge alignment at x=0.40 looks correct.

Now I'm estimating how fast the falling domino's tip speed is at φ=26°, roughly 0.4 m/s plus chain momentum, then sizing ball2 to be light (~0.02kg) so it gets flung off the pedestal in the direction of the contact normal, slightly downward from horizontal.

I'm now worried about the geometry after the push: ball2 slides off the pedestal at ~0.5-1 m/s and falls toward the cup, but the cup's near wall height needs to be low enough not to block the trajectory yet tall enough to retain the ball once it lands — this is a tight tolerance given the ball's radius and speed, so maybe raising the pedestal height instead would solve it.

Thinking about whether the pedestal could just double as the cup's near wall, but that risks the checker flagging ball2 as "already in the cup" at the start since it'd sit right on the rim. Safer to keep the pedestal and cup as separate bodies, with the cup's near wall placed a short distance away.

Now I'm working out the trajectory math: the ball leaves the pedestal edge around x=0.475 at z=0.065, needs to clear the near wall corner at (0.50, 0.03) with enough clearance given its radius, and at launch speed 0.5 it takes about 0.05s to reach x=0.50 with roughly 0.012 drop in height — checking whether that's enough to clear the wall without colliding.

Since it's marginal, I'm reconsidering the geometry: lowering the near wall further, repositioning it closer to the pedestal, or redesigning the cup with an inclined floor sloping away from the pedestal so the ball settles against the far wall instead of risking escape back toward the near side.

Actually that friction exceeds the slope's driving acceleration, so the ball won't roll down—it'll just settle wherever it stops, which is fine since the walls contain it anyway. I'll skip the tilted base and just keep the flat floor, relying on rolling friction (~0.001) to bring the ball to rest within a couple meters. I do need to check whether the near wall's low height (0.015) might let a fast-moving ball escape back toward the pedestal if it's still moving above ~0.4 m/s.

I'm now testing whether raising the pedestal and near wall could let the ball clear the corner without colliding—working through the geometry of a ball launched from the pedestal top, checking if its drop trajectory clears a wall corner at various speeds, and finding that at moderate velocity the ball still clips the corner by about a centimeter.

I'm worried the ball would land on the thin wall top and roll off inward rather than settling, so maybe removing the near wall entirely and relying on the pedestal to block the near side isn't reliable either—the ball could still roll back around it. I'm thinking I need a different pedestal configuration altogether.

Maybe I should add a thin base plate to the cup so it reads visually as a container, with the ball resting on it, and consider giving the cup a short near wall placed right against the step instead of leaving that side open.

Since the ball clears regardless, I'll just set the near wall height to match the step. Now I'm working out the cup's inner dimensions and checking ball2's trajectory: dropping from z=0.065 at up to 1.5 m/s, it should land within the cup bounds before bouncing off the far wall.

Then I'm tracking domino d3's fall onto the step edge after striking the ball — figuring out whether its top, pivoting at x=0.40 with length 0.1, ends up resting across the step corner near the cup's wall, computing the contact angle at the step edge.

Checking that the step geometry doesn't interfere with d3 hitting the ball first: the contact angle at the near step corner is steeper than the angle when the domino face touches the ball, so the ball gets struck before the domino reaches the step. Ball2 then settles centered on the step within its bounds, so I need to confirm it's positioned correctly to be pushed further.

Since the push has a downward component, friction partially resists but the ball's light enough to still be pushed along as the domino falls. I'm setting ball2's initial z slightly higher to avoid excess penetration into the step, and confirming domino dimensions (half-extents 0.01×0.04×0.05) and floor friction before checking ball1's contact height against domino d1.

Now I'm working out the ramp-to-floor transition point and assigning densities: ball1 at 1000 kg/m³ giving roughly 0.905 kg, and dominoes at 600 kg/m³ giving about 0.096 kg each, to get realistic collision dynamics when ball1 strikes the first domino.

Since ball1 is nearly 9x heavier than a domino, it should keep moving around 1.4 m/s after impact and continue chasing through the row, possibly catching up to subsequent dominoes before they fully topple. I'm now checking whether ball1 can clear the 0.04m step given its 0.06m radius — with h/r at about 0.67, it would likely need more speed than the ~1 m/s it has, meaning it might just bounce off the step instead of rolling over it.

Tracing the geometry more carefully, contact against the step face would put ball1's center at roughly x=0.388, and from there the distance to ball2 at (0.46, 0.065) comes out to about 0.072 — less than the 0.085 needed to avoid collision. So ball1 looks like it would smash straight into ball2, which complicates things since the goal was for d3 to knock ball2 into the cup, not ball1 colliding with it directly. I need to work out the full timeline accounting for the fallen dominoes lying flat on the floor as ball1 rolls over them.

To stop ball1 from continuing on and causing trouble, I'm considering making it lighter than the dominoes so it loses momentum on impact rather than plowing through. Since tipping a domino barely requires any energy (the center of mass barely rises), even a light, hollow ball moving fast enough can still knock it over while losing most of its own speed in the process — so I'll set ball1's density low enough that its mass roughly matches a domino's, letting the collision sap its momentum and leave it resting near d1 while the chain reaction continues.

Recomputing the ramp physics with rolling friction, I get a velocity around 1.58 m/s at the ramp bottom, dropping to about 1.51 m/s by the time it reaches d1 after floor friction losses. That seems workable, though I still need to check whether the ball's impact force at the 0.06m contact height is actually enough to topple the domino given its free body dynamics.

Checking the tipping energy needed: with the critical angle around 11 degrees, the required energy is roughly 1 millijoule, while the ball's kinetic energy at that density comes out to about 0.1 joules — plenty of margin. I'll go with density 150 for the first ball, though with similar masses the collision will leave the ball mostly stopped as it transfers momentum to the domino.

Even after the linear velocity drops, the ball's retained spin means friction will drive it forward again to roughly 2/7 of its original speed, around 0.43 m/s, decelerating and traveling about 0.16 m before stopping — not quite far enough to reach the second domino given the fallen first one blocks the path.

Checking the chain reaction: d1 tips forward and its top edge strikes d2's back face at a contact height above d2's center of mass, which should topple it cleanly, and the same geometry repeats for d2 hitting d3 and d3 hitting ball2. The only worry is that ball1's impact might make d1 slide rather than cleanly topple, but even then it should still reach and knock over d2.

For ball2's resulting speed, d3's angular velocity from the chain impulse (roughly 3-6 rad/s) gives it a push of maybe 0.25-0.5 m/s at the contact point, and since the ball is much lighter than the domino, the domino keeps accelerating it under gravity until the ball rolls off the step edge.

Checking the exit trajectory: if the ball leaves the edge around 0.3 m/s, I'm tracing its parabolic fall past the near wall's corner to confirm it clears with enough margin before hitting anything.

Then I'm checking d3's landing position after the ball leaves — its top corner lands within the cup space near the wall, which seems fine even if ball2 later approaches it. For ball2's motion once it's in the cup, I'm estimating its deceleration from rolling friction, factoring in the effective radius and starting speed around 0.8 m/s.

I'm reasoning through the collision softness in the simulation — with small ball radius and fine timestep, minor penetration should be tolerable. Then I'm working out the cup's base and wall geometry to see if the ball could hop over the near wall's lip toward the step, but since there's no gap between the near wall and the step, the ball would be blocked from escaping that way.

Still placing cup geometry...

No keyframe needed since gravity alone starts the motion. Now I'm computing ball1's starting position on the 15° ramp, offsetting from the surface point by the ball radius along the normal direction.

Working out the ramp box geometry: half-extents of 0.7×0.15×0.02, rotated 15° about y so it slopes down toward +x, centered at roughly (-0.6813, 0, 0.1619). I'm verifying the top surface coordinates at the low end match up with where the ball sits.

Then I'm sketching the timing: ball1 rolls down the ramp in about 1.3s, the chain reaction takes roughly 0.5s, and ball2 lands in the cup around 2s total.

Checking friction parameters: ball1's condim 6 setup with rolling and torsional friction should prevent it from getting stuck on the 15° slope since that angle comfortably exceeds the ~4.8° minimum for rolling. Dominoes use default friction, and I'll leave the integrator at default Euler unless timing issues emerge.

I'm setting timestep to 0.002 and considering implicitfast integrator, but deciding to keep things simple. I'm using density values on geoms to control mass—ball1 at 150 density gives roughly 0.136 kg, ball2 at 300 density—and now I'm double-checking whether the domino's push on ball2 might cause it to wedge against the step rather than roll cleanly, since the contact normal direction pushes both inward and downward.

Working through it, I conclude the ball should actually roll rather than stick: the friction from the push's downward component lets it roll forward instead of sliding, and even though domino-ball friction could add some rubbing, it shouldn't prevent rolling. Since contact friction takes the max between surfaces, the domino's higher friction coefficient will dominate regardless of what I set on ball2, but that's fine since the ball can still roll off the step over its 1.5 cm travel.

