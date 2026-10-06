MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_geom; starts at (0.00, 0.00, 0.03) m, moving 1.50 m/s (vx +1.50, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2_geom; starts at (0.25, 0.00, 0.03) m, at rest
- ball3: free body; its geoms: ball3_geom; starts at (0.50, 0.00, 0.03) m, at rest

What happened, in order:
 0.00 s  ball1_geom starts touching floor
 0.00 s  ball2_geom starts touching floor
 0.00 s  ball3_geom starts touching floor
 0.12 s  ball1 passes 0.26 m from ball3 (ball3_geom) without touching it: nearest points (0.21, 0.00, 0.03) m and (0.47, 0.00, 0.03) m
 0.13 s  ball1_geom leaves floor
 0.13 s  ball2_geom leaves floor
 0.13 s  ball1_geom first touches ball2_geom
 0.13 s  ball1_geom leaves ball2_geom
 0.13 s  ball2 starts moving
 0.15 s  ball2 passes 0.08 m from cup (cup_wall_000) without touching it: nearest points (0.93, 0.00, 0.19) m and (0.93, 0.00, 0.11) m
 1.03 s  ball2 is at the top of its flight, at (27.97, 0.00, 3.99) m
 1.05 s  ball1 is at the top of its flight, at (-27.67, 0.00, 4.17) m
 1.93 s  ball2_geom touches floor again
 1.95 s  ball2_geom leaves floor
 1.97 s  ball1_geom touches floor again
 1.99 s  ball1_geom leaves floor
 2.27 s  ball2 is at the top of its flight, at (63.18, 0.00, 0.52) m
 2.35 s  ball1 is at the top of its flight, at (-63.42, 0.00, 0.67) m
 2.58 s  ball2_geom touches floor again
 2.63 s  ball2_geom leaves floor
 2.72 s  ball1_geom touches floor again
 2.76 s  ball1_geom leaves floor
 2.79 s  ball2 is at the top of its flight, at (74.50, 0.00, 0.15) m
 2.94 s  ball1 is at the top of its flight, at (-75.30, 0.00, 0.18) m
 2.94 s  ball2_geom touches floor again
 3.00 s  ball2_geom leaves floor
 3.06 s  ball2 is at the top of its flight, at (80.54, 0.00, 0.05) m
 3.11 s  ball1_geom touches floor again
 3.12 s  ball2_geom touches floor 1 more times between 3.12 s and 6.00 s, still touching at the end
 3.17 s  ball1_geom leaves floor
 3.25 s  ball1 is at the top of its flight, at (-81.67, 0.00, 0.06) m
 3.33 s  ball1_geom touches floor 1 more times between 3.33 s and 6.00 s, still touching at the end
 6.00 s  ball1 is still moving at the end, 22.13 m/s
 6.00 s  ball2 is still moving at the end, 23.60 m/s

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.03) m, moving 1.50 m/s (vx +1.50, vy +0.00, vz +0.00); touching floor | ball2 at (0.25, 0.00, 0.03) m, at rest; touching floor | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
0.25 s: ball1 at (-3.44, 0.00, 1.04) m, moving 31.28 m/s (vx -30.28, vy -0.00, vz +7.83); touching nothing | ball2 at (3.95, 0.00, 1.02) m, moving 31.79 m/s (vx +30.87, vy -0.00, vz +7.63); touching nothing | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
0.50 s: ball1 at (-11.01, 0.00, 2.69) m, moving 30.76 m/s (vx -30.28, vy -0.00, vz +5.38); touching nothing | ball2 at (11.67, 0.00, 2.62) m, moving 31.30 m/s (vx +30.87, vy -0.00, vz +5.18); touching nothing | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
0.75 s: ball1 at (-18.58, 0.00, 3.74) m, moving 30.42 m/s (vx -30.28, vy -0.00, vz +2.93); touching nothing | ball2 at (19.39, 0.00, 3.61) m, moving 30.99 m/s (vx +30.87, vy -0.00, vz +2.72); touching nothing | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
1.00 s: ball1 at (-26.16, 0.00, 4.16) m, moving 30.29 m/s (vx -30.28, vy -0.00, vz +0.47); touching nothing | ball2 at (27.10, 0.00, 3.99) m, moving 30.87 m/s (vx +30.87, vy -0.00, vz +0.27); touching nothing | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
1.25 s: ball1 at (-33.73, 0.00, 3.98) m, moving 30.35 m/s (vx -30.28, vy -0.00, vz -1.98); touching nothing | ball2 at (34.82, 0.00, 3.75) m, moving 30.94 m/s (vx +30.87, vy -0.00, vz -2.18); touching nothing | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
1.50 s: ball1 at (-41.30, 0.00, 3.18) m, moving 30.61 m/s (vx -30.28, vy -0.00, vz -4.43); touching nothing | ball2 at (42.54, 0.00, 2.90) m, moving 31.21 m/s (vx +30.87, vy -0.00, vz -4.63); touching nothing | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
1.75 s: ball1 at (-48.87, 0.00, 1.77) m, moving 31.06 m/s (vx -30.28, vy -0.00, vz -6.88); touching nothing | ball2 at (50.25, 0.00, 1.44) m, moving 31.67 m/s (vx +30.87, vy -0.00, vz -7.09); touching nothing | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
2.00 s: ball1 at (-56.20, 0.00, 0.06) m, moving 20.70 m/s (vx -20.41, vy +0.00, vz +3.46); touching nothing | ball2 at (57.36, 0.00, 0.17) m, moving 21.86 m/s (vx +21.70, vy -0.00, vz +2.61); touching nothing | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
2.25 s: ball1 at (-61.30, 0.00, 0.62) m, moving 20.43 m/s (vx -20.41, vy +0.00, vz +1.01); touching nothing | ball2 at (62.79, 0.00, 0.52) m, moving 21.70 m/s (vx +21.70, vy -0.00, vz +0.16); touching nothing | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
2.50 s: ball1 at (-66.40, 0.00, 0.56) m, moving 20.46 m/s (vx -20.41, vy +0.00, vz -1.44); touching nothing | ball2 at (68.21, 0.00, 0.25) m, moving 21.82 m/s (vx +21.70, vy -0.00, vz -2.29); touching nothing | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
2.75 s: ball1 at (-71.48, 0.00, 0.02) m, moving 19.52 m/s (vx -19.50, vy -0.00, vz +0.76); touching floor | ball2 at (73.67, 0.00, 0.14) m, moving 22.05 m/s (vx +22.04, vy -0.00, vz +0.36); touching nothing | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
3.00 s: ball1 at (-76.56, 0.00, 0.16) m, moving 20.37 m/s (vx -20.36, vy -0.00, vz -0.62); touching nothing | ball2 at (79.21, 0.00, 0.03) m, moving 22.98 m/s (vx +22.97, vy +0.00, vz +0.56); touching nothing | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
3.25 s: ball1 at (-81.76, 0.00, 0.06) m, moving 21.32 m/s (vx -21.32, vy -0.00, vz -0.04); touching nothing | ball2 at (85.01, 0.00, 0.03) m, moving 23.59 m/s (vx +23.59, vy +0.00, vz +0.00); touching floor | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
3.50 s: ball1 at (-87.19, 0.00, 0.03) m, moving 22.12 m/s (vx -22.12, vy -0.00, vz +0.00); touching floor | ball2 at (90.91, 0.00, 0.03) m, moving 23.60 m/s (vx +23.60, vy +0.00, vz +0.00); touching floor | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
3.75 s: ball1 at (-92.73, 0.00, 0.03) m, moving 22.13 m/s (vx -22.13, vy -0.00, vz +0.00); touching floor | ball2 at (96.81, 0.00, 0.03) m, moving 23.60 m/s (vx +23.60, vy +0.00, vz -0.00); touching floor | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
4.00 s: ball1 at (-98.26, 0.00, 0.03) m, moving 22.13 m/s (vx -22.13, vy -0.00, vz +0.00); touching floor | ball2 at (102.71, 0.00, 0.03) m, moving 23.60 m/s (vx +23.60, vy +0.00, vz +0.00); touching floor | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
4.25 s: ball1 at (-103.79, 0.00, 0.03) m, moving 22.13 m/s (vx -22.13, vy -0.00, vz +0.00); touching floor | ball2 at (108.61, 0.00, 0.03) m, moving 23.60 m/s (vx +23.60, vy +0.00, vz -0.00); touching floor | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
4.50 s: ball1 at (-109.32, 0.00, 0.03) m, moving 22.13 m/s (vx -22.13, vy -0.00, vz -0.00); touching floor | ball2 at (114.51, 0.00, 0.03) m, moving 23.60 m/s (vx +23.60, vy +0.00, vz +0.00); touching floor | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
4.75 s: ball1 at (-114.85, 0.00, 0.03) m, moving 22.13 m/s (vx -22.13, vy -0.00, vz +0.00); touching floor | ball2 at (120.41, 0.00, 0.03) m, moving 23.60 m/s (vx +23.60, vy +0.00, vz -0.00); touching floor | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
5.00 s: ball1 at (-120.39, 0.00, 0.03) m, moving 22.13 m/s (vx -22.13, vy -0.00, vz -0.00); touching floor | ball2 at (126.31, 0.00, 0.03) m, moving 23.60 m/s (vx +23.60, vy +0.00, vz -0.00); touching floor | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
5.25 s: ball1 at (-125.92, 0.00, 0.03) m, moving 22.13 m/s (vx -22.13, vy -0.00, vz -0.00); touching floor | ball2 at (132.21, 0.00, 0.03) m, moving 23.60 m/s (vx +23.60, vy +0.00, vz +0.00); touching floor | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
5.50 s: ball1 at (-131.45, 0.00, 0.03) m, moving 22.13 m/s (vx -22.13, vy -0.00, vz +0.00); touching floor | ball2 at (138.11, 0.00, 0.03) m, moving 23.60 m/s (vx +23.60, vy +0.00, vz -0.00); touching floor | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
5.75 s: ball1 at (-136.98, 0.00, 0.03) m, moving 22.13 m/s (vx -22.13, vy -0.00, vz -0.00); touching floor | ball2 at (144.00, 0.00, 0.03) m, moving 23.60 m/s (vx +23.60, vy +0.00, vz -0.00); touching floor | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
6.00 s: ball1 at (-142.51, 0.00, 0.03) m, moving 22.13 m/s (vx -22.13, vy -0.00, vz -0.00); touching floor | ball2 at (149.90, 0.00, 0.03) m, moving 23.60 m/s (vx +23.60, vy +0.00, vz +0.00); touching floor | ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor

At the end (6.00 s):
- ball1 at (-142.51, 0.00, 0.03) m, moving 22.13 m/s (vx -22.13, vy -0.00, vz -0.00); touching floor
- ball2 at (149.90, 0.00, 0.03) m, moving 23.60 m/s (vx +23.60, vy +0.00, vz +0.00); touching floor
- ball3 at (0.50, 0.00, 0.03) m, at rest; touching floor
</history>
