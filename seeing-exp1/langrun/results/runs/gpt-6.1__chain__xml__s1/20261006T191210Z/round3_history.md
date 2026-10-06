MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_sphere; starts at (-0.45, 0.00, 0.05) m, moving 2.10 m/s (vx +2.10, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2_sphere; starts at (-0.15, 0.00, 0.05) m, at rest
- ball3: free body; its geoms: ball3_sphere; starts at (0.15, 0.00, 0.05) m, at rest

What happened, in order:
 0.00 s  ball1_sphere starts touching floor
 0.00 s  ball2_sphere starts touching floor
 0.00 s  ball3_sphere starts touching floor
 0.10 s  ball1_sphere leaves floor
 0.10 s  ball1_sphere first touches ball2_sphere
 0.10 s  ball2 starts moving
 0.12 s  ball1_sphere leaves ball2_sphere
 0.20 s  ball1_sphere touches floor again
 0.32 s  ball2_sphere leaves floor
 0.32 s  ball2_sphere first touches ball3_sphere
 0.32 s  ball3 starts moving
 0.34 s  ball2_sphere leaves ball3_sphere
 0.37 s  ball2_sphere touches floor again
 0.58 s  ball1_sphere touches ball2_sphere again
 0.58 s  ball1 passes 0.17 m from ball3 (ball3_sphere) without touching it: nearest points (0.02, 0.00, 0.05) m and (0.20, 0.00, 0.05) m
 0.61 s  ball1_sphere leaves ball2_sphere
 0.61 s  ball1 comes to rest at (-0.02, 0.00, 0.05) m
 0.62 s  ball1 passes 0.28 m from cup (cup_wall_08) without touching it: nearest points (0.03, 0.00, 0.04) m and (0.30, 0.00, 0.00) m
 0.74 s  ball3_sphere first touches cup_wall_08
 1.73 s  ball2 comes to rest at (0.21, 0.00, 0.05) m
 1.88 s  ball3_sphere first touches cup_base
 1.89 s  ball3 comes to rest at (0.57, 0.00, 0.05) m
 1.93 s  ball3_sphere leaves cup_base
 6.00 s  ball2 passes 0.03 m from cup (cup_wall_08) without touching it: nearest points (0.28, 0.00, 0.02) m and (0.30, 0.00, 0.00) m

State every 0.25 s:
0.00 s: ball1 at (-0.45, 0.00, 0.05) m, moving 2.10 m/s (vx +2.10, vy +0.00, vz +0.00); touching floor | ball2 at (-0.15, 0.00, 0.05) m, at rest; touching floor | ball3 at (0.15, 0.00, 0.05) m, at rest; touching floor
0.25 s: ball1 at (-0.18, 0.00, 0.05) m, moving 0.47 m/s (vx +0.47, vy +0.00, vz +0.05); touching floor | ball2 at (-0.01, 0.00, 0.05) m, moving 0.87 m/s (vx +0.87, vy +0.00, vz -0.01); touching floor | ball3 at (0.15, 0.00, 0.05) m, at rest; touching floor
0.50 s: ball1 at (-0.06, 0.00, 0.05) m, moving 0.44 m/s (vx +0.44, vy +0.00, vz +0.00); touching floor | ball2 at (0.07, 0.00, 0.05) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching floor | ball3 at (0.22, 0.00, 0.05) m, moving 0.35 m/s (vx +0.35, vy +0.00, vz +0.00); touching floor
0.75 s: ball1 at (-0.02, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.10, 0.00, 0.05) m, moving 0.18 m/s (vx +0.18, vy +0.00, vz -0.00); touching floor | ball3 at (0.30, 0.00, 0.05) m, moving 0.32 m/s (vx +0.32, vy +0.00, vz +0.00); touching cup_wall_08, floor
1.00 s: ball1 at (-0.02, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.14, 0.00, 0.05) m, moving 0.14 m/s (vx +0.14, vy +0.00, vz -0.00); touching floor | ball3 at (0.38, 0.00, 0.05) m, moving 0.28 m/s (vx +0.28, vy +0.00, vz +0.00); touching cup_wall_08, floor
1.25 s: ball1 at (-0.02, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.17, 0.00, 0.05) m, moving 0.11 m/s (vx +0.11, vy +0.00, vz -0.00); touching floor | ball3 at (0.44, 0.00, 0.05) m, moving 0.25 m/s (vx +0.25, vy +0.00, vz +0.00); touching cup_wall_08, floor
1.50 s: ball1 at (-0.02, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.20, 0.00, 0.05) m, moving 0.07 m/s (vx +0.07, vy +0.00, vz -0.00); touching floor | ball3 at (0.50, 0.00, 0.05) m, moving 0.21 m/s (vx +0.21, vy +0.00, vz -0.00); touching cup_wall_08, floor
1.75 s: ball1 at (-0.02, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.21, 0.00, 0.05) m, at rest; touching floor | ball3 at (0.55, 0.00, 0.05) m, moving 0.18 m/s (vx +0.18, vy +0.00, vz -0.00); touching cup_wall_08, floor
2.00 s: ball1 at (-0.03, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.22, 0.00, 0.05) m, at rest; touching floor | ball3 at (0.57, 0.00, 0.05) m, at rest; touching cup_wall_08, floor
2.25 s: ball1 at (-0.03, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.23, 0.00, 0.05) m, at rest; touching floor | ball3 at (0.56, 0.00, 0.05) m, at rest; touching cup_wall_08, floor
(the same through 2.50 s)
2.75 s: ball1 at (-0.03, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.24, 0.00, 0.05) m, at rest; touching floor | ball3 at (0.56, 0.00, 0.05) m, at rest; touching cup_wall_08, floor
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (-0.03, 0.00, 0.05) m, at rest; touching floor
- ball2 at (0.24, 0.00, 0.05) m, at rest; touching floor
- ball3 at (0.56, 0.00, 0.05) m, at rest; touching cup_wall_08, floor
</history>
