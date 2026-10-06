Your expectations, checked against the run (3 of 3 hold):

- holds: weight touches seesaw (first touch at 0.46 s)
- holds: ball touches seesaw (first touch at 0.00 s)
- holds: seesaw reaches its lower stop (at its lower stop (-28°) at 0.54 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range -28° to 0° as MuJoCo applies it; its geoms: seesaw_deck; starts at 0.0°, still
- weight: free body; its geoms: weight_sphere; starts at (-0.62, 0.00, 1.60) m, at rest
- ball: free body; its geoms: ball; starts at (0.62, 0.00, 0.52) m, at rest

What happened, in order:
 0.00 s  seesaw starts at its upper stop (0°)
 0.00 s  seesaw_deck first touches ball
 0.00 s  seesaw is at its largest, 0.0°
 0.01 s  weight starts moving
 0.46 s  seesaw_deck first touches weight_sphere
 0.46 s  ball starts moving
 0.47 s  seesaw_deck leaves weight_sphere
 0.49 s  weight passes 0.49 m from fulcrum (fulcrum_support) without touching it: nearest points (-0.53, 0.00, 0.44) m and (-0.05, 0.00, 0.43) m
 0.54 s  seesaw reaches its lower stop (-28°) moving -336°/s
 0.54 s  seesaw is at its smallest, -28.4°
 0.54 s  seesaw_deck leaves ball
 0.54 s  seesaw_deck touches weight_sphere again
 0.55 s  seesaw_deck leaves weight_sphere
 0.57 s  weight is at the top of its flight, at (-0.66, 0.00, 0.23) m
 0.74 s  weight_sphere first touches floor
 0.75 s  weight_sphere leaves floor
 0.81 s  weight_sphere touches floor again
 0.98 s  ball is at the top of its flight, at (0.27, 0.00, 1.78) m
 1.49 s  seesaw_deck touches ball again
 1.49 s  ball passes 0.03 m from fulcrum (fulcrum_axle) without touching it: nearest points (-0.06, 0.00, 0.48) m and (-0.03, 0.00, 0.46) m
 1.49 s  seesaw_deck leaves ball
 1.58 s  ball is at the top of its flight, at (-0.18, 0.00, 0.53) m
 1.76 s  seesaw_deck touches ball again
 1.77 s  seesaw reaches its lower stop (-28°) again moving -93°/s
 1.87 s  seesaw reaches its lower stop (-28°) again moving -8°/s
 2.02 s  seesaw_deck leaves ball
 2.08 s  ball first touches floor
 2.09 s  ball leaves floor
 2.14 s  ball touches floor again
 6.00 s  weight is still moving at the end, 1.69 m/s
 6.00 s  ball is still moving at the end, 2.01 m/s

State every 0.25 s:
0.00 s: seesaw at 0.0°, still; touching nothing | weight at (-0.62, 0.00, 1.60) m, at rest; touching nothing | ball at (0.62, 0.00, 0.52) m, at rest; touching nothing
0.25 s: seesaw at 0.0°, still; touching ball | weight at (-0.62, 0.00, 1.30) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | ball at (0.62, 0.00, 0.52) m, at rest; touching seesaw_deck
0.50 s: seesaw at -15.0°, turning -373°/s; touching ball | weight at (-0.62, 0.00, 0.41) m, moving 3.97 m/s (vx -0.03, vy +0.00, vz -3.97); touching nothing | ball at (0.61, 0.00, 0.68) m, moving 4.41 m/s (vx -0.34, vy -0.00, vz +4.40); touching seesaw_deck
0.75 s: seesaw at -23.7°, turning +21°/s; touching nothing | weight at (-0.98, 0.00, 0.09) m, moving 1.70 m/s (vx -1.68, vy +0.00, vz +0.25); touching nothing | ball at (0.44, 0.00, 1.53) m, moving 2.32 m/s (vx -0.74, vy -0.00, vz +2.20); touching nothing
1.00 s: seesaw at -18.7°, turning +19°/s; touching nothing | weight at (-1.41, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz +0.00); touching floor | ball at (0.25, 0.00, 1.78) m, moving 0.78 m/s (vx -0.74, vy -0.00, vz -0.25); touching nothing
1.25 s: seesaw at -14.1°, turning +18°/s; touching nothing | weight at (-1.83, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz +0.00); touching floor | ball at (0.07, 0.00, 1.41) m, moving 2.80 m/s (vx -0.74, vy -0.00, vz -2.70); touching nothing
1.50 s: seesaw at -11.0°, turning -62°/s; touching nothing | weight at (-2.25, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz +0.00); touching floor | ball at (-0.12, 0.00, 0.50) m, moving 1.12 m/s (vx -0.85, vy -0.00, vz +0.73); touching nothing
1.75 s: seesaw at -25.8°, turning -56°/s; touching nothing | weight at (-2.67, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz +0.00); touching floor | ball at (-0.33, 0.00, 0.38) m, moving 1.92 m/s (vx -0.85, vy -0.00, vz -1.73); touching nothing
2.00 s: seesaw at -28.0°, still; touching ball | weight at (-3.09, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz +0.00); touching floor | ball at (-0.70, 0.00, 0.16) m, moving 2.13 m/s (vx -1.88, vy +0.00, vz -1.00); touching seesaw_deck
2.25 s: seesaw at -28.0°, still; touching nothing | weight at (-3.52, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz -0.00); touching floor | ball at (-1.20, 0.00, 0.05) m, moving 2.01 m/s (vx -2.01, vy -0.00, vz +0.00); touching floor
2.50 s: seesaw at -28.0°, still; touching nothing | weight at (-3.94, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz +0.00); touching floor | ball at (-1.70, 0.00, 0.05) m, moving 2.01 m/s (vx -2.01, vy -0.00, vz -0.00); touching floor
2.75 s: seesaw at -28.0°, still; touching nothing | weight at (-4.36, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz +0.00); touching floor | ball at (-2.20, 0.00, 0.05) m, moving 2.01 m/s (vx -2.01, vy +0.00, vz +0.00); touching floor
3.00 s: seesaw at -28.0°, still; touching nothing | weight at (-4.78, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz +0.00); touching floor | ball at (-2.70, 0.00, 0.05) m, moving 2.01 m/s (vx -2.01, vy -0.00, vz -0.00); touching floor
3.25 s: seesaw at -28.0°, still; touching nothing | weight at (-5.20, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz +0.00); touching floor | ball at (-3.21, 0.00, 0.05) m, moving 2.01 m/s (vx -2.01, vy -0.00, vz -0.00); touching floor
3.50 s: seesaw at -28.0°, still; touching nothing | weight at (-5.63, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz +0.00); touching floor | ball at (-3.71, 0.00, 0.05) m, moving 2.01 m/s (vx -2.01, vy -0.00, vz +0.00); touching floor
3.75 s: seesaw at -28.0°, still; touching nothing | weight at (-6.05, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz +0.00); touching floor | ball at (-4.21, 0.00, 0.05) m, moving 2.01 m/s (vx -2.01, vy -0.00, vz -0.00); touching floor
4.00 s: seesaw at -28.0°, still; touching nothing | weight at (-6.47, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz +0.00); touching floor | ball at (-4.71, 0.00, 0.05) m, moving 2.01 m/s (vx -2.01, vy -0.00, vz -0.00); touching floor
4.25 s: seesaw at -28.0°, still; touching nothing | weight at (-6.89, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz -0.00); touching floor | ball at (-5.22, 0.00, 0.05) m, moving 2.01 m/s (vx -2.01, vy -0.00, vz -0.00); touching floor
4.50 s: seesaw at -28.0°, still; touching nothing | weight at (-7.31, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz -0.00); touching floor | ball at (-5.72, 0.00, 0.05) m, moving 2.01 m/s (vx -2.01, vy -0.00, vz -0.00); touching floor
4.75 s: seesaw at -28.0°, still; touching nothing | weight at (-7.74, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz -0.00); touching floor | ball at (-6.22, 0.00, 0.05) m, moving 2.01 m/s (vx -2.01, vy -0.00, vz +0.00); touching floor
5.00 s: seesaw at -28.0°, still; touching nothing | weight at (-8.16, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz -0.00); touching floor | ball at (-6.72, 0.00, 0.05) m, moving 2.01 m/s (vx -2.01, vy +0.00, vz +0.00); touching floor
5.25 s: seesaw at -28.0°, still; touching nothing | weight at (-8.58, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz +0.00); touching floor | ball at (-7.22, 0.00, 0.05) m, moving 2.01 m/s (vx -2.01, vy +0.00, vz -0.00); touching floor
5.50 s: seesaw at -28.0°, still; touching nothing | weight at (-9.00, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz -0.00); touching floor | ball at (-7.73, 0.00, 0.05) m, moving 2.01 m/s (vx -2.01, vy -0.00, vz -0.00); touching floor
5.75 s: seesaw at -28.0°, still; touching nothing | weight at (-9.42, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz -0.00); touching floor | ball at (-8.23, 0.00, 0.05) m, moving 2.01 m/s (vx -2.01, vy -0.00, vz +0.00); touching floor
6.00 s: seesaw at -28.0°, still; touching nothing | weight at (-9.85, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz -0.00); touching floor | ball at (-8.73, 0.00, 0.05) m, moving 2.01 m/s (vx -2.01, vy -0.00, vz +0.00); touching floor

At the end (6.00 s):
- seesaw at -28.0°, still; touching nothing
- weight at (-9.85, 0.00, 0.09) m, moving 1.69 m/s (vx -1.69, vy +0.00, vz -0.00); touching floor
- ball at (-8.73, 0.00, 0.05) m, moving 2.01 m/s (vx -2.01, vy -0.00, vz +0.00); touching floor
</history>
