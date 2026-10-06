Your expectations, checked against the run (3 of 4 hold):

- holds: weight touches seesaw_deck (first touch at 0.65 s)
- holds: ball touches seesaw_deck (touching from the start)
- holds: seesaw reaches its upper stop (at its upper stop (29°) at 0.73 s)
- DOES NOT HOLD: ball rises at least 0.5 m above its starting height (I can't read this; the forms are: <thing> touches <thing>; <thing> comes to rest in <thing>; <thing> drops through <thing>; <thing> reaches its lower stop; <thing> reaches its upper stop)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint seesaw_hinge about axis (0.00, -1.00, 0.00), range 0° to 28.6479° as MuJoCo applies it; its geoms: seesaw_deck; starts at 0.0°, still
- weight: free body; its geoms: weight_sphere; starts at (-0.90, 0.00, 3.00) m, at rest
- ball: free body; its geoms: ball; starts at (0.90, 0.00, 0.89) m, at rest

What happened, in order:
 0.00 s  seesaw_deck starts touching ball
 0.00 s  seesaw starts at its lower stop (0°)
 0.00 s  seesaw is at its smallest, -0.0°
 0.01 s  weight starts moving
 0.65 s  seesaw_deck first touches weight_sphere
 0.65 s  ball starts moving
 0.67 s  seesaw_deck leaves weight_sphere
 0.73 s  seesaw reaches its upper stop (28.6479°) moving +333°/s
 0.73 s  seesaw is at its largest, 29.1°
 0.73 s  seesaw_deck leaves ball
 0.73 s  seesaw_deck touches weight_sphere again
 0.75 s  seesaw_deck leaves weight_sphere
 0.98 s  weight_sphere first touches floor
 1.35 s  ball is at the top of its flight, at (0.19, 0.00, 3.27) m
 2.06 s  ball passes 0.41 m from fulcrum (fulcrum_base) without touching it: nearest points (-0.51, 0.00, 0.79) m and (-0.10, 0.00, 0.74) m
 2.06 s  seesaw_deck touches ball again
 2.08 s  seesaw_deck leaves ball
 2.15 s  seesaw reaches its upper stop (28.6479°) again moving +224°/s
 2.18 s  seesaw_deck touches ball again
 2.37 s  seesaw_deck leaves ball
 2.54 s  ball first touches floor
 6.00 s  weight is still moving at the end, 2.20 m/s
 6.00 s  ball is still moving at the end, 2.00 m/s

State every 0.25 s:
0.00 s: seesaw at 0.0°, still; touching ball | weight at (-0.90, 0.00, 3.00) m, at rest; touching nothing | ball at (0.90, 0.00, 0.89) m, at rest; touching seesaw_deck
0.25 s: seesaw at -0.0°, still; touching ball | weight at (-0.90, 0.00, 2.70) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | ball at (0.90, 0.00, 0.88) m, at rest; touching seesaw_deck
0.50 s: seesaw at -0.0°, still; touching ball | weight at (-0.90, 0.00, 1.78) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing | ball at (0.90, 0.00, 0.88) m, at rest; touching seesaw_deck
0.75 s: seesaw at 28.6°, turning -16°/s; touching weight_sphere | weight at (-0.93, 0.00, 0.45) m, moving 2.25 m/s (vx -2.23, vy +0.00, vz -0.33); touching seesaw_deck | ball at (0.84, 0.00, 1.49) m, moving 5.99 m/s (vx -1.07, vy +0.00, vz +5.90); touching nothing
1.00 s: seesaw at 24.6°, turning -16°/s; touching nothing | weight at (-1.49, 0.00, 0.11) m, moving 2.19 m/s (vx -2.17, vy +0.00, vz +0.33); touching floor | ball at (0.57, 0.00, 2.66) m, moving 3.61 m/s (vx -1.07, vy +0.00, vz +3.44); touching nothing
1.25 s: seesaw at 20.8°, turning -15°/s; touching nothing | weight at (-2.04, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (0.30, 0.00, 3.22) m, moving 1.46 m/s (vx -1.07, vy +0.00, vz +0.99); touching nothing
1.50 s: seesaw at 17.1°, turning -15°/s; touching nothing | weight at (-2.59, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz -0.00); touching floor | ball at (0.03, 0.00, 3.16) m, moving 1.81 m/s (vx -1.07, vy +0.00, vz -1.46); touching nothing
1.75 s: seesaw at 13.6°, turning -14°/s; touching nothing | weight at (-3.13, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (-0.24, 0.00, 2.49) m, moving 4.06 m/s (vx -1.07, vy +0.00, vz -3.91); touching nothing
2.00 s: seesaw at 10.1°, turning -14°/s; touching nothing | weight at (-3.68, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (-0.50, 0.00, 1.21) m, moving 6.46 m/s (vx -1.07, vy +0.00, vz -6.37); touching nothing
2.25 s: seesaw at 28.6°, turning +7°/s; touching ball | weight at (-4.23, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (-0.75, 0.00, 0.49) m, moving 1.80 m/s (vx -1.53, vy +0.00, vz -0.95); touching seesaw_deck
2.50 s: seesaw at 28.6°, still; touching nothing | weight at (-4.78, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (-1.21, 0.00, 0.15) m, moving 3.03 m/s (vx -1.92, vy +0.00, vz -2.35); touching nothing
2.75 s: seesaw at 28.6°, still; touching nothing | weight at (-5.33, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (-1.71, 0.00, 0.06) m, moving 2.00 m/s (vx -2.00, vy +0.00, vz +0.00); touching floor
3.00 s: seesaw at 28.6°, still; touching nothing | weight at (-5.88, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (-2.21, 0.00, 0.06) m, moving 2.00 m/s (vx -2.00, vy +0.00, vz +0.00); touching floor
3.25 s: seesaw at 28.6°, still; touching nothing | weight at (-6.43, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (-2.71, 0.00, 0.06) m, moving 2.00 m/s (vx -2.00, vy +0.00, vz +0.00); touching floor
3.50 s: seesaw at 28.6°, still; touching nothing | weight at (-6.98, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (-3.21, 0.00, 0.06) m, moving 2.00 m/s (vx -2.00, vy +0.00, vz +0.00); touching floor
3.75 s: seesaw at 28.6°, still; touching nothing | weight at (-7.53, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (-3.71, 0.00, 0.06) m, moving 2.00 m/s (vx -2.00, vy +0.00, vz +0.00); touching floor
4.00 s: seesaw at 28.6°, still; touching nothing | weight at (-8.07, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (-4.21, 0.00, 0.06) m, moving 2.00 m/s (vx -2.00, vy +0.00, vz +0.00); touching floor
4.25 s: seesaw at 28.6°, still; touching nothing | weight at (-8.62, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (-4.71, 0.00, 0.06) m, moving 2.00 m/s (vx -2.00, vy +0.00, vz +0.00); touching floor
4.50 s: seesaw at 28.6°, still; touching nothing | weight at (-9.17, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (-5.21, 0.00, 0.06) m, moving 2.00 m/s (vx -2.00, vy +0.00, vz +0.00); touching floor
4.75 s: seesaw at 28.6°, still; touching nothing | weight at (-9.72, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (-5.71, 0.00, 0.06) m, moving 2.00 m/s (vx -2.00, vy +0.00, vz +0.00); touching floor
5.00 s: seesaw at 28.6°, still; touching nothing | weight at (-10.27, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (-6.21, 0.00, 0.06) m, moving 2.00 m/s (vx -2.00, vy +0.00, vz +0.00); touching floor
5.25 s: seesaw at 28.6°, still; touching nothing | weight at (-10.82, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (-6.71, 0.00, 0.06) m, moving 2.00 m/s (vx -2.00, vy +0.00, vz +0.00); touching floor
5.50 s: seesaw at 28.6°, still; touching nothing | weight at (-11.37, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (-7.21, 0.00, 0.06) m, moving 2.00 m/s (vx -2.00, vy +0.00, vz +0.00); touching floor
5.75 s: seesaw at 28.6°, still; touching nothing | weight at (-11.92, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (-7.71, 0.00, 0.06) m, moving 2.00 m/s (vx -2.00, vy +0.00, vz +0.00); touching floor
6.00 s: seesaw at 28.6°, still; touching nothing | weight at (-12.46, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor | ball at (-8.21, 0.00, 0.06) m, moving 2.00 m/s (vx -2.00, vy +0.00, vz +0.00); touching floor

At the end (6.00 s):
- seesaw at 28.6°, still; touching nothing
- weight at (-12.46, 0.00, 0.12) m, moving 2.20 m/s (vx -2.20, vy +0.00, vz +0.00); touching floor
- ball at (-8.21, 0.00, 0.06) m, moving 2.00 m/s (vx -2.00, vy +0.00, vz +0.00); touching floor
</history>
