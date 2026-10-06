Your expectations, checked against the run (1 of 2 hold):

- holds: catapult reaches its upper stop (at its upper stop (45°) at 0.17 s)
- DOES NOT HOLD: ball comes to rest in bucket (ball comes to rest at (1.92, 0.00, 0.04) m, outside bucket)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- catapult: hinge joint catapult_hinge about axis (0.00, 1.00, 0.00), range 0° to 45° as MuJoCo applies it; its geoms: catapult_arm, catapult_scoop_base, catapult_scoop_back; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (-0.56, 0.00, 0.57) m, at rest

What happened, in order:
 0.00 s  catapult_scoop_back starts touching ball
 0.00 s  catapult_scoop_base starts touching ball
 0.00 s  catapult starts at its lower stop (0°)
 0.00 s  ball starts moving
 0.17 s  catapult reaches its upper stop (45°) moving +457°/s
 0.17 s  catapult_scoop_base leaves ball
 0.18 s  catapult_scoop_back leaves ball
 0.19 s  catapult is at its largest, 48.0°
 0.26 s  catapult reaches its upper stop (45°) again moving -18°/s
 0.36 s  ball is at the top of its flight, at (0.30, 0.00, 1.12) m
 0.83 s  ball first touches floor
 0.84 s  ball first touches bucket_near_wall
 0.86 s  ball leaves floor
 0.86 s  ball leaves bucket_near_wall
 0.97 s  ball is at the top of its flight, at (1.96, 0.00, 0.10) m
 1.08 s  ball touches floor again
 1.13 s  ball comes to rest at (1.92, 0.00, 0.04) m

State every 0.25 s:
0.00 s: catapult at 0.0°, still; touching ball | ball at (-0.56, 0.00, 0.57) m, at rest; touching catapult_scoop_back, catapult_scoop_base
0.25 s: catapult at 45.6°, turning -21°/s; touching nothing | ball at (-0.08, 0.00, 1.06) m, moving 3.68 m/s (vx +3.54, vy +0.00, vz +1.04); touching nothing
0.50 s: catapult at 45.1°, still; touching nothing | ball at (0.80, 0.00, 1.02) m, moving 3.81 m/s (vx +3.54, vy +0.00, vz -1.42); touching nothing
0.75 s: catapult at 45.1°, still; touching nothing | ball at (1.69, 0.00, 0.36) m, moving 5.24 m/s (vx +3.54, vy +0.00, vz -3.87); touching nothing
1.00 s: catapult at 45.1°, still; touching nothing | ball at (1.95, 0.00, 0.09) m, moving 0.45 m/s (vx -0.31, vy +0.00, vz -0.33); touching nothing
1.25 s: catapult at 45.1°, still; touching nothing | ball at (1.92, 0.00, 0.04) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- catapult at 45.1°, still; touching nothing
- ball at (1.92, 0.00, 0.04) m, at rest; touching floor
</history>
