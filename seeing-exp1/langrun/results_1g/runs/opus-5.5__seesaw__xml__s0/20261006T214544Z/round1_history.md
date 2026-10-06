Your expectations, checked against the run (2 of 4 hold):

- holds: weight touches seesaw (first touch at 0.66 s)
- DOES NOT HOLD: ball touches seesaw (they never touch)
- holds: seesaw reaches its lower stop (at its lower stop (-1°) at 0.66 s)
- DOES NOT HOLD: ball rises at least 0.5 m above its start (I can't read this; the forms are: <thing> touches <thing>; <thing> comes to rest in <thing>; <thing> drops through <thing>; <thing> reaches its lower stop; <thing> reaches its upper stop)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range -0.6° to 0° as MuJoCo applies it; its geoms: seesaw_plank, seesaw_stop; starts at 0.0°, still
- weight: free body; its geoms: weight; starts at (-0.85, 0.00, 2.60) m, at rest
- ball: free body; its geoms: ball; starts at (0.94, 0.00, 0.13) m, at rest

What happened, in order:
 0.00 s  seesaw starts at its upper stop (0°)
 0.01 s  weight starts moving
 0.01 s  ball starts moving
 0.13 s  ball first touches floor
 0.21 s  ball comes to rest at (0.94, 0.00, 0.05) m
 0.66 s  seesaw_plank first touches weight
 0.66 s  seesaw reaches its lower stop (-0.6°) moving +0°/s
 0.69 s  seesaw is at its smallest, -2.4°
 0.74 s  seesaw reaches its lower stop (-0.6°) again moving +33°/s
 0.75 s  seesaw reaches its upper stop (0°) again moving +34°/s
 0.77 s  seesaw_plank leaves weight
 0.79 s  seesaw is at its largest, 0.2°
 0.84 s  weight is at the top of its flight, at (-0.87, 0.00, 0.48) m
 0.90 s  seesaw_plank touches weight again
 0.91 s  seesaw reaches its lower stop (-0.6°) again moving -21°/s
 2.32 s  seesaw_plank leaves weight
 2.39 s  seesaw reaches its upper stop (0°) again moving +4°/s
 2.54 s  weight first touches floor
 6.00 s  weight is still moving at the end, 0.49 m/s

State every 0.25 s:
0.00 s: seesaw at 0.0°, still; touching nothing | weight at (-0.85, 0.00, 2.60) m, at rest; touching nothing | ball at (0.94, 0.00, 0.13) m, at rest; touching nothing
0.25 s: seesaw at 0.0°, still; touching nothing | weight at (-0.85, 0.00, 2.30) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
0.50 s: seesaw at 0.0°, still; touching nothing | weight at (-0.85, 0.00, 1.38) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
0.75 s: seesaw at -0.6°, turning +34°/s; touching weight | weight at (-0.86, 0.00, 0.44) m, moving 0.85 m/s (vx -0.12, vy +0.00, vz +0.84); touching seesaw_plank | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
1.00 s: seesaw at -0.7°, turning +3°/s; touching weight | weight at (-0.89, 0.00, 0.44) m, moving 0.14 m/s (vx -0.12, vy +0.00, vz +0.07); touching seesaw_plank | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
1.25 s: seesaw at -0.7°, still; touching weight | weight at (-0.92, 0.00, 0.44) m, moving 0.13 m/s (vx -0.13, vy +0.00, vz -0.00); touching seesaw_plank | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
1.50 s: seesaw at -0.7°, still; touching weight | weight at (-0.95, 0.00, 0.44) m, moving 0.14 m/s (vx -0.14, vy +0.00, vz -0.00); touching seesaw_plank | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
1.75 s: seesaw at -0.7°, still; touching weight | weight at (-0.99, 0.00, 0.44) m, moving 0.16 m/s (vx -0.16, vy +0.00, vz -0.00); touching seesaw_plank | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
2.00 s: seesaw at -0.7°, still; touching weight | weight at (-1.03, 0.00, 0.44) m, moving 0.17 m/s (vx -0.17, vy +0.00, vz -0.00); touching seesaw_plank | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
2.25 s: seesaw at -0.6°, still; touching weight | weight at (-1.08, 0.00, 0.44) m, moving 0.36 m/s (vx -0.33, vy +0.00, vz -0.14); touching seesaw_plank | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
2.50 s: seesaw at 0.0°, still; touching nothing | weight at (-1.19, 0.00, 0.18) m, moving 2.28 m/s (vx -0.44, vy +0.00, vz -2.24); touching nothing | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
2.75 s: seesaw at 0.0°, still; touching nothing | weight at (-1.31, 0.00, 0.08) m, moving 0.49 m/s (vx -0.49, vy +0.00, vz -0.00); touching floor | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
3.00 s: seesaw at 0.0°, still; touching nothing | weight at (-1.43, 0.00, 0.08) m, moving 0.49 m/s (vx -0.49, vy +0.00, vz -0.00); touching floor | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
3.25 s: seesaw at 0.0°, still; touching nothing | weight at (-1.55, 0.00, 0.08) m, moving 0.49 m/s (vx -0.49, vy +0.00, vz -0.00); touching floor | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
3.50 s: seesaw at 0.0°, still; touching nothing | weight at (-1.67, 0.00, 0.08) m, moving 0.49 m/s (vx -0.49, vy +0.00, vz -0.00); touching floor | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
3.75 s: seesaw at 0.0°, still; touching nothing | weight at (-1.79, 0.00, 0.08) m, moving 0.49 m/s (vx -0.49, vy +0.00, vz -0.00); touching floor | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
4.00 s: seesaw at 0.0°, still; touching nothing | weight at (-1.92, 0.00, 0.08) m, moving 0.49 m/s (vx -0.49, vy +0.00, vz -0.00); touching floor | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
4.25 s: seesaw at 0.0°, still; touching nothing | weight at (-2.04, 0.00, 0.08) m, moving 0.49 m/s (vx -0.49, vy +0.00, vz +0.00); touching floor | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
4.50 s: seesaw at 0.0°, still; touching nothing | weight at (-2.16, 0.00, 0.08) m, moving 0.49 m/s (vx -0.49, vy +0.00, vz +0.00); touching floor | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
4.75 s: seesaw at 0.0°, still; touching nothing | weight at (-2.28, 0.00, 0.08) m, moving 0.49 m/s (vx -0.49, vy +0.00, vz +0.00); touching floor | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
5.00 s: seesaw at 0.0°, still; touching nothing | weight at (-2.40, 0.00, 0.08) m, moving 0.49 m/s (vx -0.49, vy +0.00, vz -0.00); touching floor | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
5.25 s: seesaw at 0.0°, still; touching nothing | weight at (-2.53, 0.00, 0.08) m, moving 0.49 m/s (vx -0.49, vy +0.00, vz -0.00); touching floor | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
5.50 s: seesaw at 0.0°, still; touching nothing | weight at (-2.65, 0.00, 0.08) m, moving 0.49 m/s (vx -0.49, vy +0.00, vz +0.00); touching floor | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
5.75 s: seesaw at 0.0°, still; touching nothing | weight at (-2.77, 0.00, 0.08) m, moving 0.49 m/s (vx -0.49, vy +0.00, vz +0.00); touching floor | ball at (0.94, 0.00, 0.05) m, at rest; touching floor
6.00 s: seesaw at 0.0°, still; touching nothing | weight at (-2.89, 0.00, 0.08) m, moving 0.49 m/s (vx -0.49, vy +0.00, vz +0.00); touching floor | ball at (0.94, 0.00, 0.05) m, at rest; touching floor

At the end (6.00 s):
- seesaw at 0.0°, still; touching nothing
- weight at (-2.89, 0.00, 0.08) m, moving 0.49 m/s (vx -0.49, vy +0.00, vz +0.00); touching floor
- ball at (0.94, 0.00, 0.05) m, at rest; touching floor
</history>
