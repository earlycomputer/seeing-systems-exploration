MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1_geom; starts at (0.00, 0.00, 0.10) m, at rest
- block2: free body; its geoms: block2_geom; starts at (0.00, 0.00, 0.30) m, at rest
- block3: free body; its geoms: block3_geom; starts at (-0.01, 0.00, 0.50) m, at rest
- block4: free body; its geoms: block4_geom; starts at (-0.01, 0.00, 0.70) m, at rest
- block5: free body; its geoms: block5_geom; starts at (-0.01, 0.00, 0.90) m, at rest
- pusher: slide joint push_slide about axis (1.00, 0.00, 0.00), range 0 m to 1.6 m as MuJoCo applies it; its geoms: pusher_geom; starts at 0.000 m, still

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
 0.80 s  block1_geom first touches pusher_geom
 0.80 s  block1 starts moving
 0.80 s  block2 starts moving
 0.86 s  block1_geom leaves floor
 0.89 s  block1_geom touches floor again
 1.11 s  block1_geom leaves floor
 1.12 s  block1_geom leaves block2_geom
 1.13 s  block3_geom leaves block4_geom
 1.13 s  block4_geom leaves block5_geom
 1.14 s  block1_geom touches floor again
 1.15 s  block1_geom touches block2_geom again
 1.16 s  block3_geom touches block4_geom again
 1.17 s  block4_geom touches block5_geom again
 1.21 s  block1_geom leaves block2_geom
 1.22 s  block2_geom leaves block3_geom
 1.23 s  block3_geom leaves block4_geom
 1.23 s  block4_geom leaves block5_geom
 1.23 s  block1_geom leaves pusher_geom
 1.25 s  block1_geom touches block2_geom again
 1.25 s  block1_geom leaves block2_geom
 1.26 s  block2_geom first touches pusher_geom
 1.26 s  block2_geom touches block3_geom again
 1.27 s  block3_geom touches block4_geom again
 1.28 s  block1_geom leaves floor
 1.29 s  block4_geom touches block5_geom again
 1.29 s  block1_geom touches pusher_geom again
 1.29 s  block1_geom touches block2_geom again
 1.29 s  block1_geom leaves block2_geom
 1.31 s  block1_geom leaves pusher_geom
 1.34 s  block1_geom touches floor again
 1.34 s  block4_geom leaves block5_geom
 1.34 s  block1_geom leaves floor
 1.35 s  block1_geom touches pusher_geom again
 1.37 s  block3_geom leaves block4_geom
 1.38 s  block1_geom touches floor 8 more times between 1.38 s and 6.00 s, still touching at the end
 1.41 s  block4 passes 0.33 m from pusher (pusher_geom) without touching it: nearest points (0.04, 0.11, 0.33) m and (0.33, 0.11, 0.17) m
 1.41 s  block2_geom leaves block3_geom
 1.44 s  block3 passes 0.12 m from pusher (pusher_geom) without touching it: nearest points (0.25, 0.11, 0.22) m and (0.36, 0.11, 0.17) m
 1.54 s  block2_geom leaves pusher_geom
 1.55 s  block4_geom first touches floor
 1.56 s  block3_geom first touches floor
 1.56 s  block5_geom first touches floor
 1.58 s  block2_geom touches block3_geom again
 1.59 s  block5_geom leaves floor
 1.60 s  block2_geom leaves block3_geom
 1.60 s  block2_geom touches pusher_geom again
 1.62 s  block3 comes to rest at (0.21, 0.00, 0.09) m
 1.63 s  block4 comes to rest at (-0.06, 0.00, 0.09) m
 1.64 s  block5_geom touches floor again
 1.66 s  block2_geom leaves pusher_geom
 1.67 s  block5 comes to rest at (-0.35, 0.00, 0.09) m
 1.69 s  block2_geom touches pusher_geom again
 1.69 s  block2_geom leaves pusher_geom
 1.73 s  pusher reaches its upper stop (1.6 m) moving +0.96 m/s
 1.73 s  block1_geom leaves pusher_geom
 1.74 s  pusher is at its largest, 1.6 m
 1.74 s  block2_geom touches pusher_geom again
 1.75 s  block2_geom leaves pusher_geom
 1.75 s  block2_geom first touches floor
 1.76 s  block2_geom leaves floor
 1.79 s  block2_geom touches floor again
 1.94 s  block1 comes to rest at (0.96, 0.00, 0.10) m
 1.95 s  block2 comes to rest at (0.53, 0.00, 0.10) m

State every 0.25 s:
0.00 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (-0.01, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (-0.01, 0.00, 0.70) m, at rest; touching block3_geom | block5 at (-0.01, 0.00, 0.90) m, at rest; touching nothing | pusher at 0.000 m, still; touching nothing
0.25 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (-0.01, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (-0.01, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (-0.01, 0.00, 0.90) m, at rest; touching block4_geom | pusher at 0.209 m, moving +0.98 m/s; touching nothing
0.50 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (-0.01, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (-0.01, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (-0.01, 0.00, 0.90) m, at rest; touching block4_geom | pusher at 0.454 m, moving +0.98 m/s; touching nothing
0.75 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (-0.01, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (-0.01, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (-0.01, 0.00, 0.90) m, at rest; touching block4_geom | pusher at 0.700 m, moving +0.98 m/s; touching nothing
1.00 s: block1 at (0.16, 0.00, 0.10) m, moving 0.94 m/s (vx +0.94, vy +0.00, vz +0.11); touching block2_geom, pusher_geom | block2 at (0.12, 0.00, 0.31) m, moving 0.65 m/s (vx +0.65, vy +0.00, vz +0.08), turned 13° from how it started; touching block1_geom, block3_geom | block3 at (0.07, 0.00, 0.51) m, moving 0.41 m/s (vx +0.41, vy -0.00, vz -0.01), turned 13° from how it started; touching block2_geom, block4_geom | block4 at (0.02, 0.00, 0.70) m, moving 0.21 m/s (vx +0.20, vy -0.00, vz -0.06), turned 13° from how it started; touching block3_geom, block5_geom | block5 at (-0.02, 0.00, 0.90) m, moving 0.11 m/s (vx -0.01, vy -0.00, vz -0.10), turned 13° from how it started; touching block4_geom | pusher at 0.911 m, moving +0.85 m/s; touching block1_geom
1.25 s: block1 at (0.39, 0.00, 0.10) m, moving 1.03 m/s (vx +1.02, vy -0.00, vz -0.10), turned 1° from how it started; touching nothing | block2 at (0.28, 0.00, 0.31) m, moving 0.66 m/s (vx +0.56, vy +0.00, vz -0.35), turned 34° from how it started; touching nothing | block3 at (0.16, 0.00, 0.47) m, moving 0.59 m/s (vx +0.26, vy -0.00, vz -0.53), turned 34° from how it started; touching nothing | block4 at (0.04, 0.00, 0.64) m, moving 0.69 m/s (vx -0.14, vy -0.00, vz -0.67), turned 36° from how it started; touching nothing | block5 at (-0.08, 0.00, 0.80) m, moving 1.09 m/s (vx -0.58, vy -0.00, vz -0.92), turned 37° from how it started; touching nothing | pusher at 1.136 m, moving +0.95 m/s; touching nothing
1.50 s: block1 at (0.63, 0.00, 0.10) m, moving 0.99 m/s (vx +0.98, vy +0.00, vz -0.11); touching floor | block2 at (0.39, 0.00, 0.26) m, moving 0.30 m/s (vx +0.26, vy -0.00, vz -0.14), turned 97° from how it started; touching pusher_geom | block3 at (0.18, 0.00, 0.23) m, moving 2.00 m/s (vx +0.03, vy +0.00, vz -2.00), turned 90° from how it started; touching nothing | block4 at (-0.04, 0.00, 0.25) m, moving 2.73 m/s (vx -0.38, vy +0.00, vz -2.71), turned 84° from how it started; touching nothing | block5 at (-0.27, 0.00, 0.30) m, moving 3.26 m/s (vx -0.79, vy +0.00, vz -3.16), turned 76° from how it started; touching nothing | pusher at 1.380 m, moving +0.97 m/s; touching block2_geom
1.75 s: block1 at (0.87, 0.00, 0.10) m, moving 0.89 m/s (vx +0.89, vy -0.00, vz +0.03); touching nothing | block2 at (0.53, 0.00, 0.13) m, moving 1.10 m/s (vx +0.21, vy +0.00, vz -1.08), turned 160° from how it started; touching pusher_geom | block3 at (0.21, 0.00, 0.09) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.06, 0.00, 0.09) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.35, 0.00, 0.09) m, at rest, turned 90° from how it started; touching floor | pusher at 1.601 m, moving -0.07 m/s; touching block2_geom
2.00 s: block1 at (0.96, 0.00, 0.10) m, at rest; touching floor | block2 at (0.53, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor | block3 at (0.21, 0.00, 0.09) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.06, 0.00, 0.09) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.35, 0.00, 0.09) m, at rest, turned 90° from how it started; touching floor | pusher at 1.600 m, still; touching nothing
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (0.96, 0.00, 0.10) m, at rest; touching floor
- block2 at (0.53, 0.00, 0.10) m, at rest, turned 180° from how it started; touching floor
- block3 at (0.21, 0.00, 0.09) m, at rest, turned 90° from how it started; touching floor
- block4 at (-0.06, 0.00, 0.09) m, at rest, turned 90° from how it started; touching floor
- block5 at (-0.35, 0.00, 0.09) m, at rest, turned 90° from how it started; touching floor
- pusher at 1.600 m, still; touching nothing
</history>
