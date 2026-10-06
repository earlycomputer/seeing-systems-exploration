MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint pivot about axis (0.00, 1.00, 0.00), no range limit; its geoms: seesaw.plank, seesaw.lip; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (0.90, 0.00, 0.10) m, at rest
- weight: free body; its geoms: weight; starts at (-0.86, 0.00, 3.00) m, at rest

What happened, in order:
 0.00 s  seesaw.plank starts touching floor
 0.01 s  ball starts moving
 0.01 s  weight starts moving
 0.01 s  seesaw.lip first touches ball
 0.01 s  seesaw.plank first touches ball
 0.70 s  seesaw.plank leaves floor
 0.70 s  seesaw.plank first touches weight
 0.78 s  seesaw.plank touches floor again
 0.78 s  seesaw.plank leaves ball
 0.80 s  seesaw.lip leaves ball
 0.80 s  seesaw is at its smallest, -32.2°
 0.85 s  seesaw.plank leaves floor
 0.94 s  seesaw.plank leaves weight
 1.07 s  weight first touches floor
 1.25 s  ball is at the top of its flight, at (-0.53, 0.00, 1.66) m
 1.72 s  seesaw.plank touches floor again
 1.73 s  seesaw is at its largest, 0.3°
 1.78 s  seesaw.plank leaves floor
 1.83 s  ball first touches floor
 1.92 s  ball leaves floor
 1.96 s  ball touches floor again
 2.01 s  seesaw.plank touches floor again
 3.66 s  ball first touches weight
 3.67 s  weight leaves floor
 3.84 s  weight touches floor again
 3.84 s  ball leaves weight
 6.00 s  ball is still moving at the end, 0.47 m/s
 6.00 s  weight is still moving at the end, 0.06 m/s

State every 0.25 s:
0.00 s: seesaw at 0.0°, still; touching floor | ball at (0.90, 0.00, 0.10) m, at rest; touching nothing | weight at (-0.86, 0.00, 3.00) m, at rest; touching nothing
0.25 s: seesaw at -0.0°, still; touching ball, floor | ball at (0.90, 0.00, 0.10) m, at rest; touching seesaw.lip, seesaw.plank | weight at (-0.86, 0.00, 2.70) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing
0.50 s: seesaw at -0.0°, still; touching ball, floor | ball at (0.90, 0.00, 0.10) m, at rest; touching seesaw.lip, seesaw.plank | weight at (-0.86, 0.00, 1.78) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing
0.75 s: seesaw at -17.0°, turning -399°/s; touching ball, weight | ball at (0.93, 0.00, 0.35) m, moving 6.50 m/s (vx -0.34, vy -0.00, vz +6.49); touching seesaw.lip, seesaw.plank | weight at (-0.86, 0.00, 0.34) m, moving 5.11 m/s (vx +0.16, vy +0.00, vz -5.11); touching seesaw.plank
1.00 s: seesaw at -26.3°, turning +17°/s; touching nothing | ball at (0.24, 0.00, 1.35) m, moving 3.90 m/s (vx -3.03, vy -0.00, vz +2.46); touching nothing | weight at (-1.07, 0.00, 0.14) m, moving 1.27 m/s (vx -1.10, vy +0.00, vz -0.63); touching nothing
1.25 s: seesaw at -20.4°, turning +31°/s; touching nothing | ball at (-0.52, 0.00, 1.66) m, moving 3.03 m/s (vx -3.03, vy -0.00, vz +0.01); touching nothing | weight at (-1.35, 0.00, 0.08) m, moving 1.10 m/s (vx -1.10, vy -0.00, vz -0.00); touching floor
1.50 s: seesaw at -10.9°, turning +45°/s; touching nothing | ball at (-1.28, 0.00, 1.35) m, moving 3.89 m/s (vx -3.03, vy -0.00, vz -2.45); touching nothing | weight at (-1.62, 0.00, 0.08) m, moving 1.10 m/s (vx -1.10, vy -0.00, vz -0.00); touching floor
1.75 s: seesaw at 0.2°, turning -8°/s; touching floor | ball at (-2.04, 0.00, 0.44) m, moving 5.76 m/s (vx -3.03, vy -0.00, vz -4.90); touching nothing | weight at (-1.89, 0.00, 0.08) m, moving 1.10 m/s (vx -1.10, vy -0.00, vz +0.00); touching floor
2.00 s: seesaw at -0.1°, turning +6°/s; touching nothing | ball at (-2.45, 0.00, 0.04) m, moving 0.99 m/s (vx -0.99, vy -0.00, vz +0.02); touching floor | weight at (-2.17, 0.00, 0.08) m, moving 1.10 m/s (vx -1.10, vy -0.00, vz -0.00); touching floor
2.25 s: seesaw at -0.0°, still; touching floor | ball at (-2.69, 0.00, 0.04) m, moving 1.00 m/s (vx -1.00, vy -0.00, vz +0.00); touching floor | weight at (-2.44, 0.00, 0.08) m, moving 1.10 m/s (vx -1.10, vy +0.00, vz -0.00); touching floor
2.50 s: seesaw at -0.0°, still; touching floor | ball at (-2.94, 0.00, 0.04) m, moving 1.00 m/s (vx -1.00, vy -0.00, vz -0.00); touching floor | weight at (-2.72, 0.00, 0.08) m, moving 1.10 m/s (vx -1.10, vy +0.00, vz -0.00); touching floor
2.75 s: seesaw at -0.0°, still; touching floor | ball at (-3.19, 0.00, 0.04) m, moving 1.00 m/s (vx -1.00, vy -0.00, vz -0.00); touching floor | weight at (-2.99, 0.00, 0.08) m, moving 1.10 m/s (vx -1.10, vy +0.00, vz -0.00); touching floor
3.00 s: seesaw at -0.0°, still; touching floor | ball at (-3.44, 0.00, 0.04) m, moving 1.00 m/s (vx -1.00, vy -0.00, vz -0.00); touching floor | weight at (-3.26, 0.00, 0.08) m, moving 1.10 m/s (vx -1.10, vy +0.00, vz -0.00); touching floor
3.25 s: seesaw at -0.0°, still; touching floor | ball at (-3.69, 0.00, 0.04) m, moving 1.00 m/s (vx -1.00, vy -0.00, vz -0.00); touching floor | weight at (-3.54, 0.00, 0.08) m, moving 1.10 m/s (vx -1.10, vy +0.00, vz -0.00); touching floor
3.50 s: seesaw at -0.0°, still; touching floor | ball at (-3.94, 0.00, 0.04) m, moving 1.00 m/s (vx -1.00, vy -0.00, vz -0.00); touching floor | weight at (-3.81, 0.00, 0.08) m, moving 1.10 m/s (vx -1.10, vy +0.00, vz -0.00); touching floor
3.75 s: seesaw at -0.0°, still; touching floor | ball at (-4.16, 0.00, 0.04) m, moving 0.50 m/s (vx -0.50, vy +0.00, vz +0.01); touching floor, weight | weight at (-4.05, 0.00, 0.10) m, moving 0.53 m/s (vx -0.52, vy +0.00, vz +0.06); touching ball
4.00 s: seesaw at -0.0°, still; touching floor | ball at (-4.28, 0.00, 0.04) m, moving 0.47 m/s (vx -0.47, vy +0.00, vz -0.00); touching floor | weight at (-4.08, 0.00, 0.08) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz -0.00); touching floor
4.25 s: seesaw at -0.0°, still; touching floor | ball at (-4.39, 0.00, 0.04) m, moving 0.47 m/s (vx -0.47, vy +0.00, vz -0.00); touching floor | weight at (-4.07, 0.00, 0.08) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz -0.00); touching floor
4.50 s: seesaw at -0.0°, still; touching floor | ball at (-4.51, 0.00, 0.04) m, moving 0.47 m/s (vx -0.47, vy +0.00, vz +0.00); touching floor | weight at (-4.06, 0.00, 0.08) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor
4.75 s: seesaw at -0.0°, still; touching floor | ball at (-4.63, 0.00, 0.04) m, moving 0.47 m/s (vx -0.47, vy +0.00, vz -0.00); touching floor | weight at (-4.04, 0.00, 0.08) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor
5.00 s: seesaw at -0.0°, still; touching floor | ball at (-4.75, 0.00, 0.04) m, moving 0.47 m/s (vx -0.47, vy +0.00, vz -0.00); touching floor | weight at (-4.03, 0.00, 0.08) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor
5.25 s: seesaw at -0.0°, still; touching floor | ball at (-4.86, 0.00, 0.04) m, moving 0.47 m/s (vx -0.47, vy +0.00, vz -0.00); touching floor | weight at (-4.01, 0.00, 0.08) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor
5.50 s: seesaw at -0.0°, still; touching floor | ball at (-4.98, 0.00, 0.04) m, moving 0.47 m/s (vx -0.47, vy +0.00, vz -0.00); touching floor | weight at (-4.00, 0.00, 0.08) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor
5.75 s: seesaw at -0.0°, still; touching floor | ball at (-5.10, 0.00, 0.04) m, moving 0.47 m/s (vx -0.47, vy +0.00, vz -0.00); touching floor | weight at (-3.99, 0.00, 0.08) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor
6.00 s: seesaw at -0.0°, still; touching floor | ball at (-5.22, 0.00, 0.04) m, moving 0.47 m/s (vx -0.47, vy +0.00, vz -0.00); touching floor | weight at (-3.97, 0.00, 0.08) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor

At the end (6.00 s):
- seesaw at -0.0°, still; touching floor
- ball at (-5.22, 0.00, 0.04) m, moving 0.47 m/s (vx -0.47, vy +0.00, vz -0.00); touching floor
- weight at (-3.97, 0.00, 0.08) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.00); touching floor
</history>
