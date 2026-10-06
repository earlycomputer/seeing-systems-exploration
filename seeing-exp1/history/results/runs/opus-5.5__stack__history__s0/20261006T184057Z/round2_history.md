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
- pusher: slide joint pusher_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.64 m as MuJoCo applies it; its geoms: pusher; starts at 0.000 m, moving +1.50 m/s

What happened, in order:
 0.00 s  block1 starts touching floor
 0.00 s  block1 starts touching block2
 0.00 s  block2 starts touching block3
 0.00 s  block3 starts touching block4
 0.00 s  pusher starts at its lower stop (0 m)
 0.01 s  block5 starts moving
 0.01 s  block4 first touches block5
 0.30 s  block1 leaves floor
 0.30 s  block1 first touches pusher
 0.30 s  block1 starts moving
 0.30 s  block2 starts moving
 0.30 s  block3 starts moving
 0.30 s  block4 starts moving
 0.33 s  block1 touches floor again
 0.36 s  block1 leaves pusher
 0.39 s  block1 touches pusher again
 0.40 s  block1 leaves floor
 0.44 s  block1 touches floor again
 0.47 s  pusher reaches its upper stop (0.64 m) moving +0.82 m/s
 0.48 s  block1 leaves pusher
 0.50 s  pusher is at its largest, 0.6 m
 0.51 s  pusher reaches its upper stop (0.64 m) again moving -0.09 m/s
 0.79 s  block2 first touches pusher
 0.79 s  block1 leaves block2
 0.84 s  block1 touches block2 again
 0.89 s  block1 leaves block2
 0.96 s  block4 leaves block5
 0.98 s  block1 touches block2 again
 0.98 s  block2 leaves block3
 1.02 s  block3 leaves block4
 1.12 s  block3 first touches floor
 1.13 s  block3 touches block4 again
 1.14 s  block4 touches block5 again
 1.17 s  block3 leaves block4
 1.18 s  block4 first touches floor
 1.20 s  block3 leaves floor
 1.20 s  block4 leaves block5
 1.23 s  block3 touches floor again
 1.23 s  block5 first touches floor
 1.65 s  block5 comes to rest at (-1.13, 0.00, 0.10) m
 2.10 s  block1 leaves block2
 2.30 s  block1 touches block2 again
 2.63 s  block1 leaves block2
 2.71 s  block2 leaves pusher
 2.74 s  block2 first touches floor
 2.76 s  block1 touches block2 2 more times between 2.76 s and 2.99 s
 2.85 s  block1 comes to rest at (0.23, 0.00, 0.10) m
 2.98 s  block2 comes to rest at (0.03, 0.00, 0.10) m
 3.07 s  block3 first touches pusher
 3.30 s  block3 touches block4 again
 3.32 s  block4 passes 0.20 m from pusher without touching it: nearest points (-0.58, -0.10, 0.02) m and (-0.38, -0.10, 0.02) m
 3.35 s  block3 comes to rest at (-0.48, 0.00, 0.10) m
 3.36 s  block4 comes to rest at (-0.68, 0.00, 0.10) m
 3.47 s  block3 leaves pusher
 3.76 s  block3 leaves block4

State every 0.25 s:
0.00 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3 | block5 at (0.00, 0.00, 0.90) m, at rest; touching nothing | pusher at 0.000 m, moving +1.50 m/s; touching nothing
0.25 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4 | pusher at 0.375 m, moving +1.50 m/s; touching nothing
0.50 s: block1 at (0.20, 0.00, 0.10) m, moving 0.59 m/s (vx +0.54, vy +0.00, vz -0.24); touching block2 | block2 at (0.04, 0.00, 0.29) m, moving 0.50 m/s (vx +0.47, vy -0.00, vz -0.17), turned 7° from how it started; touching block1, block3 | block3 at (0.01, 0.00, 0.49) m, moving 0.21 m/s (vx +0.05, vy -0.00, vz -0.21), turned 7° from how it started; touching block2, block4 | block4 at (0.00, 0.00, 0.69) m, moving 0.22 m/s (vx -0.07, vy +0.00, vz -0.21), turned 7° from how it started; touching block3, block5 | block5 at (0.00, 0.00, 0.89) m, moving 0.18 m/s (vx -0.11, vy -0.00, vz -0.15), turned 7° from how it started; touching block4 | pusher at 0.646 m, moving -0.02 m/s; touching nothing
0.75 s: block1 at (0.21, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.04, 0.00, 0.28) m, moving 0.22 m/s (vx -0.18, vy -0.00, vz -0.12), turned 24° from how it started; touching block1, block3 | block3 at (-0.04, 0.00, 0.46) m, moving 0.49 m/s (vx -0.44, vy -0.00, vz -0.23), turned 24° from how it started; touching block2, block4 | block4 at (-0.09, 0.00, 0.66) m, moving 0.77 m/s (vx -0.71, vy -0.00, vz -0.31), turned 24° from how it started; touching block3, block5 | block5 at (-0.13, 0.00, 0.86) m, moving 1.04 m/s (vx -0.97, vy -0.00, vz -0.37), turned 24° from how it started; touching block4 | pusher at 0.619 m, moving -0.11 m/s; touching nothing
1.00 s: block1 at (0.21, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.03, 0.00, 0.27) m, at rest, turned 27° from how it started; touching block1, pusher | block3 at (-0.24, 0.00, 0.34) m, moving 1.46 m/s (vx -1.01, vy -0.00, vz -1.06), turned 37° from how it started; touching block4 | block4 at (-0.36, 0.00, 0.50) m, moving 1.86 m/s (vx -1.33, vy -0.00, vz -1.30), turned 36° from how it started; touching block3 | block5 at (-0.47, 0.00, 0.67) m, moving 2.16 m/s (vx -1.61, vy -0.00, vz -1.44), turned 36° from how it started; touching nothing | pusher at 0.605 m, still; touching block2
1.25 s: block1 at (0.21, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.03, 0.00, 0.27) m, at rest, turned 26° from how it started; touching block1, pusher | block3 at (-0.42, 0.00, 0.11) m, moving 0.70 m/s (vx -0.54, vy +0.00, vz -0.45), turned 86° from how it started; touching floor | block4 at (-0.68, 0.00, 0.11) m, moving 0.60 m/s (vx -0.39, vy -0.00, vz +0.46), turned 97° from how it started; touching floor | block5 at (-0.96, 0.00, 0.10) m, moving 0.92 m/s (vx -0.83, vy -0.00, vz +0.38), turned 106° from how it started; touching floor | pusher at 0.599 m, moving -0.04 m/s; touching block2
1.50 s: block1 at (0.21, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.02, 0.00, 0.27) m, at rest, turned 24° from how it started; touching block1, pusher | block3 at (-0.43, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.70, 0.00, 0.12) m, moving 0.35 m/s (vx +0.30, vy +0.00, vz -0.18), turned 103° from how it started; touching floor | block5 at (-1.11, 0.00, 0.11) m, moving 0.88 m/s (vx -0.71, vy -0.00, vz -0.52), turned 172° from how it started; touching nothing | pusher at 0.587 m, moving -0.06 m/s; touching block2
1.75 s: block1 at (0.21, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.01, 0.00, 0.27) m, moving 0.07 m/s (vx -0.07, vy -0.00, vz -0.01), turned 21° from how it started; touching block1, pusher | block3 at (-0.43, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.67, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-1.13, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | pusher at 0.569 m, moving -0.08 m/s; touching block2
2.00 s: block1 at (0.21, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (-0.01, 0.00, 0.27) m, moving 0.08 m/s (vx -0.08, vy -0.00, vz -0.01), turned 18° from how it started; touching block1, pusher | block3 at (-0.43, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.67, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-1.13, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | pusher at 0.545 m, moving -0.10 m/s; touching block2
2.25 s: block1 at (0.21, 0.00, 0.10) m, at rest; touching floor | block2 at (-0.01, 0.00, 0.24) m, moving 0.31 m/s (vx +0.30, vy +0.00, vz -0.09), turned 6° from how it started; touching pusher | block3 at (-0.43, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.67, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-1.13, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | pusher at 0.515 m, moving -0.15 m/s; touching block2
2.50 s: block1 at (0.22, 0.00, 0.10) m, at rest; touching floor | block2 at (0.00, 0.00, 0.21) m, moving 0.17 m/s (vx -0.15, vy -0.00, vz -0.09), turned 40° from how it started; touching pusher | block3 at (-0.43, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.67, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-1.13, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | pusher at 0.469 m, moving -0.22 m/s; touching block2
2.75 s: block1 at (0.22, 0.00, 0.10) m, at rest; touching floor | block2 at (-0.02, 0.00, 0.13) m, moving 0.44 m/s (vx +0.24, vy +0.00, vz -0.37), turned 59° from how it started; touching floor | block3 at (-0.43, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.67, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-1.13, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | pusher at 0.405 m, moving -0.28 m/s; touching nothing
3.00 s: block1 at (0.23, 0.00, 0.10) m, at rest; touching floor | block2 at (0.03, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.43, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.67, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-1.13, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | pusher at 0.336 m, moving -0.28 m/s; touching nothing
3.25 s: block1 at (0.23, 0.00, 0.10) m, at rest; touching floor | block2 at (0.03, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.47, 0.00, 0.10) m, moving 0.17 m/s (vx -0.16, vy +0.00, vz -0.06), turned 90° from how it started; touching pusher | block4 at (-0.67, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-1.13, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | pusher at 0.282 m, moving -0.14 m/s; touching block3
3.50 s: block1 at (0.23, 0.00, 0.10) m, at rest; touching floor | block2 at (0.03, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.48, 0.00, 0.10) m, at rest, turned 90° from how it started; touching block4, floor | block4 at (-0.68, 0.00, 0.10) m, at rest, turned 90° from how it started; touching block3, floor | block5 at (-1.13, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | pusher at 0.271 m, still; touching nothing
(the same through 3.75 s)
4.00 s: block1 at (0.23, 0.00, 0.10) m, at rest; touching floor | block2 at (0.03, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.48, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.68, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-1.13, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | pusher at 0.271 m, still; touching nothing
(the same through 4.50 s)
4.75 s: block1 at (0.23, 0.00, 0.10) m, at rest; touching floor | block2 at (0.03, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.48, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.68, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-1.13, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | pusher at 0.272 m, still; touching nothing
(the same through 5.75 s)
6.00 s: block1 at (0.23, 0.00, 0.10) m, at rest; touching floor | block2 at (0.03, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.48, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.68, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-1.13, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | pusher at 0.273 m, still; touching nothing

At the end (6.00 s):
- block1 at (0.23, 0.00, 0.10) m, at rest; touching floor
- block2 at (0.03, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- block3 at (-0.48, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- block4 at (-0.68, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- block5 at (-1.13, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor
- pusher at 0.273 m, still; touching nothing
</history>
