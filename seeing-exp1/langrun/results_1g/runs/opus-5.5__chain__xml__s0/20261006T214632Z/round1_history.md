Your expectations, checked against the run (5 of 5 hold):

- holds: ball1 touches ball2 (first touch at 0.07 s)
- holds: ball2 touches ball3 (first touch at 0.16 s)
- holds: ball3 touches ramp (first touch at 0.34 s)
- holds: ball3 touches cup (first touch at 0.48 s)
- holds: ball3 comes to rest in cup (ball3 at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_geom; starts at (0.00, 0.00, 0.03) m, moving 3.50 m/s (vx +3.50, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2_geom; starts at (0.30, 0.00, 0.03) m, at rest
- ball3: free body; its geoms: ball3_geom; starts at (0.60, 0.00, 0.03) m, at rest

What happened, in order:
 0.00 s  ball1_geom starts touching floor
 0.00 s  ball2_geom starts touching floor
 0.00 s  ball3_geom starts touching floor
 0.07 s  ball1_geom leaves floor
 0.07 s  ball1_geom first touches ball2_geom
 0.07 s  ball2 starts moving
 0.07 s  ball2_geom leaves floor
 0.08 s  ball1_geom leaves ball2_geom
 0.08 s  ball1 passes 0.29 m from ball3 (ball3_geom) without touching it: nearest points (0.28, 0.00, 0.03) m and (0.57, 0.00, 0.03) m
 0.14 s  ball1 is at the top of its flight, at (0.24, 0.00, 0.05) m
 0.15 s  ball2_geom touches floor again
 0.16 s  ball2_geom first touches ball3_geom
 0.16 s  ball3 starts moving
 0.16 s  ball3_geom leaves floor
 0.17 s  ball2_geom leaves ball3_geom
 0.17 s  ball2_geom leaves floor
 0.21 s  ball1_geom touches floor again
 0.25 s  ball2_geom touches floor again
 0.26 s  ball3_geom touches floor again
 0.34 s  ball3_geom first touches ramp_geom
 0.34 s  ball3_geom leaves floor
 0.48 s  ball3_geom first touches cup_front
 0.49 s  ball3_geom leaves ramp_geom
 0.49 s  ball3_geom leaves cup_front
 0.51 s  ball3 is at the top of its flight, at (1.33, 0.00, 0.07) m
 0.61 s  ball3_geom first touches cup_base
 0.61 s  ball3_geom touches floor again
 0.64 s  ball3_geom first touches cup_back
 0.64 s  ball3_geom leaves floor
 0.65 s  ball3_geom leaves cup_base
 0.71 s  ball3_geom leaves cup_back
 0.77 s  ball3_geom touches cup_base again
 1.35 s  ball2_geom first touches ramp_geom
 1.37 s  ball2_geom leaves floor
 1.73 s  ball1_geom first touches ramp_geom
 1.74 s  ball1_geom leaves floor
 1.76 s  ball1_geom touches ball2_geom again
 1.76 s  ball1 passes 0.24 m from cup (cup_front) without touching it: nearest points (1.04, 0.00, 0.03) m and (1.28, 0.00, 0.03) m
 1.76 s  ball1_geom leaves ball2_geom
 1.93 s  ball1_geom touches floor again
 1.96 s  ball1_geom leaves ramp_geom
 2.14 s  ball2 passes 0.11 m from cup (cup_front) without touching it: nearest points (1.17, 0.00, 0.05) m and (1.28, 0.00, 0.04) m
 2.51 s  ball3_geom touches cup_front again
 2.52 s  ball3 comes to rest at (1.33, 0.00, 0.03) m
 2.59 s  ball3_geom leaves cup_front
 2.69 s  ball2_geom touches floor again
 2.70 s  ball2_geom leaves ramp_geom
 2.81 s  ball1_geom touches ball2_geom again
 2.82 s  ball1_geom leaves ball2_geom
 6.00 s  ball1 is still moving at the end, 0.43 m/s
 6.00 s  ball2 is still moving at the end, 0.12 m/s

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.03) m, moving 3.50 m/s (vx +3.50, vy +0.00, vz +0.00); touching floor | ball2 at (0.30, 0.00, 0.03) m, at rest; touching floor | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
0.25 s: ball1 at (0.25, 0.00, 0.03) m, moving 0.50 m/s (vx +0.49, vy +0.00, vz +0.09); touching floor | ball2 at (0.57, 0.00, 0.03) m, moving 0.49 m/s (vx +0.28, vy +0.00, vz -0.40); touching nothing | ball3 at (0.81, 0.00, 0.03) m, moving 2.49 m/s (vx +2.46, vy -0.00, vz -0.39); touching nothing
0.50 s: ball1 at (0.38, 0.00, 0.03) m, moving 0.51 m/s (vx +0.51, vy +0.00, vz +0.00); touching floor | ball2 at (0.67, 0.00, 0.03) m, moving 0.39 m/s (vx +0.39, vy -0.00, vz -0.00); touching floor | ball3 at (1.31, 0.00, 0.07) m, moving 1.85 m/s (vx +1.85, vy -0.00, vz +0.13); touching nothing
0.75 s: ball1 at (0.50, 0.00, 0.03) m, moving 0.51 m/s (vx +0.51, vy +0.00, vz +0.00); touching floor | ball2 at (0.76, 0.00, 0.03) m, moving 0.39 m/s (vx +0.39, vy -0.00, vz +0.00); touching floor | ball3 at (1.56, 0.00, 0.04) m, moving 0.46 m/s (vx -0.31, vy -0.00, vz -0.34); touching nothing
1.00 s: ball1 at (0.63, 0.00, 0.03) m, moving 0.51 m/s (vx +0.51, vy +0.00, vz +0.00); touching floor | ball2 at (0.86, 0.00, 0.03) m, moving 0.39 m/s (vx +0.39, vy -0.00, vz +0.00); touching floor | ball3 at (1.52, 0.00, 0.03) m, moving 0.13 m/s (vx -0.13, vy -0.00, vz -0.00); touching cup_base
1.25 s: ball1 at (0.75, 0.00, 0.03) m, moving 0.51 m/s (vx +0.51, vy +0.00, vz -0.00); touching floor | ball2 at (0.96, 0.00, 0.03) m, moving 0.39 m/s (vx +0.39, vy -0.00, vz +0.00); touching floor | ball3 at (1.49, 0.00, 0.03) m, moving 0.13 m/s (vx -0.13, vy -0.00, vz -0.00); touching cup_base
1.50 s: ball1 at (0.88, 0.00, 0.03) m, moving 0.51 m/s (vx +0.51, vy +0.00, vz -0.00); touching floor | ball2 at (1.04, 0.00, 0.04) m, moving 0.24 m/s (vx +0.23, vy -0.00, vz +0.03); touching ramp_geom | ball3 at (1.46, 0.00, 0.03) m, moving 0.13 m/s (vx -0.13, vy +0.00, vz +0.00); touching cup_base
1.75 s: ball1 at (1.01, 0.00, 0.03) m, moving 0.48 m/s (vx +0.47, vy +0.00, vz +0.07); touching ramp_geom | ball2 at (1.07, 0.00, 0.04) m, at rest; touching ramp_geom | ball3 at (1.42, 0.00, 0.03) m, moving 0.13 m/s (vx -0.13, vy +0.00, vz +0.00); touching cup_base
2.00 s: ball1 at (0.99, 0.00, 0.03) m, moving 0.14 m/s (vx -0.14, vy +0.00, vz -0.00); touching floor | ball2 at (1.13, 0.00, 0.05) m, moving 0.14 m/s (vx +0.14, vy -0.00, vz +0.02); touching ramp_geom | ball3 at (1.39, 0.00, 0.03) m, moving 0.13 m/s (vx -0.13, vy +0.00, vz +0.00); touching cup_base
2.25 s: ball1 at (0.96, 0.00, 0.03) m, moving 0.14 m/s (vx -0.14, vy +0.00, vz -0.00); touching floor | ball2 at (1.14, 0.00, 0.05) m, moving 0.10 m/s (vx -0.10, vy -0.00, vz -0.01); touching ramp_geom | ball3 at (1.36, 0.00, 0.03) m, moving 0.13 m/s (vx -0.13, vy +0.00, vz +0.00); touching cup_base
2.50 s: ball1 at (0.92, 0.00, 0.03) m, moving 0.14 m/s (vx -0.14, vy +0.00, vz +0.00); touching floor | ball2 at (1.08, 0.00, 0.04) m, moving 0.35 m/s (vx -0.34, vy -0.00, vz -0.05); touching ramp_geom | ball3 at (1.33, 0.00, 0.03) m, moving 0.13 m/s (vx -0.13, vy +0.00, vz +0.00); touching cup_base
2.75 s: ball1 at (0.88, 0.00, 0.03) m, moving 0.14 m/s (vx -0.14, vy +0.00, vz +0.00); touching floor | ball2 at (0.97, 0.00, 0.03) m, moving 0.52 m/s (vx -0.52, vy -0.00, vz +0.00); touching floor | ball3 at (1.33, 0.00, 0.03) m, at rest; touching cup_base
3.00 s: ball1 at (0.79, 0.00, 0.03) m, moving 0.43 m/s (vx -0.43, vy +0.00, vz +0.00); touching floor | ball2 at (0.91, 0.00, 0.03) m, moving 0.12 m/s (vx -0.12, vy -0.00, vz -0.00); touching floor | ball3 at (1.33, 0.00, 0.03) m, at rest; touching cup_base
3.25 s: ball1 at (0.68, 0.00, 0.03) m, moving 0.43 m/s (vx -0.43, vy +0.00, vz -0.00); touching floor | ball2 at (0.88, 0.00, 0.03) m, moving 0.12 m/s (vx -0.12, vy -0.00, vz -0.00); touching floor | ball3 at (1.34, 0.00, 0.03) m, at rest; touching cup_base
3.50 s: ball1 at (0.58, 0.00, 0.03) m, moving 0.43 m/s (vx -0.43, vy +0.00, vz -0.00); touching floor | ball2 at (0.85, 0.00, 0.03) m, moving 0.12 m/s (vx -0.12, vy -0.00, vz -0.00); touching floor | ball3 at (1.34, 0.00, 0.03) m, at rest; touching cup_base
3.75 s: ball1 at (0.47, 0.00, 0.03) m, moving 0.43 m/s (vx -0.43, vy +0.00, vz +0.00); touching floor | ball2 at (0.82, 0.00, 0.03) m, moving 0.12 m/s (vx -0.12, vy -0.00, vz +0.00); touching floor | ball3 at (1.34, 0.00, 0.03) m, at rest; touching cup_base
4.00 s: ball1 at (0.36, 0.00, 0.03) m, moving 0.43 m/s (vx -0.43, vy +0.00, vz -0.00); touching floor | ball2 at (0.79, 0.00, 0.03) m, moving 0.12 m/s (vx -0.12, vy -0.00, vz +0.00); touching floor | ball3 at (1.35, 0.00, 0.03) m, at rest; touching cup_base
4.25 s: ball1 at (0.25, 0.00, 0.03) m, moving 0.43 m/s (vx -0.43, vy +0.00, vz +0.00); touching floor | ball2 at (0.76, 0.00, 0.03) m, moving 0.12 m/s (vx -0.12, vy -0.00, vz +0.00); touching floor | ball3 at (1.35, 0.00, 0.03) m, at rest; touching cup_base
4.50 s: ball1 at (0.14, 0.00, 0.03) m, moving 0.43 m/s (vx -0.43, vy +0.00, vz +0.00); touching floor | ball2 at (0.72, 0.00, 0.03) m, moving 0.12 m/s (vx -0.12, vy -0.00, vz -0.00); touching floor | ball3 at (1.35, 0.00, 0.03) m, at rest; touching cup_base
4.75 s: ball1 at (0.03, 0.00, 0.03) m, moving 0.43 m/s (vx -0.43, vy +0.00, vz -0.00); touching floor | ball2 at (0.69, 0.00, 0.03) m, moving 0.12 m/s (vx -0.12, vy -0.00, vz -0.00); touching floor | ball3 at (1.35, 0.00, 0.03) m, at rest; touching cup_base
5.00 s: ball1 at (-0.07, 0.00, 0.03) m, moving 0.43 m/s (vx -0.43, vy +0.00, vz +0.00); touching floor | ball2 at (0.66, 0.00, 0.03) m, moving 0.12 m/s (vx -0.12, vy -0.00, vz -0.00); touching floor | ball3 at (1.36, 0.00, 0.03) m, at rest; touching cup_base
5.25 s: ball1 at (-0.18, 0.00, 0.03) m, moving 0.43 m/s (vx -0.43, vy +0.00, vz +0.00); touching floor | ball2 at (0.63, 0.00, 0.03) m, moving 0.12 m/s (vx -0.12, vy -0.00, vz +0.00); touching floor | ball3 at (1.36, 0.00, 0.03) m, at rest; touching cup_base
5.50 s: ball1 at (-0.29, 0.00, 0.03) m, moving 0.43 m/s (vx -0.43, vy +0.00, vz -0.00); touching floor | ball2 at (0.60, 0.00, 0.03) m, moving 0.12 m/s (vx -0.12, vy -0.00, vz +0.00); touching floor | ball3 at (1.36, 0.00, 0.03) m, at rest; touching cup_base
5.75 s: ball1 at (-0.40, 0.00, 0.03) m, moving 0.43 m/s (vx -0.43, vy +0.00, vz +0.00); touching floor | ball2 at (0.57, 0.00, 0.03) m, moving 0.12 m/s (vx -0.12, vy -0.00, vz -0.00); touching floor | ball3 at (1.37, 0.00, 0.03) m, at rest; touching cup_base
6.00 s: ball1 at (-0.51, 0.00, 0.03) m, moving 0.43 m/s (vx -0.43, vy +0.00, vz +0.00); touching floor | ball2 at (0.54, 0.00, 0.03) m, moving 0.12 m/s (vx -0.12, vy -0.00, vz -0.00); touching floor | ball3 at (1.37, 0.00, 0.03) m, at rest; touching cup_base

At the end (6.00 s):
- ball1 at (-0.51, 0.00, 0.03) m, moving 0.43 m/s (vx -0.43, vy +0.00, vz +0.00); touching floor
- ball2 at (0.54, 0.00, 0.03) m, moving 0.12 m/s (vx -0.12, vy -0.00, vz -0.00); touching floor
- ball3 at (1.37, 0.00, 0.03) m, at rest; touching cup_base
</history>
