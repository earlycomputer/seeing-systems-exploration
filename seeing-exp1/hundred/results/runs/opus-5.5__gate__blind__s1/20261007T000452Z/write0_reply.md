Below is a rolling-ball chain laid out along +x. I worked out the timings by hand but have not run the file, so the transfer speeds are estimates. The two least certain spots are the slider push and where the block crosses the hoop.

1. **Ball and ramp.** The ball starts 1 m along a 20° ramp, measured on the slope, so it begins about 0.34 m higher than the ramp's foot. It rolls onto the floor at about 2 m/s.
2. **Paddle.** The ball hits the hanging paddle near its bottom and keeps pushing it until the paddle lifts clear. The ball is 0.5 kg, much heavier than the paddle.
3. **Slider.** The paddle shoves the frictionless slider, which runs about 0.14 m to its joint limit. The slider is expected to reach roughly 0.5–0.7 m/s.
4. **Block.** The slider pushes the block off the ledge's edge. The block and ledge use low friction (0.15) so the push carries the block off.
5. **Hoop and box.** The block drops about 0.15 m through a wide octagonal hoop (inner radius about 0.15 m) into a floor box, where it settles.
6. **Ball afterwards.** The ball passes under the slider, ledge and hoop and stops against the box's outer wall. A small rolling friction lets it come to rest.

```xml
<mujoco model="ball_ramp_paddle_slider_block">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.5 -1 3" dir="0 0.3 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="ramp" pos="-0.5706 0 0.1864" euler="0 20 0">
      <geom name="ramp_deck" type="box" size="0.6 0.1 0.02" rgba="0.6 0.4 0.2 1"/>
    </body>

    <body name="ball" pos="-0.9226 0 0.3890">
      <freejoint name="ball_free"/>
      <geom name="ball_geom" type="sphere" size="0.05" mass="0.5" friction="0.5 0.005 0.002" condim="6" rgba="0.8 0.1 0.1 1"/>
    </body>

    <body name="paddle" pos="0.5 0 0.6">
      <joint name="paddle_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="paddle_plate" type="box" size="0.01 0.08 0.29" pos="0 0 -0.29" mass="0.2" rgba="0.2 0.4 0.8 1"/>
    </body>

    <body name="slider" pos="0.68 0 0.40">
      <joint name="slider_slide" type="slide" axis="1 0 0" limited="true" range="0 0.14"/>
      <geom name="slider_bar" type="box" size="0.15 0.03 0.03" mass="0.1" friction="0.1" rgba="0.2 0.7 0.3 1"/>
    </body>

    <body name="ledge" pos="0.86 0 0.35">
      <geom name="ledge_shelf" type="box" size="0.06 0.08 0.01" friction="0.15" rgba="0.5 0.5 0.5 1"/>
    </body>

    <body name="block" pos="0.90 0 0.40">
      <freejoint name="block_free"/>
      <geom name="block_geom" type="box" size="0.04 0.04 0.04" mass="0.1" friction="0.15" rgba="0.9 0.7 0.1 1"/>
    </body>

    <body name="hoop" pos="1.04 0 0.25">
      <geom name="hoop_s0" type="capsule" size="0.01" fromto="0.1571 0.0651 0 0.0651 0.1571 0" rgba="0.7 0.2 0.7 1"/>
      <geom name="hoop_s1" type="capsule" size="0.01" fromto="0.0651 0.1571 0 -0.0651 0.1571 0" rgba="0.7 0.2 0.7 1"/>
      <geom name="hoop_s2" type="capsule" size="0.01" fromto="-0.0651 0.1571 0 -0.1571 0.0651 0" rgba="0.7 0.2 0.7 1"/>
      <geom name="hoop_s3" type="capsule" size="0.01" fromto="-0.1571 0.0651 0 -0.1571 -0.0651 0" rgba="0.7 0.2 0.7 1"/>
      <geom name="hoop_s4" type="capsule" size="0.01" fromto="-0.1571 -0.0651 0 -0.0651 -0.1571 0" rgba="0.7 0.2 0.7 1"/>
      <geom name="hoop_s5" type="capsule" size="0.01" fromto="-0.0651 -0.1571 0 0.0651 -0.1571 0" rgba="0.7 0.2 0.7 1"/>
      <geom name="hoop_s6" type="capsule" size="0.01" fromto="0.0651 -0.1571 0 0.1571 -0.0651 0" rgba="0.7 0.2 0.7 1"/>
      <geom name="hoop_s7" type="capsule" size="0.01" fromto="0.1571 -0.0651 0 0.1571 0.0651 0" rgba="0.7 0.2 0.7 1"/>
    </body>

    <body name="box" pos="1.06 0 0">
      <geom name="box_bottom" type="box" size="0.21 0.21 0.005" pos="0 0 0.005" rgba="0.4 0.3 0.2 1"/>
      <geom name="box_wall_left" type="box" size="0.005 0.21 0.055" pos="-0.205 0 0.065" rgba="0.4 0.3 0.2 1"/>
      <geom name="box_wall_right" type="box" size="0.005 0.21 0.055" pos="0.205 0 0.065" rgba="0.4 0.3 0.2 1"/>
      <geom name="box_wall_front" type="box" size="0.21 0.005 0.055" pos="0 -0.205 0.065" rgba="0.4 0.3 0.2 1"/>
      <geom name="box_wall_back" type="box" size="0.21 0.005 0.055" pos="0 0.205 0.065" rgba="0.4 0.3 0.2 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="-0.9226 0 0.3890 1 0 0 0  0  0  0.90 0 0.40 1 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm sketching out a Rube Goldberg chain layout along an axis, trying to pin down the ramp geometry and where the ball starts so the physics works out consistently.

Then I'll lay out the rest of the sequence: a paddle swinging like a pendulum to hit a slider, which strikes a block off a ledge, dropping through a hoop into a box. I want each piece to be simple geometric shapes so the physics stays predictable and robust.

For the ramp itself, I'm working out the exact rotation and placement so the low end meets the floor cleanly at the origin, computing the sine/cosine offsets needed to align the top surface properly.

I'll place the ball 1 meter up the ramp from the bottom, computing its center as offset from the surface by the radius along the normal, keeping it within the ramp's 1.2 m length. At the bottom, the ramp meets the floor around x≈0, so the ball should transition smoothly onto the floor as it rolls down, eventually moving at roughly 2 m/s once on flat ground.

Now I'm working out the paddle geometry: it hinges at some height with a rod hanging down to a flat plate near z=0.02-0.05, positioned at x=0.5 so the rolling ball strikes it about 0.35 m below the hinge. I'm checking the rotation direction about the y-axis to determine which way the paddle's bottom swings when struck.

I need the paddle's swing to eventually hit the slider, so I'm thinking through placement options—either letting the paddle swing as a simple pendulum and positioning the slider where the bottom arcs to, or restructuring it as a lever with the ball striking one arm while the opposite arm strikes the slider.

I'm computing the paddle's hinge position and arc so the slider sits above the ball's path (to avoid the ball itself hitting it directly) but within reach of the swinging paddle tip.

Contact happens quickly after a small rotation, then the paddle pushes the slider while the ball passes underneath near the bottom, clear of the slider's height. Since the slider uses a slide joint along x, gravity perpendicular to that axis doesn't matter, but I should add some damping so the slider doesn't drift indefinitely after impact.

I'm adding a range limit to the slider joint so it stops right after pushing the block, and working out the geometry for the ledge and block placement relative to the slider so everything lines up without interference.

Now I'm worried the rolling ball will keep moving in +x and collide with the box below the ledge after the block drops. I need to think about whether to offset things in y or add a stopper wall so the ball's path doesn't conflict with the falling block and box.

I'm also reconsidering whether the "at rest" condition applies to the ball specifically, and deciding to give it rolling friction via a higher condim and specific friction parameters so it eventually decelerates naturally rather than rolling forever.

I could offset the ledge/hoop/box setup in y to avoid interfering with the block, but then the slider mechanics get tricky—maybe a paddle hinged on a vertical axis like a swinging gate, pushed by the ball, that transfers motion to the slider along y. That seems overly complex though; simpler might be to keep the ball moving along x and add a wall to redirect it instead.

Actually, having the ball roll into the outer wall of the box and bounce off is physically fine—rolling friction will slow it down and it'll eventually settle. I'll tune the ball's mass (around 0.3 kg for a 0.05 radius sphere) and rolling friction so it stops at a reasonable point near the box, then work out the paddle's mass next.

The ball stays in contact with the paddle until its bottom edge rises above z=0.1, which needs φ>38°, so the push transfers through paddle into slider, whose effective mass at the contact radius works out to about 0.037 kg — quite light compared to the ball.

Estimating velocities: ball pushes paddle giving slider roughly 0.43× ball speed, about 0.8 m/s, which then carries frictionlessly into the block at the ledge. That collision transfers momentum so the block ends up moving near 1 m/s, then decelerates under friction at about 4.9 m/s² as it slides toward the ledge edge, where I need to position the block close enough to actually fall off.

I'm also working out the ledge height and fall trajectory so the block, launched horizontally at roughly 0.8 m/s, lands correctly relative to a hoop and box setup below, adjusting ledge height and box wall dimensions accordingly.

I'm reconsidering the layout since the ball rolling along the floor would just hit the box directly rather than interacting with the hoop or paddle meaningfully. I'm weighing options like making the paddle heavier to slow the ball, letting it oscillate back and forth with rolling friction eventually damping it, or repositioning the box so the ball naturally settles there instead of needing to clear a wall.

Calculating actual numbers: with μr=0.01 the ball decelerates too fast and stalls before reaching the paddle again, so I try μr=0.003 instead, redoing the ramp and friction math to see if the ball still arrives with enough speed to hit the paddle meaningfully.

Rather than relying purely on friction-based stopping, I'm considering adding a separate fixed stopper body for the ball to collide with, letting contact physics handle the deceleration naturally after impact.

Actually the box's own outer wall could serve as that stopper, since the box is fixed and won't be disturbed by the collision. I still need to work out the x-axis geometry carefully—making sure the ball clears the ledge and hoop, the hoop sits properly above the box for the block to fall through, and the ball's resting point relative to the box's left wall all line up correctly.

I'm reconsidering the layout: raising the slider height to 0.35 with the paddle hinge at 0.5, adjusting the ledge top to 0.31 so the block center sits at 0.35, and defining the box floor, wall height, and hoop position so the falling block clears everything properly.

Now I'm working through the fall timing—block dropping from 0.35 with horizontal speed around 0.8 lands at z=0.2 after about 0.175s, traveling roughly 0.14 in x, but since the block will likely tip and rotate off the edge I need the hoop sized generously (ring radius ~0.12) to catch it reliably regardless of orientation, which makes me reconsider slowing the slider's push so the block trickles off more predictably.

I'm computing the drop timing and clearance through the hoop given the landing speed range, checking that the block's trajectory stays within the hoop's inner radius with some margin for rotation. Tipping seems negligible at higher speeds since the block crosses the edge quickly, so I'm considering tuning the slider-to-block mass ratio to narrow the velocity spread further.

Since I can't run a real simulation, I'm padding the design with margin: enlarging the hoop's inner radius and building it from capsule segments, widening the box below, and checking clearances for the ball rolling under the ledge, slider, and hoop given their heights. I'm also verifying when the paddle stops being pushed by the ball based on the bottom edge height during rotation.

I'm tracing through the geometry again: checking the paddle's swing radius against the slider position, confirming the paddle hangs at rest with a small gap before contact, and considering what happens after the ball passes — the paddle will swing as a pendulum and may strike the slider again once it has moved further along.

I'm also working out the ball's dynamics more precisely, setting rolling friction parameters for the ball-ramp contact and computing the resulting deceleration and acceleration values to track speed as it travels down the ramp toward the paddle.

After the ramp ends, I'm estimating the ball's horizontal velocity after transitioning from slope to flat ground, factoring in losses from the vertical component and friction over the remaining 0.5m travel. Then I'm starting to model the collision between ball, paddle, and slider, considering mass and contact radius for the energy/momentum transfer.

Working through the restitution model: with MuJoCo's default near-critically-damped contact, the bounce is mostly inelastic, so the slider likely settles around 0.5 m/s, but the ball's spin (about 36 rad/s vs. rolling speed) means friction keeps driving it forward, continually pushing on the paddle rather than separating cleanly.

To get more slider speed, I try repositioning the contact point lower on the paddle — testing r_s=0.25 with r_b=0.45 gives an effective mass ratio that raises slider velocity to about 0.69 m/s, which is better. But that changes the ledge height and hoop placement, so I'm considering raising the hinge to compensate.

I then recheck with hinge z=0.6, paddle length 0.58, ball radius 0.55, slider at r_s=0.3 — computing the moment of inertia and effective masses gives a similar slider speed around 0.69-0.7 m/s, so this configuration seems consistent.

Now I'm thinking about the collision between the slider (mass 0.2) and a block (mass 0.1): treating it as inelastic gives both moving at roughly 0.47 m/s, after which the block decelerates due to friction.

Since the slider itself is frictionless, it doesn't stop at the collision — it keeps pushing the block forward. With friction only acting on the block (about 0.49 N), the combined deceleration is around 1.6 m/s², which only causes a small speed loss over the remaining 0.06 m, so the block exits at roughly 0.45 m/s while the slider continues pushing it the whole way. I want to set the slider's travel limit so it naturally stops right as the block clears the ledge edge, ensuring the block gets pushed fully off rather than stalling partway.

Now I'm placing the block close to the edge to minimize tipping risk, and considering lowering ledge friction to 0.3 for more consistent exit speed. I'm working out exact coordinates — hinge position, paddle geometry, contact points, and slider dimensions — to figure out where the slider's center and ends should sit, and what slide range to use so the block ends up positioned correctly relative to the ledge.

The 1cm gap is fine since slider motion is constrained by the limit, not needing collision exclusions. For slider travel: I need the block fully clear of the ledge, so block's left face should pass 0.80, meaning slider's right end travels from 0.69 to about 0.80, giving a range up to roughly 0.12 after the initial gap — though the limit will stop the slider abruptly while the block keeps moving. Now I'm tracing the ball's path to confirm it passes under the slider correctly.

Then I'm checking the tipping and fall sequence: once the block's center crosses the ledge edge at 0.78, it takes about 0.09s at 0.45 m/s for the left face to clear 0.82, triggering gravity-driven rotation. After that, I'm estimating fall time to the floor (about 0.156s from a 0.12m drop) and the resulting horizontal displacement, checking that the hoop's ring sits high enough (bottom at 0.17) to clear the floor tolerances while the ball passes beneath it.

I'm then verifying clearance for the falling, rotating block relative to the hoop's position — with the hoop centered around x=0.9 and spanning roughly 0.77–1.03 given a safety radius of 0.13, and the block's half-diagonal extent of about 0.057 in the rotated frame, confirming there's no collision as long as the block's center stays between 0.83 and 0.97.

Now I'm working out the geometry for the hoop itself, modeling it as eight capsule segments forming an octagon with circumradius R=0.14, giving an inner clearance radius of about 0.119, and placing each segment's midpoint tangentially around the ring using 45° angular spacing from the center at x=0.9, y=0.

Finishing the remaining vertices and checking placement — the hoop sits clear of the ledge and ball path, and I'm verifying it doesn't collide with the paddle's swing range near x≈0.5.

Now I'm checking the paddle dynamics: it pivots until the bottom clears z=0.1, requiring swing angle past about 30.5°, and estimating the angular velocity and energy balance gives a max swing angle around 26°, confirming it stays clear of the hoop.

But I realize the paddle's horizontal displacement at r=0.3 reaches 0.15 right around 30°, which is exactly the slider's travel limit — so the paddle could jam against the slider at its endpoint before swinging further. If that happens, the paddle stops near 30°, leaving its bottom edge at about z=0.098, which is tight against the ball's clearance.

Maybe instead of relying on the ball slipping under the paddle, I should let the paddle absorb and stop the ball directly, or redesign the hinge placement — like putting the pivot lower or using an inverted lever arm with a counterweight so gravity resets the paddle without needing the slider to do all the work. That feels more promising than fighting the slider's limited travel.

Let me reconsider the geometry: shrinking r_s to 0.2 pushes the paddle's blocking angle to around 53°, which seems safely unreachable. But that changes the effective slider mass and speeds, so I need to recompute velocities to check the slider still reaches a reasonable ~0.5 m/s without the ball losing too much momentum.

Checking whether other elements interfere — the slider's new height sits above the ledge and block, and I'm verifying the ball still clears the hoop opening. I also need to check whether the swinging paddle at larger angles could physically collide with the ledge or hoop structure, since at 45° its tip extends far enough that it might clip the hoop's position.

I'm checking the slider's left end position against the paddle angle, trying to pin down where the collision occurs geometrically — getting around 44° when accounting for the slider's bottom corner offset.

Now verifying the ball clears the slider at that angle since the bottom height (0.18) exceeds the minimum passage (0.1), but I need to check whether the paddle then intersects the hoop's ring at z=0.25 — tracing the paddle line's x-position at that height shows it crosses near the hoop's edge around x=0.77-0.84, so I need to check for a collision there too.

Actually the paddle appears to poke inside the hoop opening without touching the ring, but this risks blocking the falling ball right as the paddle swings through — bad timing overlap. I should spread the ledge and hoop farther apart in x to avoid this conflict.

I'm recalculating a longer slider setup: paddle hinge at (0.5,0,0.6) with length 0.58, slider spanning from x=0.53 to 0.83 centered at 0.68, block positioned just past the slider's right end near x=0.90, and ledge placed under the slider's right portion from x=0.80 to 0.92 to support the block before it drops.

Now I'm working out the slider's travel range (0 to 0.14) needed to push the block off the ledge, then tracking where the block falls and lands relative to the hoop, placing the hoop center around x=1.04 with radius 0.14 so it catches the falling block without clipping the ledge.

Checking the paddle's maximum reach when blocked by the slider at its limit, the paddle tip lands around (0.90, 0.18), just below and clear of the hoop ring's left edge — confirming no collision between paddle and hoop given the octagon's flat-side geometry.

The box sits on the floor centered at x=1.06, with inner walls spanning roughly 0.89 to 1.23 and height 0.12, well under the hoop's 0.24 — so a falling block should land safely inside around x~1.05. Meanwhile the ball rolls toward the box's left outer wall near x=0.88, passing beneath the paddle's reach, then rebounds slightly and loses speed to rolling friction before settling.

MuJoCo's low restitution means the ball won't bounce back far, and with forward spin plus friction decel around 0.28, it should come to rest fairly quickly after bumping the wall. I'm double-checking the ball's path from the ramp exit near x=0 to where it meets the paddle around x=0.44, then continues to x=0.83 — confirming the geometry lines up before it reaches the box.

Now I'm thinking through the block falling into the box: with 0.12-high walls it should settle after a small bounce, and I need to lower friction values for the block and ledge to 0.3 so the contact friction (which uses the max of the two surfaces) comes out reasonable against the box floor and slider, checking whether the slider's default friction of 1 against the block might cause unwanted lift in the vertical direction.

I'm also working through the paddle-ball contact: since the ball is spinning with forward rolling motion, the contact point velocity points downward, meaning friction from the paddle pushes the ball slightly upward while reacting downward on the paddle — a minor effect I'm accounting for in the friction setup.

Checking rolling friction requirements on the ramp, I find μ≥0.104 suffices, so a ball friction of 0.5 is plenty, and since contact friction uses the max of the two surfaces, the paddle's friction value doesn't matter much here. I'm also confirming contact dimensionality (condim) settings between ball-floor and ball-paddle default to the higher value of 6, which supports rolling friction properly, and verifying the slider and ledge geometry leaves enough gap that no contact margin issues occur.

Working through initial positions, the block rests stably on the ledge with its center just inside the edge, and the slider and paddle start at equilibrium with no unwanted drift. Then I estimate the ball's motion timing down the ramp — accelerating at roughly 2.14 m/s² over 1 m takes about 0.97s, then it travels the remaining 0.44m at near-constant speed in about 0.23s, hitting around the 1.2s mark, after which the slider's push on the block happens quickly within roughly 0.2s.

I'm now checking whether the slider delivers enough momentum: after an inelastic collision with the block its speed drops to 0.6 times its original, and it must overcome friction (deceleration ~1.18 m/s²) to travel 6-8 cm, which requires an initial slider speed above roughly 0.43 m/s — so I need to make sure the slider's pre-impact velocity clears that threshold, otherwise the block won't fall off the ledge as intended.

Maybe bumping ball mass to 0.5 kg gives more sustained momentum transfer, letting the slider reach a sturdier speed even with lighter slider/block masses and moderate friction. I'm checking that block-box contact still uses friction 1 regardless, and that a heavier ball keeps pushing the chain long enough for the slider to hit near 1 m/s, then working out the block's fall time from the ledge to the hoop.

Now I'm sizing the hoop radius so the block's landing window lines up with the achievable speed range — trying R=0.17 so the hoop's inner opening comfortably covers center positions around 0.97–1.15, matching where the block would cross given speeds from 0.4 to 1.0 m/s.

I'm now working through the slider/paddle dynamics: with the paddle acting at r=0.2 and the ball hitting at r=0.55, the slider velocity comes out to roughly 0.36 times the ball's velocity, so around 0.6 m/s during contact. I'm checking whether the ball keeps pushing the slider throughout contact or separates early, since that affects whether the block actually reaches the needed 0.5–0.7 m/s to land inside the hoop window.

Tracking through the mechanics: the slider's travel limit works out to about 0.14, with the paddle pushing it roughly 0.08 by the time the ball passes under at 30°, leaving the slider to coast the remaining 0.06 on its own momentum before decelerating with the paddle. Then the slider contacts the block after about 0.03 more travel, pushing it 0.11 before the block falls off somewhere in the 0.10–0.14 range of slider travel.

Checking the contact geometry more carefully: the paddle face tilts as it rotates, so the contact point slides down the face while the ball stays at fixed height, and friction forces on the ball (bounded by μN against its small normal force) seem low enough not to cause it to climb unexpectedly. The ramp and ball-wall collision also check out fine given the ball's 0.5 kg mass and modest speeds, with rolling friction of 0.002 giving a gentle deceleration afterward.

With MuJoCo's default solver, the spring response should be fairly critically damped, so bounce off the wall is minimal. The spin imparted at impact (~24 rad/s) means the ball's friction against the floor could drive it back toward the wall and pin it there, while friction with the wall itself might push the ball to climb slightly, but since the required friction exceeds what the small spin-driven normal force can generate, it should settle down safely before the 6-second mark, with impact occurring around 1.5 seconds and spin dissipating afterward.

I'm also checking other contacts: the cube resting in the box stays static, ball-wall collision doesn't shake anything, the paddle-ball interaction looks geometrically fine given their heights, and the ramp-to-floor transition at the origin edge is a clean handoff with no bump. I should also double check the paddle hinge setup next.

For the keyframe, I'm matching default body positions so qpos aligns correctly across the 16 values needed—covering ball (7), paddle hinge (1), slider (1), and block (7), listed in body order in the file, starting with the ball's position and orientation quaternion.

Now I'm double-checking the ball's resting position against the ramp geometry: taking the ramp surface point and offsetting by 0.05 along the normal direction confirms the ball center sits at roughly (-0.9226, 0, 0.3890). I'm also recomputing the ramp's own center coordinates using the cosine/sine offsets for the 20-degree incline, arriving at approximately (-0.5706, 0, 0.1864).

With that settled, I'm turning to the physical setup: assigning masses to each object (sphere, paddle, slider, block) and noting the slider's inertia doesn't matter here. Then I'm laying out the box's collision geometry -- the bottom panel and four thin wall pieces positioned around the edges at the correct heights and thicknesses to contain the ball.

Checking positions, I confirm the ball settles well clear of the paddle tip and the box walls, with the ledge sitting above the box and its edge clearing the box's inner wall so a dropped block falls cleanly inside. Now I'm computing the hoop's vertex positions from its radius and center using trig to place it correctly.

Working out whether a block tipping off the ledge edge clears the ring's inner flat side, I calculate that the block's center needs to be roughly 0.97 or beyond at that height, and with a slider velocity around 0.4 m/s over about 0.15 seconds, the block should travel far enough to clear it, though if the slider moves too slowly the block might just trickle off near the edge instead.

Checking clearances again — paddle tip near x=0.84-0.85 at full swing stays just clear of the ring at 0.873, and the box's left wall at 0.855-0.865 sits safely below the paddle's swing height. Good enough margins, so I'll move to writing the XML geoms, computing the hoop's octagon-style vertices from radius 0.17 using the a=0.1571, b=0.0651 offsets.

Still writing XML...

Setting up the slider joint along the x-axis with a 0-0.14 limited range, friction values for the ball, block, ledge, and slider, plus degree-based compiler defaults and a 20° ramp tilt. Adding a light source and double-checking the paddle hinge is positioned at the body origin, with the body itself placed at (0.5, 0, 0.6).

