MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.00, 0.00, 0.04) m, moving 2.80 m/s (vx +2.80, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2; starts at (0.30, 0.00, 0.04) m, at rest
- ball3: free body; its geoms: ball3; starts at (0.60, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching floor
 0.00 s  ball2 starts touching floor
 0.00 s  ball3 starts touching floor
 0.08 s  ball1 leaves floor
 0.08 s  ball2 leaves floor
 0.08 s  ball1 first touches ball2
 0.08 s  ball2 starts moving
 0.08 s  ball1 leaves ball2
 0.14 s  ball2 touches floor again
 0.15 s  ball1 is at the top of its flight, at (0.23, 0.00, 0.06) m
 0.21 s  ball2 leaves floor
 0.21 s  ball3 leaves floor
 0.21 s  ball2 first touches ball3
 0.21 s  ball3 starts moving
 0.21 s  ball2 leaves ball3
 0.22 s  ball1 touches floor again
 0.25 s  ball3 touches floor again
 0.28 s  ball2 touches floor again
 0.49 s  ball3 leaves floor
 0.49 s  ball3 first touches cup_near_wall
 0.50 s  ball3 leaves cup_near_wall
 0.56 s  ball3 touches cup_near_wall again
 1.16 s  ball2 comes to rest at (0.61, 0.00, 0.04) m
 1.50 s  ball3 first touches cup_base
 1.50 s  ball3 leaves cup_near_wall
 1.52 s  ball3 comes to rest at (0.89, 0.00, 0.04) m
 1.89 s  ball1 comes to rest at (0.53, 0.00, 0.04) m
 2.71 s  ball1 touches ball2 again
 2.71 s  ball1 leaves ball2
 6.00 s  ball1 passes 0.26 m from ball3 without touching it: nearest points (0.59, 0.00, 0.04) m and (0.85, 0.00, 0.04) m
 6.00 s  ball2 passes 0.18 m from cup (cup_near_wall) without touching it: nearest points (0.68, 0.00, 0.03) m and (0.85, 0.00, 0.01) m
 6.00 s  ball1 passes 0.26 m from cup (cup_near_wall) without touching it: nearest points (0.59, 0.00, 0.04) m and (0.85, 0.00, 0.01) m

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.04) m, moving 2.80 m/s (vx +2.80, vy +0.00, vz +0.00); touching floor | ball2 at (0.30, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.60, 0.00, 0.04) m, at rest; touching floor
0.25 s: ball1 at (0.25, 0.00, 0.04) m, moving 0.37 m/s (vx +0.36, vy -0.00, vz +0.08); touching floor | ball2 at (0.52, 0.00, 0.05) m, at rest; touching nothing | ball3 at (0.64, 0.00, 0.04) m, moving 0.90 m/s (vx +0.90, vy +0.00, vz -0.02); touching floor
0.50 s: ball1 at (0.33, 0.00, 0.04) m, moving 0.30 m/s (vx +0.30, vy -0.00, vz -0.01); touching floor | ball2 at (0.55, 0.00, 0.04) m, moving 0.13 m/s (vx +0.13, vy +0.00, vz -0.00); touching floor | ball3 at (0.83, 0.00, 0.04) m, moving 0.50 m/s (vx +0.34, vy -0.00, vz +0.37); touching cup_near_wall
0.75 s: ball1 at (0.39, 0.00, 0.04) m, moving 0.23 m/s (vx +0.23, vy -0.00, vz -0.00); touching floor | ball2 at (0.58, 0.00, 0.04) m, moving 0.09 m/s (vx +0.09, vy +0.00, vz -0.00); touching floor | ball3 at (0.87, 0.00, 0.05) m, at rest; touching cup_near_wall
1.00 s: ball1 at (0.44, 0.00, 0.04) m, moving 0.17 m/s (vx +0.17, vy -0.00, vz -0.00); touching floor | ball2 at (0.60, 0.00, 0.04) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | ball3 at (0.88, 0.00, 0.05) m, at rest; touching cup_near_wall
1.25 s: ball1 at (0.48, 0.00, 0.04) m, moving 0.13 m/s (vx +0.13, vy -0.00, vz -0.00); touching floor | ball2 at (0.61, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.88, 0.00, 0.05) m, at rest; touching cup_near_wall
1.50 s: ball1 at (0.51, 0.00, 0.04) m, moving 0.09 m/s (vx +0.09, vy -0.00, vz -0.00); touching floor | ball2 at (0.62, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.89, 0.00, 0.04) m, moving 0.09 m/s (vx +0.09, vy -0.00, vz +0.01); touching cup_base
1.75 s: ball1 at (0.53, 0.00, 0.04) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | ball2 at (0.63, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.89, 0.00, 0.04) m, at rest; touching cup_base
2.00 s: ball1 at (0.54, 0.00, 0.04) m, at rest; touching floor | ball2 at (0.63, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.89, 0.00, 0.04) m, at rest; touching cup_base
2.25 s: ball1 at (0.55, 0.00, 0.04) m, at rest; touching floor | ball2 at (0.63, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.89, 0.00, 0.04) m, at rest; touching cup_base
(the same through 2.75 s)
3.00 s: ball1 at (0.55, 0.00, 0.04) m, at rest; touching floor | ball2 at (0.64, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.89, 0.00, 0.04) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (0.55, 0.00, 0.04) m, at rest; touching floor
- ball2 at (0.64, 0.00, 0.04) m, at rest; touching floor
- ball3 at (0.89, 0.00, 0.04) m, at rest; touching cup_base
</history>
