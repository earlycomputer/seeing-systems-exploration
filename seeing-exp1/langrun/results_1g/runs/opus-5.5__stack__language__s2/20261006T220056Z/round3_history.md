Your expectations, checked against the run (2 of 2 hold):

- holds: pusher ball touches block1 (first touch at 0.65 s)
- holds: block5 touches floor (first touch at 1.08 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1; starts at (2.50, 0.00, 0.06) m, at rest
- block2: free body; its geoms: block2; starts at (2.50, 0.00, 0.18) m, at rest
- block3: free body; its geoms: block3; starts at (2.50, 0.00, 0.30) m, at rest
- block4: free body; its geoms: block4; starts at (2.50, 0.00, 0.42) m, at rest
- block5: free body; its geoms: block5; starts at (2.50, 0.00, 0.54) m, at rest
- pusher ball: free body; its geoms: pusher ball; starts at (0.20, 0.00, 0.05) m, moving 3.50 m/s (vx +3.50, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  block1 starts touching floor
 0.00 s  block1 starts touching block2
 0.00 s  block3 starts touching block4
 0.00 s  pusher ball starts touching floor
 0.00 s  block2 starts touching block3
 0.01 s  block3 starts moving
 0.01 s  block4 starts moving
 0.01 s  block5 starts moving
 0.01 s  block4 first touches block5
 0.64 s  pusher ball leaves floor
 0.65 s  block1 first touches pusher ball
 0.65 s  block1 starts moving
 0.65 s  block2 starts moving
 0.67 s  block1 leaves block2
 0.68 s  block3 passes 0.13 m from pusher ball without touching it: nearest points (2.50, 0.00, 0.25) m and (2.51, 0.00, 0.11) m
 0.68 s  block4 passes 0.25 m from pusher ball without touching it: nearest points (2.49, 0.00, 0.37) m and (2.51, 0.00, 0.11) m
 0.68 s  block5 passes 0.37 m from pusher ball without touching it: nearest points (2.49, 0.00, 0.49) m and (2.51, 0.00, 0.11) m
 0.68 s  block2 first touches pusher ball
 0.69 s  block2 leaves pusher ball
 0.70 s  block1 leaves floor
 0.71 s  block3 leaves block4
 0.71 s  block2 leaves block3
 0.71 s  block1 leaves pusher ball
 0.73 s  block4 leaves block5
 0.73 s  block3 is at the top of its flight, at (2.54, 0.00, 0.32) m
 0.75 s  block5 is at the top of its flight, at (2.47, 0.00, 0.56) m
 0.75 s  block4 is at the top of its flight, at (2.50, 0.00, 0.44) m
 0.76 s  block2 is at the top of its flight, at (2.67, 0.00, 0.21) m
 0.79 s  pusher ball touches floor again
 0.80 s  block1 touches floor again
 0.82 s  block1 leaves floor
 0.85 s  block1 touches floor again
 0.85 s  block2 touches pusher ball again
 0.87 s  pusher ball leaves floor
 0.87 s  block1 touches pusher ball again
 0.87 s  block1 leaves floor
 0.87 s  block2 leaves pusher ball
 0.89 s  block1 leaves pusher ball
 0.91 s  pusher ball touches floor again
 0.92 s  block1 touches block2 again
 0.94 s  block1 leaves block2
 0.96 s  block3 first touches floor
 1.00 s  block1 touches floor again
 1.02 s  block1 touches block2 again
 1.03 s  block4 first touches floor
 1.05 s  block4 touches block5 again
 1.08 s  block4 leaves block5
 1.08 s  block5 first touches floor
 1.08 s  pusher ball leaves floor
 1.08 s  block1 touches pusher ball again
 1.08 s  block1 leaves floor
 1.09 s  block1 leaves block2
 1.09 s  block1 leaves pusher ball
 1.11 s  block2 touches pusher ball again
 1.12 s  pusher ball touches floor again
 1.12 s  block2 leaves pusher ball
 1.14 s  block4 comes to rest at (2.45, 0.00, 0.04) m
 1.15 s  block3 comes to rest at (2.75, 0.00, 0.04) m
 1.16 s  block1 touches floor 5 more times between 1.16 s and 6.00 s, still touching at the end
 1.18 s  block5 comes to rest at (2.32, 0.00, 0.04) m
 1.19 s  block2 is at the top of its flight, at (3.45, 0.00, 0.18) m
 1.26 s  block1 touches block2 again
 1.29 s  block2 touches pusher ball again
 1.29 s  block2 leaves pusher ball
 1.29 s  block1 leaves block2
 1.29 s  block1 touches pusher ball again
 1.31 s  block1 leaves pusher ball
 1.33 s  block1 touches block2 4 more times between 1.33 s and 6.00 s, still touching at the end
 1.45 s  block2 touches pusher ball 2 more times between 1.45 s and 6.00 s, still touching at the end
 1.51 s  block1 touches pusher ball 5 more times between 1.51 s and 2.02 s
 1.56 s  block2 is at the top of its flight, at (3.83, 0.00, 0.16) m
 1.90 s  pusher ball comes to rest at (3.89, 0.00, 0.05) m
 1.91 s  block1 comes to rest at (4.00, 0.00, 0.04) m
 1.91 s  block2 comes to rest at (3.98, 0.00, 0.12) m

State every 0.25 s:
0.00 s: block1 at (2.50, 0.00, 0.06) m, at rest; touching block2, floor | block2 at (2.50, 0.00, 0.18) m, at rest; touching block1, block3 | block3 at (2.50, 0.00, 0.30) m, at rest; touching block2, block4 | block4 at (2.50, 0.00, 0.42) m, at rest; touching block3 | block5 at (2.50, 0.00, 0.54) m, at rest; touching nothing | pusher ball at (0.20, 0.00, 0.05) m, moving 3.50 m/s (vx +3.50, vy +0.00, vz +0.00); touching floor
0.25 s: block1 at (2.50, 0.00, 0.06) m, at rest; touching block2, floor | block2 at (2.50, 0.00, 0.18) m, at rest; touching block1, block3 | block3 at (2.50, 0.00, 0.30) m, at rest; touching block2, block4 | block4 at (2.50, 0.00, 0.42) m, at rest; touching block3, block5 | block5 at (2.50, 0.00, 0.54) m, at rest; touching block4 | pusher ball at (1.07, 0.00, 0.05) m, moving 3.46 m/s (vx +3.46, vy -0.00, vz +0.01); touching nothing
0.50 s: block1 at (2.50, 0.00, 0.06) m, at rest; touching block2, floor | block2 at (2.50, 0.00, 0.18) m, at rest; touching block1, block3 | block3 at (2.50, 0.00, 0.30) m, at rest; touching block2, block4 | block4 at (2.50, 0.00, 0.42) m, at rest; touching block3, block5 | block5 at (2.50, 0.00, 0.54) m, at rest; touching block4 | pusher ball at (1.92, 0.00, 0.05) m, moving 3.40 m/s (vx +3.40, vy -0.00, vz -0.01); touching nothing
0.75 s: block1 at (2.78, 0.00, 0.09) m, moving 2.47 m/s (vx +2.47, vy -0.00, vz -0.06), turned 3° from how it started; touching nothing | block2 at (2.66, 0.00, 0.21) m, moving 2.02 m/s (vx +2.02, vy -0.00, vz +0.07), turned 61° from how it started; touching nothing | block3 at (2.55, 0.00, 0.31) m, moving 0.67 m/s (vx +0.64, vy -0.00, vz -0.17), turned 35° from how it started; touching nothing | block4 at (2.50, 0.00, 0.44) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.01), turned 13° from how it started; touching nothing | block5 at (2.47, 0.00, 0.56) m, moving 0.38 m/s (vx -0.38, vy +0.00, vz -0.04), turned 13° from how it started; touching nothing | pusher ball at (2.66, 0.00, 0.07) m, moving 2.26 m/s (vx +2.24, vy -0.00, vz -0.30); touching nothing
1.00 s: block1 at (3.27, 0.00, 0.07) m, moving 1.71 m/s (vx +1.69, vy -0.00, vz -0.24), turned 38° from how it started; touching floor | block2 at (3.17, 0.00, 0.18) m, moving 1.97 m/s (vx +1.89, vy -0.00, vz -0.56), turned 147° from how it started; touching nothing | block3 at (2.70, 0.00, 0.06) m, moving 0.51 m/s (vx +0.49, vy +0.00, vz +0.14), turned 131° from how it started; touching floor | block4 at (2.48, 0.00, 0.14) m, moving 2.47 m/s (vx -0.06, vy +0.00, vz -2.47), turned 52° from how it started; touching nothing | block5 at (2.38, 0.00, 0.25) m, moving 2.52 m/s (vx -0.38, vy +0.00, vz -2.49), turned 52° from how it started; touching nothing | pusher ball at (3.12, 0.00, 0.05) m, moving 1.60 m/s (vx +1.60, vy +0.00, vz +0.00); touching floor
1.25 s: block1 at (3.60, 0.00, 0.06) m, moving 1.06 m/s (vx +0.97, vy -0.00, vz -0.42), turned 74° from how it started; touching nothing | block2 at (3.54, 0.00, 0.17) m, moving 1.62 m/s (vx +1.52, vy +0.00, vz -0.56), turned 18° from how it started; touching nothing | block3 at (2.75, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block4 at (2.45, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block5 at (2.32, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | pusher ball at (3.47, 0.00, 0.05) m, moving 1.26 m/s (vx +1.26, vy -0.00, vz +0.00); touching floor
1.50 s: block1 at (3.85, 0.00, 0.04) m, moving 0.40 m/s (vx +0.36, vy -0.00, vz +0.16), turned 89° from how it started; touching floor | block2 at (3.80, 0.00, 0.15) m, moving 0.82 m/s (vx +0.62, vy +0.00, vz +0.54), turned 16° from how it started; touching nothing | block3 at (2.75, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block4 at (2.45, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block5 at (2.32, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | pusher ball at (3.73, 0.00, 0.05) m, moving 0.87 m/s (vx +0.87, vy -0.00, vz +0.01); touching floor
1.75 s: block1 at (3.98, 0.00, 0.04) m, moving 0.27 m/s (vx +0.27, vy -0.00, vz -0.04), turned 90° from how it started; touching floor, pusher ball | block2 at (3.93, 0.00, 0.14) m, moving 0.65 m/s (vx +0.62, vy +0.00, vz -0.19), turned 90° from how it started; touching pusher ball | block3 at (2.75, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block4 at (2.45, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block5 at (2.32, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | pusher ball at (3.87, 0.00, 0.05) m, moving 0.25 m/s (vx +0.25, vy +0.00, vz +0.00); touching block1, block2, floor
2.00 s: block1 at (4.00, 0.00, 0.04) m, at rest, turned 90° from how it started; touching block2, floor, pusher ball | block2 at (3.98, 0.00, 0.13) m, at rest, turned 84° from how it started; touching block1, pusher ball | block3 at (2.75, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block4 at (2.45, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block5 at (2.32, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | pusher ball at (3.89, 0.00, 0.05) m, at rest; touching block1, block2, floor
2.25 s: block1 at (4.00, 0.00, 0.04) m, at rest, turned 90° from how it started; touching block2, floor | block2 at (3.98, 0.00, 0.13) m, at rest, turned 84° from how it started; touching block1, pusher ball | block3 at (2.75, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block4 at (2.45, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block5 at (2.32, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | pusher ball at (3.89, 0.00, 0.05) m, at rest; touching block2, floor
(the same through 2.50 s)
2.75 s: block1 at (4.00, 0.00, 0.04) m, at rest, turned 90° from how it started; touching block2, floor | block2 at (3.98, 0.00, 0.13) m, at rest, turned 85° from how it started; touching block1, pusher ball | block3 at (2.75, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block4 at (2.45, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block5 at (2.32, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | pusher ball at (3.89, 0.00, 0.05) m, at rest; touching block2, floor
3.00 s: block1 at (4.00, 0.00, 0.04) m, at rest, turned 90° from how it started; touching block2, floor | block2 at (3.98, 0.00, 0.12) m, at rest, turned 85° from how it started; touching block1, pusher ball | block3 at (2.75, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block4 at (2.45, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block5 at (2.32, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | pusher ball at (3.89, 0.00, 0.05) m, at rest; touching block2, floor
(the same through 3.25 s)
3.50 s: block1 at (4.00, 0.00, 0.04) m, at rest, turned 90° from how it started; touching block2, floor | block2 at (3.99, 0.00, 0.12) m, at rest, turned 86° from how it started; touching block1, pusher ball | block3 at (2.75, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block4 at (2.45, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block5 at (2.32, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | pusher ball at (3.89, 0.00, 0.05) m, at rest; touching block2, floor
(the same through 4.00 s)
4.25 s: block1 at (4.00, 0.00, 0.04) m, at rest, turned 90° from how it started; touching block2, floor | block2 at (3.99, 0.00, 0.12) m, at rest, turned 87° from how it started; touching block1, pusher ball | block3 at (2.75, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block4 at (2.45, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block5 at (2.32, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | pusher ball at (3.89, 0.00, 0.05) m, at rest; touching block2, floor
(the same through 4.50 s)
4.75 s: block1 at (4.00, 0.00, 0.04) m, at rest, turned 90° from how it started; touching block2, floor | block2 at (3.99, 0.00, 0.12) m, at rest, turned 88° from how it started; touching block1, pusher ball | block3 at (2.75, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block4 at (2.45, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block5 at (2.32, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | pusher ball at (3.89, 0.00, 0.05) m, at rest; touching block2, floor
(the same through 5.00 s)
5.25 s: block1 at (4.00, 0.00, 0.04) m, at rest, turned 90° from how it started; touching block2, floor | block2 at (3.99, 0.00, 0.12) m, at rest, turned 89° from how it started; touching block1, pusher ball | block3 at (2.75, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block4 at (2.45, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block5 at (2.32, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | pusher ball at (3.89, 0.00, 0.05) m, at rest; touching block2, floor
(the same through 5.50 s)
5.75 s: block1 at (4.00, 0.00, 0.04) m, at rest, turned 90° from how it started; touching block2, floor | block2 at (3.99, 0.00, 0.12) m, at rest, turned 90° from how it started; touching block1, pusher ball | block3 at (2.75, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block4 at (2.45, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | block5 at (2.32, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor | pusher ball at (3.89, 0.00, 0.05) m, at rest; touching block2, floor
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (4.00, 0.00, 0.04) m, at rest, turned 90° from how it started; touching block2, floor
- block2 at (3.99, 0.00, 0.12) m, at rest, turned 90° from how it started; touching block1, pusher ball
- block3 at (2.75, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor
- block4 at (2.45, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor
- block5 at (2.32, 0.00, 0.04) m, at rest, turned 90° from how it started; touching floor
- pusher ball at (3.89, 0.00, 0.05) m, at rest; touching block2, floor
</history>
