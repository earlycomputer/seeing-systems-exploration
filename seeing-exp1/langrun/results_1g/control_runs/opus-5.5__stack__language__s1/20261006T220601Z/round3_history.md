MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1; starts at (1.50, 0.00, 0.06) m, at rest
- block2: free body; its geoms: block2; starts at (1.50, 0.00, 0.18) m, at rest
- block3: free body; its geoms: block3; starts at (1.50, 0.00, 0.30) m, at rest
- block4: free body; its geoms: block4; starts at (1.50, 0.00, 0.42) m, at rest
- block5: free body; its geoms: block5; starts at (1.50, 0.00, 0.54) m, at rest
- pusher: free body; its geoms: pusher; starts at (0.20, 0.00, 0.05) m, moving 2.50 m/s (vx +2.50, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  block1 starts touching floor
 0.00 s  block1 starts touching block2
 0.00 s  block3 starts touching block4
 0.00 s  pusher starts touching floor
 0.00 s  block2 starts touching block3
 0.01 s  block3 starts moving
 0.01 s  block4 starts moving
 0.01 s  block5 starts moving
 0.01 s  block4 first touches block5
 0.49 s  block1 leaves block2
 0.49 s  pusher leaves floor
 0.49 s  block1 first touches pusher
 0.49 s  block1 starts moving
 0.49 s  block2 starts moving
 0.51 s  block2 leaves block3
 0.52 s  block1 leaves pusher
 0.53 s  block4 leaves block5
 0.53 s  block3 leaves block4
 0.54 s  block1 leaves floor
 0.56 s  block1 touches pusher again
 0.57 s  block2 first touches pusher
 0.57 s  block2 touches block3 again
 0.57 s  block3 touches block4 again
 0.57 s  block1 leaves pusher
 0.57 s  block2 leaves pusher
 0.57 s  block4 touches block5 again
 0.60 s  pusher touches floor again
 0.61 s  block2 leaves block3
 0.61 s  block1 touches floor again
 0.62 s  block2 touches pusher again
 0.62 s  block2 leaves pusher
 0.63 s  block1 leaves floor
 0.64 s  block4 leaves block5
 0.64 s  block3 passes 0.12 m from pusher without touching it: nearest points (1.56, 0.00, 0.18) m and (1.63, 0.00, 0.09) m
 0.64 s  block3 leaves block4
 0.66 s  block1 touches pusher again
 0.67 s  block2 first touches floor
 0.67 s  block1 touches floor again
 0.68 s  block1 leaves floor
 0.68 s  block1 leaves pusher
 0.70 s  block2 touches block3 again
 0.70 s  block3 touches block4 again
 0.70 s  block4 passes 0.20 m from pusher without touching it: nearest points (1.55, 0.00, 0.21) m and (1.71, 0.00, 0.08) m
 0.71 s  block4 touches block5 again
 0.71 s  block5 passes 0.30 m from pusher without touching it: nearest points (1.54, 0.00, 0.32) m and (1.73, 0.00, 0.09) m
 0.72 s  block1 touches pusher again
 0.73 s  block1 touches floor again
 0.74 s  block1 leaves pusher
 0.78 s  pusher leaves floor
 0.78 s  block1 touches pusher 4 more times between 0.78 s and 1.63 s
 0.78 s  block1 leaves floor
 0.81 s  pusher touches floor again
 0.83 s  block2 comes to rest at (1.56, 0.00, 0.04) m
 0.84 s  block3 comes to rest at (1.52, 0.00, 0.14) m
 0.90 s  block1 is at the top of its flight, at (2.06, 0.00, 0.10) m
 0.99 s  block1 touches floor 2 more times between 0.99 s and 6.00 s, still touching at the end
 1.06 s  block4 comes to rest at (1.53, 0.00, 0.26) m
 1.10 s  block5 comes to rest at (1.53, 0.00, 0.38) m
 1.51 s  pusher comes to rest at (2.29, 0.00, 0.05) m
 1.52 s  block1 comes to rest at (2.40, 0.00, 0.04) m

State every 0.25 s:
0.00 s: block1 at (1.50, 0.00, 0.06) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.18) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.30) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.42) m, at rest; touching block3 | block5 at (1.50, 0.00, 0.54) m, at rest; touching nothing | pusher at (0.20, 0.00, 0.05) m, moving 2.50 m/s (vx +2.50, vy +0.00, vz +0.00); touching floor
0.25 s: block1 at (1.50, 0.00, 0.06) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.18) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.30) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.42) m, at rest; touching block3, block5 | block5 at (1.50, 0.00, 0.54) m, at rest; touching block4 | pusher at (0.82, 0.00, 0.05) m, moving 2.50 m/s (vx +2.50, vy -0.00, vz -0.00); touching floor
0.50 s: block1 at (1.52, 0.00, 0.06) m, moving 2.10 m/s (vx +2.09, vy -0.00, vz +0.21); touching pusher | block2 at (1.50, 0.00, 0.18) m, moving 0.17 m/s (vx +0.13, vy -0.00, vz +0.12); touching block3 | block3 at (1.50, 0.00, 0.30) m, moving 0.14 m/s (vx +0.08, vy +0.00, vz +0.12); touching block2, block4 | block4 at (1.50, 0.00, 0.42) m, moving 0.12 m/s (vx +0.04, vy +0.00, vz +0.12); touching block3, block5 | block5 at (1.50, 0.00, 0.54) m, moving 0.12 m/s (vx +0.00, vy +0.00, vz +0.12); touching block4 | pusher at (1.44, 0.00, 0.05) m, moving 1.78 m/s (vx +1.74, vy +0.00, vz +0.38); touching block1
0.75 s: block1 at (1.90, 0.00, 0.06) m, moving 1.62 m/s (vx +1.61, vy -0.00, vz -0.18), turned 5° from how it started; touching floor | block2 at (1.55, 0.00, 0.04) m, moving 0.15 m/s (vx +0.05, vy +0.00, vz +0.14), turned 97° from how it started; touching block3, floor | block3 at (1.51, 0.00, 0.13) m, moving 0.23 m/s (vx +0.08, vy +0.00, vz +0.22), turned 5° from how it started; touching block2, block4 | block4 at (1.51, 0.00, 0.25) m, moving 0.26 m/s (vx +0.06, vy +0.00, vz +0.25), turned 4° from how it started; touching block3, block5 | block5 at (1.49, 0.00, 0.37) m, moving 0.28 m/s (vx -0.03, vy +0.00, vz +0.28), turned 2° from how it started; touching block4 | pusher at (1.80, 0.00, 0.05) m, moving 1.10 m/s (vx +1.10, vy +0.00, vz -0.01); touching floor
1.00 s: block1 at (2.21, 0.00, 0.06) m, moving 1.32 m/s (vx +1.21, vy +0.00, vz -0.52), turned 120° from how it started; touching floor | block2 at (1.56, 0.00, 0.04) m, at rest, turned 90° from how it started; touching block3, floor | block3 at (1.53, 0.00, 0.14) m, at rest, turned 1° from how it started; touching block2, block4 | block4 at (1.52, 0.00, 0.26) m, moving 0.13 m/s (vx +0.13, vy +0.00, vz -0.03), turned 1° from how it started; touching block3, block5 | block5 at (1.51, 0.00, 0.38) m, moving 0.21 m/s (vx +0.20, vy -0.00, vz -0.02), turned 1° from how it started; touching block4 | pusher at (2.03, 0.00, 0.05) m, moving 0.83 m/s (vx +0.83, vy +0.00, vz +0.00); touching floor
1.25 s: block1 at (2.34, 0.00, 0.04) m, moving 0.79 m/s (vx +0.73, vy -0.00, vz -0.31), turned 92° from how it started; touching nothing | block2 at (1.56, 0.00, 0.04) m, at rest, turned 90° from how it started; touching block3, floor | block3 at (1.53, 0.00, 0.14) m, at rest; touching block2, block4 | block4 at (1.53, 0.00, 0.26) m, at rest; touching block3, block5 | block5 at (1.53, 0.00, 0.38) m, at rest; touching block4 | pusher at (2.21, 0.00, 0.05) m, moving 0.56 m/s (vx +0.56, vy +0.00, vz +0.00); touching floor
1.50 s: block1 at (2.40, 0.00, 0.04) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.01), turned 90° from how it started; touching floor, pusher | block2 at (1.56, 0.00, 0.04) m, at rest, turned 90° from how it started; touching block3, floor | block3 at (1.53, 0.00, 0.14) m, at rest; touching block2, block4 | block4 at (1.53, 0.00, 0.26) m, at rest; touching block3, block5 | block5 at (1.53, 0.00, 0.38) m, at rest; touching block4 | pusher at (2.29, 0.00, 0.05) m, moving 0.07 m/s (vx +0.07, vy +0.00, vz +0.00); touching block1, floor
1.75 s: block1 at (2.40, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block2 at (1.56, 0.00, 0.04) m, at rest, turned 90° from how it started; touching block3, floor | block3 at (1.53, 0.00, 0.14) m, at rest; touching block2, block4 | block4 at (1.53, 0.00, 0.26) m, at rest; touching block3, block5 | block5 at (1.53, 0.00, 0.38) m, at rest; touching block4 | pusher at (2.29, 0.00, 0.05) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (2.40, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor
- block2 at (1.56, 0.00, 0.04) m, at rest, turned 90° from how it started; touching block3, floor
- block3 at (1.53, 0.00, 0.14) m, at rest; touching block2, block4
- block4 at (1.53, 0.00, 0.26) m, at rest; touching block3, block5
- block5 at (1.53, 0.00, 0.38) m, at rest; touching block4
- pusher at (2.29, 0.00, 0.05) m, at rest; touching floor
</history>
