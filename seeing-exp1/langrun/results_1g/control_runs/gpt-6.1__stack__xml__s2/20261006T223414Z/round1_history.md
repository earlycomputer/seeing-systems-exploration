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
- pusher: slide joint pusher_slide about axis (1.00, 0.00, 0.00), range 0 m to 1.55 m as MuJoCo applies it; its geoms: pusher_geom; starts at 0.000 m, still

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
 0.73 s  block1_geom first touches pusher_geom
 0.73 s  block1 starts moving
 0.73 s  block2 starts moving
 0.96 s  block1_geom leaves floor
 0.97 s  block4_geom leaves block5_geom
 0.99 s  block1_geom touches floor again
 1.01 s  block4_geom touches block5_geom again
 1.04 s  block1_geom leaves block2_geom
 1.04 s  block2_geom leaves block3_geom
 1.05 s  block3_geom leaves block4_geom
 1.05 s  block4_geom leaves block5_geom
 1.08 s  block1_geom touches block2_geom again
 1.08 s  block2_geom touches block3_geom again
 1.09 s  block3_geom touches block4_geom again
 1.10 s  block4_geom touches block5_geom again
 1.12 s  block1_geom leaves floor
 1.12 s  block1_geom leaves block2_geom
 1.12 s  block2_geom leaves block3_geom
 1.13 s  block4_geom leaves block5_geom
 1.15 s  block2_geom first touches pusher_geom
 1.16 s  block1_geom touches floor again
 1.16 s  block2_geom touches block3_geom again
 1.17 s  block1_geom leaves floor
 1.20 s  block4_geom touches block5_geom again
 1.21 s  block1_geom touches floor again
 1.22 s  block4_geom leaves block5_geom
 1.24 s  block3_geom leaves block4_geom
 1.27 s  block4 passes 0.36 m from pusher (pusher_geom) without touching it: nearest points (0.05, 0.09, 0.35) m and (0.35, 0.09, 0.16) m
 1.28 s  block2_geom leaves block3_geom
 1.36 s  block1_geom leaves pusher_geom
 1.38 s  pusher reaches its upper stop (1.55 m) moving +1.19 m/s
 1.39 s  pusher is at its largest, 1.6 m
 1.40 s  block1_geom leaves floor
 1.43 s  block3_geom first touches floor
 1.43 s  block4_geom first touches floor
 1.44 s  block5_geom first touches floor
 1.46 s  block2_geom touches block3_geom again
 1.46 s  block2_geom leaves pusher_geom
 1.46 s  block1_geom touches floor 1 more times between 1.46 s and 6.00 s, still touching at the end
 1.47 s  block3 passes 0.15 m from pusher (pusher_geom) without touching it: nearest points (0.34, 0.09, 0.16) m and (0.49, 0.09, 0.16) m
 1.49 s  block2_geom leaves block3_geom
 1.50 s  block3 comes to rest at (0.24, 0.00, 0.10) m
 1.51 s  block2_geom touches pusher_geom again
 1.51 s  block4 comes to rest at (-0.02, 0.00, 0.10) m
 1.52 s  block5 comes to rest at (-0.28, 0.00, 0.10) m
 1.55 s  block1 comes to rest at (0.81, 0.00, 0.10) m
 1.58 s  block2_geom touches block3_geom 1 more times between 1.58 s and 6.00 s, still touching at the end
 1.58 s  block2 comes to rest at (0.43, 0.00, 0.24) m

State every 0.25 s:
0.00 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3_geom | block5 at (0.00, 0.00, 0.90) m, at rest; touching nothing | pusher at 0.000 m, still; touching nothing
0.25 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4_geom | pusher at 0.272 m, moving +1.19 m/s; touching nothing
0.50 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4_geom | pusher at 0.570 m, moving +1.19 m/s; touching nothing
0.75 s: block1 at (0.02, 0.00, 0.10) m, moving 1.11 m/s (vx +1.11, vy +0.00, vz -0.02); touching pusher_geom | block2 at (0.00, 0.00, 0.30) m, moving 0.23 m/s (vx +0.23, vy +0.00, vz -0.02); touching block3_geom | block3 at (0.00, 0.00, 0.50) m, moving 0.15 m/s (vx +0.14, vy +0.00, vz -0.02); touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.70) m, moving 0.07 m/s (vx +0.07, vy +0.00, vz -0.02); touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4_geom | pusher at 0.861 m, moving +0.96 m/s; touching block1_geom
1.00 s: block1 at (0.27, 0.00, 0.10) m, moving 1.11 m/s (vx +1.09, vy -0.00, vz -0.22); touching block2_geom, pusher_geom | block2 at (0.19, 0.00, 0.31) m, moving 0.78 m/s (vx +0.78, vy -0.00, vz -0.02), turned 19° from how it started; touching block1_geom, block3_geom | block3 at (0.12, 0.00, 0.50) m, moving 0.55 m/s (vx +0.47, vy -0.00, vz -0.28), turned 19° from how it started; touching block2_geom | block4 at (0.05, 0.00, 0.69) m, moving 0.44 m/s (vx +0.18, vy +0.00, vz -0.40), turned 20° from how it started; touching nothing | block5 at (-0.02, 0.00, 0.88) m, moving 0.50 m/s (vx -0.11, vy +0.00, vz -0.48), turned 20° from how it started; touching nothing | pusher at 1.112 m, moving +1.13 m/s; touching block1_geom
1.25 s: block1 at (0.55, 0.00, 0.10) m, moving 1.19 m/s (vx +1.19, vy +0.00, vz -0.01); touching pusher_geom | block2 at (0.36, 0.00, 0.30) m, moving 0.64 m/s (vx +0.63, vy +0.00, vz -0.10), turned 56° from how it started; touching pusher_geom | block3 at (0.19, 0.00, 0.41) m, moving 0.85 m/s (vx +0.18, vy +0.00, vz -0.83), turned 56° from how it started; touching nothing | block4 at (0.02, 0.00, 0.52) m, moving 1.46 m/s (vx -0.29, vy +0.00, vz -1.43), turned 55° from how it started; touching nothing | block5 at (-0.14, 0.00, 0.64) m, moving 2.07 m/s (vx -0.74, vy +0.00, vz -1.93), turned 54° from how it started; touching nothing | pusher at 1.391 m, moving +1.18 m/s; touching block1_geom, block2_geom
1.50 s: block1 at (0.80, 0.00, 0.10) m, moving 0.41 m/s (vx +0.40, vy +0.00, vz -0.03); touching nothing | block2 at (0.43, 0.00, 0.24) m, moving 0.21 m/s (vx +0.21, vy +0.00, vz -0.03), turned 123° from how it started; touching nothing | block3 at (0.24, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.02, 0.00, 0.10) m, moving 0.10 m/s (vx +0.02, vy +0.00, vz +0.10), turned 90° from how it started; touching floor | block5 at (-0.28, 0.00, 0.10) m, moving 0.12 m/s (vx +0.01, vy -0.00, vz +0.12), turned 90° from how it started; touching floor | pusher at 1.550 m, still; touching nothing
1.75 s: block1 at (0.81, 0.00, 0.10) m, at rest; touching floor | block2 at (0.43, 0.00, 0.24) m, at rest, turned 126° from how it started; touching block3_geom, pusher_geom | block3 at (0.24, 0.00, 0.10) m, at rest, turned 90° from how it started; touching block2_geom, floor | block4 at (-0.02, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.28, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 1.550 m, still; touching block2_geom
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (0.81, 0.00, 0.10) m, at rest; touching floor
- block2 at (0.43, 0.00, 0.24) m, at rest, turned 126° from how it started; touching block3_geom, pusher_geom
- block3 at (0.24, 0.00, 0.10) m, at rest, turned 90° from how it started; touching block2_geom, floor
- block4 at (-0.02, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- block5 at (-0.28, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- pusher at 1.550 m, still; touching block2_geom
</history>
