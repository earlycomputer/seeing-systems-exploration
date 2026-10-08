Before the run, at the start:
- ball2 already touches lever1 at the start, so their touch is not something that happens in the run

MuJoCo ran your scene for 12 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 12.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- cart1: slide joint cart1_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.58 m as MuJoCo applies it; its geoms: cart1_chassis; starts at 0.000 m, still
- ball1: free body; its geoms: ball1_sphere; starts at (-0.98, 0.00, 0.54) m, at rest
- pendulum1: hinge joint pendulum1_hinge about axis (0.00, -1.00, 0.00), range 0° to 40° as MuJoCo applies it; its geoms: pendulum1_hub, pendulum1_rod, pendulum1_bob; starts at 0.0°, still
- door1: hinge joint door1_hinge about axis (0.00, 0.00, -1.00), range 0° to 70° as MuJoCo applies it; its geoms: door1_panel; starts at 0.0°, still
- block1: free body; its geoms: block1_cube; starts at (0.98, -0.14, 0.06) m, at rest
- domino1: free body; its geoms: domino1_tile; starts at (1.12, -0.53, 0.12) m, at rest
- lever1: hinge joint lever1_hinge about axis (0.00, -1.00, 0.00), range 0° to 45° as MuJoCo applies it; its geoms: lever1_beam, lever1_left_striker; starts at 0.0°, still
- ball2: free body; its geoms: ball2_sphere; starts at (1.40, -1.29, 0.87) m, at rest
- cart2: slide joint cart2_slide about axis (1.00, 0.00, 0.00), range -0.04 m to 0.04 m as MuJoCo applies it; its geoms: cart2_chassis; starts at 0.000 m, still

What happened, in order:
 0.00 s  domino1_tile starts touching floor
 0.00 s  ball1_sphere starts touching ramp1_launch_shelf
 0.00 s  block1_cube starts touching floor
 0.00 s  lever1_beam starts touching ball2_sphere
 0.00 s  cart1 starts at its lower stop (0 m)
 0.00 s  pendulum1 starts at its 0° stop (the end where it sits lower)
 0.00 s  door1 starts at its 0° stop (neither end sits lower)
 0.00 s  lever1 starts at its 0° stop (neither end sits lower)
 0.00 s  lever1 is at its largest at the start, 0.0°
 0.00 s  cart2 is at its largest at the start, 0.0 m
 0.02 s  lever1 is at its smallest, -0.0°
 0.03 s  domino1_tile first touches domino1_guide_toe
 0.03 s  domino1_tile leaves domino1_guide_toe
 0.55 s  ball1_sphere leaves ramp1_launch_shelf
 0.55 s  cart1_chassis first touches ball1_sphere
 0.55 s  ball1 starts moving
 0.56 s  cart1_chassis leaves ball1_sphere
 0.59 s  ball1_sphere touches ramp1_launch_shelf again
 0.62 s  cart1 passes 0.01 m from ramp1 (ramp1_launch_shelf) without touching it: nearest points (-1.08, 0.09, 0.50) m and (-1.08, 0.09, 0.49) m
 0.62 s  ball1_sphere first touches ramp1_incline
 0.66 s  ball1_sphere leaves ramp1_launch_shelf
 0.66 s  cart1_chassis touches ball1_sphere again
 0.66 s  cart1_chassis leaves ball1_sphere
 0.71 s  cart1 reaches its upper stop (0.58 m) moving +0.40 m/s
 0.73 s  cart1 is at its largest, 0.6 m
 1.40 s  ball1 passes 0.13 m from ball1_catch (ball1_catch_start) without touching it: nearest points (-0.15, 0.00, 0.20) m and (-0.19, 0.00, 0.08) m
 1.47 s  ball1_sphere leaves ramp1_incline
 1.51 s  ball1_sphere first touches pendulum1_bob
 1.52 s  ball1_sphere leaves pendulum1_bob
 1.67 s  ball1_sphere first touches floor
 1.68 s  ball1_sphere leaves floor
 1.72 s  ball1_sphere touches floor again
 1.73 s  ball1 passes 0.32 m from door1 (door1_panel) without touching it: nearest points (0.21, 0.00, 0.05) m and (0.54, 0.00, 0.05) m
 1.73 s  pendulum1_bob first touches door1_panel
 1.73 s  pendulum1 reaches its 40° stop (the end where it sits higher) moving +292°/s
 1.74 s  pendulum1_bob leaves door1_panel
 1.74 s  pendulum1 passes 0.32 m from block1_guide (block1_guide_roof) without touching it: nearest points (0.54, 0.00, 0.25) m and (0.84, -0.03, 0.15) m
 1.74 s  pendulum1 passes 0.40 m from block1 (block1_cube) without touching it: nearest points (0.54, -0.01, 0.25) m and (0.90, -0.10, 0.12) m
 1.74 s  pendulum1 is at its largest, 40.1°
 1.80 s  door1 passes -0.10 m from ball1_catch (ball1_catch_end) without touching it: nearest points (0.70, -0.05, 0.02) m and (0.70, -0.05, 0.12) m
 1.82 s  door1_panel first touches block1_cube
 1.82 s  block1 starts moving
 1.82 s  block1_cube first touches block1_guide_right
 1.82 s  block1_cube first touches block1_guide_roof
 1.82 s  door1 is at its largest, 71.1°
 1.83 s  door1_panel leaves block1_cube
 1.83 s  block1_cube leaves block1_guide_right
 1.83 s  block1_cube leaves block1_guide_roof
 1.83 s  block1_cube first touches block1_guide_left
 1.83 s  door1 passes -0.09 m from block1_guide (block1_guide_left) without touching it: nearest points (0.95, -0.05, 0.13) m and (0.86, -0.08, 0.13) m
 1.83 s  door1 passes 0.41 m from domino1_guide (domino1_guide_left) without touching it: nearest points (0.94, -0.10, 0.07) m and (1.08, -0.48, 0.07) m
 1.83 s  door1 passes 0.43 m from domino1 (domino1_tile) without touching it: nearest points (0.96, -0.09, 0.08) m and (1.11, -0.49, 0.08) m
 1.83 s  door1 reaches its 70° stop (neither end sits lower) moving -58°/s
 1.84 s  block1_cube leaves block1_guide_left
 1.88 s  block1_cube touches block1_guide_right again
 1.89 s  block1_cube leaves block1_guide_right
 1.89 s  block1 comes to rest at (0.99, -0.16, 0.06) m
 2.03 s  ball1 comes to rest at (0.21, 0.00, 0.05) m

State every 0.25 s:
0.00 s: cart1 at 0.000 m, still; touching nothing | ball1 at (-0.98, 0.00, 0.54) m, at rest; touching ramp1_launch_shelf | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (0.98, -0.14, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at 0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
0.25 s: cart1 at 0.181 m, moving +1.14 m/s; touching nothing | ball1 at (-0.98, 0.00, 0.54) m, at rest; touching ramp1_launch_shelf | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (0.98, -0.14, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
0.50 s: cart1 at 0.453 m, moving +1.04 m/s; touching nothing | ball1 at (-0.98, 0.00, 0.54) m, at rest; touching ramp1_launch_shelf | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (0.98, -0.14, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
0.75 s: cart1 at 0.580 m, moving -0.03 m/s; touching nothing | ball1 at (-0.88, 0.00, 0.52) m, moving 0.64 m/s (vx +0.59, vy +0.00, vz -0.24); touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (0.98, -0.14, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
1.00 s: cart1 at 0.572 m, moving -0.03 m/s; touching nothing | ball1 at (-0.68, 0.00, 0.45) m, moving 1.08 m/s (vx +1.03, vy +0.00, vz -0.30); touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (0.98, -0.14, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
1.25 s: cart1 at 0.565 m, moving -0.03 m/s; touching nothing | ball1 at (-0.37, 0.00, 0.34) m, moving 1.56 m/s (vx +1.42, vy +0.00, vz -0.63); touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (0.98, -0.14, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
1.50 s: cart1 at 0.558 m, moving -0.02 m/s; touching nothing | ball1 at (0.04, 0.00, 0.19) m, moving 2.03 m/s (vx +1.83, vy +0.00, vz -0.87); touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (0.98, -0.14, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
1.75 s: cart1 at 0.553 m, moving -0.02 m/s; touching nothing | ball1 at (0.17, 0.00, 0.05) m, moving 0.24 m/s (vx +0.24, vy +0.00, vz +0.01); touching floor | pendulum1 at 40.0°, turning -5°/s; touching nothing | door1 at 4.6°, turning +325°/s; touching nothing | block1 at (0.98, -0.14, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
2.00 s: cart1 at 0.547 m, moving -0.02 m/s; touching nothing | ball1 at (0.21, 0.00, 0.05) m, moving 0.07 m/s (vx +0.07, vy +0.00, vz -0.01); touching nothing | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
2.25 s: cart1 at 0.543 m, moving -0.02 m/s; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
2.50 s: cart1 at 0.538 m, moving -0.02 m/s; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
2.75 s: cart1 at 0.534 m, moving -0.01 m/s; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
3.00 s: cart1 at 0.531 m, moving -0.01 m/s; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
3.25 s: cart1 at 0.528 m, moving -0.01 m/s; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
3.50 s: cart1 at 0.525 m, moving -0.01 m/s; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
3.75 s: cart1 at 0.522 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
4.00 s: cart1 at 0.520 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
4.25 s: cart1 at 0.518 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
4.50 s: cart1 at 0.516 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
4.75 s: cart1 at 0.514 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
5.00 s: cart1 at 0.513 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
5.25 s: cart1 at 0.511 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
5.50 s: cart1 at 0.510 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
5.75 s: cart1 at 0.509 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
6.00 s: cart1 at 0.508 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
6.25 s: cart1 at 0.507 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
6.50 s: cart1 at 0.506 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
6.75 s: cart1 at 0.505 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
7.00 s: cart1 at 0.504 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
(the same through 7.25 s)
7.50 s: cart1 at 0.503 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
(the same through 7.75 s)
8.00 s: cart1 at 0.502 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
(the same through 8.25 s)
8.50 s: cart1 at 0.501 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
(the same through 9.00 s)
9.25 s: cart1 at 0.500 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
(the same through 10.00 s)
10.25 s: cart1 at 0.499 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing
(the same through 11.75 s)
12.00 s: cart1 at 0.498 m, still; touching nothing | ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 40.0°, still; touching nothing | door1 at 70.0°, still; touching nothing | block1 at (0.99, -0.16, 0.06) m, at rest; touching floor | domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor | lever1 at -0.0°, still; touching ball2_sphere | ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam | cart2 at 0.000 m, still; touching nothing

At the end (12.00 s):
- cart1 at 0.498 m, still; touching nothing
- ball1 at (0.21, 0.00, 0.05) m, at rest; touching floor
- pendulum1 at 40.0°, still; touching nothing
- door1 at 70.0°, still; touching nothing
- block1 at (0.99, -0.16, 0.06) m, at rest; touching floor
- domino1 at (1.12, -0.53, 0.12) m, at rest; touching floor
- lever1 at -0.0°, still; touching ball2_sphere
- ball2 at (1.40, -1.29, 0.87) m, at rest; touching lever1_beam
- cart2 at 0.000 m, still; touching nothing

Openings (fixed rings, open through the middle; height is the middle of the whole thing), and each loose thing that comes down through one's height:
domino1_guide: an opening 0.20 m across, centre (1.16, -0.63, 0.04) m
- nothing loose comes down through domino1_guide's height
ring1: an opening 0.21 m across, centre (1.40, -1.29, 0.55) m
- nothing loose comes down through ring1's height
ball2_guide: an opening 0.23 m across, centre (1.40, -1.29, 0.95) m
- nothing loose comes down through ball2_guide's height
ball1_catch: an opening 0.52 m across, centre (0.24, 0.00, 0.06) m
- ball1 comes down through ball1_catch's height at 1.67 s, 0.10 m from its centre: through it
- block1 comes down through ball1_catch's height at 0.00 s, 0.74 m from its centre: outside it, missing by 0.48 m (down through that height 4 times; this is the closest)
</history>
