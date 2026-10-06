MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_geom; starts at (0.00, 0.00, 0.04) m, moving 3.00 m/s (vx +3.00, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2_geom; starts at (0.40, 0.00, 0.04) m, at rest
- ball3: free body; its geoms: ball3_geom; starts at (0.50, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball1_geom starts touching floor
 0.00 s  ball2_geom starts touching floor
 0.00 s  ball3_geom starts touching floor
 0.11 s  ball1_geom leaves floor
 0.11 s  ball2_geom leaves floor
 0.11 s  ball1_geom first touches ball2_geom
 0.11 s  ball2 starts moving
 0.11 s  ball1_geom leaves ball2_geom
 0.12 s  ball2_geom first touches ball3_geom
 0.12 s  ball3 starts moving
 0.12 s  ball1 passes 0.09 m from ball3 (ball3_geom) without touching it: nearest points (0.37, 0.00, 0.04) m and (0.46, 0.00, 0.04) m
 0.12 s  ball3_geom leaves floor
 0.13 s  ball2_geom leaves ball3_geom
 0.15 s  ball2_geom touches floor again
 0.17 s  ball3_geom touches floor again
 0.18 s  ball1_geom touches floor again
 0.20 s  ball1_geom touches ball2_geom again
 0.20 s  ball1_geom leaves ball2_geom
 0.42 s  ball3_geom first touches ramp
 0.42 s  ball3_geom leaves floor
 0.72 s  ball3_geom leaves ramp
 0.74 s  ball3 is at the top of its flight, at (1.39, 0.00, 0.14) m
 0.88 s  ball3_geom first touches cup_bottom
 0.98 s  ball2_geom first touches ramp
 0.99 s  ball2_geom leaves floor
 1.00 s  ball3_geom first touches cup_back
 1.01 s  ball3_geom leaves cup_bottom
 1.07 s  ball3_geom leaves cup_back
 1.07 s  ball3_geom touches cup_bottom again
 1.36 s  ball2 passes 0.21 m from cup (cup_front) without touching it: nearest points (1.16, 0.00, 0.07) m and (1.37, 0.00, 0.07) m
 1.74 s  ball2_geom touches floor again
 1.74 s  ball2_geom leaves ramp
 1.82 s  ball1 passes 0.11 m from ramp without touching it: nearest points (0.90, 0.00, 0.03) m and (1.00, 0.00, 0.00) m
 1.82 s  ball1 passes 0.47 m from cup (cup_front) without touching it: nearest points (0.90, 0.00, 0.04) m and (1.37, 0.00, 0.04) m
 1.83 s  ball1_geom touches ball2_geom again
 1.83 s  ball2_geom leaves floor
 1.83 s  ball1_geom leaves floor
 1.83 s  ball1_geom leaves ball2_geom
 1.86 s  ball2_geom touches floor again
 1.86 s  ball1_geom touches floor again
 2.27 s  ball2_geom touches ramp again
 2.30 s  ball2_geom leaves floor
 2.36 s  ball2_geom touches floor 1 more times between 2.36 s and 6.00 s, still touching at the end
 2.41 s  ball2_geom leaves ramp
 2.57 s  ball3_geom first touches cup_front
 2.58 s  ball3 comes to rest at (1.42, 0.00, 0.05) m
 2.65 s  ball3_geom leaves cup_front
 6.00 s  ball1 is still moving at the end, 0.40 m/s
 6.00 s  ball2 is still moving at the end, 0.06 m/s

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.04) m, moving 3.00 m/s (vx +3.00, vy +0.00, vz +0.00); touching floor | ball2 at (0.40, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.50, 0.00, 0.04) m, at rest; touching floor
0.25 s: ball1 at (0.38, 0.00, 0.04) m, moving 0.30 m/s (vx +0.30, vy -0.00, vz -0.00); touching floor | ball2 at (0.48, 0.00, 0.04) m, moving 0.70 m/s (vx +0.70, vy +0.00, vz +0.00); touching floor | ball3 at (0.72, 0.00, 0.04) m, moving 1.60 m/s (vx +1.60, vy -0.00, vz +0.00); touching floor
0.50 s: ball1 at (0.46, 0.00, 0.04) m, moving 0.31 m/s (vx +0.31, vy -0.00, vz +0.00); touching floor | ball2 at (0.66, 0.00, 0.04) m, moving 0.70 m/s (vx +0.70, vy +0.00, vz +0.00); touching floor | ball3 at (1.11, 0.00, 0.07) m, moving 1.41 m/s (vx +1.36, vy -0.00, vz +0.38); touching ramp
0.75 s: ball1 at (0.53, 0.00, 0.04) m, moving 0.31 m/s (vx +0.31, vy -0.00, vz -0.00); touching floor | ball2 at (0.83, 0.00, 0.04) m, moving 0.70 m/s (vx +0.70, vy +0.00, vz -0.00); touching floor | ball3 at (1.40, 0.00, 0.14) m, moving 0.99 m/s (vx +0.99, vy -0.00, vz -0.07); touching nothing
1.00 s: ball1 at (0.61, 0.00, 0.04) m, moving 0.31 m/s (vx +0.31, vy -0.00, vz +0.00); touching floor | ball2 at (1.01, 0.00, 0.04) m, moving 0.65 m/s (vx +0.63, vy +0.00, vz +0.16); touching ramp | ball3 at (1.64, 0.00, 0.05) m, moving 0.80 m/s (vx +0.80, vy -0.00, vz +0.06); touching cup_back, cup_bottom
1.25 s: ball1 at (0.69, 0.00, 0.04) m, moving 0.31 m/s (vx +0.31, vy -0.00, vz -0.00); touching floor | ball2 at (1.11, 0.00, 0.07) m, moving 0.20 m/s (vx +0.19, vy +0.00, vz +0.05); touching ramp | ball3 at (1.62, 0.00, 0.05) m, moving 0.15 m/s (vx -0.15, vy -0.00, vz -0.00); touching cup_bottom
1.50 s: ball1 at (0.76, 0.00, 0.04) m, moving 0.31 m/s (vx +0.31, vy -0.00, vz -0.00); touching floor | ball2 at (1.11, 0.00, 0.07) m, moving 0.25 m/s (vx -0.24, vy +0.00, vz -0.07); touching ramp | ball3 at (1.58, 0.00, 0.05) m, moving 0.15 m/s (vx -0.15, vy -0.00, vz -0.00); touching cup_bottom
1.75 s: ball1 at (0.84, 0.00, 0.04) m, moving 0.31 m/s (vx +0.31, vy -0.00, vz -0.00); touching floor | ball2 at (0.99, 0.00, 0.04) m, moving 0.66 m/s (vx -0.66, vy +0.00, vz -0.02); touching floor | ball3 at (1.54, 0.00, 0.05) m, moving 0.15 m/s (vx -0.15, vy -0.00, vz +0.00); touching cup_bottom
2.00 s: ball1 at (0.79, 0.00, 0.04) m, moving 0.40 m/s (vx -0.40, vy -0.00, vz -0.00); touching floor | ball2 at (0.96, 0.00, 0.04) m, moving 0.12 m/s (vx +0.12, vy +0.00, vz -0.00); touching floor | ball3 at (1.51, 0.00, 0.05) m, moving 0.15 m/s (vx -0.15, vy -0.00, vz +0.00); touching cup_bottom
2.25 s: ball1 at (0.69, 0.00, 0.04) m, moving 0.40 m/s (vx -0.40, vy -0.00, vz -0.00); touching floor | ball2 at (0.99, 0.00, 0.04) m, moving 0.12 m/s (vx +0.12, vy +0.00, vz -0.00); touching floor | ball3 at (1.47, 0.00, 0.05) m, moving 0.15 m/s (vx -0.15, vy -0.00, vz +0.00); touching cup_bottom
2.50 s: ball1 at (0.59, 0.00, 0.04) m, moving 0.40 m/s (vx -0.40, vy -0.00, vz -0.00); touching floor | ball2 at (0.99, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching floor | ball3 at (1.43, 0.00, 0.05) m, moving 0.15 m/s (vx -0.15, vy -0.00, vz +0.00); touching cup_bottom
2.75 s: ball1 at (0.49, 0.00, 0.04) m, moving 0.40 m/s (vx -0.40, vy -0.00, vz +0.00); touching floor | ball2 at (0.98, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching floor | ball3 at (1.42, 0.00, 0.05) m, at rest; touching cup_bottom
3.00 s: ball1 at (0.39, 0.00, 0.04) m, moving 0.40 m/s (vx -0.40, vy -0.00, vz -0.00); touching floor | ball2 at (0.96, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching floor | ball3 at (1.43, 0.00, 0.05) m, at rest; touching cup_bottom
3.25 s: ball1 at (0.29, 0.00, 0.04) m, moving 0.40 m/s (vx -0.40, vy -0.00, vz +0.00); touching floor | ball2 at (0.95, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching floor | ball3 at (1.43, 0.00, 0.05) m, at rest; touching cup_bottom
3.50 s: ball1 at (0.19, 0.00, 0.04) m, moving 0.40 m/s (vx -0.40, vy -0.00, vz +0.00); touching floor | ball2 at (0.94, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching floor | ball3 at (1.44, 0.00, 0.05) m, at rest; touching cup_bottom
3.75 s: ball1 at (0.09, 0.00, 0.04) m, moving 0.40 m/s (vx -0.40, vy -0.00, vz -0.00); touching floor | ball2 at (0.92, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching floor | ball3 at (1.44, 0.00, 0.05) m, at rest; touching cup_bottom
4.00 s: ball1 at (-0.01, 0.00, 0.04) m, moving 0.40 m/s (vx -0.40, vy -0.00, vz +0.00); touching floor | ball2 at (0.91, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching floor | ball3 at (1.44, 0.00, 0.05) m, at rest; touching cup_bottom
4.25 s: ball1 at (-0.11, 0.00, 0.04) m, moving 0.40 m/s (vx -0.40, vy -0.00, vz +0.00); touching floor | ball2 at (0.90, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching floor | ball3 at (1.45, 0.00, 0.05) m, at rest; touching cup_bottom
4.50 s: ball1 at (-0.21, 0.00, 0.04) m, moving 0.40 m/s (vx -0.40, vy -0.00, vz +0.00); touching floor | ball2 at (0.88, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching floor | ball3 at (1.45, 0.00, 0.05) m, at rest; touching cup_bottom
4.75 s: ball1 at (-0.31, 0.00, 0.04) m, moving 0.40 m/s (vx -0.40, vy -0.00, vz +0.00); touching floor | ball2 at (0.87, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching floor | ball3 at (1.46, 0.00, 0.05) m, at rest; touching cup_bottom
5.00 s: ball1 at (-0.42, 0.00, 0.04) m, moving 0.40 m/s (vx -0.40, vy -0.00, vz -0.00); touching floor | ball2 at (0.85, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching floor | ball3 at (1.46, 0.00, 0.05) m, at rest; touching cup_bottom
5.25 s: ball1 at (-0.52, 0.00, 0.04) m, moving 0.40 m/s (vx -0.40, vy -0.00, vz -0.00); touching floor | ball2 at (0.84, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching floor | ball3 at (1.46, 0.00, 0.05) m, at rest; touching cup_bottom
5.50 s: ball1 at (-0.62, 0.00, 0.04) m, moving 0.40 m/s (vx -0.40, vy -0.00, vz +0.00); touching floor | ball2 at (0.83, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching floor | ball3 at (1.47, 0.00, 0.05) m, at rest; touching cup_bottom
5.75 s: ball1 at (-0.72, 0.00, 0.04) m, moving 0.40 m/s (vx -0.40, vy -0.00, vz -0.00); touching floor | ball2 at (0.81, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching floor | ball3 at (1.47, 0.00, 0.05) m, at rest; touching cup_bottom
6.00 s: ball1 at (-0.82, 0.00, 0.04) m, moving 0.40 m/s (vx -0.40, vy -0.00, vz -0.00); touching floor | ball2 at (0.80, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching floor | ball3 at (1.48, 0.00, 0.05) m, at rest; touching cup_bottom

At the end (6.00 s):
- ball1 at (-0.82, 0.00, 0.04) m, moving 0.40 m/s (vx -0.40, vy -0.00, vz -0.00); touching floor
- ball2 at (0.80, 0.00, 0.04) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching floor
- ball3 at (1.48, 0.00, 0.05) m, at rest; touching cup_bottom
</history>
