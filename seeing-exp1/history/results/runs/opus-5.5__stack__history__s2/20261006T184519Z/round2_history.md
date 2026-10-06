MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1; starts at (0.00, 0.00, 0.10) m, at rest
- block2: free body; its geoms: block2; starts at (0.00, 0.00, 0.30) m, at rest
- block3: free body; its geoms: block3; starts at (0.00, 0.00, 0.50) m, at rest
- block4: free body; its geoms: block4; starts at (0.00, 0.00, 0.70) m, at rest
- block5: free body; its geoms: block5; starts at (0.00, 0.00, 0.90) m, at rest
- pusher: slide joint pusher_rail about axis (1.00, 0.00, 0.00), no range limit; its geoms: pusher; starts at 0.000 m, moving +2.70 m/s

What happened, in order:
 0.00 s  block1 starts touching floor
 0.00 s  block1 starts touching block2
 0.00 s  block2 starts touching block3
 0.00 s  block3 starts touching block4
 0.01 s  block5 starts moving
 0.01 s  block4 first touches block5
 0.69 s  block1 first touches pusher
 0.69 s  block1 starts moving
 0.69 s  block2 starts moving
 0.69 s  block3 starts moving
 0.69 s  block4 starts moving
 0.99 s  block1 leaves pusher
 1.32 s  block1 leaves block2
 1.32 s  block2 first touches pusher
 1.33 s  block1 touches pusher again
 1.33 s  block3 passes 0.20 m from pusher without touching it: nearest points (-0.14, 0.00, 0.30) m and (-0.01, 0.00, 0.14) m
 1.33 s  block4 passes 0.40 m from pusher without touching it: nearest points (-0.26, 0.00, 0.45) m and (-0.01, 0.00, 0.14) m
 1.35 s  block2 leaves pusher
 1.36 s  block4 leaves block5
 1.37 s  block3 leaves block4
 1.38 s  block2 touches pusher again
 1.42 s  block2 leaves pusher
 1.42 s  block3 touches block4 again
 1.43 s  block2 first touches floor
 1.44 s  block4 touches block5 again
 1.45 s  block1 comes to rest at (0.18, 0.00, 0.10) m
 1.48 s  block3 leaves block4
 1.48 s  pusher is at its largest, 2.0 m
 1.48 s  block2 leaves block3
 1.49 s  block4 leaves block5
 1.53 s  block1 leaves pusher
 1.57 s  block3 first touches floor
 1.58 s  block4 first touches floor
 1.58 s  block5 first touches floor
 1.66 s  block3 comes to rest at (-0.46, 0.00, 0.10) m
 1.68 s  block2 comes to rest at (-0.22, 0.00, 0.10) m
 1.68 s  block4 comes to rest at (-0.70, 0.00, 0.10) m
 1.68 s  block5 comes to rest at (-0.94, 0.00, 0.10) m

State every 0.25 s:
0.00 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3 | block5 at (0.00, 0.00, 0.90) m, at rest; touching nothing | pusher at 0.000 m, moving +2.70 m/s; touching nothing
0.25 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4 | pusher at 0.675 m, moving +2.70 m/s; touching nothing
0.50 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4 | pusher at 1.350 m, moving +2.70 m/s; touching nothing
0.75 s: block1 at (0.09, 0.00, 0.10) m, moving 1.24 m/s (vx +1.24, vy +0.00, vz +0.03); touching pusher | block2 at (0.01, 0.00, 0.30) m, moving 0.25 m/s (vx +0.25, vy +0.00, vz +0.04); touching block3 | block3 at (0.00, 0.00, 0.50) m, moving 0.11 m/s (vx +0.10, vy -0.00, vz +0.05); touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, moving 0.06 m/s (vx -0.04, vy -0.00, vz +0.05); touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, moving 0.18 m/s (vx -0.18, vy -0.00, vz +0.05), turned 1° from how it started; touching block4 | pusher at 1.944 m, moving +1.01 m/s; touching block1
1.00 s: block1 at (0.17, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.05, 0.00, 0.30) m, moving 0.08 m/s (vx -0.08, vy -0.00, vz -0.01), turned 13° from how it started; touching block1, block3 | block3 at (0.00, 0.00, 0.49) m, moving 0.23 m/s (vx -0.23, vy -0.00, vz -0.05), turned 13° from how it started; touching block2, block4 | block4 at (-0.04, 0.00, 0.69) m, moving 0.38 m/s (vx -0.37, vy -0.00, vz -0.08), turned 13° from how it started; touching block3, block5 | block5 at (-0.09, 0.00, 0.88) m, moving 0.53 m/s (vx -0.51, vy -0.00, vz -0.11), turned 13° from how it started; touching block4 | pusher at 2.016 m, still; touching nothing
1.25 s: block1 at (0.17, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (-0.01, 0.00, 0.27) m, moving 0.55 m/s (vx -0.45, vy -0.00, vz -0.32), turned 29° from how it started; touching block1, block3 | block3 at (-0.11, 0.00, 0.44) m, moving 0.89 m/s (vx -0.75, vy -0.00, vz -0.48), turned 29° from how it started; touching block2, block4 | block4 at (-0.21, 0.00, 0.62) m, moving 1.22 m/s (vx -1.04, vy -0.00, vz -0.64), turned 29° from how it started; touching block3, block5 | block5 at (-0.31, 0.00, 0.79) m, moving 1.56 m/s (vx -1.34, vy -0.00, vz -0.80), turned 29° from how it started; touching block4 | pusher at 2.017 m, still; touching nothing
1.50 s: block1 at (0.18, 0.00, 0.10) m, at rest; touching floor, pusher | block2 at (-0.18, 0.00, 0.13) m, moving 0.70 m/s (vx -0.67, vy -0.00, vz -0.21), turned 69° from how it started; touching floor | block3 at (-0.37, 0.00, 0.20) m, moving 1.67 m/s (vx -1.20, vy -0.00, vz -1.16), turned 68° from how it started; touching nothing | block4 at (-0.56, 0.00, 0.28) m, moving 2.62 m/s (vx -1.75, vy -0.00, vz -1.95), turned 68° from how it started; touching nothing | block5 at (-0.74, 0.00, 0.36) m, moving 3.62 m/s (vx -2.31, vy -0.00, vz -2.79), turned 69° from how it started; touching nothing | pusher at 2.032 m, still; touching block1
1.75 s: block1 at (0.18, 0.00, 0.10) m, at rest; touching floor | block2 at (-0.22, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.46, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.70, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.94, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 2.031 m, still; touching nothing
2.00 s: block1 at (0.18, 0.00, 0.10) m, at rest; touching floor | block2 at (-0.22, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.46, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.70, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.94, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 2.030 m, still; touching nothing
(the same through 2.25 s)
2.50 s: block1 at (0.18, 0.00, 0.10) m, at rest; touching floor | block2 at (-0.22, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.46, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.70, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.94, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 2.029 m, still; touching nothing
2.75 s: block1 at (0.18, 0.00, 0.10) m, at rest; touching floor | block2 at (-0.22, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.46, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.70, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.94, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 2.028 m, still; touching nothing
(the same through 3.00 s)
3.25 s: block1 at (0.18, 0.00, 0.10) m, at rest; touching floor | block2 at (-0.22, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.46, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.70, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.94, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 2.027 m, still; touching nothing
3.50 s: block1 at (0.18, 0.00, 0.10) m, at rest; touching floor | block2 at (-0.22, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.46, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.70, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.94, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 2.026 m, still; touching nothing
(the same through 3.75 s)
4.00 s: block1 at (0.18, 0.00, 0.10) m, at rest; touching floor | block2 at (-0.22, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.46, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.70, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.94, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 2.025 m, still; touching nothing
4.25 s: block1 at (0.18, 0.00, 0.10) m, at rest; touching floor | block2 at (-0.22, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.46, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.70, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.94, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 2.024 m, still; touching nothing
(the same through 4.50 s)
4.75 s: block1 at (0.18, 0.00, 0.10) m, at rest; touching floor | block2 at (-0.22, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.46, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.70, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.94, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 2.023 m, still; touching nothing
5.00 s: block1 at (0.18, 0.00, 0.10) m, at rest; touching floor | block2 at (-0.22, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.46, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.70, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.94, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 2.022 m, still; touching nothing
(the same through 5.25 s)
5.50 s: block1 at (0.18, 0.00, 0.10) m, at rest; touching floor | block2 at (-0.22, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.46, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.70, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.94, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 2.021 m, still; touching nothing
5.75 s: block1 at (0.18, 0.00, 0.10) m, at rest; touching floor | block2 at (-0.22, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.46, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.70, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.94, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 2.020 m, still; touching nothing
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (0.18, 0.00, 0.10) m, at rest; touching floor
- block2 at (-0.22, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- block3 at (-0.46, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- block4 at (-0.70, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- block5 at (-0.94, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- pusher at 2.020 m, still; touching nothing
</history>
