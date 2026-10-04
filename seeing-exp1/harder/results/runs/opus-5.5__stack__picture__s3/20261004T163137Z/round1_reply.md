**What happens.** The 4 kg sphere rolls from x = −1.2 m toward the stack. Its copies end at about x = −0.2 m, where it touches block 1. The five-block column stays upright at x ≈ 0 through the whole residue window. It jitters slightly in place but does not tilt or fall.

**Why it fails.** The sphere's roughly 1 m/s hit gets absorbed by block 1. With friction 0.6 everywhere, the floor friction plus the drag from the four blocks on top stop block 1 within a few centimetres. The upper blocks are dragged along with it, so the stack never loses support.

**Fix.**
- **Pusher:** replace the sphere with a motor-driven pusher. It is a low, flat ram on a slide joint, driven by a velocity actuator whose control the keyframe sets to 1.5 m/s.
- **Stop point:** a joint limit stops the ram after it has shoved block 1 about 0.13 m. Block 1 coasts a few centimetres further.
- **Friction:** the blocks' own friction drops to 0.1, so block 1 slides out from under block 2 instead of carrying the column. Block-to-floor contact stays at 0.6, because MuJoCo uses the larger friction of a contacting pair.
- **Result:** the upper four blocks lag behind (μ = 0.1 is below the 0.25 tipping ratio for that column, so they don't tilt during the push). They are left offset by more than half a block width, about 0.15 m against the 0.1 m needed. Their centre of mass then hangs past block 1's trailing edge and the column topples backward.
- **Timing:** the ram starts 0.6 m away, so the stack stands untouched for about 0.4 s first.

I have not run the corrected file. The 0.15 m offset and the topple are hand estimates and need a new render to confirm.

```xml
<mujoco model="stack_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="6 6 0.1" friction="0.6 0.005 0.0001"/>
    <body name="block1" pos="0 0 0.100">
      <freejoint/>
      <geom name="block1" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.1 0.005 0.0001"/>
    </body>
    <body name="block2" pos="0 0 0.300">
      <freejoint/>
      <geom name="block2" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.1 0.005 0.0001"/>
    </body>
    <body name="block3" pos="0 0 0.500">
      <freejoint/>
      <geom name="block3" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.1 0.005 0.0001"/>
    </body>
    <body name="block4" pos="0 0 0.700">
      <freejoint/>
      <geom name="block4" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.1 0.005 0.0001"/>
    </body>
    <body name="block5" pos="0 0 0.900">
      <freejoint/>
      <geom name="block5" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.1 0.005 0.0001"/>
    </body>
    <body name="pusher" pos="-0.65 0 0.05">
      <joint name="push" type="slide" axis="1 0 0" limited="true" range="0 0.63"/>
      <geom name="pusher" type="box" size="0.05 0.15 0.03" mass="1.0" friction="0.1 0.005 0.0001"/>
    </body>
  </worldbody>
  <actuator>
    <velocity name="push_motor" joint="push" kv="500" ctrllimited="true" ctrlrange="-3 3" forcelimited="true" forcerange="-300 300"/>
  </actuator>
  <keyframe>
    <key name="start" qpos="0 0 0.100 1 0 0 0  0 0 0.300 1 0 0 0  0 0 0.500 1 0 0 0  0 0 0.700 1 0 0 0  0 0 0.900 1 0 0 0  0" qvel="0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0" ctrl="1.5"/>
  </keyframe>
</mujoco>
```

```json
{"what_happens": "The heavy sphere rolls from x=-1.2 m toward the stack and stops against block1 at about x=-0.2 m. The five-block column stays upright at x~0 the whole time, shifting slightly in place but never tilting or falling.", "works": false, "problem": "The sphere's impact only nudges block1, and with friction 0.6 throughout the upper blocks ride along with it, so the stack never topples."}
```

---
thinking (summarized):

I'm tracing the sphere's motion as it rolls from -1.2 toward the stack at 0, with residue trails showing its positions up to about 1.91 seconds, and working out how friction converts its initial sliding velocity into rolling motion, reducing its speed by the factor 5/7.

Now I'm figuring out the collision dynamics: the sphere covers roughly 1 meter before contacting the bottom block, taking about 0.8 seconds, then I'm estimating how the impact transfers momentum into the bottom block, factoring in floor friction and the friction drag from the block above it. I'm reasoning through whether this could produce a tablecloth-trick effect where the bottom block slides out while the upper blocks stay standing, or whether the friction at the base causes the upper stack to tilt backward as it lags behind.

Checking the tipping condition for the upper two-block stack, I find the required friction coefficient (width-to-height ratio) is about 0.25, while the actual friction coefficient is 0.6 — suggesting the stack would tend to tip, though this depends on how long the relative sliding motion persists. I'm then shifting to reading pixel coordinates from the image to pin down the real-world position of the right-hand column, converting the pixel range into meters using the scale factor I calculated.

Tracking the column through the sequence, it stays upright and doesn't topple within the 1.91 s window—just some residue showing the block shifted slightly. The sphere seems to hit the stack and push it a bit rather than knock it over, so I'm trying to figure out why it didn't topple given the sphere's radius and impact height relative to the column's center of mass.

To actually get a topple, I probably need a stronger, more sustained push—maybe knocking out the bottom block so the upper stack falls, rather than pushing the whole stack uniformly (which just slides it). I'm considering using a slide joint with a velocity-driven pusher moving at a moderate speed to knock the base block out from under the stack.

I'm reconsidering the friction setup — maybe lowering block-to-block friction (like 0.1) would let block1 slide out from under the stack more cleanly, with the stack lagging behind and partially overhanging the edge before tipping, rather than getting dragged along at the same speed.

Block2 contacting block1's trailing edge would tip toward the pusher side, though with low interblock friction the upper four blocks might just shear apart rather than tip as a unit, making this hard to predict without actually simulating it. Maybe I should step back and reconsider why the original setup didn't topple — the sphere hit block1 at roughly 1.07 m/s, and I need to think through how MuJoCo's contact model handles that collision.

Estimating it as a roughly inelastic collision: sphere plus block1 end up moving together, decelerating quickly from combined floor and interblock friction, stopping within about 0.16s after traveling only ~0.08m — while the upper stack, dragged along at up to 0.6g, nearly moves together with block1 rather than tipping independently.

For a more reliable topple design, I'm thinking of using a motorized pusher giving block1 a sustained push, with reduced friction between block1 and block2 so block1 slides free while the stack lags behind and falls backward. Alternatively, high friction plus a hard acceleration impulse (to around 3 m/s) on block1 could create enough torque via friction on block2 to tip the stack, provided the acceleration exceeds g*(width/height) and μ stays above roughly 0.25.

But checking the geometry more carefully, the full stack (com height 0.4, half-width 0.1) does satisfy the tipping condition since 0.6*0.4 exceeds 0.1, so it tips backward as block1 slides under. However block2 alone (com height 0.1) fails that condition — 0.6*0.1 is less than 0.1 — so it would just slide rather than tip, and the blocks above it are only dragged along by friction, which complicates whether the whole column acts rigidly or shears apart.

I'm now considering alternative ways to force a clean topple: rapidly yanking the tablecloth-style block1 out could make the stack drop and possibly tilt on landing, but that's not guaranteed; pushing block1 slowly with high friction everywhere just drags the whole stack with no topple. A more promising approach might be to displace block1 only partially — say by 0.15 m — so it moves while the upper stack stays put, requiring low friction between block1 and the stack above but enough friction elsewhere to keep the rest stationary.

I'm setting up differential friction values (block-block low, like 0.1, versus floor friction higher like 0.6) and designing a motorized slide-joint pusher that nudges block1 at a controlled velocity with a limited range of travel so it stops after roughly 0.18 m.

Trying a faster push of 1.5 m/s instead: block1 covers the 0.18 m gap in just 0.12 s, so the upper stack barely accelerates before block1 stops, then slides a bit further afterward from momentum. Total relative offset comes out around 0.165 m, which exceeds the 0.1 m threshold needed to shift the stack's center of mass past block1's edge, so this should be enough to topple it.

I'm checking where the pusher's right face sits relative to block2's overhanging corner—if the pusher top is low enough, the tilting stack would hit it partway through its fall rather than tipping freely, so I'm estimating the rotation angle before contact happens, which looks like it's still too large to prevent the stack's center of mass from swinging past the point of no return.

Since the fall direction always swings back toward the pusher, I'm considering whether a lower, thinner pusher plate would let block2 drop further before contact, buying more rotation angle margin, or whether a more complex swinging-hammer mechanism would be needed instead—but that seems overengineered, so I'll stick with a sliding pusher approach.

I'm switching to a velocity actuator for the pusher joint, estimating the force needed to overcome friction against block1's weight, and capping forcerange around 300N so the joint limit can safely absorb the push without excessive penetration. I'll set the initial ctrl value in the keyframe accordingly.

I also want the pusher to start further back for a visible "standing still" phase before contact—placing it with a 0.5m gap so it takes about a third of a second to reach the block, and I'm working out the corresponding qpos/qvel entries and slide joint range to match that travel distance.

Thinking through the physics after impact: block1's friction deceleration from the floor (accounting for the stacked load on top) means it won't stop instantly at the pusher's position—it'll slide a bit further, roughly 0.04m more, so I need to recalculate the total displacement to make sure it stays just under the threshold where the upper stack would topple versus fall straight, tuning the pusher's stop position accordingly to keep the toppling effect intact.

Checking the internal friction between block2 and block3: the available static friction of about 1.47N just barely matches the force needed to drag the upper stack along at the same acceleration, so it's borderline but workable either way. I also need to position the pusher so its bottom edge clears the floor, setting its center height with half-height 0.03 so the bottom sits at 0.02, and confirming the slide joint only moves along x so gravity doesn't interfere.

Checking pusher-block contact friction: since both pusher and blocks have friction 0.1, the effective contact friction stays at 0.1 (not lifting block1), while floor-block friction at 0.6 stays dominant — that's fine. The pusher contacts block1 low on its face (z 0.02-0.08) versus the block's center at 0.1, so the push force creates only a small tipping moment, which should be negligible given block1's heavy loading. The pusher moving at 1.5 m/s with a velocity servo will deliver an impulse on impact, which seems acceptable.

Writing velocity actuator config...

I need to work out qpos/qvel ordering: five blocks contribute 35 qpos values (7 each) plus one slide joint for the pusher, giving 36 total, and qvel has 30+1=31. Then I'm defining the pusher body itself with its slide joint along the x-axis and a box geom sized and massed appropriately, with low friction matching the block friction setting.

Checking contacts: the pusher bottom and block bottoms sit near the floor without touching it directly, and as block2 tips, the upper blocks should fall toward negative x onto the pusher's top surface, which looks fine. I'm ready to write up the final answer now.

