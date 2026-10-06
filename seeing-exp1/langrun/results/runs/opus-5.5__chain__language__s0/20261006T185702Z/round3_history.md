MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.50, 0.00, 0.03) m, moving 5.00 m/s (vx +5.00, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2; starts at (0.80, 0.00, 0.03) m, at rest
- ball3: free body; its geoms: ball3; starts at (1.10, 0.00, 0.03) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching floor
 0.00 s  ball2 starts touching floor
 0.00 s  ball3 starts touching floor
 0.00 s  ball1 leaves floor
 0.05 s  ball2 leaves floor
 0.05 s  ball1 first touches ball2
 0.05 s  ball2 starts moving
 0.06 s  ball1 leaves ball2
 0.12 s  ball1 passes 0.27 m from ball3 without touching it: nearest points (0.80, 0.00, 0.06) m and (1.07, 0.00, 0.03) m
 0.13 s  ball2 first touches ball3
 0.13 s  ball1 is at the top of its flight, at (0.77, 0.00, 0.06) m
 0.13 s  ball3 starts moving
 0.13 s  ball2 leaves ball3
 0.20 s  ball1 touches floor again
 0.22 s  ball2 touches floor again
 0.25 s  ball1 comes to rest at (0.79, 0.00, 0.03) m
 0.29 s  ball3 leaves floor
 0.29 s  ball3 first touches cup_near_wall
 0.29 s  ball3 leaves cup_near_wall
 0.35 s  ball3 is at the top of its flight, at (1.47, 0.00, 0.05) m
 0.41 s  ball3 first touches cup_base
 0.42 s  ball3 leaves cup_base
 0.48 s  ball3 touches cup_base again
 0.48 s  ball3 leaves cup_base
 0.51 s  ball3 first touches cup_far_wall
 0.53 s  ball3 leaves cup_far_wall
 0.56 s  ball3 touches cup_base again
 0.59 s  ball3 comes to rest at (1.66, 0.00, 0.03) m
 0.96 s  ball2 first touches cup_near_wall
 0.96 s  ball2 leaves floor
 1.06 s  ball2 touches floor again
 1.06 s  ball2 leaves cup_near_wall
 1.52 s  ball2 comes to rest at (1.34, 0.00, 0.03) m

State every 0.25 s:
0.00 s: ball1 at (0.50, 0.00, 0.03) m, moving 5.00 m/s (vx +5.00, vy +0.00, vz +0.00); touching floor | ball2 at (0.80, 0.00, 0.03) m, at rest; touching floor | ball3 at (1.10, 0.00, 0.03) m, at rest; touching floor
0.25 s: ball1 at (0.79, 0.00, 0.03) m, at rest; touching floor | ball2 at (1.13, 0.00, 0.03) m, moving 0.52 m/s (vx +0.51, vy -0.00, vz +0.08); touching floor | ball3 at (1.32, 0.00, 0.03) m, moving 1.66 m/s (vx +1.66, vy +0.00, vz -0.01); touching floor
0.50 s: ball1 at (0.79, 0.00, 0.03) m, at rest; touching floor | ball2 at (1.24, 0.00, 0.03) m, moving 0.40 m/s (vx +0.40, vy -0.00, vz -0.01); touching floor | ball3 at (1.65, 0.00, 0.04) m, moving 1.12 m/s (vx +1.12, vy +0.00, vz +0.04); touching nothing
0.75 s: ball1 at (0.79, 0.00, 0.03) m, at rest; touching floor | ball2 at (1.33, 0.00, 0.03) m, moving 0.29 m/s (vx +0.29, vy -0.00, vz +0.00); touching floor | ball3 at (1.65, 0.00, 0.03) m, at rest; touching cup_base
1.00 s: ball1 at (0.79, 0.00, 0.03) m, at rest; touching floor | ball2 at (1.38, 0.00, 0.03) m, at rest; touching cup_near_wall | ball3 at (1.65, 0.00, 0.03) m, at rest; touching cup_base
1.25 s: ball1 at (0.79, 0.00, 0.03) m, at rest; touching floor | ball2 at (1.36, 0.00, 0.03) m, moving 0.10 m/s (vx -0.10, vy -0.00, vz -0.00); touching floor | ball3 at (1.65, 0.00, 0.03) m, at rest; touching cup_base
1.50 s: ball1 at (0.79, 0.00, 0.03) m, at rest; touching floor | ball2 at (1.34, 0.00, 0.03) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz -0.00); touching floor | ball3 at (1.65, 0.00, 0.03) m, at rest; touching cup_base
1.75 s: ball1 at (0.79, 0.00, 0.03) m, at rest; touching floor | ball2 at (1.33, 0.00, 0.03) m, at rest; touching floor | ball3 at (1.65, 0.00, 0.03) m, at rest; touching cup_base
2.00 s: ball1 at (0.79, 0.00, 0.03) m, at rest; touching floor | ball2 at (1.32, 0.00, 0.03) m, at rest; touching floor | ball3 at (1.65, 0.00, 0.03) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (0.79, 0.00, 0.03) m, at rest; touching floor
- ball2 at (1.32, 0.00, 0.03) m, at rest; touching floor
- ball3 at (1.65, 0.00, 0.03) m, at rest; touching cup_base
</history>
