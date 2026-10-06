Your expectations, checked against the run (3 of 4 hold):

- holds: pusher touches block1 (first touch at 1.00 s)
- holds: block5 touches floor (first touch at 1.58 s)
- holds: block4 touches floor (first touch at 1.57 s)
- DOES NOT HOLD: block5 comes to rest (I can't read this; the forms are: <thing> touches <thing>; <thing> comes to rest in <thing>; <thing> drops through <thing>; <thing> reaches its lower stop; <thing> reaches its upper stop)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pusher: slide joint pusher_slide about axis (1.00, 0.00, 0.00), no range limit; its geoms: pusher_paddle; starts at 0.000 m, moving +0.50 m/s
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
 0.01 s  block3 starts moving
 0.01 s  block4 starts moving
 0.01 s  block5 starts moving
 0.01 s  block4_geom first touches block5_geom
 1.00 s  pusher_paddle first touches block1_geom
 1.00 s  block1 starts moving
 1.04 s  block2 starts moving
 1.21 s  pusher_paddle leaves block1_geom
 1.36 s  block1_geom leaves block2_geom
 1.37 s  pusher_paddle first touches block2_geom
 1.41 s  pusher passes 0.26 m from block5 (block5_geom) without touching it: nearest points (0.05, -0.05, 0.04) m and (-0.10, -0.05, 0.26) m
 1.44 s  block2_geom leaves block3_geom
 1.44 s  block3_geom leaves block4_geom
 1.44 s  block4_geom leaves block5_geom
 1.46 s  pusher passes 0.16 m from block4 (block4_geom) without touching it: nearest points (0.08, -0.05, 0.04) m and (-0.04, -0.05, 0.15) m
 1.50 s  pusher passes 0.06 m from block3 (block3_geom) without touching it: nearest points (0.10, -0.05, 0.04) m and (0.05, -0.05, 0.06) m
 1.56 s  block3_geom first touches floor
 1.57 s  block4_geom first touches floor
 1.58 s  block5_geom first touches floor
 1.59 s  pusher_paddle leaves block2_geom
 1.60 s  block2_geom touches block3_geom again
 1.61 s  block2_geom leaves block3_geom
 1.63 s  pusher_paddle touches block2_geom again
 1.64 s  block2_geom first touches floor
 1.64 s  pusher_paddle leaves block2_geom
 1.64 s  block3 comes to rest at (0.00, 0.00, 0.05) m
 1.67 s  block4 comes to rest at (-0.13, 0.00, 0.05) m
 1.68 s  block5 comes to rest at (-0.27, 0.00, 0.05) m
 1.72 s  block2_geom touches block3_geom again
 1.90 s  block2_geom leaves block3_geom
 1.96 s  block2_geom touches block3_geom again
 2.00 s  block2_geom leaves block3_geom
 2.00 s  block2 comes to rest at (0.10, 0.00, 0.05) m
 2.93 s  pusher_paddle touches block1_geom again
 3.07 s  pusher_paddle leaves block1_geom
 3.13 s  pusher_paddle touches block1_geom again
 4.95 s  pusher_paddle leaves block1_geom
 4.98 s  pusher_paddle touches block1_geom again
 5.03 s  pusher_paddle leaves block1_geom
 5.07 s  pusher_paddle touches block1_geom 1 more times between 5.07 s and 6.00 s
 6.00 s  pusher is at its largest, 3.0 m
 6.00 s  block1 is still moving at the end, 0.50 m/s

State every 0.25 s:
0.00 s: pusher at 0.000 m, moving +0.50 m/s; touching nothing | block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching nothing
0.25 s: pusher at 0.125 m, moving +0.50 m/s; touching nothing | block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
0.50 s: pusher at 0.250 m, moving +0.50 m/s; touching nothing | block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
0.75 s: pusher at 0.375 m, moving +0.50 m/s; touching nothing | block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
1.00 s: pusher at 0.500 m, moving +0.50 m/s; touching nothing | block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
1.25 s: pusher at 0.623 m, moving +0.50 m/s; touching nothing | block1 at (0.12, 0.00, 0.05) m, moving 0.54 m/s (vx +0.54, vy +0.00, vz +0.00); touching block2_geom, floor | block2 at (0.04, 0.00, 0.14) m, moving 0.43 m/s (vx +0.41, vy +0.00, vz -0.09), turned 9° from how it started; touching block1_geom, block3_geom | block3 at (0.02, 0.00, 0.24) m, moving 0.21 m/s (vx +0.17, vy -0.00, vz -0.13), turned 9° from how it started; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.34) m, moving 0.18 m/s (vx -0.07, vy -0.00, vz -0.17), turned 9° from how it started; touching block3_geom, block5_geom | block5 at (-0.01, 0.00, 0.44) m, moving 0.38 m/s (vx -0.32, vy -0.00, vz -0.21), turned 9° from how it started; touching block4_geom
1.50 s: pusher at 0.750 m, moving +0.50 m/s; touching block2_geom | block1 at (0.32, 0.00, 0.05) m, moving 0.81 m/s (vx +0.81, vy +0.00, vz -0.01), turned 1° from how it started; touching floor | block2 at (0.12, 0.00, 0.11) m, moving 0.23 m/s (vx +0.07, vy -0.00, vz -0.22), turned 72° from how it started; touching pusher_paddle | block3 at (0.02, 0.00, 0.13) m, moving 1.05 m/s (vx -0.21, vy -0.00, vz -1.03), turned 69° from how it started; touching nothing | block4 at (-0.08, 0.00, 0.17) m, moving 1.51 m/s (vx -0.58, vy -0.00, vz -1.39), turned 71° from how it started; touching nothing | block5 at (-0.19, 0.00, 0.22) m, moving 1.96 m/s (vx -0.96, vy +0.00, vz -1.71), turned 71° from how it started; touching nothing
1.75 s: pusher at 0.875 m, moving +0.50 m/s; touching nothing | block1 at (0.51, 0.00, 0.05) m, moving 0.69 m/s (vx +0.69, vy +0.00, vz +0.01), turned 4° from how it started; touching floor | block2 at (0.12, 0.00, 0.07) m, moving 0.06 m/s (vx -0.04, vy -0.02, vz -0.04), turned 152° from how it started; touching block3_geom, floor | block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2_geom, floor | block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
2.00 s: pusher at 1.000 m, moving +0.50 m/s; touching nothing | block1 at (0.66, 0.00, 0.05) m, moving 0.57 m/s (vx +0.57, vy +0.00, vz +0.01), turned 7° from how it started; touching floor | block2 at (0.10, 0.00, 0.05) m, at rest, turned 179° from how it started; touching block3_geom, floor | block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching block2_geom, floor | block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
2.25 s: pusher at 1.125 m, moving +0.50 m/s; touching nothing | block1 at (0.79, 0.00, 0.05) m, moving 0.44 m/s (vx +0.44, vy +0.00, vz +0.00), turned 10° from how it started; touching floor | block2 at (0.10, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
2.50 s: pusher at 1.250 m, moving +0.50 m/s; touching nothing | block1 at (0.88, 0.00, 0.05) m, moving 0.32 m/s (vx +0.32, vy +0.00, vz +0.01), turned 12° from how it started; touching floor | block2 at (0.10, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
2.75 s: pusher at 1.375 m, moving +0.50 m/s; touching nothing | block1 at (0.95, 0.00, 0.05) m, moving 0.20 m/s (vx +0.20, vy +0.00, vz +0.01), turned 15° from how it started; touching floor | block2 at (0.10, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
3.00 s: pusher at 1.500 m, moving +0.50 m/s; touching nothing | block1 at (1.00, 0.00, 0.05) m, moving 0.37 m/s (vx +0.37, vy +0.01, vz -0.01), turned 1° from how it started; touching floor | block2 at (0.10, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
3.25 s: pusher at 1.624 m, moving +0.50 m/s; touching block1_geom | block1 at (1.12, 0.00, 0.05) m, moving 0.50 m/s (vx +0.50, vy +0.01, vz +0.00); touching floor, pusher_paddle | block2 at (0.10, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
3.50 s: pusher at 1.749 m, moving +0.50 m/s; touching block1_geom | block1 at (1.25, 0.01, 0.05) m, moving 0.50 m/s (vx +0.50, vy +0.01, vz +0.01); touching floor, pusher_paddle | block2 at (0.10, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
3.75 s: pusher at 1.874 m, moving +0.50 m/s; touching block1_geom | block1 at (1.37, 0.01, 0.05) m, moving 0.50 m/s (vx +0.50, vy +0.01, vz -0.00); touching floor, pusher_paddle | block2 at (0.10, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
4.00 s: pusher at 1.999 m, moving +0.50 m/s; touching block1_geom | block1 at (1.50, 0.01, 0.05) m, moving 0.50 m/s (vx +0.50, vy +0.01, vz +0.01); touching floor, pusher_paddle | block2 at (0.10, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
4.25 s: pusher at 2.124 m, moving +0.50 m/s; touching block1_geom | block1 at (1.62, 0.01, 0.05) m, moving 0.50 m/s (vx +0.50, vy +0.01, vz -0.00); touching floor, pusher_paddle | block2 at (0.10, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
4.50 s: pusher at 2.249 m, moving +0.50 m/s; touching nothing | block1 at (1.75, 0.02, 0.05) m, moving 0.50 m/s (vx +0.50, vy +0.01, vz -0.00); touching floor | block2 at (0.10, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
4.75 s: pusher at 2.373 m, moving +0.50 m/s; touching block1_geom | block1 at (1.87, 0.02, 0.05) m, moving 0.50 m/s (vx +0.50, vy +0.01, vz +0.01); touching floor, pusher_paddle | block2 at (0.10, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
5.00 s: pusher at 2.498 m, moving +0.50 m/s; touching block1_geom | block1 at (2.00, 0.02, 0.05) m, moving 0.50 m/s (vx +0.50, vy +0.01, vz -0.01); touching floor, pusher_paddle | block2 at (0.10, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
5.25 s: pusher at 2.623 m, moving +0.50 m/s; touching block1_geom | block1 at (2.12, 0.02, 0.05) m, moving 0.50 m/s (vx +0.50, vy +0.01, vz -0.01); touching floor, pusher_paddle | block2 at (0.10, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
5.50 s: pusher at 2.748 m, moving +0.50 m/s; touching block1_geom | block1 at (2.25, 0.02, 0.05) m, moving 0.50 m/s (vx +0.50, vy +0.01, vz -0.00); touching floor, pusher_paddle | block2 at (0.10, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
5.75 s: pusher at 2.873 m, moving +0.50 m/s; touching block1_geom | block1 at (2.37, 0.03, 0.05) m, moving 0.50 m/s (vx +0.50, vy +0.01, vz -0.01); touching floor, pusher_paddle | block2 at (0.10, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
6.00 s: pusher at 2.997 m, moving +0.50 m/s; touching nothing | block1 at (2.50, 0.03, 0.05) m, moving 0.50 m/s (vx +0.50, vy +0.01, vz +0.01); touching floor | block2 at (0.10, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor | block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor

At the end (6.00 s):
- pusher at 2.997 m, moving +0.50 m/s; touching nothing
- block1 at (2.50, 0.03, 0.05) m, moving 0.50 m/s (vx +0.50, vy +0.01, vz +0.01); touching floor
- block2 at (0.10, 0.00, 0.05) m, at rest, turned 180° from how it started; touching floor
- block3 at (0.00, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- block4 at (-0.13, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- block5 at (-0.27, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
</history>
