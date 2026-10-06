MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_sphere; starts at (-0.60, 0.00, 0.06) m, moving 1.80 m/s (vx +1.80, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2_sphere; starts at (-0.20, 0.00, 0.06) m, at rest
- ball3: free body; its geoms: ball3_sphere; starts at (0.20, 0.00, 0.06) m, at rest

What happened, in order:
 0.00 s  ball1_sphere starts touching floor
 0.00 s  ball2_sphere starts touching floor
 0.00 s  ball3_sphere starts touching floor
 0.16 s  ball1_sphere leaves floor
 0.16 s  ball1_sphere first touches ball2_sphere
 0.16 s  ball2 starts moving
 0.17 s  ball1_sphere leaves ball2_sphere
 0.21 s  ball1_sphere touches floor again
 0.55 s  ball1 passes 0.37 m from ball3 (ball3_sphere) without touching it: nearest points (-0.23, 0.00, 0.06) m and (0.14, 0.00, 0.06) m
 0.56 s  ball2_sphere first touches ball3_sphere
 0.56 s  ball3 starts moving
 0.56 s  ball2_sphere leaves ball3_sphere
 0.74 s  ball1 comes to rest at (-0.28, 0.00, 0.06) m
 0.95 s  ball3_sphere leaves floor
 0.95 s  ball3_sphere first touches cup_bottom
 1.20 s  ball2 comes to rest at (0.16, 0.00, 0.06) m
 1.52 s  ball3 comes to rest at (0.47, 0.00, 0.06) m
 4.14 s  ball2 passes 0.16 m from cup (cup_bottom) without touching it: nearest points (0.23, 0.00, 0.04) m and (0.38, 0.00, 0.00) m

State every 0.25 s:
0.00 s: ball1 at (-0.60, 0.00, 0.06) m, moving 1.80 m/s (vx +1.80, vy +0.00, vz +0.00); touching floor | ball2 at (-0.20, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.20, 0.00, 0.06) m, at rest; touching floor
0.25 s: ball1 at (-0.33, 0.00, 0.06) m, moving 0.15 m/s (vx +0.15, vy +0.00, vz -0.03); touching nothing | ball2 at (-0.13, 0.00, 0.06) m, moving 0.72 m/s (vx +0.72, vy +0.00, vz -0.01); touching nothing | ball3 at (0.20, 0.00, 0.06) m, at rest; touching floor
0.50 s: ball1 at (-0.29, 0.00, 0.06) m, moving 0.11 m/s (vx +0.11, vy +0.00, vz -0.02); touching nothing | ball2 at (0.04, 0.00, 0.06) m, moving 0.67 m/s (vx +0.66, vy +0.00, vz -0.03); touching nothing | ball3 at (0.20, 0.00, 0.06) m, at rest; touching floor
0.75 s: ball1 at (-0.27, 0.00, 0.06) m, at rest; touching floor | ball2 at (0.11, 0.00, 0.06) m, moving 0.15 m/s (vx +0.15, vy +0.00, vz +0.00); touching floor | ball3 at (0.29, 0.00, 0.06) m, moving 0.41 m/s (vx +0.41, vy +0.00, vz +0.00); touching floor
1.00 s: ball1 at (-0.27, 0.00, 0.06) m, at rest; touching floor | ball2 at (0.15, 0.00, 0.06) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz +0.00); touching floor | ball3 at (0.38, 0.00, 0.06) m, moving 0.29 m/s (vx +0.29, vy +0.00, vz +0.02); touching cup_bottom
1.25 s: ball1 at (-0.27, 0.00, 0.06) m, at rest; touching floor | ball2 at (0.16, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.44, 0.00, 0.06) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz +0.01); touching cup_bottom
1.50 s: ball1 at (-0.27, 0.00, 0.06) m, at rest; touching floor | ball2 at (0.17, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.47, 0.00, 0.06) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching cup_bottom
1.75 s: ball1 at (-0.27, 0.00, 0.06) m, at rest; touching floor | ball2 at (0.17, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.47, 0.00, 0.06) m, at rest; touching cup_bottom
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (-0.27, 0.00, 0.06) m, at rest; touching floor
- ball2 at (0.17, 0.00, 0.06) m, at rest; touching floor
- ball3 at (0.47, 0.00, 0.06) m, at rest; touching cup_bottom
</history>
