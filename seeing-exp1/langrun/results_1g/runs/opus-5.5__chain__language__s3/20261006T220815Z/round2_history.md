Your expectations, checked against the run (4 of 4 hold):

- holds: ball1 touches ball2 (first touch at 0.05 s)
- holds: ball2 touches ball3 (first touch at 0.11 s)
- holds: ball3 touches cup (first touch at 0.27 s)
- holds: ball3 comes to rest in cup (ball3 at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (1.00, 0.00, 0.04) m, moving 4.00 m/s (vx +4.00, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2; starts at (1.25, 0.00, 0.04) m, at rest
- ball3: free body; its geoms: ball3; starts at (1.50, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching floor
 0.00 s  ball2 starts touching floor
 0.00 s  ball3 starts touching floor
 0.05 s  ball1 leaves floor
 0.05 s  ball2 leaves floor
 0.05 s  ball1 first touches ball2
 0.05 s  ball2 starts moving
 0.05 s  ball1 leaves ball2
 0.10 s  ball1 passes 0.24 m from ball3 without touching it: nearest points (1.22, 0.00, 0.07) m and (1.46, 0.00, 0.04) m
 0.11 s  ball3 leaves floor
 0.11 s  ball2 first touches ball3
 0.11 s  ball3 starts moving
 0.11 s  ball2 leaves ball3
 0.14 s  ball1 is at the top of its flight, at (1.19, 0.00, 0.09) m
 0.15 s  ball3 touches floor again
 0.19 s  ball2 touches floor again
 0.24 s  ball1 touches floor again
 0.27 s  ball3 leaves floor
 0.27 s  ball3 first touches cup_near_wall
 0.27 s  ball1 leaves floor
 0.28 s  ball3 leaves cup_near_wall
 0.31 s  ball1 touches floor again
 0.38 s  ball3 first touches cup_base
 0.39 s  ball3 leaves cup_base
 0.42 s  ball3 touches cup_base again
 0.66 s  ball3 leaves cup_base
 0.66 s  ball1 touches ball2 again
 0.67 s  ball1 leaves ball2
 0.67 s  ball3 first touches cup_far_wall
 0.68 s  ball3 leaves cup_far_wall
 0.71 s  ball3 touches cup_base again
 0.77 s  ball3 comes to rest at (2.24, 0.00, 0.04) m
 0.90 s  ball1 comes to rest at (1.40, 0.00, 0.04) m
 1.76 s  ball2 comes to rest at (1.60, 0.00, 0.04) m
 6.00 s  ball2 passes 0.13 m from cup (cup_near_wall) without touching it: nearest points (1.66, 0.00, 0.03) m and (1.79, 0.00, 0.00) m
 6.00 s  ball1 passes 0.33 m from cup (cup_near_wall) without touching it: nearest points (1.46, 0.00, 0.04) m and (1.79, 0.00, 0.00) m

State every 0.25 s:
0.00 s: ball1 at (1.00, 0.00, 0.04) m, moving 4.00 m/s (vx +4.00, vy +0.00, vz +0.00); touching floor | ball2 at (1.25, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.50, 0.00, 0.04) m, at rest; touching floor
0.25 s: ball1 at (1.19, 0.00, 0.04) m, moving 0.39 m/s (vx +0.39, vy -0.00, vz -0.03); touching floor | ball2 at (1.45, 0.00, 0.04) m, moving 0.05 m/s (vx +0.05, vy +0.00, vz +0.00); touching floor | ball3 at (1.74, 0.00, 0.04) m, moving 1.57 m/s (vx +1.57, vy -0.00, vz +0.01); touching nothing
0.50 s: ball1 at (1.32, 0.00, 0.04) m, moving 0.45 m/s (vx +0.45, vy -0.00, vz -0.01); touching floor | ball2 at (1.46, 0.00, 0.04) m, at rest; touching floor | ball3 at (2.07, 0.00, 0.04) m, moving 1.17 m/s (vx +1.17, vy +0.00, vz +0.01); touching nothing
0.75 s: ball1 at (1.39, 0.00, 0.04) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | ball2 at (1.48, 0.00, 0.04) m, moving 0.20 m/s (vx +0.20, vy +0.00, vz +0.00); touching floor | ball3 at (2.24, 0.00, 0.04) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz +0.00); touching cup_base
1.00 s: ball1 at (1.40, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.52, 0.00, 0.04) m, moving 0.15 m/s (vx +0.15, vy +0.00, vz -0.00); touching floor | ball3 at (2.24, 0.00, 0.04) m, at rest; touching cup_base
1.25 s: ball1 at (1.41, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.56, 0.00, 0.04) m, moving 0.11 m/s (vx +0.11, vy +0.00, vz -0.00); touching floor | ball3 at (2.24, 0.00, 0.04) m, at rest; touching cup_base
1.50 s: ball1 at (1.42, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.58, 0.00, 0.04) m, moving 0.08 m/s (vx +0.08, vy +0.00, vz -0.00); touching floor | ball3 at (2.24, 0.00, 0.04) m, at rest; touching cup_base
1.75 s: ball1 at (1.42, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.59, 0.00, 0.04) m, moving 0.05 m/s (vx +0.05, vy +0.00, vz -0.00); touching floor | ball3 at (2.24, 0.00, 0.04) m, at rest; touching cup_base
2.00 s: ball1 at (1.42, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.61, 0.00, 0.04) m, at rest; touching floor | ball3 at (2.24, 0.00, 0.04) m, at rest; touching cup_base
(the same through 2.50 s)
2.75 s: ball1 at (1.42, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.62, 0.00, 0.04) m, at rest; touching floor | ball3 at (2.24, 0.00, 0.04) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (1.42, 0.00, 0.04) m, at rest; touching floor
- ball2 at (1.62, 0.00, 0.04) m, at rest; touching floor
- ball3 at (2.24, 0.00, 0.04) m, at rest; touching cup_base
</history>
