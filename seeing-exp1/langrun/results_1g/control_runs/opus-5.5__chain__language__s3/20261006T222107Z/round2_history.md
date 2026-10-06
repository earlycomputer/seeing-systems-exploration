MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (1.00, 0.00, 0.04) m, moving 3.00 m/s (vx +3.00, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2; starts at (1.20, 0.00, 0.04) m, at rest
- ball3: free body; its geoms: ball3; starts at (1.40, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching floor
 0.00 s  ball2 starts touching floor
 0.00 s  ball3 starts touching floor
 0.04 s  ball1 leaves floor
 0.04 s  ball2 leaves floor
 0.04 s  ball1 first touches ball2
 0.04 s  ball2 starts moving
 0.05 s  ball1 leaves ball2
 0.05 s  ball1 passes 0.19 m from ball3 without touching it: nearest points (1.17, 0.00, 0.05) m and (1.36, 0.00, 0.04) m
 0.10 s  ball3 leaves floor
 0.10 s  ball2 first touches ball3
 0.10 s  ball3 starts moving
 0.10 s  ball2 leaves ball3
 0.13 s  ball1 is at the top of its flight, at (1.11, 0.00, 0.08) m
 0.14 s  ball3 touches floor again
 0.15 s  ball2 is at the top of its flight, at (1.32, 0.00, 0.06) m
 0.21 s  ball2 touches floor again
 0.22 s  ball1 touches floor again
 0.27 s  ball3 leaves floor
 0.27 s  ball3 first touches cup_near_wall
 0.28 s  ball3 leaves cup_near_wall
 0.35 s  ball3 is at the top of its flight, at (1.74, 0.00, 0.07) m
 0.42 s  ball3 first touches cup_base
 0.43 s  ball3 leaves cup_base
 0.48 s  ball3 touches cup_base again
 0.58 s  ball3 first touches cup_far_wall
 0.58 s  ball1 touches ball2 again
 0.59 s  ball1 leaves ball2
 0.59 s  ball1 passes 0.49 m from cup (cup_near_wall) without touching it: nearest points (1.20, 0.00, 0.04) m and (1.69, 0.00, 0.01) m
 0.59 s  ball3 leaves cup_far_wall
 0.59 s  ball1 comes to rest at (1.16, 0.00, 0.04) m
 0.59 s  ball2 comes to rest at (1.24, 0.00, 0.04) m
 0.64 s  ball3 comes to rest at (1.95, 0.00, 0.04) m
 6.00 s  ball2 passes 0.31 m from cup (cup_near_wall) without touching it: nearest points (1.39, 0.00, 0.04) m and (1.69, 0.00, 0.01) m

State every 0.25 s:
0.00 s: ball1 at (1.00, 0.00, 0.04) m, moving 3.00 m/s (vx +3.00, vy +0.00, vz +0.00); touching floor | ball2 at (1.20, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.40, 0.00, 0.04) m, at rest; touching floor
0.25 s: ball1 at (1.10, 0.00, 0.04) m, moving 0.19 m/s (vx +0.18, vy -0.00, vz +0.03); touching nothing | ball2 at (1.31, 0.00, 0.04) m, moving 0.19 m/s (vx -0.19, vy +0.00, vz -0.04); touching nothing | ball3 at (1.64, 0.00, 0.04) m, moving 1.46 m/s (vx +1.46, vy +0.00, vz +0.00); touching floor
0.50 s: ball1 at (1.15, 0.00, 0.04) m, moving 0.18 m/s (vx +0.18, vy -0.00, vz -0.00); touching floor | ball2 at (1.26, 0.00, 0.04) m, moving 0.18 m/s (vx -0.18, vy +0.00, vz -0.00); touching floor | ball3 at (1.89, 0.00, 0.04) m, moving 0.83 m/s (vx +0.83, vy +0.00, vz -0.00); touching nothing
0.75 s: ball1 at (1.16, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.25, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base
1.00 s: ball1 at (1.15, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.26, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base
(the same through 1.25 s)
1.50 s: ball1 at (1.14, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.27, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base
1.75 s: ball1 at (1.13, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.27, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base
2.00 s: ball1 at (1.13, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.28, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base
2.25 s: ball1 at (1.12, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.28, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base
2.50 s: ball1 at (1.12, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.29, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base
2.75 s: ball1 at (1.11, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.29, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base
3.00 s: ball1 at (1.11, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.30, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base
3.25 s: ball1 at (1.10, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.30, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base
3.50 s: ball1 at (1.10, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.31, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base
3.75 s: ball1 at (1.09, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.31, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base
4.00 s: ball1 at (1.09, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.32, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base
4.25 s: ball1 at (1.08, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.32, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base
(the same through 4.50 s)
4.75 s: ball1 at (1.07, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.33, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base
(the same through 5.00 s)
5.25 s: ball1 at (1.07, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.34, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base
5.50 s: ball1 at (1.06, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.34, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base
(the same through 5.75 s)
6.00 s: ball1 at (1.06, 0.00, 0.04) m, at rest; touching floor | ball2 at (1.35, 0.00, 0.04) m, at rest; touching floor | ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base

At the end (6.00 s):
- ball1 at (1.06, 0.00, 0.04) m, at rest; touching floor
- ball2 at (1.35, 0.00, 0.04) m, at rest; touching floor
- ball3 at (1.94, 0.00, 0.04) m, at rest; touching cup_base
</history>
