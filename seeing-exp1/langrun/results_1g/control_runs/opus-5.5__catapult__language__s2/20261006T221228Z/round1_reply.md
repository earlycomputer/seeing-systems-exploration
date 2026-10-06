**What happens in the run:** the spring swings the arm up to its 40° stop in 0.15 s. The arm overshoots to 43° and settles back at 40°. The ball leaves at about 4.15 m/s, but at only about 32° elevation rather than the 43° I planned; I'm not sure why the launch came out lower and flatter. It peaks at 1.07 m. It lands on the floor at x ≈ 1.85 m, short of the bucket, glances off the bucket's near wall and comes to rest on the floor at x = 1.93 m, outside the bucket.

**Fix:** I took the measured launch as given, assuming the 32° elevation stays the same and the ball's speed scales with the arm's speed.

- For the ball to drop past the wall tops at about x = 2.36 m, the horizontal speed must rise from 3.53 to about 4.07 m/s. That needs about 33% more kinetic energy, so the spring stiffness goes from 5.3 to 6.5 N·m/rad.
- I widened the bucket to 80 cm for margin. Its centre stays 3 m from the ball's start.

```world
world  catapult into a bucket

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

catapult
  is a          catapult
  pivot height  40 cm
  arm length    60 cm
  arm mass      400 g
  swings        from 0° to 40°
  spring        6.5 N·m/rad toward 90°
  damping       0.01 N·m·s/rad
  armature      0.002 kg·m²
  colour        wood

ball
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  on catapult.scoop base, at catapult.scoop base's near end

bucket
  is an     open box
  length    80 cm
  width     80 cm
  walls     30 cm
  bounce    dead
  friction  1.0, spinning 0.02, rolling 0.01
  colour    grey
  its base 3 m beyond ball

expect
  ball comes to rest in bucket
```

```json
{"what_happens": "The spring swings the catapult arm to its 40° stop in 0.15 s. The ball is released at about 4.15 m/s and roughly 32° elevation and peaks at 1.07 m. It lands on the floor at about x = 1.85 m, short of the bucket, glances off the bucket's near wall and comes to rest on the floor at x = 1.93 m, outside the bucket.", "works": false, "problem": "The launch is too weak and too flat, so the ball falls about half a metre short and stops on the floor in front of the bucket."}
```

---
thinking (summarized):

The ball fell short, landing at x=1.93, outside the bucket at 0.83s. Checking the release conditions, I calculate vx of 3.53 and vz near release around 2.19, giving a speed of about 4.15 m/s at roughly 31 degrees.

But the expected speed was 4.80 m/s at 42.9°, and the arm's angular velocity of 8.34 rad/s matches my estimate closely, which makes this discrepancy puzzling. I'm wondering if the ball separated from the scoop earlier than assumed—perhaps when the arm's tangential acceleration drops below gravity's effect on the ball, or if the ball rolled or slid within the scoop rather than staying rigidly fixed to it. I'm trying to reconcile the elevation angle with the arm angle at release, and considering whether the ball pressing against the back wall as the arm decelerates could explain the lower, flatter trajectory.

Given the uncertainty in the physical mechanism, I'm deciding to just empirically tune the parameters instead. With the current setup, release happens at t=0.15s with position (-0.38, 0.81) and velocity (3.53, 2.19), reaching apex at t=0.37s near (0.40, 1.07), and landing around x=1.75-1.85 at t=0.83s—but I need the ball to land near x=2.42 at the floor height of 0.30. I'm considering raising the stop angle to push the elevation closer to 45°, testing whether a stop angle of 50° gets me closer to the target trajectory.

I'm computing the contact point velocity on the ball's surface where it touches the back wall, using the spin vector crossed with the offset vector, and getting roughly (0.21, 0.25) m/s — matching the wall's own velocity since it's rolling with the frame. So when the wall suddenly stops, the ball's surface at that contact point is still moving at that velocity relative to the now-stationary wall, which means friction would kick in at that instant.

Friction at that moment would pull the ball backward opposite to its tangential motion, sapping some of its speed — same thing likely happens at the base contact, which could explain the observed speed loss. I'm also wondering if reducing the catapult's friction coefficient (say to 0.05) would help, since during the launch the ball is mostly held by normal forces rather than needing friction, so lower friction might reduce unwanted spin loss, though it also risks letting the ball slip unpredictably.

Instead, it seems more reliable to just retune the spring stiffness empirically while keeping the geometry fixed, assuming the elevation angle stays around 32° and speed scales with angular velocity. I'm checking the release point against the trajectory data — position and velocity at various time steps — to verify the elevation angle holds near 32°, then calculating the horizontal and vertical distances needed to reach the target point and matching that against the tangent of the launch angle.

Solving for the required exit speed, I get vx² ≈ 17.05, so vx ≈ 4.13, compared to the current 3.53 — a ratio of about 1.17. That translates to an angular velocity ratio of 1.17 and a kinetic energy ratio of 1.369, so I'm computing the current arm kinetic energy at 8.34 rad/s (~3.17 J) versus the needed 4.34 J, an increase of 1.17 J. Working through the spring's energy equation, current work comes out to 4.52 J and the new target to 5.69 J, giving a new stiffness k≈6.67 — assuming ball speed scales linearly with losses proportional to speed, though I need to double check whether the elevation angle shifts slightly due to friction effects at higher spin speeds.

I'm now verifying the trajectory with vx=4.13 and vz=2.56 against the wall geometry — checking clearance at the near wall's inner edge (around x=2.10m) to make sure the ball clears the 30-34cm height window at that point in its path.

Recomputing with a shorter target distance, I get vx around 4.07, giving a kinetic energy ratio that suggests k≈6.5. Checking the landing point against the base coefficient, x comes out to about 2.59, and the near-wall height check at 2.10m clears at z=0.54, so k=6 should work.

Let me also consider widening the bucket to 80 cm for extra margin, keeping its center at 3m with walls at 2.04 and 2.84. Checking clearance at the near wall (2.04m) gives z=0.59, which still clears comfortably — so I'll go with the 80 cm bucket.

