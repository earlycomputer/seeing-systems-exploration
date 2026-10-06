Your expectations, checked against the run (3 of 3 hold):

- holds: pusher touches block1 (first touch at 1.00 s)
- holds: block2 touches floor (first touch at 1.71 s)
- holds: block5 touches floor (first touch at 1.79 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pusher: slide joint pusher_slide about axis (1.00, 0.00, 0.00), range -0.1 m to 0.675 m as MuJoCo applies it; its geoms: pusher_paddle, pusher_arm; starts at 0.000 m, moving +0.60 m/s
- block1: free body; its geoms: block1_geom; starts at (0.00, 0.00, 0.05) m, at rest
- block2: free body; its geoms: block2_geom; starts at (0.00, 0.00, 0.15) m, at rest
- block3: free body; its geoms: block3_geom; starts at (0.00, 0.00, 0.25) m, at rest
- block4: free body; its geoms: block4_geom; starts at (0.00, 0.00, 0.35) m, at rest
- block5: free body; its geoms: block5_geom; starts at (0.00, 0.00, 0.45) m, at rest

What happened, in order:
 0.00 s  block2_geom starts touching block3_geom
 0.00 s  block1_geom starts touching floor
 0.00 s  block1_geom starts touching block2_geom
 0.00 s  block3_geom starts touching block4_geom
 0.01 s  block3 starts moving
 0.01 s  block4 starts moving
 0.01 s  block5 starts moving
 0.01 s  block4_geom first touches block5_geom
 1.00 s  pusher_paddle first touches block1_geom
 1.01 s  block1 starts moving
 1.02 s  block2 starts moving
 1.15 s  pusher reaches its upper stop (0.675 m) moving +0.44 m/s
 1.16 s  pusher_paddle leaves block1_geom
 1.21 s  block1 comes to rest at (0.09, 0.00, 0.05) m
 1.65 s  block3_geom leaves block4_geom
 1.66 s  block4_geom leaves block5_geom
 1.67 s  block2_geom leaves block3_geom
 1.67 s  block1_geom leaves block2_geom
 1.71 s  block2_geom first touches floor
 1.71 s  pusher passes 0.01 m from block2 (block2_geom) without touching it: nearest points (0.01, 0.00, 0.04) m and (0.00, 0.00, 0.04) m
 1.71 s  pusher passes 0.11 m from block3 (block3_geom) without touching it: nearest points (0.01, 0.00, 0.04) m and (-0.08, 0.00, 0.10) m
 1.71 s  pusher passes 0.21 m from block4 (block4_geom) without touching it: nearest points (0.01, 0.00, 0.04) m and (-0.17, 0.00, 0.15) m
 1.71 s  pusher passes 0.31 m from block5 (block5_geom) without touching it: nearest points (0.01, 0.00, 0.04) m and (-0.26, 0.00, 0.20) m
 1.71 s  block2_geom touches block3_geom again
 1.72 s  block3_geom touches block4_geom again
 1.73 s  block4_geom touches block5_geom again
 1.75 s  block2_geom leaves block3_geom
 1.76 s  block3_geom leaves block4_geom
 1.77 s  block3_geom first touches floor
 1.78 s  block4_geom first touches floor
 1.78 s  block4_geom leaves block5_geom
 1.79 s  block5_geom first touches floor
 1.85 s  block3 comes to rest at (-0.18, 0.00, 0.05) m
 1.87 s  block4 comes to rest at (-0.30, 0.00, 0.05) m
 1.88 s  block2 comes to rest at (-0.07, 0.00, 0.05) m
 1.89 s  block5 comes to rest at (-0.42, 0.00, 0.05) m
 2.35 s  pusher is at its largest, 0.7 m

State every 0.25 s:
0.00 s: pusher at 0.000 m, moving +0.60 m/s; touching nothing | block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching nothing
0.25 s: pusher at 0.150 m, moving +0.60 m/s; touching nothing | block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
0.50 s: pusher at 0.300 m, moving +0.60 m/s; touching nothing | block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
0.75 s: pusher at 0.450 m, moving +0.60 m/s; touching nothing | block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
1.00 s: pusher at 0.600 m, moving +0.60 m/s; touching nothing | block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
1.25 s: pusher at 0.682 m, moving +0.01 m/s; touching nothing | block1 at (0.09, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.03, 0.00, 0.15) m, moving 0.08 m/s (vx +0.08, vy +0.00, vz +0.00), turned 8° from how it started; touching block1_geom, block3_geom | block3 at (0.02, 0.00, 0.25) m, at rest, turned 8° from how it started; touching block2_geom, block4_geom | block4 at (0.01, 0.00, 0.35) m, moving 0.07 m/s (vx -0.06, vy -0.00, vz -0.01), turned 8° from how it started; touching block3_geom, block5_geom | block5 at (-0.01, 0.00, 0.45) m, moving 0.14 m/s (vx -0.13, vy -0.00, vz -0.02), turned 8° from how it started; touching block4_geom
1.50 s: pusher at 0.683 m, still; touching nothing | block1 at (0.09, 0.00, 0.05) m, at rest; touching floor | block2 at (0.02, 0.00, 0.15) m, moving 0.14 m/s (vx -0.12, vy -0.00, vz -0.06), turned 23° from how it started; touching block3_geom | block3 at (-0.02, 0.00, 0.24) m, moving 0.34 m/s (vx -0.31, vy -0.00, vz -0.14), turned 23° from how it started; touching block2_geom, block4_geom | block4 at (-0.06, 0.00, 0.33) m, moving 0.55 m/s (vx -0.51, vy -0.00, vz -0.22), turned 23° from how it started; touching block3_geom, block5_geom | block5 at (-0.10, 0.00, 0.42) m, moving 0.76 m/s (vx -0.70, vy -0.00, vz -0.30), turned 23° from how it started; touching block4_geom
1.75 s: pusher at 0.683 m, still; touching nothing | block1 at (0.09, 0.00, 0.05) m, at rest; touching floor | block2 at (-0.06, 0.00, 0.06) m, moving 0.56 m/s (vx -0.52, vy +0.00, vz -0.22), turned 79° from how it started; touching block3_geom, floor | block3 at (-0.16, 0.00, 0.07) m, moving 1.34 m/s (vx -0.79, vy +0.00, vz -1.08), turned 79° from how it started; touching block2_geom, block4_geom | block4 at (-0.26, 0.00, 0.10) m, moving 2.11 m/s (vx -1.17, vy +0.00, vz -1.76), turned 74° from how it started; touching block3_geom, block5_geom | block5 at (-0.35, 0.00, 0.14) m, moving 2.74 m/s (vx -1.49, vy +0.00, vz -2.30), turned 70° from how it started; touching block4_geom
2.00 s: pusher at 0.683 m, still; touching nothing | block1 at (0.09, 0.00, 0.05) m, at rest; touching floor | block2 at (-0.07, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block3 at (-0.18, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.30, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.42, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- pusher at 0.683 m, still; touching nothing
- block1 at (0.09, 0.00, 0.05) m, at rest; touching floor
- block2 at (-0.07, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- block3 at (-0.18, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- block4 at (-0.30, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- block5 at (-0.42, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
</history>
