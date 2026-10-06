MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_geom; starts at (0.00, 0.00, 0.03) m, moving 1.20 m/s (vx +1.20, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2_geom; starts at (0.20, 0.00, 0.03) m, at rest
- ball3: free body; its geoms: ball3_geom; starts at (0.40, 0.00, 0.03) m, at rest

What happened, in order:
 0.00 s  ball1_geom starts touching floor
 0.00 s  ball2_geom starts touching floor
 0.00 s  ball3_geom starts touching floor
 0.12 s  ball1_geom first touches ball2_geom
 0.12 s  ball2 starts moving
 0.13 s  ball1_geom leaves ball2_geom
 0.27 s  ball2_geom first touches ball3_geom
 0.27 s  ball1 passes 0.16 m from ball3 (ball3_geom) without touching it: nearest points (0.21, 0.00, 0.03) m and (0.37, 0.00, 0.03) m
 0.27 s  ball3 starts moving
 0.28 s  ball2_geom leaves ball3_geom
 1.22 s  ball3_geom first touches cup_bottom
 1.44 s  ball3_geom first touches cup_back
 1.46 s  ball3 comes to rest at (1.21, 0.00, 0.03) m
 1.55 s  ball3_geom leaves cup_back
 1.68 s  ball1_geom touches ball2_geom again
 1.69 s  ball1_geom leaves ball2_geom
 4.98 s  ball2_geom first touches cup_bottom
 5.03 s  ball2 comes to rest at (1.10, 0.00, 0.03) m
 6.00 s  ball1 is still moving at the end, 0.08 m/s
 6.00 s  ball1 passes 0.13 m from cup (cup_bottom) without touching it: nearest points (0.97, 0.00, 0.02) m and (1.10, 0.00, 0.00) m

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.03) m, moving 1.20 m/s (vx +1.20, vy +0.00, vz +0.00); touching floor | ball2 at (0.20, 0.00, 0.03) m, at rest; touching floor | ball3 at (0.40, 0.00, 0.03) m, at rest; touching floor
0.25 s: ball1 at (0.17, 0.00, 0.03) m, moving 0.25 m/s (vx +0.25, vy -0.00, vz +0.00); touching floor | ball2 at (0.32, 0.00, 0.03) m, moving 0.93 m/s (vx +0.93, vy -0.00, vz +0.00); touching floor | ball3 at (0.40, 0.00, 0.03) m, at rest; touching floor
0.50 s: ball1 at (0.23, 0.00, 0.03) m, moving 0.24 m/s (vx +0.24, vy +0.00, vz -0.00); touching floor | ball2 at (0.38, 0.00, 0.03) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz +0.00); touching floor | ball3 at (0.57, 0.00, 0.03) m, moving 0.75 m/s (vx +0.75, vy +0.00, vz +0.00); touching floor
0.75 s: ball1 at (0.29, 0.00, 0.03) m, moving 0.23 m/s (vx +0.23, vy +0.00, vz -0.00); touching floor | ball2 at (0.42, 0.00, 0.03) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz +0.00); touching floor | ball3 at (0.76, 0.00, 0.03) m, moving 0.73 m/s (vx +0.73, vy +0.00, vz -0.00); touching floor
1.00 s: ball1 at (0.35, 0.00, 0.03) m, moving 0.22 m/s (vx +0.22, vy +0.00, vz -0.00); touching floor | ball2 at (0.46, 0.00, 0.03) m, moving 0.15 m/s (vx +0.15, vy -0.00, vz +0.00); touching floor | ball3 at (0.94, 0.00, 0.03) m, moving 0.72 m/s (vx +0.72, vy +0.00, vz -0.00); touching floor
1.25 s: ball1 at (0.41, 0.00, 0.03) m, moving 0.22 m/s (vx +0.22, vy +0.00, vz -0.00); touching floor | ball2 at (0.49, 0.00, 0.03) m, moving 0.15 m/s (vx +0.15, vy -0.00, vz +0.00); touching floor | ball3 at (1.12, 0.00, 0.03) m, moving 0.67 m/s (vx +0.67, vy +0.00, vz -0.01); touching nothing
1.50 s: ball1 at (0.46, 0.00, 0.03) m, moving 0.21 m/s (vx +0.21, vy +0.00, vz -0.00); touching floor | ball2 at (0.53, 0.00, 0.03) m, moving 0.14 m/s (vx +0.14, vy -0.00, vz +0.00); touching floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_back, cup_bottom, floor
1.75 s: ball1 at (0.51, 0.00, 0.03) m, moving 0.14 m/s (vx +0.14, vy +0.00, vz -0.00); touching floor | ball2 at (0.57, 0.00, 0.03) m, moving 0.20 m/s (vx +0.20, vy -0.00, vz -0.00); touching floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor
2.00 s: ball1 at (0.54, 0.00, 0.03) m, moving 0.13 m/s (vx +0.13, vy +0.00, vz -0.00); touching floor | ball2 at (0.62, 0.00, 0.03) m, moving 0.20 m/s (vx +0.20, vy -0.00, vz -0.00); touching floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor
2.25 s: ball1 at (0.57, 0.00, 0.03) m, moving 0.13 m/s (vx +0.13, vy +0.00, vz -0.00); touching floor | ball2 at (0.67, 0.00, 0.03) m, moving 0.19 m/s (vx +0.19, vy -0.00, vz -0.00); touching floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor
2.50 s: ball1 at (0.60, 0.00, 0.03) m, moving 0.12 m/s (vx +0.12, vy +0.00, vz -0.00); touching floor | ball2 at (0.71, 0.00, 0.03) m, moving 0.18 m/s (vx +0.18, vy -0.00, vz -0.00); touching floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor
2.75 s: ball1 at (0.63, 0.00, 0.03) m, moving 0.12 m/s (vx +0.12, vy +0.00, vz -0.00); touching floor | ball2 at (0.76, 0.00, 0.03) m, moving 0.18 m/s (vx +0.18, vy -0.00, vz -0.00); touching floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor
3.00 s: ball1 at (0.66, 0.00, 0.03) m, moving 0.12 m/s (vx +0.12, vy +0.00, vz -0.00); touching floor | ball2 at (0.80, 0.00, 0.03) m, moving 0.17 m/s (vx +0.17, vy -0.00, vz -0.00); touching floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor
3.25 s: ball1 at (0.69, 0.00, 0.03) m, moving 0.11 m/s (vx +0.11, vy +0.00, vz -0.00); touching floor | ball2 at (0.84, 0.00, 0.03) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz -0.00); touching floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor
3.50 s: ball1 at (0.72, 0.00, 0.03) m, moving 0.11 m/s (vx +0.11, vy +0.00, vz -0.00); touching floor | ball2 at (0.88, 0.00, 0.03) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz -0.00); touching floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor
3.75 s: ball1 at (0.75, 0.00, 0.03) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz -0.00); touching floor | ball2 at (0.92, 0.00, 0.03) m, moving 0.15 m/s (vx +0.15, vy -0.00, vz -0.00); touching floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor
4.00 s: ball1 at (0.77, 0.00, 0.03) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz -0.00); touching floor | ball2 at (0.96, 0.00, 0.03) m, moving 0.15 m/s (vx +0.15, vy -0.00, vz -0.00); touching floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor
4.25 s: ball1 at (0.80, 0.00, 0.03) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz -0.00); touching floor | ball2 at (1.00, 0.00, 0.03) m, moving 0.14 m/s (vx +0.14, vy -0.00, vz -0.00); touching floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor
4.50 s: ball1 at (0.82, 0.00, 0.03) m, moving 0.09 m/s (vx +0.09, vy +0.00, vz -0.00); touching floor | ball2 at (1.03, 0.00, 0.03) m, moving 0.14 m/s (vx +0.14, vy -0.00, vz -0.00); touching floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor
4.75 s: ball1 at (0.84, 0.00, 0.03) m, moving 0.09 m/s (vx +0.09, vy +0.00, vz -0.00); touching floor | ball2 at (1.07, 0.00, 0.03) m, moving 0.13 m/s (vx +0.13, vy -0.00, vz -0.00); touching floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor
5.00 s: ball1 at (0.86, 0.00, 0.03) m, moving 0.09 m/s (vx +0.09, vy +0.00, vz -0.00); touching floor | ball2 at (1.10, 0.00, 0.03) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz +0.00); touching cup_bottom, floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor
5.25 s: ball1 at (0.89, 0.00, 0.03) m, moving 0.08 m/s (vx +0.08, vy +0.00, vz -0.00); touching floor | ball2 at (1.10, 0.00, 0.03) m, at rest; touching cup_bottom, floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor
5.50 s: ball1 at (0.91, 0.00, 0.03) m, moving 0.08 m/s (vx +0.08, vy +0.00, vz -0.00); touching floor | ball2 at (1.10, 0.00, 0.03) m, at rest; touching cup_bottom, floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor
5.75 s: ball1 at (0.93, 0.00, 0.03) m, moving 0.08 m/s (vx +0.08, vy +0.00, vz -0.00); touching floor | ball2 at (1.10, 0.00, 0.03) m, at rest; touching cup_bottom, floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor
6.00 s: ball1 at (0.95, 0.00, 0.03) m, moving 0.08 m/s (vx +0.08, vy +0.00, vz -0.00); touching floor | ball2 at (1.10, 0.00, 0.03) m, at rest; touching cup_bottom, floor | ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor

At the end (6.00 s):
- ball1 at (0.95, 0.00, 0.03) m, moving 0.08 m/s (vx +0.08, vy +0.00, vz -0.00); touching floor
- ball2 at (1.10, 0.00, 0.03) m, at rest; touching cup_bottom, floor
- ball3 at (1.21, 0.00, 0.03) m, at rest; touching cup_bottom, floor
</history>
