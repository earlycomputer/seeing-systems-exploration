Your expectations, checked against the run (3 of 3 hold):

- holds: ball1 touches ball2 (first touch at 0.12 s)
- holds: ball2 touches ball3 (first touch at 0.40 s)
- holds: ball3 comes to rest in cup (ball3 at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (-0.60, 0.00, 0.04) m, moving 1.40 m/s (vx +1.40, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2; starts at (-0.35, 0.00, 0.04) m, at rest
- ball3: free body; its geoms: ball3; starts at (-0.10, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching floor
 0.00 s  ball2 starts touching floor
 0.00 s  ball3 starts touching floor
 0.12 s  ball1 leaves floor
 0.12 s  ball1 first touches ball2
 0.12 s  ball2 starts moving
 0.13 s  ball1 leaves ball2
 0.18 s  ball1 touches floor again
 0.40 s  ball2 first touches ball3
 0.40 s  ball3 starts moving
 0.40 s  ball2 leaves ball3
 0.58 s  ball1 touches ball2 again
 0.58 s  ball1 leaves ball2
 0.85 s  ball3 leaves floor
 0.85 s  ball3 first touches cup_near_wall
 0.89 s  ball3 first touches cup_base
 0.89 s  ball3 leaves cup_near_wall
 1.42 s  ball2 touches ball3 again
 1.42 s  ball2 leaves ball3
 1.86 s  ball2 touches ball3 again
 1.86 s  ball2 leaves ball3
 2.29 s  ball1 touches ball2 again
 2.29 s  ball1 comes to rest at (-0.07, 0.00, 0.04) m
 2.29 s  ball1 passes 0.08 m from ball3 without touching it: nearest points (-0.03, 0.00, 0.04) m and (0.05, 0.00, 0.04) m
 2.30 s  ball2 touches ball3 again
 2.30 s  ball2 comes to rest at (0.01, 0.00, 0.04) m
 2.30 s  ball2 leaves ball3
 2.30 s  ball3 comes to rest at (0.09, 0.00, 0.04) m
 2.32 s  ball1 leaves ball2
 2.32 s  ball1 passes 0.10 m from cup (cup_near_wall) without touching it: nearest points (-0.04, 0.00, 0.03) m and (0.06, 0.00, 0.00) m
 2.45 s  ball2 touches ball3 1 more times between 2.45 s and 2.46 s
 2.46 s  ball2 passes 0.02 m from cup (cup_near_wall) without touching it: nearest points (0.04, 0.00, 0.02) m and (0.06, 0.00, 0.00) m

State every 0.25 s:
0.00 s: ball1 at (-0.60, 0.00, 0.04) m, moving 1.40 m/s (vx +1.40, vy +0.00, vz +0.00); touching floor | ball2 at (-0.35, 0.00, 0.04) m, at rest; touching floor | ball3 at (-0.10, 0.00, 0.04) m, at rest; touching floor
0.25 s: ball1 at (-0.38, 0.00, 0.04) m, moving 0.41 m/s (vx +0.41, vy -0.00, vz +0.00); touching floor | ball2 at (-0.27, 0.00, 0.04) m, moving 0.59 m/s (vx +0.59, vy -0.00, vz +0.00); touching floor | ball3 at (-0.10, 0.00, 0.04) m, at rest; touching floor
0.50 s: ball1 at (-0.28, 0.00, 0.04) m, moving 0.40 m/s (vx +0.40, vy -0.00, vz -0.00); touching floor | ball2 at (-0.18, 0.00, 0.04) m, at rest; touching floor | ball3 at (-0.06, 0.00, 0.04) m, moving 0.33 m/s (vx +0.33, vy +0.00, vz +0.00); touching floor
0.75 s: ball1 at (-0.23, 0.00, 0.04) m, moving 0.11 m/s (vx +0.11, vy +0.00, vz -0.00); touching floor | ball2 at (-0.14, 0.00, 0.04) m, moving 0.21 m/s (vx +0.21, vy -0.00, vz -0.00); touching floor | ball3 at (0.02, 0.00, 0.04) m, moving 0.32 m/s (vx +0.32, vy +0.00, vz -0.00); touching floor
1.00 s: ball1 at (-0.21, 0.00, 0.04) m, moving 0.11 m/s (vx +0.11, vy +0.00, vz -0.00); touching floor | ball2 at (-0.08, 0.00, 0.04) m, moving 0.20 m/s (vx +0.20, vy -0.00, vz -0.00); touching floor | ball3 at (0.08, 0.00, 0.04) m, moving 0.07 m/s (vx +0.07, vy +0.00, vz -0.01); touching nothing
1.25 s: ball1 at (-0.18, 0.00, 0.04) m, moving 0.11 m/s (vx +0.11, vy +0.00, vz -0.00); touching floor | ball2 at (-0.03, 0.00, 0.04) m, moving 0.20 m/s (vx +0.20, vy -0.00, vz -0.00); touching floor | ball3 at (0.08, 0.00, 0.04) m, at rest; touching cup_base
1.50 s: ball1 at (-0.15, 0.00, 0.04) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz -0.00); touching floor | ball2 at (0.00, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.09, 0.00, 0.04) m, at rest; touching cup_base
1.75 s: ball1 at (-0.13, 0.00, 0.04) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz -0.00); touching floor | ball2 at (0.00, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.09, 0.00, 0.04) m, at rest; touching cup_base
2.00 s: ball1 at (-0.10, 0.00, 0.04) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz -0.00); touching floor | ball2 at (0.01, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.09, 0.00, 0.04) m, at rest; touching cup_base
2.25 s: ball1 at (-0.08, 0.00, 0.04) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz -0.00); touching floor | ball2 at (0.01, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.09, 0.00, 0.04) m, at rest; touching cup_base
2.50 s: ball1 at (-0.07, 0.00, 0.04) m, at rest; touching floor | ball2 at (0.01, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.09, 0.00, 0.04) m, at rest; touching cup_base
(the same through 3.00 s)
3.25 s: ball1 at (-0.08, 0.00, 0.04) m, at rest; touching floor | ball2 at (0.01, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.09, 0.00, 0.04) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (-0.08, 0.00, 0.04) m, at rest; touching floor
- ball2 at (0.01, 0.00, 0.04) m, at rest; touching floor
- ball3 at (0.09, 0.00, 0.04) m, at rest; touching cup_base
</history>
