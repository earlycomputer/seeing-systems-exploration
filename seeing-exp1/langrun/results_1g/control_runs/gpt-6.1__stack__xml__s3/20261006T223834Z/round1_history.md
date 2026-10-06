MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1_geom; starts at (0.00, 0.00, 0.12) m, at rest
- block2: free body; its geoms: block2_geom; starts at (0.00, 0.00, 0.36) m, at rest
- block3: free body; its geoms: block3_geom; starts at (0.00, 0.00, 0.60) m, at rest
- block4: free body; its geoms: block4_geom; starts at (0.00, 0.00, 0.84) m, at rest
- block5: free body; its geoms: block5_geom; starts at (0.00, 0.00, 1.08) m, at rest
- pusher: slide joint pusher_slide about axis (1.00, 0.00, 0.00), range 0 m to 1.1 m as MuJoCo applies it; its geoms: pusher_geom; starts at 0.000 m, still

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
 0.21 s  block1_geom leaves floor
 0.21 s  block1_geom first touches pusher_geom
 0.21 s  block1 starts moving
 0.21 s  block2 starts moving
 0.21 s  block1_geom leaves block2_geom
 0.23 s  block4_geom leaves block5_geom
 0.23 s  block3_geom leaves block4_geom
 0.24 s  block1_geom touches floor again
 0.25 s  block1_geom leaves pusher_geom
 0.26 s  block1_geom touches block2_geom again
 0.27 s  block3_geom touches block4_geom again
 0.27 s  block4_geom touches block5_geom again
 0.29 s  block1_geom touches pusher_geom again
 0.29 s  block1_geom leaves floor
 0.30 s  block1_geom leaves block2_geom
 0.31 s  block4_geom leaves block5_geom
 0.31 s  block2_geom leaves block3_geom
 0.31 s  block3_geom leaves block4_geom
 0.35 s  block1_geom touches floor again
 0.37 s  block1_geom touches block2_geom again
 0.38 s  block2_geom touches block3_geom again
 0.39 s  block3_geom touches block4_geom again
 0.40 s  block4_geom touches block5_geom again
 0.43 s  block1_geom leaves floor
 0.43 s  block1_geom leaves block2_geom
 0.44 s  block3_geom leaves block4_geom
 0.44 s  block4_geom leaves block5_geom
 0.44 s  block2_geom leaves block3_geom
 0.47 s  block1_geom touches floor again
 0.48 s  block1_geom touches block2_geom again
 0.48 s  block2_geom touches block3_geom again
 0.50 s  block3_geom touches block4_geom again
 0.50 s  block4_geom touches block5_geom again
 0.54 s  block1_geom leaves pusher_geom
 0.54 s  block1_geom leaves floor
 0.55 s  block2_geom leaves block3_geom
 0.55 s  block4_geom leaves block5_geom
 0.56 s  block1_geom leaves block2_geom
 0.57 s  block3_geom leaves block4_geom
 0.59 s  block1_geom touches floor 1 more times between 0.59 s and 6.00 s, still touching at the end
 0.59 s  block1_geom touches block2_geom 1 more times between 0.59 s and 0.66 s
 0.59 s  block2_geom touches block3_geom again
 0.60 s  block1_geom touches pusher_geom again
 0.60 s  block3_geom touches block4_geom 1 more times between 0.60 s and 0.82 s
 0.61 s  block4_geom touches block5_geom 2 more times between 0.61 s and 0.80 s
 0.61 s  block1_geom leaves pusher_geom
 0.64 s  block1_geom touches pusher_geom again
 0.66 s  block2_geom first touches pusher_geom
 0.84 s  block4 passes 0.42 m from pusher (pusher_geom) without touching it: nearest points (-0.16, -0.10, 0.35) m and (0.22, -0.10, 0.17) m
 0.85 s  block2_geom leaves block3_geom
 0.87 s  block3 passes 0.18 m from pusher (pusher_geom) without touching it: nearest points (0.06, -0.10, 0.22) m and (0.23, -0.10, 0.17) m
 0.98 s  block3_geom first touches floor
 0.98 s  block4_geom first touches floor
 0.99 s  block5_geom first touches floor
 0.99 s  block2_geom touches block3_geom 2 more times between 0.99 s and 6.00 s, still touching at the end
 1.03 s  block3_geom leaves floor
 1.06 s  block4 comes to rest at (-0.38, 0.00, 0.10) m
 1.07 s  block3_geom touches floor again
 1.09 s  block5 comes to rest at (-0.68, 0.00, 0.10) m
 1.10 s  block3 comes to rest at (-0.11, 0.01, 0.10) m
 1.11 s  block2 comes to rest at (0.15, 0.00, 0.21) m
 1.12 s  block1 comes to rest at (0.52, 0.01, 0.12) m
 5.05 s  pusher reaches its upper stop (1.1 m) moving +0.00 m/s
 6.00 s  pusher is at its largest, 1.1 m

State every 0.25 s:
0.00 s: block1 at (0.00, 0.00, 0.12) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.36) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.60) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.84) m, at rest; touching block3_geom | block5 at (0.00, 0.00, 1.08) m, at rest; touching nothing | pusher at 0.000 m, still; touching nothing
0.25 s: block1 at (0.06, 0.00, 0.12) m, moving 1.83 m/s (vx +1.82, vy +0.00, vz +0.13); touching nothing | block2 at (0.02, 0.00, 0.36) m, moving 0.43 m/s (vx +0.42, vy -0.00, vz -0.07), turned 1° from how it started; touching nothing | block3 at (0.01, 0.00, 0.60) m, moving 0.27 m/s (vx +0.26, vy +0.00, vz -0.07), turned 1° from how it started; touching nothing | block4 at (0.00, 0.00, 0.84) m, moving 0.12 m/s (vx +0.10, vy +0.00, vz -0.07), turned 1° from how it started; touching nothing | block5 at (0.00, 0.00, 1.08) m, moving 0.09 m/s (vx -0.06, vy +0.00, vz -0.07), turned 1° from how it started; touching nothing | pusher at 0.637 m, moving +1.57 m/s; touching nothing
0.50 s: block1 at (0.32, 0.00, 0.12) m, moving 0.70 m/s (vx +0.69, vy +0.01, vz +0.15); touching block2_geom, pusher_geom | block2 at (0.17, 0.00, 0.35) m, moving 0.37 m/s (vx +0.37, vy -0.00, vz -0.03), turned 20° from how it started; touching block1_geom, block3_geom | block3 at (0.09, 0.00, 0.57) m, moving 0.16 m/s (vx -0.06, vy -0.01, vz -0.14), turned 20° from how it started; touching block2_geom, block4_geom | block4 at (0.01, 0.00, 0.80) m, moving 0.42 m/s (vx -0.17, vy +0.01, vz -0.38), turned 20° from how it started; touching block3_geom | block5 at (-0.07, 0.00, 1.03) m, moving 0.81 m/s (vx -0.41, vy +0.00, vz -0.70), turned 21° from how it started; touching nothing | pusher at 0.894 m, moving +0.63 m/s; touching block1_geom
0.75 s: block1 at (0.45, 0.00, 0.12) m, moving 0.41 m/s (vx +0.41, vy +0.01, vz +0.00); touching pusher_geom | block2 at (0.22, 0.00, 0.32) m, moving 0.09 m/s (vx -0.03, vy -0.00, vz -0.08), turned 51° from how it started; touching block3_geom, pusher_geom | block3 at (0.04, 0.00, 0.48) m, moving 0.84 m/s (vx -0.51, vy +0.01, vz -0.67), turned 51° from how it started; touching block2_geom, block4_geom | block4 at (-0.14, 0.00, 0.63) m, moving 1.58 m/s (vx -0.98, vy -0.01, vz -1.24), turned 51° from how it started; touching block3_geom | block5 at (-0.33, 0.00, 0.79) m, moving 2.25 m/s (vx -1.43, vy -0.00, vz -1.74), turned 50° from how it started; touching nothing | pusher at 1.018 m, moving +0.42 m/s; touching block1_geom, block2_geom
1.00 s: block1 at (0.50, 0.01, 0.12) m, moving 0.17 m/s (vx +0.17, vy -0.00, vz -0.00); touching pusher_geom | block2 at (0.14, 0.00, 0.22) m, moving 0.22 m/s (vx +0.22, vy +0.00, vz -0.00), turned 124° from how it started; touching block3_geom, pusher_geom | block3 at (-0.10, 0.00, 0.10) m, moving 0.19 m/s (vx -0.02, vy +0.06, vz +0.18), turned 96° from how it started; touching block2_geom, floor | block4 at (-0.38, 0.00, 0.09) m, moving 0.23 m/s (vx +0.06, vy +0.05, vz +0.21), turned 90° from how it started; touching floor | block5 at (-0.68, 0.00, 0.08) m, moving 0.18 m/s (vx -0.16, vy -0.01, vz -0.07), turned 92° from how it started; touching floor | pusher at 1.075 m, moving +0.19 m/s; touching block1_geom, block2_geom
1.25 s: block1 at (0.52, 0.01, 0.12) m, at rest; touching floor, pusher_geom | block2 at (0.15, 0.00, 0.21) m, at rest, turned 129° from how it started; touching block3_geom, pusher_geom | block3 at (-0.11, 0.01, 0.10) m, at rest, turned 90° from how it started; touching block2_geom, floor | block4 at (-0.38, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.68, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 1.091 m, still; touching block1_geom, block2_geom
1.50 s: block1 at (0.52, 0.01, 0.12) m, at rest; touching floor, pusher_geom | block2 at (0.15, 0.00, 0.21) m, at rest, turned 129° from how it started; touching block3_geom, pusher_geom | block3 at (-0.11, 0.01, 0.10) m, at rest, turned 90° from how it started; touching block2_geom, floor | block4 at (-0.38, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.68, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 1.092 m, still; touching block1_geom, block2_geom
(the same through 2.00 s)
2.25 s: block1 at (0.52, 0.01, 0.12) m, at rest; touching floor, pusher_geom | block2 at (0.15, 0.00, 0.21) m, at rest, turned 129° from how it started; touching block3_geom, pusher_geom | block3 at (-0.11, 0.01, 0.10) m, at rest, turned 90° from how it started; touching block2_geom, floor | block4 at (-0.38, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.68, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 1.093 m, still; touching block1_geom, block2_geom
(the same through 3.25 s)
3.50 s: block1 at (0.52, 0.01, 0.12) m, at rest; touching floor, pusher_geom | block2 at (0.15, 0.00, 0.21) m, at rest, turned 129° from how it started; touching block3_geom, pusher_geom | block3 at (-0.11, 0.01, 0.10) m, at rest, turned 90° from how it started; touching block2_geom, floor | block4 at (-0.38, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.68, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 1.094 m, still; touching block1_geom, block2_geom
(the same through 4.25 s)
4.50 s: block1 at (0.52, 0.01, 0.12) m, at rest; touching floor, pusher_geom | block2 at (0.15, 0.00, 0.21) m, at rest, turned 129° from how it started; touching block3_geom, pusher_geom | block3 at (-0.11, 0.01, 0.10) m, at rest, turned 90° from how it started; touching block2_geom, floor | block4 at (-0.38, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.68, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 1.095 m, still; touching block1_geom, block2_geom
(the same through 5.00 s)
5.25 s: block1 at (0.53, 0.01, 0.12) m, at rest; touching floor, pusher_geom | block2 at (0.15, 0.00, 0.21) m, at rest, turned 129° from how it started; touching block3_geom, pusher_geom | block3 at (-0.11, 0.01, 0.10) m, at rest, turned 90° from how it started; touching block2_geom, floor | block4 at (-0.38, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.68, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 1.095 m, still; touching block1_geom, block2_geom
5.50 s: block1 at (0.53, 0.01, 0.12) m, at rest; touching floor, pusher_geom | block2 at (0.16, 0.00, 0.21) m, at rest, turned 129° from how it started; touching block3_geom, pusher_geom | block3 at (-0.11, 0.01, 0.10) m, at rest, turned 90° from how it started; touching block2_geom, floor | block4 at (-0.38, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.68, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 1.095 m, still; touching block1_geom, block2_geom
5.75 s: block1 at (0.53, 0.01, 0.12) m, at rest; touching floor, pusher_geom | block2 at (0.16, 0.00, 0.21) m, at rest, turned 129° from how it started; touching block3_geom, pusher_geom | block3 at (-0.11, 0.01, 0.10) m, at rest, turned 90° from how it started; touching block2_geom, floor | block4 at (-0.38, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.68, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 1.096 m, still; touching block1_geom, block2_geom
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (0.53, 0.01, 0.12) m, at rest; touching floor, pusher_geom
- block2 at (0.16, 0.00, 0.21) m, at rest, turned 129° from how it started; touching block3_geom, pusher_geom
- block3 at (-0.11, 0.01, 0.10) m, at rest, turned 90° from how it started; touching block2_geom, floor
- block4 at (-0.38, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- block5 at (-0.68, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- pusher at 1.096 m, still; touching block1_geom, block2_geom
</history>
