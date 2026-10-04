**Expected behaviour of the submitted scene**

- The pusher sphere starts sliding at 1.5 m/s with no spin. Floor friction quickly turns this into rolling at about 5/7 × 1.5 ≈ 1.07 m/s.
- It reaches block1 after about 1 s. The collision is soft and mostly inelastic, so block1 picks up only about 0.95 m/s.
- Two friction forces then slow block1 sharply: the floor's, and block2's on its top face. Block2's friction can accelerate the upper four blocks at no more than about 5.9 m/s². Block1 therefore slides only about 5 cm relative to the stack before the two move together.
- That brief friction kick tilts the upper stack back by roughly 0.03 rad. The kinetic energy involved (about 0.07 J) is far below what is needed to lift it over its tipping edge (about 0.2 J).
- The combined group then slows at only about 2 m/s², which is too gentle to tip it forward.
- Result: the stack slides forward about 0.15–0.2 m, rocks a little, and stays upright. It does not topple.

**Fix**

Hit block1 hard enough to yank it out from under the stack.

- Start the heavy sphere already rolling at 4 m/s. That means ω_y = v/r = 40 rad/s, so no energy is lost to slip.
- Block1 then leaves at about 3.5 m/s while the pusher keeps driving it.
- The upper stack can follow at no more than about 5.9 m/s². The relative slip therefore runs far beyond the 0.1 m at which block2's centre of mass loses support.
- Block2 then drops tail-first. The upper stack is already being rotated backward by the friction at its base, so the column falls over.
- The pusher starts 2 m back, so the stack stands untouched for about 0.5 s before the hit.

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
    <body name="pusher" pos="-2.2 0 0.1">
      <freejoint/>
      <geom name="pusher" type="sphere" size="0.1" mass="4.0" friction="0.3 0.005 0.0001"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0 0 0.100 1 0 0 0  0 0 0.300 1 0 0 0  0 0 0.500 1 0 0 0  0 0 0.700 1 0 0 0  0 0 0.900 1 0 0 0  -2.2 0 0.1 1 0 0 0" qvel="0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  4 0 0 0 40 0"/>
  </keyframe>
</mujoco>
```

```json
{"what_happens": "The 4 kg sphere settles into rolling at only ~1.07 m/s and nudges block1 to ~0.95 m/s. Friction from the floor and from block2 lets block1 slip only ~5 cm under the stack before they lock together. The whole column slides ~0.15-0.2 m, rocks slightly and stays standing, well short of the energy needed to tip.", "works": false, "problem": "The push is too gentle: block1 never slides far enough relative to the upper blocks, and the brief friction kick is too small to tip the column, so the stack shifts but does not topple."}
```

---
thinking (summarized):

I'm working through the physics of a sphere sliding before it transitions to rolling: with mass 4 kg, friction 0.3, and initial velocity 1.5 m/s, friction will spin it up until it reaches the rolling condition at 5/7 of the initial speed, about 1.07 m/s, so I need to calculate the time this transition takes.

Once rolling, since MuJoCo's default contact dimension doesn't activate rolling resistance, the sphere coasts freely toward the block stack, covering roughly a 1-meter gap and arriving around the 1-second mark. I'm now figuring out the collision dynamics when the sphere strikes the bottom block of the stack — considering momentum transfer, the coupling friction between stacked blocks, and whether the impact would eject the bottom block from under the stack or cause the whole stack to slide or topple.

I'm estimating block1 decelerates around 5 m/s² against the combined pusher mass, stopping within roughly 0.2 s after about 0.1 m of travel, while the stack above keeps accelerating and sliding relative to it. The friction force acting at the base of the four-block stack also generates a torque about its center of mass, which could cause the stack to tip backward around its rear bottom edge—so I need to check the tipping condition.

Comparing the critical tipping acceleration (around 2.45 m/s² based on the stack's COM height-to-width ratio) against the friction-limited acceleration of about 5.9 m/s², it looks like tipping is likely. As block1 slides forward relative to block2, block2 loses support at its rear edge, which could cause it to tilt backward, and this instability could propagate up through the individual block interfaces in the stack above.

Even without tipping, I wonder if block1 could just slide off entirely—it needs about 0.2m of travel for block2 to lose support. Estimating the post-impact dynamics: with fairly inelastic contact, the sphere and block1 settle to a common velocity around 0.95 m/s, then friction forces from the floor start decelerating block1 from there.

Once they reach common velocity near 0.55 m/s, the upper stack tends to keep coasting while block1 decelerates under floor friction, but since the pusher isn't attached and keeps rolling forward, it continues pushing the stack along, so I estimate the combined deceleration stays below the stack's friction limit, meaning everything stays stuck together for the remaining travel of roughly 0.1-0.18 m total.

Now I'm checking whether the upper stack tips during that initial 0.09 s acceleration phase — modeling it as a rigid 2 kg block with a 0.2×0.8 footprint, pivoting about its rear bottom edge, and comparing the destabilizing pseudo-force torque from the acceleration against the restoring torque from gravity to see if it stays upright.

That comes out to 0.195 J needed versus only 0.068 J available, so it doesn't tip over. I'm now considering what happens afterward when the whole system decelerates to a stop — that deceleration is below the tipping threshold, but since this isn't a rigid body, I need to check whether individual blocks in the stack could rock or tip relative to each other, particularly the topmost ones.

For a single top block, the tipping threshold is a/g > 1, which is far higher than what's generated, so the stack of four acting together is actually the easiest configuration to tip. I'm also checking whether the friction between block2 and block3 is enough to transmit the needed force without slipping — it comes out marginal, right at the friction limit. I also want to consider whether the impact itself, hitting at block1's center height, could create a tipping torque from the floor friction at the base.

I'm realizing that at 1.07 m/s the impact is actually pretty gentle — the kinetic energy is low, so the stack probably just slides forward a bit without toppling, which doesn't satisfy what I need. I should strengthen the push, perhaps making the pusher faster or more impulsive so block1 gets knocked out from under the rest, giving the stack more rotational momentum rather than just translating.

I'm considering boosting the pusher's speed substantially, maybe around 4-5 m/s, and possibly adjusting friction or adding rolling motion so energy transfers more effectively into knocking block1 out rather than slipping.

Running the numbers, with upper friction deceleration around 5.9 m/s², I need the block1-plus-pusher velocity high enough that relative displacement clears the gap before velocities match—something like 2.5 m/s should yank block1 out by roughly half a meter, enough for the stack above to fall while also tipping backward over time.

Once block1 clears, the support contact for block2 shifts toward its front edge as block1 slides forward underneath, which means block2's center of mass can end up unsupported relative to the remaining contact patch, driving it to tip rather than just drop cleanly.

Given friction forces and timing, the stack should topple backward toward the pusher rather than settle flat, so I'll lock in a pusher velocity around 3-4 m/s rolling without slipping, and set up the collision as roughly 4 kg impacting the stack at that speed.

Toppling torques from forward force at COM and backward friction at the base roughly balance out, so block1 should stay fairly stable. With a 1.0 m gap and 4 m/s approach, impact happens around 0.25 s in, which is a brief standing period but acceptable—maybe I'll just start the pusher farther back, around -2, to give more lead-in time.

Moving pusher start to -2 pushes impact to roughly 0.5 s, floor size of 6 is still fine since MuJoCo's ground plane collision is effectively infinite regardless of rendered size. After the hit, block1 gets flung forward at ~3.6 m/s and decelerates around 5.9 m/s² from friction while the pusher keeps driving into it, which all seems reasonable—now I just need to finalize the file with correct quaternion and qvel values for the pusher's freejoint.

