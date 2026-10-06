MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1_geom; starts at (0.00, 0.00, 0.05) m, at rest
- block2: free body; its geoms: block2_geom; starts at (0.00, 0.00, 0.15) m, at rest
- block3: free body; its geoms: block3_geom; starts at (0.00, 0.00, 0.25) m, at rest
- block4: free body; its geoms: block4_geom; starts at (0.00, 0.00, 0.35) m, at rest
- block5: free body; its geoms: block5_geom; starts at (0.00, 0.00, 0.45) m, at rest
- pusher: slide joint pusher_slide about axis (1.00, 0.00, 0.00), no range limit; its geoms: pusher_geom; starts at 0.000 m, moving +0.60 m/s

What happened, in order:
 0.00 s  block1_geom starts touching floor
 0.00 s  block1_geom starts touching block2_geom
 0.00 s  block2_geom starts touching block3_geom
 0.00 s  block3_geom starts touching block4_geom
 0.01 s  block3 starts moving
 0.01 s  block4 starts moving
 0.01 s  block5 starts moving
 0.01 s  block4_geom first touches block5_geom
 1.00 s  block1_geom first touches pusher_geom
 1.00 s  block1 starts moving
 1.00 s  block2 starts moving
 1.05 s  block1_geom leaves pusher_geom
 1.08 s  block1_geom touches pusher_geom again
 1.29 s  block1_geom leaves pusher_geom
 1.32 s  block1_geom touches pusher_geom again
 1.34 s  block1_geom leaves pusher_geom
 1.38 s  block1_geom touches pusher_geom again
 1.40 s  block1_geom leaves pusher_geom
 1.43 s  block1_geom touches pusher_geom 4 more times between 1.43 s and 2.55 s
 1.62 s  block1_geom leaves block2_geom
 1.63 s  block2_geom first touches pusher_geom
 1.68 s  block3_geom leaves block4_geom
 1.69 s  block4_geom leaves block5_geom
 1.71 s  block5 passes 0.23 m from pusher (pusher_geom) without touching it: nearest points (-0.14, 0.00, 0.20) m and (0.06, 0.00, 0.08) m
 1.73 s  block2_geom leaves block3_geom
 1.73 s  block4 passes 0.13 m from pusher (pusher_geom) without touching it: nearest points (-0.06, 0.00, 0.14) m and (0.06, 0.00, 0.08) m
 1.75 s  block3 passes 0.02 m from pusher (pusher_geom) without touching it: nearest points (0.04, 0.00, 0.09) m and (0.06, 0.00, 0.08) m
 1.82 s  block3_geom first touches floor
 1.82 s  block4_geom first touches floor
 1.82 s  block5_geom first touches floor
 1.90 s  block3 comes to rest at (-0.02, 0.00, 0.05) m
 1.91 s  block4 comes to rest at (-0.15, 0.00, 0.05) m
 1.92 s  block5 comes to rest at (-0.28, 0.00, 0.05) m
 2.15 s  block2 comes to rest at (0.13, 0.00, 0.13) m
 2.19 s  block1 comes to rest at (0.25, 0.00, 0.05) m
 2.49 s  pusher is at its largest, 0.9 m

State every 0.25 s:
0.00 s: block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching nothing | pusher at 0.000 m, moving +0.60 m/s; touching nothing
0.25 s: block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom | pusher at 0.150 m, moving +0.60 m/s; touching nothing
0.50 s: block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom | pusher at 0.300 m, moving +0.60 m/s; touching nothing
0.75 s: block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom | pusher at 0.450 m, moving +0.60 m/s; touching nothing
1.00 s: block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom | pusher at 0.600 m, moving +0.60 m/s; touching nothing
1.25 s: block1 at (0.11, 0.00, 0.05) m, moving 0.34 m/s (vx +0.29, vy -0.00, vz -0.17); touching block2_geom, floor | block2 at (0.08, 0.00, 0.15) m, moving 0.34 m/s (vx +0.34, vy -0.00, vz -0.02), turned 12° from how it started; touching block1_geom, block3_geom | block3 at (0.06, 0.00, 0.25) m, moving 0.25 m/s (vx +0.24, vy -0.00, vz -0.05), turned 12° from how it started; touching block2_geom, block4_geom | block4 at (0.04, 0.00, 0.35) m, moving 0.18 m/s (vx +0.16, vy -0.00, vz -0.08), turned 12° from how it started; touching block3_geom, block5_geom | block5 at (0.01, 0.00, 0.45) m, moving 0.14 m/s (vx +0.08, vy -0.00, vz -0.12), turned 12° from how it started; touching block4_geom | pusher at 0.711 m, moving +0.35 m/s; touching nothing
1.50 s: block1 at (0.17, 0.00, 0.05) m, moving 0.24 m/s (vx +0.22, vy -0.00, vz +0.11); touching block2_geom, floor, pusher_geom | block2 at (0.13, 0.00, 0.16) m, moving 0.09 m/s (vx +0.06, vy -0.00, vz +0.06), turned 26° from how it started; touching block1_geom, block3_geom | block3 at (0.08, 0.00, 0.25) m, moving 0.09 m/s (vx -0.09, vy -0.00, vz -0.02), turned 26° from how it started; touching block2_geom, block4_geom | block4 at (0.04, 0.00, 0.34) m, moving 0.26 m/s (vx -0.24, vy -0.00, vz -0.09), turned 26° from how it started; touching block3_geom, block5_geom | block5 at (-0.01, 0.00, 0.43) m, moving 0.43 m/s (vx -0.40, vy -0.00, vz -0.16), turned 26° from how it started; touching block4_geom | pusher at 0.775 m, moving +0.18 m/s; touching block1_geom
1.75 s: block1 at (0.21, 0.00, 0.05) m, moving 0.12 m/s (vx +0.12, vy +0.00, vz +0.03); touching floor, pusher_geom | block2 at (0.11, 0.00, 0.14) m, moving 0.41 m/s (vx -0.29, vy -0.00, vz -0.28), turned 78° from how it started; touching nothing | block3 at (0.00, 0.00, 0.15) m, moving 1.17 m/s (vx -0.48, vy -0.00, vz -1.07), turned 77° from how it started; touching nothing | block4 at (-0.10, 0.00, 0.18) m, moving 1.68 m/s (vx -0.73, vy -0.00, vz -1.52), turned 74° from how it started; touching nothing | block5 at (-0.20, 0.00, 0.21) m, moving 2.13 m/s (vx -1.01, vy -0.00, vz -1.88), turned 74° from how it started; touching nothing | pusher at 0.814 m, moving +0.14 m/s; touching block1_geom
2.00 s: block1 at (0.24, 0.00, 0.05) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor | block2 at (0.11, 0.00, 0.13) m, moving 0.26 m/s (vx +0.25, vy +0.00, vz -0.07), turned 97° from how it started; touching pusher_geom | block3 at (-0.02, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.15, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.28, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | pusher at 0.839 m, moving +0.07 m/s; touching block2_geom
2.25 s: block1 at (0.25, 0.00, 0.05) m, at rest; touching floor, pusher_geom | block2 at (0.13, 0.00, 0.13) m, at rest, turned 90° from how it started; touching pusher_geom | block3 at (-0.02, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.15, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.28, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | pusher at 0.852 m, moving +0.03 m/s; touching block1_geom, block2_geom
2.50 s: block1 at (0.25, 0.00, 0.05) m, at rest; touching floor, pusher_geom | block2 at (0.13, 0.00, 0.13) m, at rest, turned 90° from how it started; touching pusher_geom | block3 at (-0.02, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.15, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.28, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | pusher at 0.854 m, still; touching block1_geom, block2_geom
2.75 s: block1 at (0.25, 0.00, 0.05) m, at rest; touching floor | block2 at (0.13, 0.00, 0.13) m, at rest, turned 90° from how it started; touching pusher_geom | block3 at (-0.02, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.15, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.28, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | pusher at 0.854 m, still; touching block2_geom
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (0.25, 0.00, 0.05) m, at rest; touching floor
- block2 at (0.13, 0.00, 0.13) m, at rest, turned 90° from how it started; touching pusher_geom
- block3 at (-0.02, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- block4 at (-0.15, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- block5 at (-0.28, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- pusher at 0.854 m, still; touching block2_geom
</history>
