MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pusher: slide joint pusher_slide about axis (1.00, 0.00, 0.00), no range limit; its geoms: pusher_geom; starts at 0.000 m, moving +2.00 m/s
- block1: free body; its geoms: block1_geom; starts at (0.00, 0.00, 0.10) m, at rest
- block2: free body; its geoms: block2_geom; starts at (0.00, 0.00, 0.30) m, at rest
- block3: free body; its geoms: block3_geom; starts at (0.00, 0.00, 0.50) m, at rest
- block4: free body; its geoms: block4_geom; starts at (0.00, 0.00, 0.70) m, at rest
- block5: free body; its geoms: block5_geom; starts at (0.00, 0.00, 0.90) m, at rest

What happened, in order:
 0.00 s  block1_geom starts touching block2_geom
 0.00 s  block3_geom starts touching block4_geom
 0.00 s  block1_geom starts touching floor
 0.00 s  block2_geom starts touching block3_geom
 0.01 s  block3 starts moving
 0.01 s  block4 starts moving
 0.01 s  block5 starts moving
 0.01 s  block4_geom first touches block5_geom
 0.48 s  pusher_geom first touches block1_geom
 0.48 s  block1 starts moving
 0.48 s  block2 starts moving
 0.65 s  pusher passes 0.05 m from block2 (block2_geom) without touching it: nearest points (-0.03, -0.12, 0.15) m and (-0.03, -0.12, 0.20) m
 0.67 s  pusher passes 0.25 m from block3 (block3_geom) without touching it: nearest points (-0.04, -0.12, 0.15) m and (-0.04, -0.12, 0.40) m
 0.67 s  pusher passes 0.45 m from block4 (block4_geom) without touching it: nearest points (-0.07, -0.12, 0.15) m and (-0.07, -0.12, 0.59) m
 0.76 s  pusher is at its largest, 0.9 m
 0.78 s  pusher_geom leaves block1_geom
 1.38 s  pusher_geom touches block1_geom again
 1.48 s  pusher_geom leaves block1_geom
 1.74 s  block1 comes to rest at (0.13, 0.00, 0.10) m
 2.23 s  block2 comes to rest at (0.11, 0.00, 0.30) m
 2.39 s  block3 comes to rest at (0.11, 0.00, 0.50) m
 2.47 s  block4 comes to rest at (0.11, 0.00, 0.70) m
 2.49 s  block5 comes to rest at (0.11, 0.00, 0.90) m

State every 0.25 s:
0.00 s: pusher at 0.000 m, moving +2.00 m/s; touching nothing | block1 at (0.00, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3_geom | block5 at (0.00, 0.00, 0.90) m, at rest; touching nothing
0.25 s: pusher at 0.442 m, moving +1.56 m/s; touching nothing | block1 at (0.00, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4_geom
0.50 s: pusher at 0.781 m, moving +0.92 m/s; touching block1_geom | block1 at (0.02, 0.00, 0.10) m, moving 1.09 m/s (vx +1.09, vy +0.00, vz -0.06); touching pusher_geom | block2 at (0.01, 0.00, 0.30) m, moving 0.44 m/s (vx +0.43, vy +0.00, vz +0.08); touching block3_geom | block3 at (0.00, 0.00, 0.50) m, moving 0.29 m/s (vx +0.27, vy -0.00, vz +0.09); touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.70) m, moving 0.14 m/s (vx +0.11, vy -0.00, vz +0.10); touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.90) m, moving 0.12 m/s (vx -0.06, vy +0.00, vz +0.10); touching block4_geom
0.75 s: pusher at 0.892 m, moving +0.01 m/s; touching block1_geom | block1 at (0.13, 0.00, 0.10) m, at rest; touching block2_geom, floor, pusher_geom | block2 at (0.10, 0.00, 0.31) m, moving 0.12 m/s (vx +0.10, vy +0.00, vz -0.07), turned 4° from how it started; touching block1_geom, block3_geom | block3 at (0.09, 0.00, 0.51) m, moving 0.25 m/s (vx +0.25, vy -0.00, vz -0.05), turned 4° from how it started; touching block2_geom, block4_geom | block4 at (0.07, 0.00, 0.71) m, moving 0.40 m/s (vx +0.40, vy -0.00, vz -0.04), turned 4° from how it started; touching block3_geom, block5_geom | block5 at (0.05, 0.00, 0.90) m, moving 0.55 m/s (vx +0.55, vy -0.00, vz -0.03), turned 4° from how it started; touching block4_geom
1.00 s: pusher at 0.890 m, still; touching nothing | block1 at (0.13, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.12, 0.00, 0.31) m, at rest, turned 5° from how it started; touching block1_geom, block3_geom | block3 at (0.14, 0.00, 0.51) m, moving 0.08 m/s (vx +0.07, vy -0.00, vz +0.02), turned 5° from how it started; touching block2_geom, block4_geom | block4 at (0.16, 0.00, 0.71) m, moving 0.12 m/s (vx +0.12, vy -0.00, vz +0.02), turned 5° from how it started; touching block3_geom, block5_geom | block5 at (0.17, 0.00, 0.91) m, moving 0.17 m/s (vx +0.17, vy -0.00, vz +0.01), turned 5° from how it started; touching block4_geom
1.25 s: pusher at 0.888 m, still; touching nothing | block1 at (0.13, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.12, 0.00, 0.30) m, moving 0.11 m/s (vx -0.07, vy -0.00, vz -0.08), turned 2° from how it started; touching block1_geom, block3_geom | block3 at (0.12, 0.00, 0.50) m, moving 0.22 m/s (vx -0.20, vy -0.00, vz -0.08), turned 2° from how it started; touching block2_geom, block4_geom | block4 at (0.13, 0.00, 0.70) m, moving 0.35 m/s (vx -0.34, vy -0.00, vz -0.07), turned 2° from how it started; touching block3_geom, block5_geom | block5 at (0.14, 0.00, 0.90) m, moving 0.48 m/s (vx -0.48, vy -0.00, vz -0.06), turned 2° from how it started; touching block4_geom
1.50 s: pusher at 0.884 m, moving -0.03 m/s; touching nothing | block1 at (0.13, 0.00, 0.11) m, at rest, turned 3° from how it started; touching block2_geom, floor | block2 at (0.09, 0.00, 0.30) m, at rest, turned 3° from how it started; touching block1_geom, block3_geom | block3 at (0.08, 0.00, 0.50) m, at rest, turned 3° from how it started; touching block2_geom, block4_geom | block4 at (0.07, 0.00, 0.70) m, at rest, turned 3° from how it started; touching block3_geom, block5_geom | block5 at (0.06, 0.00, 0.90) m, at rest, turned 3° from how it started; touching block4_geom
1.75 s: pusher at 0.876 m, moving -0.03 m/s; touching nothing | block1 at (0.13, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.11, 0.00, 0.30) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz +0.03); touching block1_geom, block3_geom | block3 at (0.11, 0.00, 0.50) m, moving 0.20 m/s (vx +0.19, vy +0.00, vz +0.03); touching block2_geom, block4_geom | block4 at (0.11, 0.00, 0.70) m, moving 0.30 m/s (vx +0.30, vy +0.00, vz +0.03); touching block3_geom, block5_geom | block5 at (0.11, 0.00, 0.90) m, moving 0.41 m/s (vx +0.41, vy -0.00, vz +0.02); touching block4_geom
2.00 s: pusher at 0.870 m, moving -0.02 m/s; touching nothing | block1 at (0.13, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.11, 0.00, 0.30) m, moving 0.06 m/s (vx -0.05, vy +0.00, vz +0.02); touching block1_geom, block3_geom | block3 at (0.11, 0.00, 0.50) m, moving 0.14 m/s (vx -0.13, vy +0.00, vz +0.01); touching block2_geom, block4_geom | block4 at (0.11, 0.00, 0.70) m, moving 0.23 m/s (vx -0.23, vy +0.00, vz +0.01); touching block3_geom, block5_geom | block5 at (0.11, 0.00, 0.90) m, moving 0.33 m/s (vx -0.33, vy +0.00, vz +0.01); touching block4_geom
2.25 s: pusher at 0.866 m, moving -0.02 m/s; touching nothing | block1 at (0.13, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.11, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.11, 0.00, 0.50) m, moving 0.09 m/s (vx +0.08, vy -0.00, vz +0.02); touching block2_geom, block4_geom | block4 at (0.11, 0.00, 0.70) m, moving 0.15 m/s (vx +0.15, vy -0.00, vz +0.02); touching block3_geom, block5_geom | block5 at (0.11, 0.00, 0.90) m, moving 0.21 m/s (vx +0.21, vy -0.00, vz +0.02); touching block4_geom
2.50 s: pusher at 0.862 m, moving -0.01 m/s; touching nothing | block1 at (0.13, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.11, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.11, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.11, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (0.11, 0.00, 0.90) m, at rest; touching block4_geom
2.75 s: pusher at 0.860 m, still; touching nothing | block1 at (0.13, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.11, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.11, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.11, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (0.11, 0.00, 0.90) m, at rest; touching block4_geom
3.00 s: pusher at 0.858 m, still; touching nothing | block1 at (0.13, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.11, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.11, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.11, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (0.11, 0.00, 0.90) m, at rest; touching block4_geom
3.25 s: pusher at 0.856 m, still; touching nothing | block1 at (0.13, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.11, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.11, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.11, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (0.11, 0.00, 0.90) m, at rest; touching block4_geom
3.50 s: pusher at 0.855 m, still; touching nothing | block1 at (0.13, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.11, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.11, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.11, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (0.11, 0.00, 0.90) m, at rest; touching block4_geom
3.75 s: pusher at 0.854 m, still; touching nothing | block1 at (0.13, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.11, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.11, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.11, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (0.11, 0.00, 0.90) m, at rest; touching block4_geom
4.00 s: pusher at 0.853 m, still; touching nothing | block1 at (0.13, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.11, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.11, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.11, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (0.11, 0.00, 0.90) m, at rest; touching block4_geom
4.25 s: pusher at 0.852 m, still; touching nothing | block1 at (0.13, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.11, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.11, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.11, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (0.11, 0.00, 0.90) m, at rest; touching block4_geom
(the same through 4.50 s)
4.75 s: pusher at 0.851 m, still; touching nothing | block1 at (0.13, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.11, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.11, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.11, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (0.11, 0.00, 0.90) m, at rest; touching block4_geom
(the same through 5.50 s)
5.75 s: pusher at 0.850 m, still; touching nothing | block1 at (0.13, 0.00, 0.10) m, at rest; touching block2_geom, floor | block2 at (0.11, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom | block3 at (0.11, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom | block4 at (0.11, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom | block5 at (0.11, 0.00, 0.90) m, at rest; touching block4_geom
(the same through 6.00 s)

At the end (6.00 s):
- pusher at 0.850 m, still; touching nothing
- block1 at (0.13, 0.00, 0.10) m, at rest; touching block2_geom, floor
- block2 at (0.11, 0.00, 0.30) m, at rest; touching block1_geom, block3_geom
- block3 at (0.11, 0.00, 0.50) m, at rest; touching block2_geom, block4_geom
- block4 at (0.11, 0.00, 0.70) m, at rest; touching block3_geom, block5_geom
- block5 at (0.11, 0.00, 0.90) m, at rest; touching block4_geom
</history>
