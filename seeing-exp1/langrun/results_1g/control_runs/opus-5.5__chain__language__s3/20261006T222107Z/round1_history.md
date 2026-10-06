MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (1.00, 0.00, 0.04) m, moving 2.00 m/s (vx +2.00, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2; starts at (1.20, 0.00, 0.04) m, at rest
- ball3: free body; its geoms: ball3; starts at (1.40, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching floor
 0.00 s  ball2 starts touching floor
 0.00 s  ball3 starts touching floor
 0.05 s  ball1 leaves floor
 0.06 s  ball2 leaves floor
 0.06 s  ball1 first touches ball2
 0.06 s  ball2 starts moving
 0.07 s  ball1 leaves ball2
 0.07 s  ball1 passes 0.20 m from ball3 without touching it: nearest points (1.16, 0.00, 0.04) m and (1.36, 0.00, 0.04) m
 0.12 s  ball2 touches floor again
 0.14 s  ball2 leaves floor
 0.15 s  ball2 first touches ball3
 0.15 s  ball3 starts moving
 0.15 s  ball2 leaves ball3
 0.17 s  ball1 touches floor again
 0.19 s  ball2 touches floor again
 0.29 s  ball1 comes to rest at (1.11, 0.00, 0.04) m
 0.89 s  ball2 comes to rest at (1.43, 0.00, 0.04) m
 1.37 s  ball3 comes to rest at (1.73, 0.00, 0.04) m
 6.00 s  ball3 passes 0.02 m from cup (cup_near_wall) without touching it: nearest points (1.77, 0.00, 0.02) m and (1.79, 0.00, 0.01) m
 6.00 s  ball2 passes 0.31 m from cup (cup_near_wall) without touching it: nearest points (1.49, 0.00, 0.04) m and (1.79, 0.00, 0.01) m

State every 0.25 s:
0.00 s: ball1 at (1.00, 0.00, 0.04) m, moving 2.00 m/s (vx +2.00, vy +0.00, vz +0.00); touching floor | ball2 at (1.20, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.40, 0.00, 0.04) m, at rest; touching floor
0.25 s: ball1 at (1.11, 0.00, 0.04) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | ball2 at (1.35, 0.00, 0.04) m, moving 0.26 m/s (vx +0.26, vy +0.00, vz +0.01); touching floor | ball3 at (1.46, 0.00, 0.04) m, moving 0.50 m/s (vx +0.50, vy -0.00, vz -0.00); touching floor
0.50 s: ball1 at (1.12, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.40, 0.00, 0.04) m, moving 0.15 m/s (vx +0.15, vy +0.00, vz -0.00); touching floor | ball3 at (1.57, 0.00, 0.04) m, moving 0.38 m/s (vx +0.38, vy -0.00, vz -0.00); touching floor
0.75 s: ball1 at (1.13, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.42, 0.00, 0.04) m, moving 0.08 m/s (vx +0.08, vy +0.00, vz -0.00); touching floor | ball3 at (1.64, 0.00, 0.04) m, moving 0.25 m/s (vx +0.25, vy -0.00, vz +0.00); touching floor
1.00 s: ball1 at (1.13, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.44, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.69, 0.00, 0.04) m, moving 0.14 m/s (vx +0.14, vy -0.00, vz -0.00); touching floor
1.25 s: ball1 at (1.13, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.44, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.72, 0.00, 0.04) m, moving 0.07 m/s (vx +0.07, vy -0.00, vz -0.00); touching floor
1.50 s: ball1 at (1.13, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.44, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.73, 0.00, 0.04) m, at rest; touching floor
1.75 s: ball1 at (1.13, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.45, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.74, 0.00, 0.04) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (1.13, 0.00, 0.04) m, at rest; touching floor
- ball2 at (1.45, 0.00, 0.04) m, at rest; touching floor
- ball3 at (1.74, 0.00, 0.04) m, at rest; touching floor
</history>
