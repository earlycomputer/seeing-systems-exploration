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
- pusher: slide joint pusher_slide about axis (1.00, 0.00, 0.00), range 0 m to 1.25 m as MuJoCo applies it; its geoms: pusher; starts at 0.000 m, moving +0.80 m/s

What happened, in order:
 0.00 s  block1 starts touching floor
 0.00 s  block1 starts touching block2
 0.00 s  block2 starts touching block3
 0.00 s  block3 starts touching block4
 0.00 s  pusher starts at its lower stop (0 m)
 0.01 s  block5 starts moving
 0.01 s  block4 first touches block5
 1.00 s  block2 passes 0.01 m from pusher without touching it: nearest points (-0.06, 0.00, 0.20) m and (-0.06, 0.00, 0.18) m
 1.00 s  block1 first touches pusher
 1.00 s  block1 starts moving
 1.00 s  block2 starts moving
 1.00 s  block3 starts moving
 1.01 s  block4 starts moving
 1.90 s  block1 leaves block2
 1.91 s  block1 leaves pusher
 1.94 s  block4 leaves block5
 1.94 s  block3 leaves block4
 1.94 s  block2 leaves block3
 1.99 s  block2 first touches floor
 1.99 s  block2 touches block3 again
 1.99 s  block3 touches block4 again
 1.99 s  block4 touches block5 again
 2.00 s  block1 comes to rest at (0.23, 0.00, 0.06) m
 2.00 s  block4 passes 0.33 m from pusher without touching it: nearest points (0.50, 0.00, 0.40) m and (0.24, 0.00, 0.18) m
 2.06 s  block4 leaves block5
 2.18 s  pusher reaches its upper stop (1.25 m) moving +0.80 m/s
 2.19 s  block3 passes 0.19 m from pusher without touching it: nearest points (0.58, 0.00, 0.22) m and (0.39, 0.00, 0.18) m
 2.21 s  pusher is at its largest, 1.3 m
 2.22 s  pusher reaches its upper stop (1.25 m) again moving -0.05 m/s
 2.22 s  block4 touches block5 again
 2.24 s  block3 leaves block4
 2.25 s  block2 leaves block3
 2.25 s  block4 leaves block5
 2.33 s  block3 first touches floor
 2.35 s  block4 first touches floor
 2.37 s  block5 first touches floor
 2.40 s  block2 comes to rest at (0.62, 0.00, 0.06) m
 2.44 s  block3 comes to rest at (0.84, 0.00, 0.06) m
 2.47 s  block4 comes to rest at (1.10, 0.00, 0.06) m
 2.49 s  block5 comes to rest at (1.36, 0.00, 0.06) m

State every 0.25 s:
0.00 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3 | block5 at (0.00, 0.00, 0.90) m, at rest; touching nothing | pusher at 0.000 m, moving +0.80 m/s; touching nothing
0.25 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4 | pusher at 0.200 m, moving +0.80 m/s; touching nothing
0.50 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4 | pusher at 0.400 m, moving +0.80 m/s; touching nothing
0.75 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4 | pusher at 0.600 m, moving +0.80 m/s; touching nothing
1.00 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4 | pusher at 0.800 m, moving +0.80 m/s; touching nothing
1.25 s: block1 at (0.05, 0.00, 0.11) m, moving 0.19 m/s (vx +0.19, vy -0.00, vz +0.03), turned 10° from how it started; touching block2, floor, pusher | block2 at (0.06, 0.00, 0.32) m, moving 0.27 m/s (vx +0.27, vy -0.00, vz +0.06), turned 3° from how it started; touching block1, block3 | block3 at (0.05, 0.00, 0.52) m, moving 0.27 m/s (vx +0.27, vy -0.00, vz +0.06), turned 3° from how it started; touching block2, block4 | block4 at (0.04, 0.00, 0.72) m, moving 0.28 m/s (vx +0.27, vy -0.00, vz +0.06), turned 3° from how it started; touching block3, block5 | block5 at (0.03, 0.00, 0.92) m, moving 0.28 m/s (vx +0.27, vy -0.00, vz +0.06), turned 3° from how it started; touching block4 | pusher at 0.856 m, moving +0.19 m/s; touching block1
1.50 s: block1 at (0.10, 0.00, 0.11) m, moving 0.20 m/s (vx +0.20, vy +0.00, vz +0.01), turned 23° from how it started; touching block2, floor, pusher | block2 at (0.14, 0.00, 0.33) m, moving 0.37 m/s (vx +0.37, vy +0.00, vz +0.01); touching block1, block3 | block3 at (0.14, 0.00, 0.53) m, moving 0.43 m/s (vx +0.43, vy +0.00, vz +0.01); touching block2, block4 | block4 at (0.14, 0.00, 0.73) m, moving 0.50 m/s (vx +0.50, vy +0.00, vz +0.01); touching block3, block5 | block5 at (0.13, 0.00, 0.93) m, moving 0.57 m/s (vx +0.57, vy +0.00, vz +0.01); touching block4 | pusher at 0.902 m, moving +0.18 m/s; touching block1
1.75 s: block1 at (0.16, 0.00, 0.11) m, moving 0.31 m/s (vx +0.30, vy +0.00, vz -0.07), turned 46° from how it started; touching block2, floor, pusher | block2 at (0.26, 0.00, 0.31) m, moving 0.65 m/s (vx +0.62, vy +0.00, vz -0.19), turned 8° from how it started; touching block1, block3 | block3 at (0.28, 0.00, 0.51) m, moving 0.79 m/s (vx +0.76, vy +0.00, vz -0.21), turned 8° from how it started; touching block2, block4 | block4 at (0.31, 0.00, 0.71) m, moving 0.94 m/s (vx +0.91, vy +0.00, vz -0.23), turned 8° from how it started; touching block3, block5 | block5 at (0.33, 0.00, 0.91) m, moving 1.09 m/s (vx +1.06, vy +0.00, vz -0.25), turned 8° from how it started; touching block4 | pusher at 0.953 m, moving +0.27 m/s; touching block1
2.00 s: block1 at (0.23, 0.00, 0.06) m, at rest, turned 91° from how it started; touching floor | block2 at (0.48, 0.00, 0.10) m, moving 0.46 m/s (vx +0.42, vy +0.00, vz -0.20), turned 15° from how it started; touching block3, floor | block3 at (0.53, 0.00, 0.29) m, moving 0.99 m/s (vx +0.88, vy +0.00, vz -0.44), turned 15° from how it started; touching block2, block4 | block4 at (0.58, 0.00, 0.48) m, moving 1.39 m/s (vx +1.19, vy +0.00, vz -0.71), turned 14° from how it started; touching block3, block5 | block5 at (0.63, 0.00, 0.67) m, moving 1.77 m/s (vx +1.52, vy +0.00, vz -0.90), turned 15° from how it started; touching block4 | pusher at 1.099 m, moving +0.79 m/s; touching nothing
2.25 s: block1 at (0.23, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block2 at (0.57, 0.00, 0.10) m, moving 0.58 m/s (vx +0.50, vy +0.00, vz -0.28), turned 60° from how it started; touching floor | block3 at (0.75, 0.00, 0.20) m, moving 1.50 m/s (vx +0.99, vy +0.00, vz -1.13), turned 60° from how it started; touching nothing | block4 at (0.92, 0.00, 0.31) m, moving 2.28 m/s (vx +1.48, vy +0.00, vz -1.74), turned 58° from how it started; touching block5 | block5 at (1.08, 0.00, 0.43) m, moving 2.87 m/s (vx +1.88, vy +0.00, vz -2.18), turned 53° from how it started; touching block4 | pusher at 1.252 m, moving -0.06 m/s; touching nothing
2.50 s: block1 at (0.23, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block2 at (0.62, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block3 at (0.84, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block4 at (1.10, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block5 at (1.36, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | pusher at 1.251 m, still; touching nothing
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (0.23, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor
- block2 at (0.62, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor
- block3 at (0.84, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor
- block4 at (1.10, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor
- block5 at (1.36, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor
- pusher at 1.251 m, still; touching nothing
</history>
