Your expectations, checked against the run (1 of 2 hold):

- holds: pusher ball touches block1 (first touch at 1.30 s)
- DOES NOT HOLD: block5 touches floor (they never touch)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1; starts at (1.50, 0.00, 0.05) m, at rest
- block2: free body; its geoms: block2; starts at (1.50, 0.00, 0.15) m, at rest
- block3: free body; its geoms: block3; starts at (1.50, 0.00, 0.25) m, at rest
- block4: free body; its geoms: block4; starts at (1.50, 0.00, 0.35) m, at rest
- block5: free body; its geoms: block5; starts at (1.50, 0.00, 0.45) m, at rest
- pusher ball: free body; its geoms: pusher ball; starts at (0.20, 0.00, 0.05) m, moving 1.50 m/s (vx +1.50, vy +0.00, vz +0.00)

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
 1.30 s  pusher ball leaves floor
 1.30 s  block1 first touches pusher ball
 1.30 s  block1 starts moving
 1.30 s  block2 starts moving
 1.34 s  pusher ball touches floor again
 1.35 s  block2 passes 0.01 m from pusher ball without touching it: nearest points (1.46, 0.00, 0.10) m and (1.45, 0.00, 0.09) m
 1.35 s  block3 passes 0.10 m from pusher ball without touching it: nearest points (1.46, 0.00, 0.20) m and (1.43, 0.00, 0.10) m
 1.35 s  block4 passes 0.20 m from pusher ball without touching it: nearest points (1.46, 0.00, 0.30) m and (1.43, 0.00, 0.10) m
 1.35 s  block5 passes 0.30 m from pusher ball without touching it: nearest points (1.45, 0.00, 0.40) m and (1.43, 0.00, 0.10) m
 1.38 s  pusher ball comes to rest at (1.42, 0.00, 0.05) m
 1.38 s  block1 comes to rest at (1.52, 0.00, 0.05) m
 1.39 s  block2 comes to rest at (1.52, 0.00, 0.15) m
 1.44 s  block1 leaves pusher ball
 1.57 s  block3 comes to rest at (1.52, 0.00, 0.25) m
 1.61 s  block4 comes to rest at (1.52, 0.00, 0.35) m
 1.62 s  block5 comes to rest at (1.52, 0.00, 0.45) m

State every 0.25 s:
0.00 s: block1 at (1.50, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.35) m, at rest; touching block3 | block5 at (1.50, 0.00, 0.45) m, at rest; touching nothing | pusher ball at (0.20, 0.00, 0.05) m, moving 1.50 m/s (vx +1.50, vy +0.00, vz +0.00); touching floor
0.25 s: block1 at (1.50, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (1.50, 0.00, 0.45) m, at rest; touching block4 | pusher ball at (0.47, 0.00, 0.05) m, moving 1.03 m/s (vx +1.02, vy -0.00, vz -0.00); touching floor
0.50 s: block1 at (1.50, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (1.50, 0.00, 0.45) m, at rest; touching block4 | pusher ball at (0.72, 0.00, 0.05) m, moving 0.96 m/s (vx +0.96, vy -0.00, vz +0.02); touching floor
0.75 s: block1 at (1.50, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (1.50, 0.00, 0.45) m, at rest; touching block4 | pusher ball at (0.95, 0.00, 0.05) m, moving 0.89 m/s (vx +0.89, vy -0.00, vz -0.01); touching nothing
1.00 s: block1 at (1.50, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (1.50, 0.00, 0.45) m, at rest; touching block4 | pusher ball at (1.17, 0.00, 0.05) m, moving 0.82 m/s (vx +0.82, vy -0.00, vz +0.01); touching floor
1.25 s: block1 at (1.50, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (1.50, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (1.50, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (1.50, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (1.50, 0.00, 0.45) m, at rest; touching block4 | pusher ball at (1.36, 0.00, 0.05) m, moving 0.75 m/s (vx +0.75, vy -0.00, vz +0.01); touching floor
1.50 s: block1 at (1.53, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (1.52, 0.00, 0.15) m, at rest, turned 1° from how it started; touching block1, block3 | block3 at (1.52, 0.00, 0.25) m, at rest, turned 1° from how it started; touching block2, block4 | block4 at (1.52, 0.00, 0.35) m, at rest, turned 1° from how it started; touching block3, block5 | block5 at (1.52, 0.00, 0.45) m, at rest, turned 1° from how it started; touching block4 | pusher ball at (1.43, 0.00, 0.05) m, at rest; touching floor
1.75 s: block1 at (1.53, 0.00, 0.05) m, at rest; touching block2, floor | block2 at (1.52, 0.00, 0.15) m, at rest; touching block1, block3 | block3 at (1.52, 0.00, 0.25) m, at rest; touching block2, block4 | block4 at (1.52, 0.00, 0.35) m, at rest; touching block3, block5 | block5 at (1.52, 0.00, 0.45) m, at rest; touching block4 | pusher ball at (1.42, 0.00, 0.05) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (1.53, 0.00, 0.05) m, at rest; touching block2, floor
- block2 at (1.52, 0.00, 0.15) m, at rest; touching block1, block3
- block3 at (1.52, 0.00, 0.25) m, at rest; touching block2, block4
- block4 at (1.52, 0.00, 0.35) m, at rest; touching block3, block5
- block5 at (1.52, 0.00, 0.45) m, at rest; touching block4
- pusher ball at (1.42, 0.00, 0.05) m, at rest; touching floor
</history>
