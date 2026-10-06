MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.50, 0.00, 0.04) m, moving 2.50 m/s (vx +2.50, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2; starts at (0.80, 0.00, 0.04) m, at rest
- ball3: free body; its geoms: ball3; starts at (1.10, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching floor
 0.00 s  ball2 starts touching floor
 0.00 s  ball3 starts touching floor
 0.09 s  ball1 leaves floor
 0.09 s  ball1 first touches ball2
 0.09 s  ball2 starts moving
 0.15 s  ball1 leaves ball2
 0.21 s  ball1 is at the top of its flight, at (0.81, 0.00, 0.10) m
 0.32 s  ball1 touches floor again
 0.39 s  ball2 leaves floor
 0.39 s  ball2 first touches ball3
 0.39 s  ball3 starts moving
 0.44 s  ball2 leaves ball3
 0.45 s  ball2 touches floor again
 0.53 s  ball1 touches ball2 again
 0.54 s  ball1 passes 0.10 m from ball3 without touching it: nearest points (0.99, 0.00, 0.04) m and (1.09, 0.00, 0.04) m
 0.55 s  ball1 comes to rest at (0.95, 0.00, 0.04) m
 0.58 s  ball1 leaves ball2
 0.91 s  ball2 comes to rest at (1.05, 0.00, 0.04) m
 1.67 s  ball3 comes to rest at (1.25, 0.00, 0.04) m

State every 0.25 s:
0.00 s: ball1 at (0.50, 0.00, 0.04) m, moving 2.50 m/s (vx +2.50, vy +0.00, vz +0.00); touching floor | ball2 at (0.80, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.10, 0.00, 0.04) m, at rest; touching floor
0.25 s: ball1 at (0.83, 0.00, 0.09) m, moving 0.66 m/s (vx +0.54, vy -0.00, vz -0.38); touching nothing | ball2 at (0.92, 0.00, 0.04) m, moving 0.74 m/s (vx +0.74, vy +0.00, vz -0.01); touching floor | ball3 at (1.10, 0.00, 0.04) m, at rest; touching floor
0.50 s: ball1 at (0.94, 0.00, 0.04) m, moving 0.37 m/s (vx +0.37, vy +0.00, vz -0.00); touching floor | ball2 at (1.03, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.12, 0.00, 0.04) m, moving 0.19 m/s (vx +0.19, vy -0.00, vz -0.00); touching floor
0.75 s: ball1 at (0.95, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.04, 0.00, 0.04) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz -0.00); touching floor | ball3 at (1.16, 0.00, 0.04) m, moving 0.15 m/s (vx +0.15, vy -0.00, vz -0.00); touching floor
1.00 s: ball1 at (0.95, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.06, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.19, 0.00, 0.04) m, moving 0.11 m/s (vx +0.11, vy -0.00, vz -0.00); touching floor
1.25 s: ball1 at (0.95, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.07, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.22, 0.00, 0.04) m, moving 0.09 m/s (vx +0.09, vy +0.00, vz -0.00); touching floor
1.50 s: ball1 at (0.95, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.07, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.24, 0.00, 0.04) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor
1.75 s: ball1 at (0.95, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.08, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.25, 0.00, 0.04) m, at rest; touching floor
2.00 s: ball1 at (0.95, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.08, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.26, 0.00, 0.04) m, at rest; touching floor
2.25 s: ball1 at (0.95, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.08, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.27, 0.00, 0.04) m, at rest; touching floor
(the same through 2.75 s)
3.00 s: ball1 at (0.95, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.08, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.28, 0.00, 0.04) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (0.95, 0.00, 0.04) m, at rest; touching floor
- ball2 at (1.08, 0.00, 0.04) m, at rest; touching floor
- ball3 at (1.28, 0.00, 0.04) m, at rest; touching floor
</history>
