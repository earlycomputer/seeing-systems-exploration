**What happens when it runs**

1. **Release.** The keyframe holds the pendulum at 1.403 rad from vertical, which puts the bob 0.5 m above its lowest point. It swings down and reaches ball1 at the bottom of the arc at about 3.1 m/s. At that moment the two centres are level and 0.05 m apart, so the push is horizontal.
2. **The chain of impacts.** Balls touch each other, and the bob touches ball1, only through explicit frictionless contact pairs.
   - These pairs use a spring of about 250 rad/s with almost no damping. Each impact lasts about 6 timesteps and should be nearly elastic.
   - Each struck ball should take nearly all of the incoming speed, and the striker should be left with roughly 0.1–0.15 m/s.
   - So ball1 hits ball2, ball2 hits ball3, and ball3 hits ball4, each after sliding across the 0.1 m gap.
3. **Sliding, not rolling.** On the rail, the rolling-friction limit (0.01·N) is larger than the torque sliding friction can apply (0.1·N·r). So the balls should slide without picking up spin, and no spin can carry a striker forward after an impact.
4. **Leftover motion dies out.** The slow leftover motion of balls 1–3 should be stopped by rail friction within a few centimetres, well before the rail end at x = 0.60. The bob is left swinging gently, only about 4 cm either way, and cannot hit the rail.
5. **Ball4 into the box.** Ball4 should leave the rail end at about 2.5–2.9 m/s.
   - The rail ends directly over the box's near wall, so it falls straight into the pit.
   - It then hits the thick, tall far wall in mid-air. That contact is stiff and critically damped, so it should lose its horizontal speed rather than bounce back.
   - It should drop to the high-friction floor, which also has rolling resistance, and stop well within the remaining ~5 s.

I can't run it, so the restitution figures above are estimates from the contact settings.

```json
{"what_happens": "The pendulum bob falls 0.5 m and hits ball1 at ~3.1 m/s at the bottom of its swing. Nearly elastic, frictionless contact pairs should pass the speed through ball2 and ball3 to ball4, while each striker keeps only a small leftover speed. Rail friction should stop balls 1-3 on the rail, and the bob is left swinging gently. Ball4 should slide off the rail end at ~2.7 m/s, fall into the sunken box, hit the far wall and stop, then come to rest on the box floor long before 6 s.", "works": true, "problem": ""}
```

---
thinking (summarized):

I'm double-checking the collision filtering logic in the second file: confirming the ball-rail pair collides correctly while ball-ball collisions are excluded by default, relying on explicit pairs instead.

The negative solref values for the pair constraint need both components negative to work correctly—checking that's satisfied here. I'm working through the friction mixing rule (taking the max across sliding, torsional, and rolling components) and estimating the effective contact stiffness and penetration depth at impact using the solver's reference acceleration formula. Then I move to checking the bob-ball contact geometry at the pendulum's lowest point.

After collisions, ball4 exits around 2.6-2.9 m/s, crossing the plank edge at x=0.60 where it tips off and becomes a projectile. Tracking its fall toward the far wall at x=1.12, I estimate it travels about 0.177 s and drops roughly 0.153 m, landing at a height that puts it just above the floor top, so it likely strikes the far wall rather than the floor.

Once it hits the wall, the critically damped contact stops its horizontal motion, then it falls and friction against the wall spins it before it lands near the far wall and settles through rolling friction. Meanwhile ball3's leftover velocity after its collision with ball4 should be small enough (around 0.15 m/s with restitution near 0.9) that it stops within a few centimeters, so I'm checking the damping ratio and default solver impedance parameters to confirm this behavior holds.

The bob's residual swing is gentle enough that its forward amplitude lands well short of where ball1 settled after striking ball2, so there's no secondary collision to worry about there.

Checking other details: rail lips are positioned above ball contact height so they don't interfere, floor isn't close to any balls, and ball4 should settle to rest against the far wall as rolling friction brings its velocity below threshold within a few seconds. Collision pairs only get evaluated when balls are within proximity margins, which keeps things efficient, and the pendulum rod's hinge and mass properties look consistent with the capsule geometry.

Verifying the keyframe qpos length comes out to 29 values, matching one free body plus four quaternion-positioned balls. The pendulum stand's pivot axle is set to contype 0 so it won't collide during the swing, and ball-ball contacts use condim 1 for frictionless interactions. I'm double-checking that the rolling friction coefficient on a sliding ball still behaves correctly, since MuJoCo's rolling friction constraints act on angular velocity about horizontal axes rather than directly opposing sliding motion.

Comparing torque limits: sliding friction only produces about 0.0025·N of torque at the ball's radius, well below the 0.01·N rolling friction limit, so rolling friction fully suppresses spin and the ball just slides without rotating—actually a cleaner outcome. Deceleration then comes purely from sliding friction at roughly 0.98 m/s², meaning a residual 0.15 m/s ball stops within about 0.011 m, and a 0.4 m/s ball within about 0.08 m, both reasonable distances.

With that confirmed, I check ball4 at ~2.7 m/s over 0.15 m, losing little speed, and verify ball1 stays within the 0.15 spacing. Everything holds together, so the answer is true.

