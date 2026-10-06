Your expectations, checked against the run (1 of 4 hold):

- holds: ball1 touches ball2 (first touch at 0.06 s)
- DOES NOT HOLD: ball2 touches ball3 (they never touch)
- DOES NOT HOLD: ball3 touches ramp (they never touch)
- DOES NOT HOLD: ball3 comes to rest in cup (ball3 comes to rest at (0.60, 0.00, 0.03) m, outside cup)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_geom; starts at (0.00, 0.00, 0.03) m, moving 4.00 m/s (vx +4.00, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2_geom; starts at (0.30, 0.00, 0.03) m, at rest
- ball3: free body; its geoms: ball3_geom; starts at (0.60, 0.00, 0.03) m, at rest

What happened, in order:
 0.00 s  ball1_geom starts touching floor
 0.00 s  ball2_geom starts touching floor
 0.00 s  ball3_geom starts touching floor
 0.06 s  ball1 passes 0.30 m from ball3 (ball3_geom) without touching it: nearest points (0.27, 0.00, 0.03) m and (0.57, 0.00, 0.03) m
 0.06 s  ball1_geom leaves floor
 0.06 s  ball2_geom leaves floor
 0.06 s  ball1_geom first touches ball2_geom
 0.06 s  ball1_geom leaves ball2_geom
 0.06 s  ball2 starts moving
 0.07 s  ball2 passes 0.02 m from ball3 (ball3_geom) without touching it: nearest points (0.57, 0.00, 0.07) m and (0.58, 0.00, 0.05) m
 0.08 s  ball2 passes 0.18 m from ramp without touching it: nearest points (0.89, 0.00, 0.14) m and (1.00, 0.00, 0.00) m
 0.10 s  ball2 passes 0.24 m from platform without touching it: nearest points (1.51, 0.00, 0.29) m and (1.50, 0.00, 0.05) m
 0.10 s  ball2 passes 0.17 m from cup (cup_left) without touching it: nearest points (1.51, 0.02, 0.29) m and (1.51, 0.10, 0.15) m
 0.86 s  ball2 is at the top of its flight, at (25.72, 0.00, 3.13) m
 0.97 s  ball1 is at the top of its flight, at (-26.90, 0.00, 4.07) m
 1.66 s  ball2_geom touches floor again
 1.67 s  ball2_geom leaves floor
 1.88 s  ball1_geom touches floor again
 1.90 s  ball1_geom leaves floor
 1.95 s  ball2 is at the top of its flight, at (58.49, 0.00, 0.40) m
 2.22 s  ball2_geom touches floor again
 2.24 s  ball2_geom leaves floor
 2.25 s  ball1 is at the top of its flight, at (-62.03, 0.00, 0.62) m
 2.35 s  ball2 is at the top of its flight, at (68.51, 0.00, 0.08) m
 2.45 s  ball2_geom touches floor again
 2.47 s  ball2_geom leaves floor
 2.55 s  ball2_geom touches floor 1 more times between 2.55 s and 6.00 s, still touching at the end
 2.59 s  ball1_geom touches floor again
 2.61 s  ball1_geom leaves floor
 2.72 s  ball1 is at the top of its flight, at (-72.52, 0.00, 0.09) m
 2.83 s  ball1_geom touches floor again
 2.85 s  ball1_geom leaves floor
 2.92 s  ball1_geom touches floor 1 more times between 2.92 s and 6.00 s, still touching at the end
 6.00 s  ball1 is still moving at the end, 24.02 m/s
 6.00 s  ball2 is still moving at the end, 26.94 m/s

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.03) m, moving 4.00 m/s (vx +4.00, vy +0.00, vz +0.00); touching floor | ball2 at (0.30, 0.00, 0.03) m, at rest; touching floor | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
0.25 s: ball1 at (-5.31, 0.00, 1.52) m, moving 30.72 m/s (vx -29.90, vy -0.00, vz +7.07); touching nothing | ball2 at (6.24, 0.00, 1.31) m, moving 32.49 m/s (vx +31.93, vy +0.00, vz +5.97); touching nothing | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
0.50 s: ball1 at (-12.79, 0.00, 2.98) m, moving 30.25 m/s (vx -29.90, vy -0.00, vz +4.61); touching nothing | ball2 at (14.22, 0.00, 2.50) m, moving 32.13 m/s (vx +31.93, vy +0.00, vz +3.52); touching nothing | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
0.75 s: ball1 at (-20.26, 0.00, 3.83) m, moving 29.98 m/s (vx -29.90, vy -0.00, vz +2.16); touching nothing | ball2 at (22.21, 0.00, 3.08) m, moving 31.95 m/s (vx +31.93, vy +0.00, vz +1.06); touching nothing | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
1.00 s: ball1 at (-27.74, 0.00, 4.06) m, moving 29.90 m/s (vx -29.90, vy -0.00, vz -0.29); touching nothing | ball2 at (30.19, 0.00, 3.04) m, moving 31.96 m/s (vx +31.93, vy +0.00, vz -1.39); touching nothing | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
1.25 s: ball1 at (-35.21, 0.00, 3.69) m, moving 30.02 m/s (vx -29.90, vy -0.00, vz -2.74); touching nothing | ball2 at (38.17, 0.00, 2.39) m, moving 32.16 m/s (vx +31.93, vy +0.00, vz -3.84); touching nothing | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
1.50 s: ball1 at (-42.68, 0.00, 2.70) m, moving 30.35 m/s (vx -29.90, vy -0.00, vz -5.20); touching nothing | ball2 at (46.16, 0.00, 1.12) m, moving 32.55 m/s (vx +31.93, vy +0.00, vz -6.29); touching nothing | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
1.75 s: ball1 at (-50.16, 0.00, 1.09) m, moving 30.86 m/s (vx -29.90, vy -0.00, vz -7.65); touching nothing | ball2 at (53.50, 0.00, 0.20) m, moving 25.01 m/s (vx +24.94, vy -0.00, vz +1.94); touching nothing | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
2.00 s: ball1 at (-56.67, 0.00, 0.32) m, moving 21.90 m/s (vx -21.77, vy +0.00, vz +2.39); touching nothing | ball2 at (59.73, 0.00, 0.39) m, moving 24.94 m/s (vx +24.94, vy -0.00, vz -0.51); touching nothing | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
2.25 s: ball1 at (-62.11, 0.00, 0.62) m, moving 21.77 m/s (vx -21.77, vy +0.00, vz -0.06); touching nothing | ball2 at (65.99, 0.00, 0.04) m, moving 26.22 m/s (vx +26.21, vy -0.00, vz +0.94); touching nothing | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
2.50 s: ball1 at (-67.56, 0.00, 0.30) m, moving 21.91 m/s (vx -21.77, vy +0.00, vz -2.51); touching nothing | ball2 at (72.56, 0.00, 0.04) m, moving 26.67 m/s (vx +26.67, vy -0.00, vz +0.08); touching nothing | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
2.75 s: ball1 at (-73.22, 0.00, 0.08) m, moving 23.23 m/s (vx -23.23, vy +0.00, vz -0.31); touching nothing | ball2 at (79.28, 0.00, 0.03) m, moving 26.94 m/s (vx +26.94, vy -0.00, vz +0.00); touching floor | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
3.00 s: ball1 at (-79.14, 0.00, 0.03) m, moving 24.02 m/s (vx -24.02, vy +0.00, vz -0.00); touching floor | ball2 at (86.02, 0.00, 0.03) m, moving 26.94 m/s (vx +26.94, vy -0.00, vz -0.00); touching floor | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
3.25 s: ball1 at (-85.15, 0.00, 0.03) m, moving 24.02 m/s (vx -24.02, vy +0.00, vz -0.00); touching floor | ball2 at (92.75, 0.00, 0.03) m, moving 26.94 m/s (vx +26.94, vy -0.00, vz -0.00); touching floor | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
3.50 s: ball1 at (-91.15, 0.00, 0.03) m, moving 24.02 m/s (vx -24.02, vy +0.00, vz +0.00); touching floor | ball2 at (99.49, 0.00, 0.03) m, moving 26.94 m/s (vx +26.94, vy -0.00, vz +0.00); touching floor | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
3.75 s: ball1 at (-97.16, 0.00, 0.03) m, moving 24.02 m/s (vx -24.02, vy +0.00, vz -0.00); touching floor | ball2 at (106.23, 0.00, 0.03) m, moving 26.94 m/s (vx +26.94, vy -0.00, vz +0.00); touching floor | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
4.00 s: ball1 at (-103.16, 0.00, 0.03) m, moving 24.02 m/s (vx -24.02, vy +0.00, vz -0.00); touching floor | ball2 at (112.96, 0.00, 0.03) m, moving 26.94 m/s (vx +26.94, vy -0.00, vz -0.00); touching floor | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
4.25 s: ball1 at (-109.17, 0.00, 0.03) m, moving 24.02 m/s (vx -24.02, vy +0.00, vz -0.00); touching floor | ball2 at (119.70, 0.00, 0.03) m, moving 26.94 m/s (vx +26.94, vy -0.00, vz -0.00); touching floor | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
4.50 s: ball1 at (-115.17, 0.00, 0.03) m, moving 24.02 m/s (vx -24.02, vy +0.00, vz +0.00); touching floor | ball2 at (126.43, 0.00, 0.03) m, moving 26.94 m/s (vx +26.94, vy -0.00, vz +0.00); touching floor | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
4.75 s: ball1 at (-121.18, 0.00, 0.03) m, moving 24.02 m/s (vx -24.02, vy +0.00, vz -0.00); touching floor | ball2 at (133.17, 0.00, 0.03) m, moving 26.94 m/s (vx +26.94, vy -0.00, vz -0.00); touching floor | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
5.00 s: ball1 at (-127.19, 0.00, 0.03) m, moving 24.02 m/s (vx -24.02, vy +0.00, vz -0.00); touching floor | ball2 at (139.91, 0.00, 0.03) m, moving 26.94 m/s (vx +26.94, vy -0.00, vz -0.00); touching floor | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
5.25 s: ball1 at (-133.19, 0.00, 0.03) m, moving 24.02 m/s (vx -24.02, vy +0.00, vz +0.00); touching floor | ball2 at (146.64, 0.00, 0.03) m, moving 26.94 m/s (vx +26.94, vy -0.00, vz -0.00); touching floor | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
5.50 s: ball1 at (-139.20, 0.00, 0.03) m, moving 24.02 m/s (vx -24.02, vy +0.00, vz -0.00); touching floor | ball2 at (153.38, 0.00, 0.03) m, moving 26.94 m/s (vx +26.94, vy -0.00, vz -0.00); touching floor | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
5.75 s: ball1 at (-145.20, 0.00, 0.03) m, moving 24.02 m/s (vx -24.02, vy +0.00, vz -0.00); touching floor | ball2 at (160.11, 0.00, 0.03) m, moving 26.94 m/s (vx +26.94, vy -0.00, vz +0.00); touching floor | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
6.00 s: ball1 at (-151.21, 0.00, 0.03) m, moving 24.02 m/s (vx -24.02, vy +0.00, vz -0.00); touching floor | ball2 at (166.85, 0.00, 0.03) m, moving 26.94 m/s (vx +26.94, vy -0.00, vz +0.00); touching floor | ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor

At the end (6.00 s):
- ball1 at (-151.21, 0.00, 0.03) m, moving 24.02 m/s (vx -24.02, vy +0.00, vz -0.00); touching floor
- ball2 at (166.85, 0.00, 0.03) m, moving 26.94 m/s (vx +26.94, vy -0.00, vz +0.00); touching floor
- ball3 at (0.60, 0.00, 0.03) m, at rest; touching floor
</history>
