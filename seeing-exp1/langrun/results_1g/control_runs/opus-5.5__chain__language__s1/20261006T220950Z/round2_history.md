MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.00, 0.00, 0.04) m, moving 4.00 m/s (vx +4.00, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2; starts at (0.30, 0.00, 0.04) m, at rest
- ball3: free body; its geoms: ball3; starts at (0.50, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching floor
 0.00 s  ball2 starts touching floor
 0.00 s  ball3 starts touching floor
 0.06 s  ball1 leaves floor
 0.06 s  ball2 leaves floor
 0.06 s  ball1 first touches ball2
 0.06 s  ball2 starts moving
 0.06 s  ball1 leaves ball2
 0.10 s  ball1 passes 0.18 m from ball3 without touching it: nearest points (0.29, 0.00, 0.06) m and (0.46, 0.00, 0.04) m
 0.11 s  ball3 leaves floor
 0.11 s  ball2 first touches ball3
 0.11 s  ball3 starts moving
 0.11 s  ball2 leaves ball3
 0.15 s  ball1 is at the top of its flight, at (0.27, 0.00, 0.08) m
 0.15 s  ball2 touches floor again
 0.17 s  ball3 touches floor again
 0.24 s  ball1 touches floor again
 0.26 s  ball3 leaves floor
 0.26 s  ball3 first touches cup_near_wall
 0.26 s  ball1 leaves floor
 0.27 s  ball3 leaves cup_near_wall
 0.28 s  ball1 touches ball2 again
 0.28 s  ball1 leaves ball2
 0.32 s  ball3 is at the top of its flight, at (0.85, 0.00, 0.06) m
 0.32 s  ball1 touches floor again
 0.37 s  ball3 first touches cup_base
 0.38 s  ball3 leaves cup_base
 0.44 s  ball3 touches cup_base again
 0.44 s  ball3 leaves cup_base
 0.48 s  ball3 touches cup_base again
 0.68 s  ball3 first touches cup_far_wall
 0.70 s  ball3 leaves cup_far_wall
 0.77 s  ball3 comes to rest at (1.23, 0.00, 0.04) m
 1.62 s  ball2 leaves floor
 1.62 s  ball2 first touches cup_near_wall
 1.76 s  ball2 touches floor again
 1.76 s  ball2 leaves cup_near_wall
 2.37 s  ball1 touches ball2 again
 2.37 s  ball1 leaves ball2
 2.37 s  ball1 passes 0.11 m from cup (cup_near_wall) without touching it: nearest points (0.67, 0.00, 0.03) m and (0.78, 0.00, 0.00) m
 2.38 s  ball1 comes to rest at (0.63, 0.00, 0.04) m
 2.49 s  ball2 comes to rest at (0.72, 0.00, 0.04) m
 3.69 s  ball2 touches cup_near_wall again
 3.72 s  ball2 leaves cup_near_wall

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.04) m, moving 4.00 m/s (vx +4.00, vy +0.00, vz +0.00); touching floor | ball2 at (0.30, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.50, 0.00, 0.04) m, at rest; touching floor
0.25 s: ball1 at (0.32, 0.00, 0.04) m, moving 0.84 m/s (vx +0.81, vy -0.00, vz +0.23); touching floor | ball2 at (0.42, 0.00, 0.04) m, moving 0.10 m/s (vx -0.10, vy +0.00, vz -0.00); touching floor | ball3 at (0.75, 0.00, 0.04) m, moving 1.56 m/s (vx +1.56, vy +0.00, vz +0.00); touching nothing
0.50 s: ball1 at (0.38, 0.00, 0.04) m, moving 0.19 m/s (vx +0.19, vy +0.00, vz -0.00); touching floor | ball2 at (0.49, 0.00, 0.04) m, moving 0.29 m/s (vx +0.29, vy -0.00, vz -0.00); touching floor | ball3 at (1.07, 0.00, 0.04) m, moving 1.11 m/s (vx +1.10, vy -0.00, vz -0.09); touching nothing
0.75 s: ball1 at (0.42, 0.00, 0.04) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz -0.00); touching floor | ball2 at (0.56, 0.00, 0.04) m, moving 0.27 m/s (vx +0.27, vy -0.00, vz -0.00); touching floor | ball3 at (1.23, 0.00, 0.04) m, moving 0.07 m/s (vx -0.07, vy -0.00, vz +0.00); touching cup_base
1.00 s: ball1 at (0.46, 0.00, 0.04) m, moving 0.16 m/s (vx +0.16, vy +0.00, vz -0.00); touching floor | ball2 at (0.62, 0.00, 0.04) m, moving 0.25 m/s (vx +0.25, vy -0.00, vz -0.00); touching floor | ball3 at (1.23, 0.00, 0.04) m, at rest; touching cup_base
1.25 s: ball1 at (0.50, 0.00, 0.04) m, moving 0.15 m/s (vx +0.15, vy +0.00, vz -0.00); touching floor | ball2 at (0.68, 0.00, 0.04) m, moving 0.23 m/s (vx +0.23, vy -0.00, vz -0.00); touching floor | ball3 at (1.23, 0.00, 0.04) m, at rest; touching cup_base
1.50 s: ball1 at (0.54, 0.00, 0.04) m, moving 0.13 m/s (vx +0.13, vy +0.00, vz -0.00); touching floor | ball2 at (0.74, 0.00, 0.04) m, moving 0.21 m/s (vx +0.21, vy -0.00, vz -0.00); touching floor | ball3 at (1.23, 0.00, 0.04) m, at rest; touching cup_base
1.75 s: ball1 at (0.57, 0.00, 0.04) m, moving 0.12 m/s (vx +0.12, vy +0.00, vz -0.00); touching floor | ball2 at (0.77, 0.00, 0.04) m, moving 0.09 m/s (vx -0.09, vy -0.00, vz -0.03); touching cup_near_wall | ball3 at (1.23, 0.00, 0.04) m, at rest; touching cup_base
2.00 s: ball1 at (0.60, 0.00, 0.04) m, moving 0.11 m/s (vx +0.11, vy +0.00, vz -0.00); touching floor | ball2 at (0.74, 0.00, 0.04) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz -0.00); touching floor | ball3 at (1.23, 0.00, 0.04) m, at rest; touching cup_base
2.25 s: ball1 at (0.62, 0.00, 0.04) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz -0.00); touching floor | ball2 at (0.72, 0.00, 0.04) m, moving 0.08 m/s (vx -0.08, vy +0.00, vz -0.00); touching floor | ball3 at (1.23, 0.00, 0.04) m, at rest; touching cup_base
2.50 s: ball1 at (0.63, 0.00, 0.04) m, at rest; touching floor | ball2 at (0.72, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.23, 0.00, 0.04) m, at rest; touching cup_base
2.75 s: ball1 at (0.62, 0.00, 0.04) m, at rest; touching floor | ball2 at (0.73, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.23, 0.00, 0.04) m, at rest; touching cup_base
3.00 s: ball1 at (0.61, 0.00, 0.04) m, at rest; touching floor | ball2 at (0.74, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.23, 0.00, 0.04) m, at rest; touching cup_base
3.25 s: ball1 at (0.61, 0.00, 0.04) m, at rest; touching floor | ball2 at (0.75, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.23, 0.00, 0.04) m, at rest; touching cup_base
3.50 s: ball1 at (0.60, 0.00, 0.04) m, at rest; touching floor | ball2 at (0.76, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.23, 0.00, 0.04) m, at rest; touching cup_base
(the same through 3.75 s)
4.00 s: ball1 at (0.59, 0.00, 0.04) m, at rest; touching floor | ball2 at (0.76, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.23, 0.00, 0.04) m, at rest; touching cup_base
(the same through 4.25 s)
4.50 s: ball1 at (0.58, 0.00, 0.04) m, at rest; touching floor | ball2 at (0.76, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.23, 0.00, 0.04) m, at rest; touching cup_base
(the same through 5.25 s)
5.50 s: ball1 at (0.57, 0.00, 0.04) m, at rest; touching floor | ball2 at (0.76, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.23, 0.00, 0.04) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (0.57, 0.00, 0.04) m, at rest; touching floor
- ball2 at (0.76, 0.00, 0.04) m, at rest; touching floor
- ball3 at (1.23, 0.00, 0.04) m, at rest; touching cup_base
</history>
