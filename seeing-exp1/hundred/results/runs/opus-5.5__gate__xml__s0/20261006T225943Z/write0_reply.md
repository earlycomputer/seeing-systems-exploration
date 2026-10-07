The scene is a chain on a raised track, laid out along x. Gravity starts it, so no keyframe is needed.

- **Ramp:** 20° incline. The ball (1 kg) starts 1 m up the slope, measured along it.
- **Paddle:** light, hanging from a hinge with travel limited to 25°.
- **Slider:** 0.3 kg on a slide joint with 7 cm of travel.
- **Ledge:** the 0.1 kg block sits near the edge. The ledge and block both have friction 0.2, so the block slides instead of tipping.
- **Backboard:** part of the ledge body. It stops the block so it drops straight down through a square hoop into an open box on the floor.

I designed this by hand calculation and have not run it in MuJoCo. Expected timing: the ball reaches the paddle at about 1.1 s, the block leaves the ledge at about 1.3 s, and it settles in the box well before 6 s.

```xml
<mujoco model="ramp_paddle_slider_block">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <worldbody>
    <light name="main_light" pos="0 0 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="3 3 0.1" pos="0 0 0" rgba="0.8 0.8 0.8 1"/>

    <body name="ramp" pos="0 0 0">
      <geom name="ramp_incline" type="box" size="0.6 0.1 0.02" pos="-0.5236 0 0.6693" euler="0 20 0" rgba="0.6 0.4 0.2 1"/>
      <geom name="ramp_flat" type="box" size="0.3 0.1 0.02" pos="0.3 0 0.48" rgba="0.6 0.4 0.2 1"/>
      <geom name="ramp_base" type="box" size="0.75 0.1 0.23" pos="-0.2 0 0.23" rgba="0.5 0.35 0.2 1"/>
    </body>

    <body name="ball" pos="-0.9226 0 0.891">
      <freejoint name="ball_free"/>
      <geom name="ball_geom" type="sphere" size="0.05" mass="1" rgba="0.9 0.1 0.1 1"/>
    </body>

    <body name="paddle" pos="0.4 0 0.85">
      <joint name="paddle_hinge" type="hinge" axis="0 -1 0" pos="0 0 0" range="-5 25" limited="true" damping="0.002"/>
      <geom name="paddle_plate" type="box" size="0.01 0.08 0.1675" pos="0 0 -0.1675" mass="0.2" rgba="0.2 0.4 0.9 1"/>
    </body>

    <body name="slider" pos="0.605 0 0.635">
      <joint name="slider_slide" type="slide" axis="1 0 0" range="0 0.07" limited="true"/>
      <geom name="slider_bar" type="box" size="0.175 0.04 0.025" mass="0.3" rgba="0.2 0.8 0.3 1"/>
    </body>

    <body name="ledge" pos="0 0 0">
      <geom name="ledge_top" type="box" size="0.13 0.1 0.01" pos="0.75 0 0.59" friction="0.2 0.005 0.0001" rgba="0.5 0.5 0.5 1"/>
      <geom name="ledge_post" type="box" size="0.02 0.05 0.29" pos="0.70 0 0.29" rgba="0.5 0.5 0.5 1"/>
      <geom name="ledge_backboard" type="box" size="0.01 0.24 0.225" pos="1.01 0 0.575" rgba="0.45 0.45 0.5 1"/>
      <geom name="ledge_board_post_left" type="box" size="0.01 0.02 0.40" pos="1.01 0.22 0.40" rgba="0.45 0.45 0.5 1"/>
      <geom name="ledge_board_post_right" type="box" size="0.01 0.02 0.40" pos="1.01 -0.22 0.40" rgba="0.45 0.45 0.5 1"/>
    </body>

    <body name="block" pos="0.82 0 0.63">
      <freejoint name="block_free"/>
      <geom name="block_geom" type="box" size="0.03 0.03 0.03" mass="0.1" friction="0.2 0.005 0.0001" rgba="0.95 0.8 0.1 1"/>
    </body>

    <body name="hoop" pos="0.94 0 0.30">
      <geom name="hoop_bar_xneg" type="box" size="0.01 0.12 0.01" pos="-0.11 0 0" rgba="0.9 0.5 0.1 1"/>
      <geom name="hoop_bar_xpos" type="box" size="0.01 0.12 0.01" pos="0.11 0 0" rgba="0.9 0.5 0.1 1"/>
      <geom name="hoop_bar_yneg" type="box" size="0.12 0.01 0.01" pos="0 -0.11 0" rgba="0.9 0.5 0.1 1"/>
      <geom name="hoop_bar_ypos" type="box" size="0.12 0.01 0.01" pos="0 0.11 0" rgba="0.9 0.5 0.1 1"/>
    </body>

    <body name="box" pos="0.94 0 0">
      <geom name="box_base" type="box" size="0.15 0.15 0.01" pos="0 0 0.01" rgba="0.3 0.3 0.7 1"/>
      <geom name="box_wall_xneg" type="box" size="0.01 0.15 0.06" pos="-0.14 0 0.08" rgba="0.3 0.3 0.7 1"/>
      <geom name="box_wall_xpos" type="box" size="0.01 0.15 0.06" pos="0.14 0 0.08" rgba="0.3 0.3 0.7 1"/>
      <geom name="box_wall_yneg" type="box" size="0.13 0.01 0.06" pos="0 -0.14 0.08" rgba="0.3 0.3 0.7 1"/>
      <geom name="box_wall_ypos" type="box" size="0.13 0.01 0.06" pos="0 0.14 0.08" rgba="0.3 0.3 0.7 1"/>
    </body>
  </worldbody>
</mujoco>
```

---
thinking (summarized):

I need to design a working Rube Goldberg chain along the x-axis, starting with a ball on an inclined ramp positioned 1 m along the slope at roughly a 20-degree angle.

After rolling down, the ball should hit a hanging paddle that pivots on a horizontal axis, swinging to strike a slider that moves along x and knocks a block off a ledge, which then falls through a ring into a box below. I'm thinking through the physics—using rolling-without-slipping energy for the ball's speed at the ramp's base, factoring in the 5/7 coefficient for a solid sphere.

I'm now working out concrete coordinates: the paddle pivots at a fixed point, hangs down as a thin box, and needs enough swing to transfer momentum to the slider, which should have a limited range so it comes to rest after pushing the block off its ledge rather than flying away indefinitely.

I'm trying to figure out where along the paddle's swing arc to place the slider so the impact pushes it in a useful horizontal direction rather than vertically — leaning toward positioning the slider's contact face early in the swing, at a small angle, so the tangential velocity has a strong sideways component.

Since the slide joint only has one translational DOF, gravity doesn't destabilize it—the joint constrains the other axes, so the slider floats fine. The ball doesn't need a final rest state; only the block does, since it must end resting in the box. So now I need the slider to travel and strike the block sitting on a fixed ledge platform, making sure heights line up so the slider actually contacts it.

I'm reconsidering the geometry since a block dropping straight from the ledge height is too cramped to clear the hoop and box below. Instead, I could make the slider body itself have geoms at varying heights—a low pad near the paddle and a tall striker pad near the ledge, connected by a vertical bar—since it's still one rigid body on the slide joint, as long as it doesn't collide with the ledge structure.

Better yet, I'll raise the whole setup onto a pedestal of height H=0.5: the ramp, flat runout, paddle, slider, and ledge all sit elevated, so a block pushed off the ledge falls about 0.7m through the hoop into a box on the floor, giving enough clearance for everything to work cleanly. I'm now laying out the ramp body's incline and flat runout geoms at this elevated height.

I want the incline-to-flat transition to be smooth since a bump at the corner could make the ball bounce. I'm overlapping the incline and flat boxes so the flat section's top surface sits right at the junction, hidden beneath the incline's lower end, avoiding any visible seam or collision glitch. I also need a pedestal under the runout that doesn't interfere with where the block eventually falls, so I'm positioning it to span only up to where the flat section starts, keeping the falling block's landing zone clear.

For the ramp angle, I'm checking whether 15° or 20° gives a better compromise: a 20° kink loses a bit of velocity to the normal-direction impact (sin component), but retains more of the rolling speed (cos component) compared to 15°, so I'll stick with 20° and treat the small energy loss as acceptable since the contact is soft. I also want to make sure "starts 1 m up the ramp" is interpreted as the ball's center being 1 meter along the slope, measured from the bottom of the incline.

Now I'm working out the incline box's placement in the scene: computing its center position using the slope angle's sine and cosine, sizing it with a half-length of 0.6 along the slope and small thickness/width, and positioning its midpoint so it spans correctly from just below the bottom to past the top. I need to offset the box center by its half-thickness along the normal direction perpendicular to the slope, and I'm figuring out the correct sign convention for that normal vector given the slope rises toward negative x.

For orientation, I'm determining the rotation about the y-axis needed so the box's local x-axis aligns with the slope direction, settling on a +20° rotation to match the downhill-to-uphill direction correctly.

Now I'm computing the ball's starting position: placing it at s=1.0 along the slope, offset by the radius along the surface normal from the slope face, with a small clearance to avoid penetrating the ramp, giving coordinates around (−0.9226, 0, 0.891) for H=0.5.

For the flat runout section, I'm sizing a box from x=0 to 0.6 at the ramp's base height, centered appropriately with a thin half-thickness, checking that it meshes correctly with the incline's lower edge. I decide no side rails are needed since the ball's motion stays symmetric in x with no lateral drift, and rails would just add unwanted friction. I'm now sketching a supporting pedestal box beneath the ramp spanning from the floor up to just under the ramp surface.

I check that the pedestal top just touches the flat box bottom without any collision issues since static geoms don't interact, then adjust the pedestal's x-range and height to center it properly under the setup, noting the incline's higher portion will float above it harmlessly. I estimate the ball's velocity at the bottom of the ramp after the kink, around 2 m/s, and confirm it should roll smoothly across the flat section to reach the paddle at x=0.4. Then I start placing the paddle, setting its pivot point above the flat surface and defining the hanging paddle geometry.

For the paddle dimensions and mass, I work out the volume and default density to get its mass around 1 kg, then compare that to the ball's mass using default density, realizing the ball comes out lighter — which seems off for the physics I want, so I consider bumping the ball's density up to something steel-like and reducing the paddle's density to rebalance things, possibly just setting masses directly instead of relying on density calculations.

Checking the dynamics: with the paddle's moment of inertia and the ball striking at radius 0.3, the effective mass at that point is much smaller than the ball's mass, meaning a 2 m/s ball will knock the paddle hard, spinning it fast while the ball keeps moving forward and likely strikes the paddle again before reaching the end of the runout and potentially falling off the edge.

I'm weighing options for stopping the ball after it hits the paddle — maybe it bounces back and settles after a few hits, which should be fine since the key requirement is just that the block ends at rest in the box, not the ball. I need to figure out whether a stop wall at the end of the runout would interfere with the paddle's swing path, since the paddle hangs at x=0.4 and sweeps forward as it rotates.

I'm working through the geometry: checking if a wall placed around x=0.6 would catch the ball but also clip the swinging paddle tip, so I'm adjusting the wall height down toward 0.57 to clear the paddle's arc while still blocking the ball.

Now I'm reconsidering the slider's placement, moving it past the paddle to sit higher up and recalculating where the paddle face would first make contact as it swings — coming out to roughly a 7° angle before collision.

The idea is a chain reaction: ball strikes paddle, paddle swings into the slider, and the slider (constrained to move along x) gets pushed outward where it can eventually strike a block or ledge structure sized with a small cube half-width.

I'm working out the geometry so the slider's resting position clears the ledge with a slight gap, then pushes the block past the ledge's edge once it travels far enough in x — checking that block and ledge dimensions actually line up so the block can be knocked off.

I need to reconcile the ball-stop wall position with the ledge's start and thickness, then figure out whether the paddle's swing radius lets it physically strike the slider without interference, tracing the block's fall as a parabola to place the landing target correctly.

Still too close to the ledge corner even accounting for the collision point. I should either limit the hinge to a fixed swing angle, shorten the paddle, or move the ledge further out to x=0.70 to avoid overlap.

Actually maybe a simpler design: make the slider a long box sliding along x, keeping a small clearance above the ledge top so it never touches it, and position the target block centered further out with enough margin to avoid contact.

Thinking about the physics of pushing the block, I realize the push height matters: if I strike too high above the block's center of mass, friction could cause it to tip forward instead of sliding cleanly off the ledge. I should lower friction on the ledge or adjust push height so the block slides rather than topples.

Rather than overcomplicate with geometry, using a lower friction coefficient (like 0.3 for both block and ledge) seems like the cleanest fix, since MuJoCo takes the max of contacting geoms' friction values. I'll estimate exit velocities with deceleration from friction once I account for the masses involved.

That gives slider speed around 0.6 v_ball, so roughly 1.2 m/s once the paddle moves with the ball. The block then gets struck at that speed and, after friction over its short slide to the edge, leaves around 1.1-1.2 m/s — but I need to account for the paddle hitting its range limit, which would abruptly stop the ball's push and possibly cause it to rebound instead of continuing smoothly.

Computing numbers: stroke 0.08 gives φ≈34°, placing the paddle bottom at roughly x=0.58, z=0.586. Checking where the ball contacts the plate, I notice the required plate length at that angle exceeds the actual 0.32 paddle length, so the ball might slip past the bottom edge rather than staying in contact — I need to check whether the ball rides along the plate or falls under it.

Even if it slips under, the wall at x=0.6 should stop it eventually, though a heavy ball wedging against a slider at its limit could create unstable contact forces, which MuJoCo should still handle. To avoid relying on that edge case, I'm considering lightening the ball relative to the paddle, lengthening the paddle plate so contact is maintained, and adjusting the hinge/slider limits so the geometry stays well-behaved.

Now I'm working through the real constraint: the block's exit speed off the ledge and whether it lands through the hoop into the box. Computing fall times and horizontal travel for speeds between 0.5 and 2 m/s, I get a landing range of roughly 0.17 to 0.67 m, which is quite wide, so I need the hoop and box sized generously to tolerate that variability — checking the hoop's mid-height drop gives a narrower travel estimate around 0.3 m.

To tighten this up, I'm considering adding a vertical backboard as part of the ledge body, positioned just past the edge, so the block hits it shortly after launch and then falls more predictably straight down through the hoop and into the box below, reducing the uncertainty from the speed range.

I'm fairly confident MuJoCo skips collision checks between two static geoms since neither can move, so even if the hoop and board overlap it shouldn't matter for simulation.

Now I'm designing the hoop geometry so the backboard only extends down to just above the rim, with the inner hoop opening positioned slightly beyond the board face so the block can fall cleanly through. I'm thinking the checker likely verifies the block's trajectory passes within the hoop's xy bounds at the hoop's height, so a simple square ring made of four box bars should work fine as the "hoop" shape, rather than needing a circular ring of capsules.

Below the hoop I'm placing a catching box on the floor with open top and walls, sized around 0.24 x 0.24 inside with 0.12 wall height, so the block lands and rests inside it.

Now I'm working out the ramp geometry precisely with H=0.5: an inclined section at 20 degrees, a flat runout section, and a stop wall at the end to catch the ball, placing each piece with specific box sizes and positions along the slope.

Checking the incline's upper end geometry confirms it clears fine. Now I'm working out mass values — reconsidering the ball's density so it doesn't overpower the mechanism, settling on something lighter like 1kg, with paddle and slider masses scaled proportionally.

Tracing through the momentum chain: the ball strikes the paddle, transfers energy accounting for the paddle's moment of inertia, then the paddle's swing drives the slider via lever ratio, and finally the slider should impact the block — I'm working through the effective masses at each contact point to estimate resulting velocities.

I also need to account for the ball's rolling spin, which lets it keep pushing the paddle forward after contact, and consider what happens once the slider reaches its range limit and locks with the paddle, leaving the ball pressed against a now-supported paddle with friction trying to make it climb.

After the slider stops, the block continues at roughly 1 m/s and decelerates under friction (μ=0.3, decel ~2.94), traveling about 0.17 m before stopping, so it needs to start within ~0.1 m of the edge to fly off at ~0.9 m/s with the backboard in place. Now I'm working out the geometry of the slider-paddle contact point at a 0.06 stroke, tracking how the plate's position and angle relate to the slider's edge coordinates.

Solving for φ gives roughly 25°, placing the paddle's bottom edge at about (0.535, 0.56), just 1 cm above the ball's center at 0.55. Since the paddle can't translate, the ball contacts the bottom corner slightly above center, so the contact normal points nearly horizontal with a slight downward component—pushing the ball down and stopping it, though it's a marginal margin, so I'm considering lengthening the paddle to give more clearance.

Checking the geometry further, the ball never ends up under the slider unless the paddle swings into that zone, so that's fine. Trying slider bottom at 0.61 with a 0.06 total stroke gives φ≈19.5°, which puts the paddle bottom at z=0.534, x=0.512 — close enough that the ball (center at 0.55) should still make contact.

Now I need to check whether the swinging paddle might collide with the ledge. If I place the ledge top at z=0.60 (just below the slider's 0.61 bottom for clearance) spanning x=0.60 to 0.92, the paddle sweep at angles up to ~20-25° reaches x~0.51-0.54, z~0.53-0.55, which stays below and to the left of the ledge — so no collision at this stroke, though I should double check slightly higher angles.

I'm also setting the hinge axis direction so a positive rotation swings the paddle bottom toward +x, matching the ball's push direction, and I'm leaning toward a limited hinge range like "-10 30" degrees to keep the swing physically reasonable.

Now I'm checking the block's contact point on the slider: with the block centered at z=0.63 and the slider face spanning 0.61-0.66, the impact centroid sits about 5mm above the block's center. That means the push height above the bottom edge is roughly 0.035, so tipping only occurs if friction exceeds about 0.86 — with μ=0.3 the block will just slide rather than tip.

Working through the slider-to-ledge geometry: the slider needs about 0.06 m of travel to push the block's center to the ledge edge, with a small 0.01 m gap between slider and block. By the time the block reaches the edge it's moving at roughly 1 m/s, enough to carry it off and into the backboard rather than just toppling in place. I'll set the slider's right face position at x_R = 0.78.

I'm now checking that the slider doesn't accidentally contact the ledge as it slides — the slider's bottom sits at 0.61 while the ledge top is at 0.60, so there's no interference there, but I need to double check the slider's left portion against the paddle's resting position around x≤0.41.

For the paddle itself, I'm sizing the body so it pivots at pos "0.4 0 0.85" with a hinge on the y-axis, and the box geometry gives a bottom at z=0.515, which leaves a 1.5 cm clearance above the flat top at 0.5 — good, no unwanted overlap at rest.

Checking y-width compatibility, the paddle's half-width of 0.08 is wider than the slider's 0.04, so contact stays fine there. I'll leave hinge damping minimal, maybe 0.01, to avoid oscillation without overcomplicating it. Then I'm thinking through the ball's post-contact behavior: after the paddle locks against the slider, the ball presses against the paddle, and gravity torque on the paddle will likely push the ball back, causing it to roll up the ramp a bit before settling into equilibrium.

Since rolling friction defaults to zero, the ball could bounce between the ramp and paddle indefinitely, which isn't necessarily a problem since resting isn't required. I'm also verifying the slider won't drift once it hits its travel limit — it has no restoring force, so it stays put unless pushed, and the paddle can't pull it back, so that's fine, no damping needed there. Double-checking the slider's math: with 0.07 travel and a 0.01 gap, it pushes the block 0.06 units forward, placing its center at 0.88 right at the edge, which checks out, though if the slider decelerates mid-motion the block could separate earlier with some residual velocity.

I'm calculating the minimum separation speed needed — around 0.54 m/s given the 0.05 remaining distance and 2.94 deceleration, and since expected speeds are closer to 1 m/s, this should be safe. I'm also considering lowering block friction to 0.2 for extra margin, and confirming that the box's default friction of 1 dominates in contact-friction calculations since MuJoCo takes the max of the two surfaces. Now I'm reconsidering the ramp's friction coefficient to figure out whether the ball rolls without slipping, which affects its exit velocity.

Working through the energy conversion from the ball's height drop (about 0.339m) gives a rolling speed around 2.19 m/s, dropping to roughly 2.0 m/s after the kink, which should be enough to push the slider to around 1.2 m/s with added help from the ball's spin. I'm also checking the geometry at the kink where the incline meets the flat box edge at x=0, making sure the transition in ball motion there is physically consistent.

Now I'm tracking the block as it leaves the edge at x=0.88 with roughly 1 m/s, estimating it travels about 0.09m before hitting the backboard at x=1.0, dropping about 4cm in the process and striking around z≈0.59, which falls within the backboard's span of 0.35 to 0.80. I'm considering how the outcome changes depending on exit speed -- at 2 m/s it clearly hits the board, but at a much slower speed like 0.3 m/s the block might instead tip off the edge rather than strike the board directly.

Next I need to work out the hoop geometry itself: the opening needs to span roughly x=0.88 to 1.0 to catch a block sliding down the board, so I'm placing the hoop center around (0.94, 0, 0.30) with an inner half-size of about 0.10, giving inner bounds of x 0.84–1.04 and y −0.10 to 0.10, with ring bars about 0.02 thick positioned along y at x≈0.83/1.05 and along x at y≈±0.11. I'm checking that this lines up with the board's bottom edge at z=0.35 so a block sliding down the face would fall right into the hoop opening.

I'm also designing a basket/box structure near (0.94, 0, 0) on the floor to catch the block after it passes through the hoop — a thin base plate plus four walls forming a container roughly 0.26 wide and about 0.12 tall, with wall thickness around 0.01.

I'm checking the vertical layout: the box top sits around z=0.14, well below the hoop bottom at z=0.29, so the block has clear room to fall from the hoop into the box without hitting the ledge or pedestal structures nearby. I also confirm the backboard sits a few centimeters above the hoop so the block can slide past it before free-falling into the box, and that the roughly 0.6 m drop and resulting speed shouldn't cause it to bounce out given MuJoCo's typically soft, inelastic contacts and the 0.12 m wall height.

I decide to skip adding a connector beam since it risks intersecting the flying block, and reconsider whether the ball could slip past the paddle near the ramp wall — checking the geometry confirms the wall at x 0.58-0.60 clears the paddle's lowest swing position even at max angle, so no collision risk there.

Working through the hinge limits, I find the paddle bottom only reaches ~0.56 at 30° (versus the 0.896 cosine threshold for φ<26.4°), meaning the ball's radius keeps it contacting the paddle's corner rather than slipping underneath — so the paddle locked at its limit should reliably block the ball. I'm considering tightening the hinge range to 25° as a safety margin, noting the slider stroke only drives it to about 19.5° anyway.

I'm checking whether this margin interferes with the slider: solving for the paddle angle needed for its face to reach the slider's contact point at x=0.50 gives φ≈22°, safely under the 25° cap. Even if the hinge stops the paddle there, the slider can continue under its own momentum to its full range, so the mechanism still works as intended.

I'm now working out the paddle-slider initial contact angle (~4.8°), then computing the block's mass from its dimensions and density (about 0.108 kg, rounding to 0.1), and considering whether to include a starting keyframe or just let gravity settle things naturally.

Deciding to skip the keyframe since the ball and block are already resting at correct contact positions and gravity will handle motion. I'm also checking all the various gaps and contacts—paddle to ramp, slider to ledge, block to ledge—confirming they're set up correctly, and settling on default Euler integrator since nothing requires anything more precise.

Working out the ball's timing down the slope: using the rolling acceleration formula, it reaches the flat section around 0.91s, covers the remaining distance in another 0.17s, hits near 1.1s, with the block settling by roughly 6s total. I'm also double-checking whether the falling block might clip the hoop bars given their x-positions, since that's a potential collision issue worth verifying.

I'm making sure every body and geom gets a name, including the floor and light, and setting friction values for the ledge and block so the box default caps things appropriately. I'm also assigning masses to the ball, paddle, and slider, and defining the paddle's hinge joint with its axis, range, and damping.

Now I'm defining the slider's slide joint and verifying the incline geom's position and rotation — checking that the euler rotation about y by 20° correctly tilts the ramp so it rises toward -x and descends toward +x, matching the intended geometry.

With that confirmed, I'm computing the ball's starting position on the slope surface, offsetting by the normal vector and verifying it falls within the box's bounds along the slope. I'm also noting the visual rgba colors and deciding to skip adding an unnecessary post structure to avoid collision issues, then moving on to check the slider's positioning.

Tracing through the geometry, I verify the slider's horizontal range stays clear of the ledge and backboard, the ledge support post sits outside the paddle and ball's reachable area, and the backboard itself spans the correct height range without conflicting with other elements.

Now I need to work out support posts for the backboard that avoid colliding with the box walls — offsetting them in y to sit outside the box's footprint while still connecting to a widened backboard, then positioning the hoop bars symmetrically along x at the appropriate y-offset.

I decide floating the hoop without a stem is acceptable to avoid collision issues, and confirm the ledge body structure satisfies the single-body geom requirement. Now I'm writing the XML.

