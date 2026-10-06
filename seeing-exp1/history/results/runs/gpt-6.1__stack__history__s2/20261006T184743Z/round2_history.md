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
- pusher: slide joint pusher_slide about axis (1.00, 0.00, 0.00), range 0 m to 1.7 m as MuJoCo applies it; its geoms: pusher; starts at 0.000 m, still

What happened, in order:
 0.00 s  block1 starts touching floor
 0.00 s  block1 starts touching block2
 0.00 s  block2 starts touching block3
 0.00 s  block3 starts touching block4
 0.00 s  pusher starts at its lower stop (0 m)
 0.01 s  block4 first touches block5
 0.77 s  block1 first touches pusher
 0.77 s  block1 starts moving
 0.77 s  block2 starts moving
 0.77 s  block3 starts moving
 0.77 s  block4 starts moving
 0.77 s  block5 starts moving
 0.77 s  block1 leaves floor
 0.81 s  block1 touches floor again
 0.82 s  block1 leaves floor
 0.82 s  block1 leaves pusher
 0.85 s  block1 touches floor again
 0.86 s  block1 touches pusher again
 0.87 s  block1 leaves floor
 0.89 s  block1 leaves block2
 0.91 s  block4 leaves block5
 0.92 s  block1 touches floor again
 0.93 s  block1 leaves floor
 0.93 s  block1 touches block2 again
 0.96 s  block1 touches floor 5 more times between 0.96 s and 6.00 s, still touching at the end
 0.98 s  block4 touches block5 again
 1.00 s  block1 leaves block2
 1.02 s  block2 leaves block3
 1.02 s  block3 leaves block4
 1.03 s  block2 first touches pusher
 1.04 s  block4 leaves block5
 1.05 s  block1 touches block2 again
 1.05 s  block2 touches block3 again
 1.06 s  block1 leaves block2
 1.07 s  block3 touches block4 again
 1.10 s  block2 leaves block3
 1.11 s  block3 leaves block4
 1.11 s  block4 passes 0.36 m from pusher without touching it: nearest points (0.04, -0.08, 0.40) m and (0.32, -0.08, 0.17) m
 1.20 s  pusher reaches its upper stop (1.7 m) moving +1.42 m/s
 1.21 s  block1 leaves pusher
 1.22 s  pusher is at its largest, 1.7 m
 1.26 s  pusher reaches its upper stop (1.7 m) again moving -0.12 m/s
 1.28 s  block3 first touches floor
 1.29 s  block4 first touches floor
 1.30 s  block2 leaves pusher
 1.31 s  block5 first touches floor
 1.33 s  block2 touches block3 again
 1.33 s  block3 passes 0.11 m from pusher without touching it: nearest points (0.34, -0.08, 0.11) m and (0.45, -0.08, 0.11) m
 1.40 s  block3 comes to rest at (0.24, 0.00, 0.06) m
 1.40 s  block4 comes to rest at (-0.04, 0.00, 0.06) m
 1.43 s  block5 comes to rest at (-0.30, 0.00, 0.06) m
 1.47 s  block2 touches pusher again
 1.48 s  block2 comes to rest at (0.40, 0.00, 0.20) m
 1.60 s  block1 comes to rest at (0.84, 0.00, 0.06) m

State every 0.25 s:
0.00 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3 | block5 at (0.00, 0.00, 0.90) m, at rest; touching nothing | pusher at 0.000 m, still; touching nothing
0.25 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4 | pusher at 0.346 m, moving +1.45 m/s; touching nothing
0.50 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4 | pusher at 0.709 m, moving +1.45 m/s; touching nothing
0.75 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4 | pusher at 1.072 m, moving +1.45 m/s; touching nothing
1.00 s: block1 at (0.32, 0.00, 0.10) m, moving 1.46 m/s (vx +1.46, vy -0.00, vz +0.01); touching pusher | block2 at (0.21, 0.00, 0.29) m, moving 1.06 m/s (vx +1.05, vy +0.00, vz -0.10), turned 30° from how it started; touching block3 | block3 at (0.12, 0.00, 0.47) m, moving 0.60 m/s (vx +0.46, vy +0.00, vz -0.39), turned 30° from how it started; touching block2, block4 | block4 at (0.02, 0.00, 0.64) m, moving 0.69 m/s (vx -0.11, vy +0.00, vz -0.68), turned 31° from how it started; touching block3, block5 | block5 at (-0.08, 0.00, 0.81) m, moving 1.15 m/s (vx -0.69, vy +0.00, vz -0.92), turned 30° from how it started; touching block4 | pusher at 1.410 m, moving +1.42 m/s; touching block1
1.25 s: block1 at (0.67, 0.00, 0.10) m, moving 0.94 m/s (vx +0.93, vy +0.00, vz +0.17); touching floor | block2 at (0.41, 0.00, 0.22) m, moving 0.30 m/s (vx -0.04, vy -0.00, vz -0.30), turned 109° from how it started; touching nothing | block3 at (0.21, 0.00, 0.16) m, moving 2.37 m/s (vx +0.35, vy -0.00, vz -2.35), turned 91° from how it started; touching nothing | block4 at (-0.04, 0.00, 0.19) m, moving 3.03 m/s (vx -0.28, vy -0.00, vz -3.02), turned 91° from how it started; touching nothing | block5 at (-0.25, 0.00, 0.28) m, moving 3.44 m/s (vx -0.69, vy +0.00, vz -3.37), turned 79° from how it started; touching nothing | pusher at 1.706 m, moving -0.14 m/s; touching nothing
1.50 s: block1 at (0.83, 0.00, 0.08) m, moving 0.98 m/s (vx +0.67, vy +0.00, vz -0.71), turned 80° from how it started; touching nothing | block2 at (0.40, 0.00, 0.20) m, at rest, turned 139° from how it started; touching block3, pusher | block3 at (0.24, 0.00, 0.06) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (-0.04, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.30, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | pusher at 1.701 m, still; touching block2
1.75 s: block1 at (0.84, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block2 at (0.40, 0.00, 0.20) m, at rest, turned 140° from how it started; touching block3, pusher | block3 at (0.23, 0.00, 0.06) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (-0.04, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.30, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | pusher at 1.701 m, still; touching block2
(the same through 4.00 s)
4.25 s: block1 at (0.84, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block2 at (0.40, 0.00, 0.20) m, at rest, turned 141° from how it started; touching block3, pusher | block3 at (0.23, 0.00, 0.06) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (-0.04, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.30, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | pusher at 1.701 m, still; touching block2
(the same through 4.75 s)
5.00 s: block1 at (0.84, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block2 at (0.39, 0.00, 0.20) m, at rest, turned 141° from how it started; touching block3, pusher | block3 at (0.23, 0.00, 0.06) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (-0.04, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.30, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | pusher at 1.701 m, still; touching block2
(the same through 5.75 s)
6.00 s: block1 at (0.84, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block2 at (0.39, 0.00, 0.19) m, at rest, turned 141° from how it started; touching block3, pusher | block3 at (0.23, 0.00, 0.06) m, at rest, turned 90° from how it started; touching block2, floor | block4 at (-0.04, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.30, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | pusher at 1.701 m, still; touching block2

At the end (6.00 s):
- block1 at (0.84, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor
- block2 at (0.39, 0.00, 0.19) m, at rest, turned 141° from how it started; touching block3, pusher
- block3 at (0.23, 0.00, 0.06) m, at rest, turned 90° from how it started; touching block2, floor
- block4 at (-0.04, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor
- block5 at (-0.30, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor
- pusher at 1.701 m, still; touching block2
</history>
