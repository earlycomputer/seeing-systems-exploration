A motor-driven ram slides in from behind, shoves the bottom block forward about 7–9 cm, and stops against its joint limit. That pulls the support out from under the upper four blocks, so they tip backward and fall.

The ram only collides with `block1`, through `contype`/`conaffinity`, so the falling blocks pass through it and land on the floor.

I haven't run this in MuJoCo. The timing, distances and outcome below are hand estimates.

- **The wait:** the ram covers 0.51 m before contact, so the stack should stand untouched for roughly 0.4–0.5 s.
- **Why it should tip:** friction from the bottom block drags the base of the upper tower forward. My estimate is about 6 m/s², roughly three times the ~2 m/s² needed to tip it.
- **Why it should end at rest:** after the push, the ram stays pressed against its limit and the blocks settle on the floor.

```xml
<mujoco model="toppling_stack">
  <option timestep="0.002"/>
  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>
  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <light name="fill" pos="-2 -2 2" dir="1 1 -1" diffuse="0.3 0.3 0.3"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.75 1" friction="0.5 0.005 0.0001"/>

    <body name="block1" pos="0 0 0.05">
      <freejoint name="block1_free"/>
      <geom name="block1_geom" type="box" size="0.04 0.04 0.05" density="500" friction="0.6 0.005 0.0001" contype="3" conaffinity="3" rgba="0.85 0.3 0.25 1"/>
    </body>
    <body name="block2" pos="0 0 0.15">
      <freejoint name="block2_free"/>
      <geom name="block2_geom" type="box" size="0.04 0.04 0.05" density="500" friction="0.6 0.005 0.0001" rgba="0.9 0.6 0.2 1"/>
    </body>
    <body name="block3" pos="0 0 0.25">
      <freejoint name="block3_free"/>
      <geom name="block3_geom" type="box" size="0.04 0.04 0.05" density="500" friction="0.6 0.005 0.0001" rgba="0.9 0.85 0.25 1"/>
    </body>
    <body name="block4" pos="0 0 0.35">
      <freejoint name="block4_free"/>
      <geom name="block4_geom" type="box" size="0.04 0.04 0.05" density="500" friction="0.6 0.005 0.0001" rgba="0.3 0.7 0.35 1"/>
    </body>
    <body name="block5" pos="0 0 0.45">
      <freejoint name="block5_free"/>
      <geom name="block5_geom" type="box" size="0.04 0.04 0.05" density="500" friction="0.6 0.005 0.0001" rgba="0.25 0.45 0.85 1"/>
    </body>

    <body name="ram" pos="-0.6 0 0.05">
      <joint name="ram_slide" type="slide" axis="1 0 0" limited="true" range="0 0.58" damping="4"/>
      <geom name="ram_geom" type="box" size="0.05 0.03 0.03" density="2000" friction="0.6 0.005 0.0001" contype="2" conaffinity="2" rgba="0.3 0.3 0.35 1"/>
    </body>
  </worldbody>

  <actuator>
    <position name="ram_motor" joint="ram_slide" kp="1000" ctrllimited="true" ctrlrange="0 1" forcelimited="true" forcerange="-10 10"/>
  </actuator>

  <keyframe>
    <key name="start" qpos="0 0 0.05 1 0 0 0  0 0 0.15 1 0 0 0  0 0 0.25 1 0 0 0  0 0 0.35 1 0 0 0  0 0 0.45 1 0 0 0  0" ctrl="1"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm planning a scene with five stacked cubes, each 0.1m, that remain stable until the bottom block gets pushed and the stack topples. I'm working out the cube positions, centering them at increasing heights, and thinking through how the pusher (maybe a sliding ball or motorized slider) initiates the push.

For reliable toppling rather than the bottom just sliding out Jenga-style, I'm considering making the blocks taller and narrower so the tower is tall and slender, which makes it tip more easily when the base is jolted. A sharp push to the bottom block should accelerate it while the inertia of the blocks above causes the whole structure to tip over.

The tower tips backward toward -x, and if the bottom block slides more than 0.06 m past block2, it falls out entirely either way. I also need the initial stack stable before any push, so I'm reconsidering dimensions—maybe 0.08 x 0.08 x 0.1 blocks with half-sizes 0.04/0.04/0.05 for a less extreme slenderness. Now I'm setting up the pusher body with a sliding joint along x and a box geom to drive the impact.

For the impact itself, I'm considering a rolling ball instead: it starts some distance away at a set velocity, strikes the bottom block, and I want to assign both linear and consistent angular velocity so it rolls naturally rather than skids and loses speed before contact.

Using density 500 for blocks gives ~0.32 kg each, while a steel-ish ball at radius 0.05 with density 7800 comes to about 4.1 kg. At 1.5 m/s, that heavy ball would send the much lighter block moving fast on impact—maybe around 1.4 m/s accounting for MuJoCo's somewhat inelastic contacts—which could push the bottom block out from under the tower while friction drags block2 along with it.

The tower's base accelerates horizontally and tips, with the bottom block likely sliding clear of the stack's footprint within a fraction of a second, causing the tower to drop and possibly tilt or topple—though there's a risk it lands standing upright, like the tablecloth trick. Complicating things further, since the ball keeps moving forward at speed, it could end up colliding with block2 right after block1 is displaced, since the tower drops down to floor level and block2's position shifts into the ball's path, triggering even more toppling. I'm now considering whether a gentler push would create a cleaner topple instead of this messier chain of collisions.

The impulsive friction between block1 and block2 is limited and small, but the sustained friction force from block1 sliding under block2 gives the four-block tower an acceleration of about μg ≈ 4.9 m/s², well above the tipping threshold of roughly 1.96 m/s². So the tower tips backward about block2's rear edge, rotating toward the ball's direction as block1 continues sliding forward beneath it.

I'm checking whether this tipping is enough to actually topple the tower over, since it needs to rotate past the critical angle where the center of mass passes beyond the rear edge—roughly atan(0.2) ≈ 11.3° for this geometry—and that depends on how much rotational energy gets imparted versus how quickly block1 decelerates from floor friction while the base keeps getting pushed forward by the ball.

Once d exceeds 0.04, the tower tips backward around block1's rear edge and slides off the back entirely. Given the ball pushes block1 much faster than friction can drag block2 along, block1 outruns block2 quickly, so the tower falls off the back onto the ball itself — a messy, chaotic outcome, but the key result is still that it topples.

A bigger issue is the "at rest" requirement: with no rolling friction in MuJoCo's default contact model, a ball could roll indefinitely and never settle, so I should avoid a free-rolling ball as the pusher. A cleaner approach is a ram body on a slide joint driven by a position actuator, moving to a fixed target via keyframe control so it naturally stops.

I could also consider a pendulum hammer swinging under gravity to strike the blocks, but it risks re-hitting them as it keeps oscillating even with damping, whereas the ram settles cleanly once it reaches its servo target.

Designing the ram: I'm sizing it to touch only block1 and clear the floor and falling blocks, positioned so its geometry spans just the right height range without intersecting anything unintended. Then I'm thinking about which direction to push so the tower topples the way I want — pulling block1 forward should send the tower falling backward.

I'm calculating the push distance for the ram: starting at x=-0.35 with front face at -0.30, contacting block1's rear face, and moving to a target center around x=0.10 so block1 gets shoved forward roughly 0.19m — fully clearing its base position and likely toppling the tower, though I consider whether a smaller shove might produce the toppling more naturally instead of just yanking the block clean out.

As block1 slides forward, block2 lags behind due to inertia, so relative to block1, block2 effectively shifts backward; once block2's center of mass passes block1's trailing edge, the tower should rotate backward about that edge and fall — landing right back on the ram, which by then occupies roughly x=0.05 to 0.15, just behind block1's new position (0.15–0.23). I'm now working out whether block2 ends up partially supported by the ram after it drags forward and falls.

Actually, with heavy loading the slide distance is tiny — only about 1.1cm given the friction deceleration — so block1 barely moves even with a decent push velocity. The tower above only picks up a small relative velocity kick from block2 over a very short timescale, so this quick jab approach doesn't translate into much motion at the top.

Checking whether this impulse causes tipping: computing the tower's mass, height, and moment of inertia, the angular velocity from a base impulse works out to around 1.44 rad/s, but I need to compare the rotational energy against the energy needed to lift the center of mass over the pivot edge, which requires only a tiny height gain of about 0.0039 m.

Given the energy margin is thin, I'm thinking I need the ram to deliver a sustained push rather than a single impulse — driving it continuously over a short distance so the base gets dragged far enough for the tower to actually topple backward. But that raises a concern: tipping backward sends the tower falling toward the ram's own position, so I need to think through whether the collapsing blocks would land back on the ram itself.

I'm reconsidering the ram's geometry to avoid this — maybe making it short and thin, positioned low to the floor, so falling blocks mostly just hit the ground instead of resting on the ram. I could also just exclude collisions between the ram and blocks 2 through 5 so only block1 interacts with it directly.

Now I'm working out the ram's drive mechanism — figuring out mass from the box geometry and density, roughly a kilogram, and thinking through whether a position actuator with damping or a velocity actuator would better control the ram to hit block1 at about 1 m/s and push it forward 8-10cm before stopping.

I realize a plain velocity actuator never stops the ram, so it'd push block1 indefinitely at a constant speed and send it flying off across the world — not what I want. Instead I'll use a position actuator with clamped force (forcerange) and a limited joint range so the ram physically stops at a mechanical limit, giving a controlled push and settle.

Working through the geometry: with the ram's joint range capped at 0.30 and the front face positioned relative to block1's rear, the ram ends up shoving block1 forward by roughly 0.09 — more than block1's own width of 0.08 — which means block1 gets pulled essentially all the way out from under block2, dragging it only slightly. Either way the tower should topple, which is the desired outcome.

I'm narrowing in on limit=0.28 (a 0.07 push) so that block2 overhangs and its center of mass ends up just behind block1's remaining support edge, causing it to tip and fall backward as it rotates about that edge.

For the ram's dynamics, I'm setting forcerange to ±15N with high kp so it saturates, plus joint damping of 5, giving a terminal velocity around 3 m/s; working out the acceleration (~15.6 m/s²) and resulting contact speed over the 0.21m travel distance before damping kicks in, landing around 2.56 m/s.

But I want more standing time before the push, so I'm reconsidering a longer ram travel (0.6m) with reduced force (6N) and damping (4), giving a slower terminal velocity (~1.5 m/s) and roughly 0.5s before contact — then checking that against the floor friction holding block1 in place (μ·5mg ≈ 7.8N) to see if the ram force is enough to overcome it.

The joint limit stops the ram abruptly around q=0.58, but block1 keeps sliding a bit further on its own momentum against floor friction, adding roughly 2 cm more displacement for a total shift near 0.09 m, enough to drag the tower and topple it backward. Afterward block1 rests in place with the ram held against its limit, and the fallen blocks lie on the floor without contacting the ram. I should double check whether the stopped ram's position actually clears the tower's footprint or still overlaps it.

I'm not worried about whether the tower falls forward or backward instead — either way it settles within a few seconds since the block friction (0.6) damps tumbling motion quickly. For initial placement, I'm stacking blocks with centers at 0.05 increments so they touch exactly, letting MuJoCo's soft contacts handle any minor penetration without needing extra margin. For the keyframe, I'm counting out all 36 qpos values — one slide joint for the ram plus seven each for five free-jointed blocks.

Writing actuator config...

Setting contype/conaffinity so ram only collides with block1 and not the floor, while block1 still contacts the floor normally. Gravity and friction values look fine for the ram's sliding motion. Now I'm working through the collision physics: at ~1.8 m/s impact, inelastic collision between ram and block1 settles to roughly 1.25 m/s, and I need to check whether friction drag from block1 onto block2 is enough to topple the tower.

The net accel on the tower's COM (~5.9 m/s²) exceeds the tipping threshold (1.96 m/s²), so the tower starts tipping backward at its base as block1 slides forward. I'm tracking how block1's displacement over roughly 0.06s shifts its position relative to block2, eventually putting block2's COM just behind block1's rear edge — enough to destabilize the stack further.

When block1 stops abruptly, block2 still carries forward momentum but friction quickly decelerates it (within about 1 cm of travel), leaving the overhang mostly intact along with the backward rotation already underway — so the tower topples, landing roughly half a meter behind its starting point.

Now I'm setting up the MJCF keyframe with initial block positions stacked vertically, placing the ram body in the worldbody after the blocks with its control activated, and naming all bodies, geoms, and freejoints before writing the file.

