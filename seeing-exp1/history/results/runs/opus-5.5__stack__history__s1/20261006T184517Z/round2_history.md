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
- pusher: free body; its geoms: pusher; starts at (-1.20, 0.00, 0.10) m, moving 4.00 m/s (vx +4.00, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  block1 starts touching floor
 0.00 s  block1 starts touching block2
 0.00 s  block3 starts touching block4
 0.00 s  pusher starts touching floor
 0.00 s  block2 starts touching block3
 0.00 s  pusher leaves floor
 0.01 s  block5 starts moving
 0.01 s  block4 first touches block5
 0.04 s  pusher touches floor again
 0.05 s  pusher leaves floor
 0.08 s  pusher touches floor again
 0.31 s  pusher leaves floor
 0.31 s  block1 first touches pusher
 0.31 s  block1 starts moving
 0.31 s  block2 starts moving
 0.31 s  block3 starts moving
 0.31 s  block4 starts moving
 0.35 s  block1 leaves pusher
 0.35 s  block2 first touches pusher
 0.38 s  block3 leaves block4
 0.38 s  block4 leaves block5
 0.38 s  block2 leaves pusher
 0.38 s  block2 leaves block3
 0.40 s  block5 is at the top of its flight, at (-0.02, 0.00, 0.91) m
 0.40 s  block4 is at the top of its flight, at (0.00, 0.00, 0.72) m
 0.40 s  pusher touches floor again
 0.42 s  block1 leaves block2
 0.45 s  block1 touches block2 again
 0.46 s  block1 leaves floor
 0.48 s  block2 touches block3 again
 0.53 s  block1 leaves block2
 0.53 s  block2 leaves block3
 0.56 s  block1 touches floor again
 0.57 s  block1 touches block2 again
 0.60 s  block2 touches pusher again
 0.60 s  block3 first touches pusher
 0.61 s  block2 leaves pusher
 0.62 s  block3 leaves pusher
 0.62 s  block1 leaves floor
 0.64 s  block1 leaves block2
 0.65 s  block1 touches pusher again
 0.66 s  block1 leaves pusher
 0.67 s  block4 passes 0.33 m from pusher without touching it: nearest points (0.15, 0.00, 0.36) m and (0.41, 0.00, 0.16) m
 0.71 s  block1 touches floor again
 0.71 s  block3 first touches floor
 0.73 s  block1 leaves floor
 0.74 s  block2 is at the top of its flight, at (0.63, 0.00, 0.37) m
 0.75 s  block4 first touches floor
 0.75 s  block1 touches pusher again
 0.77 s  block1 leaves pusher
 0.78 s  block4 touches block5 again
 0.78 s  block1 touches floor again
 0.78 s  block1 leaves floor
 0.80 s  block4 leaves floor
 0.80 s  block1 touches pusher again
 0.81 s  block5 first touches floor
 0.82 s  block1 touches floor 8 more times between 0.82 s and 6.00 s, still touching at the end
 0.83 s  block2 touches pusher again
 0.86 s  block1 leaves pusher
 0.88 s  block1 touches block2 again
 0.90 s  block1 leaves block2
 0.91 s  block1 touches pusher 11 more times between 0.91 s and 2.34 s
 0.93 s  block5 leaves floor
 0.93 s  block3 comes to rest at (0.37, 0.00, 0.10) m
 0.94 s  block2 leaves pusher
 0.96 s  block4 touches floor again
 0.96 s  block4 leaves block5
 0.99 s  block5 touches floor again
 1.02 s  block4 comes to rest at (-0.06, 0.00, 0.10) m
 1.02 s  block2 is at the top of its flight, at (1.06, 0.00, 0.37) m
 1.04 s  block5 comes to rest at (-0.27, 0.00, 0.10) m
 1.12 s  block2 touches pusher again
 1.16 s  block2 leaves pusher
 1.20 s  block1 touches block2 8 more times between 1.20 s and 6.00 s, still touching at the end
 1.55 s  block2 touches pusher 4 more times between 1.55 s and 6.00 s, still touching at the end
 2.23 s  pusher comes to rest at (1.85, 0.00, 0.10) m
 2.25 s  block1 comes to rest at (2.05, 0.00, 0.10) m
 2.48 s  block2 comes to rest at (1.91, 0.00, 0.30) m

State every 0.25 s:
0.00 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3 | block5 at (0.00, 0.00, 0.90) m, at rest; touching nothing | pusher at (-1.20, 0.00, 0.10) m, moving 4.00 m/s (vx +4.00, vy +0.00, vz +0.00); touching floor
0.25 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4 | pusher at (-0.38, 0.00, 0.10) m, moving 2.86 m/s (vx +2.86, vy -0.00, vz +0.00); touching floor
0.50 s: block1 at (0.45, 0.00, 0.12) m, moving 1.89 m/s (vx +1.89, vy +0.00, vz +0.05), turned 2° from how it started; touching block2 | block2 at (0.32, 0.00, 0.32) m, moving 1.43 m/s (vx +1.43, vy +0.00, vz -0.02), turned 47° from how it started; touching block1, block3 | block3 at (0.14, 0.00, 0.43) m, moving 1.21 m/s (vx +0.77, vy -0.00, vz -0.93), turned 53° from how it started; touching block2 | block4 at (0.00, 0.00, 0.67) m, moving 0.97 m/s (vx +0.01, vy +0.00, vz -0.97), turned 22° from how it started; touching nothing | block5 at (-0.07, 0.00, 0.86) m, moving 1.10 m/s (vx -0.44, vy +0.00, vz -1.00), turned 22° from how it started; touching nothing | pusher at (0.18, 0.00, 0.10) m, moving 1.87 m/s (vx +1.87, vy -0.00, vz +0.01); touching floor
0.75 s: block1 at (0.86, 0.00, 0.14) m, moving 1.32 m/s (vx +1.32, vy +0.00, vz +0.02), turned 29° from how it started; touching pusher | block2 at (0.65, 0.00, 0.36) m, moving 1.35 m/s (vx +1.34, vy +0.00, vz -0.13), turned 126° from how it started; touching nothing | block3 at (0.33, 0.00, 0.11) m, moving 0.64 m/s (vx +0.63, vy -0.00, vz +0.11), turned 161° from how it started; touching floor | block4 at (0.01, 0.00, 0.12) m, moving 1.60 m/s (vx -0.26, vy -0.00, vz -1.58), turned 55° from how it started; touching floor | block5 at (-0.18, 0.00, 0.31) m, moving 3.48 m/s (vx -0.44, vy +0.00, vz -3.46), turned 55° from how it started; touching nothing | pusher at (0.62, 0.00, 0.10) m, moving 1.69 m/s (vx +1.69, vy -0.00, vz +0.00); touching block1, floor
1.00 s: block1 at (1.25, 0.00, 0.13) m, moving 1.92 m/s (vx +1.86, vy +0.00, vz -0.49), turned 16° from how it started; touching nothing | block2 at (1.03, 0.00, 0.37) m, moving 1.61 m/s (vx +1.60, vy +0.00, vz +0.22), turned 119° from how it started; touching nothing | block3 at (0.37, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | block4 at (-0.05, 0.00, 0.10) m, moving 0.06 m/s (vx -0.01, vy +0.00, vz +0.06), turned 89° from how it started; touching floor | block5 at (-0.27, 0.00, 0.10) m, moving 0.07 m/s (vx -0.03, vy -0.00, vz -0.06), turned 89° from how it started; touching floor | pusher at (1.00, 0.00, 0.10) m, moving 1.37 m/s (vx +1.37, vy -0.00, vz +0.00); touching floor
1.25 s: block1 at (1.52, 0.00, 0.10) m, moving 1.66 m/s (vx +1.66, vy +0.00, vz -0.13); touching pusher | block2 at (1.43, 0.00, 0.33) m, moving 1.21 m/s (vx +1.14, vy -0.00, vz +0.41), turned 67° from how it started; touching nothing | block3 at (0.37, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | block4 at (-0.06, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (1.32, 0.00, 0.10) m, moving 1.04 m/s (vx +1.03, vy -0.00, vz -0.03); touching block1
1.50 s: block1 at (1.75, 0.00, 0.10) m, moving 0.72 m/s (vx +0.71, vy +0.00, vz +0.13), turned 2° from how it started; touching floor | block2 at (1.65, 0.00, 0.35) m, moving 0.79 m/s (vx +0.68, vy +0.00, vz -0.39), turned 141° from how it started; touching nothing | block3 at (0.37, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | block4 at (-0.06, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (1.55, 0.00, 0.10) m, moving 0.75 m/s (vx +0.75, vy -0.00, vz -0.00); touching floor
1.75 s: block1 at (1.93, 0.00, 0.11) m, moving 0.33 m/s (vx +0.29, vy +0.00, vz +0.16), turned 4° from how it started; touching nothing | block2 at (1.81, 0.00, 0.31) m, moving 1.10 m/s (vx +1.09, vy -0.00, vz -0.14), turned 171° from how it started; touching pusher | block3 at (0.37, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | block4 at (-0.06, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (1.70, 0.00, 0.10) m, moving 0.51 m/s (vx +0.51, vy -0.00, vz -0.00); touching block2, floor
2.00 s: block1 at (2.01, 0.00, 0.10) m, moving 0.37 m/s (vx +0.37, vy -0.00, vz -0.07), turned 3° from how it started; touching block2, pusher | block2 at (1.90, 0.00, 0.33) m, moving 0.17 m/s (vx -0.03, vy -0.00, vz -0.17), turned 163° from how it started; touching block1 | block3 at (0.37, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | block4 at (-0.06, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (1.81, 0.00, 0.10) m, moving 0.31 m/s (vx +0.31, vy -0.00, vz -0.00); touching block1, floor
2.25 s: block1 at (2.05, 0.00, 0.10) m, at rest; touching floor, pusher | block2 at (1.88, 0.00, 0.31) m, moving 0.14 m/s (vx +0.14, vy +0.00, vz -0.03), turned 166° from how it started; touching pusher | block3 at (0.37, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | block4 at (-0.06, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (1.85, 0.00, 0.10) m, at rest; touching block1, block2, floor
2.50 s: block1 at (2.05, 0.00, 0.10) m, at rest; touching floor | block2 at (1.91, 0.00, 0.30) m, at rest, turned 179° from how it started; touching pusher | block3 at (0.37, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | block4 at (-0.06, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (1.85, 0.00, 0.10) m, at rest; touching block2, floor
2.75 s: block1 at (2.05, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (1.91, 0.00, 0.30) m, at rest, turned 180° from how it started; touching block1, pusher | block3 at (0.37, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | block4 at (-0.06, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (1.85, 0.00, 0.10) m, at rest; touching block2, floor
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (2.05, 0.00, 0.10) m, at rest; touching block2, floor
- block2 at (1.91, 0.00, 0.30) m, at rest, turned 180° from how it started; touching block1, pusher
- block3 at (0.37, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor
- block4 at (-0.06, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- block5 at (-0.27, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- pusher at (1.85, 0.00, 0.10) m, at rest; touching block2, floor
</history>
