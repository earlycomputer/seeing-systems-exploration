MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block1: free body; its geoms: block1; starts at (0.00, 0.00, 0.10) m, at rest
- block2: free body; its geoms: block2; starts at (0.00, 0.00, 0.30) m, at rest
- block3: free body; its geoms: block3; starts at (0.00, 0.00, 0.50) m, at rest
- block4: free body; its geoms: block4; starts at (0.00, 0.00, 0.70) m, at rest
- block5: free body; its geoms: block5; starts at (0.00, 0.00, 0.90) m, at rest
- pusher: slide joint pusher_slide about axis (1.00, 0.00, 0.00), range 0 m to 1.8 m as MuJoCo applies it; its geoms: pusher; starts at 0.000 m, still

What happened, in order:
 0.00 s  block1 starts touching floor
 0.00 s  block1 starts touching block2
 0.00 s  block2 starts touching block3
 0.00 s  block3 starts touching block4
 0.00 s  pusher starts at its lower stop (0 m)
 0.01 s  block4 first touches block5
 0.01 s  block5 starts moving
 0.54 s  block1 leaves floor
 0.54 s  block1 first touches pusher
 0.54 s  block1 starts moving
 0.54 s  block2 starts moving
 0.54 s  block3 starts moving
 0.54 s  block4 starts moving
 0.54 s  block1 leaves block2
 0.58 s  block1 touches floor again
 0.59 s  block1 touches block2 again
 0.59 s  block1 leaves pusher
 0.63 s  block1 touches pusher again
 0.64 s  block1 leaves floor
 0.64 s  block1 leaves block2
 0.64 s  block1 leaves pusher
 0.66 s  block2 leaves block3
 0.67 s  block3 leaves block4
 0.68 s  block1 touches floor again
 0.68 s  block1 touches pusher again
 0.68 s  block1 leaves floor
 0.69 s  block4 leaves block5
 0.70 s  block1 touches block2 again
 0.71 s  block1 leaves block2
 0.72 s  block2 first touches pusher
 0.72 s  block1 touches floor again
 0.72 s  block2 touches block3 again
 0.72 s  block1 leaves pusher
 0.73 s  block3 touches block4 again
 0.74 s  block4 touches block5 again
 0.75 s  block1 leaves floor
 0.77 s  block1 touches pusher again
 0.81 s  block2 leaves block3
 0.81 s  block1 touches floor 6 more times between 0.81 s and 6.00 s, still touching at the end
 0.82 s  block3 leaves block4
 0.83 s  block4 leaves block5
 0.88 s  block1 leaves pusher
 0.94 s  pusher reaches its upper stop (1.8 m) moving +1.99 m/s
 0.94 s  block1 touches pusher 1 more times between 0.94 s and 0.94 s
 0.94 s  block2 leaves pusher
 0.96 s  pusher is at its largest, 1.8 m
 0.98 s  block2 touches pusher again
 1.01 s  pusher reaches its upper stop (1.8 m) again moving -0.14 m/s
 1.04 s  block3 first touches floor
 1.05 s  block4 first touches floor
 1.06 s  block5 first touches floor
 1.14 s  block3 comes to rest at (0.35, 0.00, 0.10) m
 1.14 s  block2 comes to rest at (0.61, 0.00, 0.25) m
 1.15 s  block4 passes 0.34 m from pusher without touching it: nearest points (0.18, -0.10, 0.15) m and (0.52, -0.10, 0.15) m
 1.16 s  block4 comes to rest at (0.08, 0.00, 0.10) m
 1.26 s  block1 comes to rest at (1.08, 0.00, 0.10) m
 1.38 s  block5 comes to rest at (-0.22, 0.00, 0.10) m
 1.79 s  block3 passes 0.07 m from pusher without touching it: nearest points (0.45, -0.10, 0.15) m and (0.52, -0.10, 0.15) m

State every 0.25 s:
0.00 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3 | block5 at (0.00, 0.00, 0.90) m, at rest; touching nothing | pusher at 0.000 m, still; touching nothing
0.25 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4 | pusher at 0.451 m, moving +1.99 m/s; touching nothing
0.50 s: block1 at (0.00, 0.00, 0.10) m, at rest; touching block2, floor | block2 at (0.00, 0.00, 0.30) m, at rest; touching block1, block3 | block3 at (0.00, 0.00, 0.50) m, at rest; touching block2, block4 | block4 at (0.00, 0.00, 0.70) m, at rest; touching block3, block5 | block5 at (0.00, 0.00, 0.90) m, at rest; touching block4 | pusher at 0.948 m, moving +1.99 m/s; touching nothing
0.75 s: block1 at (0.41, 0.00, 0.10) m, moving 1.94 m/s (vx +1.94, vy -0.00, vz -0.05); touching floor | block2 at (0.20, 0.00, 0.28) m, moving 1.56 m/s (vx +1.54, vy -0.00, vz +0.25), turned 27° from how it started; touching block3, pusher | block3 at (0.11, 0.00, 0.45) m, moving 0.93 m/s (vx +0.93, vy -0.00, vz -0.02), turned 28° from how it started; touching block2, block4 | block4 at (0.02, 0.00, 0.63) m, moving 0.69 m/s (vx +0.18, vy -0.00, vz -0.67), turned 26° from how it started; touching block3, block5 | block5 at (-0.05, 0.00, 0.82) m, moving 1.18 m/s (vx -0.66, vy -0.00, vz -0.98), turned 23° from how it started; touching block4 | pusher at 1.425 m, moving +1.97 m/s; touching block2
1.00 s: block1 at (0.88, 0.00, 0.10) m, moving 1.39 m/s (vx +1.37, vy +0.00, vz +0.25); touching nothing | block2 at (0.55, 0.00, 0.26) m, moving 1.22 m/s (vx +1.12, vy -0.00, vz -0.49), turned 85° from how it started; touching nothing | block3 at (0.31, 0.00, 0.19) m, moving 2.43 m/s (vx +0.82, vy -0.00, vz -2.29), turned 81° from how it started; touching nothing | block4 at (0.05, 0.00, 0.26) m, moving 2.71 m/s (vx +0.12, vy -0.00, vz -2.71), turned 87° from how it started; touching nothing | block5 at (-0.24, 0.00, 0.33) m, moving 3.28 m/s (vx -0.74, vy -0.00, vz -3.20), turned 102° from how it started; touching nothing | pusher at 1.806 m, moving -0.16 m/s; touching nothing
1.25 s: block1 at (1.08, 0.00, 0.10) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz -0.02); touching nothing | block2 at (0.61, 0.00, 0.25) m, at rest, turned 90° from how it started; touching pusher | block3 at (0.35, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (0.08, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.24, 0.00, 0.12) m, moving 0.51 m/s (vx +0.43, vy +0.00, vz -0.27), turned 102° from how it started; touching floor | pusher at 1.801 m, still; touching block2
1.50 s: block1 at (1.08, 0.00, 0.10) m, at rest; touching floor | block2 at (0.61, 0.00, 0.25) m, at rest, turned 90° from how it started; touching pusher | block3 at (0.35, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block4 at (0.08, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | block5 at (-0.22, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor | pusher at 1.801 m, still; touching block2
(the same through 6.00 s)

At the end (6.00 s):
- block1 at (1.08, 0.00, 0.10) m, at rest; touching floor
- block2 at (0.61, 0.00, 0.25) m, at rest, turned 90° from how it started; touching pusher
- block3 at (0.35, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- block4 at (0.08, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- block5 at (-0.22, 0.00, 0.10) m, at rest, turned 90° from how it started; touching floor
- pusher at 1.801 m, still; touching block2
</history>
