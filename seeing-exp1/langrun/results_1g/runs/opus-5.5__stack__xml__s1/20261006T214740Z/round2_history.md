Your expectations, checked against the run (1 of 3 hold):

- holds: pusher touches block1 (first touch at 0.60 s)
- DOES NOT HOLD: block2 touches floor (they never touch)
- DOES NOT HOLD: block5 touches floor (they never touch)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pusher: slide joint pusher_slide about axis (1.00, 0.00, 0.00), range -0.1 m to 0.68 m as MuJoCo applies it; its geoms: pusher_paddle, pusher_arm; starts at 0.000 m, moving +1.00 m/s
- block1: free body; its geoms: block1_geom; starts at (0.00, 0.00, 0.05) m, at rest
- block2: free body; its geoms: block2_geom; starts at (0.00, 0.00, 0.15) m, at rest
- block3: free body; its geoms: block3_geom; starts at (0.00, 0.00, 0.25) m, at rest
- block4: free body; its geoms: block4_geom; starts at (0.00, 0.00, 0.35) m, at rest
- block5: free body; its geoms: block5_geom; starts at (0.00, 0.00, 0.45) m, at rest

What happened, in order:
 0.00 s  block2_geom starts touching block3_geom
 0.00 s  block1_geom starts touching floor
 0.00 s  block1_geom starts touching block2_geom
 0.00 s  block3_geom starts touching block4_geom
 0.01 s  block3 starts moving
 0.01 s  block4 starts moving
 0.01 s  block5 starts moving
 0.01 s  block3 comes to rest at (0.00, 0.00, 0.25) m
 0.01 s  block4_geom first touches block5_geom
 0.60 s  pusher_arm first touches block1_geom
 0.60 s  pusher_paddle first touches block1_geom
 0.60 s  block1 starts moving
 0.61 s  block2 starts moving
 0.61 s  block2 comes to rest at (0.00, 0.00, 0.15) m
 0.64 s  pusher passes 0.06 m from block2 (block2_geom) without touching it: nearest points (-0.05, -0.03, 0.04) m and (-0.05, -0.03, 0.10) m
 0.65 s  block4 comes to rest at (0.00, 0.00, 0.35) m
 0.65 s  pusher is at its largest, 0.6 m
 0.65 s  block5 comes to rest at (0.00, 0.00, 0.45) m
 0.66 s  block1 comes to rest at (0.01, 0.00, 0.05) m
 0.69 s  pusher_arm leaves block1_geom
 0.71 s  pusher_paddle leaves block1_geom
 0.82 s  pusher passes 0.16 m from block3 (block3_geom) without touching it: nearest points (-0.05, 0.05, 0.04) m and (-0.05, 0.05, 0.20) m
 0.82 s  pusher passes 0.26 m from block4 (block4_geom) without touching it: nearest points (-0.05, 0.05, 0.04) m and (-0.05, 0.05, 0.30) m
 0.82 s  pusher passes 0.36 m from block5 (block5_geom) without touching it: nearest points (-0.05, 0.05, 0.04) m and (-0.05, 0.05, 0.40) m

State every 0.25 s:
0.00 s: pusher at 0.000 m, moving +1.00 m/s; touching nothing | block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching nothing
0.25 s: pusher at 0.250 m, moving +1.00 m/s; touching nothing | block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
0.50 s: pusher at 0.500 m, moving +1.00 m/s; touching nothing | block1 at (0.00, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
0.75 s: pusher at 0.612 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
1.00 s: pusher at 0.605 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
1.25 s: pusher at 0.599 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
1.50 s: pusher at 0.592 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
1.75 s: pusher at 0.585 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
2.00 s: pusher at 0.579 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
2.25 s: pusher at 0.572 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
2.50 s: pusher at 0.565 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
2.75 s: pusher at 0.558 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
3.00 s: pusher at 0.552 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
3.25 s: pusher at 0.545 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
3.50 s: pusher at 0.538 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
3.75 s: pusher at 0.532 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
4.00 s: pusher at 0.525 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
4.25 s: pusher at 0.518 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
4.50 s: pusher at 0.511 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
4.75 s: pusher at 0.505 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
5.00 s: pusher at 0.498 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
5.25 s: pusher at 0.491 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
5.50 s: pusher at 0.484 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
5.75 s: pusher at 0.478 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
6.00 s: pusher at 0.471 m, moving -0.03 m/s; touching nothing | block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor | block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom | block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom | block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom | block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom

At the end (6.00 s):
- pusher at 0.471 m, moving -0.03 m/s; touching nothing
- block1 at (0.01, 0.00, 0.05) m, at rest; touching block2_geom, floor
- block2 at (0.00, 0.00, 0.15) m, at rest; touching block1_geom, block3_geom
- block3 at (0.00, 0.00, 0.25) m, at rest; touching block2_geom, block4_geom
- block4 at (0.00, 0.00, 0.35) m, at rest; touching block3_geom, block5_geom
- block5 at (0.00, 0.00, 0.45) m, at rest; touching block4_geom
</history>
