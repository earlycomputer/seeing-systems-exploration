Ball 1 starts rolling at 2.5 m/s and passes its momentum down the line. Ball 3 then rolls up a 15° ramp, goes over the low front wall of an open-topped box cup, and drops inside.

Design choices:
- **Ball–ball contacts** are defined as nearly elastic, frictionless contact pairs. Each collision hands almost all the speed to the next ball.
- **The trailing balls** (1 and 2) keep only their spin, so they end up much slower than ball 3.
- **Rolling friction** together with the 4 cm ramp height stops the slower trailing balls before they can climb the ramp. It also brings everything to rest well before 6 s.

I have not run this. The figures below are hand estimates, not simulation results:
- Ball 3 should reach the top of the ramp at about 1 m/s.
- The trailing balls should stop before reaching the ramp.

The main risk is how bouncy MuJoCo's ball–ball contacts actually are. If they lose much more energy than intended, ball 3 may not clear the ramp, and ball 1, which keeps its spin, could end up as fast as ball 3. A test run should check those two things first.

```xml
<mujoco model="three_ball_chain_into_cup">
  <option timestep="0.002"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="0.6 -1 2" dir="0 0.4 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="ball1" pos="0 0 0.03">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.03" mass="0.1" condim="6" friction="1 0.005 0.002" rgba="0.9 0.2 0.2 1"/>
    </body>
    <body name="ball2" pos="0.15 0 0.03">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.03" mass="0.1" condim="6" friction="1 0.005 0.002" rgba="0.2 0.7 0.2 1"/>
    </body>
    <body name="ball3" pos="0.3 0 0.03">
      <freejoint name="ball3_free"/>
      <geom name="ball3_geom" type="sphere" size="0.03" mass="0.1" condim="6" friction="1 0.005 0.002" rgba="0.2 0.3 0.9 1"/>
    </body>

    <body name="ramp" pos="1.0179 0 0.0103" euler="0 -15 0">
      <geom name="ramp_geom" type="box" size="0.08 0.07 0.01" rgba="0.6 0.5 0.3 1"/>
    </body>

    <body name="cup" pos="1.19 0 0">
      <geom name="cup_base" type="box" pos="0 0 0.0025" size="0.1 0.08 0.0025" rgba="0.95 0.85 0.3 1"/>
      <geom name="cup_front_wall" type="box" pos="-0.095 0 0.02" size="0.005 0.08 0.02" rgba="0.95 0.85 0.3 1"/>
      <geom name="cup_back_wall" type="box" pos="0.095 0 0.04" size="0.005 0.08 0.04" rgba="0.95 0.85 0.3 1"/>
      <geom name="cup_left_wall" type="box" pos="0 0.075 0.04" size="0.1 0.005 0.04" rgba="0.95 0.85 0.3 1"/>
      <geom name="cup_right_wall" type="box" pos="0 -0.075 0.04" size="0.1 0.005 0.04" rgba="0.95 0.85 0.3 1"/>
    </body>
  </worldbody>

  <contact>
    <exclude name="ex12" body1="ball1" body2="ball2"/>
    <exclude name="ex23" body1="ball2" body2="ball3"/>
    <pair name="pair12" geom1="ball1_geom" geom2="ball2_geom" condim="1" solref="-200000 -5"/>
    <pair name="pair23" geom1="ball2_geom" geom2="ball3_geom" condim="1" solref="-200000 -5"/>
  </contact>

  <keyframe>
    <key name="start" qpos="0 0 0.03 1 0 0 0 0.15 0 0.03 1 0 0 0 0.3 0 0.03 1 0 0 0" qvel="2.5 0 0 0 83.3333 0 0 0 0 0 0 0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm thinking through how to stage three balls in a row, with the first ball's velocity transferring through collisions until the third rolls into a cup—and working out how the cup needs to be positioned, maybe lying on its side, so a rolling ball can actually enter it.

I'm considering using condim 6 in the physics setup to get rolling friction, so the balls naturally decelerate and settle at rest rather than bouncing out of the cup or drifting after collisions from residual spin.

I'm also weighing cup geometries: since the floor plane can't have a literal hole, a solid cup with walls needs either low enough walls combined with low approach speed, or a ramp leading up to the rim so the ball rolls up and over into the cup with just enough energy. For the ramp option I need to calculate the minimum rolling speed required to climb height H using the rolling-ball kinetic energy relation, then make sure that speed is still slow enough that the ball doesn't bounce back out once inside.

But then the collision between balls complicates things — energy transfer, spin, and slip friction all reduce each subsequent ball's speed by roughly a factor each time, so I'm tracing through how ball1's leftover spin and ball2/ball3's inherited velocities evolve to make sure they all still have enough speed to clear the ramp without overshooting out of the cup.

With dampratio 1 (critically damped), collisions become nearly inelastic, so the Newton's cradle effect won't transfer cleanly—I need to tune solref toward something bouncier, like a smaller dampratio or negative restitution values, while being mindful that the ball-floor contact uses the same mixed solref and should stay stable since balls start at rest there.

The chain reaction should push ball2 and ball3 forward with momentum, so I need rolling friction to bring everything to rest, with ball3 ideally in the cup while ball1/2 stay out. Checking the numbers: with condim 6 giving rolling resistance, a sphere of radius 0.03m and rolling friction coefficient 0.002 decelerates at roughly 0.467 m/s² — so a ball starting at 1 m/s should settle down reasonably quickly.

I'm also weighing whether the cup needs a ramp entrance, or whether a shallow tray-style cup lying with a low lip facing the balls might be simpler to design.

Settling on the ramp approach, I'm laying out positions along the x-axis: balls spaced roughly 0.3m apart starting at the origin, each with 0.03m radius resting at z=0.03, leading up to a ramp placed further along to carry a ball into the cup.

Now I'm working out the cup geometry as a small box with thin walls (thickness 0.005, height 0.05) and figuring the ramp angle (~15°) and length needed so a ball rolling down gains enough speed (around 0.84 m/s) to clear the wall rim and land inside, accounting for the ball's radius offset at the ramp's end.

I'm checking whether the ball's trajectory after leaving the ramp overshoots the far wall of the cup given its fall time (~0.1s) and horizontal speed, and whether bounces off interior walls (with some restitution) could knock it back out, since the walls are vertical and too short to let the ball roll up but tall enough that a bounce could send it over.

I'm also working out how to apply bouncy contact properties only to ball-ball collisions by using explicit contact pairs, while excluding those same body pairs from the default dynamic collision generation to avoid duplicate contacts—essentially combining `<pair>` for the special solref values with `<exclude>` to prevent MuJoCo from double-counting the interaction.

Working through the impedance math, I'm checking that with dampratio ζ=0.1 the effective restitution comes out around 0.73, which seems like a reasonable approximation despite the softer impedance mixing with actual dynamics. I'm also sanity-checking that the contact duration relative to the timestep stays physically reasonable.

But testing a few parameter choices, I find τ=0.1s, ζ=0.1 gives a contact duration of only 1.5ms, way too stiff for a 2ms timestep. Trying τ=0.02, ζ=0.2 instead gives ω≈263 rad/s, a half-period of about 12ms (6 steps), restitution e≈0.53, and penetration around 7.6mm — reasonable but not great. I also try ζ=0.15 with the same τ, getting ω≈351, duration ~9ms (4.5 steps), e≈0.62, which seems like a decent tradeoff.

I'll settle on solref values around "0.02 0.15" as a workable compromise, noting that MuJoCo's default solimp (0.9, 0.95, 0.001) means penetration depths beyond 1mm reach the full d=0.95, which should be fine here. Now I shift to setting up initial velocities, starting with the rolling ball's angular velocity about the y-axis given its linear speed and radius.

Then I work through the collision between the two balls, using restitution and friction assumptions to figure out how much linear and angular velocity each ball ends up with, then how each transitions into rolling using conservation of angular momentum about the contact point.

This is getting messy — the chain reactions could cause ball1 or ball2 to catch up and collide again, even pushing into the cup, since rolling friction decelerates everyone at similar rates and faster balls simply travel farther. I think the fix is to have ball1 collide while still purely sliding without spin, so it ends up much slower (around 0.14v0) and can't catch up — I need to think through how ball1's own roll develops given the spacing between balls.

That approach doesn't really help either and just affects floor normal forces slightly. Let me instead consider unequal masses — making ball1 lighter so it rebounds backward after impact while a heavier ball2 moves forward more slowly, checking whether the resulting velocity after the restitution formula still gives ball3 enough speed at the ramp.

Working through the numbers, ball1 nearly stops but its spin pushes it forward again to about 0.24v0, ball2 ends up rolling near 0.38v0, and ball3 only reaches roughly 0.145v0 — far too slow, and ball1 ironically ends up faster than ball2. This mass arrangement isn't working, so I need to rethink how to avoid the spin-driven follow-through problem.

I'm considering whether tuning the coefficient of restitution and rolling friction so followers decelerate to a stop before catching the leader could help, but the chained collisions make this very complicated to track cleanly. A simpler fix might be to eliminate spin effects entirely by using a very low floor friction so the balls slide instead of roll.

I'm reconsidering the collision chain order — it seems ball1 ends up moving faster than ball3 due to retained spin, which breaks the intended sequencing. Trying e≈1 instead: recalculating the speed transfers through each collision to see if ball3 still ends up with enough velocity relative to the followers.

I'm working out the solref parameters to get near-elastic collisions, thinking through how the damping ratio and stiffness terms translate into the actual constraint acceleration given the impedance blending between unconstrained and reference accelerations.

Checking the resulting contact duration and penetration depth against the ball radius, I settle on stiffness around 100000 and damping 10 as a reasonable balance between stability and bounce behavior.

Now working through the velocity chain: ball3 needs to reach the ramp with enough speed after energy losses through successive collisions, so with each transfer imparting roughly 0.975x efficiency, ball2 ends up rolling near 0.70v0 and ball3 near 0.49v0, then I need to check rolling friction decay over the remaining distance so ball2's trailing speed doesn't cause it to catch up prematurely.

I'm also realizing without rolling friction (condim 3 default), followers on flat ground would never stop and could oscillate indefinitely at the ramp base, so I need condim 6 with a rolling friction coefficient (like 0.002) set on the ball geoms so they actually decelerate to rest within the 5 cm/s stopping criterion, with friction combining by taking the max against the floor's own rolling friction value.

Good, at rest it should hold firmly. Now I'm laying out positions: balls at x=0, 0.15, 0.30, ramp foot at x=0.6, with initial speed 2.5 m/s. Working through the gap travel for each ball with the small rolling deceleration, I estimate ball3 arrives at the ramp around 1.17 m/s after losses, and I need to check whether that's enough to clear the ramp height given the rolling energy requirement plus friction and transition losses.

For the flat-to-incline transition itself, I'm reasoning through angular momentum conservation about the new contact point as the ball's center crosses onto the slope—for a 15° incline the velocity retention factor comes out to roughly 0.976, so the energy loss there is minor. With a cup wall height of 0.04 m, I'm checking what bottom velocity is required to make it over, factoring in the 1.4x rolling energy coefficient.

Working through the numbers: the threshold requirement comes to v ≥ 0.81 m/s, while ball 3 clears it at roughly 0.82 m/s—a tight margin. Checking the follower ball, its velocity falls short, meaning it rolls back rather than reaching the top, so the separation between balls is real but the margins are uncomfortably thin, making me consider increasing rolling friction to create a clearer distinction.

With v_top≈0.39 the margin feels thin given possible collision losses, so I try bumping v0 to 3: ball3's velocity squared works out to about 0.79 at the top (v_top≈0.89), which feels safer. Checking the follower ball2 at this speed, it comes out to v²≈0.76, meaning it would stop after roughly 0.81 m — so I need to track where the follower starts relative to that stopping distance.

Tracing the follower collisions: ball2 hits ball3 around x≈0.24-0.3, then travels toward the ramp at 0.94, arriving with v²≈0.11 — just enough to roll up a bit before rolling back and settling via friction. Ball1 similarly ends up stopping around 0.39 m in. These follower energies are low enough not to cause problems, so I move on to checking whether the ball clears the cup wall at v_top=0.89, factoring in the ball's center height at the ramp top.

Working through the geometry after clearing the wall: the ball becomes a projectile falling from center height ~0.071 to its resting height inside the cup (accounting for base thickness 0.005, so final center at 0.035). That gives a fall of 0.036 m, taking about 0.086s, with horizontal travel of roughly 0.077 m plus the starting offset. I need the cup's inner dimensions to be large enough to contain this trajectory — settling on roughly 0.16 x 0.12 for inner length and width, and considering whether the far wall needs extra height given the ball's incoming speed.

I'll make the walls taller (0.08) except the near wall at 0.04, giving the cup an asymmetric look while still functioning. Ball3 should land, bounce a bit, then roll back toward the near wall, where rolling friction and the wall's vertical inner face (taller than the ball radius) should keep it contained without climbing out.

For the ramp's orientation, I'm working out the correct rotation sign: since rotating about y turns +z toward +x for positive angles, I need the ramp's euler rotation to be the negative of the tilt angle so the surface normal tilts correctly toward -x, making the ramp rise in the +x direction as intended.

Now I'm computing the ramp box's geometry: given a 15° incline and 0.04 height, I'm finding the horizontal run and slope length, then working out where the box's center should sit relative to the top surface midpoint, offsetting along the surface normal by half the box thickness.

I'll extend the ramp slightly so its top overshoots the wall height by a hair rather than falling short, which avoids the ball catching on a wall edge — the overlap is negligible. Now I'm setting up the cup geometry, starting with the base plate dimensions and position.

Placing ball3 at x=0.30, then working out the ramp geometry: foot at x0≈0.9407, ramp center around (1.018, 0, 0.0103), with the box tilted 15 degrees using half-sizes 0.08x0.07x0.01. I'm computing the top corner position by adding the half-length along the slope direction and half-thickness along the normal to check it lands near (1.093, 0.041).

Then checking the bottom corner of the ramp lands just under the floor near (0.939, -0.001), confirming the ramp spans correctly. Now I'm designing the cup geometry: near wall at x≈1.095 with thin thickness, interior cavity spanning 0.18 units in x, far wall at x≈1.285 taller (height 0.08), and side walls bounding the interior at y=±0.07.

Adding side walls and base...

Working out the ball's trajectory off the ramp: launched at 15° with modest vertical and horizontal velocity, it lands within the cup floor around x≈1.17, well short of the far wall at 1.28, then rolls toward the far wall at roughly 0.8 m/s. With forward spin, it might climb slightly up that wall on impact due to friction.

After this, ball3 bounces back toward the near wall at low speed and should settle well before t=6, while ball2 reaches the ramp around 0.3 m/s, partially climbs, returns, and stops within about a second — I need to double-check whether ball1 catches up to ball2 again after their first collision.

Checking ball2's slip timing: after colliding with ball1, ball2 is still sliding (not yet rolling) when it reaches ball3 only 0.03s later, since the slip-to-roll transition takes about 0.085s. So ball2 hits ball3 at roughly 2.63 m/s rather than its fully-rolling speed, meaning I need to redo that collision with the sliding velocity instead.

Continuing the energy loss down to the ramp, I get v_top around 1.39 m/s off the edge. Checking the projectile timing, the ball's center reaches the far wall horizontally in about 0.125s, while falling takes roughly 0.13s to drop to wall-contact height — so it arrives right around the same moment it would hit the far wall.

That velocity seems a bit high though, so I'm considering dropping v0 to 2.5 instead, then rechecking the follower balls' margins with the lower speed — ball2 and ball3 still clear the needed thresholds comfortably with plenty of margin.

But I'm worried about uncertainty in the ball-ball restitution coefficient in MuJoCo — if it's worse than expected (say 0.7 instead of ideal), ball3's transferred energy drops enough that it barely fails to clear the ramp threshold, which is too marginal for comfort. I could compensate by lowering rolling friction losses over the travel distance, trading off against relying on the ramp threshold itself, and I want to estimate how much energy the follower balls carry relative to ball3 more generally.

Looking at the energy ratios: ball3 should carry roughly 4x the energy of the trailing followers, so I need the gap between ball3's energy minus the distance loss (must exceed threshold) and the follower's energy minus its distance loss (must stay below threshold) to hold across plausible restitution values. With e=0.95, ball3's v² comes out around 2.34 and the follower's around 0.56, with the combined distance+threshold requirement near 1.37 — roughly centered between those values, which feels reasonably safe. But if e drops to 0.7, I need to recheck whether ball3 still clears it.

Even raising v0 to 3 doesn't fully fix things — with poor restitution, a follower retaining spin and partial velocity can still produce a relative speed near 1.18 m/s, which actually exceeds the threshold and would cause a false trigger. So the real fix is ensuring high effective restitution through the contact solver's solref settings rather than just tuning velocities, which pushes me to think through how MuJoCo's constraint solver actually computes post-contact acceleration from the reference acceleration and damping terms.

I'm working out how solref maps to the stiffness and damping coefficients the solver uses when solref[0] is negative versus positive, since that determines the effective spring-damper behavior applied at contact.

Picking -solref0=1e5 and damping 5 gives an effective frequency of ~316 rad/s and a small damping ratio around 0.008, so I'm checking that ω·dt stays near 0.63, keeping the semi-implicit integration stable and roughly energy-conserving.

I'm also weighing extra safeguards like making the balls heavier or lowering floor friction, but those don't seem necessary. I'm considering adding contact pairs with condim 1 between balls and possibly excluding certain body pairs to avoid unwanted collisions.

Now I'm setting up the ball friction properties and confirming how condim and friction mixing work between balls, floor, cup, and ramp — the balls' higher condim should dominate. Then I'm working out the keyframe values: initial positions for the three free-jointed balls spaced along the track, and their initial velocities including rolling angular velocity.

I'm verifying the physics of rolling without slipping — checking that the contact point velocity cancels out using the cross product between angular velocity and the ball's radius vector, confirming ω = v/r gives zero slip at the contact. I note the balls start exactly touching the floor so there might be slight settling penetration, which should be fine, and now I'm considering what mass or density to assign the ball geoms.

I'm checking timing — ball3's rebound off the far wall should decay under rolling friction well within the 6-second simulation window. I also verify ball2's collision speed against ball3 gives acceptable contact penetration and stiffness values, testing a stiffer spring constant to confirm the simulation remains numerically stable with reasonable penetration depth.

Now I'm finalizing the file structure: setting floor dimensions, adding a light source, giving every body and geom explicit names (ramp, ramp_geom, floor, ball geoms), and writing out contact pair definitions with appropriate solver reference parameters for each ball-to-ball interaction, confirming negative solref values are valid for direct-mode contacts.

With gap spacing between balls set to 0.09 for initial clearance and collisions remaining elastic throughout, everything checks out, so I'm ready to write the complete file.

