Your expectations, checked against the run (2 of 2 hold):

- holds: pusher touches block1 (first touch at 0.63 s)
- holds: block5 touches floor (first touch at 1.47 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1; starts at (0.00, 0.00, 0.11) m, at rest
- block2: free body; its geoms: block2; starts at (0.00, 0.00, 0.33) m, at rest
- block3: free body; its geoms: block3; starts at (0.00, 0.00, 0.55) m, at rest
- block4: free body; its geoms: block4; starts at (0.00, 0.00, 0.77) m, at rest
- block5: free body; its geoms: block5; starts at (0.00, 0.00, 0.99) m, at rest
- pusher: free body; its geoms: pusher; starts at (-1.00, 0.00, 0.06) m, moving 1.50 m/s (vx +1.50, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  block1 starts touching floor
 0.00 s  block4 starts touching block5
 0.00 s  block3 starts touching block4
 0.00 s  pusher starts touching floor
 0.01 s  block1 first touches block2
 0.01 s  block3 starts moving
 0.01 s  block4 starts moving
 0.01 s  block5 starts moving
 0.01 s  block2 first touches block3
 0.63 s  block1 first touches pusher
 0.63 s  block1 starts moving
 0.63 s  block2 starts moving
 0.67 s  block1 leaves floor
 0.68 s  block1 leaves pusher
 0.70 s  block1 touches floor again
 0.72 s  block1 touches pusher again
 0.73 s  block1 leaves floor
 0.76 s  block1 touches floor again
 0.86 s  block2 passes 0.10 m from pusher without touching it: nearest points (0.08, -0.12, 0.22) m and (0.08, -0.12, 0.12) m
 0.94 s  pusher comes to rest at (0.00, 0.00, 0.06) m
 0.98 s  block1 leaves pusher
 1.21 s  block4 leaves block5
 1.25 s  block3 leaves block4
 1.28 s  block2 leaves block3
 1.37 s  block2 touches block3 again
 1.37 s  block2 leaves block3
 1.40 s  block1 touches pusher again
 1.40 s  block1 passes 0.28 m from block4 without touching it: nearest points (0.10, 0.12, 0.22) m and (-0.17, 0.12, 0.29) m
 1.41 s  block5 passes 0.37 m from pusher without touching it: nearest points (-0.45, 0.12, 0.23) m and (-0.10, 0.12, 0.12) m
 1.46 s  block1 leaves pusher
 1.47 s  block5 first touches floor
 1.47 s  block4 first touches floor
 1.48 s  block3 first touches pusher
 1.48 s  block3 leaves pusher
 1.49 s  block1 comes to rest at (0.16, 0.00, 0.11) m
 1.52 s  block3 touches block4 again
 1.54 s  block3 touches pusher again
 1.55 s  block3 leaves block4
 1.56 s  block5 comes to rest at (-0.62, 0.00, 0.06) m
 1.64 s  block4 passes 0.10 m from pusher without touching it: nearest points (-0.20, 0.12, 0.12) m and (-0.10, 0.12, 0.12) m
 1.66 s  block1 passes 0.07 m from block3 without touching it: nearest points (0.10, 0.12, 0.22) m and (0.03, 0.12, 0.22) m
 1.67 s  block4 comes to rest at (-0.31, 0.00, 0.06) m
 1.68 s  block2 comes to rest at (0.16, 0.00, 0.33) m
 1.93 s  block3 comes to rest at (-0.08, 0.00, 0.18) m

State every 0.25 s:
0.00 s: block1 at (0.00, 0.00, 0.11) m, at rest; touching floor | block2 at (0.00, 0.00, 0.33) m, at rest; touching nothing | block3 at (0.00, 0.00, 0.55) m, at rest; touching block4 | block4 at (0.00, 0.00, 0.77) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.99) m, at rest; touching block4 | pusher at (-1.00, 0.00, 0.06) m, moving 1.50 m/s (vx +1.50, vy +0.00, vz +0.00); touching floor
0.25 s: block1 at (0.00, 0.00, 0.11) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.33) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.55) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.77) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.99) m, at rest; touching block4 | pusher at (-0.64, 0.00, 0.06) m, moving 1.38 m/s (vx +1.38, vy +0.00, vz -0.04); touching nothing
0.50 s: block1 at (0.00, 0.00, 0.11) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.33) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.55) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.77) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.99) m, at rest; touching block4 | pusher at (-0.31, 0.00, 0.06) m, moving 1.26 m/s (vx +1.26, vy +0.00, vz -0.05); touching nothing
0.75 s: block1 at (0.10, 0.00, 0.11) m, moving 0.73 m/s (vx +0.72, vy -0.00, vz -0.11); touching block2 | block2 at (0.08, 0.00, 0.34) m, moving 0.59 m/s (vx +0.59, vy +0.00, vz -0.10), turned 8° from how it started; touching block1, block3 | block3 at (0.05, 0.00, 0.56) m, moving 0.47 m/s (vx +0.44, vy +0.00, vz -0.17), turned 9° from how it started; touching block2, block4 | block4 at (0.01, 0.00, 0.77) m, moving 0.23 m/s (vx +0.22, vy +0.00, vz -0.08), turned 11° from how it started; touching block3, block5 | block5 at (-0.03, 0.00, 1.00) m, moving 0.38 m/s (vx -0.31, vy +0.00, vz -0.22), turned 6° from how it started; touching block4 | pusher at (-0.06, 0.00, 0.06) m, moving 0.63 m/s (vx +0.62, vy +0.00, vz -0.08); touching floor
1.00 s: block1 at (0.17, 0.00, 0.11) m, at rest, turned 2° from how it started; touching block2, floor | block2 at (0.17, 0.00, 0.33) m, at rest, turned 2° from how it started; touching block1, block3 | block3 at (0.11, 0.00, 0.57) m, moving 0.10 m/s (vx -0.10, vy +0.00, vz +0.00), turned 30° from how it started; touching block2, block4 | block4 at (0.00, 0.00, 0.76) m, moving 0.37 m/s (vx -0.35, vy +0.00, vz -0.14), turned 30° from how it started; touching block3, block5 | block5 at (-0.11, 0.00, 0.95) m, moving 0.66 m/s (vx -0.59, vy +0.00, vz -0.28), turned 30° from how it started; touching block4 | pusher at (0.00, 0.00, 0.06) m, at rest; touching floor
1.25 s: block1 at (0.17, 0.00, 0.11) m, at rest, turned 3° from how it started; touching block2, floor | block2 at (0.18, 0.00, 0.33) m, at rest, turned 3° from how it started; touching block1, block3 | block3 at (0.04, 0.00, 0.54) m, moving 0.59 m/s (vx -0.45, vy +0.00, vz -0.39), turned 66° from how it started; touching block2, block4 | block4 at (-0.16, 0.00, 0.63) m, moving 1.54 m/s (vx -0.86, vy +0.00, vz -1.28), turned 66° from how it started; touching block3 | block5 at (-0.36, 0.00, 0.72) m, moving 2.28 m/s (vx -1.24, vy +0.00, vz -1.92), turned 63° from how it started; touching nothing | pusher at (0.00, 0.00, 0.06) m, at rest; touching floor
1.50 s: block1 at (0.16, 0.00, 0.11) m, at rest; touching block2, floor | block2 at (0.16, 0.00, 0.33) m, moving 0.11 m/s (vx +0.11, vy -0.00, vz +0.02); touching block1 | block3 at (-0.10, 0.00, 0.21) m, moving 1.17 m/s (vx -0.93, vy +0.00, vz -0.71), turned 133° from how it started; touching nothing | block4 at (-0.34, 0.00, 0.08) m, moving 0.79 m/s (vx +0.76, vy -0.00, vz -0.20), turned 111° from how it started; touching floor | block5 at (-0.62, 0.00, 0.05) m, moving 0.38 m/s (vx +0.01, vy -0.00, vz +0.38), turned 88° from how it started; touching floor | pusher at (0.00, 0.00, 0.06) m, at rest; touching floor
1.75 s: block1 at (0.16, 0.00, 0.11) m, at rest; touching block2, floor | block2 at (0.16, 0.00, 0.33) m, at rest; touching block1 | block3 at (-0.08, 0.00, 0.18) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.02), turned 93° from how it started; touching pusher | block4 at (-0.31, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.62, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | pusher at (0.00, 0.00, 0.06) m, at rest; touching block3, floor
2.00 s: block1 at (0.16, 0.00, 0.11) m, at rest; touching block2, floor | block2 at (0.16, 0.00, 0.33) m, at rest; touching block1 | block3 at (-0.08, 0.00, 0.18) m, at rest, turned 90° from how it started; touching pusher | block4 at (-0.31, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.62, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | pusher at (0.00, 0.00, 0.06) m, at rest; touching block3, floor
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (0.16, 0.00, 0.11) m, at rest; touching block2, floor
- block2 at (0.16, 0.00, 0.33) m, at rest; touching block1
- block3 at (-0.08, 0.00, 0.18) m, at rest, turned 90° from how it started; touching pusher
- block4 at (-0.31, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor
- block5 at (-0.62, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor
- pusher at (0.00, 0.00, 0.06) m, at rest; touching block3, floor
</history>
