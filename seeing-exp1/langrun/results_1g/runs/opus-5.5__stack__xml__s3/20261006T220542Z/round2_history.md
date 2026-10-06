Your expectations, checked against the run (3 of 3 hold):

- holds: pusher touches block1 (first touch at 0.19 s)
- holds: block5 touches floor (first touch at 0.71 s)
- holds: block4 touches floor (first touch at 0.71 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pusher: slide joint pusher_slide about axis (1.00, 0.00, 0.00), range 0 m to 1.35 m as MuJoCo applies it; its geoms: pusher_geom; starts at 0.000 m, moving +4.00 m/s
- block1: free body; its geoms: block1_geom; starts at (0.00, 0.00, 0.05) m, at rest
- block2: free body; its geoms: block2_geom; starts at (0.00, 0.00, 0.15) m, at rest
- block3: free body; its geoms: block3_geom; starts at (0.00, 0.00, 0.25) m, at rest
- block4: free body; its geoms: block4_geom; starts at (0.00, 0.00, 0.35) m, at rest
- block5: free body; its geoms: block5_geom; starts at (0.00, 0.00, 0.45) m, at rest

What happened, in order:
 0.00 s  block1_geom starts touching block2_geom
 0.00 s  block3_geom starts touching block4_geom
 0.00 s  block1_geom starts touching floor
 0.00 s  block2_geom starts touching block3_geom
 0.00 s  pusher starts at its lower stop (0 m)
 0.01 s  block3 starts moving
 0.01 s  block4 starts moving
 0.01 s  block5 starts moving
 0.01 s  block4_geom first touches block5_geom
 0.18 s  pusher passes 0.14 m from block3 (block3_geom) without touching it: nearest points (-0.06, 0.00, 0.07) m and (-0.05, 0.00, 0.20) m
 0.18 s  pusher passes 0.23 m from block4 (block4_geom) without touching it: nearest points (-0.06, 0.00, 0.07) m and (-0.05, 0.00, 0.30) m
 0.18 s  pusher passes 0.33 m from block5 (block5_geom) without touching it: nearest points (-0.06, 0.00, 0.07) m and (-0.05, 0.00, 0.40) m
 0.19 s  block1_geom leaves floor
 0.19 s  pusher_geom first touches block1_geom
 0.19 s  block1 starts moving
 0.19 s  block2 starts moving
 0.19 s  block1_geom leaves block2_geom
 0.19 s  pusher passes 0.04 m from block2 (block2_geom) without touching it: nearest points (-0.05, 0.00, 0.07) m and (-0.05, 0.00, 0.10) m
 0.21 s  block4_geom leaves block5_geom
 0.21 s  block2_geom leaves block3_geom
 0.22 s  block3_geom leaves block4_geom
 0.23 s  block2 is at the top of its flight, at (0.03, 0.00, 0.16) m
 0.23 s  block3 is at the top of its flight, at (0.02, 0.00, 0.26) m
 0.23 s  block4 is at the top of its flight, at (0.01, 0.00, 0.36) m
 0.23 s  block5 is at the top of its flight, at (0.00, 0.00, 0.46) m
 0.24 s  block1_geom touches floor again
 0.24 s  block1_geom leaves floor
 0.25 s  pusher_geom leaves block1_geom
 0.29 s  block1_geom touches floor again
 0.30 s  block1_geom leaves floor
 0.38 s  block2_geom first touches floor
 0.39 s  block1_geom touches floor again
 0.39 s  block2_geom touches block3_geom again
 0.39 s  block3_geom touches block4_geom again
 0.39 s  pusher reaches its upper stop (1.35 m) moving +2.87 m/s
 0.40 s  block1_geom leaves floor
 0.40 s  block4_geom touches block5_geom again
 0.41 s  pusher is at its largest, 1.4 m
 0.43 s  block1_geom touches floor 7 more times between 0.43 s and 6.00 s, still touching at the end
 0.46 s  pusher reaches its upper stop (1.35 m) again moving -0.28 m/s
 0.48 s  block4_geom leaves block5_geom
 0.51 s  block2 comes to rest at (0.14, 0.00, 0.05) m
 0.53 s  block4_geom touches block5_geom again
 0.59 s  block3_geom leaves block4_geom
 0.61 s  block2_geom leaves block3_geom
 0.62 s  block4_geom leaves block5_geom
 0.71 s  block5_geom first touches floor
 0.71 s  block4_geom first touches floor
 0.72 s  block3_geom first touches floor
 0.80 s  block4 comes to rest at (-0.09, 0.00, 0.05) m
 0.80 s  block3 comes to rest at (0.02, 0.00, 0.05) m
 0.81 s  block5 comes to rest at (-0.22, 0.00, 0.05) m
 1.04 s  block1 comes to rest at (1.80, 0.00, 0.05) m

State every 0.25 s:
0.00 s: pusher at 0.000 m, moving +4.00 m/s; touching nothing | block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching nothing
0.25 s: pusher at 0.917 m, moving +3.15 m/s; touching block1_geom | block1 at (0.21, 0.00, 0.05) m, moving 3.85 m/s (vx +3.85, vy -0.00, vz +0.18); touching pusher_geom | block2 at (0.03, 0.00, 0.16) m, moving 0.56 m/s (vx +0.54, vy -0.00, vz -0.16), turned 7° from how it started; touching nothing | block3 at (0.02, 0.00, 0.26) m, moving 0.37 m/s (vx +0.33, vy -0.00, vz -0.16), turned 7° from how it started; touching nothing | block4 at (0.01, 0.00, 0.36) m, moving 0.22 m/s (vx +0.14, vy +0.00, vz -0.16), turned 7° from how it started; touching nothing | block5 at (0.00, 0.00, 0.46) m, moving 0.17 m/s (vx -0.04, vy +0.00, vz -0.16), turned 7° from how it started; touching nothing
0.50 s: pusher at 1.345 m, moving -0.19 m/s; touching nothing | block1 at (1.04, 0.00, 0.06) m, moving 2.88 m/s (vx +2.86, vy +0.00, vz -0.30); touching nothing | block2 at (0.14, 0.00, 0.05) m, moving 0.13 m/s (vx +0.11, vy +0.00, vz -0.06); touching block3_geom, floor | block3 at (0.08, 0.00, 0.16) m, moving 0.10 m/s (vx -0.01, vy +0.00, vz -0.10), turned 35° from how it started; touching block2_geom | block4 at (0.01, 0.00, 0.23) m, moving 0.37 m/s (vx -0.23, vy +0.00, vz -0.29), turned 38° from how it started; touching nothing | block5 at (-0.06, 0.00, 0.31) m, moving 0.70 m/s (vx -0.57, vy +0.00, vz -0.40), turned 39° from how it started; touching nothing
0.75 s: pusher at 1.336 m, still; touching nothing | block1 at (1.57, 0.00, 0.05) m, moving 1.36 m/s (vx +1.31, vy +0.00, vz +0.34), turned 2° from how it started; touching nothing | block2 at (0.14, 0.00, 0.05) m, at rest; touching floor | block3 at (0.02, 0.00, 0.04) m, moving 0.16 m/s (vx +0.03, vy +0.00, vz +0.16), turned 92° from how it started; touching floor | block4 at (-0.10, 0.00, 0.04) m, moving 0.21 m/s (vx +0.03, vy +0.00, vz +0.21), turned 91° from how it started; touching floor | block5 at (-0.22, 0.00, 0.04) m, moving 0.26 m/s (vx +0.02, vy -0.00, vz +0.26), turned 92° from how it started; touching floor
1.00 s: pusher at 1.336 m, still; touching nothing | block1 at (1.79, 0.00, 0.05) m, moving 0.29 m/s (vx +0.28, vy +0.00, vz -0.05); touching floor | block2 at (0.14, 0.00, 0.05) m, at rest; touching floor | block3 at (0.02, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.09, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.22, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
1.25 s: pusher at 1.336 m, still; touching nothing | block1 at (1.80, 0.00, 0.05) m, at rest; touching floor | block2 at (0.14, 0.00, 0.05) m, at rest; touching floor | block3 at (0.02, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.09, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.22, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- pusher at 1.336 m, still; touching nothing
- block1 at (1.80, 0.00, 0.05) m, at rest; touching floor
- block2 at (0.14, 0.00, 0.05) m, at rest; touching floor
- block3 at (0.02, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- block4 at (-0.09, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- block5 at (-0.22, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
</history>
