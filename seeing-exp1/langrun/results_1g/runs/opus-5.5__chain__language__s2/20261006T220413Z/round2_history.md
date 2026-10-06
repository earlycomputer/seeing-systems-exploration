Your expectations, checked against the run (4 of 4 hold):

- holds: ball1 touches ball2 (first touch at 0.04 s)
- holds: ball2 touches ball3 (first touch at 0.11 s)
- holds: ball3 touches cup (first touch at 0.34 s)
- holds: ball3 comes to rest in cup (ball3 at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.00, 0.00, 0.05) m, moving 4.00 m/s (vx +4.00, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2; starts at (0.25, 0.00, 0.05) m, at rest
- ball3: free body; its geoms: ball3; starts at (0.50, 0.00, 0.05) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching floor
 0.00 s  ball2 starts touching floor
 0.00 s  ball3 starts touching floor
 0.04 s  ball1 leaves floor
 0.04 s  ball1 first touches ball2
 0.04 s  ball2 starts moving
 0.04 s  ball1 leaves ball2
 0.07 s  ball2 leaves floor
 0.10 s  ball2 touches floor again
 0.11 s  ball2 leaves floor
 0.11 s  ball2 first touches ball3
 0.11 s  ball3 starts moving
 0.11 s  ball2 leaves ball3
 0.13 s  ball1 is at the top of its flight, at (0.22, 0.00, 0.09) m
 0.18 s  ball2 touches floor again
 0.21 s  ball1 touches floor again
 0.32 s  ball1 leaves floor
 0.32 s  ball1 touches ball2 again
 0.32 s  ball1 leaves ball2
 0.34 s  ball3 leaves floor
 0.34 s  ball3 first touches cup_near_wall
 0.34 s  ball3 leaves cup_near_wall
 0.37 s  ball1 touches floor again
 0.42 s  ball3 first touches cup_base
 0.43 s  ball3 leaves cup_base
 0.46 s  ball3 touches cup_base again
 0.66 s  ball2 leaves floor
 0.66 s  ball2 first touches cup_near_wall
 0.66 s  ball2 leaves cup_near_wall
 0.71 s  ball2 first touches cup_base
 0.71 s  ball2 touches cup_near_wall again
 0.71 s  ball2 leaves cup_near_wall
 0.81 s  ball2 touches ball3 again
 0.81 s  ball2 leaves ball3
 1.03 s  ball1 touches ball2 again
 1.03 s  ball1 leaves ball2
 1.08 s  ball2 touches ball3 again
 1.08 s  ball2 comes to rest at (0.80, 0.00, 0.05) m
 1.08 s  ball2 leaves ball3
 1.09 s  ball3 comes to rest at (0.90, 0.00, 0.05) m
 1.15 s  ball1 touches ball2 again
 1.15 s  ball1 comes to rest at (0.70, 0.00, 0.05) m
 1.15 s  ball1 leaves ball2
 1.16 s  ball1 passes 0.10 m from ball3 without touching it: nearest points (0.75, 0.00, 0.05) m and (0.85, 0.00, 0.05) m
 1.16 s  ball1 passes 0.01 m from cup (cup_near_wall) without touching it: nearest points (0.74, 0.00, 0.01) m and (0.74, 0.00, 0.00) m

State every 0.25 s:
0.00 s: ball1 at (0.00, 0.00, 0.05) m, moving 4.00 m/s (vx +4.00, vy +0.00, vz +0.00); touching floor | ball2 at (0.25, 0.00, 0.05) m, at rest; touching floor | ball3 at (0.50, 0.00, 0.05) m, at rest; touching floor
0.25 s: ball1 at (0.32, 0.00, 0.05) m, moving 1.08 m/s (vx +1.08, vy +0.00, vz +0.02); touching nothing | ball2 at (0.46, 0.00, 0.05) m, moving 0.44 m/s (vx +0.44, vy +0.00, vz +0.00); touching floor | ball3 at (0.65, 0.00, 0.05) m, moving 0.94 m/s (vx +0.94, vy -0.00, vz +0.00); touching floor
0.50 s: ball1 at (0.47, 0.00, 0.05) m, moving 0.42 m/s (vx +0.42, vy -0.00, vz +0.00); touching floor | ball2 at (0.62, 0.00, 0.05) m, moving 0.69 m/s (vx +0.69, vy +0.00, vz -0.00); touching floor | ball3 at (0.84, 0.00, 0.05) m, moving 0.50 m/s (vx +0.49, vy +0.00, vz +0.03); touching nothing
0.75 s: ball1 at (0.58, 0.00, 0.05) m, moving 0.42 m/s (vx +0.42, vy -0.00, vz -0.00); touching floor | ball2 at (0.78, 0.00, 0.05) m, moving 0.42 m/s (vx +0.41, vy +0.00, vz -0.04); touching nothing | ball3 at (0.89, 0.00, 0.05) m, at rest; touching cup_base
1.00 s: ball1 at (0.68, 0.00, 0.05) m, moving 0.42 m/s (vx +0.42, vy -0.00, vz -0.00); touching floor | ball2 at (0.79, 0.00, 0.05) m, at rest; touching cup_base | ball3 at (0.90, 0.00, 0.05) m, at rest; touching cup_base
1.25 s: ball1 at (0.70, 0.00, 0.05) m, at rest; touching floor | ball2 at (0.80, 0.00, 0.05) m, at rest; touching cup_base | ball3 at (0.90, 0.00, 0.05) m, at rest; touching cup_base
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (0.70, 0.00, 0.05) m, at rest; touching floor
- ball2 at (0.80, 0.00, 0.05) m, at rest; touching cup_base
- ball3 at (0.90, 0.00, 0.05) m, at rest; touching cup_base
</history>
