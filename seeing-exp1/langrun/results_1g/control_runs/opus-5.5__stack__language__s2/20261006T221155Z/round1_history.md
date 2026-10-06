MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1; starts at (1.00, 0.00, 0.08) m, at rest
- block2: free body; its geoms: block2; starts at (1.00, 0.00, 0.24) m, at rest
- block3: free body; its geoms: block3; starts at (1.00, 0.00, 0.40) m, at rest
- block4: free body; its geoms: block4; starts at (1.00, 0.00, 0.56) m, at rest
- block5: free body; its geoms: block5; starts at (1.00, 0.00, 0.72) m, at rest
- ball: free body; its geoms: ball; starts at (-0.20, 0.00, 0.06) m, moving 1.20 m/s (vx +1.20, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  block1 starts touching floor
 0.00 s  block4 starts touching block5
 0.00 s  block1 starts touching block2
 0.00 s  ball starts touching floor
 0.01 s  block2 first touches block3
 0.01 s  block4 starts moving
 0.01 s  block5 starts moving
 0.01 s  block3 first touches block4
 1.01 s  ball leaves floor
 1.01 s  block1 first touches ball
 1.01 s  block1 starts moving
 1.01 s  block2 starts moving
 1.01 s  block3 starts moving
 1.04 s  block2 passes 0.05 m from ball without touching it: nearest points (0.97, 0.00, 0.16) m and (0.95, 0.00, 0.12) m
 1.05 s  block3 passes 0.20 m from ball without touching it: nearest points (0.97, 0.00, 0.32) m and (0.93, 0.00, 0.12) m
 1.05 s  block4 passes 0.36 m from ball without touching it: nearest points (0.96, 0.00, 0.48) m and (0.93, 0.00, 0.12) m
 1.08 s  ball touches floor again
 1.08 s  block1 leaves ball
 1.09 s  ball comes to rest at (0.93, 0.00, 0.06) m
 1.11 s  block1 comes to rest at (1.03, 0.00, 0.08) m
 1.19 s  block1 touches ball again
 1.25 s  block1 leaves ball
 1.29 s  block1 touches ball again
 1.31 s  block1 leaves ball
 1.35 s  block2 comes to rest at (1.02, 0.00, 0.24) m
 1.38 s  block3 comes to rest at (1.02, 0.00, 0.40) m
 1.41 s  block4 comes to rest at (1.02, 0.00, 0.56) m
 1.63 s  block5 comes to rest at (1.02, 0.00, 0.72) m

State every 0.25 s:
0.00 s: block1 at (1.00, 0.00, 0.08) m, at rest; touching block2, floor | block2 at (1.00, 0.00, 0.24) m, at rest; touching block1 | block3 at (1.00, 0.00, 0.40) m, at rest; touching nothing | block4 at (1.00, 0.00, 0.56) m, at rest; touching block5 | block5 at (1.00, 0.00, 0.72) m, at rest; touching block4 | ball at (-0.20, 0.00, 0.06) m, moving 1.20 m/s (vx +1.20, vy +0.00, vz +0.00); touching floor
0.25 s: block1 at (1.00, 0.00, 0.08) m, at rest; touching block2, floor | block2 at (1.00, 0.00, 0.24) m, at rest; touching block1, block3 | block3 at (1.00, 0.00, 0.40) m, at rest; touching block2, block4 | block4 at (1.00, 0.00, 0.56) m, at rest; touching block3, block5 | block5 at (1.00, 0.00, 0.72) m, at rest; touching block4 | ball at (0.09, 0.00, 0.06) m, moving 1.15 m/s (vx +1.15, vy +0.00, vz -0.00); touching nothing
0.50 s: block1 at (1.00, 0.00, 0.08) m, at rest; touching block2, floor | block2 at (1.00, 0.00, 0.24) m, at rest; touching block1, block3 | block3 at (1.00, 0.00, 0.40) m, at rest; touching block2, block4 | block4 at (1.00, 0.00, 0.56) m, at rest; touching block3, block5 | block5 at (1.00, 0.00, 0.72) m, at rest; touching block4 | ball at (0.37, 0.00, 0.06) m, moving 1.09 m/s (vx +1.09, vy +0.00, vz +0.01); touching floor
0.75 s: block1 at (1.00, 0.00, 0.08) m, at rest; touching block2, floor | block2 at (1.00, 0.00, 0.24) m, at rest; touching block1, block3 | block3 at (1.00, 0.00, 0.40) m, at rest; touching block2, block4 | block4 at (1.00, 0.00, 0.56) m, at rest; touching block3, block5 | block5 at (1.00, 0.00, 0.72) m, at rest; touching block4 | ball at (0.64, 0.00, 0.06) m, moving 1.03 m/s (vx +1.03, vy +0.00, vz +0.01); touching floor
1.00 s: block1 at (1.00, 0.00, 0.08) m, at rest; touching block2, floor | block2 at (1.00, 0.00, 0.24) m, at rest; touching block1, block3 | block3 at (1.00, 0.00, 0.40) m, at rest; touching block2, block4 | block4 at (1.00, 0.00, 0.56) m, at rest; touching block3, block5 | block5 at (1.00, 0.00, 0.72) m, at rest; touching block4 | ball at (0.89, 0.00, 0.06) m, moving 0.98 m/s (vx +0.98, vy +0.00, vz -0.01); touching nothing
1.25 s: block1 at (1.03, 0.00, 0.08) m, at rest; touching ball, block2, floor | block2 at (1.02, 0.00, 0.24) m, at rest; touching block1, block3 | block3 at (1.02, 0.00, 0.40) m, moving 0.08 m/s (vx -0.08, vy +0.00, vz +0.01); touching block2, block4 | block4 at (1.01, 0.00, 0.56) m, moving 0.05 m/s (vx -0.00, vy +0.00, vz -0.05), turned 3° from how it started; touching block3, block5 | block5 at (1.00, 0.00, 0.72) m, moving 0.20 m/s (vx +0.20, vy +0.00, vz -0.04), turned 3° from how it started; touching block4 | ball at (0.93, 0.00, 0.06) m, at rest; touching block1, floor
1.50 s: block1 at (1.03, 0.00, 0.08) m, at rest; touching block2, floor | block2 at (1.02, 0.00, 0.24) m, at rest; touching block1, block3 | block3 at (1.02, 0.00, 0.40) m, at rest; touching block2, block4 | block4 at (1.03, 0.00, 0.56) m, at rest; touching block3, block5 | block5 at (1.03, 0.00, 0.72) m, at rest; touching block4 | ball at (0.93, 0.00, 0.06) m, at rest; touching floor
1.75 s: block1 at (1.03, 0.00, 0.08) m, at rest; touching block2, floor | block2 at (1.02, 0.00, 0.24) m, at rest; touching block1, block3 | block3 at (1.02, 0.00, 0.40) m, at rest; touching block2, block4 | block4 at (1.02, 0.00, 0.56) m, at rest; touching block3, block5 | block5 at (1.02, 0.00, 0.72) m, at rest; touching block4 | ball at (0.92, 0.00, 0.06) m, at rest; touching floor
(the same through 3.00 s)
3.25 s: block1 at (1.03, 0.00, 0.08) m, at rest; touching block2, floor | block2 at (1.02, 0.00, 0.24) m, at rest; touching block1, block3 | block3 at (1.02, 0.00, 0.40) m, at rest; touching block2, block4 | block4 at (1.02, 0.00, 0.56) m, at rest; touching block3, block5 | block5 at (1.02, 0.00, 0.72) m, at rest; touching block4 | ball at (0.91, 0.00, 0.06) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (1.03, 0.00, 0.08) m, at rest; touching block2, floor
- block2 at (1.02, 0.00, 0.24) m, at rest; touching block1, block3
- block3 at (1.02, 0.00, 0.40) m, at rest; touching block2, block4
- block4 at (1.02, 0.00, 0.56) m, at rest; touching block3, block5
- block5 at (1.02, 0.00, 0.72) m, at rest; touching block4
- ball at (0.91, 0.00, 0.06) m, at rest; touching floor
</history>
