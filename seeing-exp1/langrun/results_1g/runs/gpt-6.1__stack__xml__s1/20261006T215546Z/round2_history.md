Your expectations, checked against the run (3 of 4 hold):

- holds: pusher touches block1 (first touch at 0.55 s)
- holds: block1 touches floor (touching from the start)
- DOES NOT HOLD: block3 touches floor (they never touch)
- holds: block5 touches floor (first touch at 1.15 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1_geom; starts at (0.00, 0.00, 0.12) m, at rest
- block2: free body; its geoms: block2_geom; starts at (-0.01, 0.00, 0.36) m, at rest
- block3: free body; its geoms: block3_geom; starts at (-0.01, 0.00, 0.60) m, at rest
- block4: free body; its geoms: block4_geom; starts at (-0.01, 0.00, 0.84) m, at rest
- block5: free body; its geoms: block5_geom; starts at (-0.02, 0.00, 1.08) m, at rest
- pusher: slide joint pusher_slide about axis (1.00, 0.00, 0.00), range 0 m to 1.5 m as MuJoCo applies it; its geoms: pusher_geom; starts at 0.000 m, still

What happened, in order:
 0.00 s  block1_geom starts touching floor
 0.00 s  block1_geom starts touching block2_geom
 0.00 s  block2_geom starts touching block3_geom
 0.00 s  block3_geom starts touching block4_geom
 0.00 s  pusher starts at its lower stop (0 m)
 0.01 s  block3 starts moving
 0.01 s  block4 starts moving
 0.01 s  block5 starts moving
 0.01 s  block4_geom first touches block5_geom
 0.55 s  block1_geom first touches pusher_geom
 0.55 s  block1 starts moving
 0.55 s  block2 starts moving
 0.59 s  block1_geom leaves block2_geom
 0.60 s  block4_geom leaves block5_geom
 0.60 s  block2_geom leaves block3_geom
 0.60 s  block3_geom leaves block4_geom
 0.63 s  block1_geom leaves floor
 0.64 s  block1_geom leaves pusher_geom
 0.65 s  block5 is at the top of its flight, at (-0.05, 0.00, 1.12) m
 0.66 s  block4 is at the top of its flight, at (0.00, 0.00, 0.88) m
 0.66 s  block3 is at the top of its flight, at (0.05, 0.00, 0.64) m
 0.66 s  block2 is at the top of its flight, at (0.10, 0.00, 0.41) m
 0.72 s  block1_geom touches floor again
 0.77 s  block2_geom first touches pusher_geom
 0.79 s  block2_geom touches block3_geom again
 0.81 s  block3_geom touches block4_geom again
 0.83 s  block4_geom touches block5_geom again
 0.87 s  block4_geom leaves block5_geom
 0.87 s  block3_geom leaves block4_geom
 0.89 s  block2_geom leaves block3_geom
 0.94 s  block4 passes 0.43 m from pusher (pusher_geom) without touching it: nearest points (0.07, -0.10, 0.48) m and (0.42, -0.10, 0.22) m
 1.04 s  pusher reaches its upper stop (1.5 m) moving +1.50 m/s
 1.05 s  pusher is at its largest, 1.5 m
 1.07 s  block1_geom first touches block3_geom
 1.07 s  block3 passes 0.17 m from pusher (pusher_geom) without touching it: nearest points (0.39, -0.10, 0.23) m and (0.57, -0.10, 0.22) m
 1.10 s  block1 comes to rest at (0.27, 0.00, 0.06) m
 1.12 s  block1 passes 0.05 m from block4 (block4_geom) without touching it: nearest points (0.15, -0.10, 0.12) m and (0.09, -0.10, 0.12) m
 1.12 s  block1 passes 0.36 m from block5 (block5_geom) without touching it: nearest points (0.15, -0.10, 0.12) m and (-0.20, -0.10, 0.19) m
 1.13 s  block4_geom first touches floor
 1.14 s  block2_geom leaves pusher_geom
 1.15 s  block5_geom first touches floor
 1.25 s  block4 comes to rest at (-0.03, 0.00, 0.06) m
 1.26 s  block5 comes to rest at (-0.36, 0.00, 0.06) m
 1.28 s  block2_geom first touches floor
 1.30 s  block2_geom touches block3_geom again
 1.32 s  block3 comes to rest at (0.26, 0.00, 0.18) m
 1.32 s  block2_geom leaves block3_geom
 1.55 s  block2_geom touches pusher_geom again
 1.56 s  block2 comes to rest at (0.51, 0.00, 0.12) m

State every 0.25 s:
0.00 s: block1 at (0.00, 0.00, 0.12) m, at rest; touching block2_geom, floor | block2 at (-0.01, 0.00, 0.36) m, at rest; touching block1_geom, block3_geom | block3 at (-0.01, 0.00, 0.60) m, at rest; touching block2_geom, block4_geom | block4 at (-0.01, 0.00, 0.84) m, at rest; touching block3_geom | block5 at (-0.02, 0.00, 1.08) m, at rest; touching nothing | pusher at 0.000 m, still; touching nothing
0.25 s: block1 at (0.00, 0.00, 0.12) m, at rest; touching block2_geom, floor | block2 at (-0.01, 0.00, 0.36) m, at rest; touching block1_geom, block3_geom | block3 at (-0.01, 0.00, 0.60) m, at rest; touching block2_geom, block4_geom | block4 at (-0.02, 0.00, 0.84) m, at rest; touching block3_geom, block5_geom | block5 at (-0.02, 0.00, 1.08) m, at rest; touching block4_geom | pusher at 0.356 m, moving +1.49 m/s; touching nothing
0.50 s: block1 at (0.00, 0.00, 0.12) m, at rest; touching block2_geom, floor | block2 at (-0.01, 0.00, 0.36) m, at rest; touching block1_geom, block3_geom | block3 at (-0.01, 0.00, 0.60) m, at rest; touching block2_geom, block4_geom | block4 at (-0.02, 0.00, 0.84) m, at rest; touching block3_geom, block5_geom | block5 at (-0.02, 0.00, 1.08) m, at rest; touching block4_geom | pusher at 0.729 m, moving +1.49 m/s; touching nothing
0.75 s: block1 at (0.26, 0.00, 0.06) m, moving 0.19 m/s (vx +0.16, vy -0.00, vz +0.10), turned 88° from how it started; touching floor | block2 at (0.20, 0.00, 0.37) m, moving 1.40 m/s (vx +1.10, vy +0.00, vz -0.87), turned 21° from how it started; touching nothing | block3 at (0.11, 0.00, 0.60) m, moving 1.10 m/s (vx +0.63, vy +0.00, vz -0.90), turned 21° from how it started; touching nothing | block4 at (0.01, 0.00, 0.84) m, moving 0.94 m/s (vx +0.16, vy +0.00, vz -0.92), turned 20° from how it started; touching nothing | block5 at (-0.07, 0.00, 1.07) m, moving 1.00 m/s (vx -0.30, vy -0.00, vz -0.95), turned 20° from how it started; touching nothing | pusher at 1.065 m, moving +1.49 m/s; touching nothing
1.00 s: block1 at (0.27, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block2 at (0.49, 0.00, 0.29) m, moving 1.37 m/s (vx +1.12, vy -0.00, vz -0.80), turned 85° from how it started; touching nothing | block3 at (0.24, 0.00, 0.35) m, moving 2.03 m/s (vx +0.49, vy -0.00, vz -1.97), turned 70° from how it started; touching nothing | block4 at (-0.01, 0.00, 0.46) m, moving 2.53 m/s (vx -0.16, vy -0.00, vz -2.52), turned 64° from how it started; touching nothing | block5 at (-0.23, 0.00, 0.61) m, moving 3.02 m/s (vx -0.80, vy -0.00, vz -2.92), turned 58° from how it started; touching nothing | pusher at 1.440 m, moving +1.50 m/s; touching nothing
1.25 s: block1 at (0.27, 0.00, 0.06) m, at rest, turned 90° from how it started; touching block3_geom, floor | block2 at (0.49, 0.00, 0.18) m, moving 1.43 m/s (vx -0.33, vy +0.00, vz -1.39), turned 174° from how it started; touching nothing | block3 at (0.26, 0.00, 0.18) m, at rest, turned 90° from how it started; touching block1_geom | block4 at (-0.03, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.35, 0.00, 0.06) m, moving 0.22 m/s (vx -0.10, vy -0.00, vz -0.20), turned 89° from how it started; touching floor | pusher at 1.500 m, still; touching nothing
1.50 s: block1 at (0.27, 0.00, 0.06) m, at rest, turned 90° from how it started; touching block3_geom, floor | block2 at (0.49, 0.00, 0.13) m, moving 0.26 m/s (vx +0.24, vy -0.00, vz -0.08), turned 171° from how it started; touching floor | block3 at (0.26, 0.00, 0.18) m, at rest, turned 90° from how it started; touching block1_geom | block4 at (-0.03, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.36, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | pusher at 1.500 m, still; touching nothing
1.75 s: block1 at (0.27, 0.00, 0.06) m, at rest, turned 90° from how it started; touching block3_geom, floor | block2 at (0.51, 0.00, 0.12) m, at rest, turned 177° from how it started; touching floor, pusher_geom | block3 at (0.26, 0.00, 0.18) m, at rest, turned 90° from how it started; touching block1_geom | block4 at (-0.03, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.36, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | pusher at 1.500 m, still; touching block2_geom
(the same through 4.50 s)
4.75 s: block1 at (0.27, 0.00, 0.06) m, at rest, turned 90° from how it started; touching block3_geom, floor | block2 at (0.51, 0.00, 0.12) m, at rest, turned 178° from how it started; touching floor, pusher_geom | block3 at (0.26, 0.00, 0.18) m, at rest, turned 90° from how it started; touching block1_geom | block4 at (-0.03, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.36, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | pusher at 1.500 m, still; touching block2_geom
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (0.27, 0.00, 0.06) m, at rest, turned 90° from how it started; touching block3_geom, floor
- block2 at (0.51, 0.00, 0.12) m, at rest, turned 178° from how it started; touching floor, pusher_geom
- block3 at (0.26, 0.00, 0.18) m, at rest, turned 90° from how it started; touching block1_geom
- block4 at (-0.03, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor
- block5 at (-0.36, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor
- pusher at 1.500 m, still; touching block2_geom
</history>
