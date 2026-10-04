**What I expect from the original file.** The sphere starts at 1.5 m/s. It skids briefly and then rolls at about 1.07 m/s. Its `0.005` rolling-friction value does nothing, because the default `condim` of 3 does not model rolling friction. It strikes the bottom block at mid-height.

The contact absorbs most of the bounce, so the sphere and block1 continue together at roughly 0.95 m/s. Two friction forces brake block1:
- the floor, which carries the weight of the whole stack (about 15 N),
- the underside of block2 (about 12 N).

The same block1–block2 friction drags the four upper blocks forward with it. By my estimate, block1 slips only about 4 cm under block2 before everything moves as one. The sphere, block1 and the stack then slide a few centimetres and stop.

The upper column does get a brief backward tilt during the hit. But its tip-over energy and the energy it receives are about equal, so whether it falls is a coin flip. Most likely the stack ends slightly shifted and still standing. That does not satisfy "then topples".

**What the corrected file does.**
- The four upper blocks start as a straight column offset +6 cm over block1, so the column's centre of mass is 4 cm inside block1's +x edge. The stack is statically stable.
- A 1 kg box pusher slides in from the +x side at 3 m/s and hits block1 low on its face, below block2.
- Block1 has lower friction (0.3, given `priority="1"` so it governs all of block1's contacts).
- By my estimate, block1 is knocked about 7 cm in −x relative to the column. That is more than the 4 cm margin and less than the 14 cm that would clear block1 out from under block2 entirely.
- The column's centre of mass ends up beyond block1's +x edge. The friction drag on its base also tips it the same way, so it falls over toward +x, onto the pusher and the floor.
- The pusher is low and wide, so its own friction stop does not tip it.

```xml
<mujoco model="stack_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="6 6 0.1" friction="0.6 0.005 0.0001"/>
    <body name="block1" pos="0 0 0.100">
      <freejoint/>
      <geom name="block1" type="box" size="0.1 0.1 0.1" mass="0.5" priority="1" friction="0.3 0.005 0.0001"/>
    </body>
    <body name="block2" pos="0.06 0 0.300">
      <freejoint/>
      <geom name="block2" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block3" pos="0.06 0 0.500">
      <freejoint/>
      <geom name="block3" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block4" pos="0.06 0 0.700">
      <freejoint/>
      <geom name="block4" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="block5" pos="0.06 0 0.900">
      <freejoint/>
      <geom name="block5" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.6 0.005 0.0001"/>
    </body>
    <body name="pusher" pos="0.5 0 0.06">
      <freejoint/>
      <geom name="pusher" type="box" size="0.06 0.08 0.06" mass="1.0" friction="0.6 0.005 0.0001"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0 0 0.100 1 0 0 0  0.06 0 0.300 1 0 0 0  0.06 0 0.500 1 0 0 0  0.06 0 0.700 1 0 0 0  0.06 0 0.900 1 0 0 0  0.5 0 0.06 1 0 0 0" qvel="0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  -3.0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```json
{"what_happens": "The sphere rolls in at about 1 m/s and shoves the bottom block, but block1-block2 friction drags the upper stack along after only ~4 cm of slip. The whole stack slides a few centimetres and most likely stays standing, slightly shifted, rather than toppling.", "works": false, "problem": "The push is too weak and too friction-coupled to undermine the stack: the bottom block slips only a few centimetres before the stack moves with it, and the brief tilt of the column is too marginal to reliably topple it."}
```

---
thinking (summarized):

I'm working through the sphere's motion: starting with friction-driven sliding that transitions to pure rolling, where the solid sphere settles at 5/7 of its initial speed, roughly 1.07 m/s, then factoring in rolling friction for the continued deceleration.

Checking MuJoCo's default settings, though, I realize condim=3 means rolling friction coefficients are ignored entirely, so the sphere actually maintains its ~1.07 m/s rolling speed right up to impact with the bottom block. Now I'm sizing up the collision: a 4 kg sphere moving at about 1 m/s striking a 0.5 kg block that's supporting a 2.5 kg stack above it.

I'm weighing the resisting friction forces on that bottom block — from the floor and from the block above it — against the sphere's momentum, trying to figure out whether the impact just slides the bottom block out from under the stack like a tablecloth trick, or whether it drags the whole tower forward. If the base block gets kicked out quickly, the stack above would drop and possibly destabilize, with friction at the base potentially inducing a backward tipping tendency in the remaining tower as it's yanked forward.

Then I'm tracing where block2 ends up — whether it lands on the floor or gets caught by the sphere, since the sphere keeps moving at +x after the collision. Estimating post-collision velocities using a mass ratio of roughly 4:0.5, I get block1 moving around 1-2 m/s depending on how elastic the contact is, then checking whether it clears the 0.2m needed to slide out from under block2, and noticing the sphere's height puts it right at block2's bottom surface, meaning it would likely roll into contact with it too.

Given friction values (~14.7N floor friction, ~11.8N on block2), I'm working out whether block1 and the sphere stay coupled and decelerate together, and whether that's enough to call this a clean "topple" versus a messier partial collapse with the sphere sliding underneath the upper blocks.

I'm reconsidering whether block1 moves alone or drags the whole upper stack via friction — treating the stack above as rigidly moving together, I compute the combined system (sphere plus all blocks, 6.5 kg) decelerating under floor friction at about 2.26 m/s².

But since the impact occurs over a very short timescale, the friction-limited impulse transmitted to the upper stack is small compared to the large velocity jump block1 receives directly from the impact. This suggests block1 slips relative to block2 rather than moving together with it, since MuJoCo's default contact solver behaves close to critically damped with near-zero restitution.

I'm checking whether the upper stack tips: its tipping threshold is about 2.45 m/s², but the base acceleration of 5.9 m/s² exceeds that, so the stack would tip backward, pivoting about the trailing edge of block2's contact with block1. I need to work out how much that trailing edge overhangs given block1's 3.8cm forward slide.

Computing the pivot location, I find the overlap region shifts by the same amount block1 moved, and inter-block friction between block2 and block3 also caps at 5.9 m/s², matching the threshold exactly — but the acceleration only lasts about 0.08s, so the angular impulse from this tipping torque may be too small to actually topple the stack before everything reaches a common velocity.

Actually, accounting for the sphere's rolling inertia, its effective mass is 5.6 kg, giving a combined effective mass of 8.1 kg and a deceleration of 1.8 m/s². That means the system stops after about 0.27 s, traveling roughly 6 cm, after which both block and sphere come to rest together with the sphere pressed against the block.

Checking whether the stack tips during the initial 0.08 s impulse, I estimate the net torque about the pivot edge from the inertial force versus the restoring gravity torque comes out to around 3.5 N·m, so I need to compare this against the stack's moment of inertia about that edge to see if it's enough to topple it.

Working through the angular acceleration (~8 rad/s² over 0.08 s gives ω≈0.64 rad/s), I find the kinetic energy gained (~0.09 J) is nearly equal to the energy needed to tip the COM over the pivot (~0.094 J) — it's genuinely borderline. Given the uncertainty from the later deceleration phase and the fact that blocks aren't rigidly connected, I can't be confident whether it actually topples or just rocks and settles back.

Given that marginality, I think the design needs to be more robust: rather than relying on this knockout tipping effect, I should rethink the mechanism to guarantee toppling instead of a classic "shoot the bottom block out and the stack drops straight down" trick, which wouldn't satisfy the actual goal of making it fall over.

Working through the geometry: if block1's shift stays under 0.1 the stack's center remains supported, but between 0.1 and 0.2 the stack's center hangs past block1's trailing edge and topples backward off the stack, while beyond 0.2 block1 just clears out from under it entirely. It's a narrow window to hit, and friction dragging the stack forward will complicate tuning it precisely.

Maybe instead of a sudden impulse, I should consider a sustained slow push — but the strong friction between block1 and block2 means the stack would just get dragged along rather than tip, since tipping needs acceleration, not just steady motion. Perhaps a cleaner mechanism is hitting block1 off-center so it also rotates slightly, inducing asymmetric loss of support.

Another angle: make the tower taller and narrower relative to its base so dynamic tipping is more sensitive — say blocks about 0.1 wide and 0.2 tall, giving a lower tipping acceleration threshold while still being statically stable until pushed.

This still feels uncertain and chaotic given the forward/backward deceleration swings on a 5-block independent stack, so I'm considering a more deterministic setup instead — maybe something that uses a hinge or a continuously moving heavy pusher rather than relying on a fragile tipping energy balance.

Trying a constant-speed pusher against block1 just drags the whole stack along uniformly without toppling it, so that doesn't work either. I'm now thinking about lowering the friction specifically between block1 and block2 to decouple their motion and force a topple.

A constant-velocity push won't work since zero acceleration just drags the whole stack along together. I need an impulsive push instead: give block1 a quick velocity so with low friction to block2 it slides out relative to the stack, but then the pusher sphere's continued contact complicates the dynamics—maybe I should make the pusher lighter so it delivers an impulse and disengages rather than sustaining the push.

Thinking about toppling direction too: with a partial knockout the stack would tip backward toward the sphere, which isn't reliable on its own. I could instead try an asymmetric leaning stack configuration where the combined center of mass sits near the edge of block1's footprint, so a push shifts things just enough to tip it over rather than just displacing block1.

Actually a straight stack works fine too—margin just needs to be 0, so direction of push doesn't matter there. Let me think about slender cube blocks and designing a leaning stack where blocks 2-5 sit offset so their combined COM stays just within block1's footprint but close to the edge, making a small push enough to topple it.

So the pusher must approach from the +x side, striking block1's face at x=0.1, but I need to check whether the overhanging block2 (which spans up to x=0.16) would interfere with the sphere's path given its radius and height, checking the exact contact geometry near x=0.16.

I'm leaning toward using a sliding box pusher instead of a sphere — sitting on the floor with initial velocity, decelerating from friction and stopping naturally rather than pushing indefinitely, which seems cleaner than fiddling with sphere radius and contact height to avoid tipping or hitting block2.

For the block1-block2 interaction, I'm considering lowering the friction via an explicit contact pair rather than relying on the default 0.6, since that would reduce unwanted drag. I need to check whether MuJoCo adds this explicit pair on top of the automatically generated contact or replaces it.

Actually, maybe I should use geom priority to control which friction value applies in each contact pair instead of relying on the combination rule — giving block1 lower priority friction so its contact with the floor uses 0.15 while still combining properly elsewhere. Then I'm reconsidering whether lowering friction is even necessary, since with 0.6 friction between block1 and block2 the whole column would get dragged along with block1's acceleration, risking a tip toward the opposite direction.

I decide a moderate friction of 0.3 via priority works for block1's contacts with both block2 and the floor. Now I'm working through the dynamics: the pusher box slides in on floor friction and strikes block1, and I want block1 to shift relative to block2 by roughly 0.05-0.1 m so the column's center of mass passes the pivot point and topples.

I'm calculating the slip threshold needed for block1 to fully clear block2's contact region (around 0.14 m), but I actually want a smaller slip of about 0.08 m so the column tips without the block fully separating. I'm now setting the pusher mass to 1.0 with friction against the floor giving a max combined friction of 0.6.

I'm working out the pusher's approach: starting 0.34 m from impact with an initial speed of 2.5 m/s and decelerating at roughly 5.9 m/s² due to friction, so it hits block1 at about 1.5 m/s before transferring momentum in the collision.

After impact, I'm treating the pusher and block1 as moving together, combining their masses with the frictional forces from the floor and from block1's contact with block2, giving a deceleration around 12.8 m/s² for the joined pair right after collision.

Separately I'm computing the column's own acceleration from its base friction, roughly 2.9 m/s², and comparing the relative velocity decay between column and pusher-block system. The relative slip distance comes out to about 0.032 m, which falls short of what's needed, so I check whether the column tips instead — tracking how its center of mass shifts toward the pivot edge as it decelerates, finding the tipping threshold is exceeded, and starting to work out the torque impulse that would initiate tipping.

Then I estimate the moment of inertia about the pivot, getting roughly 0.43, which gives an angular velocity around 0.27 rad/s and kinetic energy of about 0.016 J, compared against a potential energy barrier of about 0.0016 J — the kinetic energy clears the barrier, suggesting the column topples, though I flag this as a marginal result given the approximations. I decide to try a stronger initial push velocity to get a cleaner, less ambiguous outcome.

Testing v0 around 3.0-3.5, I compute the slip distance after impact to land between 0.04 and 0.14 meters, which keeps the center of mass clearly past the tipping edge while staying within the range where the column remains in contact with the surface — settling on v0≈3.0 as a solid middle-ground choice that gives a definitive toppling result.

Once block1 shifts, the column tips about its edge and falls onto the pusher and floor, so it topples as intended. I check whether the push itself, applied low near the floor, could tip block1 forward—but since the force acts below its center of mass with floor friction at the base, it shouldn't tip much. The pusher box itself stays stable while decelerating since it's low and wide enough that friction alone won't exceed its tipping threshold.

I also verify the initial leaning stack is statically stable, with the column's center of mass comfortably within block1's support polygon. Checking the friction priority settings confirms contacts correctly use block1's friction values. Finally, I reason through why the original setup likely doesn't topple—the sphere's impact speed is modest enough that the bottom block only slides a few centimeters before the whole stack gets dragged along together, rather than block1 slipping out from under the column.

Setting up the keyframe positions now: blocks stacked at x=0.06 from z=0.1 up to z=0.9, with the pusher starting at x=0.5 moving at -3.0 velocity. I check the geometry—pusher's front face at x=0.44 versus block1's face at x=0.1 gives a 0.34m gap, so about 0.12s before impact, which lines up with my earlier timing estimate.

