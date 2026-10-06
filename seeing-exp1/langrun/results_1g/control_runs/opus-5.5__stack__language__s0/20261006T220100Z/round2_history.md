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
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.04) m, moving 4.00 m/s (vx +4.00, vy +0.00, vz +0.00)

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
 0.49 s  ball leaves floor
 0.49 s  block1 first touches ball
 0.49 s  block1 starts moving
 0.49 s  block2 starts moving
 0.51 s  block1 leaves block2
 0.52 s  block2 first touches ball
 0.52 s  block3 passes 0.10 m from ball without touching it: nearest points (2.02, 0.00, 0.20) m and (2.02, 0.00, 0.10) m
 0.52 s  block4 passes 0.20 m from ball without touching it: nearest points (2.01, 0.00, 0.30) m and (2.02, 0.00, 0.10) m
 0.52 s  block5 passes 0.30 m from ball without touching it: nearest points (2.01, 0.00, 0.40) m and (2.02, 0.00, 0.10) m
 0.55 s  block1 leaves floor
 0.55 s  block2 leaves block3
 0.55 s  block3 leaves block4
 0.56 s  block4 leaves block5
 0.57 s  block1 leaves ball
 0.57 s  block2 leaves ball
 0.58 s  block3 is at the top of its flight, at (2.02, 0.00, 0.27) m
 0.59 s  block5 is at the top of its flight, at (1.98, 0.00, 0.47) m
 0.59 s  block4 is at the top of its flight, at (2.00, 0.00, 0.37) m
 0.60 s  block2 is at the top of its flight, at (2.11, 0.00, 0.17) m
 0.65 s  block1 touches floor again
 0.66 s  block1 leaves floor
 0.67 s  ball touches floor again
 0.72 s  block1 is at the top of its flight, at (2.52, 0.00, 0.06) m
 0.75 s  block2 first touches floor
 0.77 s  block1 touches floor again
 0.80 s  block3 first touches floor
 0.82 s  block1 leaves floor
 0.84 s  block4 first touches floor
 0.86 s  block4 touches block5 again
 0.89 s  block5 first touches floor
 0.89 s  block1 touches floor again
 0.89 s  block4 leaves block5
 0.90 s  block3 comes to rest at (2.10, 0.00, 0.03) m
 0.92 s  ball leaves floor
 0.92 s  block1 touches ball again
 0.95 s  block4 comes to rest at (1.96, 0.00, 0.03) m
 0.96 s  block1 leaves floor
 0.98 s  block1 leaves ball
 0.99 s  block5 comes to rest at (1.85, 0.00, 0.03) m
 1.00 s  block1 touches floor 1 more times between 1.00 s and 6.00 s, still touching at the end
 1.00 s  ball touches floor again
 1.08 s  block1 touches ball again
 1.11 s  block1 leaves ball
 1.16 s  block1 touches ball again
 1.20 s  block1 comes to rest at (2.81, 0.00, 0.03) m
 1.21 s  block2 comes to rest at (2.31, 0.00, 0.05) m
 1.21 s  ball comes to rest at (2.72, 0.00, 0.04) m
 1.31 s  block1 leaves ball

State every 0.25 s:
0.00 s: block1 at (2.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.35) m, at rest; touching block3 | block5 at (2.00, 0.00, 0.45) m, at rest; touching nothing | ball at (0.00, 0.00, 0.04) m, moving 4.00 m/s (vx +4.00, vy +0.00, vz +0.00); touching floor
0.25 s: block1 at (2.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.00, 0.00, 0.45) m, at rest; touching block4 | ball at (0.99, 0.00, 0.04) m, moving 3.99 m/s (vx +3.99, vy +0.00, vz -0.01); touching floor
0.50 s: block1 at (2.02, 0.00, 0.05) m, moving 2.14 m/s (vx +2.09, vy +0.00, vz +0.47); touching ball, block2 | block2 at (2.00, 0.00, 0.15) m, moving 0.34 m/s (vx +0.33, vy +0.00, vz +0.07), turned 2° from how it started; touching block1, block3 | block3 at (2.00, 0.00, 0.25) m, moving 0.18 m/s (vx +0.13, vy +0.00, vz +0.11); touching block2, block4 | block4 at (2.00, 0.00, 0.35) m, moving 0.12 m/s (vx +0.03, vy +0.00, vz +0.12); touching block3, block5 | block5 at (2.00, 0.00, 0.45) m, moving 0.13 m/s (vx -0.06, vy +0.00, vz +0.12); touching block4 | ball at (1.97, 0.00, 0.05) m, moving 2.57 m/s (vx +2.43, vy -0.00, vz +0.83); touching block1
0.75 s: block1 at (2.56, 0.00, 0.05) m, moving 1.51 m/s (vx +1.48, vy +0.00, vz -0.33), turned 78° from how it started; touching nothing | block2 at (2.30, 0.00, 0.06) m, moving 1.94 m/s (vx +1.24, vy -0.00, vz -1.49), turned 165° from how it started; touching nothing | block3 at (2.08, 0.00, 0.13) m, moving 1.68 m/s (vx +0.35, vy -0.00, vz -1.64), turned 69° from how it started; touching nothing | block4 at (1.99, 0.00, 0.24) m, moving 1.60 m/s (vx -0.05, vy +0.00, vz -1.60), turned 38° from how it started; touching nothing | block5 at (1.92, 0.00, 0.34) m, moving 1.65 m/s (vx -0.32, vy +0.00, vz -1.62), turned 38° from how it started; touching nothing | ball at (2.38, 0.00, 0.04) m, moving 1.23 m/s (vx +1.23, vy -0.00, vz +0.04); touching floor
1.00 s: block1 at (2.74, 0.00, 0.03) m, moving 0.97 m/s (vx +0.94, vy +0.00, vz -0.26), turned 90° from how it started; touching floor | block2 at (2.31, 0.00, 0.05) m, moving 0.24 m/s (vx -0.22, vy +0.00, vz -0.10), turned 173° from how it started; touching floor | block3 at (2.10, 0.00, 0.03) m, at rest, turned 90° from how it started; touching floor | block4 at (1.96, 0.00, 0.03) m, at rest, turned 90° from how it started; touching floor | block5 at (1.85, 0.00, 0.03) m, at rest, turned 91° from how it started; touching floor | ball at (2.64, 0.00, 0.04) m, moving 0.64 m/s (vx +0.61, vy -0.00, vz -0.20); touching floor
1.25 s: block1 at (2.81, 0.00, 0.03) m, at rest, turned 90° from how it started; touching ball, floor | block2 at (2.31, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (2.10, 0.00, 0.03) m, at rest, turned 90° from how it started; touching floor | block4 at (1.96, 0.00, 0.03) m, at rest, turned 90° from how it started; touching floor | block5 at (1.85, 0.00, 0.03) m, at rest, turned 90° from how it started; touching floor | ball at (2.72, 0.00, 0.04) m, at rest; touching block1, floor
1.50 s: block1 at (2.81, 0.00, 0.03) m, at rest, turned 90° from how it started; touching floor | block2 at (2.31, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (2.10, 0.00, 0.03) m, at rest, turned 90° from how it started; touching floor | block4 at (1.96, 0.00, 0.03) m, at rest, turned 90° from how it started; touching floor | block5 at (1.85, 0.00, 0.03) m, at rest, turned 90° from how it started; touching floor | ball at (2.72, 0.00, 0.04) m, at rest; touching floor
(the same through 2.00 s)
2.25 s: block1 at (2.81, 0.00, 0.03) m, at rest, turned 90° from how it started; touching floor | block2 at (2.31, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (2.10, 0.00, 0.03) m, at rest, turned 90° from how it started; touching floor | block4 at (1.96, 0.00, 0.03) m, at rest, turned 90° from how it started; touching floor | block5 at (1.85, 0.00, 0.03) m, at rest, turned 90° from how it started; touching floor | ball at (2.71, 0.00, 0.04) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (2.81, 0.00, 0.03) m, at rest, turned 90° from how it started; touching floor
- block2 at (2.31, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor
- block3 at (2.10, 0.00, 0.03) m, at rest, turned 90° from how it started; touching floor
- block4 at (1.96, 0.00, 0.03) m, at rest, turned 90° from how it started; touching floor
- block5 at (1.85, 0.00, 0.03) m, at rest, turned 90° from how it started; touching floor
- ball at (2.71, 0.00, 0.04) m, at rest; touching floor
</history>
