**What happens.** The arm swings up to its stop and throws the ball high, peaking around z ≈ 1.3–1.4 m near x ≈ 0–0.6 m. The ball comes down at the near side of the bucket rather than inside it. It ends up back on the floor outside the bucket. A line of copies runs along the floor between the catapult base and the bucket's near wall, and the last copy rests outside the bucket. The bucket centre is now correctly 3 m from the ball's start.

I can't fully resolve the descent at this resolution. The most consistent reading is that the ball clips the top of the near wall and bounces back out, then rolls along the floor.

**Why.** If the ball just clips the near rim (x ≈ 1.68 m, z ≈ 0.46 m), the launch speed was about 3.85 m/s. I had predicted about 4.0 m/s, so about 0.2 J more is lost than I estimated. The 35° launch angle also brings the ball in shallow, so even a small shortfall catches the rim.

**Fix.** Raise the hinge stiffness from 2.5 to 2.65, which gives a launch of about 4.1 m/s.
- At the near wall the ball would then be about 0.3 m above the rim.
- It would come down on the bucket floor at about x ≈ 2.15 m.
- The ball's centre can land anywhere from 1.75 to 2.41 m and still be inside, so this leaves some margin either way.

```json
{"what_happens": "The arm swings up to its stop and throws the ball in a high arc, but the ball comes down at the bucket's near rim, probably clipping it and bouncing back, and ends up rolling on the floor outside the bucket between the catapult and the near wall.", "works": false, "problem": "The throw is slightly too weak for the shallow 35° launch, so the ball reaches the near rim of the bucket instead of dropping inside it."}
```

```xml
<mujoco model="catapult_fixture">
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="8 8 0.1"/>
    <geom name="catapult_base" type="box" pos="0 0 0.170" size="0.08 0.12 0.170"/>
    <body name="catapult_arm" pos="0 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 55" stiffness="2.65" springref="150" damping="0.05" armature="0.01"/>
      <geom name="catapult_beam" type="box" pos="-0.500 0 0" size="0.500 0.03 0.02" mass="0.3"/>
      <geom name="catapult_cup_floor" type="box" pos="-0.920 0 0.025" size="0.08 0.08 0.005" mass="0.02"/>
      <geom name="catapult_cup_back" type="box" pos="-1.005 0 0.07" size="0.005 0.08 0.05" mass="0.01"/>
    </body>
    <body name="ball" pos="-0.920 0 0.4895">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.06" mass="0.15" condim="6" friction="0.8 0.01 0.004" solref="0.01 1"/>
    </body>
    <body name="bucket" pos="2.08 0 0">
      <geom name="bucket_base" type="box" pos="0 0 0.01" size="0.4 0.4 0.01"/>
      <geom name="bucket_near" type="box" pos="-0.4 0 0.2" size="0.01 0.4 0.2"/>
      <geom name="bucket_far" type="box" pos="0.4 0 0.2" size="0.01 0.4 0.2"/>
      <geom name="bucket_left" type="box" pos="0 0.4 0.2" size="0.4 0.01 0.2"/>
      <geom name="bucket_right" type="box" pos="0 -0.4 0.2" size="0.4 0.01 0.2"/>
    </body>
  </worldbody>
</mujoco>
```

---
thinking (summarized):

I'm tracing the ball's trajectory through the dot pattern, checking where the arc crosses row 47 near column 40-88 to figure out its landing position relative to the bucket wall.

Trying different velocity estimates doesn't match cleanly - the top arc near (45,13) and (60,15) suggests a much slower horizontal speed than what would carry it to that bucket, so maybe the launch angle or release point is different than I assumed. It's possible those top dots are actually residue from the cup/arm rather than the ball itself, which would explain the discrepancy.

Short range would mean the ball hits the near wall early rather than flying far — so maybe it isn't leaving the cup cleanly. I'm checking whether the back wall correctly provides centripetal force toward the hinge, and considering the net tangential acceleration from torque versus gravity during the swing.

I'm also wondering if MuJoCo's degree-to-radian conversion applies to springref the same way it does for range and ref, and whether a joint limit might be clipping the arm's motion before the ball actually leaves the cup.

Tracing the trajectory points by hand, the ball's path seems to arc toward the bucket as expected — but my pixel-level reading of the rendered dots is rough, so I can't be fully confident the landing matches without checking the image more carefully.

The darkest trailing dots near the bucket wall suggest the ball ended up resting against it, so maybe the throw was weaker than I thought and it landed short before rolling to the wall. The spacing between copies (~15px at 0.15s intervals) implies a velocity around 3.3, but I'm not seeing the descending arc clearly, so I'm unsure if these dots are truly sequential frames of the same flight.

Another possibility is the ball fell back near the catapult base itself and rolled from there — at roughly 1.1 m/s it could cover the needed 1.6m distance in about 1.5 seconds, which would fit. It could also be a shallow-angle landing with bounces before settling into a roll, with friction gradually slowing it down — perhaps caused by the arm overshooting its intended release point.

I'm trying to map out where successive ball copies should land given the 0.15s interval and horizontal speed, checking if columns at 75, 90, and 105 px align with the expected descending heights — maybe the ball actually bounces partway through instead of flying straight to the floor.

The floor-row dots could represent the ball rolling after landing, but comparing with the earlier k=2.0 image suggests the stiffness change barely altered the trajectory, meaning something else must be driving the dynamics.

I'm wondering if the real issue is the ball's resting position in the cup—maybe its center height relative to the arm setup isn't quite what I'm assuming.

Checking the collision geometry: the cup floor and ball bottom positions seem to have slight overlap but nothing alarming, and the arm's parent-child filtering should exclude unwanted contacts between the arm and base. The ball shouldn't be interacting with the arm after release since the cup floor was the last thing pushing it.

Tracing the trajectory: the ball likely arcs from roughly x=1.1,z=1.0 to x=1.6,z=0.5, landing near the wall whose top edge sits around x=1.68, z=0.4 — close enough that the ball could clip the wall top and bounce backward, rolling left across the floor before settling, which would explain the trail of position copies.

That matches the dot row starting right next to the catapult base and running to the bucket wall in both images — the ball keeps clipping the near rim and bouncing back instead of dropping in. My current range estimate lands around 1.68 against a target near 2.08, so I'm roughly 2.13 m short of center; I probably need to boost launch stiffness by something like 10% to close that gap.

I'm recalibrating the energy loss factor from the actual trajectory data, finding losses around 2.8 J instead of the idealized model, and using that to back-solve for the kinetic energy actually needed to land the ball at the target floor position.

To account for bucket margins, I'm computing the allowed landing range given the ball radius and bucket width, then re-deriving the trajectory equation relating launch speed to landing position so I can check sensitivity near v²=14.86.

Actually at that speed it lands at x≈1.93, well inside, but the trajectory still clips the rim's edge earlier at x=1.68, which is a problem since that's marginal at a 35° launch angle. I think a steeper angle, closer to 45°, would clear the rim more safely.

Let me try increasing the velocity so the ball lands near the center with better clearance, then recheck the rim height at x=1.68 to confirm it clears comfortably this time.

For the far wall, since the ball lands before reaching it, that's fine, and I still need to confirm the bounce stays controlled given the vertical landing speed and rolling velocity toward the far wall.

Since the ball's radius keeps it below the rim, it should just bounce back rather than escape. I'll settle on k=2.65 and note the uncertainty honestly in the description.

