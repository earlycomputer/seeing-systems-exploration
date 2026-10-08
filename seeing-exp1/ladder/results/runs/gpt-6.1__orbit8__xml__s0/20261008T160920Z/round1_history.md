Before the run, at the start:
- seesaw1 already touches seesaw1_catch at the start, so their touch is not something that happens in the run

MuJoCo ran your scene for 12 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 12.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum1: hinge joint pendulum1_hinge about axis (0.00, -1.00, 0.00), range -5° to 125° as MuJoCo applies it; its geoms: pendulum1_rod, pendulum1_bob; starts at 0.0°, still
- ball1: free body; its geoms: ball1_sphere; starts at (0.09, 0.00, 0.48) m, at rest
- cart1: slide joint cart1_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.4 m as MuJoCo applies it; its geoms: cart1_chassis; starts at 0.000 m, still
- domino1: free body; its geoms: domino1_block; starts at (1.66, 0.00, 0.12) m, at rest
- flap1: hinge joint flap1_hinge about axis (0.00, 1.00, 0.00), range 0° to 65° as MuJoCo applies it; its geoms: flap1_panel; starts at 0.0°, still
- ball2: free body; its geoms: ball2_sphere; starts at (2.14, 0.13, 0.48) m, at rest
- seesaw1: hinge joint seesaw1_hinge about axis (0.00, -1.00, 0.00), range 0° to 40° as MuJoCo applies it; its geoms: seesaw1_beam; starts at 0.0°, still
- seesaw1_catch: hinge joint seesaw1_catch_hinge about axis (0.00, 1.00, 0.00), range 0° to 100° as MuJoCo applies it; its geoms: seesaw1_catch_arm; starts at 0.0°, still
- block1: free body; its geoms: block1_cube; starts at (3.57, 0.25, 0.67) m, at rest
- door1: hinge joint door1_hinge about axis (0.00, 1.00, 0.00), range -75° to 0° as MuJoCo applies it; its geoms: door1_panel; starts at 0.0°, still

What happened, in order:
 0.00 s  ball1_sphere starts touching ramp1_retaining_lip
 0.00 s  seesaw1_beam starts touching seesaw1_catch_arm
 0.00 s  ball1_sphere starts touching ramp1_surface
 0.00 s  ball2_sphere starts touching ramp2_surface
 0.00 s  ball2_sphere starts touching ramp2_retaining_lip
 0.00 s  domino1_block starts touching floor
 0.00 s  cart1 starts at its lower stop (0 m)
 0.00 s  cart1 is at its largest at the start, 0.0 m
 0.00 s  flap1 starts at its 0° stop (the end where it sits higher)
 0.00 s  flap1 is at its largest at the start, 0.0°
 0.00 s  seesaw1 starts at its 0° stop (neither end sits lower)
 0.00 s  seesaw1_catch starts at its 0° stop (the end where it sits higher)
 0.00 s  door1 starts at its 0° stop (the end where it sits lower)
 0.00 s  seesaw1_beam first touches block1_cube
 0.01 s  flap1 is at its smallest, -0.0°
 0.01 s  door1 is at its largest, 0.0°
 0.02 s  seesaw1_catch is at its largest, 0.0°
 0.29 s  block1_cube first touches block1_guide_right_near
 0.29 s  block1_cube first touches block1_guide_right_far
 0.29 s  block1_cube leaves block1_guide_right_near
 0.29 s  block1_cube leaves block1_guide_right_far
 0.36 s  block1_cube touches block1_guide_right_near again
 0.36 s  block1_cube touches block1_guide_right_far again
 0.40 s  pendulum1_bob first touches ball1_sphere
 0.40 s  ball1 starts moving
 0.40 s  pendulum1 is at its largest, 55.3°
 0.41 s  pendulum1_bob leaves ball1_sphere
 0.41 s  ball1_sphere leaves ramp1_retaining_lip
 0.45 s  block1_cube leaves block1_guide_right_far
 0.47 s  ball1_sphere touches ramp1_retaining_lip again
 0.47 s  ball1_sphere leaves ramp1_surface
 0.49 s  block1_cube touches block1_guide_right_far again
 0.52 s  ball1_sphere leaves ramp1_retaining_lip
 0.52 s  ball1_sphere touches ramp1_surface again
 0.52 s  ball1 comes to rest at (0.09, 0.00, 0.48) m
 0.56 s  ball1_sphere touches ramp1_retaining_lip again
 0.56 s  ball1_sphere leaves ramp1_surface
 0.60 s  ball1_sphere touches ramp1_surface again
 1.14 s  pendulum1_bob touches ball1_sphere again
 1.15 s  pendulum1_bob leaves ball1_sphere
 1.89 s  pendulum1_bob touches ball1_sphere again
 1.90 s  pendulum1_bob leaves ball1_sphere
 2.10 s  pendulum1 passes 0.02 m from ramp1 (ramp1_surface) without touching it: nearest points (0.00, 0.00, 0.48) m and (0.00, 0.00, 0.46) m
 2.63 s  pendulum1_bob touches ball1_sphere again
 2.64 s  pendulum1_bob leaves ball1_sphere
 3.37 s  pendulum1_bob touches ball1_sphere 4 more times between 3.37 s and 5.84 s
 9.65 s  block1_cube first touches block1_guide_left_far
 9.65 s  block1_cube first touches block1_guide_left_near
 9.65 s  block1_cube leaves block1_guide_right_near
 9.65 s  block1_cube leaves block1_guide_right_far
12.00 s  seesaw1 is at its largest, 0.3°
12.00 s  seesaw1_catch is at its smallest, -1.0°

State every 0.25 s:
0.00 s: pendulum1 at 0.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching seesaw1_catch_arm | seesaw1_catch at 0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching nothing | door1 at 0.0°, still; touching nothing
0.25 s: pendulum1 at 24.9°, turning +181°/s; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at 0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching seesaw1_beam | door1 at 0.0°, still; touching nothing
0.50 s: pendulum1 at 51.6°, turning -35°/s; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at 0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
0.75 s: pendulum1 at 46.4°, turning -2°/s; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
1.00 s: pendulum1 at 50.3°, turning +30°/s; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
1.25 s: pendulum1 at 54.0°, turning -9°/s; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
1.50 s: pendulum1 at 52.8°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
1.75 s: pendulum1 at 53.9°, turning +8°/s; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching seesaw1_beam | door1 at 0.0°, still; touching nothing
2.00 s: pendulum1 at 54.7°, turning -2°/s; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
2.25 s: pendulum1 at 54.4°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.1°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
2.50 s: pendulum1 at 54.7°, turning +2°/s; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.1°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
2.75 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.1°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
3.00 s: pendulum1 at 54.9°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.1°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, seesaw1_beam | door1 at 0.0°, still; touching nothing
3.25 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.1°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
(the same through 4.00 s)
4.25 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.2°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
(the same through 5.25 s)
5.50 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.2°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching seesaw1_beam | door1 at 0.0°, still; touching nothing
5.75 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.3°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
(the same through 6.25 s)
6.50 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.3°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching seesaw1_beam | door1 at 0.0°, still; touching nothing
6.75 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.4°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
7.00 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.4°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching seesaw1_beam | door1 at 0.0°, still; touching nothing
7.25 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.1°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.4°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching seesaw1_beam | door1 at 0.0°, still; touching nothing
7.50 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.1°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.4°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
7.75 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.1°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.5°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
8.00 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.1°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.5°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching seesaw1_beam | door1 at 0.0°, still; touching nothing
(the same through 8.25 s)
8.50 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.1°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.6°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching seesaw1_beam | door1 at 0.0°, still; touching nothing
(the same through 8.75 s)
9.00 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.1°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.6°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
9.25 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.1°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.7°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching seesaw1_beam | door1 at 0.0°, still; touching nothing
(the same through 9.50 s)
9.75 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.2°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.7°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_left_far, block1_guide_left_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
10.00 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.2°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.8°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_left_far, block1_guide_left_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
(the same through 10.50 s)
10.75 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.2°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.9°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_left_far, block1_guide_left_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
(the same through 11.00 s)
11.25 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.3°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.9°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_left_far, block1_guide_left_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
(the same through 11.75 s)
12.00 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface | seesaw1 at 0.3°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -1.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_left_far, block1_guide_left_near, seesaw1_beam | door1 at 0.0°, still; touching nothing

At the end (12.00 s):
- pendulum1 at 55.0°, still; touching nothing
- ball1 at (0.09, 0.00, 0.48) m, at rest; touching ramp1_retaining_lip, ramp1_surface
- cart1 at 0.000 m, still; touching nothing
- domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor
- flap1 at -0.0°, still; touching nothing
- ball2 at (2.14, 0.13, 0.48) m, at rest; touching ramp2_retaining_lip, ramp2_surface
- seesaw1 at 0.3°, still; touching block1_cube, seesaw1_catch_arm
- seesaw1_catch at -1.0°, still; touching seesaw1_beam
- block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_left_far, block1_guide_left_near, seesaw1_beam
- door1 at 0.0°, still; touching nothing

Openings (fixed rings, open through the middle; height is the middle of the whole thing), and each loose thing that comes down through one's height:
block1_guide: an opening 0.14 m across, centre (3.57, 0.25, 0.75) m
- nothing loose comes down through block1_guide's height
ring1: an opening 0.19 m across, centre (3.57, 0.25, 0.37) m
- nothing loose comes down through ring1's height
</history>
