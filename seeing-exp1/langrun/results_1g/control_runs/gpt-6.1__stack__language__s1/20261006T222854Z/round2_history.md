MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1; starts at (1.80, 0.00, 0.10) m, at rest
- block2: free body; its geoms: block2; starts at (1.80, 0.00, 0.30) m, at rest
- block3: free body; its geoms: block3; starts at (1.80, 0.00, 0.50) m, at rest
- block4: free body; its geoms: block4; starts at (1.80, 0.00, 0.70) m, at rest
- block5: free body; its geoms: block5; starts at (1.80, 0.00, 0.90) m, at rest
- pusher: free body; its geoms: pusher; starts at (0.00, 0.00, 0.08) m, moving 3.00 m/s (vx +3.00, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  block1 starts touching floor
 0.00 s  block1 starts touching block2
 0.00 s  block3 starts touching block4
 0.00 s  pusher starts touching floor
 0.00 s  block2 starts touching block3
 0.01 s  block5 starts moving
 0.01 s  block4 first touches block5
 0.54 s  pusher leaves floor
 0.54 s  block4 passes 0.45 m from pusher without touching it: nearest points (1.70, 0.00, 0.60) m and (1.63, 0.00, 0.16) m
 0.54 s  block1 first touches pusher
 0.54 s  block1 starts moving
 0.54 s  block2 starts moving
 0.54 s  block3 starts moving
 0.54 s  block4 starts moving
 0.55 s  block1 leaves block2
 0.55 s  block1 leaves floor
 0.55 s  block2 leaves block3
 0.55 s  block4 leaves block5
 0.55 s  block1 leaves pusher
 0.56 s  block3 leaves block4
 0.58 s  pusher touches floor again
 0.61 s  block1 touches floor again
 0.61 s  block1 leaves floor
 0.62 s  block2 is at the top of its flight, at (1.86, 0.00, 0.33) m
 0.63 s  block3 is at the top of its flight, at (1.84, 0.00, 0.53) m
 0.63 s  block4 is at the top of its flight, at (1.82, 0.00, 0.73) m
 0.63 s  block5 is at the top of its flight, at (1.79, 0.00, 0.93) m
 0.67 s  block1 is at the top of its flight, at (2.24, 0.00, 0.13) m
 0.74 s  block1 touches floor again
 0.76 s  block1 leaves floor
 0.77 s  block2 passes 0.03 m from pusher without touching it: nearest points (2.13, 0.00, 0.17) m and (2.15, 0.00, 0.14) m
 0.79 s  block3 passes 0.25 m from pusher without touching it: nearest points (2.05, 0.00, 0.34) m and (2.20, 0.00, 0.14) m
 0.79 s  block1 touches floor again
 0.81 s  block1 leaves floor
 0.82 s  block2 first touches floor
 0.85 s  block2 touches block3 again
 0.86 s  block3 touches block4 again
 0.87 s  block4 touches block5 again
 0.88 s  block1 touches floor 47 more times between 0.88 s and 6.00 s, still touching at the end
 0.90 s  block4 leaves block5
 0.99 s  block4 touches block5 again
 1.14 s  block4 leaves block5
 1.18 s  block2 leaves block3
 1.18 s  block3 leaves block4
 1.25 s  block3 first touches floor
 1.26 s  block1 touches pusher again
 1.26 s  block3 touches block4 again
 1.27 s  block1 leaves pusher
 1.28 s  block4 first touches floor
 1.28 s  block3 leaves block4
 1.28 s  block4 touches block5 again
 1.29 s  block4 leaves block5
 1.29 s  block5 first touches floor
 1.32 s  block3 leaves floor
 1.32 s  block4 leaves floor
 1.34 s  block5 leaves floor
 1.36 s  block1 is at the top of its flight, at (3.92, 0.00, 0.14) m
 1.37 s  block3 touches floor again
 1.38 s  block4 touches floor again
 1.40 s  block2 comes to rest at (1.90, 0.00, 0.10) m
 1.42 s  block5 touches floor again
 1.43 s  block3 comes to rest at (1.65, 0.00, 0.10) m
 1.46 s  block4 comes to rest at (1.42, 0.00, 0.10) m
 1.55 s  block5 comes to rest at (1.12, 0.02, 0.10) m
 1.62 s  block1 is at the top of its flight, at (4.62, 0.00, 0.12) m
 1.91 s  block1 touches pusher again
 1.92 s  block1 leaves pusher
 2.10 s  block1 is at the top of its flight, at (5.58, 0.00, 0.13) m
 2.25 s  block1 is at the top of its flight, at (5.89, 0.00, 0.12) m
 2.46 s  block1 touches pusher again
 2.47 s  block1 leaves pusher
 2.93 s  block1 touches pusher 24 more times between 2.93 s and 5.99 s
 6.00 s  block1 is still moving at the end, 0.85 m/s
 6.00 s  pusher is still moving at the end, 0.72 m/s

State every 0.25 s:
0.00 s: block1 at (1.80, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (1.80, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (1.80, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (1.80, 0.00, 0.70) m, at rest; touching block3 | block5 at (1.80, 0.00, 0.90) m, at rest; touching nothing | pusher at (0.00, 0.00, 0.08) m, moving 3.00 m/s (vx +3.00, vy +0.00, vz +0.00); touching floor
0.25 s: block1 at (1.80, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (1.80, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (1.80, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (1.80, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (1.80, 0.00, 0.90) m, at rest; touching block4 | pusher at (0.74, 0.00, 0.08) m, moving 3.00 m/s (vx +3.00, vy -0.00, vz +0.02); touching floor
0.50 s: block1 at (1.80, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (1.80, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (1.80, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (1.80, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (1.80, 0.00, 0.90) m, at rest; touching block4 | pusher at (1.49, 0.00, 0.08) m, moving 2.98 m/s (vx +2.98, vy -0.00, vz +0.01); touching floor
0.75 s: block1 at (2.53, 0.00, 0.10) m, moving 3.22 m/s (vx +3.22, vy +0.00, vz -0.10); touching nothing | block2 at (1.98, 0.00, 0.24) m, moving 1.55 m/s (vx +0.86, vy +0.00, vz -1.29), turned 25° from how it started; touching nothing | block3 at (1.90, 0.00, 0.46) m, moving 1.31 m/s (vx +0.48, vy +0.00, vz -1.22), turned 17° from how it started; touching nothing | block4 at (1.84, 0.00, 0.66) m, moving 1.24 m/s (vx +0.19, vy +0.00, vz -1.22), turned 17° from how it started; touching nothing | block5 at (1.78, 0.00, 0.86) m, moving 1.23 m/s (vx -0.09, vy +0.00, vz -1.22), turned 17° from how it started; touching nothing | pusher at (2.14, 0.00, 0.08) m, moving 2.51 m/s (vx +2.51, vy -0.00, vz +0.01); touching floor
1.00 s: block1 at (3.19, 0.00, 0.11) m, moving 2.20 m/s (vx +2.18, vy +0.00, vz -0.25), turned 3° from how it started; touching nothing | block2 at (2.05, 0.00, 0.14) m, moving 0.15 m/s (vx -0.14, vy +0.00, vz +0.05), turned 29° from how it started; touching block3, floor | block3 at (1.90, 0.00, 0.29) m, moving 0.46 m/s (vx -0.44, vy -0.00, vz -0.13), turned 35° from how it started; touching block2, block4 | block4 at (1.78, 0.00, 0.45) m, moving 0.88 m/s (vx -0.79, vy +0.00, vz -0.41), turned 35° from how it started; touching block3, block5 | block5 at (1.66, 0.00, 0.61) m, moving 1.17 m/s (vx -0.92, vy +0.00, vz -0.72), turned 37° from how it started; touching block4 | pusher at (2.77, 0.00, 0.08) m, moving 2.49 m/s (vx +2.49, vy -0.00, vz +0.00); touching floor
1.25 s: block1 at (3.57, 0.00, 0.10) m, moving 1.00 m/s (vx +1.00, vy +0.00, vz -0.06); touching nothing | block2 at (1.97, 0.00, 0.13) m, moving 0.56 m/s (vx -0.53, vy -0.00, vz -0.20), turned 66° from how it started; touching floor | block3 at (1.74, 0.00, 0.13) m, moving 1.78 m/s (vx -0.77, vy +0.00, vz -1.60), turned 73° from how it started; touching nothing | block4 at (1.54, 0.00, 0.17) m, moving 2.41 m/s (vx -1.06, vy +0.00, vz -2.16), turned 73° from how it started; touching nothing | block5 at (1.34, 0.00, 0.23) m, moving 2.97 m/s (vx -1.35, vy -0.01, vz -2.65), turned 72° from how it started; touching nothing | pusher at (3.38, 0.00, 0.08) m, moving 2.46 m/s (vx +2.46, vy -0.00, vz +0.02); touching floor
1.50 s: block1 at (4.33, 0.00, 0.12) m, moving 2.78 m/s (vx +2.76, vy +0.00, vz -0.27), turned 1° from how it started; touching nothing | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.13, 0.01, 0.10) m, moving 0.29 m/s (vx -0.27, vy +0.07, vz -0.09), turned 89° from how it started; touching floor | pusher at (3.96, 0.00, 0.08) m, moving 2.27 m/s (vx +2.27, vy -0.00, vz +0.01); touching floor
1.75 s: block1 at (4.86, 0.00, 0.11) m, moving 1.52 m/s (vx +1.52, vy +0.00, vz +0.04); touching nothing | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (4.52, 0.00, 0.08) m, moving 2.25 m/s (vx +2.25, vy -0.00, vz -0.02); touching nothing
2.00 s: block1 at (5.31, 0.00, 0.13) m, moving 2.83 m/s (vx +2.83, vy -0.00, vz +0.11), turned 9° from how it started; touching nothing | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (5.06, 0.00, 0.08) m, moving 2.07 m/s (vx +2.07, vy +0.00, vz -0.02); touching nothing
2.25 s: block1 at (5.90, 0.00, 0.12) m, moving 1.79 m/s (vx +1.79, vy -0.00, vz -0.02); touching nothing | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (5.58, 0.00, 0.08) m, moving 2.05 m/s (vx +2.05, vy +0.00, vz +0.01); touching floor
2.50 s: block1 at (6.29, 0.00, 0.11) m, moving 2.76 m/s (vx +2.76, vy +0.00, vz -0.03), turned 3° from how it started; touching nothing | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (6.08, 0.00, 0.08) m, moving 1.89 m/s (vx +1.89, vy -0.00, vz -0.01); touching nothing
2.75 s: block1 at (6.84, 0.00, 0.11) m, moving 1.83 m/s (vx +1.80, vy +0.00, vz -0.36), turned 4° from how it started; touching nothing | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (6.55, 0.00, 0.08) m, moving 1.87 m/s (vx +1.87, vy -0.00, vz +0.00); touching floor
3.00 s: block1 at (7.23, 0.00, 0.11) m, moving 2.31 m/s (vx +2.30, vy -0.00, vz +0.12), turned 5° from how it started; touching nothing | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (7.01, 0.00, 0.08) m, moving 1.73 m/s (vx +1.73, vy +0.00, vz -0.01); touching nothing
3.25 s: block1 at (7.69, 0.00, 0.10) m, moving 1.17 m/s (vx +1.15, vy -0.00, vz +0.24); touching nothing | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (7.44, 0.00, 0.08) m, moving 1.71 m/s (vx +1.71, vy +0.00, vz +0.01); touching floor
3.50 s: block1 at (8.04, 0.00, 0.10) m, moving 1.76 m/s (vx +1.75, vy -0.00, vz -0.24); touching nothing | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (7.86, 0.00, 0.08) m, moving 1.59 m/s (vx +1.59, vy +0.00, vz +0.01); touching floor
3.75 s: block1 at (8.44, 0.00, 0.10) m, moving 1.56 m/s (vx +1.56, vy -0.00, vz -0.07); touching nothing | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (8.24, 0.00, 0.08) m, moving 1.51 m/s (vx +1.51, vy +0.00, vz -0.01); touching nothing
4.00 s: block1 at (8.80, 0.00, 0.10) m, moving 1.16 m/s (vx +1.16, vy +0.00, vz -0.01); touching nothing | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (8.61, 0.00, 0.08) m, moving 1.44 m/s (vx +1.44, vy -0.00, vz -0.01); touching floor
4.25 s: block1 at (9.16, 0.00, 0.10) m, moving 1.08 m/s (vx +1.07, vy -0.00, vz -0.13); touching nothing | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (8.95, 0.00, 0.08) m, moving 1.36 m/s (vx +1.36, vy +0.00, vz +0.01); touching floor
4.50 s: block1 at (9.47, 0.00, 0.11) m, moving 1.51 m/s (vx +1.50, vy -0.00, vz -0.20), turned 1° from how it started; touching nothing | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (9.28, 0.00, 0.08) m, moving 1.24 m/s (vx +1.24, vy +0.00, vz -0.01); touching floor
4.75 s: block1 at (9.76, 0.00, 0.10) m, moving 1.24 m/s (vx +1.22, vy +0.00, vz +0.22); touching nothing | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (9.58, 0.00, 0.08) m, moving 1.15 m/s (vx +1.15, vy -0.00, vz -0.00); touching floor
5.00 s: block1 at (10.04, 0.00, 0.10) m, moving 0.96 m/s (vx +0.96, vy -0.00, vz -0.05); touching nothing | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (9.86, 0.00, 0.08) m, moving 1.08 m/s (vx +1.08, vy +0.00, vz +0.01); touching floor
5.25 s: block1 at (10.30, 0.00, 0.10) m, moving 0.82 m/s (vx +0.82, vy +0.00, vz -0.07); touching nothing | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (10.12, 0.00, 0.08) m, moving 1.00 m/s (vx +1.00, vy -0.00, vz +0.01); touching floor
5.50 s: block1 at (10.54, 0.00, 0.10) m, moving 0.87 m/s (vx +0.86, vy +0.00, vz +0.06); touching nothing | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (10.35, 0.00, 0.08) m, moving 0.90 m/s (vx +0.90, vy -0.00, vz +0.01); touching floor
5.75 s: block1 at (10.75, 0.00, 0.10) m, moving 0.78 m/s (vx +0.78, vy +0.00, vz +0.01); touching nothing | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (10.56, 0.00, 0.08) m, moving 0.81 m/s (vx +0.81, vy -0.00, vz +0.01); touching floor
6.00 s: block1 at (10.94, 0.00, 0.10) m, moving 0.85 m/s (vx +0.85, vy +0.00, vz -0.04); touching floor | block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at (10.76, 0.00, 0.08) m, moving 0.72 m/s (vx +0.72, vy -0.00, vz -0.01); touching floor

At the end (6.00 s):
- block1 at (10.94, 0.00, 0.10) m, moving 0.85 m/s (vx +0.85, vy +0.00, vz -0.04); touching floor
- block2 at (1.90, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- block3 at (1.65, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- block4 at (1.42, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- block5 at (1.12, 0.02, 0.10) m, at rest, turned 90° from how it started; touching floor
- pusher at (10.76, 0.00, 0.08) m, moving 0.72 m/s (vx +0.72, vy -0.00, vz -0.01); touching floor
</history>
