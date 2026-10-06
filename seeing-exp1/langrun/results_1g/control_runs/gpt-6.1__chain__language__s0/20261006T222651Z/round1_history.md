MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.00, 0.00, 0.04) m, moving 1.20 m/s (vx +1.20, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2; starts at (0.30, 0.00, 0.04) m, at rest
- ball3: free body; its geoms: ball3; starts at (0.60, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching floor
 0.00 s  ball2 starts touching floor
 0.00 s  ball3 starts touching floor
 0.19 s  ball1 leaves floor
 0.19 s  ball1 first touches ball2
 0.19 s  ball2 starts moving
 0.19 s  ball1 leaves ball2
 0.23 s  ball1 touches floor again
 0.59 s  ball2 first touches ball3
 0.59 s  ball3 starts moving
 0.60 s  ball2 leaves ball3
 0.96 s  ball1 touches ball2 again
 0.96 s  ball1 leaves ball2
 1.16 s  ball3 leaves floor
 1.16 s  ball3 first touches cup_near_wall
 1.22 s  ball3 first touches cup_base
 1.31 s  ball3 leaves cup_near_wall
 1.80 s  ball2 touches ball3 again
 1.80 s  ball2 leaves ball3
 1.80 s  ball2 comes to rest at (0.70, 0.00, 0.04) m
 1.84 s  ball3 comes to rest at (0.78, 0.00, 0.04) m
 1.95 s  ball2 touches ball3 again
 1.95 s  ball2 leaves ball3
 2.69 s  ball1 touches ball2 again
 2.69 s  ball1 comes to rest at (0.62, 0.00, 0.04) m
 2.70 s  ball1 leaves ball2
 2.70 s  ball1 passes 0.08 m from ball3 without touching it: nearest points (0.66, 0.00, 0.04) m and (0.74, 0.00, 0.04) m
 2.70 s  ball2 touches ball3 again
 2.71 s  ball2 leaves ball3
 2.75 s  ball1 passes 0.11 m from cup (cup_near_wall) without touching it: nearest points (0.66, 0.00, 0.03) m and (0.77, 0.00, 0.00) m
 2.75 s  ball1 touches ball2 again
 2.76 s  ball1 leaves ball2
 3.52 s  ball2 touches ball3 1 more times between 3.52 s and 3.53 s
 3.53 s  ball2 passes 0.03 m from cup (cup_near_wall) without touching it: nearest points (0.74, 0.00, 0.02) m and (0.77, 0.00, 0.00) m

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.04) m, moving 1.20 m/s (vx +1.20, vy +0.00, vz +0.00); touching floor | ball2 at (0.30, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.60, 0.00, 0.04) m, at rest; touching floor
0.25 s: ball1 at (0.24, 0.00, 0.04) m, moving 0.32 m/s (vx +0.32, vy -0.00, vz +0.05); touching floor | ball2 at (0.34, 0.00, 0.04) m, moving 0.53 m/s (vx +0.53, vy +0.00, vz +0.00); touching floor | ball3 at (0.60, 0.00, 0.04) m, at rest; touching floor
0.50 s: ball1 at (0.32, 0.00, 0.04) m, moving 0.32 m/s (vx +0.32, vy -0.00, vz +0.00); touching floor | ball2 at (0.47, 0.00, 0.04) m, moving 0.53 m/s (vx +0.53, vy +0.00, vz -0.00); touching floor | ball3 at (0.60, 0.00, 0.04) m, at rest; touching floor
0.75 s: ball1 at (0.40, 0.00, 0.04) m, moving 0.32 m/s (vx +0.32, vy -0.00, vz +0.00); touching floor | ball2 at (0.53, 0.00, 0.04) m, moving 0.07 m/s (vx +0.07, vy +0.00, vz +0.00); touching floor | ball3 at (0.64, 0.00, 0.04) m, moving 0.28 m/s (vx +0.28, vy -0.00, vz -0.00); touching floor
1.00 s: ball1 at (0.47, 0.00, 0.04) m, moving 0.09 m/s (vx +0.09, vy -0.00, vz +0.01); touching floor | ball2 at (0.55, 0.00, 0.04) m, moving 0.18 m/s (vx +0.18, vy +0.00, vz +0.00); touching floor | ball3 at (0.71, 0.00, 0.04) m, moving 0.27 m/s (vx +0.27, vy -0.00, vz +0.00); touching floor
1.25 s: ball1 at (0.49, 0.00, 0.04) m, moving 0.09 m/s (vx +0.09, vy -0.00, vz +0.00); touching floor | ball2 at (0.60, 0.00, 0.04) m, moving 0.18 m/s (vx +0.18, vy +0.00, vz -0.00); touching floor | ball3 at (0.77, 0.00, 0.04) m, moving 0.10 m/s (vx +0.10, vy -0.00, vz +0.00); touching cup_base, cup_near_wall
1.50 s: ball1 at (0.51, 0.00, 0.04) m, moving 0.09 m/s (vx +0.09, vy -0.00, vz +0.00); touching floor | ball2 at (0.64, 0.00, 0.04) m, moving 0.18 m/s (vx +0.18, vy +0.00, vz +0.00); touching floor | ball3 at (0.78, 0.00, 0.04) m, at rest; touching cup_base
1.75 s: ball1 at (0.54, 0.00, 0.04) m, moving 0.09 m/s (vx +0.09, vy -0.00, vz +0.00); touching floor | ball2 at (0.69, 0.00, 0.04) m, moving 0.18 m/s (vx +0.18, vy +0.00, vz +0.00); touching floor | ball3 at (0.78, 0.00, 0.04) m, at rest; touching cup_base
2.00 s: ball1 at (0.56, 0.00, 0.04) m, moving 0.09 m/s (vx +0.09, vy -0.00, vz +0.00); touching floor | ball2 at (0.70, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.78, 0.00, 0.04) m, at rest; touching cup_base
2.25 s: ball1 at (0.58, 0.00, 0.04) m, moving 0.09 m/s (vx +0.09, vy -0.00, vz +0.00); touching floor | ball2 at (0.70, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.78, 0.00, 0.04) m, at rest; touching cup_base
2.50 s: ball1 at (0.60, 0.00, 0.04) m, moving 0.09 m/s (vx +0.09, vy -0.00, vz +0.00); touching floor | ball2 at (0.70, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.78, 0.00, 0.04) m, at rest; touching cup_base
2.75 s: ball1 at (0.62, 0.00, 0.04) m, at rest; touching floor | ball2 at (0.70, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.78, 0.00, 0.04) m, at rest; touching cup_base
(the same through 4.75 s)
5.00 s: ball1 at (0.61, 0.00, 0.04) m, at rest; touching floor | ball2 at (0.70, 0.00, 0.04) m, at rest; touching floor | ball3 at (0.78, 0.00, 0.04) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (0.61, 0.00, 0.04) m, at rest; touching floor
- ball2 at (0.70, 0.00, 0.04) m, at rest; touching floor
- ball3 at (0.78, 0.00, 0.04) m, at rest; touching cup_base
</history>
