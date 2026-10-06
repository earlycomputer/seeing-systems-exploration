Your expectations, checked against the run (1 of 2 hold):

- holds: ball touches bucket (first touch at 0.97 s)
- DOES NOT HOLD: ball comes to rest in bucket (ball comes to rest at (1.23, -0.00, 0.04) m, outside bucket)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- catapult: hinge joint catapult_hinge about axis (0.00, 1.00, 0.00), range 0° to 45° as MuJoCo applies it; its geoms: catapult_arm, catapult_scoop_base, catapult_scoop_back; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (-0.96, 0.00, 0.67) m, at rest

What happened, in order:
 0.00 s  catapult_scoop_back starts touching ball
 0.00 s  catapult starts at its lower stop (0°)
 0.00 s  catapult_scoop_back leaves ball
 0.00 s  catapult_scoop_base first touches ball
 0.00 s  ball starts moving
 0.05 s  catapult_scoop_back touches ball again
 0.30 s  catapult reaches its upper stop (45°) moving +252°/s
 0.31 s  catapult_scoop_base leaves ball
 0.31 s  catapult_scoop_back leaves ball
 0.32 s  catapult is at its largest, 46.7°
 0.37 s  catapult reaches its upper stop (45°) again moving -18°/s
 0.51 s  ball is at the top of its flight, at (0.04, 0.00, 1.54) m
 0.97 s  ball first touches bucket_near_wall
 0.98 s  ball leaves bucket_near_wall
 1.10 s  ball first touches floor
 1.15 s  ball leaves floor
 1.21 s  ball touches floor again
 1.60 s  ball comes to rest at (1.24, 0.00, 0.04) m

State every 0.25 s:
0.00 s: catapult at 0.0°, still; touching ball | ball at (-0.96, 0.00, 0.67) m, at rest; touching catapult_scoop_back
0.25 s: catapult at 31.7°, turning +227°/s; touching ball | ball at (-0.79, 0.00, 1.16) m, moving 3.82 m/s (vx +2.21, vy -0.00, vz +3.12); touching catapult_scoop_back, catapult_scoop_base
0.50 s: catapult at 45.0°, still; touching nothing | ball at (0.00, 0.00, 1.54) m, moving 3.31 m/s (vx +3.30, vy +0.00, vz +0.10); touching nothing
0.75 s: catapult at 45.0°, still; touching nothing | ball at (0.83, 0.00, 1.26) m, moving 4.06 m/s (vx +3.30, vy +0.00, vz -2.35); touching nothing
1.00 s: catapult at 45.0°, still; touching nothing | ball at (1.53, 0.00, 0.41) m, moving 3.50 m/s (vx -0.86, vy +0.00, vz -3.40); touching nothing
1.25 s: catapult at 45.0°, still; touching nothing | ball at (1.34, 0.00, 0.04) m, moving 0.58 m/s (vx -0.58, vy -0.00, vz -0.06); touching nothing
1.50 s: catapult at 45.0°, still; touching nothing | ball at (1.25, 0.00, 0.04) m, moving 0.19 m/s (vx -0.19, vy -0.00, vz +0.02); touching floor
1.75 s: catapult at 45.0°, still; touching nothing | ball at (1.23, 0.00, 0.04) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- catapult at 45.0°, still; touching nothing
- ball at (1.23, 0.00, 0.04) m, at rest; touching floor
</history>
