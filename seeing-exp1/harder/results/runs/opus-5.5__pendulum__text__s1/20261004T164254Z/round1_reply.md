I expect the scene to work, but I haven't run it, so this is a prediction from hand calculations.

**Expected run**
1. The pendulum is released from 45°. Its 0.5 kg bob reaches the bottom of its arc at about 1.7 m/s, where it is touching the ball.
2. The bob drives the ball toward +x. The ball slides for a few tens of milliseconds while friction spins it up. The heavy bob may keep pushing it during that time.
3. The ball then rolls at roughly 1–2 m/s. With the default contact settings there is no rolling resistance, so it keeps that speed across about 0.67 m of floor.
4. It reaches the ramp in front of the cup. The 9° kink at the ramp foot costs it about 1% of its speed. The roughly 2–3 mm step onto the front wall top costs a little more.
5. It climbs the 4 cm rise, which needs a rolling speed of about 0.75 m/s or more. That should happen in under a second.
6. It drops inside the cup and hits the 14 cm back wall. It may bounce a few times between the back and front walls.
7. It cannot escape:
   - The walls are taller than the ball's 3 cm radius, so it can only meet a vertical face.
   - The bounces are soft.
   - Nothing pushes it sideways, so it stays at y = 0.
   - It should settle within about 4 cm of the cup centre at x = 1.
8. The pendulum keeps swinging near the start and never reaches the cup.

**Checks behind this**
- **Swing direction:** a positive hinge angle about +y puts the bob on the −x side, so gravity swings it toward the ball.
- **Bob clearance:** at the bottom the bob clears the floor by 5 mm, and the gap to the ball is about 0.2 mm.
- **Ramp geometry:** the ramp's lower edge sits 1 mm below the floor, and its upper end meets the front wall top at x = 0.92.

**Main risk**
The ball's launch speed is uncertain because the soft contact gives an uncertain restitution, and the bob may push the ball more than once. Even at the low end, the ball should roll at about 1 m/s, which is above the ramp threshold.

```json
{"what_happens": "The pendulum released from 45° swings down and its heavy bob drives the resting ball along +x. The ball rolls at roughly 1-2 m/s across the floor, climbs a shallow 4 cm ramp over the cup's low front lip and drops into the cup centred at x = 1 m. Its tall back and side walls trap it, and it settles inside while the pendulum keeps swinging near the start.", "works": true, "problem": ""}
```

---
thinking (summarized):

I'm double-checking the hinge rotation math, confirming that a positive angle swings the pendulum bob toward positive x as expected, and now verifying where the ball's contact point sits relative to the bob's center.

Then I check the bob's clearance above the floor, which looks fine. I work through the ramp's rotation about the y-axis to confirm its leading edge tilts upward correctly, and compute the world-space positions of both ends of the ramp's top surface to verify they're buried slightly and reach the right height — both check out.

I also confirm the ramp width fits between the walls. Looking at where the ball transitions from the ramp onto the wall top, I find a small ~2.6mm step at the junction; at speeds of 1 m/s or more the ball should roll over this bump without issue, so I'll leave it as is rather than fixing it.

At the kink where the ramp meets the 9° incline, the ball loses some energy from the impact, but with speeds in the 1.1–2.2 m/s range there's enough margin above the minimum required velocity. I'm also checking whether the ball might slip initially since the contact normal from the bob points slightly downward into the floor.

With sliding friction converting to rolling at 5/7 of the initial velocity since the ball was struck near its center, I'm now wondering if the pendulum could strike the ball a second time — since the ball decelerates quickly from friction (μg≈9.8 m/s²) while the pendulum barely decelerates near the bottom of its swing, the heavy bob could catch up and push the ball again before it finishes its slip phase.

Estimating the slip time at roughly 0.045 s, the bob only travels about 0.07 m in that span and slows gravitationally by a small amount (~1.4 m/s² tangential), so it stays close to the ball's speed and keeps nudging it forward. The ball's final rolling speed ends up somewhat below the bob's speed but still comfortably above the 0.75 threshold I need.

Working through the kink loss at the ramp transition, using conservation of angular momentum about the new contact point for a rolling ball hitting an incline. The ball's speed only drops slightly through the kink, to about 0.991 times its incoming speed, so the loss there is minor.

Checking the climb condition over the wall requires v'² ≥ 10gh/7, which works out comfortably satisfied. Then inside the cup, I verify the ball's center stays within the cup walls, which are taller than the ball's radius, so it can't climb out, and any bounce stays contained given the low restitution. The pendulum afterward just swings freely without hitting anything else on either side.

There's no issue with the ball colliding with the bob at t=0, and the symmetric y-drift confirms everything checks out—so overall this statement is true.

