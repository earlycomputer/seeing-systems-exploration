Your expectations, checked against the run (2 of 2 hold):

- holds: weight touches seesaw (first touch at 0.56 s)
- holds: ball touches seesaw (first touch at 0.13 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint seesaw_pivot about axis (0.00, 1.00, 0.00), range -20° to 10° as MuJoCo applies it; its geoms: seesaw, seesaw.lip; starts at 10.0°, still
- ball: free body; its geoms: ball; starts at (0.45, 0.00, 0.34) m, at rest
- weight: free body; its geoms: weight; starts at (-0.45, 0.00, 2.00) m, at rest

What happened, in order:
 0.00 s  seesaw starts at its upper stop (10°)
 0.01 s  ball starts moving
 0.01 s  weight starts moving
 0.13 s  seesaw first touches ball
 0.13 s  seesaw.lip first touches ball
 0.56 s  seesaw first touches weight
 0.61 s  seesaw reaches its lower stop (-20°) moving -667°/s
 0.61 s  seesaw leaves ball
 0.62 s  weight passes 0.37 m from fulcrum without touching it: nearest points (-0.39, 0.00, 0.18) m and (-0.02, 0.00, 0.18) m
 0.62 s  seesaw.lip leaves ball
 0.64 s  seesaw is at its smallest, -25.9°
 0.66 s  seesaw leaves weight
 0.69 s  weight is at the top of its flight, at (-0.54, 0.00, 0.15) m
 0.70 s  seesaw reaches its lower stop (-20°) again moving +109°/s
 0.83 s  weight first touches floor
 0.94 s  seesaw reaches its upper stop (10°) again moving +133°/s
 0.97 s  seesaw is at its largest, 10.9°
 0.98 s  ball is at the top of its flight, at (-0.58, 0.00, 1.15) m
 1.00 s  seesaw reaches its upper stop (10°) again moving -16°/s
 1.23 s  seesaw reaches its upper stop (10°) again moving +7°/s
 1.45 s  ball first touches floor
 1.50 s  weight leaves floor
 1.50 s  ball first touches weight
 1.87 s  ball leaves weight
 1.90 s  weight touches floor again
 2.49 s  ball comes to rest at (-2.35, 0.00, 0.03) m
 6.00 s  weight is still moving at the end, 0.16 m/s

State every 0.25 s:
0.00 s: seesaw at 10.0°, still; touching nothing | ball at (0.45, 0.00, 0.34) m, at rest; touching nothing | weight at (-0.45, 0.00, 2.00) m, at rest; touching nothing
0.25 s: seesaw at 10.0°, still; touching ball | ball at (0.45, 0.00, 0.26) m, at rest; touching seesaw, seesaw.lip | weight at (-0.45, 0.00, 1.70) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing
0.50 s: seesaw at 10.0°, still; touching ball | ball at (0.45, 0.00, 0.26) m, at rest; touching seesaw, seesaw.lip | weight at (-0.45, 0.00, 0.78) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing
0.75 s: seesaw at -14.4°, turning +114°/s; touching nothing | ball at (0.04, 0.00, 0.90) m, moving 3.52 m/s (vx -2.74, vy +0.00, vz +2.21); touching nothing | weight at (-0.64, 0.00, 0.13) m, moving 1.78 m/s (vx -1.68, vy +0.00, vz -0.61); touching nothing
1.00 s: seesaw at 10.4°, turning -15°/s; touching nothing | ball at (-0.64, 0.00, 1.15) m, moving 2.75 m/s (vx -2.74, vy +0.00, vz -0.24); touching nothing | weight at (-1.05, 0.00, 0.06) m, moving 1.61 m/s (vx -1.61, vy +0.00, vz +0.00); touching floor
1.25 s: seesaw at 9.7°, turning +10°/s; touching nothing | ball at (-1.33, 0.00, 0.78) m, moving 3.84 m/s (vx -2.74, vy +0.00, vz -2.70); touching nothing | weight at (-1.45, 0.00, 0.06) m, moving 1.61 m/s (vx -1.61, vy +0.00, vz +0.00); touching floor
1.50 s: seesaw at 10.0°, still; touching nothing | ball at (-1.94, 0.00, 0.03) m, moving 1.05 m/s (vx -0.98, vy +0.00, vz +0.38); touching floor | weight at (-1.85, 0.00, 0.06) m, moving 1.61 m/s (vx -1.61, vy +0.00, vz +0.00); touching floor
1.75 s: seesaw at 10.0°, still; touching nothing | ball at (-2.10, 0.00, 0.03) m, moving 0.58 m/s (vx -0.58, vy +0.00, vz +0.00); touching floor, weight | weight at (-2.06, 0.00, 0.11) m, moving 0.47 m/s (vx -0.47, vy -0.00, vz -0.06); touching ball
2.00 s: seesaw at 10.0°, still; touching nothing | ball at (-2.24, 0.00, 0.03) m, moving 0.44 m/s (vx -0.44, vy +0.00, vz +0.00); touching floor | weight at (-2.09, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz +0.00); touching floor
2.25 s: seesaw at 10.0°, still; touching nothing | ball at (-2.32, 0.00, 0.03) m, moving 0.23 m/s (vx -0.23, vy +0.00, vz -0.01); touching nothing | weight at (-2.05, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz +0.00); touching floor
2.50 s: seesaw at 10.0°, still; touching nothing | ball at (-2.35, 0.00, 0.03) m, at rest; touching floor | weight at (-2.01, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz -0.00); touching floor
2.75 s: seesaw at 10.0°, still; touching nothing | ball at (-2.36, 0.00, 0.03) m, at rest; touching floor | weight at (-1.97, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz +0.00); touching floor
3.00 s: seesaw at 10.0°, still; touching nothing | ball at (-2.36, 0.00, 0.03) m, at rest; touching floor | weight at (-1.93, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz +0.00); touching floor
3.25 s: seesaw at 10.0°, still; touching nothing | ball at (-2.36, 0.00, 0.03) m, at rest; touching floor | weight at (-1.88, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz -0.00); touching floor
3.50 s: seesaw at 10.0°, still; touching nothing | ball at (-2.36, 0.00, 0.03) m, at rest; touching floor | weight at (-1.84, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz -0.00); touching floor
3.75 s: seesaw at 10.0°, still; touching nothing | ball at (-2.36, 0.00, 0.03) m, at rest; touching floor | weight at (-1.80, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz -0.00); touching floor
4.00 s: seesaw at 10.0°, still; touching nothing | ball at (-2.36, 0.00, 0.03) m, at rest; touching floor | weight at (-1.76, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz +0.00); touching floor
4.25 s: seesaw at 10.0°, still; touching nothing | ball at (-2.36, 0.00, 0.03) m, at rest; touching floor | weight at (-1.72, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz +0.00); touching floor
4.50 s: seesaw at 10.0°, still; touching nothing | ball at (-2.36, 0.00, 0.03) m, at rest; touching floor | weight at (-1.68, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz -0.00); touching floor
4.75 s: seesaw at 10.0°, still; touching nothing | ball at (-2.36, 0.00, 0.03) m, at rest; touching floor | weight at (-1.64, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz -0.00); touching floor
5.00 s: seesaw at 10.0°, still; touching nothing | ball at (-2.36, 0.00, 0.03) m, at rest; touching floor | weight at (-1.60, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz +0.00); touching floor
5.25 s: seesaw at 10.0°, still; touching nothing | ball at (-2.36, 0.00, 0.03) m, at rest; touching floor | weight at (-1.56, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz +0.00); touching floor
5.50 s: seesaw at 10.0°, still; touching nothing | ball at (-2.36, 0.00, 0.03) m, at rest; touching floor | weight at (-1.51, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz -0.00); touching floor
5.75 s: seesaw at 10.0°, still; touching nothing | ball at (-2.36, 0.00, 0.03) m, at rest; touching floor | weight at (-1.47, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz -0.00); touching floor
6.00 s: seesaw at 10.0°, still; touching nothing | ball at (-2.36, 0.00, 0.03) m, at rest; touching floor | weight at (-1.43, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz -0.00); touching floor

At the end (6.00 s):
- seesaw at 10.0°, still; touching nothing
- ball at (-2.36, 0.00, 0.03) m, at rest; touching floor
- weight at (-1.43, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz -0.00); touching floor
</history>
