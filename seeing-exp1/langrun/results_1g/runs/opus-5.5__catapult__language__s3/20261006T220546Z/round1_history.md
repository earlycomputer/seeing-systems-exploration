Your expectations, checked against the run (0 of 1 hold):

- DOES NOT HOLD: ball comes to rest in bucket (ball comes to rest at (2.16, -0.00, 0.04) m, outside bucket)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- catapult: hinge joint catapult_hinge about axis (0.00, 1.00, 0.00), range 0° to 35° as MuJoCo applies it; its geoms: catapult_arm, catapult_scoop_base, catapult_scoop_back; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (-0.36, 0.00, 0.57) m, at rest

What happened, in order:
 0.00 s  catapult_scoop_base starts touching ball
 0.00 s  catapult starts at its lower stop (0°)
 0.00 s  ball starts moving
 0.00 s  catapult_scoop_back first touches ball
 0.09 s  catapult reaches its upper stop (35°) moving +719°/s
 0.09 s  catapult_scoop_base leaves ball
 0.10 s  catapult_scoop_back leaves ball
 0.10 s  catapult is at its largest, 39.6°
 0.20 s  catapult reaches its upper stop (35°) again moving -11°/s
 0.30 s  ball is at the top of its flight, at (0.45, 0.00, 0.99) m
 0.74 s  ball first touches floor
 0.82 s  ball leaves floor
 0.87 s  ball touches floor again
 0.90 s  ball leaves floor
 0.92 s  ball first touches bucket_near_wall
 0.96 s  ball leaves bucket_near_wall
 0.99 s  ball touches floor again
 1.16 s  ball comes to rest at (2.17, 0.00, 0.04) m

State every 0.25 s:
0.00 s: catapult at 0.0°, still; touching ball | ball at (-0.36, 0.00, 0.57) m, at rest; touching catapult_scoop_base
0.25 s: catapult at 35.2°, turning -1°/s; touching nothing | ball at (0.29, 0.00, 0.98) m, moving 3.42 m/s (vx +3.39, vy +0.00, vz +0.46); touching nothing
0.50 s: catapult at 35.2°, still; touching nothing | ball at (1.13, 0.00, 0.79) m, moving 3.93 m/s (vx +3.39, vy +0.00, vz -2.00); touching nothing
0.75 s: catapult at 35.2°, still; touching nothing | ball at (1.97, 0.00, 0.01) m, moving 1.97 m/s (vx +1.87, vy -0.00, vz -0.61); touching floor
1.00 s: catapult at 35.2°, still; touching nothing | ball at (2.18, 0.00, 0.04) m, moving 0.14 m/s (vx -0.14, vy -0.00, vz -0.05); touching floor
1.25 s: catapult at 35.2°, still; touching nothing | ball at (2.17, 0.00, 0.04) m, at rest; touching floor
1.50 s: catapult at 35.2°, still; touching nothing | ball at (2.16, 0.00, 0.04) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- catapult at 35.2°, still; touching nothing
- ball at (2.16, 0.00, 0.04) m, at rest; touching floor
</history>
