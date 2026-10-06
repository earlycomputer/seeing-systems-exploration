Your expectations, checked against the run (4 of 4 hold):

- holds: ball1 touches ball2 (first touch at 0.07 s)
- holds: ball2 touches ball3 (first touch at 0.17 s)
- holds: ball3 touches cup (first touch at 0.56 s)
- holds: ball3 comes to rest in cup (ball3 at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.50, 0.00, 0.04) m, moving 3.50 m/s (vx +3.50, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2; starts at (0.80, 0.00, 0.04) m, at rest
- ball3: free body; its geoms: ball3; starts at (1.10, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching floor
 0.00 s  ball2 starts touching floor
 0.00 s  ball3 starts touching floor
 0.07 s  ball1 leaves floor
 0.07 s  ball2 leaves floor
 0.07 s  ball1 first touches ball2
 0.07 s  ball2 starts moving
 0.07 s  ball1 leaves ball2
 0.12 s  ball2 touches floor again
 0.13 s  ball2 leaves floor
 0.14 s  ball1 is at the top of its flight, at (0.75, 0.00, 0.07) m
 0.16 s  ball2 touches floor again
 0.17 s  ball2 leaves floor
 0.17 s  ball3 leaves floor
 0.17 s  ball2 first touches ball3
 0.17 s  ball3 starts moving
 0.17 s  ball2 leaves ball3
 0.21 s  ball3 touches floor again
 0.22 s  ball1 touches floor again
 0.25 s  ball2 touches floor again
 0.56 s  ball3 leaves floor
 0.56 s  ball3 first touches cup_near_wall
 0.57 s  ball3 leaves cup_near_wall
 0.63 s  ball1 leaves floor
 0.63 s  ball1 touches ball2 again
 0.64 s  ball1 leaves ball2
 0.64 s  ball3 first touches cup_base
 0.65 s  ball3 leaves cup_base
 0.66 s  ball1 touches floor again
 0.69 s  ball3 touches cup_base again
 0.84 s  ball3 comes to rest at (1.60, 0.00, 0.04) m
 1.86 s  ball2 leaves floor
 1.86 s  ball2 first touches cup_near_wall
 2.07 s  ball2 touches floor 1 more times between 2.07 s and 6.00 s, still touching at the end
 2.08 s  ball2 comes to rest at (1.48, 0.00, 0.04) m
 2.08 s  ball2 leaves cup_near_wall
 3.09 s  ball1 touches ball2 again
 3.09 s  ball1 comes to rest at (1.37, 0.00, 0.04) m
 3.09 s  ball1 leaves ball2
 3.09 s  ball1 passes 0.15 m from ball3 without touching it: nearest points (1.40, 0.00, 0.04) m and (1.56, 0.00, 0.04) m
 3.09 s  ball1 passes 0.10 m from cup (cup_near_wall) without touching it: nearest points (1.40, 0.00, 0.03) m and (1.49, 0.00, 0.00) m
 4.16 s  ball2 touches cup_near_wall again
 4.18 s  ball2 leaves cup_near_wall

State every 0.25 s:
0.00 s: ball1 at (0.50, 0.00, 0.04) m, moving 3.50 m/s (vx +3.50, vy +0.00, vz +0.00); touching floor | ball2 at (0.80, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.10, 0.00, 0.04) m, at rest; touching floor
0.25 s: ball1 at (0.79, 0.00, 0.04) m, moving 0.65 m/s (vx +0.65, vy -0.00, vz +0.09); touching floor | ball2 at (1.03, 0.00, 0.04) m, moving 0.39 m/s (vx +0.06, vy -0.00, vz -0.38); touching nothing | ball3 at (1.19, 0.00, 0.04) m, moving 0.96 m/s (vx +0.96, vy +0.00, vz -0.00); touching floor
0.50 s: ball1 at (0.95, 0.00, 0.04) m, moving 0.62 m/s (vx +0.62, vy -0.00, vz +0.00); touching floor | ball2 at (1.08, 0.00, 0.04) m, moving 0.21 m/s (vx +0.21, vy -0.00, vz -0.00); touching floor | ball3 at (1.43, 0.00, 0.04) m, moving 0.92 m/s (vx +0.92, vy +0.00, vz -0.00); touching floor
0.75 s: ball1 at (1.05, 0.00, 0.04) m, moving 0.20 m/s (vx +0.20, vy -0.00, vz -0.00); touching floor | ball2 at (1.15, 0.00, 0.04) m, moving 0.35 m/s (vx +0.35, vy -0.00, vz -0.00); touching floor | ball3 at (1.58, 0.00, 0.04) m, moving 0.28 m/s (vx +0.28, vy -0.00, vz +0.01); touching nothing
1.00 s: ball1 at (1.10, 0.00, 0.04) m, moving 0.18 m/s (vx +0.18, vy -0.00, vz -0.00); touching floor | ball2 at (1.23, 0.00, 0.04) m, moving 0.32 m/s (vx +0.32, vy -0.00, vz -0.00); touching floor | ball3 at (1.60, 0.00, 0.04) m, at rest; touching cup_base
1.25 s: ball1 at (1.14, 0.00, 0.04) m, moving 0.17 m/s (vx +0.17, vy -0.00, vz -0.00); touching floor | ball2 at (1.31, 0.00, 0.04) m, moving 0.30 m/s (vx +0.30, vy -0.00, vz -0.00); touching floor | ball3 at (1.60, 0.00, 0.04) m, at rest; touching cup_base
1.50 s: ball1 at (1.18, 0.00, 0.04) m, moving 0.15 m/s (vx +0.15, vy -0.00, vz -0.00); touching floor | ball2 at (1.39, 0.00, 0.04) m, moving 0.28 m/s (vx +0.28, vy -0.00, vz -0.00); touching floor | ball3 at (1.60, 0.00, 0.04) m, at rest; touching cup_base
1.75 s: ball1 at (1.22, 0.00, 0.04) m, moving 0.14 m/s (vx +0.14, vy -0.00, vz -0.00); touching floor | ball2 at (1.45, 0.00, 0.04) m, moving 0.26 m/s (vx +0.26, vy -0.00, vz -0.00); touching floor | ball3 at (1.60, 0.00, 0.04) m, at rest; touching cup_base
2.00 s: ball1 at (1.25, 0.00, 0.04) m, moving 0.13 m/s (vx +0.13, vy -0.00, vz -0.00); touching floor | ball2 at (1.48, 0.00, 0.04) m, at rest; touching cup_near_wall | ball3 at (1.60, 0.00, 0.04) m, at rest; touching cup_base
2.25 s: ball1 at (1.28, 0.00, 0.04) m, moving 0.11 m/s (vx +0.11, vy -0.00, vz -0.00); touching floor | ball2 at (1.47, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.60, 0.00, 0.04) m, at rest; touching cup_base
2.50 s: ball1 at (1.31, 0.00, 0.04) m, moving 0.10 m/s (vx +0.10, vy -0.00, vz -0.00); touching floor | ball2 at (1.46, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.60, 0.00, 0.04) m, at rest; touching cup_base
2.75 s: ball1 at (1.34, 0.00, 0.04) m, moving 0.09 m/s (vx +0.09, vy -0.00, vz -0.00); touching floor | ball2 at (1.45, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.60, 0.00, 0.04) m, at rest; touching cup_base
3.00 s: ball1 at (1.36, 0.00, 0.04) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz -0.00); touching floor | ball2 at (1.45, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.60, 0.00, 0.04) m, at rest; touching cup_base
3.25 s: ball1 at (1.36, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.45, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.60, 0.00, 0.04) m, at rest; touching cup_base
3.50 s: ball1 at (1.36, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.46, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.60, 0.00, 0.04) m, at rest; touching cup_base
3.75 s: ball1 at (1.36, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.47, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.60, 0.00, 0.04) m, at rest; touching cup_base
4.00 s: ball1 at (1.35, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.48, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.60, 0.00, 0.04) m, at rest; touching cup_base
(the same through 5.50 s)
5.75 s: ball1 at (1.34, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.48, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.60, 0.00, 0.04) m, at rest; touching cup_base
6.00 s: ball1 at (1.34, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.47, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.60, 0.00, 0.04) m, at rest; touching cup_base

At the end (6.00 s):
- ball1 at (1.34, 0.00, 0.04) m, at rest; touching floor
- ball2 at (1.47, 0.00, 0.04) m, at rest; touching floor
- ball3 at (1.60, 0.00, 0.04) m, at rest; touching cup_base
</history>
