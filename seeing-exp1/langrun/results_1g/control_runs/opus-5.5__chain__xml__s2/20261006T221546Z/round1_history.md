MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_geom; starts at (0.00, 0.00, 0.02) m, moving 2.00 m/s (vx +2.00, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2_geom; starts at (0.20, 0.00, 0.02) m, at rest
- ball3: free body; its geoms: ball3_geom; starts at (0.40, 0.00, 0.02) m, at rest

What happened, in order:
 0.00 s  ball1_geom starts touching floor
 0.00 s  ball2_geom starts touching floor
 0.00 s  ball3_geom starts touching floor
 0.08 s  ball1_geom first touches ball2_geom
 0.08 s  ball2 starts moving
 0.09 s  ball2_geom leaves floor
 0.09 s  ball1_geom leaves ball2_geom
 0.13 s  ball2_geom touches floor again
 0.18 s  ball1 passes 0.16 m from ball3 (ball3_geom) without touching it: nearest points (0.22, 0.00, 0.02) m and (0.38, 0.00, 0.02) m
 0.18 s  ball2_geom first touches ball3_geom
 0.18 s  ball3 starts moving
 0.18 s  ball2_geom leaves floor
 0.18 s  ball3_geom leaves floor
 0.19 s  ball2_geom leaves ball3_geom
 0.22 s  ball2_geom touches floor again
 0.22 s  ball3_geom touches floor again
 0.51 s  ball3_geom leaves floor
 0.51 s  ball3_geom first touches ramp_slab
 0.72 s  ball3_geom first touches cup_wall_front
 0.73 s  ball3_geom leaves ramp_slab
 0.73 s  ball3_geom leaves cup_wall_front
 0.81 s  ball3_geom first touches cup_base
 0.82 s  ball3_geom touches floor again
 0.85 s  ball3_geom leaves floor
 0.86 s  ball3_geom first touches cup_wall_back
 0.88 s  ball3_geom leaves cup_base
 0.93 s  ball3_geom touches cup_base again
 0.93 s  ball3_geom leaves cup_wall_back
 1.09 s  ball1_geom touches ball2_geom again
 1.09 s  ball1_geom leaves ball2_geom
 1.81 s  ball3_geom touches cup_wall_front again
 1.81 s  ball3 comes to rest at (1.02, 0.00, 0.02) m
 1.89 s  ball3_geom leaves cup_wall_front
 2.21 s  ball2_geom first touches ramp_slab
 2.23 s  ball2_geom leaves floor
 2.34 s  ball2 passes 0.17 m from cup (cup_wall_front) without touching it: nearest points (0.83, 0.00, 0.02) m and (1.00, 0.00, 0.02) m
 2.47 s  ball2_geom touches floor again
 2.48 s  ball2_geom leaves ramp_slab
 2.97 s  ball1_geom touches ball2_geom again
 2.97 s  ball1 passes 0.07 m from ramp (ramp_slab) without touching it: nearest points (0.73, 0.00, 0.02) m and (0.80, 0.00, 0.00) m
 2.97 s  ball1 passes 0.27 m from cup (cup_wall_front) without touching it: nearest points (0.73, 0.00, 0.02) m and (1.00, 0.00, 0.02) m
 2.97 s  ball2 comes to rest at (0.75, 0.00, 0.02) m
 2.98 s  ball1_geom leaves ball2_geom
 3.45 s  ball1 comes to rest at (0.68, 0.00, 0.02) m

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.02) m, moving 2.00 m/s (vx +2.00, vy +0.00, vz +0.00); touching floor | ball2 at (0.20, 0.00, 0.02) m, at rest; touching floor | ball3 at (0.40, 0.00, 0.02) m, at rest; touching floor
0.25 s: ball1 at (0.23, 0.00, 0.02) m, moving 0.43 m/s (vx +0.43, vy +0.00, vz -0.00); touching floor | ball2 at (0.37, 0.00, 0.02) m, moving 0.27 m/s (vx +0.27, vy -0.00, vz +0.02); touching floor | ball3 at (0.49, 0.00, 0.02) m, moving 1.22 m/s (vx +1.22, vy +0.00, vz +0.04); touching floor
0.50 s: ball1 at (0.33, 0.00, 0.02) m, moving 0.38 m/s (vx +0.38, vy +0.00, vz -0.00); touching floor | ball2 at (0.44, 0.00, 0.02) m, moving 0.25 m/s (vx +0.25, vy -0.00, vz -0.00); touching floor | ball3 at (0.78, 0.00, 0.02) m, moving 1.12 m/s (vx +1.12, vy +0.00, vz +0.00); touching floor
0.75 s: ball1 at (0.42, 0.00, 0.02) m, moving 0.34 m/s (vx +0.34, vy +0.00, vz -0.00); touching floor | ball2 at (0.50, 0.00, 0.02) m, moving 0.21 m/s (vx +0.21, vy -0.00, vz -0.00); touching floor | ball3 at (1.02, 0.00, 0.05) m, moving 0.81 m/s (vx +0.80, vy +0.00, vz -0.12); touching nothing
1.00 s: ball1 at (0.50, 0.00, 0.02) m, moving 0.30 m/s (vx +0.30, vy +0.00, vz -0.00); touching floor | ball2 at (0.55, 0.00, 0.02) m, moving 0.18 m/s (vx +0.18, vy -0.00, vz -0.00); touching floor | ball3 at (1.10, 0.00, 0.02) m, moving 0.12 m/s (vx -0.12, vy +0.00, vz +0.01); touching cup_base
1.25 s: ball1 at (0.55, 0.00, 0.02) m, moving 0.16 m/s (vx +0.16, vy +0.00, vz -0.00); touching floor | ball2 at (0.61, 0.00, 0.02) m, moving 0.26 m/s (vx +0.26, vy -0.00, vz -0.00); touching floor | ball3 at (1.07, 0.00, 0.02) m, moving 0.10 m/s (vx -0.10, vy +0.00, vz -0.00); touching cup_base
1.50 s: ball1 at (0.59, 0.00, 0.02) m, moving 0.14 m/s (vx +0.14, vy +0.00, vz -0.00); touching floor | ball2 at (0.67, 0.00, 0.02) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz -0.00); touching floor | ball3 at (1.05, 0.00, 0.02) m, moving 0.08 m/s (vx -0.08, vy +0.00, vz -0.00); touching cup_base
1.75 s: ball1 at (0.62, 0.00, 0.02) m, moving 0.12 m/s (vx +0.12, vy +0.00, vz -0.00); touching floor | ball2 at (0.72, 0.00, 0.02) m, moving 0.19 m/s (vx +0.19, vy -0.00, vz -0.00); touching floor | ball3 at (1.03, 0.00, 0.02) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching cup_base
2.00 s: ball1 at (0.65, 0.00, 0.02) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz -0.00); touching floor | ball2 at (0.76, 0.00, 0.02) m, moving 0.17 m/s (vx +0.17, vy -0.00, vz -0.00); touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching cup_base
2.25 s: ball1 at (0.67, 0.00, 0.02) m, moving 0.08 m/s (vx +0.08, vy +0.00, vz -0.00); touching floor | ball2 at (0.80, 0.00, 0.02) m, moving 0.10 m/s (vx +0.10, vy -0.00, vz +0.02); touching ramp_slab | ball3 at (1.03, 0.00, 0.02) m, at rest; touching cup_base
2.50 s: ball1 at (0.69, 0.00, 0.02) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz -0.00); touching floor | ball2 at (0.80, 0.00, 0.02) m, moving 0.11 m/s (vx -0.11, vy -0.00, vz -0.00); touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching cup_base
2.75 s: ball1 at (0.70, 0.00, 0.02) m, moving 0.05 m/s (vx +0.05, vy +0.00, vz -0.00); touching floor | ball2 at (0.77, 0.00, 0.02) m, moving 0.09 m/s (vx -0.09, vy -0.00, vz -0.00); touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching cup_base
3.00 s: ball1 at (0.71, 0.00, 0.02) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz -0.00); touching floor | ball2 at (0.75, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching cup_base
3.25 s: ball1 at (0.69, 0.00, 0.02) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching floor | ball2 at (0.76, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching cup_base
3.50 s: ball1 at (0.68, 0.00, 0.02) m, at rest; touching floor | ball2 at (0.77, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching cup_base
3.75 s: ball1 at (0.67, 0.00, 0.02) m, at rest; touching floor | ball2 at (0.77, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching cup_base
4.00 s: ball1 at (0.66, 0.00, 0.02) m, at rest; touching floor | ball2 at (0.78, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching cup_base
4.25 s: ball1 at (0.65, 0.00, 0.02) m, at rest; touching floor | ball2 at (0.78, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching cup_base
(the same through 4.50 s)
4.75 s: ball1 at (0.64, 0.00, 0.02) m, at rest; touching floor | ball2 at (0.79, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching cup_base
(the same through 5.25 s)
5.50 s: ball1 at (0.63, 0.00, 0.02) m, at rest; touching floor | ball2 at (0.79, 0.00, 0.02) m, at rest; touching floor | ball3 at (1.03, 0.00, 0.02) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (0.63, 0.00, 0.02) m, at rest; touching floor
- ball2 at (0.79, 0.00, 0.02) m, at rest; touching floor
- ball3 at (1.03, 0.00, 0.02) m, at rest; touching cup_base
</history>
