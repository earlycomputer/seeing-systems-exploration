Your expectations, checked against the run (4 of 4 hold):

- holds: ball1 touches ball2 (first touch at 0.06 s)
- holds: ball2 touches ball3 (first touch at 0.23 s)
- holds: ball3 touches ramp (first touch at 0.42 s)
- holds: ball3 comes to rest in cup (ball3 at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.00, 0.00, 0.04) m, moving 4.00 m/s (vx +4.00, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2; starts at (0.30, 0.00, 0.04) m, at rest
- ball3: free body; its geoms: ball3; starts at (0.80, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching floor
 0.00 s  ball2 starts touching floor
 0.00 s  ball3 starts touching floor
 0.06 s  ball1 leaves floor
 0.06 s  ball2 leaves floor
 0.06 s  ball1 first touches ball2
 0.06 s  ball2 starts moving
 0.06 s  ball1 leaves ball2
 0.14 s  ball1 is at the top of its flight, at (0.27, 0.00, 0.07) m
 0.15 s  ball2 touches floor again
 0.15 s  ball2 leaves floor
 0.20 s  ball2 touches floor again
 0.23 s  ball1 touches floor again
 0.23 s  ball2 leaves floor
 0.23 s  ball2 first touches ball3
 0.23 s  ball3 starts moving
 0.23 s  ball2 leaves ball3
 0.29 s  ball2 touches floor again
 0.42 s  ball3 leaves floor
 0.42 s  ball3 first touches ramp
 0.43 s  ball3 leaves ramp
 0.48 s  ball3 touches ramp again
 0.73 s  ball2 leaves floor
 0.73 s  ball2 first touches ramp
 0.95 s  ball1 leaves floor
 0.95 s  ball1 first touches ramp
 0.95 s  ball1 touches ball2 again
 0.96 s  ball1 leaves ramp
 0.96 s  ball1 leaves ball2
 1.05 s  ball1 touches ramp again
 1.25 s  ball3 leaves ramp
 1.30 s  ball3 first touches cup_base
 1.97 s  ball2 touches ball3 again
 1.97 s  ball2 leaves ball3
 1.98 s  ball3 comes to rest at (1.49, 0.00, 0.04) m
 2.02 s  ball2 touches ball3 again
 2.02 s  ball2 passes 0.02 m from cup (cup_near_wall) without touching it: nearest points (1.44, 0.00, 0.03) m and (1.45, 0.00, 0.01) m
 2.02 s  ball2 leaves ball3
 2.32 s  ball1 passes 0.14 m from ball3 without touching it: nearest points (1.32, 0.00, 0.05) m and (1.45, 0.00, 0.04) m
 2.32 s  ball1 passes 0.13 m from cup (cup_near_wall) without touching it: nearest points (1.32, 0.00, 0.05) m and (1.45, 0.00, 0.01) m
 2.78 s  ball1 touches ball2 again
 2.78 s  ball1 leaves ball2
 3.66 s  ball1 leaves ramp
 3.66 s  ball1 touches floor again
 3.90 s  ball2 leaves ramp
 3.91 s  ball2 touches floor 1 more times between 3.91 s and 6.00 s, still touching at the end
 4.95 s  ball1 touches ball2 again
 4.95 s  ball1 leaves ball2
 6.00 s  ball1 is still moving at the end, 0.47 m/s
 6.00 s  ball2 is still moving at the end, 0.37 m/s

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.04) m, moving 4.00 m/s (vx +4.00, vy +0.00, vz +0.00); touching floor | ball2 at (0.30, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.80, 0.00, 0.04) m, at rest; touching floor
0.25 s: ball1 at (0.33, 0.00, 0.04) m, moving 0.93 m/s (vx +0.92, vy -0.00, vz +0.15); touching floor | ball2 at (0.73, 0.00, 0.04) m, moving 0.44 m/s (vx +0.42, vy +0.00, vz +0.11); touching nothing | ball3 at (0.82, 0.00, 0.04) m, moving 1.28 m/s (vx +1.28, vy -0.00, vz -0.11); touching nothing
0.50 s: ball1 at (0.57, 0.00, 0.04) m, moving 0.93 m/s (vx +0.93, vy -0.00, vz -0.00); touching floor | ball2 at (0.86, 0.00, 0.04) m, moving 0.53 m/s (vx +0.53, vy +0.00, vz -0.00); touching floor | ball3 at (1.04, 0.00, 0.05) m, moving 0.69 m/s (vx +0.69, vy -0.00, vz +0.06); touching ramp
0.75 s: ball1 at (0.80, 0.00, 0.04) m, moving 0.93 m/s (vx +0.93, vy -0.00, vz -0.00); touching floor | ball2 at (0.99, 0.00, 0.04) m, moving 0.41 m/s (vx +0.40, vy +0.00, vz +0.11); touching nothing | ball3 at (1.20, 0.00, 0.05) m, moving 0.61 m/s (vx +0.61, vy -0.00, vz +0.03); touching ramp
1.00 s: ball1 at (1.01, 0.00, 0.05) m, moving 0.38 m/s (vx +0.38, vy -0.00, vz +0.03); touching nothing | ball2 at (1.09, 0.00, 0.05) m, moving 0.49 m/s (vx +0.49, vy +0.00, vz +0.02); touching ramp | ball3 at (1.34, 0.00, 0.06) m, moving 0.53 m/s (vx +0.53, vy -0.00, vz +0.02); touching ramp
1.25 s: ball1 at (1.10, 0.00, 0.05) m, moving 0.34 m/s (vx +0.34, vy -0.00, vz +0.01); touching ramp | ball2 at (1.20, 0.00, 0.05) m, moving 0.41 m/s (vx +0.41, vy +0.00, vz +0.02); touching ramp | ball3 at (1.46, 0.00, 0.06) m, moving 0.51 m/s (vx +0.48, vy -0.00, vz -0.18); touching ramp
1.50 s: ball1 at (1.17, 0.00, 0.05) m, moving 0.26 m/s (vx +0.26, vy -0.00, vz +0.01); touching ramp | ball2 at (1.30, 0.00, 0.06) m, moving 0.33 m/s (vx +0.33, vy +0.00, vz +0.01); touching ramp | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
1.75 s: ball1 at (1.23, 0.00, 0.06) m, moving 0.18 m/s (vx +0.18, vy -0.00, vz +0.01); touching ramp | ball2 at (1.37, 0.00, 0.06) m, moving 0.25 m/s (vx +0.25, vy +0.00, vz +0.01); touching ramp | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
2.00 s: ball1 at (1.26, 0.00, 0.06) m, moving 0.10 m/s (vx +0.10, vy -0.00, vz +0.00); touching ramp | ball2 at (1.42, 0.00, 0.06) m, at rest; touching ramp | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
2.25 s: ball1 at (1.28, 0.00, 0.06) m, at rest; touching ramp | ball2 at (1.41, 0.00, 0.06) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz -0.00); touching ramp | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
2.50 s: ball1 at (1.27, 0.00, 0.06) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching ramp | ball2 at (1.38, 0.00, 0.06) m, moving 0.15 m/s (vx -0.15, vy +0.00, vz -0.01); touching ramp | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
2.75 s: ball1 at (1.25, 0.00, 0.06) m, moving 0.13 m/s (vx -0.13, vy -0.00, vz -0.01); touching ramp | ball2 at (1.33, 0.00, 0.06) m, moving 0.23 m/s (vx -0.23, vy +0.00, vz -0.01); touching ramp | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
3.00 s: ball1 at (1.20, 0.00, 0.05) m, moving 0.23 m/s (vx -0.23, vy -0.00, vz -0.01); touching ramp | ball2 at (1.29, 0.00, 0.06) m, moving 0.20 m/s (vx -0.20, vy +0.00, vz -0.01); touching ramp | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
3.25 s: ball1 at (1.13, 0.00, 0.05) m, moving 0.31 m/s (vx -0.31, vy -0.00, vz -0.01); touching ramp | ball2 at (1.23, 0.00, 0.06) m, moving 0.28 m/s (vx -0.28, vy +0.00, vz -0.01); touching ramp | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
3.50 s: ball1 at (1.05, 0.00, 0.05) m, moving 0.39 m/s (vx -0.39, vy -0.00, vz -0.02); touching ramp | ball2 at (1.15, 0.00, 0.05) m, moving 0.36 m/s (vx -0.36, vy +0.00, vz -0.02); touching ramp | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
3.75 s: ball1 at (0.94, 0.00, 0.04) m, moving 0.46 m/s (vx -0.46, vy -0.00, vz -0.00); touching floor | ball2 at (1.05, 0.00, 0.05) m, moving 0.43 m/s (vx -0.43, vy +0.00, vz -0.02); touching ramp | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
4.00 s: ball1 at (0.83, 0.00, 0.04) m, moving 0.46 m/s (vx -0.46, vy -0.00, vz -0.00); touching floor | ball2 at (0.93, 0.00, 0.04) m, moving 0.49 m/s (vx -0.49, vy +0.00, vz -0.00); touching floor | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
4.25 s: ball1 at (0.71, 0.00, 0.04) m, moving 0.45 m/s (vx -0.45, vy -0.00, vz -0.00); touching floor | ball2 at (0.81, 0.00, 0.04) m, moving 0.48 m/s (vx -0.48, vy +0.00, vz -0.00); touching floor | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
4.50 s: ball1 at (0.60, 0.00, 0.04) m, moving 0.45 m/s (vx -0.45, vy -0.00, vz -0.00); touching floor | ball2 at (0.69, 0.00, 0.04) m, moving 0.48 m/s (vx -0.48, vy +0.00, vz -0.00); touching floor | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
4.75 s: ball1 at (0.49, 0.00, 0.04) m, moving 0.45 m/s (vx -0.45, vy -0.00, vz -0.00); touching floor | ball2 at (0.57, 0.00, 0.04) m, moving 0.48 m/s (vx -0.48, vy +0.00, vz -0.00); touching floor | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
5.00 s: ball1 at (0.37, 0.00, 0.04) m, moving 0.48 m/s (vx -0.48, vy -0.00, vz -0.00); touching floor | ball2 at (0.46, 0.00, 0.04) m, moving 0.37 m/s (vx -0.37, vy +0.00, vz +0.00); touching floor | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
5.25 s: ball1 at (0.25, 0.00, 0.04) m, moving 0.48 m/s (vx -0.48, vy -0.00, vz -0.00); touching floor | ball2 at (0.36, 0.00, 0.04) m, moving 0.37 m/s (vx -0.37, vy +0.00, vz -0.00); touching floor | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
5.50 s: ball1 at (0.13, 0.00, 0.04) m, moving 0.48 m/s (vx -0.48, vy -0.00, vz -0.00); touching floor | ball2 at (0.27, 0.00, 0.04) m, moving 0.37 m/s (vx -0.37, vy +0.00, vz -0.00); touching floor | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
5.75 s: ball1 at (0.01, 0.00, 0.04) m, moving 0.48 m/s (vx -0.48, vy -0.00, vz -0.00); touching floor | ball2 at (0.18, 0.00, 0.04) m, moving 0.37 m/s (vx -0.37, vy +0.00, vz -0.00); touching floor | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
6.00 s: ball1 at (-0.11, 0.00, 0.04) m, moving 0.47 m/s (vx -0.47, vy -0.00, vz -0.00); touching floor | ball2 at (0.09, 0.00, 0.04) m, moving 0.37 m/s (vx -0.37, vy +0.00, vz -0.00); touching floor | ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base

At the end (6.00 s):
- ball1 at (-0.11, 0.00, 0.04) m, moving 0.47 m/s (vx -0.47, vy -0.00, vz -0.00); touching floor
- ball2 at (0.09, 0.00, 0.04) m, moving 0.37 m/s (vx -0.37, vy +0.00, vz -0.00); touching floor
- ball3 at (1.49, 0.00, 0.04) m, at rest; touching cup_base
</history>
