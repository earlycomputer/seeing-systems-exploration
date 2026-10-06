Your expectations, checked against the run (2 of 4 hold):

- holds: ball1 touches ball2 (first touch at 0.21 s)
- holds: ball2 touches ball3 (first touch at 0.72 s)
- DOES NOT HOLD: ball3 touches cup (they never touch)
- DOES NOT HOLD: ball3 comes to rest in cup (ball3 comes to rest at (1.27, -0.00, 0.04) m, outside cup)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.00, 0.00, 0.04) m, moving 2.00 m/s (vx +2.00, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2; starts at (0.50, 0.00, 0.04) m, at rest
- ball3: free body; its geoms: ball3; starts at (1.00, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching floor
 0.00 s  ball2 starts touching floor
 0.00 s  ball3 starts touching floor
 0.21 s  ball1 leaves floor
 0.21 s  ball1 first touches ball2
 0.21 s  ball2 starts moving
 0.22 s  ball1 leaves ball2
 0.29 s  ball1 touches floor again
 0.72 s  ball2 leaves floor
 0.72 s  ball2 first touches ball3
 0.72 s  ball3 starts moving
 0.72 s  ball2 leaves ball3
 0.75 s  ball2 touches floor again
 1.95 s  ball1 touches ball2 again
 1.95 s  ball1 passes 0.23 m from ball3 without touching it: nearest points (0.96, 0.00, 0.04) m and (1.19, 0.00, 0.04) m
 1.95 s  ball1 comes to rest at (0.92, 0.00, 0.04) m
 1.95 s  ball1 leaves ball2
 1.98 s  ball2 comes to rest at (1.00, 0.00, 0.04) m
 2.24 s  ball3 comes to rest at (1.25, 0.00, 0.04) m
 6.00 s  ball3 passes 0.19 m from cup (cup_near_wall) without touching it: nearest points (1.31, 0.00, 0.03) m and (1.50, 0.00, 0.01) m
 6.00 s  ball2 passes 0.43 m from cup (cup_near_wall) without touching it: nearest points (1.07, 0.00, 0.04) m and (1.49, 0.00, 0.01) m

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.04) m, moving 2.00 m/s (vx +2.00, vy +0.00, vz +0.00); touching floor | ball2 at (0.50, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.00, 0.00, 0.04) m, at rest; touching floor
0.25 s: ball1 at (0.44, 0.00, 0.05) m, moving 0.38 m/s (vx +0.38, vy -0.00, vz +0.02); touching nothing | ball2 at (0.54, 0.00, 0.04) m, moving 1.04 m/s (vx +1.04, vy +0.00, vz -0.07); touching floor | ball3 at (1.00, 0.00, 0.04) m, at rest; touching floor
0.50 s: ball1 at (0.55, 0.00, 0.04) m, moving 0.47 m/s (vx +0.47, vy -0.00, vz -0.00); touching floor | ball2 at (0.75, 0.00, 0.04) m, moving 0.81 m/s (vx +0.81, vy +0.00, vz -0.03); touching nothing | ball3 at (1.00, 0.00, 0.04) m, at rest; touching floor
0.75 s: ball1 at (0.66, 0.00, 0.04) m, moving 0.38 m/s (vx +0.38, vy -0.00, vz +0.00); touching floor | ball2 at (0.92, 0.00, 0.04) m, moving 0.13 m/s (vx +0.11, vy +0.00, vz -0.06); touching floor | ball3 at (1.01, 0.00, 0.04) m, moving 0.33 m/s (vx +0.33, vy -0.00, vz -0.00); touching floor
1.00 s: ball1 at (0.75, 0.00, 0.04) m, moving 0.30 m/s (vx +0.30, vy -0.00, vz +0.00); touching floor | ball2 at (0.95, 0.00, 0.04) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz -0.00); touching floor | ball3 at (1.08, 0.00, 0.04) m, moving 0.25 m/s (vx +0.25, vy -0.00, vz +0.00); touching floor
1.25 s: ball1 at (0.81, 0.00, 0.04) m, moving 0.23 m/s (vx +0.23, vy -0.00, vz -0.00); touching floor | ball2 at (0.97, 0.00, 0.04) m, moving 0.07 m/s (vx +0.07, vy +0.00, vz -0.00); touching floor | ball3 at (1.14, 0.00, 0.04) m, moving 0.19 m/s (vx +0.19, vy -0.00, vz -0.00); touching floor
1.50 s: ball1 at (0.86, 0.00, 0.04) m, moving 0.17 m/s (vx +0.17, vy -0.00, vz -0.00); touching floor | ball2 at (0.99, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.18, 0.00, 0.04) m, moving 0.14 m/s (vx +0.14, vy -0.00, vz -0.00); touching floor
1.75 s: ball1 at (0.90, 0.00, 0.04) m, moving 0.13 m/s (vx +0.13, vy -0.00, vz -0.00); touching floor | ball2 at (1.00, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.21, 0.00, 0.04) m, moving 0.10 m/s (vx +0.10, vy -0.00, vz -0.00); touching floor
2.00 s: ball1 at (0.92, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.00, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.23, 0.00, 0.04) m, moving 0.07 m/s (vx +0.07, vy -0.00, vz -0.00); touching floor
2.25 s: ball1 at (0.92, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.01, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.25, 0.00, 0.04) m, at rest; touching floor
2.50 s: ball1 at (0.92, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.02, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.26, 0.00, 0.04) m, at rest; touching floor
(the same through 2.75 s)
3.00 s: ball1 at (0.93, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.02, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.27, 0.00, 0.04) m, at rest; touching floor
3.25 s: ball1 at (0.93, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.03, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.27, 0.00, 0.04) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (0.93, 0.00, 0.04) m, at rest; touching floor
- ball2 at (1.03, 0.00, 0.04) m, at rest; touching floor
- ball3 at (1.27, 0.00, 0.04) m, at rest; touching floor
</history>
