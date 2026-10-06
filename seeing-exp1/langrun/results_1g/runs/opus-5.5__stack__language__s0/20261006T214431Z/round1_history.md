Your expectations, checked against the run (2 of 2 hold):

- holds: ball touches block1 (first touch at 0.27 s)
- holds: block5 touches floor (first touch at 0.79 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1; starts at (1.00, 0.00, 0.05) m, at rest
- block2: free body; its geoms: block2; starts at (1.00, 0.00, 0.15) m, at rest
- block3: free body; its geoms: block3; starts at (1.00, 0.00, 0.25) m, at rest
- block4: free body; its geoms: block4; starts at (1.00, 0.00, 0.35) m, at rest
- block5: free body; its geoms: block5; starts at (1.00, 0.00, 0.45) m, at rest
- ball: free body; its geoms: ball; starts at (0.40, 0.00, 0.05) m, moving 2.50 m/s (vx +2.50, vy +0.00, vz +0.00)

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
 0.04 s  ball leaves floor
 0.07 s  ball touches floor again
 0.26 s  ball leaves floor
 0.27 s  block1 first touches ball
 0.27 s  block1 starts moving
 0.27 s  block2 starts moving
 0.27 s  block1 leaves block2
 0.30 s  block1 leaves ball
 0.30 s  block2 first touches ball
 0.33 s  block1 touches block2 again
 0.33 s  ball touches floor again
 0.58 s  ball comes to rest at (1.06, 0.00, 0.05) m
 0.64 s  block4 leaves block5
 0.66 s  block3 leaves block4
 0.67 s  block2 leaves block3
 0.67 s  block4 touches block5 again
 0.68 s  block4 leaves block5
 0.68 s  block1 leaves block2
 0.69 s  block1 touches ball again
 0.71 s  block5 passes 0.23 m from ball without touching it: nearest points (0.81, 0.00, 0.16) m and (1.02, 0.00, 0.07) m
 0.72 s  block1 comes to rest at (1.16, 0.00, 0.05) m
 0.73 s  block4 passes 0.12 m from ball without touching it: nearest points (0.90, 0.00, 0.10) m and (1.02, 0.00, 0.06) m
 0.75 s  block3 passes 0.01 m from ball without touching it: nearest points (1.00, 0.00, 0.06) m and (1.01, 0.00, 0.06) m
 0.78 s  block1 leaves ball
 0.79 s  block4 first touches floor
 0.79 s  block3 first touches floor
 0.79 s  block5 first touches floor
 0.88 s  block3 comes to rest at (0.94, 0.00, 0.05) m
 0.88 s  block4 comes to rest at (0.82, 0.00, 0.05) m
 0.90 s  block5 comes to rest at (0.69, 0.00, 0.05) m
 0.98 s  block2 touches block3 again
 0.98 s  block2 leaves ball
 1.03 s  block2 comes to rest at (1.01, 0.00, 0.15) m
 1.05 s  block2 touches ball again
 4.44 s  block1 touches ball again

State every 0.25 s:
0.00 s: block1 at (1.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (1.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (1.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (1.00, 0.00, 0.35) m, at rest; touching block3 | block5 at (1.00, 0.00, 0.45) m, at rest; touching nothing | ball at (0.40, 0.00, 0.05) m, moving 2.50 m/s (vx +2.50, vy +0.00, vz +0.00); touching floor
0.25 s: block1 at (1.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (1.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (1.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (1.00, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (1.00, 0.00, 0.45) m, at rest; touching block4 | ball at (0.87, 0.00, 0.05) m, moving 1.73 m/s (vx +1.73, vy -0.00, vz -0.01); touching nothing
0.50 s: block1 at (1.15, 0.00, 0.05) m, moving 0.15 m/s (vx +0.14, vy +0.00, vz +0.05); touching block2, floor | block2 at (1.10, 0.00, 0.16) m, at rest, turned 29° from how it started; touching ball, block1, block3 | block3 at (1.05, 0.00, 0.24) m, moving 0.17 m/s (vx -0.16, vy -0.00, vz -0.05), turned 29° from how it started; touching block2, block4 | block4 at (1.00, 0.00, 0.33) m, moving 0.36 m/s (vx -0.34, vy -0.00, vz -0.12), turned 30° from how it started; touching block3, block5 | block5 at (0.95, 0.00, 0.41) m, moving 0.54 m/s (vx -0.50, vy +0.00, vz -0.20), turned 30° from how it started; touching block4 | ball at (1.05, 0.00, 0.05) m, moving 0.19 m/s (vx +0.19, vy +0.00, vz +0.00); touching block2, floor
0.75 s: block1 at (1.16, 0.00, 0.05) m, at rest; touching ball, floor | block2 at (1.07, 0.00, 0.15) m, moving 0.21 m/s (vx -0.21, vy +0.00, vz -0.00), turned 84° from how it started; touching ball | block3 at (0.96, 0.00, 0.12) m, moving 1.45 m/s (vx -0.48, vy +0.00, vz -1.37), turned 84° from how it started; touching nothing | block4 at (0.85, 0.00, 0.13) m, moving 1.98 m/s (vx -0.73, vy +0.00, vz -1.84), turned 83° from how it started; touching nothing | block5 at (0.74, 0.00, 0.15) m, moving 2.38 m/s (vx -0.96, vy +0.00, vz -2.18), turned 79° from how it started; touching nothing | ball at (1.06, 0.00, 0.05) m, at rest; touching block1, block2, floor
1.00 s: block1 at (1.16, 0.00, 0.05) m, at rest; touching floor | block2 at (1.01, 0.00, 0.14) m, moving 0.12 m/s (vx -0.10, vy -0.00, vz +0.06), turned 133° from how it started; touching block3 | block3 at (0.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (0.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (0.69, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (1.06, 0.00, 0.05) m, at rest; touching floor
1.25 s: block1 at (1.16, 0.00, 0.05) m, at rest; touching floor | block2 at (1.01, 0.00, 0.15) m, at rest, turned 131° from how it started; touching ball, block3 | block3 at (0.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (0.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (0.69, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (1.06, 0.00, 0.05) m, at rest; touching block2, floor
1.50 s: block1 at (1.16, 0.00, 0.05) m, at rest; touching floor | block2 at (1.02, 0.00, 0.15) m, at rest, turned 129° from how it started; touching ball, block3 | block3 at (0.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (0.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (0.69, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (1.06, 0.00, 0.05) m, at rest; touching block2, floor
1.75 s: block1 at (1.16, 0.00, 0.05) m, at rest; touching floor | block2 at (1.02, 0.00, 0.14) m, at rest, turned 128° from how it started; touching ball, block3 | block3 at (0.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (0.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (0.69, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (1.06, 0.00, 0.05) m, at rest; touching block2, floor
2.00 s: block1 at (1.16, 0.00, 0.05) m, at rest; touching floor | block2 at (1.02, 0.00, 0.14) m, at rest, turned 127° from how it started; touching ball, block3 | block3 at (0.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (0.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (0.69, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (1.06, 0.00, 0.05) m, at rest; touching block2, floor
2.25 s: block1 at (1.16, 0.00, 0.05) m, at rest; touching floor | block2 at (1.02, 0.00, 0.14) m, at rest, turned 126° from how it started; touching ball, block3 | block3 at (0.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (0.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (0.69, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (1.06, 0.00, 0.05) m, at rest; touching block2, floor
2.50 s: block1 at (1.16, 0.00, 0.05) m, at rest; touching floor | block2 at (1.02, 0.00, 0.14) m, at rest, turned 125° from how it started; touching ball, block3 | block3 at (0.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (0.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (0.69, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (1.06, 0.00, 0.05) m, at rest; touching block2, floor
(the same through 3.00 s)
3.25 s: block1 at (1.16, 0.00, 0.05) m, at rest; touching floor | block2 at (1.02, 0.00, 0.14) m, at rest, turned 124° from how it started; touching ball, block3 | block3 at (0.94, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (0.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (0.69, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (1.06, 0.00, 0.05) m, at rest; touching block2, floor
(the same through 4.25 s)
4.50 s: block1 at (1.16, 0.00, 0.05) m, at rest; touching ball, floor | block2 at (1.02, 0.00, 0.14) m, at rest, turned 124° from how it started; touching ball, block3 | block3 at (0.93, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (0.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (0.69, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (1.06, 0.00, 0.05) m, at rest; touching block1, block2, floor
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (1.16, 0.00, 0.05) m, at rest; touching ball, floor
- block2 at (1.02, 0.00, 0.14) m, at rest, turned 124° from how it started; touching ball, block3
- block3 at (0.93, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor
- block4 at (0.82, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- block5 at (0.69, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- ball at (1.06, 0.00, 0.05) m, at rest; touching block1, block2, floor
</history>
