MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.00, 0.00, 0.04) m, moving 2.50 m/s (vx +2.50, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2; starts at (0.40, 0.00, 0.04) m, at rest
- ball3: free body; its geoms: ball3; starts at (0.80, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching floor
 0.00 s  ball2 starts touching floor
 0.00 s  ball3 starts touching floor
 0.13 s  ball1 leaves floor
 0.13 s  ball2 leaves floor
 0.13 s  ball1 first touches ball2
 0.13 s  ball2 starts moving
 0.13 s  ball1 leaves ball2
 0.20 s  ball1 is at the top of its flight, at (0.32, 0.00, 0.06) m
 0.23 s  ball2 touches floor again
 0.26 s  ball1 touches floor again
 0.32 s  ball2 leaves floor
 0.32 s  ball3 leaves floor
 0.32 s  ball2 first touches ball3
 0.32 s  ball3 starts moving
 0.32 s  ball2 leaves ball3
 0.37 s  ball3 touches floor again
 0.39 s  ball2 touches floor again
 0.72 s  ball3 leaves floor
 0.72 s  ball3 first touches cup_near_wall
 0.75 s  ball3 leaves cup_near_wall
 0.79 s  ball3 touches cup_near_wall again
 0.85 s  ball3 leaves cup_near_wall
 0.86 s  ball3 first touches cup_base
 1.37 s  ball3 first touches cup_far_wall
 1.39 s  ball3 leaves cup_far_wall
 2.16 s  ball2 leaves floor
 2.16 s  ball2 first touches cup_near_wall
 2.23 s  ball2 leaves cup_near_wall
 2.23 s  ball2 touches floor again
 3.23 s  ball1 touches ball2 again
 3.23 s  ball1 passes 0.20 m from cup (cup_near_wall) without touching it: nearest points (0.94, 0.00, 0.04) m and (1.13, 0.00, 0.01) m
 3.23 s  ball1 leaves ball2
 3.29 s  ball1 comes to rest at (0.89, 0.00, 0.04) m
 4.25 s  ball3 touches cup_near_wall again
 4.25 s  ball1 passes 0.24 m from ball3 without touching it: nearest points (0.89, 0.00, 0.04) m and (1.13, 0.00, 0.04) m
 4.25 s  ball3 leaves cup_base
 4.29 s  ball3 leaves cup_near_wall
 4.29 s  ball3 touches cup_base again
 4.87 s  ball2 touches cup_near_wall again
 4.90 s  ball2 leaves cup_near_wall
 4.90 s  ball2 comes to rest at (1.11, 0.00, 0.04) m
 6.00 s  ball3 is still moving at the end, 0.06 m/s

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.04) m, moving 2.50 m/s (vx +2.50, vy +0.00, vz +0.00); touching floor | ball2 at (0.40, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.80, 0.00, 0.04) m, at rest; touching floor
0.25 s: ball1 at (0.31, 0.00, 0.05) m, moving 0.55 m/s (vx -0.10, vy -0.00, vz -0.54); touching nothing | ball2 at (0.62, 0.00, 0.04) m, moving 1.48 m/s (vx +1.48, vy -0.00, vz +0.05); touching nothing | ball3 at (0.80, 0.00, 0.04) m, at rest; touching floor
0.50 s: ball1 at (0.36, 0.00, 0.04) m, moving 0.21 m/s (vx +0.21, vy -0.00, vz -0.00); touching floor | ball2 at (0.75, 0.00, 0.04) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz -0.00); touching floor | ball3 at (0.94, 0.00, 0.04) m, moving 0.73 m/s (vx +0.73, vy +0.00, vz -0.00); touching floor
0.75 s: ball1 at (0.41, 0.00, 0.04) m, moving 0.20 m/s (vx +0.20, vy -0.00, vz -0.00); touching floor | ball2 at (0.81, 0.00, 0.04) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz -0.00); touching floor | ball3 at (1.12, 0.00, 0.05) m, moving 0.49 m/s (vx +0.42, vy +0.00, vz +0.26); touching nothing
1.00 s: ball1 at (0.46, 0.00, 0.04) m, moving 0.20 m/s (vx +0.20, vy -0.00, vz -0.00); touching floor | ball2 at (0.86, 0.00, 0.04) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz -0.00); touching floor | ball3 at (1.24, 0.00, 0.04) m, moving 0.48 m/s (vx +0.48, vy +0.00, vz +0.00); touching cup_base
1.25 s: ball1 at (0.51, 0.00, 0.04) m, moving 0.20 m/s (vx +0.20, vy -0.00, vz -0.00); touching floor | ball2 at (0.92, 0.00, 0.04) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz -0.00); touching floor | ball3 at (1.36, 0.00, 0.04) m, moving 0.48 m/s (vx +0.48, vy +0.00, vz -0.00); touching cup_base
1.50 s: ball1 at (0.56, 0.00, 0.04) m, moving 0.20 m/s (vx +0.20, vy -0.00, vz -0.00); touching floor | ball2 at (0.97, 0.00, 0.04) m, moving 0.21 m/s (vx +0.21, vy -0.00, vz -0.00); touching floor | ball3 at (1.41, 0.00, 0.04) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz +0.00); touching cup_base
1.75 s: ball1 at (0.61, 0.00, 0.04) m, moving 0.20 m/s (vx +0.20, vy -0.00, vz -0.00); touching floor | ball2 at (1.02, 0.00, 0.04) m, moving 0.21 m/s (vx +0.21, vy -0.00, vz -0.00); touching floor | ball3 at (1.38, 0.00, 0.04) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz -0.00); touching cup_base
2.00 s: ball1 at (0.66, 0.00, 0.04) m, moving 0.19 m/s (vx +0.19, vy -0.00, vz -0.00); touching floor | ball2 at (1.08, 0.00, 0.04) m, moving 0.21 m/s (vx +0.21, vy -0.00, vz -0.00); touching floor | ball3 at (1.36, 0.00, 0.04) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz -0.00); touching cup_base
2.25 s: ball1 at (0.71, 0.00, 0.04) m, moving 0.19 m/s (vx +0.19, vy -0.00, vz -0.00); touching floor | ball2 at (1.11, 0.00, 0.04) m, moving 0.14 m/s (vx -0.14, vy -0.00, vz +0.02); touching floor | ball3 at (1.34, 0.00, 0.04) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz -0.00); touching cup_base
2.50 s: ball1 at (0.76, 0.00, 0.04) m, moving 0.19 m/s (vx +0.19, vy -0.00, vz -0.00); touching floor | ball2 at (1.07, 0.00, 0.04) m, moving 0.14 m/s (vx -0.14, vy -0.00, vz +0.00); touching floor | ball3 at (1.32, 0.00, 0.04) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz -0.00); touching cup_base
2.75 s: ball1 at (0.81, 0.00, 0.04) m, moving 0.19 m/s (vx +0.19, vy -0.00, vz -0.00); touching floor | ball2 at (1.04, 0.00, 0.04) m, moving 0.13 m/s (vx -0.13, vy -0.00, vz +0.00); touching floor | ball3 at (1.30, 0.00, 0.04) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz -0.00); touching cup_base
3.00 s: ball1 at (0.85, 0.00, 0.04) m, moving 0.19 m/s (vx +0.19, vy -0.00, vz -0.00); touching floor | ball2 at (1.01, 0.00, 0.04) m, moving 0.13 m/s (vx -0.13, vy -0.00, vz +0.00); touching floor | ball3 at (1.27, 0.00, 0.04) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz -0.00); touching cup_base
3.25 s: ball1 at (0.89, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching floor | ball2 at (0.98, 0.00, 0.04) m, moving 0.09 m/s (vx +0.09, vy -0.00, vz -0.00); touching floor | ball3 at (1.25, 0.00, 0.04) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz -0.00); touching cup_base
3.50 s: ball1 at (0.88, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.00, 0.00, 0.04) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz -0.00); touching floor | ball3 at (1.23, 0.00, 0.04) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz -0.00); touching cup_base
3.75 s: ball1 at (0.87, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.02, 0.00, 0.04) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz +0.00); touching floor | ball3 at (1.21, 0.00, 0.04) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz -0.00); touching cup_base
4.00 s: ball1 at (0.86, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.04, 0.00, 0.04) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz +0.00); touching floor | ball3 at (1.19, 0.00, 0.04) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz -0.00); touching cup_base
4.25 s: ball1 at (0.85, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.06, 0.00, 0.04) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz +0.00); touching floor | ball3 at (1.17, 0.00, 0.04) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz +0.01); touching cup_base, cup_near_wall
4.50 s: ball1 at (0.83, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.08, 0.00, 0.04) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz +0.00); touching floor | ball3 at (1.18, 0.00, 0.04) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz -0.00); touching cup_base
4.75 s: ball1 at (0.82, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.10, 0.00, 0.04) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz +0.00); touching floor | ball3 at (1.20, 0.00, 0.04) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz -0.00); touching cup_base
5.00 s: ball1 at (0.81, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.10, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.21, 0.00, 0.04) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz -0.00); touching cup_base
5.25 s: ball1 at (0.80, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.09, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.23, 0.00, 0.04) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz -0.00); touching cup_base
5.50 s: ball1 at (0.79, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.08, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.25, 0.00, 0.04) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz -0.00); touching cup_base
5.75 s: ball1 at (0.78, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.07, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.26, 0.00, 0.04) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz -0.00); touching cup_base
6.00 s: ball1 at (0.77, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.06, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.28, 0.00, 0.04) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz -0.00); touching cup_base

At the end (6.00 s):
- ball1 at (0.77, 0.00, 0.04) m, at rest; touching floor
- ball2 at (1.06, 0.00, 0.04) m, at rest; touching floor
- ball3 at (1.28, 0.00, 0.04) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz -0.00); touching cup_base
</history>
