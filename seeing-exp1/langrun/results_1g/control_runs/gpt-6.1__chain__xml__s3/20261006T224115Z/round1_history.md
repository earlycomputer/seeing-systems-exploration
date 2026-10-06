MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_geom; starts at (-0.60, 0.00, 0.06) m, moving 1.00 m/s (vx +1.00, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2_geom; starts at (-0.33, 0.00, 0.06) m, at rest
- ball3: free body; its geoms: ball3_geom; starts at (-0.06, 0.00, 0.06) m, at rest

What happened, in order:
 0.00 s  ball1_geom starts touching floor
 0.00 s  ball2_geom starts touching floor
 0.00 s  ball3_geom starts touching floor
 0.16 s  ball1_geom first touches ball2_geom
 0.16 s  ball2 starts moving
 0.17 s  ball1_geom leaves ball2_geom
 0.26 s  ball1 comes to rest at (-0.44, 0.00, 0.06) m
 0.34 s  ball1 passes 0.25 m from ball3 (ball3_geom) without touching it: nearest points (-0.37, 0.00, 0.06) m and (-0.12, 0.00, 0.06) m
 0.35 s  ball2_geom first touches ball3_geom
 0.35 s  ball3 starts moving
 0.36 s  ball2_geom leaves ball3_geom
 0.40 s  ball2 comes to rest at (-0.17, 0.00, 0.06) m
 0.53 s  ball3_geom first touches cup_wall_06
 0.83 s  ball3_geom first touches cup_back
 0.85 s  ball3_geom leaves cup_back
 1.05 s  ball3 comes to rest at (0.22, 0.00, 0.06) m
 1.27 s  ball1 passes 0.44 m from cup (cup_wall_06) without touching it: nearest points (-0.37, 0.00, 0.05) m and (0.06, 0.00, 0.00) m
 1.44 s  ball2 passes 0.17 m from cup (cup_wall_06) without touching it: nearest points (-0.11, 0.00, 0.04) m and (0.06, 0.00, 0.00) m

State every 0.25 s:
0.00 s: ball1 at (-0.60, 0.00, 0.06) m, moving 1.00 m/s (vx +1.00, vy +0.00, vz +0.00); touching floor | ball2 at (-0.33, 0.00, 0.06) m, at rest; touching floor | ball3 at (-0.06, 0.00, 0.06) m, at rest; touching floor
0.25 s: ball1 at (-0.44, 0.00, 0.06) m, moving 0.05 m/s (vx +0.05, vy +0.00, vz +0.00); touching floor | ball2 at (-0.26, 0.00, 0.06) m, moving 0.82 m/s (vx +0.82, vy +0.00, vz -0.00); touching nothing | ball3 at (-0.06, 0.00, 0.06) m, at rest; touching floor
0.50 s: ball1 at (-0.43, 0.00, 0.06) m, at rest; touching floor | ball2 at (-0.17, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.04, 0.00, 0.06) m, moving 0.66 m/s (vx +0.66, vy +0.00, vz +0.01); touching floor
0.75 s: ball1 at (-0.43, 0.00, 0.06) m, at rest; touching floor | ball2 at (-0.17, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.19, 0.00, 0.06) m, moving 0.57 m/s (vx +0.57, vy +0.00, vz -0.01); touching nothing
1.00 s: ball1 at (-0.43, 0.00, 0.06) m, at rest; touching floor | ball2 at (-0.17, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.23, 0.00, 0.06) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz +0.00); touching cup_wall_06, floor
1.25 s: ball1 at (-0.43, 0.00, 0.06) m, at rest; touching floor | ball2 at (-0.17, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.22, 0.00, 0.06) m, at rest; touching cup_wall_06, floor
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (-0.43, 0.00, 0.06) m, at rest; touching floor
- ball2 at (-0.17, 0.00, 0.06) m, at rest; touching floor
- ball3 at (0.22, 0.00, 0.06) m, at rest; touching cup_wall_06, floor
</history>
