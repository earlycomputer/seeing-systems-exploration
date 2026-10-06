Your expectations, checked against the run (4 of 4 hold):

- holds: weight touches seesaw (first touch at 0.54 s)
- holds: ball touches seesaw (touching from the start)
- holds: seesaw reaches its lower stop (at its lower stop (-28°) at 0.62 s)
- holds: ball touches floor (first touch at 2.18 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range -28° to 0° as MuJoCo applies it; its geoms: seesaw_beam; starts at 0.0°, still
- weight: free body; its geoms: weight_sphere; starts at (-0.80, 0.00, 2.20) m, at rest
- ball: free body; its geoms: ball; starts at (0.80, 0.00, 0.70) m, at rest

What happened, in order:
 0.00 s  seesaw_beam starts touching ball
 0.00 s  seesaw starts at its upper stop (0°)
 0.00 s  seesaw is at its largest, 0.0°
 0.01 s  weight starts moving
 0.54 s  seesaw_beam first touches weight_sphere
 0.54 s  ball starts moving
 0.59 s  seesaw_beam leaves weight_sphere
 0.62 s  seesaw reaches its lower stop (-28°) moving -330°/s
 0.62 s  seesaw_beam leaves ball
 0.63 s  seesaw_beam touches weight_sphere again
 0.63 s  weight passes 0.48 m from support (support_base) without touching it: nearest points (-0.68, 0.00, 0.30) m and (-0.25, 0.00, 0.10) m
 0.72 s  seesaw_beam leaves weight_sphere
 0.81 s  weight_sphere first touches floor
 1.17 s  ball is at the top of its flight, at (0.32, 0.00, 2.58) m
 1.80 s  ball passes 0.08 m from support (support_axle) without touching it: nearest points (-0.12, 0.00, 0.61) m and (-0.04, 0.00, 0.60) m
 1.80 s  seesaw_beam touches ball again
 1.80 s  seesaw is at its smallest, -28.1°
 1.81 s  seesaw_beam leaves ball
 1.98 s  seesaw_beam touches ball again
 1.99 s  seesaw_beam leaves ball
 2.02 s  seesaw reaches its lower stop (-28°) again moving -34°/s
 2.04 s  seesaw_beam touches ball again
 2.10 s  seesaw_beam leaves ball
 2.18 s  ball first touches floor
 4.55 s  ball leaves floor
 4.55 s  weight_sphere first touches ball
 4.55 s  weight_sphere leaves ball
 4.59 s  ball touches floor again
 6.00 s  weight is still moving at the end, 1.99 m/s
 6.00 s  ball is still moving at the end, 0.98 m/s

State every 0.25 s:
0.00 s: seesaw at 0.0°, still; touching ball | weight at (-0.80, 0.00, 2.20) m, at rest; touching nothing | ball at (0.80, 0.00, 0.70) m, at rest; touching seesaw_beam
0.25 s: seesaw at 0.0°, still; touching ball | weight at (-0.80, 0.00, 1.90) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | ball at (0.80, 0.00, 0.70) m, at rest; touching seesaw_beam
0.50 s: seesaw at 0.0°, still; touching ball | weight at (-0.80, 0.00, 0.98) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing | ball at (0.80, 0.00, 0.70) m, at rest; touching seesaw_beam
0.75 s: seesaw at -28.0°, still; touching nothing | weight at (-1.02, 0.00, 0.24) m, moving 2.23 m/s (vx -1.82, vy -0.00, vz -1.28); touching nothing | ball at (0.66, 0.00, 1.72) m, moving 4.18 m/s (vx -0.82, vy -0.00, vz +4.10); touching nothing
1.00 s: seesaw at -27.9°, still; touching nothing | weight at (-1.49, 0.00, 0.14) m, moving 1.89 m/s (vx -1.89, vy -0.00, vz +0.00); touching floor | ball at (0.45, 0.00, 2.44) m, moving 1.84 m/s (vx -0.82, vy -0.00, vz +1.65); touching nothing
1.25 s: seesaw at -27.9°, still; touching nothing | weight at (-1.96, 0.00, 0.14) m, moving 1.89 m/s (vx -1.89, vy +0.00, vz -0.00); touching floor | ball at (0.25, 0.00, 2.55) m, moving 1.15 m/s (vx -0.82, vy -0.00, vz -0.81); touching nothing
1.50 s: seesaw at -27.8°, still; touching nothing | weight at (-2.43, 0.00, 0.14) m, moving 1.89 m/s (vx -1.89, vy +0.00, vz -0.00); touching floor | ball at (0.05, 0.00, 2.04) m, moving 3.36 m/s (vx -0.82, vy -0.00, vz -3.26); touching nothing
1.75 s: seesaw at -27.8°, still; touching nothing | weight at (-2.91, 0.00, 0.14) m, moving 1.89 m/s (vx -1.89, vy +0.00, vz -0.00); touching floor | ball at (-0.16, 0.00, 0.92) m, moving 5.77 m/s (vx -0.82, vy -0.00, vz -5.71); touching nothing
2.00 s: seesaw at -26.9°, turning -34°/s; touching nothing | weight at (-3.38, 0.00, 0.14) m, moving 1.89 m/s (vx -1.89, vy +0.00, vz +0.00); touching floor | ball at (-0.66, 0.00, 0.38) m, moving 2.87 m/s (vx -2.39, vy -0.00, vz -1.59); touching nothing
2.25 s: seesaw at -28.0°, still; touching nothing | weight at (-3.85, 0.00, 0.14) m, moving 1.89 m/s (vx -1.89, vy -0.00, vz +0.00); touching floor | ball at (-1.34, 0.00, 0.08) m, moving 2.89 m/s (vx -2.89, vy -0.00, vz +0.00); touching floor
2.50 s: seesaw at -28.0°, still; touching nothing | weight at (-4.32, 0.00, 0.14) m, moving 1.89 m/s (vx -1.89, vy -0.00, vz -0.00); touching floor | ball at (-2.07, 0.00, 0.08) m, moving 2.89 m/s (vx -2.89, vy -0.00, vz -0.00); touching floor
2.75 s: seesaw at -28.0°, still; touching nothing | weight at (-4.80, 0.00, 0.14) m, moving 1.89 m/s (vx -1.89, vy -0.00, vz -0.00); touching floor | ball at (-2.79, 0.00, 0.08) m, moving 2.89 m/s (vx -2.89, vy -0.00, vz -0.00); touching floor
3.00 s: seesaw at -28.0°, still; touching nothing | weight at (-5.27, 0.00, 0.14) m, moving 1.89 m/s (vx -1.89, vy -0.00, vz -0.00); touching floor | ball at (-3.51, 0.00, 0.08) m, moving 2.89 m/s (vx -2.89, vy -0.00, vz -0.00); touching floor
3.25 s: seesaw at -28.0°, still; touching nothing | weight at (-5.74, 0.00, 0.14) m, moving 1.89 m/s (vx -1.89, vy -0.00, vz -0.00); touching floor | ball at (-4.23, 0.00, 0.08) m, moving 2.89 m/s (vx -2.89, vy -0.00, vz -0.00); touching floor
3.50 s: seesaw at -28.0°, still; touching nothing | weight at (-6.22, 0.00, 0.14) m, moving 1.89 m/s (vx -1.89, vy -0.00, vz +0.00); touching floor | ball at (-4.96, 0.00, 0.08) m, moving 2.89 m/s (vx -2.89, vy -0.00, vz +0.00); touching floor
3.75 s: seesaw at -28.0°, still; touching nothing | weight at (-6.69, 0.00, 0.14) m, moving 1.89 m/s (vx -1.89, vy -0.00, vz -0.00); touching floor | ball at (-5.68, 0.00, 0.08) m, moving 2.89 m/s (vx -2.89, vy -0.00, vz +0.00); touching floor
4.00 s: seesaw at -28.0°, still; touching nothing | weight at (-7.16, 0.00, 0.14) m, moving 1.89 m/s (vx -1.89, vy -0.00, vz +0.00); touching floor | ball at (-6.40, 0.00, 0.08) m, moving 2.89 m/s (vx -2.89, vy -0.00, vz -0.00); touching floor
4.25 s: seesaw at -28.0°, still; touching nothing | weight at (-7.64, 0.00, 0.14) m, moving 1.89 m/s (vx -1.89, vy -0.00, vz +0.00); touching floor | ball at (-7.12, 0.00, 0.08) m, moving 2.89 m/s (vx -2.89, vy -0.00, vz +0.00); touching floor
4.50 s: seesaw at -28.0°, still; touching nothing | weight at (-8.11, 0.00, 0.14) m, moving 1.89 m/s (vx -1.89, vy -0.00, vz +0.00); touching floor | ball at (-7.85, 0.00, 0.08) m, moving 2.89 m/s (vx -2.89, vy -0.00, vz -0.00); touching floor
4.75 s: seesaw at -28.0°, still; touching nothing | weight at (-8.60, 0.00, 0.14) m, moving 1.99 m/s (vx -1.99, vy -0.00, vz +0.00); touching floor | ball at (-8.19, 0.00, 0.08) m, moving 0.98 m/s (vx -0.98, vy +0.00, vz +0.00); touching floor
5.00 s: seesaw at -28.0°, still; touching nothing | weight at (-9.10, 0.00, 0.14) m, moving 1.99 m/s (vx -1.99, vy -0.00, vz +0.00); touching floor | ball at (-8.43, 0.00, 0.08) m, moving 0.98 m/s (vx -0.98, vy +0.00, vz -0.00); touching floor
5.25 s: seesaw at -28.0°, still; touching nothing | weight at (-9.60, 0.00, 0.14) m, moving 1.99 m/s (vx -1.99, vy -0.00, vz -0.00); touching floor | ball at (-8.68, 0.00, 0.08) m, moving 0.98 m/s (vx -0.98, vy +0.00, vz -0.00); touching floor
5.50 s: seesaw at -28.0°, still; touching nothing | weight at (-10.09, 0.00, 0.14) m, moving 1.99 m/s (vx -1.99, vy -0.00, vz -0.00); touching floor | ball at (-8.92, 0.00, 0.08) m, moving 0.98 m/s (vx -0.98, vy +0.00, vz +0.00); touching floor
5.75 s: seesaw at -28.0°, still; touching nothing | weight at (-10.59, 0.00, 0.14) m, moving 1.99 m/s (vx -1.99, vy -0.00, vz +0.00); touching floor | ball at (-9.17, 0.00, 0.08) m, moving 0.98 m/s (vx -0.98, vy +0.00, vz +0.00); touching floor
6.00 s: seesaw at -28.0°, still; touching nothing | weight at (-11.09, 0.00, 0.14) m, moving 1.99 m/s (vx -1.99, vy -0.00, vz -0.00); touching floor | ball at (-9.41, 0.00, 0.08) m, moving 0.98 m/s (vx -0.98, vy +0.00, vz -0.00); touching floor

At the end (6.00 s):
- seesaw at -28.0°, still; touching nothing
- weight at (-11.09, 0.00, 0.14) m, moving 1.99 m/s (vx -1.99, vy -0.00, vz -0.00); touching floor
- ball at (-9.41, 0.00, 0.08) m, moving 0.98 m/s (vx -0.98, vy +0.00, vz -0.00); touching floor
</history>
