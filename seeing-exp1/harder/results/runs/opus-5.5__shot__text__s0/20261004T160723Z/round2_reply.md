**What I expect to happen:** at `start` the ball sits on the floor at the origin with launch velocity (3.077, 0, 8.641) m/s. With `density` left at its default of 0, there is no drag or Magnus force, so the flight is a pure parabola. The checks below are hand calculations from that parabola, not measurements of a run.

1. **Climb and descent.** The ball peaks about 3.9 m high near x ≈ 2.7 m. It comes down through the rim plane at about t = 1.3 s, with its center essentially at the rim center (4, 0, 3.05). That position allows for the ~1.3 cm lag of MuJoCo's semi-implicit integrator. It descends at about 53° below horizontal.
2. **Rim clearance.** Measured perpendicular to the path, the gap from the ball center to the front rim tube and to the back rim tube is each about 0.19 m. Ball radius plus tube radius is 0.127 m, so there is about 6 cm of room on each side. The capsule chords bulge inward only slightly: their inner edge sits at about 0.224 m from the rim center, versus 0.2286 m for a true circle. That does not change the clearance.
3. **Bracket and backboard.** The bracket's front-bottom corner is about 0.18 m from the path, more than the ball radius. The backboard's bottom edge is about 0.21 m from it, and the path only gets steeper and farther away. So the ball passes under the bracket and under the backboard.
4. **After the hoop.** The ball hits the support pole at roughly 1.2 m height, bounces back, and settles on the floor. All of this happens well within the 6 s run.

The initial floor contact is at zero penetration with a separating velocity, so it gives no meaningful impulse.

```json
{"what_happens": "The ball launches from the floor in a clean parabola, peaks about 3.9 m high, and comes down at about 53 degrees through the center of the rim at (4, 0, 3.05) around t = 1.3 s, clearing the rim by about 6 cm on each side. It passes under the backboard, bounces off the support pole and settles on the floor.", "works": true, "problem": ""}
```

---
thinking (summarized):

I'm rechecking the corrected trajectory file, confirming x(t) and z(t) values at t=1.3 match expectations after accounting for integrator lag, getting z≈3.050 which looks correct. Now I'm considering how MuJoCo determines initial floor contact given zero margin.

Since the ball is moving away from the floor during the first step, any separating velocity means no contact force applies, so I can treat this as negligible. I'm also verifying the rim's inner clearance geometry — the vertices sit at radius 0.2366 with inner edges around 0.224, which seems fine, and confirming the ball's trajectory stays clear of the backboard by checking the bottom corner position at x=4.381, computing z there to compare against the backboard height of 2.9.

Now I'm checking the perpendicular distance from the ball's path to the backboard corner using the trajectory's direction vector — the cross product gives roughly 0.215, which is safely more than the ball's radius of 0.119, and since the path curves downward it moves even farther from that corner. I'm now checking the mounting bracket box near x=4.24 to 4.381, z=3.028 to 3.052, starting with the front-bottom corner's relative position.

Then the ball hits the pole and bounces back toward the floor, so this trajectory works — no net is needed for it to "drop through," and since it passes at 1.3 seconds within a 6-second window, the timing checks out too.

