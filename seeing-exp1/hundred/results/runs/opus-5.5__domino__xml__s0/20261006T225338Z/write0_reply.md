The ramp rolls ball1 onto a raised platform where the three dominoes stand. d3 then shoves ball2 off the platform edge into a walled cup on the floor. I worked this out by hand and have not run it, so the timing and landing spot are estimates.

- **Ramp:** 8° incline. ball1 starts 1 m along it, so it rolls about 1.4 m/s by the bottom.
- **Dominoes:** 0.12 m tall and spaced 0.07 m apart. ball1 (r = 0.07) strikes d1 just above its centre of mass, so d1 should tip forward rather than slide.
- **ball2:** sits 7 cm in front of d3's front face. At the predicted speeds it should land well inside the 0.4 m-long cup. The platform's side wall closes the cup's near end.
- **Rolling friction (`condim="6"`) on ball2:** the cup walls absorb most of its bounce energy. Rolling friction then brings it to rest within the 6 s.

```xml
<mujoco model="ramp_domino_cup">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="ramp" pos="0 0 0">
      <geom name="ramp_incline" type="box" size="0.65 0.15 0.02" pos="-0.646457 0 0.220657" euler="0 8 0" rgba="0.6 0.4 0.2 1"/>
      <geom name="ramp_platform" type="box" size="0.285 0.15 0.075" pos="0.265 0 0.075" rgba="0.6 0.4 0.2 1"/>
    </body>

    <body name="ball1" pos="-0.980526 0 0.358492">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.07" mass="0.15" condim="6" friction="1 0.005 0.0005" rgba="0.9 0.1 0.1 1"/>
    </body>

    <body name="d1" pos="0.30 0 0.21">
      <freejoint name="d1_free"/>
      <geom name="d1_geom" type="box" size="0.01 0.04 0.06" rgba="0.1 0.3 0.9 1"/>
    </body>

    <body name="d2" pos="0.37 0 0.21">
      <freejoint name="d2_free"/>
      <geom name="d2_geom" type="box" size="0.01 0.04 0.06" rgba="0.1 0.5 0.9 1"/>
    </body>

    <body name="d3" pos="0.44 0 0.21">
      <freejoint name="d3_free"/>
      <geom name="d3_geom" type="box" size="0.01 0.04 0.06" rgba="0.1 0.7 0.9 1"/>
    </body>

    <body name="ball2" pos="0.52 0 0.175">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.025" condim="6" friction="1 0.005 0.002" rgba="0.1 0.8 0.2 1"/>
    </body>

    <body name="cup" pos="0 0 0">
      <geom name="cup_base" type="box" size="0.2 0.13 0.005" pos="0.75 0 0.005" rgba="0.9 0.8 0.1 1"/>
      <geom name="cup_far_wall" type="box" size="0.01 0.15 0.08" pos="0.96 0 0.08" rgba="0.9 0.8 0.1 1"/>
      <geom name="cup_side_left" type="box" size="0.21 0.01 0.08" pos="0.76 0.14 0.08" rgba="0.9 0.8 0.1 1"/>
      <geom name="cup_side_right" type="box" size="0.21 0.01 0.08" pos="0.76 -0.14 0.08" rgba="0.9 0.8 0.1 1"/>
    </body>
  </worldbody>
</mujoco>
```

---
thinking (summarized):

I'm working through the physics setup for the scene, figuring out how to position the ball on the ramp—deciding whether "1 m up the ramp" means a distance along the incline or a height, and leaning toward interpreting it as distance along the ramp surface.

I'm picking a 15-degree incline for a gentler, more reasonable drop height and exit speed, then working out the ramp's geometry as a tilted box ending at floor level, considering how a static ramp body interacts with the floor plane in MuJoCo.

Now I'm computing the ball's starting position one meter up the ramp, placing its center offset from the contact point by the radius along the normal, giving a contact height of about 0.259m. I'm also checking how the ramp's top edge aligns with the floor at the bottom corner.

After the ramp-to-floor kink, the ball's horizontal speed should be roughly 1.9 m/s times cos(15°), and since there's no rolling friction defined, it keeps rolling without decay. The concern now is domino geometry: if the ball's radius of 0.03 means it strikes near the base of a 0.4m-tall domino, the impact point is too low and might just slide the domino rather than topple it, so I need to reconsider the collision height.

I'm rescaling things so the ball strikes higher relative to domino height—making the ball radius 0.05 and shrinking the dominoes to 0.2m tall (half-height 0.1), 0.02m thick, 0.1m wide, so the impact lands at a quarter of the domino's height instead of near the base. Working out masses: the ball at that radius comes to about 0.52 kg with default density, versus roughly 0.4 kg for each domino, so the heavier, fast-moving ball should topple them more reliably at this impact point.

I'm trying small domino dimensions so the ball's contact point lands just above center, and considering whether tiny dominoes against a heavy fast ball would topple cleanly or just scatter chaotically. I keep adjusting ball radius and domino height to get the contact height slightly above center of mass for a clean forward tip.

I should dial down the ball's mass to around 0.05 kg so it's comparable to the dominoes rather than overpowering them, and check the resulting speed off a 10° ramp — roughly 1.56 m/s, which is still enough to topple the dominoes without sending them flying. I'm leaning toward keeping the setup simple rather than overengineering with raised platforms, settling on a 10° ramp angle for the ball.

I'm working out domino dimensions now — settling on a height of 0.08m, thickness 0.016m, width 0.06m, giving a mass around 0.077kg, with the ball set to 0.08kg mass to keep momentum transfer balanced. I'm also calculating spacing so each falling domino's arc reaches the next one at the right height to keep the chain reaction going.

Now I'm laying out the actual positions: ramp at x=0, dominoes d1-d3 spaced around 0.05m apart starting at x=0.3, then placing a second ball just ahead of d3 so its falling arc strikes the ball near the end of its swing.

The bigger problem I'm realizing is the cup: a cup resting flat on the floor with upright walls can't actually catch a ball rolling along the same floor, since the ball would just hit the outer wall rather than enter. I need to rethink the catching mechanism, maybe using a recessed opening instead.

I could add rolling friction to the ball so it decelerates naturally via torsional contact properties, estimating deceleration from the rolling friction coefficient — at a small μr the ball would stop within roughly a meter, so the cup needs to be positioned close enough to catch it before it loses momentum. Now I'm thinking through how to actually construct the cup itself, perhaps as a ring of walls on the floor with a ramp entry.

Actually a cleaner setup might be an elevated table where ball2 sits, with the cup positioned on the floor below its edge -- domino d3 knocks the ball off the table so it falls down into the cup, which is just an open-top box with walls.

Working out the fall physics: with edge height around 0.15m, the ball lands roughly 0.05-0.26m out depending on speed, so I'm sizing the cup generously with a 0.3m inner length right at the platform edge and tall walls to catch it. I'll give ball2 extra rolling friction via its contact properties so it settles inside rather than bouncing back and forth indefinitely.

I'm working out the geometry of d3 toppling toward ball2 near the edge, calculating where the domino's face would intersect the ball's radius as it pivots forward, using the angle of fall to find the contact distance from the ball's center.

Using energy from the fall plus the initial push gives ω around 8 rad/s, so roughly 0.3-0.4 m/s if ball2 is light (~0.01 kg). That lands it about 0.07 m beyond the edge, within the cup's 0.25 m length. Let me try repositioning ball2 farther out so the domino's top edge strikes it, solving for the tip angle again with the new distance.

At 58° the contact point sits near the domino's top (0.07 of its 0.08 height), giving a faster strike speed, so I'll settle on that angle with ball2's center 0.03 m from the platform edge. Now I need to figure out the ramp geometry so ball1 rolls down into the platform correctly, accounting for the incline's height and angle feeding into the platform's starting height.

Computing incline box position...

The lower corner of the incline sits just slightly under the platform, but since they're the same body with no collision between them, that's fine — the transition at x=0 is coplanar, so the ball will roll smoothly from incline to platform. Now I'm working out the starting position for the first ball, placing it 1 meter along the incline from the platform edge.

Computing the ball's center position along the ramp, I check that it stays well within the incline's bounds. The incline box floats without support, but since it's static that's not an issue.

I calculate the ball's speed when it reaches the platform using energy conservation with rolling resistance, getting roughly 1.56 m/s along the ramp, which translates to about 1.54 m/s horizontally after the small bend at the kink, accounting for it starting from rest and rolling under friction.

Now I'm placing three dominoes on the platform and checking contact geometry—the ball strikes the first domino slightly above its center, so I'm working through whether this off-center impulse plus friction at the domino's base will cause it to tip forward given the ball's mass, speed, and the domino's rotational inertia.

I'm leaning toward taller, heavier dominoes (0.12m height, ~0.192 kg) for more stable toppling, with a larger ball (r=0.07) hitting above center at an 8° ramp angle, spacing them so the gap stays under the domino height. Since I can't actually simulate this, I'll just commit to this reasonable configuration and move forward.

Chain continues through d2 to d3, which needs to tip and strike ball2 positioned near its top for proper contact. Checking the geometry, with ball2 placed 0.09 along the pivot direction, the domino rotates to about 65° before contact occurs at roughly 0.09 up the face—comfortably under the 0.12 height, so the strike lands correctly rather than slipping off the top.

Calculating the angular speed from energy conservation: the center of mass drops about 0.035 m as the domino falls from vertical to 65°, giving an angular velocity near 11.8 rad/s and a point speed at the contact location of roughly 1.06 m/s. Since ball2 is light, it picks up somewhere between 1-2 m/s and gets launched off the edge at an angle, landing around 0.26 m away.

I'm now reconsidering the setup since the cup needs to cover a range from 0 to 0.35 m, which feels risky with these numbers. Making ball2 heavier (around 0.065 kg with radius 0.025 at default density) and working out the effective domino mass at the contact point (~0.117 kg), I estimate the collision gives ball2 a velocity somewhere between 0.7-1.2 m/s, though the domino continuing to push afterward complicates the exact value.

I'm recalculating the contact angle with the new ball radius, finding it lands near 59 degrees, and verifying the geometry checks out along the domino face. Now I'm thinking about whether lowering the platform height would reduce the horizontal travel needed, and considering that the cup's near wall could just be the platform edge itself rather than a separate wall, which affects how I lay out the cup's base and side walls.

I'm sizing the cup's inner span from the platform edge, working out the far wall height and side wall width so the ball bounces and settles with rolling friction, and double-checking ball2's resting position relative to the platform top. I'm also tracing through whether ball1, after knocking into domino1, might continue moving and potentially end up inside the cup too.

Now I'm computing the exact ramp geometry: an 8° incline angle gives cosine and sine values I'm using to locate the incline's top center and box center relative to platform height, then placing ball1's contact point based on its radius.

I'm also working out the rolling speed at the bottom of the ramp using energy conservation with solid-sphere rotational inertia, getting about 1.40 m/s, and checking that explicit mass settings give physically consistent inertia. Now I'm considering the kink where the incline meets the flat ground at x=0.

I'm positioning the platform so it overlaps slightly with the incline base, then laying out the three dominoes along the flat section at spaced x-coordinates with varying heights, figuring out ball and domino contact points so each collision triggers correctly down the chain.

Now I'm laying out the cup geometry: a base plate, far wall, and two side walls with specific positions and heights, then working through how the near wall should align with the platform edge without overlapping it, since the platform's y-span is narrower than the cup's inner width.

Actually, static-static collisions likely still get filtered or just don't matter dynamically, so I can simplify by matching platform width to the cup's outer width, letting the platform edge double as the near wall. I'll just confirm the ball's resting position stays within the cup's inner bounds rather than overengineering the wall geometry.

For the bounce physics, I'm estimating the fall time and landing x-position given the ball's initial speed, then checking it lands within cup bounds and computing rolling friction deceleration to see how far it travels before settling against the far wall.

Adding the flat section gets ball1 to about 1.5s, then dominoes toppling sequentially bring ball2 into play around 2.2s, with everything settling by 3.8s — timing seems fine. I need to check friction parameters at the cup base and platform contacts to make sure condim and friction settings carry through properly, and consider whether ball1 retains enough momentum after hitting the first domino to interfere with ball2 or the remaining dominoes later.

The fallen dominoes form a leaning pile that ball1 likely can't climb over, so I'll just accept that it gets stuck there—adding a tiny bit of rolling friction (μr 0.0005) so it settles without materially affecting the ramp dynamics.

Separately, I'm checking whether domino d3 tips off the platform edge near x=0.57—its COM sits around 0.51, still within the platform, so it should rest rather than fall into the cup. For ball2, I'm computing the push direction from the domino face at 59°: the normal points mostly downward-forward (0.515, -0.857), meaning the force drives the ball mainly into the platform with only a modest horizontal push.

Since ball2 sits near the edge at 0.54 with the edge at 0.57, even a small 0.03 nudge forward sends it off, landing somewhere around 0.65-0.7. But I'm now worried the falling domino, once flat, could land directly on top of ball2 before it rolls off, since the domino's flat resting position overlaps ball2's location and height.

Let me reconsider the geometry — maybe placing ball2 closer with a smaller offset gives a more horizontal contact angle but slows the domino's push, so there's a tradeoff to balance. Testing a=0.07 gives a contact angle around 50-51 degrees, which seems like a reasonable compromise, so I'll go with that placement for ball2's center.

Now I'm working out the cup and platform dimensions — setting the edge position, platform half-widths, and the cup's base and wall geometry coordinates.

I'm also checking whether a near wall near x 0.55-0.565 could interfere with the ball's trajectory as it rolls off the platform edge, since its falling path might graze the wall's top height.

Deciding to skip the near wall since the platform face itself can act as that boundary. I'm setting the cup and ramp bodies at the origin with absolute geom positions, giving the floor a 3x3 plane, and skipping a keyframe entirely since gravity will set ball1 in motion from its initial resting placement touching the ramp. Now I'm positioning the dominoes.

Ball1 hits d1 slightly above center, which looks fine, and the small ramp kink at x=0 shouldn't cause issues given the ball radius. Timing checks out roughly for the ball reaching the dominoes, so I'll finalize the XML with a 0.002 timestep and solver defaults, while noting the setup hasn't been numerically verified.

