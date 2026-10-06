Your expectations, checked against the run (4 of 4 hold):

- holds: ball1 touches ball2 (first touch at 0.12 s)
- holds: ball2 touches ball3 (first touch at 0.34 s)
- holds: ball3 touches cup_ramp (first touch at 0.41 s)
- holds: ball3 comes to rest in cup (ball3 at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_geom; starts at (-1.35, 0.00, 0.06) m, moving 4.00 m/s (vx +4.00, vy +0.00, vz +0.00)
- ball2: free body; its geoms: ball2_geom; starts at (-0.75, 0.00, 0.06) m, at rest
- ball3: free body; its geoms: ball3_geom; starts at (0.00, 0.00, 0.06) m, at rest

What happened, in order:
 0.00 s  ball1_geom starts touching floor
 0.00 s  ball2_geom starts touching floor
 0.00 s  ball3_geom starts touching floor
 0.00 s  ball1_geom leaves floor
 0.04 s  ball1_geom touches floor again
 0.06 s  ball1_geom leaves floor
 0.09 s  ball1_geom touches floor again
 0.12 s  ball1_geom leaves floor
 0.12 s  ball1_geom first touches ball2_geom
 0.12 s  ball2 starts moving
 0.13 s  ball2_geom leaves floor
 0.14 s  ball1_geom leaves ball2_geom
 0.15 s  ball1_geom touches floor again
 0.15 s  ball1_geom leaves floor
 0.19 s  ball2_geom touches floor again
 0.19 s  ball2_geom leaves floor
 0.20 s  ball1_geom touches floor 3 more times between 0.20 s and 6.00 s, still touching at the end
 0.26 s  ball2_geom touches floor again
 0.27 s  ball2_geom leaves floor
 0.33 s  ball2_geom touches floor again
 0.33 s  ball2_geom leaves floor
 0.34 s  ball2_geom first touches ball3_geom
 0.34 s  ball3 starts moving
 0.35 s  ball3_geom leaves floor
 0.36 s  ball2_geom leaves ball3_geom
 0.38 s  ball2_geom touches floor 2 more times between 0.38 s and 0.76 s
 0.39 s  ball3_geom touches floor again
 0.39 s  ball3_geom leaves floor
 0.41 s  ball3_geom first touches cup_ramp
 0.41 s  ball3_geom leaves cup_ramp
 0.46 s  ball3_geom touches cup_ramp again
 0.46 s  ball3_geom leaves cup_ramp
 0.50 s  ball3_geom touches cup_ramp again
 0.50 s  ball3_geom leaves cup_ramp
 0.54 s  ball3_geom touches cup_ramp again
 0.54 s  ball3_geom leaves cup_ramp
 0.57 s  ball3_geom touches cup_ramp 1 more times between 0.57 s and 0.57 s
 0.57 s  ball3_geom first touches cup_front_lip
 0.57 s  ball3_geom leaves cup_front_lip
 0.59 s  ball3 is at the top of its flight, at (0.38, 0.00, 0.10) m
 0.68 s  ball3_geom first touches cup_bottom
 0.69 s  ball3_geom leaves cup_bottom
 0.74 s  ball3_geom touches cup_bottom again
 0.75 s  ball3_geom leaves cup_bottom
 0.76 s  ball2_geom first touches cup_ramp
 0.78 s  ball3_geom touches cup_bottom again
 1.04 s  ball3 comes to rest at (0.63, 0.00, 0.07) m
 1.10 s  ball1_geom touches ball2_geom again
 1.12 s  ball1_geom leaves ball2_geom
 1.16 s  ball1 comes to rest at (0.02, 0.00, 0.06) m
 1.21 s  ball2 comes to rest at (0.16, 0.00, 0.07) m
 6.00 s  ball1 passes 0.05 m from cup (cup_ramp) without touching it: nearest points (0.08, 0.00, 0.03) m and (0.12, 0.00, 0.00) m
 6.00 s  ball1 passes 0.49 m from ball3 (ball3_geom) without touching it: nearest points (0.09, 0.00, 0.06) m and (0.57, 0.00, 0.07) m

State every 0.25 s:
0.00 s: ball1 at (-1.35, 0.00, 0.06) m, moving 4.00 m/s (vx +4.00, vy +0.00, vz +0.00); touching floor | ball2 at (-0.75, 0.00, 0.06) m, at rest; touching floor | ball3 at (0.00, 0.00, 0.06) m, at rest; touching floor
0.25 s: ball1 at (-0.76, 0.00, 0.06) m, moving 0.85 m/s (vx +0.83, vy +0.00, vz -0.17); touching nothing | ball2 at (-0.37, 0.00, 0.06) m, moving 3.06 m/s (vx +3.05, vy +0.00, vz -0.25); touching nothing | ball3 at (0.00, 0.00, 0.06) m, at rest; touching floor
0.50 s: ball1 at (-0.48, 0.00, 0.06) m, moving 1.10 m/s (vx +1.10, vy +0.00, vz +0.05); touching floor | ball2 at (-0.03, 0.00, 0.06) m, moving 0.65 m/s (vx +0.65, vy +0.00, vz +0.05); touching floor | ball3 at (0.27, 0.00, 0.08) m, moving 1.36 m/s (vx +1.34, vy +0.00, vz +0.25); touching cup_ramp
0.75 s: ball1 at (-0.23, 0.00, 0.06) m, moving 0.88 m/s (vx +0.88, vy +0.00, vz -0.03); touching nothing | ball2 at (0.11, 0.00, 0.06) m, moving 0.43 m/s (vx +0.43, vy +0.00, vz +0.02); touching floor | ball3 at (0.52, 0.00, 0.07) m, moving 0.69 m/s (vx +0.67, vy +0.00, vz +0.14); touching cup_bottom
1.00 s: ball1 at (-0.04, 0.00, 0.06) m, moving 0.64 m/s (vx +0.64, vy +0.00, vz +0.00); touching nothing | ball2 at (0.14, 0.00, 0.06) m, at rest; touching cup_ramp | ball3 at (0.63, 0.00, 0.07) m, moving 0.14 m/s (vx +0.14, vy +0.00, vz -0.02); touching nothing
1.25 s: ball1 at (0.03, 0.00, 0.06) m, at rest; touching floor | ball2 at (0.16, 0.00, 0.07) m, at rest; touching cup_ramp | ball3 at (0.63, 0.00, 0.07) m, at rest; touching cup_bottom
(the same through 4.25 s)
4.50 s: ball1 at (0.03, 0.00, 0.06) m, at rest; touching floor | ball2 at (0.15, 0.00, 0.07) m, at rest; touching cup_ramp | ball3 at (0.63, 0.00, 0.07) m, at rest; touching cup_bottom
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (0.03, 0.00, 0.06) m, at rest; touching floor
- ball2 at (0.15, 0.00, 0.07) m, at rest; touching cup_ramp
- ball3 at (0.63, 0.00, 0.07) m, at rest; touching cup_bottom
</history>
