MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1; starts at (2.00, 0.00, 0.10) m, at rest
- block2: free body; its geoms: block2; starts at (2.00, 0.00, 0.30) m, at rest
- block3: free body; its geoms: block3; starts at (2.00, 0.00, 0.50) m, at rest
- block4: free body; its geoms: block4; starts at (2.00, 0.00, 0.70) m, at rest
- block5: free body; its geoms: block5; starts at (2.00, 0.00, 0.90) m, at rest
- pusher: free body; its geoms: pusher; starts at (0.30, 0.00, 0.09) m, moving 3.00 m/s (vx +3.00, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  block1 starts touching floor
 0.00 s  block1 starts touching block2
 0.00 s  block3 starts touching block4
 0.00 s  pusher starts touching floor
 0.00 s  block2 starts touching block3
 0.01 s  block5 starts moving
 0.01 s  block4 first touches block5
 0.50 s  pusher leaves floor
 0.51 s  block1 first touches pusher
 0.51 s  block1 starts moving
 0.51 s  block2 starts moving
 0.51 s  block3 starts moving
 0.51 s  block4 starts moving
 0.51 s  block1 leaves block2
 0.53 s  block1 leaves floor
 0.53 s  block1 leaves pusher
 0.53 s  block4 leaves block5
 0.54 s  block2 leaves block3
 0.54 s  block3 leaves block4
 0.57 s  block2 first touches pusher
 0.57 s  block2 touches block3 again
 0.57 s  block3 touches block4 again
 0.57 s  block4 touches block5 again
 0.58 s  block2 leaves pusher
 0.58 s  block1 touches floor again
 0.58 s  block1 leaves floor
 0.59 s  block3 leaves block4
 0.60 s  block4 leaves block5
 0.61 s  block2 leaves block3
 0.61 s  pusher touches floor again
 0.62 s  block1 touches floor again
 0.62 s  block1 leaves floor
 0.64 s  block1 touches block2 again
 0.64 s  block2 touches pusher again
 0.65 s  block2 leaves pusher
 0.65 s  block2 touches block3 again
 0.66 s  block1 leaves block2
 0.67 s  block2 leaves block3
 0.69 s  block1 touches floor again
 0.69 s  block1 leaves floor
 0.70 s  block1 touches block2 again
 0.73 s  block1 touches floor 8 more times between 0.73 s and 6.00 s, still touching at the end
 0.73 s  block2 touches pusher again
 0.74 s  block2 touches block3 again
 0.74 s  block2 leaves block3
 0.78 s  block3 first touches pusher
 0.79 s  block2 leaves pusher
 0.79 s  block3 leaves pusher
 0.85 s  block3 touches pusher again
 0.87 s  block3 touches block4 again
 0.87 s  block4 passes 0.20 m from pusher without touching it: nearest points (2.16, 0.00, 0.30) m and (2.30, 0.00, 0.16) m
 0.89 s  block3 leaves block4
 0.90 s  block3 leaves pusher
 0.90 s  block4 touches block5 again
 0.92 s  block5 passes 0.42 m from pusher without touching it: nearest points (2.00, 0.00, 0.38) m and (2.35, 0.00, 0.14) m
 0.94 s  block3 is at the top of its flight, at (2.26, 0.00, 0.27) m
 0.95 s  block1 leaves block2
 0.95 s  block4 first touches floor
 0.97 s  block4 leaves block5
 1.00 s  block1 touches block2 again
 1.01 s  block1 leaves block2
 1.03 s  block5 first touches floor
 1.04 s  block1 touches block2 4 more times between 1.04 s and 1.36 s
 1.04 s  block2 first touches floor
 1.06 s  pusher leaves floor
 1.06 s  block2 touches pusher again
 1.07 s  block2 leaves pusher
 1.07 s  block2 leaves floor
 1.09 s  pusher touches floor again
 1.11 s  block4 comes to rest at (1.99, 0.00, 0.10) m
 1.11 s  block3 first touches floor
 1.11 s  block2 touches pusher 4 more times between 1.11 s and 1.57 s
 1.15 s  block2 touches floor again
 1.20 s  block2 leaves floor
 1.25 s  block2 touches floor again
 1.43 s  block1 comes to rest at (3.19, 0.00, 0.10) m
 1.47 s  pusher comes to rest at (2.80, 0.00, 0.09) m
 1.48 s  block2 comes to rest at (2.99, 0.00, 0.10) m
 1.60 s  block5 comes to rest at (1.67, 0.00, 0.10) m
 1.60 s  block3 comes to rest at (2.36, 0.00, 0.10) m

State every 0.25 s:
0.00 s: block1 at (2.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.70) m, at rest; touching block3 | block5 at (2.00, 0.00, 0.90) m, at rest; touching nothing | pusher at (0.30, 0.00, 0.09) m, moving 3.00 m/s (vx +3.00, vy +0.00, vz +0.00); touching floor
0.25 s: block1 at (2.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (2.00, 0.00, 0.90) m, at rest; touching block4 | pusher at (1.04, 0.00, 0.09) m, moving 2.98 m/s (vx +2.98, vy +0.00, vz -0.01); touching floor
0.50 s: block1 at (2.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (2.00, 0.00, 0.90) m, at rest; touching block4 | pusher at (1.78, 0.00, 0.09) m, moving 2.94 m/s (vx +2.94, vy +0.00, vz +0.00); touching floor
0.75 s: block1 at (2.54, 0.00, 0.11) m, moving 1.92 m/s (vx +1.92, vy -0.00, vz +0.10), turned 3° from how it started; touching nothing | block2 at (2.34, 0.00, 0.23) m, moving 2.12 m/s (vx +2.12, vy +0.00, vz -0.13), turned 59° from how it started; touching pusher | block3 at (2.16, 0.00, 0.36) m, moving 1.73 m/s (vx +0.77, vy +0.00, vz -1.55), turned 51° from how it started; touching nothing | block4 at (2.02, 0.00, 0.58) m, moving 1.57 m/s (vx +0.09, vy +0.00, vz -1.56), turned 26° from how it started; touching nothing | block5 at (1.93, 0.00, 0.78) m, moving 1.61 m/s (vx -0.36, vy -0.00, vz -1.57), turned 27° from how it started; touching nothing | pusher at (2.20, 0.00, 0.09) m, moving 1.32 m/s (vx +1.32, vy -0.00, vz +0.00); touching block2, floor
1.00 s: block1 at (2.94, 0.00, 0.10) m, moving 1.18 m/s (vx +1.15, vy -0.00, vz -0.27); touching block2 | block2 at (2.74, 0.00, 0.15) m, moving 1.51 m/s (vx +1.08, vy +0.00, vz -1.06), turned 89° from how it started; touching block1 | block3 at (2.26, 0.00, 0.25) m, moving 0.57 m/s (vx +0.15, vy +0.00, vz -0.55), turned 131° from how it started; touching nothing | block4 at (1.98, 0.00, 0.10) m, moving 0.26 m/s (vx -0.11, vy -0.00, vz +0.23), turned 92° from how it started; touching floor | block5 at (1.73, 0.00, 0.17) m, moving 3.35 m/s (vx -2.45, vy -0.00, vz -2.29), turned 79° from how it started; touching nothing | pusher at (2.52, 0.00, 0.09) m, moving 1.25 m/s (vx +1.25, vy -0.00, vz +0.00); touching floor
1.25 s: block1 at (3.14, 0.00, 0.10) m, moving 0.43 m/s (vx +0.42, vy -0.00, vz -0.07); touching nothing | block2 at (2.94, 0.00, 0.11) m, moving 0.75 m/s (vx +0.73, vy -0.00, vz -0.15), turned 93° from how it started; touching floor | block3 at (2.28, 0.00, 0.14) m, moving 0.08 m/s (vx +0.07, vy +0.00, vz -0.01), turned 54° from how it started; touching floor | block4 at (1.99, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.60, 0.00, 0.14) m, at rest, turned 121° from how it started; touching floor | pusher at (2.73, 0.00, 0.09) m, moving 0.52 m/s (vx +0.52, vy -0.00, vz +0.00); touching floor
1.50 s: block1 at (3.19, 0.00, 0.10) m, at rest; touching floor | block2 at (2.99, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor, pusher | block3 at (2.35, 0.00, 0.11) m, moving 0.70 m/s (vx +0.53, vy +0.00, vz -0.45), turned 85° from how it started; touching nothing | block4 at (1.99, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.66, 0.00, 0.11) m, moving 0.66 m/s (vx +0.51, vy +0.00, vz -0.42), turned 95° from how it started; touching floor | pusher at (2.80, 0.00, 0.09) m, at rest; touching block2, floor
1.75 s: block1 at (3.19, 0.00, 0.10) m, at rest; touching floor | block2 at (2.99, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (2.36, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.99, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.67, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (2.80, 0.00, 0.09) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (3.19, 0.00, 0.10) m, at rest; touching floor
- block2 at (2.99, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- block3 at (2.36, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- block4 at (1.99, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- block5 at (1.67, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- pusher at (2.80, 0.00, 0.09) m, at rest; touching floor
</history>
