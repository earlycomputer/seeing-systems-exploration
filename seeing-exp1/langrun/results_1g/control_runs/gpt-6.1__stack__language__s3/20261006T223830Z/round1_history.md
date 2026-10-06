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
- pusher: free body; its geoms: pusher; starts at (-1.38, 0.00, 0.08) m, moving 2.00 m/s (vx +2.00, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  block1 starts touching floor
 0.00 s  block1 starts touching block2
 0.00 s  block3 starts touching block4
 0.00 s  pusher starts touching floor
 0.00 s  block2 starts touching block3
 0.01 s  block5 starts moving
 0.01 s  block4 first touches block5
 0.60 s  pusher leaves floor
 0.60 s  block1 first touches pusher
 0.60 s  block1 starts moving
 0.60 s  block2 starts moving
 0.60 s  block3 starts moving
 0.60 s  block4 starts moving
 0.62 s  block1 leaves pusher
 0.68 s  pusher touches floor again
 0.69 s  block1 touches pusher again
 0.73 s  block1 leaves pusher
 0.79 s  block1 touches pusher again
 0.79 s  block1 leaves pusher
 0.81 s  block1 leaves floor
 0.85 s  block1 touches floor again
 0.89 s  block1 touches pusher again
 0.90 s  block1 leaves block2
 0.91 s  block1 leaves pusher
 0.91 s  block1 leaves floor
 0.91 s  block4 leaves block5
 0.93 s  block2 first touches pusher
 0.94 s  block1 touches floor again
 0.95 s  block4 touches block5 again
 1.02 s  block1 touches pusher 5 more times between 1.02 s and 1.56 s
 1.06 s  block1 touches block2 again
 1.10 s  block4 leaves block5
 1.14 s  block4 touches block5 again
 1.16 s  block4 leaves block5
 1.16 s  block3 leaves block4
 1.19 s  block2 leaves block3
 1.23 s  block4 passes 0.29 m from pusher without touching it: nearest points (-0.14, 0.00, 0.20) m and (0.14, 0.00, 0.10) m
 1.28 s  block3 passes 0.06 m from pusher without touching it: nearest points (0.09, 0.00, 0.09) m and (0.15, 0.00, 0.09) m
 1.28 s  block1 leaves floor
 1.29 s  block1 leaves block2
 1.31 s  block3 first touches floor
 1.31 s  block4 first touches floor
 1.31 s  block1 touches floor again
 1.32 s  block5 first touches floor
 1.38 s  block2 touches block3 again
 1.38 s  block2 leaves pusher
 1.39 s  block4 comes to rest at (-0.28, 0.00, 0.10) m
 1.40 s  block2 leaves block3
 1.40 s  block5 comes to rest at (-0.52, 0.00, 0.10) m
 1.43 s  block3 comes to rest at (0.00, 0.00, 0.10) m
 1.44 s  block2 touches block3 again
 1.50 s  pusher comes to rest at (0.26, 0.00, 0.08) m
 1.51 s  block1 comes to rest at (0.44, 0.00, 0.10) m
 1.53 s  block2 leaves block3
 1.53 s  block2 touches pusher again
 1.85 s  block2 touches block3 again
 1.86 s  block2 comes to rest at (0.19, 0.00, 0.25) m

State every 0.25 s:
0.00 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3 | block5 at (0.00, 0.00, 0.90) m, at rest; touching nothing | pusher at (-1.38, 0.00, 0.08) m, moving 2.00 m/s (vx +2.00, vy +0.00, vz +0.00); touching floor
0.25 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4 | pusher at (-0.88, 0.00, 0.08) m, moving 2.00 m/s (vx +2.00, vy -0.00, vz +0.00); touching floor
0.50 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4 | pusher at (-0.39, 0.00, 0.08) m, moving 1.99 m/s (vx +1.99, vy -0.00, vz -0.00); touching floor
0.75 s: block1 at (0.19, 0.00, 0.10) m, moving 0.90 m/s (vx +0.88, vy +0.00, vz +0.21), turned 1° from how it started; touching block2, floor | block2 at (0.09, 0.00, 0.30) m, moving 0.52 m/s (vx +0.52, vy +0.00, vz -0.06), turned 11° from how it started; touching block1, block3 | block3 at (0.05, 0.00, 0.50) m, moving 0.41 m/s (vx +0.33, vy -0.00, vz -0.24), turned 11° from how it started; touching block2, block4 | block4 at (0.01, 0.00, 0.70) m, moving 0.22 m/s (vx +0.03, vy -0.00, vz -0.21), turned 10° from how it started; touching block3, block5 | block5 at (-0.03, 0.00, 0.89) m, moving 0.30 m/s (vx -0.19, vy -0.00, vz -0.23), turned 10° from how it started; touching block4 | pusher at (0.00, 0.00, 0.08) m, moving 0.91 m/s (vx +0.91, vy -0.00, vz +0.00); touching floor
1.00 s: block1 at (0.33, 0.00, 0.10) m, moving 0.13 m/s (vx +0.12, vy -0.00, vz -0.03), turned 1° from how it started; touching floor | block2 at (0.18, 0.00, 0.30) m, moving 0.37 m/s (vx +0.37, vy +0.00, vz +0.05), turned 34° from how it started; touching block3, pusher | block3 at (0.07, 0.00, 0.46) m, moving 0.26 m/s (vx -0.05, vy +0.00, vz -0.26), turned 34° from how it started; touching block2, block4 | block4 at (-0.05, 0.00, 0.63) m, moving 0.72 m/s (vx -0.48, vy +0.00, vz -0.54), turned 34° from how it started; touching block3 | block5 at (-0.16, 0.00, 0.79) m, moving 1.22 m/s (vx -0.89, vy +0.00, vz -0.83), turned 34° from how it started; touching nothing | pusher at (0.14, 0.00, 0.08) m, moving 0.35 m/s (vx +0.35, vy -0.00, vz +0.00); touching block2, floor
1.25 s: block1 at (0.40, 0.00, 0.10) m, moving 0.33 m/s (vx +0.32, vy -0.00, vz -0.07), turned 2° from how it started; touching block2 | block2 at (0.20, 0.00, 0.26) m, moving 0.14 m/s (vx -0.12, vy +0.00, vz -0.07), turned 91° from how it started; touching block1, pusher | block3 at (-0.01, 0.00, 0.24) m, moving 1.89 m/s (vx -0.40, vy +0.00, vz -1.84), turned 88° from how it started; touching nothing | block4 at (-0.22, 0.00, 0.27) m, moving 2.67 m/s (vx -0.85, vy +0.00, vz -2.53), turned 79° from how it started; touching nothing | block5 at (-0.43, 0.00, 0.33) m, moving 3.28 m/s (vx -1.19, vy -0.00, vz -3.05), turned 76° from how it started; touching nothing | pusher at (0.22, 0.00, 0.08) m, moving 0.26 m/s (vx +0.26, vy -0.00, vz -0.00); touching block2, floor
1.50 s: block1 at (0.44, 0.00, 0.10) m, moving 0.07 m/s (vx +0.06, vy +0.00, vz +0.03); touching floor, pusher | block2 at (0.19, 0.00, 0.26) m, moving 0.27 m/s (vx +0.16, vy +0.00, vz -0.22), turned 133° from how it started; touching block3 | block3 at (0.00, 0.00, 0.10) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (-0.28, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.52, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (0.26, 0.00, 0.08) m, at rest; touching block1, floor
1.75 s: block1 at (0.44, 0.00, 0.10) m, at rest; touching floor | block2 at (0.21, 0.00, 0.25) m, moving 0.08 m/s (vx -0.08, vy +0.00, vz -0.02), turned 115° from how it started; touching pusher | block3 at (0.00, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.28, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.52, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (0.26, 0.00, 0.08) m, at rest; touching block2, floor
2.00 s: block1 at (0.44, 0.00, 0.10) m, at rest; touching floor | block2 at (0.19, 0.00, 0.25) m, at rest, turned 120° from how it started; touching block3, pusher | block3 at (0.00, 0.00, 0.10) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (-0.28, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.52, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (0.26, 0.00, 0.08) m, at rest; touching block2, floor
(the same through 4.00 s)
4.25 s: block1 at (0.44, 0.00, 0.10) m, at rest; touching floor | block2 at (0.19, 0.00, 0.25) m, at rest, turned 119° from how it started; touching block3, pusher | block3 at (0.00, 0.00, 0.10) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (-0.28, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.52, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (0.26, 0.00, 0.08) m, at rest; touching block2, floor
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (0.44, 0.00, 0.10) m, at rest; touching floor
- block2 at (0.19, 0.00, 0.25) m, at rest, turned 119° from how it started; touching block3, pusher
- block3 at (0.00, 0.00, 0.10) m, at rest, turned 90° from how it started; touching block2, floor
- block4 at (-0.28, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- block5 at (-0.52, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- pusher at (0.26, 0.00, 0.08) m, at rest; touching block2, floor
</history>
