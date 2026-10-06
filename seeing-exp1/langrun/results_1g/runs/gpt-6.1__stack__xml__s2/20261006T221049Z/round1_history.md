Your expectations, checked against the run (2 of 3 hold):

- holds: pusher touches block1 (first touch at 0.24 s)
- holds: block5 touches floor (first touch at 0.63 s)
- DOES NOT HOLD: pusher reaches its upper stop (pusher has no hinge with a range)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1_box; starts at (0.00, 0.00, 0.06) m, at rest
- block2: free body; its geoms: block2_box; starts at (0.00, 0.00, 0.18) m, at rest
- block3: free body; its geoms: block3_box; starts at (0.00, 0.00, 0.30) m, at rest
- block4: free body; its geoms: block4_box; starts at (0.00, 0.00, 0.42) m, at rest
- block5: free body; its geoms: block5_box; starts at (0.00, 0.00, 0.54) m, at rest
- pusher: slide joint pusher_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.7 m as MuJoCo applies it; its geoms: pusher_box; starts at 0.000 m, still

What happened, in order:
 0.00 s  block1_box starts touching floor
 0.00 s  block1_box starts touching block2_box
 0.00 s  block2_box starts touching block3_box
 0.00 s  block3_box starts touching block4_box
 0.00 s  pusher starts at its lower stop (0 m)
 0.01 s  block3 starts moving
 0.01 s  block4 starts moving
 0.01 s  block5 starts moving
 0.01 s  block4_box first touches block5_box
 0.24 s  block1_box first touches pusher_box
 0.24 s  block1 starts moving
 0.24 s  block2 starts moving
 0.24 s  block1_box leaves block2_box
 0.26 s  block4_box leaves block5_box
 0.26 s  block3_box leaves block4_box
 0.27 s  block1_box leaves pusher_box
 0.28 s  block1_box touches block2_box again
 0.29 s  block3_box touches block4_box again
 0.31 s  block4_box touches block5_box again
 0.31 s  block1_box touches pusher_box again
 0.32 s  block1_box leaves floor
 0.32 s  block1_box leaves pusher_box
 0.33 s  block3_box leaves block4_box
 0.34 s  block1_box leaves block2_box
 0.34 s  block4_box leaves block5_box
 0.34 s  block2_box leaves block3_box
 0.36 s  block1_box touches pusher_box again
 0.41 s  block2_box first touches pusher_box
 0.41 s  block2_box leaves pusher_box
 0.42 s  block1_box touches floor again
 0.42 s  block1_box leaves floor
 0.43 s  block2_box touches block3_box again
 0.43 s  block4 passes 0.25 m from pusher (pusher_box) without touching it: nearest points (0.02, 0.06, 0.29) m and (0.16, 0.06, 0.08) m
 0.44 s  block3 passes 0.12 m from pusher (pusher_box) without touching it: nearest points (0.11, 0.00, 0.17) m and (0.18, 0.00, 0.07) m
 0.45 s  block2_box leaves block3_box
 0.50 s  pusher reaches its upper stop (0.7 m) moving +2.43 m/s
 0.51 s  block1_box leaves pusher_box
 0.51 s  block2_box first touches floor
 0.51 s  block1_box touches floor again
 0.51 s  block1_box leaves floor
 0.52 s  block2_box touches block3_box again
 0.52 s  pusher is at its largest, 0.7 m
 0.53 s  block2_box leaves floor
 0.53 s  block3_box touches block4_box again
 0.55 s  block2_box leaves block3_box
 0.56 s  block1_box touches floor again
 0.57 s  block3_box leaves block4_box
 0.57 s  pusher reaches its upper stop (0.7 m) again moving -0.17 m/s
 0.58 s  block1_box leaves floor
 0.58 s  block4_box touches block5_box again
 0.59 s  block3_box first touches floor
 0.59 s  block2_box touches pusher_box again
 0.59 s  block4_box first touches floor
 0.60 s  block4_box leaves block5_box
 0.61 s  block2_box touches floor again
 0.62 s  block2_box touches block3_box again
 0.62 s  block2_box leaves pusher_box
 0.63 s  block5_box first touches floor
 0.65 s  block2_box leaves block3_box
 0.65 s  block2_box touches pusher_box again
 0.65 s  block3 comes to rest at (0.12, 0.00, 0.06) m
 0.67 s  block1_box touches floor 2 more times between 0.67 s and 6.00 s, still touching at the end
 0.67 s  block4 comes to rest at (0.00, 0.00, 0.06) m
 0.68 s  block2_box leaves pusher_box
 0.70 s  block5 comes to rest at (-0.16, 0.00, 0.06) m
 0.73 s  block2_box touches pusher_box again
 0.74 s  block2 comes to rest at (0.27, 0.00, 0.06) m
 0.76 s  block2_box leaves pusher_box
 0.86 s  block1 comes to rest at (0.87, 0.00, 0.06) m

State every 0.25 s:
0.00 s: block1 at (0.00, 0.00, 0.06) m, at rest; touching block2_box, floor | block2 at (0.00, 0.00, 0.18) m, at rest; touching block1_box, block3_box | block3 at (0.00, 0.00, 0.30) m, at rest; touching block2_box, block4_box | block4 at (0.00, 0.00, 0.42) m, at rest; touching block3_box | block5 at (0.00, 0.00, 0.54) m, at rest; touching nothing | pusher at 0.000 m, still; touching nothing
0.25 s: block1 at (0.02, 0.00, 0.06) m, moving 1.56 m/s (vx +1.56, vy -0.00, vz -0.01); touching pusher_box | block2 at (0.01, 0.00, 0.18) m, moving 0.45 m/s (vx +0.42, vy +0.00, vz +0.16), turned 1° from how it started; touching block3_box | block3 at (0.00, 0.00, 0.30) m, moving 0.30 m/s (vx +0.25, vy +0.00, vz +0.16), turned 1° from how it started; touching block2_box, block4_box | block4 at (0.00, 0.00, 0.42) m, moving 0.18 m/s (vx +0.08, vy +0.00, vz +0.16), turned 1° from how it started; touching block3_box, block5_box | block5 at (0.00, 0.00, 0.54) m, moving 0.18 m/s (vx -0.08, vy +0.00, vz +0.16), turned 1° from how it started; touching block4_box | pusher at 0.249 m, moving +1.35 m/s; touching block1_box
0.50 s: block1 at (0.46, 0.00, 0.06) m, moving 2.40 m/s (vx +2.39, vy -0.00, vz -0.22), turned 2° from how it started; touching pusher_box | block2 at (0.22, 0.00, 0.09) m, moving 1.55 m/s (vx +1.05, vy -0.00, vz -1.14), turned 55° from how it started; touching nothing | block3 at (0.11, 0.00, 0.16) m, moving 1.60 m/s (vx +0.48, vy -0.00, vz -1.52), turned 54° from how it started; touching nothing | block4 at (0.02, 0.00, 0.25) m, moving 1.80 m/s (vx +0.06, vy -0.00, vz -1.80), turned 48° from how it started; touching nothing | block5 at (-0.08, 0.00, 0.36) m, moving 1.89 m/s (vx -0.40, vy +0.00, vz -1.84), turned 49° from how it started; touching nothing | pusher at 0.690 m, moving +2.43 m/s; touching block1_box
0.75 s: block1 at (0.83, 0.00, 0.06) m, moving 0.73 m/s (vx +0.73, vy -0.00, vz -0.07); touching nothing | block2 at (0.27, 0.00, 0.06) m, at rest, turned 89° from how it started; touching floor, pusher_box | block3 at (0.12, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block4 at (0.00, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.16, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | pusher at 0.700 m, still; touching block2_box
1.00 s: block1 at (0.87, 0.00, 0.06) m, at rest; touching floor | block2 at (0.26, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block3 at (0.12, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block4 at (0.00, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.16, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor | pusher at 0.700 m, still; touching nothing
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (0.87, 0.00, 0.06) m, at rest; touching floor
- block2 at (0.26, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor
- block3 at (0.12, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor
- block4 at (0.00, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor
- block5 at (-0.16, 0.00, 0.06) m, at rest, turned 90° from how it started; touching floor
- pusher at 0.700 m, still; touching nothing
</history>
