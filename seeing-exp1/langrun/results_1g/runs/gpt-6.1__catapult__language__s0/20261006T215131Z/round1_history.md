Your expectations, checked against the run (1 of 2 hold):

- holds: ball touches catapult (touching from the start)
- DOES NOT HOLD: ball comes to rest in bucket (ball comes to rest at (1.64, -0.00, 0.04) m, outside bucket)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- catapult: hinge joint catapult_hinge about axis (0.00, 1.00, 0.00), range 0° to 50° as MuJoCo applies it; its geoms: catapult_arm, catapult_scoop_base, catapult_scoop_back; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (-0.76, 0.00, 0.47) m, at rest

What happened, in order:
 0.00 s  catapult_scoop_base starts touching ball
 0.00 s  catapult starts at its lower stop (0°)
 0.00 s  catapult_scoop_back first touches ball
 0.00 s  ball starts moving
 0.27 s  catapult reaches its upper stop (50°) moving +313°/s
 0.27 s  catapult_scoop_base leaves ball
 0.28 s  catapult_scoop_back leaves ball
 0.29 s  catapult is at its largest, 52.1°
 0.35 s  catapult reaches its upper stop (50°) again moving -18°/s
 0.44 s  ball is at the top of its flight, at (0.09, 0.00, 1.17) m
 0.92 s  ball first touches floor
 0.94 s  ball first touches bucket_near_wall
 1.01 s  ball comes to rest at (1.64, 0.00, 0.04) m
 1.43 s  ball leaves bucket_near_wall

State every 0.25 s:
0.00 s: catapult at 0.0°, still; touching ball | ball at (-0.76, 0.00, 0.47) m, at rest; touching catapult_scoop_base
0.25 s: catapult at 43.5°, turning +302°/s; touching ball | ball at (-0.50, 0.00, 0.97) m, moving 4.01 m/s (vx +3.02, vy -0.00, vz +2.65); touching catapult_scoop_back, catapult_scoop_base
0.50 s: catapult at 50.0°, still; touching nothing | ball at (0.28, 0.00, 1.15) m, moving 3.18 m/s (vx +3.13, vy -0.00, vz -0.59); touching nothing
0.75 s: catapult at 50.0°, still; touching nothing | ball at (1.06, 0.00, 0.70) m, moving 4.36 m/s (vx +3.13, vy -0.00, vz -3.04); touching nothing
1.00 s: catapult at 50.0°, still; touching nothing | ball at (1.64, 0.00, 0.04) m, moving 0.07 m/s (vx -0.02, vy +0.00, vz +0.06); touching bucket_near_wall, floor
1.25 s: catapult at 50.0°, still; touching nothing | ball at (1.64, 0.00, 0.04) m, at rest; touching bucket_near_wall, floor
1.50 s: catapult at 50.0°, still; touching nothing | ball at (1.64, 0.00, 0.04) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- catapult at 50.0°, still; touching nothing
- ball at (1.64, 0.00, 0.04) m, at rest; touching floor
</history>
