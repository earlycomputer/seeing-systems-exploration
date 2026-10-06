Your expectations, checked against the run (4 of 5 hold):

- holds: weight touches seesaw_deck (first touch at 0.63 s)
- holds: ball touches seesaw_deck (touching from the start)
- holds: seesaw reaches its lower stop (at its lower stop (-29°) at 0.70 s)
- DOES NOT HOLD: ball reaches at least 0.50 m above its starting height (I can't read this; the forms are: <thing> touches <thing>; <thing> comes to rest in <thing>; <thing> drops through <thing>; <thing> reaches its lower stop; <thing> reaches its upper stop)
- holds: ball touches floor (first touch at 1.99 s)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range -28.6479° to 5.72958° as MuJoCo applies it; its geoms: seesaw_deck, seesaw_counterweight; starts at 0.0°, still
- weight: free body; its geoms: weight_sphere; starts at (-0.70, 0.00, 2.50) m, at rest
- ball: free body; its geoms: ball; starts at (0.70, 0.00, 0.52) m, at rest

What happened, in order:
 0.00 s  seesaw_deck starts touching ball
 0.00 s  seesaw is at its largest at the start, 0.0°
 0.01 s  weight starts moving
 0.63 s  seesaw_deck first touches weight_sphere
 0.63 s  ball starts moving
 0.65 s  seesaw_deck leaves weight_sphere
 0.70 s  seesaw reaches its lower stop (-28.6479°) moving -402°/s
 0.70 s  seesaw is at its smallest, -29.3°
 0.70 s  seesaw_deck leaves ball
 0.70 s  seesaw reaches its lower stop (-28.6479°) again moving -398°/s
 0.70 s  weight passes 0.47 m from support (support_base) without touching it: nearest points (-0.61, 0.00, 0.18) m and (-0.16, 0.00, 0.05) m
 0.70 s  seesaw_deck touches weight_sphere again
 0.72 s  seesaw_deck leaves weight_sphere
 0.81 s  seesaw reaches its lower stop (-28.6479°) again moving -11°/s
 0.83 s  weight_sphere first touches floor
 1.28 s  ball is at the top of its flight, at (0.02, 0.00, 2.54) m
 1.99 s  ball first touches floor
 2.04 s  ball leaves floor
 2.14 s  ball touches floor again
 6.00 s  weight is still moving at the end, 1.97 m/s
 6.00 s  ball is still moving at the end, 0.11 m/s

State every 0.25 s:
0.00 s: seesaw at 0.0°, still; touching ball | weight at (-0.70, 0.00, 2.50) m, at rest; touching nothing | ball at (0.70, 0.00, 0.52) m, at rest; touching seesaw_deck
0.25 s: seesaw at -0.0°, still; touching ball | weight at (-0.70, 0.00, 2.20) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | ball at (0.70, 0.00, 0.51) m, at rest; touching seesaw_deck
0.50 s: seesaw at -0.0°, still; touching ball | weight at (-0.70, 0.00, 1.28) m, moving 4.91 m/s (vx +0.00, vy +0.00, vz -4.91); touching nothing | ball at (0.70, 0.00, 0.51) m, at rest; touching seesaw_deck
0.75 s: seesaw at -28.1°, turning +10°/s; touching nothing | weight at (-0.79, 0.00, 0.17) m, moving 2.09 m/s (vx -2.01, vy +0.00, vz -0.60); touching nothing | ball at (0.61, 0.00, 1.17) m, moving 5.29 m/s (vx -1.10, vy +0.00, vz +5.17); touching nothing
1.00 s: seesaw at -28.6°, still; touching nothing | weight at (-1.29, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (0.33, 0.00, 2.16) m, moving 2.94 m/s (vx -1.10, vy +0.00, vz +2.72); touching nothing
1.25 s: seesaw at -28.6°, still; touching nothing | weight at (-1.78, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (0.06, 0.00, 2.53) m, moving 1.14 m/s (vx -1.10, vy +0.00, vz +0.27); touching nothing
1.50 s: seesaw at -28.6°, still; touching nothing | weight at (-2.27, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-0.22, 0.00, 2.29) m, moving 2.45 m/s (vx -1.10, vy +0.00, vz -2.19); touching nothing
1.75 s: seesaw at -28.6°, still; touching nothing | weight at (-2.77, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-0.50, 0.00, 1.44) m, moving 4.77 m/s (vx -1.10, vy +0.00, vz -4.64); touching nothing
2.00 s: seesaw at -28.6°, still; touching nothing | weight at (-3.26, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-0.77, 0.00, 0.02) m, moving 0.41 m/s (vx -0.25, vy +0.00, vz -0.32); touching floor
2.25 s: seesaw at -28.6°, still; touching nothing | weight at (-3.75, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-0.80, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching floor
2.50 s: seesaw at -28.6°, still; touching nothing | weight at (-4.25, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-0.82, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching floor
2.75 s: seesaw at -28.6°, still; touching nothing | weight at (-4.74, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-0.85, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching floor
3.00 s: seesaw at -28.6°, still; touching nothing | weight at (-5.23, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-0.88, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching floor
3.25 s: seesaw at -28.6°, still; touching nothing | weight at (-5.73, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-0.91, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching floor
3.50 s: seesaw at -28.6°, still; touching nothing | weight at (-6.22, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-0.94, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching floor
3.75 s: seesaw at -28.6°, still; touching nothing | weight at (-6.71, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-0.96, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching floor
4.00 s: seesaw at -28.6°, still; touching nothing | weight at (-7.21, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-0.99, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching floor
4.25 s: seesaw at -28.6°, still; touching nothing | weight at (-7.70, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-1.02, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching floor
4.50 s: seesaw at -28.6°, still; touching nothing | weight at (-8.19, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-1.05, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching floor
4.75 s: seesaw at -28.6°, still; touching nothing | weight at (-8.68, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-1.08, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching floor
5.00 s: seesaw at -28.6°, still; touching nothing | weight at (-9.18, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-1.10, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching floor
5.25 s: seesaw at -28.6°, still; touching nothing | weight at (-9.67, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-1.13, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching floor
5.50 s: seesaw at -28.6°, still; touching nothing | weight at (-10.16, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-1.16, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching floor
5.75 s: seesaw at -28.6°, still; touching nothing | weight at (-10.66, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-1.19, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching floor
6.00 s: seesaw at -28.6°, still; touching nothing | weight at (-11.15, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor | ball at (-1.21, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching floor

At the end (6.00 s):
- seesaw at -28.6°, still; touching nothing
- weight at (-11.15, 0.00, 0.09) m, moving 1.97 m/s (vx -1.97, vy +0.00, vz +0.00); touching floor
- ball at (-1.21, 0.00, 0.04) m, moving 0.11 m/s (vx -0.11, vy +0.00, vz +0.00); touching floor
</history>
