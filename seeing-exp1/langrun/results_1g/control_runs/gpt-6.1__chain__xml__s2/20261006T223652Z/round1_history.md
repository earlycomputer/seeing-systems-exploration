MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_sphere; starts at (-0.48, 0.00, 0.06) m, moving 1.10 m/s (vx +1.10, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2_sphere; starts at (-0.24, 0.00, 0.06) m, at rest
- ball3: free body; its geoms: ball3_sphere; starts at (0.00, 0.00, 0.06) m, at rest

What happened, in order:
 0.01 s  ball2 starts moving
 0.01 s  ball3 starts moving
 0.01 s  ball1_sphere first touches floor
 0.01 s  ball2_sphere first touches floor
 0.01 s  ball3_sphere first touches floor
 0.11 s  ball1_sphere first touches ball2_sphere
 0.12 s  ball1_sphere leaves floor
 0.12 s  ball1_sphere leaves ball2_sphere
 0.13 s  ball2_sphere leaves floor
 0.15 s  ball1_sphere touches floor again
 0.17 s  ball2_sphere touches floor again
 0.27 s  ball1 passes 0.20 m from ball3 (ball3_sphere) without touching it: nearest points (-0.26, 0.00, 0.06) m and (-0.06, 0.00, 0.06) m
 0.27 s  ball2_sphere first touches ball3_sphere
 0.28 s  ball2_sphere leaves ball3_sphere
 0.61 s  ball2 comes to rest at (-0.08, 0.00, 0.06) m
 0.62 s  ball1 comes to rest at (-0.28, 0.00, 0.06) m
 1.19 s  ball3_sphere first touches cup_bottom
 1.21 s  ball1 passes 0.37 m from cup (cup_wall_08) without touching it: nearest points (-0.22, 0.00, 0.05) m and (0.15, 0.00, 0.00) m
 1.21 s  ball3_sphere leaves cup_bottom
 1.26 s  ball3 comes to rest at (0.47, 0.00, 0.06) m
 3.30 s  ball2 passes 0.18 m from cup (cup_wall_08) without touching it: nearest points (-0.02, 0.00, 0.04) m and (0.15, 0.00, 0.00) m

State every 0.25 s:
0.00 s: ball1 at (-0.48, 0.00, 0.06) m, moving 1.10 m/s (vx +1.10, vy +0.00, vz +0.00); touching nothing | ball2 at (-0.24, 0.00, 0.06) m, at rest; touching nothing | ball3 at (0.00, 0.00, 0.06) m, at rest; touching nothing
0.25 s: ball1 at (-0.33, 0.00, 0.06) m, moving 0.22 m/s (vx +0.22, vy +0.00, vz -0.01); touching nothing | ball2 at (-0.14, 0.00, 0.06) m, moving 0.73 m/s (vx +0.73, vy +0.00, vz +0.01); touching nothing | ball3 at (0.00, 0.00, 0.06) m, at rest; touching floor
0.50 s: ball1 at (-0.29, 0.00, 0.06) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz -0.01); touching nothing | ball2 at (-0.09, 0.00, 0.06) m, moving 0.09 m/s (vx +0.09, vy +0.00, vz +0.00); touching floor | ball3 at (0.12, 0.00, 0.06) m, moving 0.54 m/s (vx +0.54, vy +0.00, vz -0.01); touching nothing
0.75 s: ball1 at (-0.27, 0.00, 0.06) m, at rest; touching floor | ball2 at (-0.08, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.25, 0.00, 0.06) m, moving 0.51 m/s (vx +0.51, vy +0.00, vz +0.01); touching floor
1.00 s: ball1 at (-0.27, 0.00, 0.06) m, at rest; touching floor | ball2 at (-0.08, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.38, 0.00, 0.06) m, moving 0.49 m/s (vx +0.49, vy +0.00, vz +0.01); touching floor
1.25 s: ball1 at (-0.27, 0.00, 0.06) m, at rest; touching floor | ball2 at (-0.08, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.47, 0.00, 0.06) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz +0.00); touching floor
1.50 s: ball1 at (-0.27, 0.00, 0.06) m, at rest; touching floor | ball2 at (-0.08, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.46, 0.00, 0.06) m, at rest; touching floor
1.75 s: ball1 at (-0.27, 0.00, 0.06) m, at rest; touching floor | ball2 at (-0.08, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.45, 0.00, 0.06) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (-0.27, 0.00, 0.06) m, at rest; touching floor
- ball2 at (-0.08, 0.00, 0.06) m, at rest; touching floor
- ball3 at (0.45, 0.00, 0.06) m, at rest; touching floor
</history>
