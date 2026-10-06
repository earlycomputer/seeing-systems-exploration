Your expectations, checked against the run (2 of 2 hold):

- holds: ball touches block1 (first touch at 0.84 s)
- holds: block5 touches floor (first touch at 1.59 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1; starts at (2.50, 0.00, 0.05) m, at rest
- block2: free body; its geoms: block2; starts at (2.50, 0.00, 0.15) m, at rest
- block3: free body; its geoms: block3; starts at (2.50, 0.00, 0.25) m, at rest
- block4: free body; its geoms: block4; starts at (2.50, 0.00, 0.35) m, at rest
- block5: free body; its geoms: block5; starts at (2.50, 0.00, 0.45) m, at rest
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.04) m, moving 3.00 m/s (vx +3.00, vy +0.00, vz +0.00)

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
 0.84 s  ball leaves floor
 0.84 s  block1 first touches ball
 0.84 s  block1 starts moving
 0.84 s  block2 starts moving
 0.86 s  block1 leaves ball
 0.88 s  block2 first touches ball
 0.90 s  block2 leaves ball
 0.90 s  block1 leaves floor
 0.94 s  block1 touches floor again
 0.94 s  block1 touches ball again
 0.94 s  ball touches floor again
 1.00 s  block1 leaves ball
 1.37 s  block2 touches ball again
 1.38 s  block1 leaves block2
 1.41 s  block1 touches block2 again
 1.42 s  block1 touches ball again
 1.43 s  block4 leaves block5
 1.44 s  ball comes to rest at (2.50, 0.00, 0.04) m
 1.44 s  block1 comes to rest at (2.59, 0.00, 0.05) m
 1.47 s  block1 leaves block2
 1.48 s  block3 leaves block4
 1.49 s  block4 touches block5 again
 1.49 s  block4 leaves block5
 1.50 s  block2 leaves block3
 1.51 s  block5 passes 0.26 m from ball without touching it: nearest points (2.23, 0.00, 0.16) m and (2.47, 0.00, 0.06) m
 1.52 s  block4 passes 0.15 m from ball without touching it: nearest points (2.33, 0.00, 0.10) m and (2.47, 0.00, 0.05) m
 1.55 s  block3 passes 0.04 m from ball without touching it: nearest points (2.43, 0.00, 0.05) m and (2.47, 0.00, 0.05) m
 1.58 s  block4 first touches floor
 1.58 s  block3 first touches floor
 1.59 s  block5 first touches floor
 1.61 s  block2 touches block3 again
 1.61 s  block2 leaves ball
 1.66 s  block2 touches ball again
 1.67 s  block3 comes to rest at (2.37, 0.00, 0.05) m
 1.68 s  block4 comes to rest at (2.24, 0.00, 0.05) m
 1.69 s  block2 leaves block3
 1.69 s  block1 leaves ball
 1.69 s  block5 comes to rest at (2.11, 0.00, 0.05) m
 1.78 s  block2 touches block3 again
 1.78 s  block2 comes to rest at (2.46, 0.00, 0.12) m
 2.40 s  block1 touches ball again

State every 0.25 s:
0.00 s: block1 at (2.50, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.50, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.50, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.50, 0.00, 0.35) m, at rest; touching block3 | block5 at (2.50, 0.00, 0.45) m, at rest; touching nothing | ball at (0.00, 0.00, 0.04) m, moving 3.00 m/s (vx +3.00, vy +0.00, vz +0.00); touching floor
0.25 s: block1 at (2.50, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.50, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.50, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.50, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.50, 0.00, 0.45) m, at rest; touching block4 | ball at (0.74, 0.00, 0.04) m, moving 2.95 m/s (vx +2.95, vy -0.00, vz -0.01); touching nothing
0.50 s: block1 at (2.50, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.50, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.50, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.50, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.50, 0.00, 0.45) m, at rest; touching block4 | ball at (1.47, 0.00, 0.04) m, moving 2.86 m/s (vx +2.86, vy -0.00, vz +0.03); touching nothing
0.75 s: block1 at (2.50, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.50, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.50, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.50, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.50, 0.00, 0.45) m, at rest; touching block4 | ball at (2.17, 0.00, 0.04) m, moving 2.78 m/s (vx +2.78, vy +0.00, vz +0.02); touching nothing
1.00 s: block1 at (2.59, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.55, 0.00, 0.15) m, at rest, turned 11° from how it started; touching block1, block3 | block3 at (2.53, 0.00, 0.25) m, at rest, turned 10° from how it started; touching block2, block4 | block4 at (2.51, 0.00, 0.35) m, at rest, turned 9° from how it started; touching block3, block5 | block5 at (2.49, 0.00, 0.44) m, at rest, turned 9° from how it started; touching block4 | ball at (2.50, 0.00, 0.04) m, at rest; touching floor
1.25 s: block1 at (2.59, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.54, 0.00, 0.15) m, moving 0.08 m/s (vx -0.08, vy -0.00, vz -0.01), turned 19° from how it started; touching block1, block3 | block3 at (2.50, 0.00, 0.24) m, moving 0.23 m/s (vx -0.22, vy -0.00, vz -0.06), turned 19° from how it started; touching block2, block4 | block4 at (2.47, 0.00, 0.34) m, moving 0.38 m/s (vx -0.36, vy -0.00, vz -0.11), turned 19° from how it started; touching block3, block5 | block5 at (2.44, 0.00, 0.43) m, moving 0.53 m/s (vx -0.51, vy -0.00, vz -0.16), turned 19° from how it started; touching block4 | ball at (2.50, 0.00, 0.04) m, at rest; touching floor
1.50 s: block1 at (2.60, 0.00, 0.05) m, at rest; touching ball, floor | block2 at (2.50, 0.00, 0.14) m, moving 0.31 m/s (vx -0.29, vy -0.00, vz -0.10), turned 70° from how it started; touching ball, block3 | block3 at (2.41, 0.00, 0.17) m, moving 1.05 m/s (vx -0.54, vy -0.00, vz -0.90), turned 71° from how it started; touching block2 | block4 at (2.31, 0.00, 0.20) m, moving 1.67 m/s (vx -0.82, vy -0.00, vz -1.46), turned 70° from how it started; touching nothing | block5 at (2.22, 0.00, 0.24) m, moving 2.09 m/s (vx -1.08, vy -0.00, vz -1.79), turned 65° from how it started; touching nothing | ball at (2.51, 0.00, 0.04) m, at rest; touching block1, block2, floor
1.75 s: block1 at (2.60, 0.00, 0.05) m, at rest; touching floor | block2 at (2.47, 0.00, 0.12) m, at rest, turned 122° from how it started; touching ball | block3 at (2.37, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (2.25, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (2.11, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (2.50, 0.00, 0.04) m, at rest; touching block2, floor
2.00 s: block1 at (2.60, 0.00, 0.05) m, at rest; touching floor | block2 at (2.46, 0.00, 0.12) m, at rest, turned 122° from how it started; touching ball, block3 | block3 at (2.37, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (2.25, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (2.11, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (2.50, 0.00, 0.04) m, at rest; touching block2, floor
(the same through 2.25 s)
2.50 s: block1 at (2.60, 0.00, 0.05) m, at rest; touching ball, floor | block2 at (2.46, 0.00, 0.12) m, at rest, turned 121° from how it started; touching ball, block3 | block3 at (2.37, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (2.25, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (2.11, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (2.51, 0.00, 0.04) m, at rest; touching block1, block2, floor
(the same through 3.25 s)
3.50 s: block1 at (2.60, 0.00, 0.05) m, at rest; touching ball, floor | block2 at (2.46, 0.00, 0.12) m, at rest, turned 120° from how it started; touching ball, block3 | block3 at (2.37, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (2.25, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (2.11, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (2.51, 0.00, 0.04) m, at rest; touching block1, block2, floor
(the same through 4.75 s)
5.00 s: block1 at (2.60, 0.00, 0.05) m, at rest; touching ball, floor | block2 at (2.46, 0.00, 0.12) m, at rest, turned 120° from how it started; touching ball, block3 | block3 at (2.36, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (2.25, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (2.11, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | ball at (2.51, 0.00, 0.04) m, at rest; touching block1, block2, floor
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (2.60, 0.00, 0.05) m, at rest; touching ball, floor
- block2 at (2.46, 0.00, 0.12) m, at rest, turned 120° from how it started; touching ball, block3
- block3 at (2.36, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2, floor
- block4 at (2.25, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- block5 at (2.11, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- ball at (2.51, 0.00, 0.04) m, at rest; touching block1, block2, floor
</history>
