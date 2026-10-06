MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.50, 0.00, 0.04) m, moving 4.00 m/s (vx +4.00, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2; starts at (0.80, 0.00, 0.04) m, at rest
- ball3: free body; its geoms: ball3; starts at (1.10, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching floor
 0.00 s  ball2 starts touching floor
 0.00 s  ball3 starts touching floor
 0.05 s  ball1 leaves floor
 0.06 s  ball2 leaves floor
 0.06 s  ball1 first touches ball2
 0.06 s  ball2 starts moving
 0.06 s  ball1 leaves ball2
 0.09 s  ball1 touches floor again
 0.09 s  ball1 leaves floor
 0.13 s  ball1 touches floor again
 0.14 s  ball2 first touches ball3
 0.14 s  ball3 starts moving
 0.14 s  ball2 leaves ball3
 0.16 s  ball2 touches floor again
 0.34 s  ball1 leaves floor
 0.34 s  ball2 leaves floor
 0.34 s  ball1 touches ball2 again
 0.34 s  ball1 leaves ball2
 0.37 s  ball2 touches floor again
 0.38 s  ball1 touches floor again
 0.67 s  ball3 leaves floor
 0.67 s  ball3 first touches cup_near_wall
 0.68 s  ball3 leaves cup_near_wall
 0.75 s  ball3 is at the top of its flight, at (1.89, 0.00, 0.07) m
 0.80 s  ball3 touches cup_near_wall again
 0.82 s  ball3 leaves cup_near_wall
 0.86 s  ball3 touches cup_near_wall again
 0.86 s  ball3 leaves cup_near_wall
 0.88 s  ball3 first touches cup_base
 0.96 s  ball2 leaves floor
 0.96 s  ball2 first touches cup_near_wall
 0.97 s  ball2 leaves cup_near_wall
 1.06 s  ball2 touches cup_near_wall again
 1.13 s  ball2 touches ball3 again
 1.13 s  ball2 leaves ball3
 1.78 s  ball1 touches ball2 again
 1.79 s  ball2 touches ball3 again
 1.79 s  ball2 leaves ball3
 1.79 s  ball1 passes 0.08 m from ball3 without touching it: nearest points (1.86, 0.00, 0.04) m and (1.93, 0.00, 0.04) m
 1.80 s  ball1 comes to rest at (1.82, 0.00, 0.04) m
 1.80 s  ball1 leaves ball2
 1.83 s  ball2 comes to rest at (1.90, 0.00, 0.05) m
 1.85 s  ball3 comes to rest at (1.98, 0.00, 0.04) m
 1.91 s  ball1 touches ball2 again
 1.91 s  ball1 leaves ball2
 1.96 s  ball1 touches ball2 2 more times between 1.96 s and 2.34 s
 2.34 s  ball1 passes 0.03 m from cup (cup_near_wall) without touching it: nearest points (1.86, 0.00, 0.03) m and (1.89, 0.00, 0.01) m

State every 0.25 s:
0.00 s: ball1 at (0.50, 0.00, 0.04) m, moving 4.00 m/s (vx +4.00, vy +0.00, vz +0.00); touching floor | ball2 at (0.80, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.10, 0.00, 0.04) m, at rest; touching floor
0.25 s: ball1 at (0.95, 0.00, 0.04) m, moving 1.44 m/s (vx +1.44, vy +0.00, vz +0.03); touching floor | ball2 at (1.10, 0.00, 0.04) m, moving 0.64 m/s (vx +0.64, vy +0.00, vz +0.01); touching floor | ball3 at (1.28, 0.00, 0.04) m, moving 1.46 m/s (vx +1.46, vy -0.00, vz +0.03); touching floor
0.50 s: ball1 at (1.19, 0.00, 0.04) m, moving 0.71 m/s (vx +0.71, vy +0.00, vz -0.01); touching floor | ball2 at (1.35, 0.00, 0.04) m, moving 1.18 m/s (vx +1.18, vy -0.00, vz +0.03); touching floor | ball3 at (1.64, 0.00, 0.04) m, moving 1.37 m/s (vx +1.37, vy -0.00, vz -0.00); touching nothing
0.75 s: ball1 at (1.36, 0.00, 0.04) m, moving 0.62 m/s (vx +0.62, vy +0.00, vz +0.01); touching floor | ball2 at (1.64, 0.00, 0.04) m, moving 1.09 m/s (vx +1.09, vy -0.00, vz +0.02); touching floor | ball3 at (1.89, 0.00, 0.07) m, moving 0.35 m/s (vx +0.35, vy -0.00, vz -0.05); touching nothing
1.00 s: ball1 at (1.50, 0.00, 0.04) m, moving 0.53 m/s (vx +0.53, vy +0.00, vz +0.00); touching floor | ball2 at (1.87, 0.00, 0.06) m, moving 0.33 m/s (vx +0.21, vy -0.00, vz +0.25); touching nothing | ball3 at (1.96, 0.00, 0.04) m, moving 0.14 m/s (vx +0.14, vy -0.00, vz +0.00); touching cup_base
1.25 s: ball1 at (1.62, 0.00, 0.04) m, moving 0.45 m/s (vx +0.45, vy +0.00, vz +0.01); touching floor | ball2 at (1.89, 0.00, 0.05) m, at rest; touching cup_near_wall | ball3 at (1.97, 0.00, 0.04) m, at rest; touching cup_base
1.50 s: ball1 at (1.72, 0.00, 0.04) m, moving 0.37 m/s (vx +0.37, vy +0.00, vz +0.00); touching floor | ball2 at (1.89, 0.00, 0.05) m, at rest; touching cup_near_wall | ball3 at (1.97, 0.00, 0.04) m, at rest; touching cup_base
1.75 s: ball1 at (1.81, 0.00, 0.04) m, moving 0.29 m/s (vx +0.29, vy +0.00, vz -0.01); touching floor | ball2 at (1.89, 0.00, 0.05) m, at rest; touching cup_near_wall | ball3 at (1.97, 0.00, 0.04) m, at rest; touching cup_base
2.00 s: ball1 at (1.82, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.90, 0.00, 0.05) m, at rest; touching cup_near_wall | ball3 at (1.98, 0.00, 0.04) m, at rest; touching cup_base
2.25 s: ball1 at (1.82, 0.00, 0.04) m, at rest; touching ball2, floor | ball2 at (1.90, 0.00, 0.05) m, at rest; touching ball1, cup_near_wall | ball3 at (1.98, 0.00, 0.04) m, at rest; touching cup_base
2.50 s: ball1 at (1.82, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.90, 0.00, 0.05) m, at rest; touching cup_near_wall | ball3 at (1.98, 0.00, 0.04) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (1.82, 0.00, 0.04) m, at rest; touching floor
- ball2 at (1.90, 0.00, 0.05) m, at rest; touching cup_near_wall
- ball3 at (1.98, 0.00, 0.04) m, at rest; touching cup_base
</history>
