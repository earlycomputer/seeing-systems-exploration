**What happens in the run.** The stack stands from 0 to 0.92 s. Meanwhile the 4 kg sphere rolls in and slows from 1.50 to 1.07 m/s as it converts to rolling. At 0.92 s it hits block1. The whole stack slides about 5 cm in +x as one column and wobbles by about 3°. By 1.71 s every block is at rest, still stacked, at x ≈ 0.05. The pusher stops against block1 at x ≈ -0.15. Nothing topples.

**Why it fails.** The blocks all have friction 0.6, so block1 carries the four blocks above it along. The sphere has too little energy to do more than nudge the whole column.

**The fix.** I changed it so block1 is pulled out from under the column:

- **Low friction under the column.** Block1 and block2 now have friction 0.05. MuJoCo uses the larger of the two geoms' friction values, so the block1–block2 interface is slippery. Block1–floor stays at 0.6, and so does block2–block3.
- **A ram on a rail.** The pusher is now a frictionless ram on an x slide joint at the height of block1's centre, so its speed at impact is known. It is 1 kg and starts at 2.7 m/s, 1.85 m from the block.
- **How far block1 should slide.** After the hit, the ram and block1 should move off together at about 1.8 m/s and slow at about 10.5 m/s². That comes from about 15.7 N of floor and interface friction acting on 1.5 kg. Block1 should therefore stop about 0.15 m along, while block2–5 stay near x = 0.
- **Why the column then falls.** With block1 moved 0.15 m, the column's support spans x = 0.05 to 0.1. The column's centre of mass is at x = 0, outside that support, so it should tip over toward −x and fall.
- **Not yet checked.** These numbers are my estimates. I have not run the corrected file.

```json
{"what_happens": "The stack stands while a 4 kg sphere rolls in at about 1.07 m/s. At 0.92 s it hits block1, and the whole stack slides about 5 cm as one column, tilts about 3°, and settles back upright by 1.7 s. All five blocks are still stacked and at rest at 6 s; nothing topples.", "works": false, "problem": "High friction between the blocks makes the push slide the whole stack a few centimetres as a unit, so it never loses support and never topples."}
```

```xml
<mujoco model="stack_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="6 6 0.1" friction="0.6 0.005 0.0001"/>
    <body name="block1" pos="0 0 0.100">
      <freejoint/>
      <geom name="block1" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.05 0.005 0.0001"/>
    </body>
    <body name="block2" pos="0 0 0.300">
      <freejoint/>
      <geom name="block2" type="box" size="0.1 0.1 0.1" mass="0.5" friction="0.05 0.005 0.0001"/>
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
    <body name="pusher" pos="-2.0 0 0.1">
      <joint name="pusher_rail" type="slide" axis="1 0 0"/>
      <geom name="pusher" type="sphere" size="0.05" mass="1.0" friction="0.05 0.005 0.0001"/>
    </body>
  </worldbody>
  <keyframe>
    <key name="start" qpos="0 0 0.100 1 0 0 0  0 0 0.300 1 0 0 0  0 0 0.500 1 0 0 0  0 0 0.700 1 0 0 0  0 0 0.900 1 0 0 0  0" qvel="0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  0 0 0 0 0 0  2.7"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

The simulation shows the stack just shifts and wobbles without toppling, so this setup doesn't achieve the goal. I need to rethink the push mechanics—maybe applying force higher up or making the stack less stable—so the block actually tips over instead of sliding as a rigid unit.

Actually a cleaner approach: push block1 partially out so it slides 0.15 m then stops, with low friction between block1 and block2 so the upper blocks stay put. Then their support shrinks so the column's center of mass falls outside the remaining contact area, guaranteeing it tips toward the pusher side and topples.

Since MuJoCo contact friction is the max of two geoms', I'm setting blocks 1 and 2 to low friction so their interface stays slippery, while blocks 3-5 keep normal floor-level friction so the block2-block3 contact remains high and the column stays intact above.

Now I'm estimating block1's deceleration: the floor friction under the whole stack's weight gives roughly 31 m/s² of deceleration, so to slide about 0.15 m I need an initial velocity near 3 m/s, though I still need to check how block2's friction affects things as it also starts moving.

The tricky part is actually imparting that initial 3 m/s to block1 realistically from the pusher collision—if the pusher is heavy it keeps pushing, if masses are equal it's an inelastic collision where both end up at half speed, and friction complicates it further. I'm thinking through alternate pusher setups to get a cleaner initial velocity.

Maybe a sliding pusher box with floor friction would stay in contact with block1 after an inelastic collision, with both decelerating together due to combined friction forces. I'm working out that combined deceleration for a chosen pusher mass to then compute the resulting stopping distance.

I could try giving the pusher zero floor friction and no floor contact using gravcomp so it floats at the right height without needing support, avoiding pre-impact deceleration entirely. Then once it contacts block1, the combined system decelerates together until they stop.

Since the pusher won't touch the floor there's no friction issue there, and contact with block1 happens at center height so no torque gets introduced. I'm weighing whether gravcomp is reliable versus a cleaner alternative: giving the pusher a slide joint along x instead, which avoids gravity concerns entirely since the joint constrains z. I'll name the joint for clarity and need to account for it in the keyframe qpos ordering alongside the free joints.

Once contact happens, the ram and block1 move together since block1 decelerates faster due to friction while the frictionless ram keeps pushing — I'm estimating the combined deceleration force from the normal and friction components, roughly 15-16 N depending on mass values, though this changes as the column on block1 tips. I'm settling on a mass of 1.0 for the ram and working out the starting gap so contact occurs at the right position given the sphere radius.

I'm computing the post-collision velocity using momentum conservation (roughly two-thirds of the pre-collision speed), then working backward from a target displacement of 0.15 m to find how fast the ram needs to be moving and how long it should stand still before being pushed — settling on starting the ram further back, around -2.0, giving about 0.7 seconds of standing time before impact.

Now I'm checking robustness: making sure the column's center of mass ends up outside the overlapping support region after impact, which requires the displacement d to exceed 0.1, while also considering torque effects from friction that might tip block1 and the influence of MuJoCo's soft contact dynamics on the impact spike.

Blocks will still topple either way, and block1 itself might tilt as the column loads its edge, which is fine for the effect. Friction at the block1-block2 interface is small enough not to matter much, so I'll settle on d≈0.16 and v=2.7 as reasonable targets, keeping block dimensions unchanged.

With the ram moving at the same speed as block1, both decelerate together; once the column starts tipping (around d>0.1, taking roughly 0.3s to fall) block1 will have already stopped since its stopping time is much shorter, so the edge loading stays mostly consistent. I'm now setting up the ram as a sphere with mass 1.0, positioning it so it doesn't collide with the floor, and configuring its slide joint and initial position.

Checking friction interactions: block2's lower friction combined with block1's and the floor's higher friction values should resolve correctly via the max rule, so the contacts between block1-floor and block2-block3 remain at 0.6 as intended, and the column blocks sliding against each other during tipping should behave fine too. I'm ready to write up the final answer now.

