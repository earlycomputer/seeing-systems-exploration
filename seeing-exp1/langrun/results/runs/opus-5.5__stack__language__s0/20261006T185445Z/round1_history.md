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
- ball: free body; its geoms: ball; starts at (0.50, 0.00, 0.04) m, moving 2.00 m/s (vx +2.00, vy +0.00, vz +0.00)

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
 1.28 s  ball leaves floor
 1.29 s  block1 first touches ball
 1.29 s  block1 starts moving
 1.29 s  block2 starts moving
 1.31 s  block2 passes 0.03 m from ball without touching it: nearest points (1.95, 0.00, 0.10) m and (1.94, 0.00, 0.08) m
 1.31 s  block3 passes 0.12 m from ball without touching it: nearest points (1.95, 0.00, 0.20) m and (1.93, 0.00, 0.08) m
 1.32 s  block4 passes 0.22 m from ball without touching it: nearest points (1.95, 0.00, 0.30) m and (1.93, 0.00, 0.08) m
 1.32 s  block5 passes 0.32 m from ball without touching it: nearest points (1.95, 0.00, 0.40) m and (1.92, 0.00, 0.08) m
 1.33 s  ball touches floor again
 1.33 s  ball comes to rest at (1.92, 0.00, 0.04) m
 1.34 s  block1 comes to rest at (2.01, 0.00, 0.05) m
 1.34 s  block2 comes to rest at (2.01, 0.00, 0.15) m
 1.38 s  block1 leaves ball
 1.38 s  block3 comes to rest at (2.01, 0.00, 0.25) m
 1.39 s  block4 comes to rest at (2.01, 0.00, 0.35) m
 1.40 s  block5 comes to rest at (2.01, 0.00, 0.45) m

State every 0.25 s:
0.00 s: block1 at (2.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.35) m, at rest; touching block3 | block5 at (2.00, 0.00, 0.45) m, at rest; touching nothing | ball at (0.50, 0.00, 0.04) m, moving 2.00 m/s (vx +2.00, vy +0.00, vz +0.00); touching floor
0.25 s: block1 at (2.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.00, 0.00, 0.45) m, at rest; touching block4 | ball at (0.87, 0.00, 0.04) m, moving 1.34 m/s (vx +1.34, vy -0.00, vz +0.00); touching nothing
0.50 s: block1 at (2.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.00, 0.00, 0.45) m, at rest; touching block4 | ball at (1.19, 0.00, 0.04) m, moving 1.18 m/s (vx +1.18, vy -0.00, vz -0.00); touching floor
0.75 s: block1 at (2.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.00, 0.00, 0.45) m, at rest; touching block4 | ball at (1.46, 0.00, 0.04) m, moving 1.01 m/s (vx +1.01, vy -0.00, vz +0.03); touching nothing
1.00 s: block1 at (2.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.00, 0.00, 0.45) m, at rest; touching block4 | ball at (1.69, 0.00, 0.04) m, moving 0.85 m/s (vx +0.85, vy -0.00, vz -0.01); touching nothing
1.25 s: block1 at (2.00, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.00, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.00, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.00, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.00, 0.00, 0.45) m, at rest; touching block4 | ball at (1.89, 0.00, 0.04) m, moving 0.69 m/s (vx +0.69, vy -0.00, vz -0.02); touching nothing
1.50 s: block1 at (2.01, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (2.01, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (2.01, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (2.01, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (2.01, 0.00, 0.45) m, at rest; touching block4 | ball at (1.92, 0.00, 0.04) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (2.01, 0.00, 0.05) m, at rest; touching block2, floor
- block2 at (2.01, 0.00, 0.15) m, at rest; touching block1, block3
- block3 at (2.01, 0.00, 0.25) m, at rest; touching block2, block4
- block4 at (2.01, 0.00, 0.35) m, at rest; touching block3, block5
- block5 at (2.01, 0.00, 0.45) m, at rest; touching block4
- ball at (1.92, 0.00, 0.04) m, at rest; touching floor
</history>
