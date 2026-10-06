Your expectations, checked against the run (3 of 3 hold):

- holds: ball1 touches ball2 (first touch at 0.07 s)
- holds: ball2 touches ball3 (first touch at 0.18 s)
- holds: ball3 comes to rest in cup (ball3 at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.00, 0.00, 0.06) m, moving 1.80 m/s (vx +1.80, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2; starts at (0.24, 0.00, 0.06) m, at rest
- ball3: free body; its geoms: ball3; starts at (0.48, 0.00, 0.06) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching floor
 0.00 s  ball2 starts touching floor
 0.00 s  ball3 starts touching floor
 0.06 s  ball1 leaves floor
 0.07 s  ball2 leaves floor
 0.07 s  ball1 first touches ball2
 0.07 s  ball2 starts moving
 0.07 s  ball1 leaves ball2
 0.12 s  ball2 touches floor again
 0.15 s  ball1 touches floor again
 0.17 s  ball2 leaves floor
 0.18 s  ball3 leaves floor
 0.18 s  ball2 first touches ball3
 0.18 s  ball3 starts moving
 0.18 s  ball2 leaves ball3
 0.18 s  ball1 passes 0.22 m from ball3 without touching it: nearest points (0.20, 0.00, 0.06) m and (0.42, 0.00, 0.06) m
 0.21 s  ball3 touches floor again
 0.22 s  ball2 touches floor again
 0.38 s  ball3 leaves floor
 0.38 s  ball3 first touches cup_near_wall
 0.42 s  ball3 first touches cup_base
 0.43 s  ball3 leaves cup_near_wall
 0.52 s  ball2 comes to rest at (0.39, 0.00, 0.06) m
 1.03 s  ball1 comes to rest at (0.27, 0.00, 0.06) m
 1.41 s  ball1 touches ball2 again
 1.41 s  ball1 leaves ball2
 1.58 s  ball3 comes to rest at (0.85, 0.00, 0.06) m
 6.00 s  ball2 passes 0.14 m from cup (cup_near_wall) without touching it: nearest points (0.46, 0.00, 0.04) m and (0.59, 0.00, 0.00) m
 6.00 s  ball1 passes 0.26 m from cup (cup_near_wall) without touching it: nearest points (0.34, 0.00, 0.05) m and (0.59, 0.00, 0.00) m

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.06) m, moving 1.80 m/s (vx +1.80, vy +0.00, vz +0.00); touching floor | ball2 at (0.24, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.48, 0.00, 0.06) m, at rest; touching floor
0.25 s: ball1 at (0.16, 0.00, 0.06) m, moving 0.26 m/s (vx +0.26, vy -0.00, vz -0.00); touching floor | ball2 at (0.37, 0.00, 0.06) m, moving 0.10 m/s (vx +0.10, vy -0.00, vz +0.01); touching floor | ball3 at (0.52, 0.00, 0.06) m, moving 0.49 m/s (vx +0.49, vy +0.00, vz +0.01); touching floor
0.50 s: ball1 at (0.21, 0.00, 0.06) m, moving 0.17 m/s (vx +0.17, vy -0.00, vz +0.00); touching floor | ball2 at (0.38, 0.00, 0.06) m, moving 0.05 m/s (vx +0.05, vy -0.00, vz -0.00); touching floor | ball3 at (0.63, 0.00, 0.06) m, moving 0.39 m/s (vx +0.39, vy +0.00, vz +0.01); touching cup_base
0.75 s: ball1 at (0.25, 0.00, 0.06) m, moving 0.10 m/s (vx +0.10, vy -0.00, vz +0.00); touching floor | ball2 at (0.39, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.72, 0.00, 0.06) m, moving 0.30 m/s (vx +0.30, vy +0.00, vz -0.00); touching cup_base
1.00 s: ball1 at (0.27, 0.00, 0.06) m, moving 0.05 m/s (vx +0.05, vy -0.00, vz -0.00); touching floor | ball2 at (0.40, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.78, 0.00, 0.06) m, moving 0.22 m/s (vx +0.22, vy +0.00, vz -0.00); touching cup_base
1.25 s: ball1 at (0.28, 0.00, 0.06) m, at rest; touching floor | ball2 at (0.40, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.83, 0.00, 0.06) m, moving 0.13 m/s (vx +0.13, vy +0.00, vz +0.00); touching cup_base
1.50 s: ball1 at (0.28, 0.00, 0.06) m, at rest; touching floor | ball2 at (0.40, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.85, 0.00, 0.06) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching cup_base
1.75 s: ball1 at (0.28, 0.00, 0.06) m, at rest; touching floor | ball2 at (0.40, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.86, 0.00, 0.06) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (0.28, 0.00, 0.06) m, at rest; touching floor
- ball2 at (0.40, 0.00, 0.06) m, at rest; touching floor
- ball3 at (0.86, 0.00, 0.06) m, at rest; touching cup_base
</history>
