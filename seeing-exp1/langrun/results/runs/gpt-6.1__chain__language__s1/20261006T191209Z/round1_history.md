MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.00, 0.00, 0.04) m, moving 1.80 m/s (vx +1.80, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2; starts at (0.30, 0.00, 0.04) m, at rest
- ball3: free body; its geoms: ball3; starts at (0.60, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching floor
 0.00 s  ball2 starts touching floor
 0.00 s  ball3 starts touching floor
 0.13 s  ball1 leaves floor
 0.13 s  ball2 leaves floor
 0.13 s  ball1 first touches ball2
 0.13 s  ball2 starts moving
 0.13 s  ball1 leaves ball2
 0.17 s  ball2 touches floor again
 0.22 s  ball1 touches floor again
 0.33 s  ball2 leaves floor
 0.33 s  ball2 first touches ball3
 0.33 s  ball3 starts moving
 0.33 s  ball2 leaves ball3
 0.37 s  ball2 touches floor again
 0.76 s  ball3 leaves floor
 0.76 s  ball3 first touches cup_near_wall
 0.79 s  ball3 first touches cup_base
 0.81 s  ball3 leaves cup_near_wall
 1.43 s  ball3 comes to rest at (0.96, 0.00, 0.04) m
 1.46 s  ball2 leaves floor
 1.46 s  ball2 first touches cup_near_wall
 1.55 s  ball2 first touches cup_base
 1.59 s  ball2 leaves cup_near_wall
 3.47 s  ball1 touches ball2 again
 3.47 s  ball1 comes to rest at (0.77, 0.00, 0.04) m
 3.47 s  ball1 leaves ball2
 3.55 s  ball2 comes to rest at (0.86, 0.00, 0.04) m
 6.00 s  ball1 passes 0.10 m from ball3 without touching it: nearest points (0.82, 0.00, 0.04) m and (0.92, 0.00, 0.04) m
 6.00 s  ball1 passes 0.01 m from cup (cup_near_wall) without touching it: nearest points (0.81, 0.00, 0.01) m and (0.81, 0.00, 0.00) m

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.04) m, moving 1.80 m/s (vx +1.80, vy +0.00, vz +0.00); touching floor | ball2 at (0.30, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.60, 0.00, 0.04) m, at rest; touching floor
0.25 s: ball1 at (0.22, 0.00, 0.04) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz +0.04); touching floor | ball2 at (0.44, 0.00, 0.04) m, moving 1.02 m/s (vx +1.02, vy -0.00, vz +0.00); touching floor | ball3 at (0.60, 0.00, 0.04) m, at rest; touching floor
0.50 s: ball1 at (0.27, 0.00, 0.04) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz +0.00); touching floor | ball2 at (0.56, 0.00, 0.04) m, moving 0.25 m/s (vx +0.25, vy -0.00, vz +0.00); touching floor | ball3 at (0.68, 0.00, 0.04) m, moving 0.47 m/s (vx +0.47, vy +0.00, vz -0.00); touching floor
0.75 s: ball1 at (0.31, 0.00, 0.04) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz +0.00); touching floor | ball2 at (0.62, 0.00, 0.04) m, moving 0.25 m/s (vx +0.25, vy -0.00, vz -0.00); touching floor | ball3 at (0.80, 0.00, 0.04) m, moving 0.47 m/s (vx +0.47, vy +0.00, vz +0.00); touching floor
1.00 s: ball1 at (0.35, 0.00, 0.04) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz +0.00); touching floor | ball2 at (0.69, 0.00, 0.04) m, moving 0.25 m/s (vx +0.25, vy -0.00, vz +0.00); touching floor | ball3 at (0.89, 0.00, 0.04) m, moving 0.28 m/s (vx +0.28, vy -0.00, vz -0.00); touching cup_base
1.25 s: ball1 at (0.40, 0.00, 0.04) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz +0.00); touching floor | ball2 at (0.75, 0.00, 0.04) m, moving 0.25 m/s (vx +0.25, vy -0.00, vz +0.00); touching floor | ball3 at (0.94, 0.00, 0.04) m, moving 0.12 m/s (vx +0.12, vy -0.00, vz +0.00); touching cup_base
1.50 s: ball1 at (0.44, 0.00, 0.04) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz +0.00); touching floor | ball2 at (0.81, 0.00, 0.04) m, moving 0.18 m/s (vx +0.18, vy -0.00, vz +0.02); touching cup_near_wall | ball3 at (0.96, 0.00, 0.04) m, at rest; touching cup_base
1.75 s: ball1 at (0.48, 0.00, 0.04) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz +0.00); touching floor | ball2 at (0.84, 0.00, 0.04) m, moving 0.07 m/s (vx +0.07, vy -0.00, vz -0.00); touching cup_base | ball3 at (0.96, 0.00, 0.04) m, at rest; touching cup_base
2.00 s: ball1 at (0.52, 0.00, 0.04) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz +0.00); touching floor | ball2 at (0.85, 0.00, 0.04) m, at rest; touching cup_base | ball3 at (0.96, 0.00, 0.04) m, at rest; touching cup_base
2.25 s: ball1 at (0.57, 0.00, 0.04) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz +0.00); touching floor | ball2 at (0.85, 0.00, 0.04) m, at rest; touching cup_base | ball3 at (0.96, 0.00, 0.04) m, at rest; touching cup_base
2.50 s: ball1 at (0.61, 0.00, 0.04) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz +0.00); touching floor | ball2 at (0.85, 0.00, 0.04) m, at rest; touching cup_base | ball3 at (0.96, 0.00, 0.04) m, at rest; touching cup_base
2.75 s: ball1 at (0.65, 0.00, 0.04) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz +0.00); touching floor | ball2 at (0.85, 0.00, 0.04) m, at rest; touching cup_base | ball3 at (0.96, 0.00, 0.04) m, at rest; touching cup_base
3.00 s: ball1 at (0.69, 0.00, 0.04) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz +0.00); touching floor | ball2 at (0.85, 0.00, 0.04) m, at rest; touching cup_base | ball3 at (0.96, 0.00, 0.04) m, at rest; touching cup_base
3.25 s: ball1 at (0.74, 0.00, 0.04) m, moving 0.17 m/s (vx +0.17, vy +0.00, vz +0.00); touching floor | ball2 at (0.85, 0.00, 0.04) m, at rest; touching cup_base | ball3 at (0.96, 0.00, 0.04) m, at rest; touching cup_base
3.50 s: ball1 at (0.77, 0.00, 0.04) m, at rest; touching floor | ball2 at (0.86, 0.00, 0.04) m, moving 0.07 m/s (vx +0.07, vy -0.00, vz +0.00); touching cup_base | ball3 at (0.96, 0.00, 0.04) m, at rest; touching cup_base
3.75 s: ball1 at (0.78, 0.00, 0.04) m, at rest; touching floor | ball2 at (0.86, 0.00, 0.04) m, at rest; touching cup_base | ball3 at (0.96, 0.00, 0.04) m, at rest; touching cup_base
4.00 s: ball1 at (0.78, 0.00, 0.04) m, at rest; touching floor | ball2 at (0.87, 0.00, 0.04) m, at rest; touching cup_base | ball3 at (0.96, 0.00, 0.04) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (0.78, 0.00, 0.04) m, at rest; touching floor
- ball2 at (0.87, 0.00, 0.04) m, at rest; touching cup_base
- ball3 at (0.96, 0.00, 0.04) m, at rest; touching cup_base
</history>
