Before the run, at the start:
- seesaw1 already touches seesaw1_catch at the start, so their touch is not something that happens in the run

MuJoCo ran your scene for 12 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 12.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum1: hinge joint pendulum1_hinge about axis (0.00, -1.00, 0.00), range -5° to 125° as MuJoCo applies it; its geoms: pendulum1_rod, pendulum1_bob; starts at 0.0°, still
- ball1: free body; its geoms: ball1_sphere; starts at (0.07, 0.00, 0.51) m, at rest
- cart1: slide joint cart1_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.405 m as MuJoCo applies it; its geoms: cart1_chassis; starts at 0.000 m, still
- domino1: free body; its geoms: domino1_block; starts at (1.66, 0.00, 0.12) m, at rest
- flap1: hinge joint flap1_hinge about axis (0.00, 1.00, 0.00), range 0° to 65° as MuJoCo applies it; its geoms: flap1_panel; starts at 0.0°, still
- ball2: free body; its geoms: ball2_sphere; starts at (2.08, 0.13, 0.51) m, at rest
- seesaw1: hinge joint seesaw1_hinge about axis (0.00, -1.00, 0.00), range 0° to 40° as MuJoCo applies it; its geoms: seesaw1_beam; starts at 0.0°, still
- seesaw1_catch: hinge joint seesaw1_catch_hinge about axis (0.00, 1.00, 0.00), range 0° to 100° as MuJoCo applies it; its geoms: seesaw1_catch_arm; starts at 0.0°, still
- block1: free body; its geoms: block1_cube; starts at (3.57, 0.25, 0.67) m, at rest
- door1: hinge joint door1_hinge about axis (0.00, 1.00, 0.00), range -75° to 0° as MuJoCo applies it; its geoms: door1_panel; starts at 0.0°, still

What happened, in order:
 0.00 s  ball2_sphere starts touching ramp2_staging_pad
 0.00 s  seesaw1_beam starts touching seesaw1_catch_arm
 0.00 s  ball1_sphere starts touching ramp1_staging_pad
 0.00 s  domino1_block starts touching floor
 0.00 s  cart1 starts at its lower stop (0 m)
 0.00 s  flap1 starts at its 0° stop (the end where it sits higher)
 0.00 s  seesaw1 starts at its 0° stop (neither end sits lower)
 0.00 s  seesaw1_catch starts at its 0° stop (the end where it sits higher)
 0.00 s  door1 starts at its 0° stop (the end where it sits lower)
 0.00 s  flap1 is at its smallest, -0.0°
 0.00 s  door1 is at its largest, 0.0°
 0.00 s  seesaw1_beam first touches block1_cube
 0.29 s  block1_cube first touches block1_guide_right_near
 0.29 s  block1_cube first touches block1_guide_right_far
 0.29 s  block1_cube leaves block1_guide_right_near
 0.29 s  block1_cube leaves block1_guide_right_far
 0.36 s  block1_cube touches block1_guide_right_near again
 0.36 s  block1_cube touches block1_guide_right_far again
 0.40 s  ball1_sphere leaves ramp1_staging_pad
 0.40 s  pendulum1_bob first touches ball1_sphere
 0.40 s  ball1 starts moving
 0.41 s  pendulum1_bob leaves ball1_sphere
 0.44 s  ball1 is at the top of its flight, at (0.11, 0.00, 0.52) m
 0.45 s  block1_cube leaves block1_guide_right_far
 0.49 s  block1_cube touches block1_guide_right_far again
 0.57 s  ball1_sphere first touches ramp1_surface
 0.75 s  pendulum1 is at its largest, 73.9°
 1.07 s  ball1_sphere leaves ramp1_surface
 1.10 s  ball1_sphere first touches cart1_chassis
 1.11 s  ball1_sphere leaves cart1_chassis
 1.25 s  ball1 passes 0.02 m from cart1_track (cart1_track_near) without touching it: nearest points (1.02, -0.05, 0.05) m and (1.02, -0.07, 0.05) m
 1.26 s  ball1_sphere first touches floor
 1.27 s  ball1_sphere leaves floor
 1.33 s  ball1_sphere touches floor again
 1.65 s  ball1 comes to rest at (1.06, 0.00, 0.05) m
 1.88 s  cart1 reaches its upper stop (0.405 m) moving +0.44 m/s
 1.88 s  cart1_chassis first touches domino1_block
 1.88 s  domino1 starts moving
 1.90 s  cart1_chassis leaves domino1_block
 1.91 s  cart1 is at its largest, 0.4 m
 1.92 s  cart1 passes 0.20 m from flap1 (flap1_panel) without touching it: nearest points (1.64, 0.08, 0.18) m and (1.84, 0.08, 0.18) m
 1.92 s  cart1 passes 0.47 m from ramp2 (ramp2_surface) without touching it: nearest points (1.64, 0.09, 0.18) m and (2.04, 0.10, 0.43) m
 1.92 s  cart1 passes 0.50 m from ball2 (ball2_sphere) without touching it: nearest points (1.64, 0.09, 0.18) m and (2.04, 0.13, 0.48) m
 2.30 s  domino1_block first touches flap1_panel
 2.30 s  domino1_block leaves flap1_panel
 2.36 s  domino1_block touches flap1_panel again
 2.36 s  domino1 comes to rest at (1.75, 0.00, 0.10) m
 2.67 s  flap1_panel first touches ball2_sphere
 2.67 s  ball2 starts moving
 2.69 s  flap1_panel leaves ball2_sphere
 2.75 s  flap1 passes 0.00 m from ramp2 (ramp2_staging_pad) without touching it: nearest points (2.05, 0.10, 0.45) m and (2.05, 0.10, 0.45) m
 2.89 s  ball2_sphere leaves ramp2_staging_pad
 2.90 s  ball2_sphere first touches ramp2_surface
 2.95 s  flap1 reaches its 65° stop (the end where it sits lower) moving +275°/s
 2.95 s  flap1 is at its largest, 65.1°
 3.25 s  ball2_sphere leaves ramp2_surface
 3.26 s  ball2_sphere first touches ramp2_near_funnel
 3.26 s  ball2_sphere leaves ramp2_near_funnel
 3.28 s  ball2_sphere touches ramp2_surface again
 3.59 s  ball2_sphere leaves ramp2_surface
 3.60 s  ball2_sphere first touches ramp2_far_funnel
 3.60 s  ball2_sphere leaves ramp2_far_funnel
 3.65 s  ball2_sphere touches ramp2_surface again
 3.68 s  ball2_sphere leaves ramp2_surface
 3.68 s  ball2_sphere touches ramp2_near_funnel again
 3.68 s  ball2_sphere leaves ramp2_near_funnel
 3.71 s  ball2_sphere touches ramp2_far_funnel again
 3.71 s  ball2_sphere leaves ramp2_far_funnel
 3.75 s  seesaw1_catch is at its smallest, -0.0°
 3.75 s  seesaw1_beam leaves seesaw1_catch_arm
 3.75 s  ball2_sphere first touches seesaw1_catch_arm
 3.75 s  seesaw1 is at its smallest, -0.0°
 3.75 s  block1 starts moving
 3.76 s  ball2 passes 0.01 m from seesaw1 (seesaw1_beam) without touching it: nearest points (3.05, 0.25, 0.21) m and (3.06, 0.25, 0.21) m
 3.77 s  block1_cube first touches block1_guide_left_far
 3.77 s  block1_cube first touches block1_guide_left_near
 3.77 s  ball2 passes 0.45 m from ring1 (ring1_segment_4) without touching it: nearest points (3.06, 0.25, 0.20) m and (3.47, 0.25, 0.37) m
 3.77 s  ball2 passes 0.49 m from block1_guide (block1_guide_left_near) without touching it: nearest points (3.06, 0.25, 0.20) m and (3.50, 0.20, 0.40) m
 3.79 s  ball2_sphere leaves seesaw1_catch_arm
 3.80 s  seesaw1_beam touches seesaw1_catch_arm again
 3.82 s  seesaw1_beam leaves seesaw1_catch_arm
 3.82 s  block1_cube leaves block1_guide_right_near
 3.82 s  block1_cube leaves block1_guide_right_far
 3.83 s  ball2_sphere touches seesaw1_catch_arm again
 3.86 s  block1_cube touches block1_guide_right_near again
 3.86 s  block1_cube touches block1_guide_right_far again
 3.87 s  ball2 passes 0.29 m from door1 (door1_panel) without touching it: nearest points (3.07, 0.24, 0.09) m and (3.36, 0.24, 0.06) m
 3.87 s  ball2_sphere leaves seesaw1_catch_arm
 3.90 s  seesaw1_beam touches seesaw1_catch_arm again
 3.91 s  block1_cube leaves block1_guide_right_near
 3.91 s  block1_cube leaves block1_guide_right_far
 3.91 s  ball2_sphere first touches floor
 3.94 s  block1_cube touches block1_guide_right_near again
 3.94 s  block1_cube leaves block1_guide_right_near
 3.94 s  block1_cube touches block1_guide_right_far 6 more times between 3.94 s and 6.64 s
 3.99 s  block1_cube touches block1_guide_right_near 5 more times between 3.99 s and 6.64 s
 4.15 s  seesaw1_beam leaves seesaw1_catch_arm
 4.22 s  seesaw1_beam touches seesaw1_catch_arm again
 4.24 s  seesaw1_beam leaves seesaw1_catch_arm
 4.52 s  seesaw1_beam touches seesaw1_catch_arm 1 more times between 4.52 s and 4.58 s
 4.55 s  seesaw1_beam leaves block1_cube
 4.57 s  block1_cube leaves block1_guide_left_far
 4.57 s  block1_cube leaves block1_guide_left_near
 4.60 s  seesaw1 reaches its 40° stop (neither end sits lower) moving +514°/s
 4.60 s  seesaw1 is at its largest, 40.2°
 4.61 s  seesaw1 passes 0.11 m from door1 (door1_panel) without touching it: nearest points (3.25, 0.30, 0.09) m and (3.36, 0.30, 0.06) m
 4.61 s  block1_cube touches block1_guide_left_far again
 4.61 s  block1_cube touches block1_guide_left_near again
 4.75 s  ball2 comes to rest at (2.89, 0.15, 0.05) m
 4.99 s  seesaw1_catch passes 0.14 m from door1 (door1_panel) without touching it: nearest points (3.22, 0.25, 0.05) m and (3.36, 0.25, 0.05) m
 5.18 s  seesaw1_catch reaches its 100° stop (the end where it sits lower) moving +39°/s
 5.19 s  seesaw1_catch is at its largest, 100.0°
 6.65 s  block1_cube leaves block1_guide_left_far
 6.65 s  block1_cube leaves block1_guide_left_near
 6.68 s  block1_cube first touches ring1_segment_8
 6.68 s  block1_cube leaves ring1_segment_8
 6.68 s  block1_cube first touches ring1_segment_1
 6.68 s  block1_cube leaves ring1_segment_1
 6.81 s  block1_cube first touches door1_panel
 6.81 s  seesaw1_catch passes 0.30 m from block1 (block1_cube) without touching it: nearest points (3.22, 0.25, 0.03) m and (3.50, 0.25, 0.14) m
 6.82 s  block1_cube leaves door1_panel
 6.87 s  block1_cube touches door1_panel again
 6.99 s  block1 comes to rest at (3.59, 0.25, 0.12) m
 9.91 s  pendulum1 passes 0.03 m from ramp1 (ramp1_staging_pad) without touching it: nearest points (0.00, 0.00, 0.49) m and (0.00, 0.00, 0.46) m

State every 0.25 s:
0.00 s: pendulum1 at 0.0°, still; touching nothing | ball1 at (0.07, 0.00, 0.51) m, at rest; touching ramp1_staging_pad | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | ball2 at (2.08, 0.13, 0.51) m, at rest; touching ramp2_staging_pad | seesaw1 at 0.0°, still; touching seesaw1_catch_arm | seesaw1_catch at 0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching nothing | door1 at 0.0°, still; touching nothing
0.25 s: pendulum1 at 24.9°, turning +181°/s; touching nothing | ball1 at (0.07, 0.00, 0.51) m, at rest; touching ramp1_staging_pad | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.08, 0.13, 0.51) m, at rest; touching ramp2_staging_pad | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at 0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching seesaw1_beam | door1 at 0.0°, still; touching nothing
0.50 s: pendulum1 at 63.5°, turning +75°/s; touching nothing | ball1 at (0.17, 0.00, 0.50) m, moving 1.19 m/s (vx +1.02, vy +0.00, vz -0.61); touching nothing | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.08, 0.13, 0.51) m, at rest; touching ramp2_staging_pad | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at 0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
0.75 s: pendulum1 at 73.9°, turning +2°/s; touching nothing | ball1 at (0.43, 0.00, 0.37) m, moving 1.27 m/s (vx +1.19, vy +0.00, vz -0.44); touching nothing | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.08, 0.13, 0.51) m, at rest; touching ramp2_staging_pad | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
1.00 s: pendulum1 at 64.6°, turning -67°/s; touching nothing | ball1 at (0.79, 0.00, 0.24) m, moving 1.77 m/s (vx +1.68, vy +0.00, vz -0.54); touching ramp1_surface | cart1 at 0.000 m, still; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.08, 0.13, 0.51) m, at rest; touching ramp2_staging_pad | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
1.25 s: pendulum1 at 46.7°, turning -63°/s; touching nothing | ball1 at (1.02, 0.00, 0.06) m, moving 1.56 m/s (vx +0.32, vy +0.00, vz -1.53); touching nothing | cart1 at 0.086 m, moving +0.56 m/s; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.08, 0.13, 0.51) m, at rest; touching ramp2_staging_pad | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
1.50 s: pendulum1 at 38.6°, turning +3°/s; touching nothing | ball1 at (1.05, 0.00, 0.05) m, moving 0.09 m/s (vx +0.09, vy +0.00, vz +0.00); touching floor | cart1 at 0.220 m, moving +0.51 m/s; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.08, 0.13, 0.51) m, at rest; touching ramp2_staging_pad | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
1.75 s: pendulum1 at 47.6°, turning +60°/s; touching nothing | ball1 at (1.06, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.341 m, moving +0.46 m/s; touching nothing | domino1 at (1.66, 0.00, 0.12) m, at rest; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.08, 0.13, 0.51) m, at rest; touching ramp2_staging_pad | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
2.00 s: pendulum1 at 63.1°, turning +52°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.403 m, moving -0.02 m/s; touching nothing | domino1 at (1.68, 0.00, 0.12) m, moving 0.14 m/s (vx +0.14, vy +0.00, vz -0.01), turned 8° from how it started; touching nothing | flap1 at -0.0°, still; touching nothing | ball2 at (2.08, 0.13, 0.51) m, at rest; touching ramp2_staging_pad | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
2.25 s: pendulum1 at 69.2°, turning -7°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.397 m, moving -0.02 m/s; touching nothing | domino1 at (1.73, 0.00, 0.11) m, moving 0.37 m/s (vx +0.34, vy +0.00, vz -0.14), turned 31° from how it started; touching floor | flap1 at -0.0°, still; touching nothing | ball2 at (2.08, 0.13, 0.51) m, at rest; touching ramp2_staging_pad | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
2.50 s: pendulum1 at 60.6°, turning -54°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.392 m, moving -0.02 m/s; touching nothing | domino1 at (1.75, 0.00, 0.10) m, at rest, turned 43° from how it started; touching flap1_panel, floor | flap1 at 9.9°, turning +62°/s; touching domino1_block | ball2 at (2.08, 0.13, 0.51) m, at rest; touching ramp2_staging_pad | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
2.75 s: pendulum1 at 47.2°, turning -43°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.387 m, moving -0.02 m/s; touching nothing | domino1 at (1.75, 0.00, 0.10) m, at rest, turned 45° from how it started; touching flap1_panel, floor | flap1 at 29.4°, turning +80°/s; touching domino1_block | ball2 at (2.09, 0.14, 0.51) m, moving 0.15 m/s (vx +0.14, vy +0.07, vz -0.03); touching nothing | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
3.00 s: pendulum1 at 42.8°, turning +10°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.383 m, moving -0.02 m/s; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.18, 0.15, 0.47) m, moving 0.68 m/s (vx +0.63, vy +0.06, vz -0.23); touching nothing | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
3.25 s: pendulum1 at 51.0°, turning +48°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.379 m, moving -0.01 m/s; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.40, 0.17, 0.39) m, moving 1.18 m/s (vx +1.12, vy +0.05, vz -0.36); touching nothing | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
3.50 s: pendulum1 at 62.4°, turning +35°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.376 m, moving -0.01 m/s; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.69, 0.25, 0.29) m, moving 1.52 m/s (vx +1.39, vy +0.32, vz -0.52); touching nothing | seesaw1 at 0.0°, still; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at -0.0°, still; touching seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
3.75 s: pendulum1 at 65.4°, turning -12°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.373 m, moving -0.01 m/s; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (3.01, 0.25, 0.18) m, moving 0.40 m/s (vx +0.29, vy -0.11, vz -0.26); touching seesaw1_catch_arm | seesaw1 at -0.0°, turning -25°/s; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at 0.1°, turning +39°/s; touching ball2_sphere, seesaw1_beam | block1 at (3.57, 0.25, 0.67) m, at rest; touching block1_guide_right_far, block1_guide_right_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
4.00 s: pendulum1 at 57.7°, turning -43°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.370 m, moving -0.01 m/s; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.99, 0.22, 0.05) m, moving 0.26 m/s (vx -0.22, vy -0.14, vz +0.01); touching floor | seesaw1 at 7.4°, turning +19°/s; touching block1_cube, seesaw1_catch_arm | seesaw1_catch at 21.3°, turning +43°/s; touching seesaw1_beam | block1 at (3.57, 0.25, 0.70) m, moving 0.14 m/s (vx +0.04, vy -0.00, vz +0.13); touching block1_guide_left_far, block1_guide_left_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
4.25 s: pendulum1 at 48.0°, turning -28°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.367 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.94, 0.19, 0.05) m, moving 0.19 m/s (vx -0.16, vy -0.10, vz +0.00); touching floor | seesaw1 at 12.6°, turning +25°/s; touching block1_cube | seesaw1_catch at 32.0°, turning +26°/s; touching nothing | block1 at (3.57, 0.25, 0.72) m, at rest; touching seesaw1_beam | door1 at 0.0°, still; touching nothing
4.50 s: pendulum1 at 46.2°, turning +13°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.365 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.91, 0.17, 0.05) m, moving 0.12 m/s (vx -0.10, vy -0.07, vz +0.00); touching floor | seesaw1 at 14.8°, still; touching block1_cube | seesaw1_catch at 37.4°, turning +23°/s; touching nothing | block1 at (3.57, 0.25, 0.73) m, at rest; touching block1_guide_left_far, block1_guide_left_near, seesaw1_beam | door1 at 0.0°, still; touching nothing
4.75 s: pendulum1 at 53.3°, turning +37°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.363 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 82.8°, turning +39°/s; touching nothing | block1 at (3.57, 0.25, 0.70) m, moving 0.17 m/s (vx -0.10, vy -0.00, vz -0.14); touching nothing | door1 at 0.0°, still; touching nothing
5.00 s: pendulum1 at 61.5°, turning +22°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.361 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 92.5°, turning +39°/s; touching nothing | block1 at (3.57, 0.25, 0.66) m, moving 0.30 m/s (vx +0.14, vy -0.00, vz -0.27); touching nothing | door1 at 0.0°, still; touching nothing
5.25 s: pendulum1 at 62.4°, turning -14°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.359 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.57, 0.25, 0.62) m, moving 0.14 m/s (vx +0.05, vy -0.00, vz -0.13); touching block1_guide_left_far, block1_guide_left_near | door1 at 0.0°, still; touching nothing
5.50 s: pendulum1 at 55.9°, turning -33°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.358 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.57, 0.25, 0.58) m, moving 0.29 m/s (vx +0.03, vy -0.00, vz -0.29); touching nothing | door1 at 0.0°, still; touching nothing
5.75 s: pendulum1 at 49.0°, turning -17°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.356 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.57, 0.25, 0.53) m, moving 0.17 m/s (vx +0.10, vy -0.00, vz -0.14); touching nothing | door1 at 0.0°, still; touching nothing
6.00 s: pendulum1 at 48.8°, turning +14°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.355 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.57, 0.25, 0.49) m, moving 0.20 m/s (vx -0.12, vy -0.00, vz -0.16); touching nothing | door1 at 0.0°, still; touching nothing
6.25 s: pendulum1 at 54.8°, turning +28°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.354 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.57, 0.25, 0.46) m, moving 0.18 m/s (vx +0.11, vy -0.00, vz -0.14); touching nothing | door1 at 0.0°, still; touching nothing
6.50 s: pendulum1 at 60.4°, turning +13°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.353 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.57, 0.25, 0.41) m, moving 0.27 m/s (vx -0.06, vy +0.00, vz -0.26); touching block1_guide_right_far, block1_guide_right_near | door1 at 0.0°, still; touching nothing
6.75 s: pendulum1 at 60.1°, turning -14°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.352 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.57, 0.25, 0.24) m, moving 1.45 m/s (vx -0.06, vy -0.00, vz -1.45), turned 11° from how it started; touching nothing | door1 at 0.0°, still; touching nothing
7.00 s: pendulum1 at 54.7°, turning -25°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.351 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
7.25 s: pendulum1 at 50.1°, turning -9°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.350 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
7.50 s: pendulum1 at 50.8°, turning +14°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.350 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
7.75 s: pendulum1 at 55.7°, turning +21°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.349 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
8.00 s: pendulum1 at 59.4°, turning +6°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.348 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
8.25 s: pendulum1 at 58.4°, turning -13°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.348 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
8.50 s: pendulum1 at 54.1°, turning -18°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.347 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
8.75 s: pendulum1 at 51.1°, turning -4°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.347 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
9.00 s: pendulum1 at 52.3°, turning +13°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.347 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
9.25 s: pendulum1 at 56.1°, turning +15°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.346 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
9.50 s: pendulum1 at 58.5°, turning +2°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.346 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
9.75 s: pendulum1 at 57.2°, turning -12°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.346 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
10.00 s: pendulum1 at 53.8°, turning -13°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.345 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
10.25 s: pendulum1 at 51.9°, still; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.345 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
10.50 s: pendulum1 at 53.3°, turning +11°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.345 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
10.75 s: pendulum1 at 56.3°, turning +11°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.345 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
11.00 s: pendulum1 at 57.7°, still; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.345 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
11.25 s: pendulum1 at 56.3°, turning -10°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.344 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
11.50 s: pendulum1 at 53.7°, turning -9°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.344 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
11.75 s: pendulum1 at 52.7°, still; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.344 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube
12.00 s: pendulum1 at 54.1°, turning +9°/s; touching nothing | ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor | cart1 at 0.344 m, still; touching nothing | domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor | flap1 at 65.0°, still; touching domino1_block | ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor | seesaw1 at 40.0°, still; touching nothing | seesaw1_catch at 100.0°, still; touching nothing | block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel | door1 at 0.0°, still; touching block1_cube

At the end (12.00 s):
- pendulum1 at 54.1°, turning +9°/s; touching nothing
- ball1 at (1.07, 0.00, 0.05) m, at rest; touching floor
- cart1 at 0.344 m, still; touching nothing
- domino1 at (1.76, 0.00, 0.10) m, at rest, turned 47° from how it started; touching flap1_panel, floor
- flap1 at 65.0°, still; touching domino1_block
- ball2 at (2.89, 0.15, 0.05) m, at rest; touching floor
- seesaw1 at 40.0°, still; touching nothing
- seesaw1_catch at 100.0°, still; touching nothing
- block1 at (3.59, 0.25, 0.12) m, at rest; touching door1_panel
- door1 at 0.0°, still; touching block1_cube

Openings (fixed rings, open through the middle; height is the middle of the whole thing), and each loose thing that comes down through one's height:
block1_guide: an opening 0.14 m across, centre (3.57, 0.25, 0.75) m
- nothing loose comes down through block1_guide's height
ring1: an opening 0.19 m across, centre (3.57, 0.25, 0.37) m
- ball1 comes down through ring1's height at 0.73 s, 3.18 m from its centre: outside it, missing by 3.08 m
- ball2 comes down through ring1's height at 3.31 s, 1.12 m from its centre: outside it, missing by 1.02 m
- block1 comes down through ring1's height at 6.59 s, 0.00 m from its centre: through it
</history>
