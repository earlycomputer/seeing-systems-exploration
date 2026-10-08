MuJoCo ran your scene for 12 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 12.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_sphere; starts at (-0.16, 0.10, 1.36) m, at rest
- lever1: hinge joint lever1_hinge about axis (0.00, -1.00, 0.00), range 0° to 45° as MuJoCo applies it; its geoms: lever1_beam; starts at 0.0°, still
- cart1: slide joint cart1_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.6 m as MuJoCo applies it; its geoms: cart1_box; starts at 0.000 m, still
- domino1: free body; its geoms: domino1_box; starts at (0.92, 0.10, 0.43) m, at rest
- ball2: free body; its geoms: ball2_sphere; starts at (1.10, 0.10, 0.54) m, at rest
- door1: hinge joint door1_hinge about axis (0.00, 1.00, 0.00), range 0° to 70° as MuJoCo applies it; its geoms: door1_panel; starts at 0.0°, still
- pendulum1: hinge joint pendulum1_hinge about axis (0.00, 1.00, 0.00), range 0° to 38° as MuJoCo applies it; its geoms: pendulum1_rod; starts at 0.0°, still
- block1: free body; its geoms: block1_cube; starts at (2.90, 0.10, 0.56) m, at rest

What happened, in order:
 0.00 s  ball2_sphere starts touching ramp1_retaining_lip
 0.00 s  lever1 starts at its 0° stop (neither end sits lower)
 0.00 s  cart1 starts at its lower stop (0 m)
 0.00 s  door1 starts at its 0° stop (the end where it sits higher)
 0.00 s  pendulum1 starts at its 0° stop (the end where it sits higher)
 0.00 s  ball2_sphere first touches ramp1_surface
 0.00 s  domino1_box first touches domino_support_box
 0.00 s  block1_cube first touches block_support_box
 0.01 s  ball1 starts moving
 0.25 s  ball1 passes 0.03 m from ring1 (ring1_segment02) without touching it: nearest points (-0.12, 0.13, 1.05) m and (-0.09, 0.14, 1.06) m
 0.34 s  ball1_sphere first touches lever1_beam
 0.38 s  lever1_beam first touches cart1_box
 0.38 s  lever1_beam leaves cart1_box
 0.45 s  ball1_sphere first touches lever_ball_catcher_wall
 0.45 s  ball1 passes 0.35 m from cart1 (cart1_box) without touching it: nearest points (0.00, 0.10, 0.62) m and (0.30, 0.10, 0.46) m
 0.46 s  ball1_sphere leaves lever_ball_catcher_wall
 0.59 s  lever1 reaches its 45° stop (neither end sits lower) moving +172°/s
 0.59 s  lever1 is at its largest, 45.3°
 0.70 s  lever1 reaches its 45° stop (neither end sits lower) again moving +18°/s
 0.72 s  ball1 comes to rest at (-0.07, 0.10, 0.62) m
 1.19 s  cart1 passes 0.05 m from domino_support (domino_support_box) without touching it: nearest points (0.88, 0.19, 0.36) m and (0.88, 0.19, 0.31) m
 1.22 s  cart1_box first touches domino1_box
 1.22 s  domino1 starts moving
 1.25 s  cart1_box leaves domino1_box
 1.30 s  cart1_box touches domino1_box again
 1.32 s  cart1_box leaves domino1_box
 1.45 s  cart1_box touches domino1_box again
 1.45 s  cart1_box leaves domino1_box
 1.77 s  ball2_sphere leaves ramp1_surface
 1.77 s  domino1_box first touches ball2_sphere
 1.78 s  ball2 starts moving
 1.79 s  domino1_box leaves ball2_sphere
 1.82 s  domino1_box touches ball2_sphere again
 2.36 s  cart1 passes 0.14 m from ball2 (ball2_sphere) without touching it: nearest points (0.93, 0.10, 0.46) m and (1.06, 0.10, 0.52) m
 2.36 s  cart1 is at its largest, 0.4 m
 2.36 s  cart1_box touches domino1_box again
 2.37 s  cart1 passes 0.14 m from ramp1 (ramp1_surface) without touching it: nearest points (0.93, 0.11, 0.45) m and (1.07, 0.11, 0.45) m
 2.38 s  cart1_box leaves domino1_box
 4.33 s  domino1_box leaves ball2_sphere
 4.37 s  domino1_box touches ball2_sphere again
 4.37 s  domino1_box leaves ball2_sphere
 4.41 s  domino1_box first touches ramp1_surface
 4.42 s  domino1 comes to rest at (1.00, 0.10, 0.42) m
 4.50 s  ball2_sphere leaves ramp1_retaining_lip
 4.52 s  ball2_sphere touches ramp1_surface again
 5.27 s  ball2_sphere leaves ramp1_surface
 5.31 s  ball2_sphere first touches door1_panel
 5.32 s  ball2_sphere leaves door1_panel
 5.35 s  ball2_sphere touches ramp1_surface again
 5.36 s  ball2_sphere leaves ramp1_surface
 5.42 s  ball2 passes 0.39 m from pendulum1 (pendulum1_rod) without touching it: nearest points (2.13, 0.10, 0.14) m and (2.52, 0.10, 0.17) m
 5.43 s  ball2_sphere touches door1_panel again
 5.43 s  ball2_sphere leaves door1_panel
 5.51 s  ball2_sphere first touches floor
 5.53 s  ball2_sphere leaves floor
 5.56 s  ball2_sphere touches floor again
 5.71 s  door1 passes 0.40 m from block1 (block1_cube) without touching it: nearest points (2.50, 0.16, 0.30) m and (2.84, 0.16, 0.50) m
 5.73 s  door1_panel first touches pendulum1_rod
 5.74 s  door1_panel leaves pendulum1_rod
 5.76 s  ball2 comes to rest at (2.04, 0.10, 0.05) m
 5.80 s  door1_panel touches pendulum1_rod again
 5.92 s  door1 reaches its 70° stop (the end where it sits lower) moving +45°/s
 5.93 s  door1_panel leaves pendulum1_rod
 5.94 s  door1 is at its largest, 70.0°
 5.94 s  door1 passes 0.30 m from block_support (block_support_box) without touching it: nearest points (2.54, 0.19, 0.20) m and (2.84, 0.19, 0.20) m
 5.94 s  pendulum1 reaches its 38° stop (the end where it sits lower) moving +233°/s
 5.94 s  pendulum1_rod first touches block1_cube
 5.94 s  pendulum1 is at its largest, 38.0°
 5.94 s  block1 starts moving
 5.96 s  pendulum1 passes 0.02 m from block_support (block_support_box) without touching it: nearest points (2.83, 0.10, 0.51) m and (2.84, 0.10, 0.50) m
 5.96 s  pendulum1_rod leaves block1_cube
 5.97 s  block1 comes to rest at (2.90, 0.10, 0.56) m

State every 0.25 s:
0.00 s: ball1 at (-0.16, 0.10, 1.36) m, at rest; touching nothing | lever1 at 0.0°, still; touching nothing | cart1 at 0.000 m, still; touching nothing | domino1 at (0.92, 0.10, 0.43) m, at rest; touching nothing | ball2 at (1.10, 0.10, 0.54) m, at rest; touching ramp1_retaining_lip | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching nothing
0.25 s: ball1 at (-0.16, 0.10, 1.05) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | lever1 at 0.0°, still; touching nothing | cart1 at 0.000 m, still; touching nothing | domino1 at (0.92, 0.10, 0.43) m, at rest; touching domino_support_box | ball2 at (1.10, 0.10, 0.54) m, at rest; touching ramp1_retaining_lip, ramp1_surface | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
0.50 s: ball1 at (-0.06, 0.10, 0.64) m, moving 0.24 m/s (vx -0.13, vy +0.00, vz -0.20); touching lever1_beam | lever1 at 30.0°, turning +167°/s; touching ball1_sphere | cart1 at 0.071 m, moving +0.56 m/s; touching nothing | domino1 at (0.92, 0.10, 0.43) m, at rest; touching domino_support_box | ball2 at (1.10, 0.10, 0.54) m, at rest; touching ramp1_retaining_lip, ramp1_surface | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
0.75 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.204 m, moving +0.51 m/s; touching nothing | domino1 at (0.92, 0.10, 0.43) m, at rest; touching domino_support_box | ball2 at (1.10, 0.10, 0.54) m, at rest; touching ramp1_retaining_lip, ramp1_surface | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
1.00 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.325 m, moving +0.46 m/s; touching nothing | domino1 at (0.92, 0.10, 0.43) m, at rest; touching domino_support_box | ball2 at (1.10, 0.10, 0.54) m, at rest; touching ramp1_retaining_lip, ramp1_surface | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
1.25 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.425 m, moving +0.08 m/s; touching nothing | domino1 at (0.93, 0.10, 0.43) m, moving 0.19 m/s (vx +0.19, vy +0.00, vz +0.04); touching nothing | ball2 at (1.10, 0.10, 0.54) m, at rest; touching ramp1_retaining_lip, ramp1_surface | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
1.50 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.435 m, moving +0.02 m/s; touching nothing | domino1 at (0.95, 0.10, 0.43) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00), turned 11° from how it started; touching domino_support_box | ball2 at (1.10, 0.10, 0.54) m, at rest; touching ramp1_retaining_lip, ramp1_surface | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
1.75 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.439 m, moving +0.02 m/s; touching nothing | domino1 at (0.98, 0.10, 0.43) m, moving 0.22 m/s (vx +0.21, vy +0.00, vz -0.05), turned 24° from how it started; touching domino_support_box | ball2 at (1.10, 0.10, 0.54) m, at rest; touching ramp1_retaining_lip, ramp1_surface | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
2.00 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.442 m, moving +0.01 m/s; touching nothing | domino1 at (0.98, 0.10, 0.43) m, at rest, turned 27° from how it started; touching ball2_sphere, domino_support_box | ball2 at (1.10, 0.10, 0.54) m, at rest; touching domino1_box, ramp1_retaining_lip | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
2.25 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.446 m, moving +0.01 m/s; touching nothing | domino1 at (0.98, 0.10, 0.43) m, at rest, turned 28° from how it started; touching domino_support_box | ball2 at (1.10, 0.10, 0.54) m, at rest; touching ramp1_retaining_lip | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
2.50 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.447 m, still; touching nothing | domino1 at (0.98, 0.10, 0.43) m, at rest, turned 28° from how it started; touching ball2_sphere | ball2 at (1.10, 0.10, 0.54) m, at rest; touching domino1_box, ramp1_retaining_lip | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
2.75 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.446 m, still; touching nothing | domino1 at (0.98, 0.10, 0.43) m, at rest, turned 28° from how it started; touching ball2_sphere, domino_support_box | ball2 at (1.11, 0.10, 0.54) m, at rest; touching domino1_box, ramp1_retaining_lip | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
3.00 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.446 m, still; touching nothing | domino1 at (0.99, 0.10, 0.43) m, at rest, turned 28° from how it started; touching domino_support_box | ball2 at (1.11, 0.10, 0.54) m, at rest; touching ramp1_retaining_lip | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
3.25 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.445 m, still; touching nothing | domino1 at (0.99, 0.10, 0.43) m, at rest, turned 28° from how it started; touching domino_support_box | ball2 at (1.11, 0.10, 0.54) m, at rest; touching ramp1_retaining_lip | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
3.50 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.445 m, still; touching nothing | domino1 at (0.99, 0.10, 0.42) m, at rest, turned 29° from how it started; touching ball2_sphere, domino_support_box | ball2 at (1.11, 0.10, 0.54) m, at rest; touching domino1_box, ramp1_retaining_lip | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
(the same through 3.75 s)
4.00 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.444 m, still; touching nothing | domino1 at (0.99, 0.10, 0.42) m, at rest, turned 29° from how it started; touching ball2_sphere, domino_support_box | ball2 at (1.11, 0.10, 0.54) m, at rest; touching domino1_box, ramp1_retaining_lip | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
4.25 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.444 m, still; touching nothing | domino1 at (0.99, 0.10, 0.42) m, at rest, turned 30° from how it started; touching domino_support_box | ball2 at (1.11, 0.10, 0.54) m, at rest; touching ramp1_retaining_lip | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
4.50 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.444 m, still; touching nothing | domino1 at (1.00, 0.10, 0.42) m, at rest, turned 37° from how it started; touching domino_support_box, ramp1_surface | ball2 at (1.15, 0.10, 0.53) m, moving 0.45 m/s (vx +0.34, vy +0.00, vz -0.29); touching nothing | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
4.75 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.443 m, still; touching nothing | domino1 at (1.00, 0.10, 0.42) m, at rest, turned 37° from how it started; touching domino_support_box, ramp1_surface | ball2 at (1.30, 0.10, 0.47) m, moving 0.91 m/s (vx +0.87, vy +0.00, vz -0.29); touching ramp1_surface | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
5.00 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.443 m, still; touching nothing | domino1 at (1.00, 0.10, 0.42) m, at rest, turned 37° from how it started; touching domino_support_box, ramp1_surface | ball2 at (1.58, 0.10, 0.37) m, moving 1.43 m/s (vx +1.34, vy +0.00, vz -0.50); touching nothing | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
5.25 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.443 m, still; touching nothing | domino1 at (1.00, 0.10, 0.42) m, at rest, turned 37° from how it started; touching domino_support_box, ramp1_surface | ball2 at (1.97, 0.10, 0.22) m, moving 1.93 m/s (vx +1.82, vy +0.00, vz -0.64); touching ramp1_surface | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
5.50 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.443 m, still; touching nothing | domino1 at (1.00, 0.10, 0.42) m, at rest, turned 36° from how it started; touching domino_support_box, ramp1_surface | ball2 at (2.07, 0.10, 0.06) m, moving 1.30 m/s (vx -0.15, vy +0.00, vz -1.29); touching nothing | door1 at 17.3°, turning +114°/s; touching nothing | pendulum1 at 0.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
5.75 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.443 m, still; touching nothing | domino1 at (1.00, 0.10, 0.42) m, at rest, turned 36° from how it started; touching domino_support_box | ball2 at (2.04, 0.10, 0.05) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz +0.00); touching floor | door1 at 61.0°, turning +32°/s; touching nothing | pendulum1 at 3.5°, turning +145°/s; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
6.00 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.443 m, still; touching nothing | domino1 at (1.00, 0.10, 0.42) m, at rest, turned 36° from how it started; touching domino_support_box, ramp1_surface | ball2 at (2.04, 0.10, 0.05) m, at rest; touching floor | door1 at 70.0°, still; touching nothing | pendulum1 at 38.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
6.25 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.442 m, still; touching nothing | domino1 at (1.00, 0.10, 0.42) m, at rest, turned 36° from how it started; touching domino_support_box, ramp1_surface | ball2 at (2.04, 0.10, 0.05) m, at rest; touching floor | door1 at 70.0°, still; touching nothing | pendulum1 at 38.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
(the same through 6.50 s)
6.75 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.442 m, still; touching nothing | domino1 at (1.00, 0.10, 0.42) m, at rest, turned 36° from how it started; touching domino_support_box | ball2 at (2.04, 0.10, 0.05) m, at rest; touching floor | door1 at 70.0°, still; touching nothing | pendulum1 at 38.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
7.00 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.442 m, still; touching nothing | domino1 at (1.01, 0.10, 0.42) m, at rest, turned 36° from how it started; touching ramp1_surface | ball2 at (2.04, 0.10, 0.05) m, at rest; touching floor | door1 at 70.0°, still; touching nothing | pendulum1 at 38.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
7.25 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.442 m, still; touching nothing | domino1 at (1.01, 0.10, 0.42) m, at rest, turned 36° from how it started; touching domino_support_box, ramp1_surface | ball2 at (2.04, 0.10, 0.05) m, at rest; touching floor | door1 at 70.0°, still; touching nothing | pendulum1 at 38.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
(the same through 7.50 s)
7.75 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.442 m, still; touching nothing | domino1 at (1.01, 0.10, 0.42) m, at rest, turned 36° from how it started; touching domino_support_box | ball2 at (2.04, 0.10, 0.05) m, at rest; touching floor | door1 at 70.0°, still; touching nothing | pendulum1 at 38.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
8.00 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.442 m, still; touching nothing | domino1 at (1.01, 0.10, 0.42) m, at rest, turned 36° from how it started; touching domino_support_box, ramp1_surface | ball2 at (2.04, 0.10, 0.05) m, at rest; touching floor | door1 at 70.0°, still; touching nothing | pendulum1 at 38.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
(the same through 8.25 s)
8.50 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.442 m, still; touching nothing | domino1 at (1.01, 0.10, 0.42) m, at rest, turned 35° from how it started; touching domino_support_box | ball2 at (2.04, 0.10, 0.05) m, at rest; touching floor | door1 at 70.0°, still; touching nothing | pendulum1 at 38.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
8.75 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.442 m, still; touching nothing | domino1 at (1.01, 0.10, 0.42) m, at rest, turned 35° from how it started; touching domino_support_box, ramp1_surface | ball2 at (2.04, 0.10, 0.05) m, at rest; touching floor | door1 at 70.0°, still; touching nothing | pendulum1 at 38.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
9.00 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.442 m, still; touching nothing | domino1 at (1.01, 0.10, 0.42) m, at rest, turned 35° from how it started; touching domino_support_box | ball2 at (2.04, 0.10, 0.05) m, at rest; touching floor | door1 at 70.0°, still; touching nothing | pendulum1 at 38.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
9.25 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.442 m, still; touching nothing | domino1 at (1.01, 0.10, 0.42) m, at rest, turned 35° from how it started; touching domino_support_box, ramp1_surface | ball2 at (2.04, 0.10, 0.05) m, at rest; touching floor | door1 at 70.0°, still; touching nothing | pendulum1 at 38.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
(the same through 9.75 s)
10.00 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.442 m, still; touching nothing | domino1 at (1.01, 0.10, 0.42) m, at rest, turned 35° from how it started; touching domino_support_box | ball2 at (2.04, 0.10, 0.05) m, at rest; touching floor | door1 at 70.0°, still; touching nothing | pendulum1 at 38.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
10.25 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.441 m, still; touching nothing | domino1 at (1.01, 0.10, 0.42) m, at rest, turned 35° from how it started; touching domino_support_box | ball2 at (2.04, 0.10, 0.05) m, at rest; touching floor | door1 at 70.0°, still; touching nothing | pendulum1 at 38.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
10.50 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.441 m, still; touching nothing | domino1 at (1.01, 0.10, 0.42) m, at rest, turned 35° from how it started; touching ramp1_surface | ball2 at (2.04, 0.10, 0.05) m, at rest; touching floor | door1 at 70.0°, still; touching nothing | pendulum1 at 38.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
10.75 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.441 m, still; touching nothing | domino1 at (1.01, 0.10, 0.42) m, at rest, turned 35° from how it started; touching domino_support_box, ramp1_surface | ball2 at (2.04, 0.10, 0.05) m, at rest; touching floor | door1 at 70.0°, still; touching nothing | pendulum1 at 38.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
(the same through 11.25 s)
11.50 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.441 m, still; touching nothing | domino1 at (1.01, 0.10, 0.42) m, at rest, turned 34° from how it started; touching domino_support_box | ball2 at (2.04, 0.10, 0.05) m, at rest; touching floor | door1 at 70.0°, still; touching nothing | pendulum1 at 38.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
11.75 s: ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam | lever1 at 45.0°, still; touching ball1_sphere | cart1 at 0.441 m, still; touching nothing | domino1 at (1.01, 0.10, 0.42) m, at rest, turned 34° from how it started; touching domino_support_box, ramp1_surface | ball2 at (2.04, 0.10, 0.05) m, at rest; touching floor | door1 at 70.0°, still; touching nothing | pendulum1 at 38.0°, still; touching nothing | block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box
(the same through 12.00 s)

At the end (12.00 s):
- ball1 at (-0.07, 0.10, 0.62) m, at rest; touching lever1_beam
- lever1 at 45.0°, still; touching ball1_sphere
- cart1 at 0.441 m, still; touching nothing
- domino1 at (1.01, 0.10, 0.42) m, at rest, turned 34° from how it started; touching domino_support_box, ramp1_surface
- ball2 at (2.04, 0.10, 0.05) m, at rest; touching floor
- door1 at 70.0°, still; touching nothing
- pendulum1 at 38.0°, still; touching nothing
- block1 at (2.90, 0.10, 0.56) m, at rest; touching block_support_box

Openings (fixed rings, open through the middle; height is the middle of the whole thing), and each loose thing that comes down through one's height:
ring1: an opening 0.21 m across, centre (-0.16, 0.10, 1.06) m
- ball1 comes down through ring1's height at 0.25 s, 0.00 m from its centre: through it
</history>
