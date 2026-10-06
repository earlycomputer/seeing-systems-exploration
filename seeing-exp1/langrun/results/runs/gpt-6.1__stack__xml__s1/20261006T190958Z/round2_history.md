MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1_geom; starts at (0.00, 0.00, 0.10) m, at rest
- block2: free body; its geoms: block2_geom; starts at (0.00, 0.00, 0.30) m, at rest
- block3: free body; its geoms: block3_geom; starts at (0.00, 0.00, 0.50) m, at rest
- block4: free body; its geoms: block4_geom; starts at (0.00, 0.00, 0.70) m, at rest
- block5: free body; its geoms: block5_geom; starts at (0.00, 0.00, 0.90) m, at rest
- pusher: slide joint pusher_slide about axis (1.00, 0.00, 0.00), range 0 m to 1.5 m as MuJoCo applies it; its geoms: pusher_geom; starts at 0.000 m, still

What happened, in order:
 0.00 s  block1_geom starts touching floor
 0.00 s  block1_geom starts touching block2_geom
 0.00 s  block2_geom starts touching block3_geom
 0.00 s  block3_geom starts touching block4_geom
 0.00 s  pusher starts at its lower stop (0 m)
 0.00 s  block4_geom first touches block5_geom
 0.01 s  block3 starts moving
 0.01 s  block4 starts moving
 0.01 s  block5 starts moving
 0.78 s  block1_geom first touches pusher_geom
 0.78 s  block1 starts moving
 0.78 s  block2 starts moving
 0.80 s  block1_geom leaves block2_geom
 0.81 s  block2_geom leaves block3_geom
 0.81 s  block3_geom leaves block4_geom
 0.81 s  block4_geom leaves block5_geom
 0.83 s  block1_geom leaves floor
 0.83 s  block1_geom leaves pusher_geom
 0.88 s  block5 is at the top of its flight, at (-0.03, 0.00, 0.94) m
 0.88 s  block3 is at the top of its flight, at (0.07, 0.00, 0.54) m
 0.88 s  block2 is at the top of its flight, at (0.14, 0.00, 0.35) m
 0.88 s  block4 is at the top of its flight, at (0.02, 0.00, 0.75) m
 0.94 s  block1_geom touches floor again
 1.04 s  block2_geom first touches pusher_geom
 1.05 s  pusher reaches its upper stop (1.5 m) moving +1.42 m/s
 1.06 s  block2_geom leaves pusher_geom
 1.06 s  pusher is at its largest, 1.5 m
 1.11 s  block3_geom first touches pusher_geom
 1.15 s  block2_geom first touches floor
 1.18 s  block3_geom touches block4_geom again
 1.18 s  block2_geom leaves floor
 1.20 s  block3_geom leaves block4_geom
 1.20 s  block4 passes 0.11 m from pusher (pusher_geom) without touching it: nearest points (0.16, 0.08, 0.22) m and (0.26, 0.08, 0.20) m
 1.24 s  block2 is at the top of its flight, at (0.74, 0.00, 0.13) m
 1.25 s  block3_geom leaves pusher_geom
 1.26 s  block1_geom first touches block4_geom
 1.26 s  block5 passes 0.31 m from pusher (pusher_geom) without touching it: nearest points (-0.05, 0.08, 0.23) m and (0.26, 0.07, 0.19) m
 1.27 s  block1_geom leaves block4_geom
 1.27 s  block4_geom first touches floor
 1.28 s  block4_geom touches block5_geom again
 1.28 s  block1 passes 0.16 m from block5 (block5_geom) without touching it: nearest points (0.09, 0.09, 0.10) m and (-0.06, 0.09, 0.14) m
 1.29 s  block3 is at the top of its flight, at (0.22, 0.00, 0.31) m
 1.30 s  block4_geom leaves block5_geom
 1.30 s  block4_geom leaves floor
 1.31 s  block5_geom first touches floor
 1.32 s  block2_geom touches floor again
 1.34 s  block2_geom leaves floor
 1.34 s  block5_geom leaves floor
 1.35 s  block4_geom touches floor again
 1.40 s  block5_geom touches floor again
 1.43 s  block2_geom touches floor again
 1.45 s  block1_geom first touches block3_geom
 1.47 s  block1_geom leaves block3_geom
 1.47 s  block4_geom touches block5_geom again
 1.47 s  block4_geom leaves floor
 1.51 s  block1_geom touches block3_geom again
 1.53 s  block1_geom leaves block3_geom
 1.53 s  block4_geom touches floor again
 1.54 s  block1 comes to rest at (0.19, 0.00, 0.05) m
 1.54 s  block3_geom touches block4_geom again
 1.56 s  block4_geom leaves floor
 1.57 s  block3_geom leaves block4_geom
 1.57 s  block4_geom leaves block5_geom
 1.59 s  block4_geom touches floor again
 1.62 s  block3_geom touches block4_geom again
 1.63 s  block1_geom touches block3_geom again
 1.63 s  block2 comes to rest at (1.11, 0.00, 0.05) m
 1.64 s  block4 comes to rest at (-0.12, 0.00, 0.11) m
 1.64 s  block3 comes to rest at (0.04, 0.00, 0.13) m
 1.67 s  block4_geom touches block5_geom again
 1.67 s  block5 comes to rest at (-0.28, 0.00, 0.11) m

State every 0.25 s:
0.00 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3_geom | block5 at (0.00, 0.00, 0.90) m, at rest; touching nothing | pusher at 0.000 m, still; touching nothing
0.25 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4_geom | pusher at 0.329 m, moving +1.49 m/s; touching nothing
0.50 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4_geom | pusher at 0.701 m, moving +1.49 m/s; touching nothing
0.75 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4_geom | pusher at 1.073 m, moving +1.49 m/s; touching nothing
1.00 s: block1 at (0.19, 0.00, 0.05) m, moving 0.27 m/s (vx -0.13, vy +0.00, vz -0.24), turned 91° from how it started; touching floor | block2 at (0.31, 0.00, 0.28) m, moving 1.86 m/s (vx +1.44, vy +0.00, vz -1.19), turned 43° from how it started; touching nothing | block3 at (0.17, 0.00, 0.47) m, moving 1.43 m/s (vx +0.76, vy +0.00, vz -1.21), turned 40° from how it started; touching nothing | block4 at (0.04, 0.00, 0.67) m, moving 1.21 m/s (vx +0.19, vy +0.00, vz -1.19), turned 31° from how it started; touching nothing | block5 at (-0.07, 0.00, 0.87) m, moving 1.26 m/s (vx -0.33, vy +0.00, vz -1.22), turned 33° from how it started; touching nothing | pusher at 1.423 m, moving +1.49 m/s; touching nothing
1.25 s: block1 at (0.19, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block2 at (0.76, 0.00, 0.13) m, moving 1.50 m/s (vx +1.50, vy +0.00, vz -0.10), turned 71° from how it started; touching nothing | block3 at (0.25, 0.00, 0.30) m, moving 0.70 m/s (vx -0.57, vy +0.00, vz +0.40), turned 160° from how it started; touching pusher_geom | block4 at (0.03, 0.00, 0.14) m, moving 2.71 m/s (vx -0.73, vy +0.00, vz -2.61), turned 115° from how it started; touching nothing | block5 at (-0.15, 0.00, 0.26) m, moving 3.69 m/s (vx -0.33, vy +0.00, vz -3.67), turned 71° from how it started; touching nothing | pusher at 1.500 m, still; touching block3_geom
1.50 s: block1 at (0.19, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block2 at (1.03, 0.00, 0.11) m, moving 0.86 m/s (vx +0.83, vy -0.00, vz -0.19), turned 140° from how it started; touching floor | block3 at (0.08, 0.00, 0.16) m, moving 1.41 m/s (vx -1.01, vy +0.00, vz -0.99), turned 90° from how it started; touching nothing | block4 at (-0.11, 0.00, 0.11) m, moving 0.18 m/s (vx -0.18, vy +0.00, vz +0.01), turned 161° from how it started; touching block5_geom | block5 at (-0.28, 0.00, 0.11) m, moving 0.11 m/s (vx -0.11, vy -0.00, vz +0.02), turned 142° from how it started; touching block4_geom, floor | pusher at 1.500 m, still; touching nothing
1.75 s: block1 at (0.19, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block3_geom, floor | block2 at (1.11, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block3 at (0.04, 0.00, 0.13) m, at rest, turned 48° from how it started; touching block1_geom, block4_geom | block4 at (-0.12, 0.00, 0.11) m, at rest, turned 165° from how it started; touching block3_geom, block5_geom, floor | block5 at (-0.28, 0.00, 0.11) m, at rest, turned 144° from how it started; touching block4_geom, floor | pusher at 1.500 m, still; touching nothing
(the same through 2.00 s)
2.25 s: block1 at (0.19, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block3_geom, floor | block2 at (1.11, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block3 at (0.04, 0.00, 0.13) m, at rest, turned 48° from how it started; touching block1_geom, block4_geom | block4 at (-0.12, 0.00, 0.11) m, at rest, turned 166° from how it started; touching block3_geom, block5_geom, floor | block5 at (-0.28, 0.00, 0.11) m, at rest, turned 144° from how it started; touching block4_geom, floor | pusher at 1.500 m, still; touching nothing
(the same through 2.75 s)
3.00 s: block1 at (0.19, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block3_geom, floor | block2 at (1.11, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block3 at (0.04, 0.00, 0.13) m, at rest, turned 47° from how it started; touching block1_geom, block4_geom | block4 at (-0.12, 0.00, 0.11) m, at rest, turned 166° from how it started; touching block3_geom, block5_geom, floor | block5 at (-0.28, 0.00, 0.11) m, at rest, turned 144° from how it started; touching block4_geom, floor | pusher at 1.500 m, still; touching nothing
(the same through 3.75 s)
4.00 s: block1 at (0.19, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block3_geom, floor | block2 at (1.11, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block3 at (0.04, 0.00, 0.13) m, at rest, turned 47° from how it started; touching block1_geom, block4_geom | block4 at (-0.12, 0.00, 0.11) m, at rest, turned 166° from how it started; touching block3_geom, floor | block5 at (-0.28, 0.00, 0.11) m, at rest, turned 143° from how it started; touching floor | pusher at 1.500 m, still; touching nothing
4.25 s: block1 at (0.19, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block3_geom, floor | block2 at (1.11, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block3 at (0.04, 0.00, 0.13) m, at rest, turned 47° from how it started; touching block1_geom, block4_geom | block4 at (-0.12, 0.00, 0.11) m, at rest, turned 166° from how it started; touching block3_geom, block5_geom, floor | block5 at (-0.28, 0.00, 0.11) m, at rest, turned 143° from how it started; touching block4_geom, floor | pusher at 1.500 m, still; touching nothing
4.50 s: block1 at (0.19, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block3_geom, floor | block2 at (1.11, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block3 at (0.04, 0.00, 0.13) m, at rest, turned 47° from how it started; touching block1_geom, block4_geom | block4 at (-0.12, 0.00, 0.11) m, at rest, turned 167° from how it started; touching block3_geom, block5_geom, floor | block5 at (-0.28, 0.00, 0.11) m, at rest, turned 143° from how it started; touching block4_geom, floor | pusher at 1.500 m, still; touching nothing
(the same through 5.25 s)
5.50 s: block1 at (0.19, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block3_geom, floor | block2 at (1.11, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block3 at (0.04, 0.00, 0.13) m, at rest, turned 46° from how it started; touching block1_geom, block4_geom | block4 at (-0.12, 0.00, 0.11) m, at rest, turned 167° from how it started; touching block3_geom, block5_geom, floor | block5 at (-0.28, 0.00, 0.11) m, at rest, turned 143° from how it started; touching block4_geom, floor | pusher at 1.500 m, still; touching nothing
(the same through 5.75 s)
6.00 s: block1 at (0.19, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block3_geom, floor | block2 at (1.11, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block3 at (0.04, 0.00, 0.13) m, at rest, turned 46° from how it started; touching block1_geom, block4_geom | block4 at (-0.12, 0.00, 0.11) m, at rest, turned 167° from how it started; touching block3_geom, block5_geom, floor | block5 at (-0.28, 0.00, 0.11) m, at rest, turned 142° from how it started; touching block4_geom, floor | pusher at 1.500 m, still; touching nothing

At the end (6.00 s):
- block1 at (0.19, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block3_geom, floor
- block2 at (1.11, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- block3 at (0.04, 0.00, 0.13) m, at rest, turned 46° from how it started; touching block1_geom, block4_geom
- block4 at (-0.12, 0.00, 0.11) m, at rest, turned 167° from how it started; touching block3_geom, block5_geom, floor
- block5 at (-0.28, 0.00, 0.11) m, at rest, turned 142° from how it started; touching block4_geom, floor
- pusher at 1.500 m, still; touching nothing
</history>
