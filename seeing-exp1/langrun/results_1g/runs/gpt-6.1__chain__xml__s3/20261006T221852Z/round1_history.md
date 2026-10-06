Your expectations, checked against the run (3 of 3 hold):

- holds: ball1 touches ball2 (first touch at 0.10 s)
- holds: ball2 touches ball3 (first touch at 0.25 s)
- holds: ball3 comes to rest in cup (ball3 at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_sphere; starts at (-1.10, 0.00, 0.06) m, moving 3.80 m/s (vx +3.80, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2_sphere; starts at (-0.60, 0.00, 0.06) m, at rest
- ball3: free body; its geoms: ball3_sphere; starts at (-0.10, 0.00, 0.06) m, at rest

What happened, in order:
 0.01 s  ball2 starts moving
 0.01 s  ball3 starts moving
 0.01 s  ball1_sphere first touches floor
 0.01 s  ball1_sphere leaves floor
 0.01 s  ball2_sphere first touches floor
 0.01 s  ball3_sphere first touches floor
 0.08 s  ball1_sphere touches floor again
 0.08 s  ball1_sphere leaves floor
 0.10 s  ball1_sphere first touches ball2_sphere
 0.11 s  ball1_sphere leaves ball2_sphere
 0.13 s  ball2_sphere leaves floor
 0.16 s  ball1_sphere touches floor again
 0.16 s  ball1_sphere leaves floor
 0.21 s  ball2_sphere touches floor again
 0.22 s  ball1_sphere touches floor again
 0.23 s  ball1_sphere leaves floor
 0.23 s  ball2_sphere leaves floor
 0.25 s  ball1 passes 0.36 m from ball3 (ball3_sphere) without touching it: nearest points (-0.52, 0.00, 0.06) m and (-0.16, 0.00, 0.06) m
 0.25 s  ball3_sphere leaves floor
 0.25 s  ball2_sphere first touches ball3_sphere
 0.26 s  ball2_sphere leaves ball3_sphere
 0.27 s  ball2_sphere touches floor again
 0.28 s  ball1_sphere touches floor 2 more times between 0.28 s and 6.00 s, still touching at the end
 0.29 s  ball3_sphere touches floor again
 0.29 s  ball3_sphere leaves floor
 0.32 s  ball3_sphere touches floor again
 0.67 s  ball1_sphere touches ball2_sphere again
 0.68 s  ball1_sphere leaves ball2_sphere
 0.91 s  ball3_sphere first touches cup_base
 0.93 s  ball3_sphere leaves cup_base
 1.09 s  ball1 comes to rest at (-0.01, 0.00, 0.06) m
 1.16 s  ball3 comes to rest at (0.80, 0.00, 0.06) m
 1.40 s  ball2 comes to rest at (0.24, 0.00, 0.06) m
 6.00 s  ball2 passes 0.09 m from cup (cup_wall08) without touching it: nearest points (0.30, 0.00, 0.03) m and (0.38, 0.00, 0.00) m
 6.00 s  ball1 passes 0.34 m from cup (cup_wall08) without touching it: nearest points (0.05, 0.00, 0.05) m and (0.38, 0.00, 0.00) m

State every 0.25 s:
0.00 s: ball1 at (-1.10, 0.00, 0.06) m, moving 3.80 m/s (vx +3.80, vy +0.00, vz +0.00); touching nothing | ball2 at (-0.60, 0.00, 0.06) m, at rest; touching nothing | ball3 at (-0.10, 0.00, 0.06) m, at rest; touching nothing
0.25 s: ball1 at (-0.59, 0.00, 0.06) m, moving 1.17 m/s (vx +1.17, vy +0.00, vz +0.04); touching nothing | ball2 at (-0.22, 0.00, 0.06) m, moving 2.28 m/s (vx +2.28, vy +0.00, vz -0.01); touching nothing | ball3 at (-0.10, 0.00, 0.06) m, at rest; touching floor
0.50 s: ball1 at (-0.30, 0.00, 0.06) m, moving 1.04 m/s (vx +1.04, vy +0.00, vz -0.00); touching nothing | ball2 at (-0.08, 0.00, 0.06) m, moving 0.49 m/s (vx +0.49, vy +0.00, vz -0.04); touching nothing | ball3 at (0.27, 0.00, 0.06) m, moving 1.38 m/s (vx +1.38, vy +0.00, vz +0.04); touching floor
0.75 s: ball1 at (-0.10, 0.00, 0.06) m, moving 0.44 m/s (vx +0.44, vy +0.00, vz +0.03); touching floor | ball2 at (0.03, 0.00, 0.06) m, moving 0.58 m/s (vx +0.58, vy +0.00, vz +0.03); touching floor | ball3 at (0.61, 0.00, 0.06) m, moving 1.32 m/s (vx +1.32, vy +0.00, vz -0.00); touching nothing
1.00 s: ball1 at (-0.02, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy +0.00, vz -0.00); touching nothing | ball2 at (0.15, 0.00, 0.06) m, moving 0.38 m/s (vx +0.38, vy +0.00, vz -0.00); touching nothing | ball3 at (0.81, 0.00, 0.06) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz +0.00); touching floor
1.25 s: ball1 at (-0.01, 0.00, 0.06) m, at rest; touching floor | ball2 at (0.22, 0.00, 0.06) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz -0.01); touching nothing | ball3 at (0.80, 0.00, 0.06) m, at rest; touching floor
1.50 s: ball1 at (-0.01, 0.00, 0.06) m, at rest; touching floor | ball2 at (0.24, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.80, 0.00, 0.06) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (-0.01, 0.00, 0.06) m, at rest; touching floor
- ball2 at (0.24, 0.00, 0.06) m, at rest; touching floor
- ball3 at (0.80, 0.00, 0.06) m, at rest; touching floor
</history>
