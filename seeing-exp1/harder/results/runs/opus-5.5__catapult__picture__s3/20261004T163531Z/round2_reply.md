**What the second run shows**

The ball still does not reach the bucket. It rises on a short, steep arc near the catapult, to about z ≈ 1.4 m around x ≈ −0.4. It comes down at about x ≈ 0 and rolls slowly along the floor. It stops against the outside of the bucket's near wall at about x ≈ 1.4–1.5.

**Why my first fix was wrong**

My spring-energy estimate predicted a landing near x ≈ 2.2. The ball instead leaves almost straight up, much too early, and the result looks nearly the same as the first run even though I changed the stiffness.

That pattern fits a spring torque that is far larger than intended. If `springref="150"` is taken as 150 rad rather than 150°, the torque is about 390 N·m. The arm then slams to its stop in a few hundredths of a second. The cup only partly pushes the ball through the soft contact before it is gone. This is my diagnosis from the picture; I have not confirmed it in MuJoCo's source.

**The fix**

I now give every angle in radians, with `<compiler angle="radian"/>`, so nothing depends on degree conversion:

| Setting | Value |
|---|---|
| Joint range | 0 to 0.9599 rad (55°) |
| `springref` | 2.618 rad (150°) |
| Stiffness | 2.6 N·m/rad |
| Bucket position | x = 2.08 |

With these values I expect a release at about 4.2 m/s, about 29° above horizontal, from (−0.45, 1.2). The ball should clear the near rim with margin and land on the bucket floor near x ≈ 2.2. The bucket centre stays 3 m from the ball's start.

```json
{"what_happens": "The arm snaps up and the ball pops out early on a short, steep arc near the catapult (apex about 1.4 m). It lands around x≈0 and rolls along the floor to rest outside the bucket's near wall, never entering the bucket.", "works": false, "problem": "The spring rest angle seems to be read as 150 radians rather than 150 degrees, so a huge spring torque slams the arm up and the ball is released early and weakly instead of on the designed 4.2 m/s arc."}
```

```xml
<mujoco model="catapult_fixture">
  <compiler angle="radian"/>
  <option timestep="0.002"/>
  <worldbody>
    <geom name="floor" type="plane" size="8 8 0.1"/>
    <geom name="catapult_base" type="box" pos="0 0 0.170" size="0.08 0.12 0.170"/>
    <body name="catapult_arm" pos="0 0 0.4">
      <joint name="catapult_hinge" type="hinge" axis="0 1 0" range="0 0.9599" stiffness="2.6" springref="2.618" damping="0.05" armature="0.01"/>
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

I'm trying to work out the pixel-to-meter scale in the image, checking where the ball sits along the floor row and mapping that against the bucket position to estimate the height axis calibration.

Now I'm tracing the dots to figure out the ball's trajectory — there's a cluster at mid-height that could be the flight arc, and another band along the floor that looks like the ball rolling slowly toward the bucket afterward, maybe around 1 m/s based on the spacing between frames. This seems to contradict my earlier estimate of the arm speed, so I think the ball travels a shorter distance before landing and then rolls the rest of the way, possibly stopping near a wall close to the bucket.

I'm wondering if I mishandled springref — if it's actually in radians rather than degrees, the torque would spike enormously, causing the arm to snap upward almost instantly. With such a huge angular acceleration, the arm would reach its target angle in a fraction of a second with a very high angular velocity, which changes everything about how the ball gets launched.

Maybe what I'm seeing as scattered dots near the top-left isn't the ball's trajectory at all but residual copies of the arm/cup overlapping as it moves. Trying to trace an actual parabolic path for the ball among these points, I keep getting inconsistent landing positions compared to my calculated launch velocity, so I'm reconsidering which dots actually belong to the ball.

Reconsidering the arc, maybe it's the arm's swing path rather than the ball's flight—only a couple copies during the brief 0.2s motion. Tracing from the launch point down to the next dot suggests a fairly steep descent, implying a slow horizontal speed of roughly 1.3 m/s during the fall, before the ball transitions to rolling.

That gives a near-vertical launch velocity around (1.3, 2.2), implying a 60° angle rather than the expected 55°—so maybe the ball releases later than I assumed, possibly riding up the cup's back wall under centrifugal force before separating from the arm.

I check the torque balance at 25° with spring dominating gravity, which still gives positive acceleration — so that doesn't explain separation either. I wonder if springref isn't actually converted to radians, which would produce a wildly oversized torque and unrealistic launch speeds, so I'm reconsidering whether the compiler's degree-to-radian conversion even applies to springref in MuJoCo's joint handling.

Looking back at the arc shapes across both runs, they look nearly identical despite the stiffness change, which makes me suspect the dots I'm seeing are just copies of the arm/cup at different swing positions rather than something driven by the new parameter.

Checking the cup geometry, the ball sits against the floor with a small gap to the back wall, and during rotation without enough centripetal force it would slide outward but still be contained by that wall since the contact point falls below the wall's upper edge — so the ball should stay put mechanically.

Looking at the bucket region, I notice dots clustered near row 47 spanning a wide horizontal range, which doesn't fit a parabolic flight path—a trajectory landing further out would pass through a much higher point at that x-range, not a flat line. That horizontal arrangement seems inconsistent with projectile motion, so it's probably something else like the static arm rather than the ball's predicted path.

Actually, maybe those dots represent the ball rolling after falling short of the target, which both runs seem to show. I'm now wondering if there's a systematic error causing undershoot—perhaps the launch force is much weaker than intended, or there's an issue with how springref is being interpreted as degrees versus radians, which could cause the arm to swing with very different torque and timing than expected, potentially leaving the ball behind during the short launch window.

I'm trying to recall whether MuJoCo's compiler converts springref to radians alongside ref when the degree setting is active, but I'm not fully certain of the exact conversion logic across versions. To stay safe regardless of the answer, I should design the fix to work either way.

Instead, maybe the cleanest solution is to skip modifying springref entirely and instead give the arm an initial velocity through a keyframe, letting the scene itself drive the motion rather than worrying about spring reference units. I'm now working through what happens physically if the arm's hinge has angular velocity and the cup suddenly contacts the resting ball — checking whether the impulse transfer through the contact over a short timestep would slow the arm down given the relative inertias of the arm versus the ball.

Setting consistent initial velocities for both arm and ball (so the ball starts with the tangential velocity matching the arm's rotation) avoids that abrupt impulse. I'm then comparing how gravity decelerates the arm versus the ball along the tangential direction, computing the arm's angular deceleration from gravity torque against the ball's deceleration, to figure out whether the cup slows down faster than the ball would naturally fall — which determines whether the ball stays in contact with the cup or separates early.

Working through it, the cup actually decelerates faster than the ball's free-fall tangential component, which means the ball would separate from the cup prematurely without some corrective force like a spring. So I need to be careful about ambiguity in how springref is interpreted (degrees vs radians), and I'm considering explicitly setting the compiler's angle unit to radians to remove that ambiguity entirely.

But then I second-guess myself — if springref was already correctly converted in an earlier run, my diagnosis might be wrong and the short throw issue lies elsewhere. Comparing the observed ball trajectory (apex position) against what my predicted launch angle and velocity would produce, the numbers don't line up well, which actually supports the idea that the ball is being released early, nearly vertically, due to an overly strong force — consistent with what I saw when I used radians for springref with k=2.0 in the first run.

I'm now thinking through the contact mechanics: with solref timeconst around 0.015s for the ball versus the arm reaching its limit in about 0.03s, the ball could get rapidly accelerated upward by the soft contact penetration before the cup stops at 55°, leaving it still moving mostly upward when released — which fits the observed short, steep trajectory.

I'll keep the setup as is, set the joint range to radians with springref 2.618, and stick with k=2.6.

