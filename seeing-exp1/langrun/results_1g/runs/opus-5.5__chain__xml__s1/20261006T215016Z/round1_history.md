Your expectations, checked against the run (1 of 5 hold):

- holds: ball1 touches ball2 (first touch at 0.11 s)
- DOES NOT HOLD: ball2 touches ball3 (they never touch)
- DOES NOT HOLD: ball3 touches cup_ramp (they never touch)
- DOES NOT HOLD: ball3 touches cup_back (they never touch)
- DOES NOT HOLD: ball3 comes to rest in cup (ball3 comes to rest at (0.50, 0.00, 0.02) m, outside cup)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_geom; starts at (0.00, 0.00, 0.02) m, moving 2.00 m/s (vx +2.00, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2_geom; starts at (0.25, 0.00, 0.02) m, at rest
- ball3: free body; its geoms: ball3_geom; starts at (0.50, 0.00, 0.02) m, at rest

What happened, in order:
 0.00 s  ball1_geom starts touching floor
 0.00 s  ball2_geom starts touching floor
 0.00 s  ball3_geom starts touching floor
 0.10 s  ball1 passes 0.26 m from ball3 (ball3_geom) without touching it: nearest points (0.22, 0.00, 0.02) m and (0.48, 0.00, 0.02) m
 0.11 s  ball1_geom leaves floor
 0.11 s  ball2_geom leaves floor
 0.11 s  ball1_geom first touches ball2_geom
 0.11 s  ball1_geom leaves ball2_geom
 0.11 s  ball2 starts moving
 0.11 s  ball2 passes 0.09 m from ball3 (ball3_geom) without touching it: nearest points (0.39, 0.00, 0.05) m and (0.48, 0.00, 0.03) m
 0.12 s  ball2 passes 0.11 m from cup (cup_side_right) without touching it: nearest points (0.69, -0.01, 0.14) m and (0.75, -0.07, 0.06) m
 1.05 s  ball1 is at the top of its flight, at (-27.97, 0.00, 4.34) m
 1.07 s  ball2 is at the top of its flight, at (30.07, 0.00, 4.56) m
 1.98 s  ball1_geom touches floor again
 2.00 s  ball1_geom leaves floor
 2.03 s  ball2_geom touches floor again
 2.05 s  ball2_geom leaves floor
 2.39 s  ball1 is at the top of its flight, at (-65.75, 0.00, 0.77) m
 2.56 s  ball2 is at the top of its flight, at (72.49, 0.00, 1.31) m
 2.78 s  ball1_geom touches floor again
 2.80 s  ball1_geom leaves floor
 2.96 s  ball1 is at the top of its flight, at (-78.59, 0.00, 0.14) m
 3.08 s  ball2_geom touches floor again
 3.10 s  ball2_geom leaves floor
 3.11 s  ball1_geom touches floor again
 3.16 s  ball1_geom leaves floor
 3.22 s  ball1 is at the top of its flight, at (-83.95, 0.00, 0.04) m
 3.29 s  ball1_geom touches floor 2 more times between 3.29 s and 6.00 s, still touching at the end
 3.32 s  ball2 is at the top of its flight, at (89.52, 0.00, 0.26) m
 3.54 s  ball2_geom touches floor again
 3.57 s  ball2_geom leaves floor
 3.67 s  ball2 is at the top of its flight, at (96.42, 0.00, 0.07) m
 3.77 s  ball2_geom touches floor 2 more times between 3.77 s and 6.00 s, still touching at the end
 6.00 s  ball1 is still moving at the end, 21.42 m/s
 6.00 s  ball2 is still moving at the end, 20.10 m/s

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.02) m, moving 2.00 m/s (vx +2.00, vy +0.00, vz +0.00); touching floor | ball2 at (0.25, 0.00, 0.02) m, at rest; touching floor | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
0.25 s: ball1 at (-4.05, 0.00, 1.23) m, moving 31.04 m/s (vx -30.05, vy -0.00, vz +7.80); touching nothing | ball2 at (4.65, 0.00, 1.26) m, moving 32.03 m/s (vx +31.00, vy -0.00, vz +8.04); touching nothing | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
0.50 s: ball1 at (-11.57, 0.00, 2.87) m, moving 30.52 m/s (vx -30.05, vy -0.00, vz +5.35); touching nothing | ball2 at (12.40, 0.00, 2.97) m, moving 31.50 m/s (vx +31.00, vy -0.00, vz +5.58); touching nothing | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
0.75 s: ball1 at (-19.08, 0.00, 3.91) m, moving 30.18 m/s (vx -30.05, vy -0.00, vz +2.89); touching nothing | ball2 at (20.15, 0.00, 4.06) m, moving 31.16 m/s (vx +31.00, vy -0.00, vz +3.13); touching nothing | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
1.00 s: ball1 at (-26.59, 0.00, 4.33) m, moving 30.05 m/s (vx -30.05, vy -0.00, vz +0.44); touching nothing | ball2 at (27.90, 0.00, 4.54) m, moving 31.01 m/s (vx +31.00, vy -0.00, vz +0.68); touching nothing | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
1.25 s: ball1 at (-34.10, 0.00, 4.13) m, moving 30.11 m/s (vx -30.05, vy -0.00, vz -2.01); touching nothing | ball2 at (35.65, 0.00, 4.40) m, moving 31.05 m/s (vx +31.00, vy -0.00, vz -1.77); touching nothing | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
1.50 s: ball1 at (-41.61, 0.00, 3.32) m, moving 30.38 m/s (vx -30.05, vy -0.00, vz -4.46); touching nothing | ball2 at (43.40, 0.00, 3.65) m, moving 31.29 m/s (vx +31.00, vy -0.00, vz -4.23); touching nothing | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
1.75 s: ball1 at (-49.12, 0.00, 1.90) m, moving 30.83 m/s (vx -30.05, vy -0.00, vz -6.92); touching nothing | ball2 at (51.16, 0.00, 2.29) m, moving 31.71 m/s (vx +31.00, vy -0.00, vz -6.68); touching nothing | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
2.00 s: ball1 at (-56.56, 0.00, 0.02) m, moving 23.76 m/s (vx -23.45, vy -0.00, vz +3.83); touching floor | ball2 at (58.91, 0.00, 0.32) m, moving 32.32 m/s (vx +31.00, vy -0.00, vz -9.13); touching nothing | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
2.25 s: ball1 at (-62.42, 0.00, 0.67) m, moving 23.49 m/s (vx -23.45, vy -0.00, vz +1.38); touching nothing | ball2 at (65.11, 0.00, 0.83) m, moving 23.88 m/s (vx +23.68, vy -0.00, vz +3.06); touching nothing | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
2.50 s: ball1 at (-68.28, 0.00, 0.71) m, moving 23.47 m/s (vx -23.45, vy -0.00, vz -1.07); touching nothing | ball2 at (71.03, 0.00, 1.29) m, moving 23.69 m/s (vx +23.68, vy -0.00, vz +0.61); touching nothing | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
2.75 s: ball1 at (-74.15, 0.00, 0.14) m, moving 23.71 m/s (vx -23.45, vy -0.00, vz -3.53); touching nothing | ball2 at (76.95, 0.00, 1.14) m, moving 23.75 m/s (vx +23.68, vy -0.00, vz -1.85); touching nothing | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
3.00 s: ball1 at (-79.42, 0.00, 0.13) m, moving 20.66 m/s (vx -20.66, vy -0.00, vz -0.41); touching nothing | ball2 at (82.87, 0.00, 0.38) m, moving 24.07 m/s (vx +23.68, vy -0.00, vz -4.30); touching nothing | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
3.25 s: ball1 at (-84.57, 0.00, 0.04) m, moving 20.60 m/s (vx -20.60, vy -0.00, vz -0.30); touching nothing | ball2 at (88.17, 0.00, 0.24) m, moving 19.99 m/s (vx +19.98, vy -0.00, vz +0.65); touching nothing | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
3.50 s: ball1 at (-89.84, 0.00, 0.02) m, moving 21.40 m/s (vx -21.40, vy +0.00, vz +0.00); touching floor | ball2 at (93.16, 0.00, 0.10) m, moving 20.06 m/s (vx +19.98, vy -0.00, vz -1.80); touching nothing | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
3.75 s: ball1 at (-95.19, 0.00, 0.02) m, moving 21.42 m/s (vx -21.42, vy +0.00, vz +0.00); touching floor | ball2 at (97.93, 0.00, 0.04) m, moving 18.92 m/s (vx +18.91, vy -0.00, vz -0.79); touching nothing | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
4.00 s: ball1 at (-100.55, 0.00, 0.02) m, moving 21.42 m/s (vx -21.42, vy +0.00, vz +0.00); touching floor | ball2 at (102.83, 0.00, 0.02) m, moving 20.07 m/s (vx +20.07, vy -0.00, vz +0.00); touching floor | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
4.25 s: ball1 at (-105.90, 0.00, 0.02) m, moving 21.42 m/s (vx -21.42, vy +0.00, vz +0.00); touching floor | ball2 at (107.85, 0.00, 0.02) m, moving 20.10 m/s (vx +20.10, vy -0.00, vz +0.00); touching floor | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
4.50 s: ball1 at (-111.26, 0.00, 0.02) m, moving 21.42 m/s (vx -21.42, vy +0.00, vz +0.00); touching floor | ball2 at (112.88, 0.00, 0.02) m, moving 20.10 m/s (vx +20.10, vy -0.00, vz +0.00); touching floor | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
4.75 s: ball1 at (-116.61, 0.00, 0.02) m, moving 21.42 m/s (vx -21.42, vy +0.00, vz -0.00); touching floor | ball2 at (117.90, 0.00, 0.02) m, moving 20.10 m/s (vx +20.10, vy -0.00, vz -0.00); touching floor | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
5.00 s: ball1 at (-121.97, 0.00, 0.02) m, moving 21.42 m/s (vx -21.42, vy +0.00, vz +0.00); touching floor | ball2 at (122.93, 0.00, 0.02) m, moving 20.10 m/s (vx +20.10, vy -0.00, vz +0.00); touching floor | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
5.25 s: ball1 at (-127.32, 0.00, 0.02) m, moving 21.42 m/s (vx -21.42, vy +0.00, vz +0.00); touching floor | ball2 at (127.95, 0.00, 0.02) m, moving 20.10 m/s (vx +20.10, vy -0.00, vz +0.00); touching floor | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
5.50 s: ball1 at (-132.68, 0.00, 0.02) m, moving 21.42 m/s (vx -21.42, vy +0.00, vz -0.00); touching floor | ball2 at (132.98, 0.00, 0.02) m, moving 20.10 m/s (vx +20.10, vy -0.00, vz +0.00); touching floor | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
5.75 s: ball1 at (-138.03, 0.00, 0.02) m, moving 21.42 m/s (vx -21.42, vy +0.00, vz +0.00); touching floor | ball2 at (138.00, 0.00, 0.02) m, moving 20.10 m/s (vx +20.10, vy -0.00, vz -0.00); touching floor | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
6.00 s: ball1 at (-143.39, 0.00, 0.02) m, moving 21.42 m/s (vx -21.42, vy +0.00, vz -0.00); touching floor | ball2 at (143.02, 0.00, 0.02) m, moving 20.10 m/s (vx +20.10, vy -0.00, vz +0.00); touching floor | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor

At the end (6.00 s):
- ball1 at (-143.39, 0.00, 0.02) m, moving 21.42 m/s (vx -21.42, vy +0.00, vz -0.00); touching floor
- ball2 at (143.02, 0.00, 0.02) m, moving 20.10 m/s (vx +20.10, vy -0.00, vz +0.00); touching floor
- ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
</history>
