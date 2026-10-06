Your expectations, checked against the run (3 of 3 hold):

- holds: weight touches seesaw (first touch at 0.62 s)
- holds: ball touches seesaw (first touch at 0.00 s)
- holds: seesaw reaches its lower stop (at its lower stop (-34°) at 0.73 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range -34.3775° to 0° as MuJoCo applies it; its geoms: seesaw_plank, seesaw_stop; starts at 0.0°, still
- weight: free body; its geoms: weight; starts at (-0.85, 0.00, 2.60) m, at rest
- ball: free body; its geoms: ball; starts at (0.94, 0.00, 0.13) m, at rest

What happened, in order:
 0.00 s  seesaw starts at its upper stop (0°)
 0.00 s  seesaw_plank first touches ball
 0.01 s  seesaw_stop first touches ball
 0.01 s  weight starts moving
 0.62 s  seesaw_plank first touches weight
 0.62 s  ball starts moving
 0.70 s  seesaw_plank leaves weight
 0.73 s  seesaw reaches its lower stop (-34.3775°) moving -356°/s
 0.73 s  seesaw_plank leaves ball
 0.74 s  seesaw_plank first touches floor
 0.74 s  seesaw_plank touches weight again
 0.74 s  seesaw_stop leaves ball
 0.75 s  seesaw is at its smallest, -36.7°
 0.78 s  seesaw_plank leaves floor
 0.80 s  seesaw reaches its lower stop (-34.3775°) again moving +34°/s
 0.94 s  seesaw_plank leaves weight
 0.98 s  seesaw reaches its lower stop (-34.3775°) again moving -12°/s
 1.01 s  weight first touches floor
 1.14 s  ball is at the top of its flight, at (-0.30, 0.00, 1.54) m
 1.66 s  weight first touches ball
 1.73 s  weight leaves ball
 1.87 s  ball first touches floor
 2.15 s  seesaw reaches its upper stop (0°) again moving +61°/s
 2.18 s  seesaw is at its largest, 0.4°
 6.00 s  weight is still moving at the end, 1.23 m/s
 6.00 s  ball is still moving at the end, 1.71 m/s

State every 0.25 s:
0.00 s: seesaw at 0.0°, still; touching nothing | weight at (-0.85, 0.00, 2.60) m, at rest; touching nothing | ball at (0.94, 0.00, 0.13) m, at rest; touching nothing
0.25 s: seesaw at 0.0°, still; touching ball | weight at (-0.85, 0.00, 2.30) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | ball at (0.94, 0.00, 0.13) m, at rest; touching seesaw_plank, seesaw_stop
0.50 s: seesaw at 0.0°, still; touching ball | weight at (-0.85, 0.00, 1.38) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing | ball at (0.94, 0.00, 0.13) m, at rest; touching seesaw_plank, seesaw_stop
0.75 s: seesaw at -36.6°, turning +7°/s; touching floor, weight | weight at (-0.84, 0.00, 0.14) m, moving 1.05 m/s (vx -0.73, vy -0.00, vz -0.75); touching seesaw_plank | ball at (0.85, 0.00, 0.79) m, moving 4.84 m/s (vx -2.97, vy -0.00, vz +3.83); touching nothing
1.00 s: seesaw at -34.1°, turning -11°/s; touching nothing | weight at (-1.11, 0.00, 0.10) m, moving 1.64 m/s (vx -1.09, vy -0.00, vz -1.22); touching nothing | ball at (0.11, 0.00, 1.44) m, moving 3.27 m/s (vx -2.97, vy -0.00, vz +1.37); touching nothing
1.25 s: seesaw at -33.2°, turning +11°/s; touching nothing | weight at (-1.39, 0.00, 0.08) m, moving 1.12 m/s (vx -1.12, vy -0.00, vz -0.00); touching floor | ball at (-0.63, 0.00, 1.48) m, moving 3.16 m/s (vx -2.97, vy -0.00, vz -1.08); touching nothing
1.50 s: seesaw at -28.7°, turning +25°/s; touching nothing | weight at (-1.67, 0.00, 0.08) m, moving 1.12 m/s (vx -1.12, vy -0.00, vz -0.00); touching floor | ball at (-1.37, 0.00, 0.91) m, moving 4.61 m/s (vx -2.97, vy -0.00, vz -3.53); touching nothing
1.75 s: seesaw at -20.7°, turning +39°/s; touching nothing | weight at (-1.96, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz +0.00); touching floor | ball at (-2.07, 0.00, 0.17) m, moving 2.49 m/s (vx -2.45, vy -0.00, vz -0.42); touching nothing
2.00 s: seesaw at -9.3°, turning +53°/s; touching nothing | weight at (-2.27, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz +0.00); touching floor | ball at (-2.59, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.01); touching floor
2.25 s: seesaw at -0.0°, turning -4°/s; touching nothing | weight at (-2.58, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz -0.00); touching floor | ball at (-3.02, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.00); touching floor
2.50 s: seesaw at 0.0°, still; touching nothing | weight at (-2.89, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz +0.00); touching floor | ball at (-3.45, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor
2.75 s: seesaw at 0.0°, still; touching nothing | weight at (-3.19, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz -0.00); touching floor | ball at (-3.88, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.00); touching floor
3.00 s: seesaw at 0.0°, still; touching nothing | weight at (-3.50, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz -0.00); touching floor | ball at (-4.31, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.00); touching floor
3.25 s: seesaw at 0.0°, still; touching nothing | weight at (-3.81, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz -0.00); touching floor | ball at (-4.73, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.00); touching floor
3.50 s: seesaw at 0.0°, still; touching nothing | weight at (-4.12, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz -0.00); touching floor | ball at (-5.16, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.00); touching floor
3.75 s: seesaw at 0.0°, still; touching nothing | weight at (-4.43, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz +0.00); touching floor | ball at (-5.59, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.00); touching floor
4.00 s: seesaw at 0.0°, still; touching nothing | weight at (-4.74, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz +0.00); touching floor | ball at (-6.02, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.00); touching floor
4.25 s: seesaw at 0.0°, still; touching nothing | weight at (-5.05, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz +0.00); touching floor | ball at (-6.45, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.00); touching floor
4.50 s: seesaw at 0.0°, still; touching nothing | weight at (-5.35, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz +0.00); touching floor | ball at (-6.88, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.00); touching floor
4.75 s: seesaw at 0.0°, still; touching nothing | weight at (-5.66, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz +0.00); touching floor | ball at (-7.31, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor
5.00 s: seesaw at 0.0°, still; touching nothing | weight at (-5.97, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz +0.00); touching floor | ball at (-7.73, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor
5.25 s: seesaw at 0.0°, still; touching nothing | weight at (-6.28, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz +0.00); touching floor | ball at (-8.16, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.00); touching floor
5.50 s: seesaw at 0.0°, still; touching nothing | weight at (-6.59, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz +0.00); touching floor | ball at (-8.59, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz +0.00); touching floor
5.75 s: seesaw at 0.0°, still; touching nothing | weight at (-6.90, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz +0.00); touching floor | ball at (-9.02, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor
6.00 s: seesaw at 0.0°, still; touching nothing | weight at (-7.21, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz +0.00); touching floor | ball at (-9.45, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor

At the end (6.00 s):
- seesaw at 0.0°, still; touching nothing
- weight at (-7.21, 0.00, 0.08) m, moving 1.23 m/s (vx -1.23, vy +0.00, vz +0.00); touching floor
- ball at (-9.45, 0.00, 0.05) m, moving 1.71 m/s (vx -1.71, vy -0.00, vz -0.00); touching floor
</history>
