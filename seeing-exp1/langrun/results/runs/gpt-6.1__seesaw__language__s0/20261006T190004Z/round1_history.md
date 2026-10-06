MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range 0° to 45° as MuJoCo applies it; its geoms: seesaw; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (-0.85, 0.00, 0.90) m, at rest
- weight: free body; its geoms: weight; starts at (0.85, 0.00, 3.40) m, at rest

What happened, in order:
 0.00 s  seesaw starts at its lower stop (0°)
 0.00 s  seesaw first touches ball
 0.01 s  weight starts moving
 0.71 s  seesaw first touches weight
 0.71 s  ball starts moving
 0.75 s  seesaw leaves weight
 0.81 s  seesaw leaves ball
 0.83 s  seesaw reaches its upper stop (45°) moving +360°/s
 0.85 s  seesaw is at its largest, 47.2°
 0.86 s  weight first touches floor
 0.90 s  seesaw reaches its upper stop (45°) again moving -41°/s
 0.92 s  weight leaves floor
 1.02 s  weight touches floor again
 1.06 s  weight comes to rest at (0.84, 0.00, 0.05) m
 1.48 s  ball is at the top of its flight, at (0.31, 0.00, 3.72) m
 2.04 s  seesaw reaches its lower stop (0°) again moving -38°/s
 2.07 s  seesaw is at its smallest, -0.3°
 2.35 s  ball first touches floor
 2.41 s  ball leaves floor
 2.47 s  ball is at the top of its flight, at (1.73, 0.00, 0.04) m
 2.52 s  ball touches floor again
 2.64 s  ball comes to rest at (1.75, 0.00, 0.03) m

State every 0.25 s:
0.00 s: seesaw at 0.0°, still; touching nothing | ball at (-0.85, 0.00, 0.90) m, at rest; touching nothing | weight at (0.85, 0.00, 3.40) m, at rest; touching nothing
0.25 s: seesaw at -0.0°, still; touching ball | ball at (-0.85, 0.00, 0.89) m, at rest; touching seesaw | weight at (0.85, 0.00, 3.10) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing
0.50 s: seesaw at -0.0°, still; touching ball | ball at (-0.85, 0.00, 0.89) m, at rest; touching seesaw | weight at (0.85, 0.00, 2.18) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing
0.75 s: seesaw at 14.7°, turning +410°/s; touching ball | ball at (-0.84, 0.00, 1.10) m, moving 6.40 m/s (vx +0.54, vy +0.00, vz +6.37); touching seesaw | weight at (0.85, 0.00, 0.71) m, moving 5.53 m/s (vx -0.09, vy +0.00, vz -5.53); touching nothing
1.00 s: seesaw at 41.2°, turning -41°/s; touching nothing | ball at (-0.47, 0.00, 2.57) m, moving 5.00 m/s (vx +1.62, vy -0.00, vz +4.73); touching nothing | weight at (0.84, 0.00, 0.06) m, moving 0.31 m/s (vx +0.02, vy +0.00, vz -0.31); touching nothing
1.25 s: seesaw at 31.1°, turning -40°/s; touching nothing | ball at (-0.06, 0.00, 3.45) m, moving 2.79 m/s (vx +1.62, vy -0.00, vz +2.28); touching nothing | weight at (0.85, 0.00, 0.05) m, at rest; touching floor
1.50 s: seesaw at 21.2°, turning -39°/s; touching nothing | ball at (0.34, 0.00, 3.71) m, moving 1.63 m/s (vx +1.62, vy -0.00, vz -0.18); touching nothing | weight at (0.85, 0.00, 0.05) m, at rest; touching floor
1.75 s: seesaw at 11.5°, turning -38°/s; touching nothing | ball at (0.74, 0.00, 3.37) m, moving 3.09 m/s (vx +1.62, vy -0.00, vz -2.63); touching nothing | weight at (0.85, 0.00, 0.05) m, at rest; touching floor
2.00 s: seesaw at 2.0°, turning -38°/s; touching nothing | ball at (1.15, 0.00, 2.40) m, moving 5.33 m/s (vx +1.62, vy -0.00, vz -5.08); touching nothing | weight at (0.85, 0.00, 0.05) m, at rest; touching floor
2.25 s: seesaw at 0.6°, turning +5°/s; touching nothing | ball at (1.55, 0.00, 0.83) m, moving 7.71 m/s (vx +1.62, vy -0.00, vz -7.53); touching nothing | weight at (0.86, 0.00, 0.05) m, at rest; touching floor
2.50 s: seesaw at 1.8°, turning +5°/s; touching nothing | ball at (1.74, 0.00, 0.04) m, moving 0.34 m/s (vx +0.08, vy +0.00, vz -0.33); touching nothing | weight at (0.86, 0.00, 0.05) m, at rest; touching floor
2.75 s: seesaw at 2.9°, turning +5°/s; touching nothing | ball at (1.75, 0.00, 0.03) m, at rest; touching floor | weight at (0.86, 0.00, 0.05) m, at rest; touching floor
3.00 s: seesaw at 4.1°, turning +5°/s; touching nothing | ball at (1.76, 0.00, 0.03) m, at rest; touching floor | weight at (0.86, 0.00, 0.05) m, at rest; touching floor
3.25 s: seesaw at 5.2°, turning +4°/s; touching nothing | ball at (1.76, 0.00, 0.03) m, at rest; touching floor | weight at (0.86, 0.00, 0.05) m, at rest; touching floor
3.50 s: seesaw at 6.3°, turning +4°/s; touching nothing | ball at (1.76, 0.00, 0.03) m, at rest; touching floor | weight at (0.86, 0.00, 0.05) m, at rest; touching floor
3.75 s: seesaw at 7.4°, turning +4°/s; touching nothing | ball at (1.76, 0.00, 0.03) m, at rest; touching floor | weight at (0.86, 0.00, 0.05) m, at rest; touching floor
4.00 s: seesaw at 8.4°, turning +4°/s; touching nothing | ball at (1.76, 0.00, 0.03) m, at rest; touching floor | weight at (0.86, 0.00, 0.05) m, at rest; touching floor
4.25 s: seesaw at 9.5°, turning +4°/s; touching nothing | ball at (1.76, 0.00, 0.03) m, at rest; touching floor | weight at (0.86, 0.00, 0.05) m, at rest; touching floor
4.50 s: seesaw at 10.5°, turning +4°/s; touching nothing | ball at (1.76, 0.00, 0.03) m, at rest; touching floor | weight at (0.86, 0.00, 0.05) m, at rest; touching floor
4.75 s: seesaw at 11.5°, turning +4°/s; touching nothing | ball at (1.76, 0.00, 0.03) m, at rest; touching floor | weight at (0.86, 0.00, 0.05) m, at rest; touching floor
5.00 s: seesaw at 12.5°, turning +4°/s; touching nothing | ball at (1.76, 0.00, 0.03) m, at rest; touching floor | weight at (0.86, 0.00, 0.05) m, at rest; touching floor
5.25 s: seesaw at 13.4°, turning +4°/s; touching nothing | ball at (1.76, 0.00, 0.03) m, at rest; touching floor | weight at (0.86, 0.00, 0.05) m, at rest; touching floor
5.50 s: seesaw at 14.4°, turning +4°/s; touching nothing | ball at (1.76, 0.00, 0.03) m, at rest; touching floor | weight at (0.86, 0.00, 0.05) m, at rest; touching floor
5.75 s: seesaw at 15.3°, turning +4°/s; touching nothing | ball at (1.76, 0.00, 0.03) m, at rest; touching floor | weight at (0.86, 0.00, 0.05) m, at rest; touching floor
6.00 s: seesaw at 16.2°, turning +4°/s; touching nothing | ball at (1.76, 0.00, 0.03) m, at rest; touching floor | weight at (0.86, 0.00, 0.05) m, at rest; touching floor

At the end (6.00 s):
- seesaw at 16.2°, turning +4°/s; touching nothing
- ball at (1.76, 0.00, 0.03) m, at rest; touching floor
- weight at (0.86, 0.00, 0.05) m, at rest; touching floor
</history>
