MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1; starts at (2.00, 0.00, 0.05) m, at rest
- block2: free body; its geoms: block2; starts at (2.00, 0.00, 0.15) m, at rest
- block3: free body; its geoms: block3; starts at (2.00, 0.00, 0.25) m, at rest
- block4: free body; its geoms: block4; starts at (2.00, 0.00, 0.35) m, at rest
- block5: free body; its geoms: block5; starts at (2.00, 0.00, 0.45) m, at rest
- ball: free body; its geoms: ball; starts at (1.00, 0.00, 0.05) m, moving 1.60 m/s (vx +1.60, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  block1 starts touching floor
 0.00 s  block1 starts touching block2
 0.00 s  block3 starts touching block4
 0.00 s  ball starts touching floor
 0.00 s  block2 starts touching block3
 0.01 s  block3 starts moving
 0.01 s  block4 starts moving
 0.01 s  block5 starts moving
 0.01 s  block4 first touches block5
 0.59 s  ball leaves floor
 0.59 s  block1 first touches ball
 0.59 s  block1 starts moving
 0.59 s  block2 starts moving
 0.62 s  block1 leaves ball
 0.64 s  block2 first touches ball
 0.65 s  ball touches floor again
 0.66 s  block1 touches ball again
 0.69 s  block1 leaves ball
 0.74 s  block1 touches ball again
 0.75 s  block2 leaves ball
 0.75 s  block1 leaves ball
 0.80 s  block2 touches ball again
 0.81 s  block1 touches ball again
 0.83 s  block1 leaves ball
 0.87 s  block1 touches ball 3 more times between 0.87 s and 6.00 s, still touching at the end
 0.93 s  ball comes to rest at (2.06, 0.00, 0.05) m
 1.01 s  block4 leaves block5
 1.01 s  block1 leaves block2
 1.03 s  block3 leaves block4
 1.04 s  block2 leaves block3
 1.05 s  block1 comes to rest at (2.17, 0.00, 0.05) m
 1.07 s  block5 passes 0.23 m from ball without touching it: nearest points (1.81, 0.00, 0.16) m and (2.02, 0.00, 0.07) m
 1.09 s  block4 passes 0.12 m from ball without touching it: nearest points (1.90, 0.00, 0.10) m and (2.02, 0.00, 0.06) m
 1.11 s  block3 passes 0.01 m from ball without touching it: nearest points (2.00, 0.00, 0.06) m and (2.02, 0.00, 0.06) m
 1.15 s  block4 first touches floor
 1.15 s  block3 first touches floor
 1.15 s  block5 first touches floor
 1.24 s  block3 comes to rest at (1.95, 0.00, 0.05) m
 1.24 s  block4 comes to rest at (1.82, 0.00, 0.05) m
 1.25 s  block5 comes to rest at (1.70, 0.00, 0.05) m
 1.28 s  block2 touches block3 again
 1.28 s  block2 leaves ball
 1.37 s  block2 touches ball again
 1.37 s  block2 comes to rest at (2.01, 0.00, 0.15) m

State every 0.25 s:
0.00 s: block1 at (2.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.35) m, at rest; touching block3 | block5 at (2.00, 0.00, 0.45) m, at rest; touching nothing | ball at (1.00, 0.00, 0.05) m, moving 1.60 m/s (vx +1.60, vy +0.00, vz +0.00); touching floor
0.25 s: block1 at (2.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.00, 0.00, 0.45) m, at rest; touching block4 | ball at (1.39, 0.00, 0.05) m, moving 1.54 m/s (vx +1.54, vy +0.00, vz +0.02); touching floor
0.50 s: block1 at (2.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.00, 0.00, 0.45) m, at rest; touching block4 | ball at (1.77, 0.00, 0.05) m, moving 1.48 m/s (vx +1.48, vy +0.00, vz +0.02); touching floor
0.75 s: block1 at (2.13, 0.00, 0.05) m, moving 0.60 m/s (vx +0.59, vy +0.00, vz +0.12), turned 1° from how it started; touching ball, block2, floor | block2 at (2.08, 0.00, 0.16) m, moving 0.41 m/s (vx +0.36, vy +0.00, vz +0.19), turned 20° from how it started; touching block1, block3 | block3 at (2.05, 0.00, 0.25) m, moving 0.15 m/s (vx +0.11, vy +0.00, vz +0.09), turned 20° from how it started; touching block2, block4 | block4 at (2.02, 0.00, 0.34) m, at rest, turned 20° from how it started; touching block3, block5 | block5 at (1.98, 0.00, 0.44) m, moving 0.16 m/s (vx -0.15, vy +0.00, vz -0.06), turned 20° from how it started; touching block4 | ball at (2.03, 0.00, 0.05) m, moving 0.43 m/s (vx +0.43, vy -0.00, vz -0.05); touching block1
1.00 s: block1 at (2.16, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.09, 0.00, 0.15) m, moving 0.20 m/s (vx -0.19, vy -0.00, vz -0.06), turned 55° from how it started; touching ball, block1, block3 | block3 at (2.01, 0.00, 0.21) m, moving 0.62 m/s (vx -0.44, vy +0.00, vz -0.44), turned 55° from how it started; touching block2, block4 | block4 at (1.93, 0.00, 0.27) m, moving 1.06 m/s (vx -0.70, vy -0.00, vz -0.79), turned 55° from how it started; touching block3, block5 | block5 at (1.84, 0.00, 0.33) m, moving 1.49 m/s (vx -0.95, vy -0.00, vz -1.14), turned 54° from how it started; touching block4 | ball at (2.06, 0.00, 0.05) m, at rest; touching block2, floor
1.25 s: block1 at (2.17, 0.00, 0.05) m, at rest; touching floor | block2 at (2.03, 0.00, 0.15) m, moving 0.31 m/s (vx -0.31, vy -0.01, vz -0.05), turned 126° from how it started; touching ball | block3 at (1.95, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (1.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (1.70, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (2.07, 0.00, 0.05) m, at rest; touching block2, floor
1.50 s: block1 at (2.17, 0.00, 0.05) m, at rest; touching floor | block2 at (2.01, 0.00, 0.15) m, at rest, turned 147° from how it started; touching ball, block3 | block3 at (1.95, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (1.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (1.70, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (2.06, 0.00, 0.05) m, at rest; touching block2, floor
1.75 s: block1 at (2.17, 0.00, 0.05) m, at rest; touching floor | block2 at (2.02, 0.00, 0.15) m, at rest, turned 138° from how it started; touching ball, block3 | block3 at (1.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (1.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (1.70, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (2.06, 0.00, 0.05) m, at rest; touching block2, floor
2.00 s: block1 at (2.17, 0.00, 0.05) m, at rest; touching floor | block2 at (2.02, 0.00, 0.15) m, at rest, turned 131° from how it started; touching ball, block3 | block3 at (1.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (1.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (1.70, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (2.06, 0.00, 0.05) m, at rest; touching block2, floor
2.25 s: block1 at (2.17, 0.00, 0.05) m, at rest; touching floor | block2 at (2.02, 0.00, 0.15) m, at rest, turned 129° from how it started; touching ball, block3 | block3 at (1.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (1.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (1.70, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (2.06, 0.00, 0.05) m, at rest; touching block2, floor
2.50 s: block1 at (2.17, 0.00, 0.05) m, at rest; touching floor | block2 at (2.02, 0.00, 0.15) m, at rest, turned 127° from how it started; touching ball, block3 | block3 at (1.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (1.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (1.70, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (2.06, 0.00, 0.05) m, at rest; touching block2, floor
2.75 s: block1 at (2.17, 0.00, 0.05) m, at rest; touching floor | block2 at (2.02, 0.00, 0.14) m, at rest, turned 126° from how it started; touching ball, block3 | block3 at (1.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (1.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (1.70, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (2.06, 0.00, 0.05) m, at rest; touching block2, floor
3.00 s: block1 at (2.17, 0.00, 0.05) m, at rest; touching floor | block2 at (2.02, 0.00, 0.14) m, at rest, turned 125° from how it started; touching ball, block3 | block3 at (1.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (1.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (1.70, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (2.06, 0.00, 0.05) m, at rest; touching block2, floor
(the same through 3.25 s)
3.50 s: block1 at (2.17, 0.00, 0.05) m, at rest; touching floor | block2 at (2.02, 0.00, 0.14) m, at rest, turned 124° from how it started; touching ball, block3 | block3 at (1.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (1.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (1.70, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (2.06, 0.00, 0.05) m, at rest; touching block2, floor
(the same through 4.00 s)
4.25 s: block1 at (2.17, 0.00, 0.05) m, at rest; touching floor | block2 at (2.02, 0.00, 0.14) m, at rest, turned 123° from how it started; touching ball, block3 | block3 at (1.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (1.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (1.70, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (2.06, 0.00, 0.05) m, at rest; touching block2, floor
4.50 s: block1 at (2.17, 0.00, 0.05) m, at rest; touching floor | block2 at (2.02, 0.00, 0.14) m, at rest, turned 123° from how it started; touching ball, block3 | block3 at (1.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (1.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (1.70, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (2.07, 0.00, 0.05) m, at rest; touching block2, floor
(the same through 5.00 s)
5.25 s: block1 at (2.17, 0.00, 0.05) m, at rest; touching ball, floor | block2 at (2.02, 0.00, 0.14) m, at rest, turned 123° from how it started; touching ball, block3 | block3 at (1.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (1.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (1.70, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (2.07, 0.00, 0.05) m, at rest; touching block1, block2, floor
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (2.17, 0.00, 0.05) m, at rest; touching ball, floor
- block2 at (2.02, 0.00, 0.14) m, at rest, turned 123° from how it started; touching ball, block3
- block3 at (1.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor
- block4 at (1.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- block5 at (1.70, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- ball at (2.07, 0.00, 0.05) m, at rest; touching block1, block2, floor
</history>
