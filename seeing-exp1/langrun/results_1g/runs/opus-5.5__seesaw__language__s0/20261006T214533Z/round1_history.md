Your expectations, checked against the run (2 of 2 hold):

- holds: weight touches seesaw (first touch at 0.62 s)
- holds: ball touches seesaw (first touch at 0.03 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range -15° to 15° as MuJoCo applies it; its geoms: seesaw, seesaw.stop; starts at 15.0°, still
- ball: free body; its geoms: ball; starts at (0.89, 0.00, 0.14) m, at rest
- weight: free body; its geoms: weight; starts at (-0.88, 0.00, 2.50) m, at rest

What happened, in order:
 0.00 s  seesaw starts at its upper stop (15°)
 0.01 s  ball starts moving
 0.01 s  weight starts moving
 0.03 s  seesaw first touches ball
 0.20 s  seesaw.stop first touches ball
 0.62 s  seesaw first touches weight
 0.68 s  seesaw leaves weight
 0.71 s  seesaw leaves ball
 0.71 s  seesaw reaches its lower stop (-15°) moving -342°/s
 0.72 s  seesaw first touches floor
 0.73 s  seesaw.stop leaves ball
 0.73 s  seesaw touches weight again
 0.73 s  seesaw is at its smallest, -17.3°
 0.77 s  seesaw leaves floor
 0.79 s  seesaw reaches its lower stop (-15°) again moving +39°/s
 0.85 s  seesaw leaves weight
 0.85 s  weight is at the top of its flight, at (-1.00, 0.00, 0.14) m
 0.98 s  weight first touches floor
 1.13 s  ball is at the top of its flight, at (-0.15, 0.00, 1.48) m
 1.57 s  seesaw reaches its upper stop (15°) again moving +61°/s
 1.59 s  seesaw is at its largest, 15.4°
 1.67 s  ball first touches floor
 1.69 s  ball passes 0.24 m from weight without touching it: nearest points (-1.58, 0.00, 0.03) m and (-1.82, 0.00, 0.05) m
 3.71 s  ball comes to rest at (-2.43, 0.00, 0.05) m
 6.00 s  weight is still moving at the end, 1.04 m/s

State every 0.25 s:
0.00 s: seesaw at 15.0°, still; touching nothing | ball at (0.89, 0.00, 0.14) m, at rest; touching nothing | weight at (-0.88, 0.00, 2.50) m, at rest; touching nothing
0.25 s: seesaw at 15.0°, still; touching ball | ball at (0.92, 0.00, 0.13) m, at rest; touching seesaw, seesaw.stop | weight at (-0.88, 0.00, 2.20) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing
0.50 s: seesaw at 15.0°, still; touching ball | ball at (0.92, 0.00, 0.13) m, at rest; touching seesaw, seesaw.stop | weight at (-0.88, 0.00, 1.28) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing
0.75 s: seesaw at -16.9°, turning +35°/s; touching floor, weight | ball at (0.81, 0.00, 0.75) m, moving 4.52 m/s (vx -2.50, vy +0.00, vz +3.76); touching nothing | weight at (-0.89, 0.00, 0.09) m, moving 1.29 m/s (vx -1.05, vy +0.00, vz +0.76); touching seesaw
1.00 s: seesaw at -10.3°, turning +27°/s; touching nothing | ball at (0.18, 0.00, 1.39) m, moving 2.82 m/s (vx -2.50, vy +0.00, vz +1.31); touching nothing | weight at (-1.16, 0.00, 0.06) m, moving 1.04 m/s (vx -1.03, vy +0.00, vz +0.13); touching floor
1.25 s: seesaw at -1.7°, turning +42°/s; touching nothing | ball at (-0.44, 0.00, 1.41) m, moving 2.75 m/s (vx -2.50, vy +0.00, vz -1.14); touching nothing | weight at (-1.42, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz +0.00); touching floor
1.50 s: seesaw at 10.7°, turning +57°/s; touching nothing | ball at (-1.07, 0.00, 0.82) m, moving 4.38 m/s (vx -2.50, vy +0.00, vz -3.60); touching nothing | weight at (-1.68, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz +0.00); touching floor
1.75 s: seesaw at 14.8°, still; touching nothing | ball at (-1.58, 0.00, 0.05) m, moving 0.91 m/s (vx -0.87, vy +0.00, vz +0.27); touching floor | weight at (-1.94, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz +0.00); touching floor
2.00 s: seesaw at 15.0°, still; touching nothing | ball at (-1.80, 0.00, 0.05) m, moving 0.80 m/s (vx -0.80, vy +0.00, vz -0.01); touching floor | weight at (-2.20, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz -0.00); touching floor
2.25 s: seesaw at 15.0°, still; touching nothing | ball at (-1.98, 0.00, 0.05) m, moving 0.67 m/s (vx -0.67, vy +0.00, vz +0.00); touching floor | weight at (-2.46, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz -0.00); touching floor
2.50 s: seesaw at 15.0°, still; touching nothing | ball at (-2.13, 0.00, 0.05) m, moving 0.53 m/s (vx -0.53, vy +0.00, vz -0.00); touching floor | weight at (-2.72, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy -0.00, vz +0.00); touching floor
2.75 s: seesaw at 15.0°, still; touching nothing | ball at (-2.25, 0.00, 0.05) m, moving 0.40 m/s (vx -0.40, vy +0.00, vz +0.00); touching floor | weight at (-2.98, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz +0.00); touching floor
3.00 s: seesaw at 15.0°, still; touching nothing | ball at (-2.33, 0.00, 0.05) m, moving 0.27 m/s (vx -0.27, vy +0.00, vz -0.01); touching floor | weight at (-3.24, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz -0.00); touching floor
3.25 s: seesaw at 15.0°, still; touching nothing | ball at (-2.38, 0.00, 0.05) m, moving 0.16 m/s (vx -0.16, vy +0.00, vz -0.00); touching floor | weight at (-3.50, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz -0.00); touching floor
3.50 s: seesaw at 15.0°, still; touching nothing | ball at (-2.41, 0.00, 0.05) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz -0.00); touching floor | weight at (-3.76, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz +0.00); touching floor
3.75 s: seesaw at 15.0°, still; touching nothing | ball at (-2.43, 0.00, 0.05) m, at rest; touching floor | weight at (-4.02, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz +0.00); touching floor
4.00 s: seesaw at 15.0°, still; touching nothing | ball at (-2.44, 0.00, 0.05) m, at rest; touching floor | weight at (-4.28, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz -0.00); touching floor
4.25 s: seesaw at 15.0°, still; touching nothing | ball at (-2.44, 0.00, 0.05) m, at rest; touching floor | weight at (-4.54, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz -0.00); touching floor
4.50 s: seesaw at 15.0°, still; touching nothing | ball at (-2.44, 0.00, 0.05) m, at rest; touching floor | weight at (-4.80, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz +0.00); touching floor
4.75 s: seesaw at 15.0°, still; touching nothing | ball at (-2.44, 0.00, 0.05) m, at rest; touching floor | weight at (-5.06, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz +0.00); touching floor
5.00 s: seesaw at 15.0°, still; touching nothing | ball at (-2.44, 0.00, 0.05) m, at rest; touching floor | weight at (-5.32, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz -0.00); touching floor
5.25 s: seesaw at 15.0°, still; touching nothing | ball at (-2.44, 0.00, 0.05) m, at rest; touching floor | weight at (-5.58, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz -0.00); touching floor
5.50 s: seesaw at 15.0°, still; touching nothing | ball at (-2.44, 0.00, 0.05) m, at rest; touching floor | weight at (-5.84, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz +0.00); touching floor
5.75 s: seesaw at 15.0°, still; touching nothing | ball at (-2.44, 0.00, 0.05) m, at rest; touching floor | weight at (-6.10, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz +0.00); touching floor
6.00 s: seesaw at 15.0°, still; touching nothing | ball at (-2.44, 0.00, 0.05) m, at rest; touching floor | weight at (-6.36, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz -0.00); touching floor

At the end (6.00 s):
- seesaw at 15.0°, still; touching nothing
- ball at (-2.44, 0.00, 0.05) m, at rest; touching floor
- weight at (-6.36, 0.00, 0.06) m, moving 1.04 m/s (vx -1.04, vy +0.00, vz -0.00); touching floor
</history>
