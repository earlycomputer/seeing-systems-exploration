**What I expect from the original file:** it will not topple.

- **The sphere's trip.** The sphere starts with 1.5 m/s of sliding and no spin. Floor friction quickly turns this into rolling at about 5/7 of that speed, roughly 1.07 m/s. It rolls about 1 m and reaches `block1` after about 1 s.
- **The impact.** The 4 kg ball strikes the bottom block at its centre height. The contacts are soft and nearly inelastic, so ball and block move off together at about 0.95 m/s. Floor friction on the loaded bottom block is about 15 N, and friction from the stack above adds about 12 N. Ball and block therefore stop within about 0.15 s, after only a few centimetres.
- **The stack's response.** The blocks above are dragged forward briefly and then braked again. The backward lean from the start of the shove is roughly cancelled by the forward lean from the stop. The stack ends up shuffled slightly and still standing on its footprint, which is far less than a topple.

**The fix.** I replaced the coasting ball with a slide-jointed ram already touching `block1`. A motor, whose control the keyframe sets, pushes it with a steady 30 N.

- **Acceleration.** That force accelerates ram, bottom block and riding stack at about 0.45 g. This is below the inter-block friction limit of 0.6 g, so the upper blocks are carried along rather than slipping off.
- **Why that tips the stack.** In the accelerating frame, effective gravity leans by about 24°. Blocks 2–5 form a column 0.8 m tall and 0.2 m wide, which tips once the lean passes about 14°. So the column rotates backward about block 2's trailing edge.
- **Timing.** The ram stops at a joint limit after 0.6 m, at about 0.5 s. By then the column has already tipped past its balance point, so it falls back toward the ram and onto the floor.

```json
{"what_happens": "In the original, the sphere rolls about 1 m and hits the bottom block at about 1 m/s. Ball and block stop within a few centimetres under floor and inter-block friction. The stack shuffles slightly and stays standing. In the corrected file, a motor-driven ram pushes the bottom block with steady 0.45 g acceleration. The upper four blocks are carried along by friction, rotate backward past their tipping angle, and fall off as the bottom block is shoved away.", "works": false, "problem": "The rolling sphere delivers a brief ~1 m/s nudge that friction stops within a few centimetres, too gentle and too short to tip the stack, so all five blocks stay standing."}
```

```xml
<mujoco model="stack_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="6 6 0.1" friction="0.6 0.005 0.0001"/>
    <body name="block1" pos="0 0 0.100">
      <freejoint/>
      <geom name="block1" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block2" pos="0 0 0.300">
      <freejoint/>
      <geom name="block2" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block3" pos="0 0 0.500">
      <freejoint/>
      <geom name="block3" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block4" pos="0 0 0.700">
      <freejoint/>
      <geom name="block4" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block5" pos="0 0 0.900">
      <freejoint/>
      <geom name="block5" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="pusher" pos="-0.1505 0 0.1">
      <joint name="pusher_slide" type="slide" axis="1 0 0" limited="true" range="0 0.6"/>
      <geom name="pusher" type="box" size="0.05 0.12 0.08" mass="1.0" friction="0.6 0.005 0.0001"/>
    </body>
  </worldbody>
  <actuator>
    <motor name="push" joint="pusher_slide" gear="1" ctrllimited="true" ctrlrange="0 40"/>
  </actuator>
  <keyframe>
    <key name="start" qpos="0 0 0.100 1 0 0 0  0 0 0.300 1 0 0 0  0 0 0.500 1 0 0 0  0 0 0.700 1 0 0 0  0 0 0.900 1 0 0 0  0" qvel="0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0" ctrl="30"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out the physics here: a sphere of radius 0.1 and mass 4 starts at x=-1.2, z=0.1 with initial velocity 1.5 m/s but no spin, rolling on the floor. Since MuJoCo combines contact friction by taking the max of the two geom frictions, the effective friction becomes 0.6 rather than 0.3, which will affect how quickly rolling without slipping is established.

I'm calculating the transition from sliding to rolling: with mu=0.6, the sphere reaches pure rolling velocity (5/7 of initial, about 1.07 m/s) after roughly 0.073 seconds, then rolls at constant speed since condim=3 means no rolling resistance. From there I estimate the sphere travels about 1 meter (taking roughly 1 second) before striking the bottom block of a stack, where it transfers momentum — treating the collision as inelastic with the 0.5 kg block (plus 2 kg stacked on it) gives a combined velocity around 0.95 m/s, after which friction continues to act as the block begins sliding out from under the stack.

Recomputing with deceleration gives stop time around 0.16s and distance roughly 0.08m for block1, though the sphere's rolling contact and spin add complications I'm approximating. So block1 shifts maybe 0.08-0.1m while block2 drags along maybe 0.04m due to friction, meaning the upper stack's base shifts relative to block1 but perhaps not enough to topple.

Since each block in the 4-block stack gets dragged individually by friction from the block below rather than acting as one rigid column, they likely shear and slide slightly past each other rather than collectively tipping over - I need to check what horizontal acceleration threshold would actually cause a 0.2x0.2 block to tip rather than just slide.

It's a close call so the problem is ambiguous, but let me think about it as a dynamic tipping problem instead. With the impulse lasting about 0.16s, the base gets a velocity change near 0.9 m/s, and treating the column as rigid, it would need to rotate about 14° (tan⁻¹(0.1/0.4)) to tip over its trailing edge—so I should check whether the impulse delivers enough energy to raise the center of mass that far.

Computing the pivot moment of inertia and required angular velocity to lift the CoM by 0.012 m gives ω≈1.02 rad/s needed, but I realize the horizontal base impulse passes right through the pivot point itself, so it actually produces no torque about that pivot—meaning the naive impulse-angular-momentum argument doesn't directly apply, and the real tipping mechanism comes from the column lagging behind the accelerating base, effectively acting like gravity tilted in the accelerating frame.

That effective tilt angle of 31° exceeds the 14° stability threshold, so the column does tip backward while the acceleration phase lasts. I compute the torque about the pivot from this effective gravity, giving angular acceleration α≈6.05 rad/s², and over the 0.16s acceleration duration this yields ω≈0.97 rad/s and a tip angle of about 4.4°. Then I start considering what happens right as block1 stops—the column, now moving forward at around 0.94 m/s, would experience a backward friction impulse at its base that could tip it forward instead.

I'm also checking whether block1 itself might slide out from under the column rather than just decelerate it. Looking at the sphere-block contact point, I work out that the sphere's rotation gives its leading contact surface a downward velocity, meaning friction pushes the block down and the sphere up, which seems fine. I'm also wondering whether MuJoCo's default soft-contact parameters might introduce some unwanted bounce.

With critical damping there's little bounce, though the lighter 0.5 kg block could still pick up significant velocity. Overall this is quite uncertain — the stack likely sways and shifts rather than cleanly topples unless the bottom block is knocked out fast enough that the blocks above fall straight down and simply restack, similar to the tablecloth trick.

To get a reliable topple, I should instead drag the base block partially so the column overhangs, or rely on strong friction between block1 and block2 so pushing block1 drags the whole base and tips the column backward — essentially a sustained, strong lateral push rather than a brief impulse. A heavy, fast pusher (like a 20 kg sphere at high speed) striking block1 seems like the simplest way to achieve this.

A constant-velocity push won't do it, so instead I consider shoving the bottom block sideways enough that the stack above loses support: if block1 shifts about 0.15m while block2's center stays put, the overlap shrinks until block2's center of mass falls outside the support region, causing it to topple backward around block1's trailing edge—this seems like a reliable way to trigger toppling.

If block1 moves out too slowly it just gradually drags the stack along; if too fast, the whole stack drops flat without tipping. The right regime is a quick partial shove, so that once the trailing edge passes the upper stack's CoM, the stack begins rotating backward with little support left, falling roughly 0.2m while rotating, landing on its trailing edge.

I'm reconsidering a slower, continuous push instead—like a heavy slow pusher at low speed, where static friction might just drag the whole stack together without toppling. So maybe the key variable is lowering friction specifically so block1 slides under block2 while the upper blocks maintain enough friction with each other to stay put.

Since MuJoCo uses the max of contact frictions, I need to tune floor friction down too, otherwise block1-floor contact stays high and resists sliding. The plan: push block1 slowly but with enough momentum (heavy pusher, moderate speed) so it slides out from under the stack while the stack above barely moves due to low drag, until block1's trailing edge clears the stack's position.

Once that support edge recedes, the stack tips toward the pusher side since its center of mass sits behind the shrinking support — I'm working through the torque buildup as the lever arm grows, computing angular acceleration and rotation angle over the short window before support is fully lost, finding the tilt stays small (~0.02 rad) before the column begins to free-fall the remaining drop distance.

But then I realize the pusher sphere itself occupies exactly the space where block2 would land, since the sphere's leading edge tracks block1's trailing edge — meaning the falling stack would actually come down right on top of the ball rather than onto the floor.

Trying a slower push instead: at 0.2 m/s, I work out the tilt angle grows roughly as t³, reaching about 0.18 rad (10°) by t=0.5s with angular velocity near 1.08 rad/s, which is close to the tipping threshold I estimated earlier for a 14° critical angle. So even with a gentler push, the column likely still topples once it loses base support, and then lands on the sphere anyway.

But I realize I need to check friction coupling: with μ=0.1, static friction could drag the upper stack along with block1 before it ever slips free, since the friction acceleration is enough to bring the stack up to 0.2 m/s within about 0.2 seconds — meaning no relative sliding actually happens, which ruins the intended mechanism. I need an impulsive start instead, accelerating block1 fast enough that friction can't keep up and drag the stack along with it.

Even working through the numbers for v=0.6 m/s, the relative slip comes out to 0.18 m — more than the 0.1 m needed for the center of mass to pass the trailing edge — but then it's tipping while still sliding, which complicates the dynamics a lot. I think I need a completely different approach: maybe strike the bottom block directly in a "rug pull" style maneuver that tips the stack backward, rather than relying on friction dragging alone.

Checking the tipping condition more carefully, each interface can sustain acceleration up to μg given uniform friction coefficients, so a sustained a=0.5g should eventually tip the column — I'm estimating the angular acceleration needed and the duration required for this to actually happen.

To implement this physically, I'd need a pusher object on a slide joint with a motor driving constant acceleration into the stack, accounting for the combined mass of the pusher and blocks plus floor friction to size the required force.

But I need to reconsider whether the stacked blocks move together rigidly or slip against each other instead of tipping — a single cube tips only if acceleration exceeds g times its width-to-height ratio, and slips if acceleration exceeds mu*g. Since mu=0.6 is less than 1, individual blocks would slip before tipping, so I need to think through how the interfaces between stacked blocks behave under this acceleration to determine if the column tips as a rigid unit or the blocks shift relative to each other.

checking that 3-5 also wants to tip relative to block2, confirming it's messy but the stack topples backward toward -x since a=0.5g stays under the friction limit of 0.6g, so no slip occurs. I should also check block1 against the floor: the 1-5 column has tipping threshold tan 0.2, but the pusher's contact force at block1's face complicates whether block1 itself tips about the floor edge.

So the whole stack topples backward onto the pusher, which is fine since toppling is the goal — though I need to make sure the stack falling onto the pusher doesn't cause issues with the actuator pushing for the full 6 seconds. I'll give the pusher's slide joint a limited range (like 0 to 0.6 m) so it just stops against the limit once it reaches it, rather than relying on a free sphere with initial velocity which can't sustain acceleration — a motor is simpler and more reliable here.

Now I'm positioning the pusher body with its slide joint and motor actuator, controlled via a keyframe ctrl value, working out the exact starting position and box dimensions so the pusher's front face just touches block1 initially without a gap, while keeping its geometry clear of the floor.

Since gravity acts only along the constrained slide axis via the world parent, I don't need separate contact handling for the pusher against the floor. I'm estimating the force needed to produce roughly 0.45g acceleration across the combined pusher-and-blocks mass, factoring in floor friction on block1 to size the required push force.

I should double check whether this acceleration is sufficient to tip the block column past its stability threshold, since the friction demand on block2 from block1 stays within the available max friction even as the stack begins tipping and normal forces shift slightly.

Computing the pivot moment of inertia for the column (treating it as a rigid rectangle about the corner), I get the torque from the combined effect of horizontal acceleration and gravity, giving an angular acceleration around 3.44 rad/s². I'm now checking the time needed to rotate to the critical tipping angle against how long the acceleration phase actually lasts before the slide reaches its limit.

Setting the slide range at 0.6 m, I find the acceleration ends around t=0.52s with the block rotated well past 0.46 rad—a comfortable margin, with exit velocity around 2.3 m/s. The pusher stops but the block keeps sliding under friction while already tipped past the point of no return, so the topple is secure as long as acceleration stays under roughly 0.6g to avoid slip at block 2—though slip there might not even stop the topple from propagating up the stack.

Now I'm setting up the pusher joint—placing it directly in the world body with a slide joint, explicit limits (0 to 0.6), no damping, and a motor actuator with gear 1 and ctrlrange 0-40. The keyframe needs a ctrl value of 30 and the qpos array sized to match.

I'm reconsidering the total state size—5 bodies × 7 plus 1 gives 36 qpos entries and 31 qvel. I'm also thinking about timing: if the pusher starts with a gap before touching the stack, it would build up speed and cause an impact rather than a gentle push, so it's safer to keep the pusher already in contact at t=0 so the stack starts standing and gets pushed smoothly from the start rather than introducing a delay or impact velocity.

Simulating the scenario mentally, the sphere rolls about a meter and taps block1 at roughly 1 m/s, which nudges the stack enough to wobble without toppling it—seems workable. I'm also checking friction and contact geometry so the pusher box stays properly aligned against block1's face without vertical sliding, and confirming that if the stack tips backward it lands safely onto the pusher. Now I'm finalizing the pusher's dimensions and mass before writing it into the file.

Adding the slide joint with its name, keyframe control value, and final qpos entry...

