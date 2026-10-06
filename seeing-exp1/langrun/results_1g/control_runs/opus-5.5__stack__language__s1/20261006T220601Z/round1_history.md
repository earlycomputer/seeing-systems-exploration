MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1; starts at (1.50, 0.00, 0.06) m, at rest
- block2: free body; its geoms: block2; starts at (1.50, 0.00, 0.18) m, at rest
- block3: free body; its geoms: block3; starts at (1.50, 0.00, 0.30) m, at rest
- block4: free body; its geoms: block4; starts at (1.50, 0.00, 0.42) m, at rest
- block5: free body; its geoms: block5; starts at (1.50, 0.00, 0.54) m, at rest
- pusher: free body; its geoms: pusher; starts at (0.20, 0.00, 0.05) m, moving 1.50 m/s (vx +1.50, vy +0.00, vz +0.00)

What happened, in order:
 0.00 s  block1 starts touching floor
 0.00 s  block1 starts touching block2
 0.00 s  block3 starts touching block4
 0.00 s  pusher starts touching floor
 0.00 s  block2 starts touching block3
 0.01 s  block3 starts moving
 0.01 s  block4 starts moving
 0.01 s  block5 starts moving
 0.01 s  block3 comes to rest at (1.50, 0.00, 0.30) m
 0.01 s  block4 first touches block5
 0.01 s  block4 comes to rest at (1.50, 0.00, 0.42) m
 0.02 s  block5 comes to rest at (1.50, 0.00, 0.54) m
 2.18 s  pusher comes to rest at (1.39, 0.00, 0.05) m
 6.00 s  block1 passes 0.00 m from pusher without touching it: nearest points (1.46, 0.00, 0.05) m and (1.46, 0.00, 0.05) m
 6.00 s  block2 passes 0.04 m from pusher without touching it: nearest points (1.46, 0.00, 0.12) m and (1.44, 0.00, 0.09) m
 6.00 s  block3 passes 0.15 m from pusher without touching it: nearest points (1.46, 0.00, 0.24) m and (1.42, 0.00, 0.10) m
 6.00 s  block4 passes 0.26 m from pusher without touching it: nearest points (1.46, 0.00, 0.36) m and (1.41, 0.00, 0.10) m
 6.00 s  block5 passes 0.38 m from pusher without touching it: nearest points (1.46, 0.00, 0.48) m and (1.41, 0.00, 0.10) m

State every 0.25 s:
0.00 s: block1 at (1.50, 0.00, 0.06) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.18) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.30) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.42) m, at rest; touching block3 | block5 at (1.50, 0.00, 0.54) m, at rest; touching nothing | pusher at (0.20, 0.00, 0.05) m, moving 1.50 m/s (vx +1.50, vy +0.00, vz +0.00); touching floor
0.25 s: block1 at (1.50, 0.00, 0.06) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.18) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.30) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.42) m, at rest; touching block3, block5 | block5 at (1.50, 0.00, 0.54) m, at rest; touching block4 | pusher at (0.47, 0.00, 0.05) m, moving 0.98 m/s (vx +0.98, vy -0.00, vz +0.02); touching floor
0.50 s: block1 at (1.50, 0.00, 0.06) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.18) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.30) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.42) m, at rest; touching block3, block5 | block5 at (1.50, 0.00, 0.54) m, at rest; touching block4 | pusher at (0.70, 0.00, 0.05) m, moving 0.85 m/s (vx +0.85, vy -0.00, vz +0.01); touching floor
0.75 s: block1 at (1.50, 0.00, 0.06) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.18) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.30) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.42) m, at rest; touching block3, block5 | block5 at (1.50, 0.00, 0.54) m, at rest; touching block4 | pusher at (0.90, 0.00, 0.05) m, moving 0.72 m/s (vx +0.72, vy -0.00, vz -0.00); touching nothing
1.00 s: block1 at (1.50, 0.00, 0.06) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.18) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.30) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.42) m, at rest; touching block3, block5 | block5 at (1.50, 0.00, 0.54) m, at rest; touching block4 | pusher at (1.06, 0.00, 0.05) m, moving 0.59 m/s (vx +0.59, vy -0.00, vz -0.01); touching nothing
1.25 s: block1 at (1.50, 0.00, 0.06) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.18) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.30) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.42) m, at rest; touching block3, block5 | block5 at (1.50, 0.00, 0.54) m, at rest; touching block4 | pusher at (1.19, 0.00, 0.05) m, moving 0.45 m/s (vx +0.45, vy -0.00, vz +0.00); touching floor
1.50 s: block1 at (1.50, 0.00, 0.06) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.18) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.30) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.42) m, at rest; touching block3, block5 | block5 at (1.50, 0.00, 0.54) m, at rest; touching block4 | pusher at (1.29, 0.00, 0.05) m, moving 0.32 m/s (vx +0.32, vy -0.00, vz -0.00); touching floor
1.75 s: block1 at (1.50, 0.00, 0.06) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.18) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.30) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.42) m, at rest; touching block3, block5 | block5 at (1.50, 0.00, 0.54) m, at rest; touching block4 | pusher at (1.35, 0.00, 0.05) m, moving 0.18 m/s (vx +0.18, vy +0.00, vz +0.00); touching floor
2.00 s: block1 at (1.50, 0.00, 0.06) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.18) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.30) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.42) m, at rest; touching block3, block5 | block5 at (1.50, 0.00, 0.54) m, at rest; touching block4 | pusher at (1.38, 0.00, 0.05) m, moving 0.09 m/s (vx +0.09, vy +0.00, vz -0.00); touching floor
2.25 s: block1 at (1.50, 0.00, 0.06) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.18) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.30) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.42) m, at rest; touching block3, block5 | block5 at (1.50, 0.00, 0.54) m, at rest; touching block4 | pusher at (1.40, 0.00, 0.05) m, at rest; touching floor
(the same through 2.50 s)
2.75 s: block1 at (1.50, 0.00, 0.06) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.18) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.30) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.42) m, at rest; touching block3, block5 | block5 at (1.50, 0.00, 0.54) m, at rest; touching block4 | pusher at (1.41, 0.00, 0.05) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (1.50, 0.00, 0.06) m, at rest; touching block2, floor
- block2 at (1.50, 0.00, 0.18) m, at rest; touching block1, block3
- block3 at (1.50, 0.00, 0.30) m, at rest; touching block2, block4
- block4 at (1.50, 0.00, 0.42) m, at rest; touching block3, block5
- block5 at (1.50, 0.00, 0.54) m, at rest; touching block4
- pusher at (1.41, 0.00, 0.05) m, at rest; touching floor
</history>
