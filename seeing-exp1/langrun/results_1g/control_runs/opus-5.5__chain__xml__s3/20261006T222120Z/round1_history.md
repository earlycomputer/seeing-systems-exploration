MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_geom; starts at (0.00, 0.00, 0.03) m, moving 2.50 m/s (vx +2.50, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2_geom; starts at (0.15, 0.00, 0.03) m, at rest
- ball3: free body; its geoms: ball3_geom; starts at (0.30, 0.00, 0.03) m, at rest

What happened, in order:
 0.00 s  ball1_geom starts touching floor
 0.00 s  ball2_geom starts touching floor
 0.00 s  ball3_geom starts touching floor
 0.04 s  ball1_geom leaves floor
 0.04 s  ball2_geom leaves floor
 0.04 s  ball1_geom first touches ball2_geom
 0.04 s  ball2 starts moving
 0.04 s  ball1_geom leaves ball2_geom
 0.08 s  ball2_geom first touches ball3_geom
 0.08 s  ball3 starts moving
 0.08 s  ball3_geom leaves floor
 0.08 s  ball2_geom leaves ball3_geom
 0.09 s  ball1_geom touches floor again
 0.10 s  ball2_geom touches floor again
 0.11 s  ball3_geom touches floor again
 0.35 s  ball1_geom touches ball2_geom again
 0.36 s  ball1_geom leaves ball2_geom
 0.36 s  ball1 comes to rest at (0.19, 0.00, 0.03) m
 0.39 s  ball3_geom leaves floor
 0.39 s  ball3_geom first touches ramp_geom
 0.47 s  ball3_geom leaves ramp_geom
 0.52 s  ball3 is at the top of its flight, at (1.16, 0.00, 0.08) m
 0.58 s  ball3_geom first touches cup_back_wall
 0.65 s  ball3_geom leaves cup_back_wall
 0.67 s  ball3_geom first touches cup_base
 1.36 s  ball3_geom first touches cup_front_wall
 1.36 s  ball3 comes to rest at (1.13, 0.00, 0.03) m
 1.43 s  ball3_geom leaves cup_front_wall
 2.06 s  ball2 comes to rest at (0.53, 0.00, 0.03) m
 6.00 s  ball2 passes 0.35 m from ramp (ramp_geom) without touching it: nearest points (0.59, 0.00, 0.03) m and (0.94, 0.00, 0.00) m

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.03) m, moving 2.50 m/s (vx +2.50, vy +0.00, vz +0.00); touching floor | ball2 at (0.15, 0.00, 0.03) m, at rest; touching floor | ball3 at (0.30, 0.00, 0.03) m, at rest; touching floor
0.25 s: ball1 at (0.15, 0.00, 0.03) m, moving 0.38 m/s (vx +0.38, vy +0.00, vz +0.00); touching floor | ball2 at (0.25, 0.00, 0.03) m, at rest; touching floor | ball3 at (0.67, 0.00, 0.03) m, moving 2.00 m/s (vx +2.00, vy +0.00, vz -0.01); touching floor
0.50 s: ball1 at (0.20, 0.00, 0.03) m, at rest; touching floor | ball2 at (0.29, 0.00, 0.03) m, moving 0.29 m/s (vx +0.29, vy -0.00, vz +0.00); touching floor | ball3 at (1.13, 0.00, 0.08) m, moving 1.58 m/s (vx +1.57, vy +0.00, vz +0.18); touching nothing
0.75 s: ball1 at (0.21, 0.00, 0.03) m, at rest; touching floor | ball2 at (0.36, 0.00, 0.03) m, moving 0.23 m/s (vx +0.23, vy -0.00, vz -0.00); touching floor | ball3 at (1.23, 0.00, 0.03) m, moving 0.21 m/s (vx -0.21, vy +0.00, vz +0.03); touching cup_base
1.00 s: ball1 at (0.21, 0.00, 0.03) m, at rest; touching floor | ball2 at (0.41, 0.00, 0.03) m, moving 0.18 m/s (vx +0.18, vy -0.00, vz -0.00); touching floor | ball3 at (1.18, 0.00, 0.03) m, moving 0.16 m/s (vx -0.16, vy +0.00, vz -0.00); touching cup_base
1.25 s: ball1 at (0.22, 0.00, 0.03) m, at rest; touching floor | ball2 at (0.45, 0.00, 0.03) m, moving 0.14 m/s (vx +0.14, vy -0.00, vz -0.00); touching floor | ball3 at (1.14, 0.00, 0.03) m, moving 0.13 m/s (vx -0.13, vy +0.00, vz -0.00); touching cup_base
1.50 s: ball1 at (0.22, 0.00, 0.03) m, at rest; touching floor | ball2 at (0.48, 0.00, 0.03) m, moving 0.11 m/s (vx +0.11, vy -0.00, vz -0.00); touching floor | ball3 at (1.13, 0.00, 0.03) m, at rest; touching cup_base
1.75 s: ball1 at (0.22, 0.00, 0.03) m, at rest; touching floor | ball2 at (0.51, 0.00, 0.03) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz -0.00); touching floor | ball3 at (1.13, 0.00, 0.03) m, at rest; touching cup_base
2.00 s: ball1 at (0.22, 0.00, 0.03) m, at rest; touching floor | ball2 at (0.52, 0.00, 0.03) m, moving 0.05 m/s (vx +0.05, vy -0.00, vz -0.00); touching floor | ball3 at (1.13, 0.00, 0.03) m, at rest; touching cup_base
2.25 s: ball1 at (0.22, 0.00, 0.03) m, at rest; touching floor | ball2 at (0.53, 0.00, 0.03) m, at rest; touching floor | ball3 at (1.14, 0.00, 0.03) m, at rest; touching cup_base
2.50 s: ball1 at (0.22, 0.00, 0.03) m, at rest; touching floor | ball2 at (0.54, 0.00, 0.03) m, at rest; touching floor | ball3 at (1.14, 0.00, 0.03) m, at rest; touching cup_base
2.75 s: ball1 at (0.22, 0.00, 0.03) m, at rest; touching floor | ball2 at (0.55, 0.00, 0.03) m, at rest; touching floor | ball3 at (1.14, 0.00, 0.03) m, at rest; touching cup_base
(the same through 3.50 s)
3.75 s: ball1 at (0.22, 0.00, 0.03) m, at rest; touching floor | ball2 at (0.56, 0.00, 0.03) m, at rest; touching floor | ball3 at (1.14, 0.00, 0.03) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (0.22, 0.00, 0.03) m, at rest; touching floor
- ball2 at (0.56, 0.00, 0.03) m, at rest; touching floor
- ball3 at (1.14, 0.00, 0.03) m, at rest; touching cup_base
</history>
