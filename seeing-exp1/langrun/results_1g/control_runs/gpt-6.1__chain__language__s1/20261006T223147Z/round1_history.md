MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.00, 0.00, 0.05) m, moving 1.20 m/s (vx +1.20, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2; starts at (0.30, 0.00, 0.05) m, at rest
- ball3: free body; its geoms: ball3; starts at (0.60, 0.00, 0.05) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching floor
 0.00 s  ball2 starts touching floor
 0.00 s  ball3 starts touching floor
 0.17 s  ball1 leaves floor
 0.17 s  ball2 leaves floor
 0.17 s  ball1 first touches ball2
 0.17 s  ball2 starts moving
 0.17 s  ball1 leaves ball2
 0.20 s  ball2 touches floor again
 0.22 s  ball1 touches floor again
 0.49 s  ball2 first touches ball3
 0.49 s  ball3 starts moving
 0.49 s  ball2 leaves ball3
 1.20 s  ball3 leaves floor
 1.20 s  ball3 first touches cup_near_wall
 1.26 s  ball3 first touches cup_base
 1.30 s  ball3 leaves cup_near_wall
 2.00 s  ball2 touches ball3 again
 2.00 s  ball2 leaves ball3
 2.32 s  ball1 touches ball2 again
 2.33 s  ball1 leaves ball2
 2.47 s  ball2 leaves floor
 2.47 s  ball2 first touches cup_near_wall
 2.49 s  ball2 touches ball3 again
 2.49 s  ball2 leaves ball3
 2.50 s  ball3 comes to rest at (0.89, 0.00, 0.05) m
 2.54 s  ball2 touches floor again
 2.54 s  ball2 leaves cup_near_wall
 2.58 s  ball1 passes 0.11 m from ball3 without touching it: nearest points (0.73, 0.00, 0.05) m and (0.84, 0.00, 0.05) m
 2.58 s  ball1 passes 0.07 m from cup (cup_near_wall) without touching it: nearest points (0.73, 0.00, 0.03) m and (0.80, 0.00, 0.00) m
 2.58 s  ball1 touches ball2 again
 2.58 s  ball1 comes to rest at (0.68, 0.00, 0.05) m
 2.58 s  ball2 comes to rest at (0.78, 0.00, 0.05) m
 2.59 s  ball1 leaves ball2
 2.70 s  ball2 touches cup_near_wall again
 2.73 s  ball2 leaves cup_near_wall

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.05) m, moving 1.20 m/s (vx +1.20, vy +0.00, vz +0.00); touching floor | ball2 at (0.30, 0.00, 0.05) m, at rest; touching floor | ball3 at (0.60, 0.00, 0.05) m, at rest; touching floor
0.25 s: ball1 at (0.21, 0.00, 0.05) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz +0.04); touching floor | ball2 at (0.36, 0.00, 0.05) m, moving 0.60 m/s (vx +0.60, vy +0.00, vz +0.01); touching floor | ball3 at (0.60, 0.00, 0.05) m, at rest; touching floor
0.50 s: ball1 at (0.27, 0.00, 0.05) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz +0.00); touching floor | ball2 at (0.50, 0.00, 0.05) m, moving 0.12 m/s (vx +0.12, vy +0.00, vz -0.02); touching nothing | ball3 at (0.60, 0.00, 0.05) m, moving 0.33 m/s (vx +0.33, vy -0.00, vz -0.00); touching nothing
0.75 s: ball1 at (0.32, 0.00, 0.05) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz +0.00); touching floor | ball2 at (0.55, 0.00, 0.05) m, moving 0.18 m/s (vx +0.18, vy +0.00, vz -0.00); touching floor | ball3 at (0.67, 0.00, 0.05) m, moving 0.26 m/s (vx +0.26, vy +0.00, vz +0.00); touching floor
1.00 s: ball1 at (0.38, 0.00, 0.05) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz +0.00); touching floor | ball2 at (0.59, 0.00, 0.05) m, moving 0.18 m/s (vx +0.18, vy +0.00, vz +0.00); touching floor | ball3 at (0.73, 0.00, 0.05) m, moving 0.26 m/s (vx +0.26, vy +0.00, vz +0.00); touching floor
1.25 s: ball1 at (0.43, 0.00, 0.05) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz +0.00); touching floor | ball2 at (0.63, 0.00, 0.05) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz +0.00); touching floor | ball3 at (0.80, 0.00, 0.05) m, moving 0.20 m/s (vx +0.20, vy +0.00, vz +0.00); touching cup_near_wall
1.50 s: ball1 at (0.49, 0.00, 0.05) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz +0.00); touching floor | ball2 at (0.68, 0.00, 0.05) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz +0.00); touching floor | ball3 at (0.83, 0.00, 0.05) m, moving 0.11 m/s (vx +0.11, vy +0.00, vz -0.00); touching cup_base
1.75 s: ball1 at (0.54, 0.00, 0.05) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz +0.00); touching floor | ball2 at (0.72, 0.00, 0.05) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz +0.00); touching floor | ball3 at (0.85, 0.00, 0.05) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz -0.00); touching cup_base
2.00 s: ball1 at (0.60, 0.00, 0.05) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz +0.00); touching floor | ball2 at (0.76, 0.00, 0.05) m, moving 0.11 m/s (vx +0.11, vy +0.00, vz +0.01); touching ball3, floor | ball3 at (0.86, 0.00, 0.05) m, moving 0.05 m/s (vx +0.05, vy +0.00, vz +0.00); touching ball2, cup_base
2.25 s: ball1 at (0.65, 0.00, 0.05) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz +0.00); touching floor | ball2 at (0.77, 0.00, 0.05) m, at rest; touching floor | ball3 at (0.88, 0.00, 0.05) m, at rest; touching cup_base
2.50 s: ball1 at (0.68, 0.00, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor | ball2 at (0.79, 0.00, 0.05) m, at rest; touching cup_near_wall | ball3 at (0.89, 0.00, 0.05) m, moving 0.05 m/s (vx +0.05, vy -0.00, vz -0.00); touching cup_base
2.75 s: ball1 at (0.68, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.78, 0.00, 0.05) m, at rest; touching floor | ball3 at (0.90, 0.00, 0.05) m, at rest; touching cup_base
(the same through 3.00 s)
3.25 s: ball1 at (0.67, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.78, 0.00, 0.05) m, at rest; touching floor | ball3 at (0.90, 0.00, 0.05) m, at rest; touching cup_base
(the same through 3.50 s)
3.75 s: ball1 at (0.66, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.78, 0.00, 0.05) m, at rest; touching floor | ball3 at (0.90, 0.00, 0.05) m, at rest; touching cup_base
(the same through 4.25 s)
4.50 s: ball1 at (0.65, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.77, 0.00, 0.05) m, at rest; touching floor | ball3 at (0.90, 0.00, 0.05) m, at rest; touching cup_base
(the same through 5.00 s)
5.25 s: ball1 at (0.64, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.77, 0.00, 0.05) m, at rest; touching floor | ball3 at (0.90, 0.00, 0.05) m, at rest; touching cup_base
(the same through 5.50 s)
5.75 s: ball1 at (0.63, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.77, 0.00, 0.05) m, at rest; touching floor | ball3 at (0.90, 0.00, 0.05) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (0.63, 0.00, 0.05) m, at rest; touching floor
- ball2 at (0.77, 0.00, 0.05) m, at rest; touching floor
- ball3 at (0.90, 0.00, 0.05) m, at rest; touching cup_base
</history>
