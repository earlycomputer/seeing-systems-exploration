Your expectations, checked against the run (1 of 2 hold):

- holds: ball touches bucket (first touch at 0.87 s)
- DOES NOT HOLD: ball comes to rest in bucket (ball comes to rest at (2.01, 0.00, 0.03) m, outside bucket)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- catapult: hinge joint catapult_hinge about axis (0.00, 1.00, 0.00), range 0° to 38° as MuJoCo applies it; its geoms: catapult_arm, catapult_scoop_base, catapult_scoop_back; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (-0.52, 0.00, 0.56) m, at rest

What happened, in order:
 0.00 s  catapult starts at its lower stop (0°)
 0.00 s  catapult_scoop_base first touches ball
 0.00 s  ball starts moving
 0.12 s  catapult_scoop_back first touches ball
 0.14 s  catapult reaches its upper stop (38°) moving +469°/s
 0.14 s  catapult_scoop_base leaves ball
 0.15 s  catapult_scoop_back leaves ball
 0.16 s  catapult is at its largest, 41.4°
 0.23 s  catapult reaches its upper stop (38°) again moving -17°/s
 0.36 s  ball is at the top of its flight, at (0.35, 0.00, 1.16) m
 0.84 s  ball first touches floor
 0.87 s  ball first touches bucket_near_wall
 0.89 s  ball leaves floor
 0.90 s  ball leaves bucket_near_wall
 0.99 s  ball is at the top of its flight, at (2.02, 0.00, 0.08) m
 1.09 s  ball touches floor again
 1.16 s  ball comes to rest at (2.01, 0.00, 0.03) m

State every 0.25 s:
0.00 s: catapult at 0.0°, still; touching nothing | ball at (-0.52, 0.00, 0.56) m, at rest; touching nothing
0.25 s: catapult at 38.3°, turning -7°/s; touching nothing | ball at (-0.04, 0.00, 1.09) m, moving 3.59 m/s (vx +3.42, vy +0.00, vz +1.10); touching nothing
0.50 s: catapult at 38.1°, still; touching nothing | ball at (0.82, 0.00, 1.07) m, moving 3.68 m/s (vx +3.42, vy +0.00, vz -1.35); touching nothing
0.75 s: catapult at 38.1°, still; touching nothing | ball at (1.67, 0.00, 0.42) m, moving 5.11 m/s (vx +3.42, vy +0.00, vz -3.80); touching nothing
1.00 s: catapult at 38.1°, still; touching nothing | ball at (2.02, 0.00, 0.08) m, moving 0.24 m/s (vx -0.20, vy -0.00, vz -0.14); touching nothing
1.25 s: catapult at 38.1°, still; touching nothing | ball at (2.01, 0.00, 0.03) m, at rest; touching floor
(the same through 6.00 s)

At the end (6.00 s):
- catapult at 38.1°, still; touching nothing
- ball at (2.01, 0.00, 0.03) m, at rest; touching floor
</history>
