MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1; starts at (2.00, 0.00, 0.05) m, at rest
- block2: free body; its geoms: block2; starts at (2.00, 0.00, 0.15) m, at rest
- block3: free body; its geoms: block3; starts at (2.00, 0.00, 0.25) m, at rest
- block4: free body; its geoms: block4; starts at (2.00, 0.00, 0.35) m, at rest
- block5: free body; its geoms: block5; starts at (2.00, 0.00, 0.45) m, at rest
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.04) m, moving 2.50 m/s (vx +2.50, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  block1 starts touching floor
 0.00 s  block1 starts touching block2
 0.00 s  block3 starts touching block4
 0.00 s  ball starts touching floor
 0.00 s  block2 starts touching block3
 0.01 s  block3 starts moving
 0.01 s  block4 starts moving
 0.01 s  block5 starts moving
 0.01 s  block4 first touches block5
 1.31 s  block1 first touches ball
 1.31 s  block1 starts moving
 1.31 s  block2 starts moving
 1.31 s  ball leaves floor
 1.35 s  block2 passes 0.02 m from ball without touching it: nearest points (1.98, 0.00, 0.10) m and (1.97, 0.00, 0.08) m
 1.35 s  block3 passes 0.12 m from ball without touching it: nearest points (1.98, 0.00, 0.20) m and (1.96, 0.00, 0.08) m
 1.35 s  block4 passes 0.22 m from ball without touching it: nearest points (1.97, 0.00, 0.30) m and (1.96, 0.00, 0.08) m
 1.35 s  block5 passes 0.32 m from ball without touching it: nearest points (1.97, 0.00, 0.40) m and (1.95, 0.00, 0.08) m
 1.37 s  ball touches floor again
 1.38 s  ball comes to rest at (1.96, 0.00, 0.04) m
 1.39 s  block1 comes to rest at (2.03, 0.00, 0.05) m
 1.44 s  block1 leaves ball
 1.47 s  block2 comes to rest at (2.02, 0.00, 0.15) m
 1.58 s  block3 comes to rest at (2.02, 0.00, 0.25) m
 1.59 s  block4 comes to rest at (2.02, 0.00, 0.35) m
 1.77 s  block5 comes to rest at (2.01, 0.00, 0.45) m

State every 0.25 s:
0.00 s: block1 at (2.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.35) m, at rest; touching block3 | block5 at (2.00, 0.00, 0.45) m, at rest; touching nothing | ball at (0.00, 0.00, 0.04) m, moving 2.50 m/s (vx +2.50, vy +0.00, vz +0.00); touching floor
0.25 s: block1 at (2.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.00, 0.00, 0.45) m, at rest; touching block4 | ball at (0.48, 0.00, 0.04) m, moving 1.72 m/s (vx +1.72, vy -0.00, vz -0.05); touching nothing
0.50 s: block1 at (2.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.00, 0.00, 0.45) m, at rest; touching block4 | ball at (0.88, 0.00, 0.04) m, moving 1.55 m/s (vx +1.55, vy -0.00, vz +0.01); touching nothing
0.75 s: block1 at (2.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.00, 0.00, 0.45) m, at rest; touching block4 | ball at (1.25, 0.00, 0.04) m, moving 1.39 m/s (vx +1.39, vy -0.00, vz -0.01); touching nothing
1.00 s: block1 at (2.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.00, 0.00, 0.45) m, at rest; touching block4 | ball at (1.58, 0.00, 0.04) m, moving 1.23 m/s (vx +1.23, vy -0.00, vz -0.01); touching nothing
1.25 s: block1 at (2.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.00, 0.00, 0.45) m, at rest; touching block4 | ball at (1.87, 0.00, 0.04) m, moving 1.06 m/s (vx +1.06, vy +0.00, vz +0.00); touching floor
1.50 s: block1 at (2.02, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.01, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.01, 0.00, 0.25) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz +0.01); touching block2, block4 | block4 at (2.01, 0.00, 0.35) m, moving 0.07 m/s (vx +0.02, vy -0.00, vz -0.07), turned 1° from how it started; touching block3, block5 | block5 at (2.01, 0.00, 0.45) m, moving 0.25 m/s (vx +0.24, vy -0.00, vz -0.06), turned 2° from how it started; touching block4 | ball at (1.95, 0.00, 0.04) m, at rest; touching floor
1.75 s: block1 at (2.03, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.02, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.02, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.01, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.01, 0.00, 0.45) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching block4 | ball at (1.95, 0.00, 0.04) m, at rest; touching floor
2.00 s: block1 at (2.02, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.02, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.02, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.01, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.01, 0.00, 0.45) m, at rest; touching block4 | ball at (1.95, 0.00, 0.04) m, at rest; touching floor
(the same through 2.50 s)
2.75 s: block1 at (2.02, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.02, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.01, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.01, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.01, 0.00, 0.45) m, at rest; touching block4 | ball at (1.95, 0.00, 0.04) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (2.02, 0.00, 0.05) m, at rest; touching block2, floor
- block2 at (2.02, 0.00, 0.15) m, at rest; touching block1, block3
- block3 at (2.01, 0.00, 0.25) m, at rest; touching block2, block4
- block4 at (2.01, 0.00, 0.35) m, at rest; touching block3, block5
- block5 at (2.01, 0.00, 0.45) m, at rest; touching block4
- ball at (1.95, 0.00, 0.04) m, at rest; touching floor
</history>
