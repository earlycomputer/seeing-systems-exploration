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
- pusher: slide joint pusher_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.6 m as MuJoCo applies it; its geoms: pusher_geom; starts at 0.000 m, still

What happened, in order:
 0.00 s  block1_geom starts touching floor
 0.00 s  block1_geom starts touching block2_geom
 0.00 s  block2_geom starts touching block3_geom
 0.00 s  block3_geom starts touching block4_geom
 0.00 s  pusher starts at its lower stop (0 m)
 0.01 s  block4_geom first touches block5_geom
 0.01 s  block5 starts moving
 0.32 s  block1_geom first touches pusher_geom
 0.32 s  block1 starts moving
 0.32 s  block2 starts moving
 0.32 s  block3 starts moving
 0.32 s  block4 starts moving
 0.43 s  block1_geom leaves floor
 0.46 s  block1_geom touches floor again
 0.57 s  block1_geom leaves block2_geom
 0.57 s  block2_geom first touches pusher_geom
 0.64 s  block4_geom leaves block5_geom
 0.64 s  block1_geom leaves pusher_geom
 0.67 s  block5 passes 0.27 m from pusher (pusher_geom) without touching it: nearest points (-0.07, -0.05, 0.25) m and (0.14, -0.05, 0.08) m
 0.68 s  block2_geom leaves block3_geom
 0.68 s  block1_geom touches pusher_geom again
 0.68 s  block3_geom leaves block4_geom
 0.70 s  block4 passes 0.16 m from pusher (pusher_geom) without touching it: nearest points (0.02, -0.05, 0.16) m and (0.16, -0.05, 0.08) m
 0.72 s  block3 passes 0.06 m from pusher (pusher_geom) without touching it: nearest points (0.12, -0.05, 0.10) m and (0.18, -0.05, 0.08) m
 0.77 s  pusher reaches its upper stop (0.6 m) moving +0.80 m/s
 0.78 s  block1_geom leaves pusher_geom
 0.80 s  block3_geom first touches floor
 0.80 s  pusher is at its largest, 0.6 m
 0.80 s  block4_geom first touches floor
 0.81 s  block5_geom first touches floor
 0.82 s  pusher reaches its upper stop (0.6 m) again moving -0.09 m/s
 0.86 s  block2_geom touches block3_geom again
 0.89 s  block3 comes to rest at (0.10, 0.00, 0.05) m
 0.90 s  block4 comes to rest at (-0.02, 0.00, 0.05) m
 0.91 s  block1 comes to rest at (0.40, 0.01, 0.05) m
 0.91 s  block5 comes to rest at (-0.16, 0.00, 0.05) m
 0.92 s  block2 comes to rest at (0.20, 0.00, 0.12) m

State every 0.25 s:
0.00 s: block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching nothing | pusher at 0.000 m, still; touching nothing
0.25 s: block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom | pusher at 0.194 m, moving +0.80 m/s; touching nothing
0.50 s: block1 at (0.13, 0.00, 0.05) m, moving 0.85 m/s (vx +0.85, vy -0.00, vz +0.06), turned 2° from how it started; touching block2_geom, floor, pusher_geom | block2 at (0.08, 0.00, 0.15) m, moving 0.54 m/s (vx +0.54, vy +0.00, vz +0.01), turned 17° from how it started; touching block1_geom, block3_geom | block3 at (0.05, 0.00, 0.25) m, moving 0.30 m/s (vx +0.29, vy +0.00, vz -0.06), turned 17° from how it started; touching block2_geom, block4_geom | block4 at (0.02, 0.00, 0.34) m, moving 0.14 m/s (vx +0.05, vy +0.00, vz -0.13), turned 17° from how it started; touching block3_geom, block5_geom | block5 at (-0.01, 0.00, 0.44) m, moving 0.26 m/s (vx -0.18, vy +0.00, vz -0.19), turned 18° from how it started; touching block4_geom | pusher at 0.385 m, moving +0.76 m/s; touching block1_geom
0.75 s: block1 at (0.33, 0.00, 0.05) m, moving 0.80 m/s (vx +0.80, vy +0.03, vz -0.02); touching floor, pusher_geom | block2 at (0.20, 0.00, 0.14) m, moving 0.49 m/s (vx +0.33, vy +0.00, vz -0.36), turned 84° from how it started; touching pusher_geom | block3 at (0.09, 0.00, 0.13) m, moving 1.36 m/s (vx +0.09, vy -0.00, vz -1.36), turned 80° from how it started; touching nothing | block4 at (-0.01, 0.00, 0.15) m, moving 1.80 m/s (vx -0.22, vy +0.00, vz -1.79), turned 78° from how it started; touching nothing | block5 at (-0.12, 0.00, 0.19) m, moving 2.14 m/s (vx -0.52, vy -0.01, vz -2.08), turned 72° from how it started; touching nothing | pusher at 0.583 m, moving +0.80 m/s; touching block1_geom, block2_geom
1.00 s: block1 at (0.40, 0.01, 0.05) m, at rest, turned 2° from how it started; touching floor | block2 at (0.20, 0.00, 0.12) m, at rest, turned 115° from how it started; touching block3_geom, pusher_geom | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2_geom, floor | block4 at (-0.02, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.16, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | pusher at 0.602 m, still; touching block2_geom
(the same through 1.25 s)
1.50 s: block1 at (0.40, 0.01, 0.05) m, at rest, turned 2° from how it started; touching floor | block2 at (0.20, 0.00, 0.12) m, at rest, turned 116° from how it started; touching block3_geom, pusher_geom | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2_geom, floor | block4 at (-0.02, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.16, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | pusher at 0.602 m, still; touching block2_geom
(the same through 2.25 s)
2.50 s: block1 at (0.40, 0.01, 0.05) m, at rest, turned 2° from how it started; touching floor | block2 at (0.20, 0.00, 0.12) m, at rest, turned 117° from how it started; touching block3_geom, pusher_geom | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2_geom, floor | block4 at (-0.02, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.16, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | pusher at 0.602 m, still; touching block2_geom
(the same through 2.75 s)
3.00 s: block1 at (0.40, 0.01, 0.05) m, at rest, turned 2° from how it started; touching floor | block2 at (0.19, 0.00, 0.12) m, at rest, turned 117° from how it started; touching block3_geom, pusher_geom | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2_geom, floor | block4 at (-0.02, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.16, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | pusher at 0.602 m, still; touching block2_geom
(the same through 3.25 s)
3.50 s: block1 at (0.40, 0.01, 0.05) m, at rest, turned 2° from how it started; touching floor | block2 at (0.19, 0.00, 0.12) m, at rest, turned 118° from how it started; touching block3_geom, pusher_geom | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2_geom, floor | block4 at (-0.02, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.16, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | pusher at 0.602 m, still; touching block2_geom
(the same through 4.50 s)
4.75 s: block1 at (0.40, 0.01, 0.05) m, at rest, turned 2° from how it started; touching floor | block2 at (0.19, 0.00, 0.12) m, at rest, turned 119° from how it started; touching block3_geom, pusher_geom | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2_geom, floor | block4 at (-0.02, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.16, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | pusher at 0.602 m, still; touching block2_geom
(the same through 5.75 s)
6.00 s: block1 at (0.40, 0.01, 0.05) m, at rest, turned 2° from how it started; touching floor | block2 at (0.19, 0.00, 0.12) m, at rest, turned 120° from how it started; touching block3_geom, pusher_geom | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2_geom, floor | block4 at (-0.02, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.16, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | pusher at 0.602 m, still; touching block2_geom

At the end (6.00 s):
- block1 at (0.40, 0.01, 0.05) m, at rest, turned 2° from how it started; touching floor
- block2 at (0.19, 0.00, 0.12) m, at rest, turned 120° from how it started; touching block3_geom, pusher_geom
- block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2_geom, floor
- block4 at (-0.02, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- block5 at (-0.16, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- pusher at 0.602 m, still; touching block2_geom
</history>
