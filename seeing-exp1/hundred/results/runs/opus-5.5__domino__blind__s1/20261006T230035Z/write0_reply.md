The ball starts 1 m along a gentle 5° ramp and reaches about 1.1 m/s at the bottom. It is 0.1 m in radius, so it strikes the 0.15 m-tall d1 at 2/3 of its height. At that height the impact turns d1 about its base rather than sliding it. Each falling domino hits the next one high up. d3's top knocks ball2 off a low fixed shelf, and ball2 drops into the cup. The cup floor has rolling friction so the ball settles. I worked this out by hand and have not run the simulation, so the timing and the final resting speed are unconfirmed. I read "1 m up ramp" as 1 m along the slope; the start height is only about 0.09 m.

```xml
<mujoco model="ramp_domino_cup">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" pos="0 0 0" size="3 3 0.1" rgba="0.8 0.8 0.8 1" friction="1 0.005 0.0001"/>

    <body name="ramp" pos="0 0 0">
      <geom name="ramp_deck" type="box" pos="-0.5995 0 0.0324" size="0.65 0.15 0.02" euler="0 5 0" rgba="0.6 0.4 0.2 1" friction="1 0.005 0.0001"/>
    </body>

    <body name="ball1" pos="-0.9875 0 0.1868">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.1" mass="0.1" rgba="0.9 0.1 0.1 1" friction="1 0.005 0.0001"/>
    </body>

    <body name="d1" pos="0.30 0 0.075">
      <freejoint name="d1_free"/>
      <geom name="d1_geom" type="box" size="0.01 0.05 0.075" mass="0.2" rgba="0.1 0.3 0.9 1" friction="1 0.005 0.0001"/>
    </body>

    <body name="d2" pos="0.39 0 0.075">
      <freejoint name="d2_free"/>
      <geom name="d2_geom" type="box" size="0.01 0.05 0.075" mass="0.2" rgba="0.1 0.5 0.9 1" friction="1 0.005 0.0001"/>
    </body>

    <body name="d3" pos="0.48 0 0.075">
      <freejoint name="d3_free"/>
      <geom name="d3_geom" type="box" size="0.01 0.05 0.075" mass="0.2" rgba="0.1 0.7 0.9 1" friction="1 0.005 0.0001"/>
    </body>

    <body name="shelf" pos="0 0 0">
      <geom name="shelf_block" type="box" pos="0.625 0 0.04" size="0.055 0.06 0.04" rgba="0.5 0.5 0.5 1" friction="1 0.005 0.0001"/>
    </body>

    <body name="ball2" pos="0.61 0 0.11">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.03" mass="0.05" rgba="0.95 0.8 0.1 1" friction="1 0.005 0.0001"/>
    </body>

    <body name="cup" pos="0 0 0">
      <geom name="cup_floor" type="box" pos="0.79 0 0.005" size="0.12 0.09 0.005" condim="6" friction="1 0.005 0.005" rgba="0.2 0.7 0.2 1"/>
      <geom name="cup_back" type="box" pos="0.675 0 0.035" size="0.005 0.09 0.025" rgba="0.2 0.7 0.2 1"/>
      <geom name="cup_front" type="box" pos="0.905 0 0.035" size="0.005 0.09 0.025" rgba="0.2 0.7 0.2 1"/>
      <geom name="cup_left" type="box" pos="0.79 0.085 0.035" size="0.12 0.005 0.025" rgba="0.2 0.7 0.2 1"/>
      <geom name="cup_right" type="box" pos="0.79 -0.085 0.035" size="0.12 0.005 0.025" rgba="0.2 0.7 0.2 1"/>
    </body>
  </worldbody>
</mujoco>
```

---
thinking (summarized):

I need to lay out the scene along the x-axis and figure out what "1 m up ramp" means for the ball's starting position — whether that's distance along the ramp's slope or vertical height above the floor. I'll treat it as height above the floor for now to keep the physics reasoning tractable.

Working out the ramp geometry with a rotated box, figuring the rotation angle and box placement so the tilted top surface meets the floor smoothly at the bottom edge where the ball transitions from ramp to ground.

Computing contact point and ball center position along the slope, offsetting by radius along the normal. Since both the ramp and floor are static bodies, they won't collide with each other even though the ramp geometry slightly overlaps the floor near its edge, so that's not an issue. The ball should slide straight down with no side forces, reaching the bottom of the slope at roughly 2.6 m/s.

After the kink transition, the ball loses most of its vertical velocity and keeps about 2.29 m/s horizontal — that's fast enough it might send a domino flying rather than toppling it cleanly. I need to think about ball mass and domino dimensions; if the ball strikes too low near the domino's base, it may just slide it rather than tip it over. I'll increase the ball radius to 0.1 so it strikes higher up the domino.

For a rod-like domino struck below its center of percussion, the physics of impulsive collision matters: if the impact height is less than half the domino's height, the bottom tends to rotate backward relative to the top, affecting whether it topples forward or just slides against floor friction.

Given this complexity, it seems safer to arrange for the ball to strike above the domino's center of mass to ensure reliable forward toppling.

Actually, simpler approach: keep dominoes on the floor but size the ball so it strikes near the top third of the domino, at the rod's center of percussion where the base has zero instantaneous velocity, producing pure rotation. With a domino height of 0.15 and ball radius 0.1, the hit lands right at that 2/3-height sweet spot, so I can set domino half-sizes and spacing accordingly for clean toppling.

For masses, I'd give the wooden domino around 0.18 kg (density ~600, small volume) and the ball something light like 0.3 kg, with speed around 2–2.3 m/s so it's a solid but not excessive hit. The concern is that after striking domino 1, the ball keeps moving forward and might slam into domino 2 directly or push through the line, so I need to make sure domino 1 absorbs or redirects enough energy that the chain reaction happens as intended rather than the ball interfering.

I'm checking whether the ball's momentum is enough to topple the domino — the energy needed to tip it over the pivot point is tiny compared to the ball's kinetic energy, so the collision should easily work even though the masses are similar and the ball will slow down after impact.

Let me try a gentler ramp angle to keep ball speed manageable—at 5° the height is about 0.087m with acceleration around 0.611 m/s², giving roughly 1.8s travel time and a final velocity near 1.1 m/s, which should still leave enough time for the domino chain and ball2's journey into the cup within the 6-second window.

That gives roughly 0.2 m/s continuing, so the ball likely rolls up onto the fallen domino or rebounds slightly — either outcome seems acceptable for the setup. Checking whether d1 actually topples, I estimate domino tip rotational speed around 2 rad/s and compare the resulting rotational energy against what's needed to tip it over.

Redoing the numbers with a heavier 0.1 kg ball and lighter domino gives a much larger energy margin — roughly ten times the toppling threshold — so this configuration reliably knocks the domino over.

But then I check whether the ball itself rolls far enough afterward to catch up to the fallen domino and climb over its 0.02 m edge, and the energy needed to pivot over that step exceeds the ball's post-collision speed. So the ball likely just stops against the fallen domino rather than rolling past it.

Then I'm tracing the chain further: d2 topples d3, and d3's top edge needs to strike ball2 to launch it toward the cup, but getting ball2 to actually settle inside a cup with raised walls means it needs enough speed to clear the rim and then lose momentum inside.

A digging-in cup won't work since the floor plane fights anything placed below z=0, so I'm considering elevating the dominoes on a small table so ball2 falls off the edge into a floor-level cup, or designing the cup as a shallow tray with a sloped front lip that lets the ball roll in without needing to clear a wall.

Actually a cleaner approach: give ball2 a raised shelf as a separate fixed body, so domino d3 knocks it off the shelf's edge and it drops into the cup below.

So the ball gets pushed off the shelf edge by d3's impact, rolling a short distance before falling into the cup below, with the fall height and velocity determining a modest horizontal travel—maybe 6cm—landing it just inside the cup's near wall.

Once inside, since MuJoCo's default contact model is fairly inelastic (low restitution), the ball should bounce between the cup walls a few times and lose energy quickly, settling near the bottom. I'm considering adding rolling friction to ball2's contact properties (condim 6 with small rolling/torsional friction coefficients) along with a high-friction cup floor to help it come to rest rather than oscillating indefinitely.

Working through the physics, though, 0.01 rolling friction coefficient would create way too much deceleration for a ball rolling on the shelf -- it'd stop almost instantly, which isn't realistic there. Since contacts combine via the max of the two geoms' friction values, I can't easily give the shelf lower rolling resistance while the ball has high values; I need to think about whether to isolate strong rolling friction just to the cup floor geom instead.

I'll keep the shelf as a separate body rather than part of the cup itself, since merging them could confuse bounds-checking for whether ball2 ends up inside the cup. Now moving to the domino geometry: half sizes around (0.01, 0.05, 0.075), height 0.15, and center-to-center spacing of 0.09, with each domino falling forward pivoting about its front edge.

Working through the angles, d2 topples into d3 when the top front corner sweeps 0.07 horizontally, giving θ≈27.8° and a contact height around 0.133 — high enough on d3 to topple it cleanly. Now I need to position the shelf in front of d3, aligned with its front face.

I'm then solving for where ball2 sits on the shelf: setting shelf height 0.08 so the ball's center sits at z=0.11, I find d3's falling top corner reaches that height at θ≈42.8°, giving a horizontal travel of 0.102 — which tells me to place the ball's back edge at roughly x3+0.142 so d3 strikes it squarely.

Now I'm refining that placement by checking corner-to-sphere contact more precisely, trying xb=x3+0.13 and testing distances at θ=35° and 37° to confirm the corner actually grazes the ball's surface (radius 0.03) at a reasonable angle, which lands around 0.031-0.036 — close enough to call it a hit.

I also need to verify the domino's front face doesn't clip the shelf's near edge before reaching the ball: at θ≈37.5°, the face crosses the shelf's top height (0.08) at roughly x3+0.071, so the shelf edge needs to sit past that point to avoid premature contact.

Setting the shelf near edge at x3+0.08, with the ball resting at x3+0.13 giving a safety margin, and a far edge at x3+0.20 so the ball eventually rolls off — that sizes the shelf as centered at x3+0.14 with half-extents 0.06 x 0.06 x 0.04.

Now I'm checking whether the falling domino actually delivers enough energy to the ball, estimating the angular velocity gain from gravity as it rotates to 37° plus whatever momentum carries over from the earlier chain reaction.

Working through the corner speed of about 1 m/s, I estimate the ball could pick up roughly 1-1.5 m/s when struck, then calculating its subsequent fall off the shelf edge and how far it travels before landing, to make sure the cup below is positioned and sized correctly to catch it.

Meanwhile domino 3 doesn't fall flat — it ends up leaning against the shelf edge at around 41°, and contact with the ball actually begins earlier near 37.5°, so there's only a few degrees of travel during the actual impact, which affects how much momentum gets transferred.

Moving the shelf edge closer still keeps the ball contact valid, so I'll stop the domino at 45°. For ball2's speed, I'm estimating momentum transfer by giving it more mass (~0.1 kg) so the common velocity comes out around 0.4 m/s, while also accounting for how rolling friction affects the ball's effective translational response to a center-height push.

At roughly 0.3-0.4 m/s, ball2 rolls across the shelf and off the edge, falling into the cup and landing about 0.04-0.05 m beyond the edge. I'm now sketching the cup as its own structure with a back wall right against the shelf, walls about 0.06 m tall, and checking that the ball clears the cup's back wall as it falls from the shelf height.

Actually, maybe simpler: omit the near wall entirely but embed a low wall overlapping the shelf's far face so it's hidden inside the shelf volume, keeping the cup visually closed while the floor still bounds the ball properly.

With the ball dropping only about 0.07m onto the cup floor, it should settle with minimal bounce, and rolling friction with the floor's contact properties should bring it to rest without much drama.

Now checking ball1 on the ramp — with mass 0.1 kg and radius 0.1, friction of 1 should be plenty to prevent slipping on a shallow 5° slope, so I need to verify how the ramp geometry interacts with the domino setup below.

Computing the ramp box geometry and surface normal, then placing the ball's starting contact point along the slope using the center and offset vectors.

I'm second-guessing whether "1 m up the ramp" means distance along the slope or vertical height—a 1 m vertical drop would make the ball too fast, so I'll stick with distance along the ramp's surface.

Working out ball1's exit speed off the ramp using rolling-without-slipping dynamics, then estimating its travel time along the floor to reach the first domino, factoring in contact geometry where the ball's surface meets the domino's back face.

Checking the chain reaction: domino spacing and heights seem consistent for each one to tip the next, since the strike points land above their centers of percussion, meaning the base stays put via friction while the top gets pushed forward.

Now I'm positioning the shelf relative to d3 and the second ball, verifying the geometry so the domino's falling face reaches the shelf edge after the ball makes contact, not before — confirming the angles work out with the ball striking at roughly 37.5° while the domino edge would only reach the shelf corner at 45°.

Then I'm mapping out the cup's interior dimensions — the back wall, floor, front wall, and side walls — so that when the ball rolls off the shelf edge at x=0.68, it drops cleanly onto the cup floor.

Checking whether ball2 might get deflected sideways as it tips off the shelf corner, but the setup is symmetric so it should fall straight. I'm also tracking that domino d1, now leaning against d2 rather than lying flat, keeps its base near x~0.3, so ball1 will strike that same leaning base again as it continues at 0.44 m/s.

Masses: dominoes 0.2 kg, balls 0.1 kg each. Given d3's rotational speed at the corner, ball2 likely ends up with a modest forward velocity around 0.2-0.4 m/s depending on the exact contact speed.

I'm checking the geometry near the shelf edge — d3 rotated to 45° has its corner close enough to the ball that it keeps pushing it forward without over-penetrating, so the ball should roll cleanly off the edge. To make sure the final speed is enough for the cup to catch it, I'll lighten ball2 to 0.05 kg, which should bump its exit speed up to around 0.57 m/s.

I'm also sanity-checking contact softness and sizes — default solref of 0.02 should be fine for these small, lightweight objects, and domino thickness of 0.02 works with the 0.002 timestep. For the keyframe, I'll just define a "start" keyframe at time 0 and let qpos default to the model's initial qpos0 rather than specifying everything explicitly.

I'll also skip adding velocity since nothing needs an initial push, and I'm checking that friction combines properly between the ball, cup floor, and walls using the max-friction rule. Now I'm ready to assemble the actual XML — setting up lighting, the ground plane, default floor friction, and the ramp's tilt angle using euler rotation.

Calculating final positions...

The ball leaves the shelf edge at about 0.4 m/s and lands roughly 0.05 beyond it, which works fine. I also confirm the ramp's top surface extends across s from -0.65 to 0.65, covering ball1's starting position, so that checks out too. Time to write it up.

