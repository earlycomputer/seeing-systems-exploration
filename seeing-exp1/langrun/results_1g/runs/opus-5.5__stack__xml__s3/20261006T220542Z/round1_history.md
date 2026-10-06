Your expectations, checked against the run (2 of 3 hold):

- holds: pusher touches block1 (first touch at 0.18 s)
- DOES NOT HOLD: block5 touches floor (they never touch)
- holds: block4 touches floor (first touch at 0.63 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pusher: slide joint pusher_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.74 m as MuJoCo applies it; its geoms: pusher_geom; starts at 0.000 m, moving +4.00 m/s
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
 0.18 s  block1_geom leaves floor
 0.18 s  pusher_geom first touches block1_geom
 0.18 s  block1 starts moving
 0.18 s  block2 starts moving
 0.18 s  block1_geom leaves block2_geom
 0.18 s  pusher passes 0.03 m from block2 (block2_geom) without touching it: nearest points (-0.05, 0.00, 0.07) m and (-0.05, 0.00, 0.10) m
 0.19 s  pusher reaches its upper stop (0.74 m) moving +3.73 m/s
 0.20 s  block4_geom leaves block5_geom
 0.20 s  block2_geom leaves block3_geom
 0.20 s  pusher_geom leaves block1_geom
 0.20 s  pusher is at its largest, 0.8 m
 0.21 s  block3_geom leaves block4_geom
 0.22 s  block1_geom touches floor again
 0.23 s  block1_geom leaves floor
 0.23 s  block2 is at the top of its flight, at (0.03, 0.00, 0.16) m
 0.23 s  block3 is at the top of its flight, at (0.02, 0.00, 0.26) m
 0.23 s  block4 is at the top of its flight, at (0.01, 0.00, 0.36) m
 0.23 s  block5 is at the top of its flight, at (0.00, 0.00, 0.46) m
 0.25 s  pusher reaches its upper stop (0.74 m) again moving -0.44 m/s
 0.30 s  block1_geom touches floor again
 0.33 s  block1_geom leaves floor
 0.35 s  pusher passes 0.11 m from block3 (block3_geom) without touching it: nearest points (-0.05, 0.00, 0.07) m and (0.04, 0.00, 0.13) m
 0.38 s  block2_geom first touches floor
 0.38 s  block1_geom touches floor again
 0.39 s  block2_geom touches block3_geom again
 0.40 s  block3_geom touches block4_geom again
 0.41 s  block4_geom touches block5_geom again
 0.42 s  block1_geom leaves floor
 0.46 s  block2_geom leaves floor
 0.47 s  block2_geom leaves block3_geom
 0.47 s  block3_geom leaves block4_geom
 0.47 s  block4_geom leaves block5_geom
 0.51 s  block2_geom touches floor again
 0.51 s  block1_geom touches floor 3 more times between 0.51 s and 6.00 s, still touching at the end
 0.53 s  block2_geom touches block3_geom again
 0.55 s  block2_geom leaves block3_geom
 0.58 s  block2 comes to rest at (0.20, 0.00, 0.05) m
 0.58 s  pusher passes 0.08 m from block4 (block4_geom) without touching it: nearest points (-0.15, 0.00, 0.07) m and (-0.07, 0.00, 0.09) m
 0.61 s  pusher_geom first touches block5_geom
 0.63 s  block4_geom first touches floor
 0.65 s  block3_geom first touches floor
 0.69 s  block2_geom touches block3_geom again
 0.72 s  block4 comes to rest at (-0.03, 0.00, 0.05) m
 0.72 s  block3 comes to rest at (0.10, 0.00, 0.05) m
 0.74 s  block2_geom leaves block3_geom
 0.76 s  block1 comes to rest at (0.86, 0.00, 0.05) m
 1.88 s  pusher reaches its lower stop (0 m) again moving -0.46 m/s
 1.91 s  pusher is at its smallest, -0.0 m
 1.98 s  block5 comes to rest at (-0.79, 0.00, 0.12) m

State every 0.25 s:
0.00 s: pusher at 0.000 m, moving +4.00 m/s; touching nothing | block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching nothing
0.25 s: pusher at 0.746 m, moving -0.44 m/s; touching nothing | block1 at (0.19, 0.00, 0.06) m, moving 2.47 m/s (vx +2.46, vy -0.00, vz +0.20), turned 1° from how it started; touching nothing | block2 at (0.04, 0.00, 0.16) m, moving 0.63 m/s (vx +0.61, vy +0.00, vz -0.17), turned 9° from how it started; touching nothing | block3 at (0.03, 0.00, 0.26) m, moving 0.41 m/s (vx +0.38, vy +0.00, vz -0.17), turned 9° from how it started; touching nothing | block4 at (0.01, 0.00, 0.36) m, moving 0.24 m/s (vx +0.17, vy +0.00, vz -0.17), turned 9° from how it started; touching nothing | block5 at (0.00, 0.00, 0.46) m, moving 0.18 m/s (vx -0.04, vy +0.00, vz -0.17), turned 9° from how it started; touching nothing
0.50 s: pusher at 0.636 m, moving -0.44 m/s; touching nothing | block1 at (0.67, 0.00, 0.06) m, moving 1.57 m/s (vx +1.52, vy +0.00, vz -0.38); touching nothing | block2 at (0.18, 0.00, 0.05) m, moving 0.47 m/s (vx +0.43, vy -0.00, vz -0.20); touching nothing | block3 at (0.10, 0.00, 0.15) m, moving 0.28 m/s (vx +0.11, vy -0.00, vz -0.26), turned 53° from how it started; touching nothing | block4 at (0.01, 0.00, 0.21) m, moving 0.63 m/s (vx -0.35, vy -0.00, vz -0.52), turned 56° from how it started; touching nothing | block5 at (-0.08, 0.00, 0.26) m, moving 1.16 m/s (vx -0.89, vy +0.00, vz -0.74), turned 56° from how it started; touching nothing
0.75 s: pusher at 0.523 m, moving -0.46 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz +0.02); touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.24, 0.00, 0.12) m, moving 0.46 m/s (vx -0.46, vy -0.00, vz +0.01), turned 90° from how it started; touching pusher_geom
1.00 s: pusher at 0.408 m, moving -0.46 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.36, 0.00, 0.12) m, moving 0.46 m/s (vx -0.46, vy +0.00, vz +0.00), turned 90° from how it started; touching pusher_geom
1.25 s: pusher at 0.294 m, moving -0.46 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.47, 0.00, 0.12) m, moving 0.46 m/s (vx -0.46, vy +0.00, vz +0.00), turned 90° from how it started; touching pusher_geom
1.50 s: pusher at 0.179 m, moving -0.46 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.59, 0.00, 0.12) m, moving 0.46 m/s (vx -0.46, vy +0.00, vz -0.00), turned 90° from how it started; touching pusher_geom
1.75 s: pusher at 0.064 m, moving -0.46 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.70, 0.00, 0.12) m, moving 0.46 m/s (vx -0.46, vy +0.00, vz -0.00), turned 90° from how it started; touching pusher_geom
2.00 s: pusher at 0.002 m, moving +0.05 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.79, 0.00, 0.12) m, at rest, turned 90° from how it started; touching pusher_geom
2.25 s: pusher at 0.013 m, moving +0.05 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.78, 0.00, 0.12) m, at rest, turned 90° from how it started; touching pusher_geom
2.50 s: pusher at 0.025 m, moving +0.05 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.76, 0.00, 0.12) m, at rest, turned 90° from how it started; touching pusher_geom
2.75 s: pusher at 0.036 m, moving +0.05 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.75, 0.00, 0.12) m, at rest, turned 90° from how it started; touching pusher_geom
3.00 s: pusher at 0.048 m, moving +0.05 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.74, 0.00, 0.12) m, at rest, turned 90° from how it started; touching pusher_geom
3.25 s: pusher at 0.059 m, moving +0.05 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.73, 0.00, 0.12) m, at rest, turned 90° from how it started; touching pusher_geom
3.50 s: pusher at 0.071 m, moving +0.05 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.72, 0.00, 0.12) m, at rest, turned 90° from how it started; touching pusher_geom
3.75 s: pusher at 0.082 m, moving +0.05 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.71, 0.00, 0.12) m, at rest, turned 90° from how it started; touching pusher_geom
4.00 s: pusher at 0.093 m, moving +0.05 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.70, 0.00, 0.12) m, at rest, turned 90° from how it started; touching pusher_geom
4.25 s: pusher at 0.105 m, moving +0.05 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.68, 0.00, 0.12) m, at rest, turned 90° from how it started; touching pusher_geom
4.50 s: pusher at 0.116 m, moving +0.05 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.67, 0.00, 0.12) m, at rest, turned 90° from how it started; touching pusher_geom
4.75 s: pusher at 0.128 m, moving +0.05 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.66, 0.00, 0.12) m, at rest, turned 90° from how it started; touching pusher_geom
5.00 s: pusher at 0.139 m, moving +0.05 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.65, 0.00, 0.12) m, at rest, turned 90° from how it started; touching pusher_geom
5.25 s: pusher at 0.151 m, moving +0.05 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.64, 0.00, 0.12) m, at rest, turned 90° from how it started; touching pusher_geom
5.50 s: pusher at 0.162 m, moving +0.05 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.63, 0.00, 0.12) m, at rest, turned 90° from how it started; touching pusher_geom
5.75 s: pusher at 0.174 m, moving +0.05 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.61, 0.00, 0.12) m, at rest, turned 90° from how it started; touching pusher_geom
6.00 s: pusher at 0.185 m, moving +0.05 m/s; touching block5_geom | block1 at (0.86, 0.00, 0.05) m, at rest; touching floor | block2 at (0.20, 0.00, 0.05) m, at rest; touching floor | block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.60, 0.00, 0.12) m, at rest, turned 90° from how it started; touching pusher_geom

At the end (6.00 s):
- pusher at 0.185 m, moving +0.05 m/s; touching block5_geom
- block1 at (0.86, 0.00, 0.05) m, at rest; touching floor
- block2 at (0.20, 0.00, 0.05) m, at rest; touching floor
- block3 at (0.10, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- block4 at (-0.03, 0.00, 0.05) m, at rest, turned 90° from how it started; touching floor
- block5 at (-0.60, 0.00, 0.12) m, at rest, turned 90° from how it started; touching pusher_geom
</history>
