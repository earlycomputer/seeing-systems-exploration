MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pusher: slide joint pusher_slide about axis (1.00, 0.00, 0.00), range 0 m to 1.8 m as MuJoCo applies it; its geoms: pusher_geom; starts at 0.000 m, still
- block1: free body; its geoms: block1_geom; starts at (0.00, 0.00, 0.10) m, at rest
- block2: free body; its geoms: block2_geom; starts at (-0.01, 0.00, 0.30) m, at rest
- block3: free body; its geoms: block3_geom; starts at (-0.02, 0.00, 0.50) m, at rest
- block4: free body; its geoms: block4_geom; starts at (-0.03, 0.00, 0.70) m, at rest
- block5: free body; its geoms: block5_geom; starts at (-0.04, 0.00, 0.90) m, at rest

What happened, in order:
 0.00 s  block1_geom starts touching block2_geom
 0.00 s  block3_geom starts touching block4_geom
 0.00 s  block1_geom starts touching floor
 0.00 s  block2_geom starts touching block3_geom
 0.00 s  pusher starts at its lower stop (0 m)
 0.01 s  block4_geom first touches block5_geom
 0.48 s  block1_geom leaves floor
 0.48 s  pusher_geom first touches block1_geom
 0.48 s  block1 starts moving
 0.48 s  block2 starts moving
 0.48 s  block3 starts moving
 0.48 s  block4 starts moving
 0.48 s  block5 starts moving
 0.49 s  block1_geom leaves block2_geom
 0.51 s  block4_geom leaves block5_geom
 0.51 s  block2_geom leaves block3_geom
 0.51 s  block3_geom leaves block4_geom
 0.52 s  block1_geom touches floor again
 0.52 s  block1_geom leaves floor
 0.52 s  pusher_geom leaves block1_geom
 0.54 s  block5 is at the top of its flight, at (-0.06, 0.00, 0.91) m
 0.54 s  block3 is at the top of its flight, at (0.01, 0.00, 0.52) m
 0.54 s  block4 is at the top of its flight, at (-0.02, 0.00, 0.71) m
 0.59 s  block1 is at the top of its flight, at (0.27, 0.00, 0.12) m
 0.61 s  pusher_geom first touches block2_geom
 0.61 s  pusher_geom leaves block2_geom
 0.63 s  block2_geom touches block3_geom again
 0.65 s  pusher passes 0.20 m from block3 (block3_geom) without touching it: nearest points (0.20, 0.00, 0.18) m and (0.12, 0.00, 0.37) m
 0.66 s  block1_geom touches floor again
 0.66 s  block1_geom leaves floor
 0.66 s  block2_geom leaves block3_geom
 0.68 s  pusher passes 0.41 m from block4 (block4_geom) without touching it: nearest points (0.28, -0.12, 0.18) m and (0.11, -0.12, 0.56) m
 0.70 s  block3_geom touches block4_geom again
 0.71 s  block3_geom leaves block4_geom
 0.72 s  pusher_geom touches block1_geom again
 0.74 s  block1_geom touches floor again
 0.75 s  block1_geom leaves floor
 0.78 s  block2_geom first touches floor
 0.80 s  block1_geom touches floor 7 more times between 0.80 s and 6.00 s, still touching at the end
 0.80 s  block2_geom touches block3_geom again
 0.80 s  block2_geom leaves floor
 0.81 s  block3_geom touches block4_geom again
 0.83 s  block2_geom leaves block3_geom
 0.84 s  block4_geom touches block5_geom again
 0.84 s  pusher reaches its upper stop (1.8 m) moving +2.86 m/s
 0.85 s  pusher_geom leaves block1_geom
 0.85 s  pusher is at its largest, 1.8 m
 0.87 s  pusher reaches its upper stop (1.8 m) again moving -0.28 m/s
 0.87 s  block3_geom first touches floor
 0.89 s  block3_geom leaves floor
 0.89 s  block2_geom touches floor again
 0.90 s  block4_geom leaves block5_geom
 0.91 s  block3_geom leaves block4_geom
 0.94 s  block4_geom first touches floor
 0.95 s  block3_geom touches floor again
 0.96 s  block2 comes to rest at (0.42, 0.00, 0.08) m
 0.97 s  block5_geom first touches floor
 0.97 s  block3_geom touches block4_geom again
 0.98 s  block3_geom leaves block4_geom
 1.01 s  block4 comes to rest at (-0.05, 0.00, 0.08) m
 1.03 s  block5_geom leaves floor
 1.06 s  block3 comes to rest at (0.18, 0.00, 0.08) m
 1.12 s  block5 is at the top of its flight, at (-0.53, 0.00, 0.15) m
 1.21 s  block5_geom touches floor again
 1.55 s  block5 comes to rest at (-0.61, 0.00, 0.10) m
 1.66 s  block1 comes to rest at (1.68, 0.00, 0.08) m

State every 0.25 s:
0.00 s: pusher at 0.000 m, still; touching nothing | block1 at (0.00, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (-0.01, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (-0.02, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (-0.03, 0.00, 0.70) m, at rest; touching block3_geom | block5 at (-0.04, 0.00, 0.90) m, at rest; touching nothing
0.25 s: pusher at 0.294 m, moving +2.02 m/s; touching nothing | block1 at (0.00, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (-0.01, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (-0.02, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (-0.03, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (-0.04, 0.00, 0.90) m, at rest; touching block4_geom
0.50 s: pusher at 0.904 m, moving +2.20 m/s; touching block1_geom | block1 at (0.03, 0.00, 0.10) m, moving 2.55 m/s (vx +2.55, vy +0.00, vz -0.01); touching pusher_geom | block2 at (0.01, 0.00, 0.31) m, moving 1.11 m/s (vx +1.03, vy +0.00, vz +0.42), turned 2° from how it started; touching block3_geom | block3 at (-0.01, 0.00, 0.51) m, moving 0.71 m/s (vx +0.58, vy +0.00, vz +0.40), turned 2° from how it started; touching block2_geom, block4_geom | block4 at (-0.03, 0.00, 0.71) m, moving 0.43 m/s (vx +0.15, vy +0.00, vz +0.40), turned 2° from how it started; touching block3_geom, block5_geom | block5 at (-0.04, 0.00, 0.91) m, moving 0.46 m/s (vx -0.25, vy +0.00, vz +0.38), turned 2° from how it started; touching block4_geom
0.75 s: pusher at 1.532 m, moving +2.78 m/s; touching nothing | block1 at (0.67, 0.00, 0.10) m, moving 2.52 m/s (vx +2.49, vy +0.00, vz -0.38); touching nothing | block2 at (0.29, 0.00, 0.18) m, moving 2.01 m/s (vx +1.24, vy +0.00, vz -1.57), turned 44° from how it started; touching nothing | block3 at (0.13, 0.00, 0.32) m, moving 1.98 m/s (vx +0.58, vy +0.00, vz -1.89), turned 44° from how it started; touching nothing | block4 at (0.01, 0.00, 0.50) m, moving 2.03 m/s (vx +0.12, vy +0.00, vz -2.03), turned 31° from how it started; touching nothing | block5 at (-0.11, 0.00, 0.70) m, moving 2.09 m/s (vx -0.25, vy +0.00, vz -2.07), turned 30° from how it started; touching nothing
1.00 s: pusher at 1.800 m, still; touching nothing | block1 at (1.29, 0.00, 0.11) m, moving 1.70 m/s (vx +1.69, vy +0.00, vz +0.23), turned 3° from how it started; touching nothing | block2 at (0.42, 0.00, 0.08) m, at rest, turned 90° from how it started; touching floor | block3 at (0.16, 0.00, 0.10) m, moving 0.32 m/s (vx +0.25, vy -0.00, vz -0.20), turned 102° from how it started; touching floor | block4 at (-0.05, 0.00, 0.08) m, moving 0.19 m/s (vx +0.13, vy +0.00, vz -0.14), turned 90° from how it started; touching floor | block5 at (-0.42, 0.00, 0.08) m, moving 2.43 m/s (vx -2.23, vy +0.00, vz -0.95), turned 93° from how it started; touching nothing
1.25 s: pusher at 1.800 m, still; touching nothing | block1 at (1.54, 0.00, 0.12) m, moving 0.35 m/s (vx +0.34, vy -0.00, vz +0.09), turned 24° from how it started; touching floor | block2 at (0.42, 0.00, 0.08) m, at rest, turned 90° from how it started; touching floor | block3 at (0.18, 0.00, 0.08) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.05, 0.00, 0.08) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.62, 0.00, 0.11) m, moving 0.31 m/s (vx -0.22, vy +0.00, vz +0.21), turned 175° from how it started; touching floor
1.50 s: pusher at 1.800 m, still; touching nothing | block1 at (1.61, 0.00, 0.12) m, moving 0.37 m/s (vx +0.35, vy -0.00, vz -0.10), turned 55° from how it started; touching floor | block2 at (0.42, 0.00, 0.08) m, at rest, turned 90° from how it started; touching floor | block3 at (0.18, 0.00, 0.08) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.05, 0.00, 0.08) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.61, 0.00, 0.10) m, moving 0.09 m/s (vx -0.07, vy +0.00, vz -0.05), turned 179° from how it started; touching floor
1.75 s: pusher at 1.800 m, still; touching nothing | block1 at (1.68, 0.00, 0.08) m, at rest, turned 90° from how it started; touching floor | block2 at (0.42, 0.00, 0.08) m, at rest, turned 90° from how it started; touching floor | block3 at (0.18, 0.00, 0.08) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.05, 0.00, 0.08) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.61, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- pusher at 1.800 m, still; touching nothing
- block1 at (1.68, 0.00, 0.08) m, at rest, turned 90° from how it started; touching floor
- block2 at (0.42, 0.00, 0.08) m, at rest, turned 90° from how it started; touching floor
- block3 at (0.18, 0.00, 0.08) m, at rest, turned 90° from how it started; touching floor
- block4 at (-0.05, 0.00, 0.08) m, at rest, turned 90° from how it started; touching floor
- block5 at (-0.61, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor
</history>
