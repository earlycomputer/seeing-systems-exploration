Your expectations, checked against the run (4 of 4 hold):

- holds: ball1 touches ball2 (first touch at 0.12 s)
- holds: ball2 touches ball3 (first touch at 0.37 s)
- holds: ball3 touches cup (first touch at 0.59 s)
- holds: ball3 comes to rest in cup (ball3 at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_geom; starts at (0.00, 0.00, 0.03) m, moving 2.50 m/s (vx +2.50, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2_geom; starts at (0.35, 0.00, 0.03) m, at rest
- ball3: free body; its geoms: ball3_geom; starts at (0.75, 0.00, 0.03) m, at rest

What happened, in order:
 0.00 s  ball1_geom starts touching floor
 0.00 s  ball2_geom starts touching floor
 0.00 s  ball3_geom starts touching floor
 0.12 s  ball1_geom first touches ball2_geom
 0.12 s  ball2 starts moving
 0.13 s  ball2_geom leaves floor
 0.14 s  ball1_geom leaves ball2_geom
 0.16 s  ball2_geom touches floor again
 0.37 s  ball2_geom first touches ball3_geom
 0.37 s  ball3 starts moving
 0.39 s  ball2_geom leaves ball3_geom
 0.59 s  ball3_geom leaves floor
 0.59 s  ball3_geom first touches cup_lip
 0.60 s  ball1_geom touches ball2_geom again
 0.62 s  ball1_geom leaves ball2_geom
 0.62 s  ball3_geom leaves cup_lip
 0.65 s  ball3_geom touches floor again
 0.73 s  ball2_geom leaves floor
 0.73 s  ball2_geom first touches cup_lip
 0.75 s  ball2_geom leaves cup_lip
 0.76 s  ball3_geom first touches cup_back
 0.76 s  ball3_geom leaves floor
 0.79 s  ball2_geom touches floor again
 0.80 s  ball3_geom touches floor again
 0.82 s  ball2_geom touches ball3_geom again
 0.83 s  ball2_geom leaves floor
 0.83 s  ball2_geom leaves ball3_geom
 0.84 s  ball1_geom leaves floor
 0.84 s  ball1_geom first touches cup_lip
 0.85 s  ball1_geom touches ball2_geom again
 0.85 s  ball1_geom leaves cup_lip
 0.86 s  ball1 passes 0.05 m from ball3 (ball3_geom) without touching it: nearest points (0.96, 0.00, 0.03) m and (1.01, 0.00, 0.03) m
 0.86 s  ball1_geom leaves ball2_geom
 0.87 s  ball2_geom touches ball3_geom again
 0.87 s  ball2_geom touches floor again
 0.88 s  ball3 comes to rest at (1.04, 0.00, 0.02) m
 0.89 s  ball2_geom leaves ball3_geom
 0.90 s  ball1_geom touches cup_lip again
 0.92 s  ball1_geom touches floor again
 0.96 s  ball3_geom leaves cup_back
 0.96 s  ball1_geom leaves cup_lip
 1.00 s  ball1_geom touches ball2_geom again
 1.01 s  ball1_geom leaves ball2_geom
 1.19 s  ball2_geom touches cup_lip again
 1.19 s  ball2 comes to rest at (0.95, 0.00, 0.02) m
 1.27 s  ball2_geom leaves cup_lip
 2.48 s  ball1 comes to rest at (0.81, 0.00, 0.02) m
 3.37 s  ball2_geom touches ball3_geom again
 3.39 s  ball2_geom leaves ball3_geom

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.03) m, moving 2.50 m/s (vx +2.50, vy +0.00, vz +0.00); touching floor | ball2 at (0.35, 0.00, 0.03) m, at rest; touching floor | ball3 at (0.75, 0.00, 0.03) m, at rest; touching floor
0.25 s: ball1 at (0.43, 0.00, 0.02) m, moving 1.04 m/s (vx +1.04, vy +0.00, vz +0.00); touching floor | ball2 at (0.54, 0.00, 0.02) m, moving 1.39 m/s (vx +1.39, vy +0.00, vz -0.00); touching floor | ball3 at (0.75, 0.00, 0.02) m, at rest; touching floor
0.50 s: ball1 at (0.68, 0.00, 0.02) m, moving 0.97 m/s (vx +0.97, vy +0.00, vz -0.00); touching floor | ball2 at (0.77, 0.00, 0.02) m, moving 0.53 m/s (vx +0.53, vy +0.00, vz +0.00); touching floor | ball3 at (0.85, 0.00, 0.02) m, moving 0.78 m/s (vx +0.78, vy -0.00, vz +0.00); touching floor
0.75 s: ball1 at (0.87, 0.00, 0.02) m, moving 0.63 m/s (vx +0.63, vy +0.00, vz -0.00); touching floor | ball2 at (0.94, 0.00, 0.03) m, moving 0.69 m/s (vx +0.68, vy +0.00, vz +0.08); touching cup_lip | ball3 at (1.03, 0.00, 0.02) m, moving 0.65 m/s (vx +0.65, vy -0.00, vz +0.00); touching floor
1.00 s: ball1 at (0.92, 0.00, 0.02) m, moving 0.10 m/s (vx -0.10, vy -0.00, vz +0.00); touching ball2_geom, floor | ball2 at (0.97, 0.00, 0.02) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching ball1_geom, floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching floor
1.25 s: ball1 at (0.90, 0.00, 0.02) m, moving 0.10 m/s (vx -0.10, vy -0.00, vz -0.00); touching floor | ball2 at (0.95, 0.00, 0.02) m, at rest; touching cup_lip, floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching floor
1.50 s: ball1 at (0.87, 0.00, 0.02) m, moving 0.09 m/s (vx -0.09, vy -0.00, vz -0.00); touching floor | ball2 at (0.96, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching floor
1.75 s: ball1 at (0.85, 0.00, 0.02) m, moving 0.07 m/s (vx -0.07, vy -0.00, vz -0.00); touching floor | ball2 at (0.96, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching floor
2.00 s: ball1 at (0.83, 0.00, 0.02) m, moving 0.07 m/s (vx -0.07, vy -0.00, vz -0.00); touching floor | ball2 at (0.96, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching floor
2.25 s: ball1 at (0.82, 0.00, 0.02) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz -0.00); touching floor | ball2 at (0.97, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching floor
2.50 s: ball1 at (0.81, 0.00, 0.02) m, at rest; touching floor | ball2 at (0.97, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching floor
2.75 s: ball1 at (0.79, 0.00, 0.02) m, at rest; touching floor | ball2 at (0.97, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching floor
3.00 s: ball1 at (0.78, 0.00, 0.02) m, at rest; touching floor | ball2 at (0.97, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.02, 0.00, 0.02) m, at rest; touching floor
(the same through 3.25 s)
3.50 s: ball1 at (0.77, 0.00, 0.02) m, at rest; touching floor | ball2 at (0.97, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.02, 0.00, 0.02) m, at rest; touching floor
3.75 s: ball1 at (0.76, 0.00, 0.02) m, at rest; touching floor | ball2 at (0.97, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.02, 0.00, 0.02) m, at rest; touching floor
4.00 s: ball1 at (0.76, 0.00, 0.02) m, at rest; touching floor | ball2 at (0.97, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching floor
4.25 s: ball1 at (0.75, 0.00, 0.02) m, at rest; touching floor | ball2 at (0.97, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching floor
(the same through 4.50 s)
4.75 s: ball1 at (0.74, 0.00, 0.02) m, at rest; touching floor | ball2 at (0.97, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching floor
(the same through 5.25 s)
5.50 s: ball1 at (0.73, 0.00, 0.02) m, at rest; touching floor | ball2 at (0.97, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (0.73, 0.00, 0.02) m, at rest; touching floor
- ball2 at (0.97, 0.00, 0.02) m, at rest; touching floor
- ball3 at (1.03, 0.00, 0.02) m, at rest; touching floor
</history>
