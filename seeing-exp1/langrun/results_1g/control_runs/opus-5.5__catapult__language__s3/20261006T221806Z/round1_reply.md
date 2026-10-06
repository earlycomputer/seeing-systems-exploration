**What happened:** the catapult swung up and hit its 45° stop at 449°/s after 0.19 s, close to the planned 8 rad/s. The ball, though, left at only about 3.9 m/s and about 26° above horizontal, not the planned 4.5 m/s at 38°. The likeliest cause is the soft contact with the scoop's back wall springing back as the arm stopped, pushing the ball forward and down. The ball peaked at 1.11 m, landed on the floor around x ≈ 1.9 m, bounced into the outside of the bucket's near wall, and came to rest on the floor at x = 2.01 m. The bucket's centre is at 2.44 m, so the ball fell short and never entered it.

**Fix:** I kept the measured release direction and height, about 26° from (−0.32, 0.96) m. Over the 2.76 m to the bucket centre at 12 cm high, that needs about 4.6 m/s, which is about 1.38 times the kinetic energy of this run. I scaled the spring work to match, allowing for the small losses seen in this run, so the spring goes from 2.355 to 2.98 N·m/rad. I also widened the bucket to 80 cm for margin.

```json
{"what_happens": "The catapult arm swings up and hits its 45° stop at 0.19 s, but the ball leaves at only ~3.9 m/s and ~26°, peaks at 1.11 m, lands on the floor short of the bucket, bounces off the outside of the bucket's near wall and comes to rest on the floor at x = 2.01 m, about 0.4 m short of the bucket centre at 2.44 m.", "works": false, "problem": "The throw is too weak and too flat, so the ball lands short of the bucket instead of in it."}
```

```world
world  catapult into a bucket

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

catapult
  is a          catapult
  pivot height  50 cm
  arm length    60 cm
  arm mass      500 g
  swings        from 0° to 45°
  spring        2.98 N·m/rad toward 180°
  damping       0 N·m·s/rad
  armature      0.01 kg·m²
  colour        wood
  stands        on floor

ball
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on catapult.scoop base, at catapult.scoop base's near end

bucket
  is an     open box
  length    80 cm
  width     80 cm
  walls     25 cm
  bounce    dead
  friction  0.9, spinning 0.01, rolling 0.01
  colour    grey
  stands    on floor, its base 3 m beyond ball

expect
  ball comes to rest in bucket
```

---
thinking (summarized):

Checking the release velocity against the data: back-calculating from vz=1.17 at t=0.25s gives a release speed around 3.91 m/s at roughly 26°, well short of the expected 4.52 m/s at 37.9°, so the throw fell short of target both in speed and angle.

Trying to figure out the discrepancy — the arm's angular velocity at the stop was 7.84 rad/s, close to the predicted 8.0, which should give ball speed of ω·r ≈ 4.42 m/s, not 3.91. I'm wondering if the ball had been pressed against the back wall by centrifugal force during the swing, and when the arm hit the stop, the contact spring released energy in a direction that reduced the forward component — pushing the ball toward the pivot rather than fully along the tangential release direction, which would explain both the lower speed and the lower angle than expected.

Calculating the trajectory empirically: given the apex at (0.29, 1.11) at 0.37s and constant vx of 3.52, I find the ball lands at x=1.87 when z drops to the 0.12m target height, which falls 0.57m short of the 2.44m target. Scaling from the release point, I need roughly 26% more horizontal distance, so I'm considering whether boosting the spring force while keeping the same launch angle and geometry could close that gap.

Working through the trajectory equations, I find the required release speed is about 4.60 m/s versus the current 3.91 m/s, giving a ratio of 1.176 and a kinetic energy ratio of roughly 1.383. Since ball speed should scale with the arm's angular velocity, I'm scaling the arm's kinetic energy at the stop point by that same factor to find the needed adjustment.

Comparing nominal versus effective work accounting for small losses, I get a ratio of about 0.971 between them, which lets me back out the new spring constant needed—landing around 2.98 N·m/rad. I'm now questioning whether the deviation seen earlier is just contact artifacts that scale with force, which would affect whether this correction direction is actually right.

Checking the landing trajectory with the 26° launch angle, I work out the descent angle comes out around 47.6°, and the rim crossing point lands close enough to center to be fine. With bucket margins around ±0.2m there's some uncertainty, so I'm considering widening the bucket to 80-90 cm for safety since the brief doesn't restrict that dimension.

