Your expectations, checked against the run (5 of 5 hold):

- holds: ball1 touches ball2 (first touch at 0.09 s)
- holds: ball2 touches ball3 (first touch at 0.26 s)
- holds: ball3 touches cup_ramp (first touch at 0.70 s)
- holds: ball3 touches cup_back (first touch at 1.11 s)
- holds: ball3 comes to rest in cup (ball3 at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_geom; starts at (0.00, 0.00, 0.02) m, moving 2.50 m/s (vx +2.50, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2_geom; starts at (0.25, 0.00, 0.02) m, at rest
- ball3: free body; its geoms: ball3_geom; starts at (0.50, 0.00, 0.02) m, at rest

What happened, in order:
 0.00 s  ball1_geom starts touching floor
 0.00 s  ball2_geom starts touching floor
 0.00 s  ball3_geom starts touching floor
 0.09 s  ball1_geom leaves floor
 0.09 s  ball2_geom leaves floor
 0.09 s  ball1_geom first touches ball2_geom
 0.09 s  ball2 starts moving
 0.10 s  ball1_geom leaves ball2_geom
 0.17 s  ball2_geom touches floor again
 0.18 s  ball1_geom touches floor again
 0.26 s  ball3_geom leaves floor
 0.26 s  ball2_geom first touches ball3_geom
 0.26 s  ball3 starts moving
 0.26 s  ball2_geom leaves ball3_geom
 0.29 s  ball3_geom touches floor again
 0.34 s  ball2_geom touches ball3_geom again
 0.34 s  ball2_geom leaves ball3_geom
 0.36 s  ball2_geom leaves floor
 0.36 s  ball1_geom touches ball2_geom again
 0.36 s  ball1_geom leaves ball2_geom
 0.37 s  ball2_geom touches ball3_geom again
 0.37 s  ball2_geom leaves ball3_geom
 0.39 s  ball2_geom touches floor again
 0.40 s  ball1_geom touches ball2_geom again
 0.40 s  ball1_geom leaves ball2_geom
 0.70 s  ball3_geom first touches cup_ramp
 0.70 s  ball3_geom leaves floor
 0.80 s  ball3_geom leaves cup_ramp
 0.83 s  ball2_geom first touches cup_ramp
 0.83 s  ball2_geom leaves floor
 0.85 s  ball3_geom first touches cup_floor
 0.86 s  ball3_geom touches floor again
 0.88 s  ball3_geom leaves floor
 0.98 s  ball2_geom leaves cup_ramp
 0.99 s  ball1_geom first touches cup_ramp
 0.99 s  ball1_geom leaves floor
 1.01 s  ball2_geom first touches cup_floor
 1.02 s  ball2_geom touches floor again
 1.03 s  ball2_geom leaves floor
 1.11 s  ball3_geom first touches cup_back
 1.17 s  ball3_geom leaves cup_back
 1.20 s  ball1_geom leaves cup_ramp
 1.21 s  ball1_geom first touches cup_floor
 1.22 s  ball1_geom touches floor again
 1.23 s  ball1_geom leaves floor
 1.23 s  ball2_geom touches ball3_geom again
 1.24 s  ball2_geom leaves ball3_geom
 1.27 s  ball3_geom touches cup_back again
 1.27 s  ball2_geom touches ball3_geom 4 more times between 1.27 s and 5.66 s
 1.33 s  ball3_geom leaves cup_back
 1.37 s  ball1_geom touches ball2_geom again
 1.37 s  ball1 passes 0.04 m from ball3 (ball3_geom) without touching it: nearest points (0.89, 0.00, 0.02) m and (0.93, 0.00, 0.02) m
 1.38 s  ball3_geom touches cup_back again
 1.38 s  ball2 comes to rest at (0.91, 0.00, 0.02) m
 1.38 s  ball3 comes to rest at (0.95, 0.00, 0.02) m
 1.38 s  ball1 comes to rest at (0.87, 0.00, 0.02) m
 1.42 s  ball1_geom leaves ball2_geom
 1.44 s  ball3_geom leaves cup_back
 4.42 s  ball1_geom touches cup_ramp again
 4.49 s  ball1_geom leaves cup_ramp
 5.22 s  ball1_geom touches ball2_geom 2 more times between 5.22 s and 5.66 s
 5.49 s  ball1_geom touches cup_ramp again
 5.57 s  ball1_geom leaves cup_ramp
 5.62 s  ball1_geom touches cup_ramp again
 5.71 s  ball1_geom leaves cup_ramp

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.02) m, moving 2.50 m/s (vx +2.50, vy +0.00, vz +0.00); touching floor | ball2 at (0.25, 0.00, 0.02) m, at rest; touching floor | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
0.25 s: ball1 at (0.35, 0.00, 0.02) m, moving 1.00 m/s (vx +1.00, vy +0.00, vz +0.02); touching floor | ball2 at (0.45, 0.00, 0.02) m, moving 1.04 m/s (vx +1.04, vy -0.00, vz +0.01); touching floor | ball3 at (0.50, 0.00, 0.02) m, at rest; touching floor
0.50 s: ball1 at (0.53, 0.00, 0.02) m, moving 0.45 m/s (vx +0.45, vy +0.00, vz +0.00); touching floor | ball2 at (0.58, 0.00, 0.02) m, moving 0.52 m/s (vx +0.52, vy -0.00, vz +0.00); touching floor | ball3 at (0.63, 0.00, 0.02) m, moving 0.60 m/s (vx +0.60, vy +0.00, vz +0.00); touching floor
0.75 s: ball1 at (0.64, 0.00, 0.02) m, moving 0.45 m/s (vx +0.45, vy +0.00, vz +0.00); touching floor | ball2 at (0.71, 0.00, 0.02) m, moving 0.52 m/s (vx +0.52, vy -0.00, vz +0.00); touching floor | ball3 at (0.78, 0.00, 0.02) m, moving 0.54 m/s (vx +0.53, vy +0.00, vz +0.09); touching cup_ramp
1.00 s: ball1 at (0.75, 0.00, 0.02) m, moving 0.43 m/s (vx +0.42, vy +0.00, vz +0.06); touching cup_ramp | ball2 at (0.82, 0.00, 0.02) m, moving 0.49 m/s (vx +0.38, vy -0.00, vz -0.31); touching nothing | ball3 at (0.90, 0.00, 0.02) m, moving 0.48 m/s (vx +0.48, vy +0.00, vz +0.00); touching cup_floor
1.25 s: ball1 at (0.83, 0.00, 0.02) m, moving 0.31 m/s (vx +0.31, vy +0.00, vz +0.04); touching cup_floor | ball2 at (0.91, 0.00, 0.02) m, moving 0.11 m/s (vx +0.11, vy -0.00, vz -0.02); touching cup_floor | ball3 at (0.95, 0.00, 0.02) m, moving 0.12 m/s (vx +0.12, vy +0.00, vz -0.02); touching cup_floor
1.50 s: ball1 at (0.87, 0.00, 0.02) m, at rest; touching cup_floor | ball2 at (0.91, 0.00, 0.02) m, at rest; touching cup_floor | ball3 at (0.95, 0.00, 0.02) m, at rest; touching cup_floor
1.75 s: ball1 at (0.86, 0.00, 0.02) m, at rest; touching cup_floor | ball2 at (0.91, 0.00, 0.02) m, at rest; touching cup_floor | ball3 at (0.95, 0.00, 0.02) m, at rest; touching cup_floor
2.00 s: ball1 at (0.86, 0.00, 0.02) m, at rest; touching cup_floor | ball2 at (0.90, 0.00, 0.02) m, at rest; touching cup_floor | ball3 at (0.94, 0.00, 0.02) m, at rest; touching cup_floor
(the same through 2.25 s)
2.50 s: ball1 at (0.85, 0.00, 0.02) m, at rest; touching cup_floor | ball2 at (0.90, 0.00, 0.02) m, at rest; touching cup_floor | ball3 at (0.94, 0.00, 0.02) m, at rest; touching cup_floor
2.75 s: ball1 at (0.85, 0.00, 0.02) m, at rest; touching cup_floor | ball2 at (0.89, 0.00, 0.02) m, at rest; touching cup_floor | ball3 at (0.93, 0.00, 0.02) m, at rest; touching cup_floor
3.00 s: ball1 at (0.84, 0.00, 0.02) m, at rest; touching cup_floor | ball2 at (0.89, 0.00, 0.02) m, at rest; touching cup_floor | ball3 at (0.93, 0.00, 0.02) m, at rest; touching cup_floor
(the same through 3.25 s)
3.50 s: ball1 at (0.84, 0.00, 0.02) m, at rest; touching cup_floor | ball2 at (0.88, 0.00, 0.02) m, at rest; touching cup_floor | ball3 at (0.92, 0.00, 0.02) m, at rest; touching cup_floor
3.75 s: ball1 at (0.83, 0.00, 0.02) m, at rest; touching cup_floor | ball2 at (0.88, 0.00, 0.02) m, at rest; touching cup_floor | ball3 at (0.92, 0.00, 0.02) m, at rest; touching cup_floor
(the same through 4.00 s)
4.25 s: ball1 at (0.82, 0.00, 0.02) m, at rest; touching cup_floor | ball2 at (0.87, 0.00, 0.02) m, at rest; touching cup_floor | ball3 at (0.91, 0.00, 0.02) m, at rest; touching cup_floor
(the same through 4.75 s)
5.00 s: ball1 at (0.82, 0.00, 0.02) m, at rest; touching cup_floor | ball2 at (0.86, 0.00, 0.02) m, at rest; touching cup_floor | ball3 at (0.90, 0.00, 0.02) m, at rest; touching cup_floor
(the same through 5.25 s)
5.50 s: ball1 at (0.82, 0.00, 0.02) m, at rest; touching cup_floor, cup_ramp | ball2 at (0.86, 0.00, 0.02) m, at rest; touching cup_floor | ball3 at (0.90, 0.00, 0.02) m, at rest; touching cup_floor
5.75 s: ball1 at (0.82, 0.00, 0.02) m, at rest; touching cup_floor | ball2 at (0.86, 0.00, 0.02) m, at rest; touching cup_floor | ball3 at (0.90, 0.00, 0.02) m, at rest; touching cup_floor
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (0.82, 0.00, 0.02) m, at rest; touching cup_floor
- ball2 at (0.86, 0.00, 0.02) m, at rest; touching cup_floor
- ball3 at (0.90, 0.00, 0.02) m, at rest; touching cup_floor
</history>
