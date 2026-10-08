MuJoCo ran your scene for 12 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 12.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_sphere; starts at (-0.88, 0.00, 0.52) m, at rest
- domino1: free body; its geoms: domino1_box; starts at (0.14, 0.00, 0.12) m, at rest
- domino2: free body; its geoms: domino2_box; starts at (0.32, 0.00, 0.12) m, at rest
- flap1: hinge joint flap1_hinge about axis (0.00, 1.00, 0.00), range 0° to 65° as MuJoCo applies it; its geoms: flap1_panel; starts at 0.0°, still
- cart1: slide joint cart1_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.6 m as MuJoCo applies it; its geoms: cart1_box, cart1_striker_extension; starts at 0.000 m, still
- ball2: free body; its geoms: ball2_sphere; starts at (1.55, 0.00, 0.53) m, at rest
- lever1: hinge joint lever1_hinge about axis (0.00, -1.00, 0.00), range 0° to 45° as MuJoCo applies it; its geoms: lever1_bar, lever1_left_trigger; starts at 0.0°, still
- ball3: free body; its geoms: ball3_sphere; starts at (3.14, 0.00, 0.92) m, at rest
- pendulum1: hinge joint pendulum1_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum1_left_rod, pendulum1_right_rod, pendulum1_left_bridge, pendulum1_right_bridge, pendulum1_bob; starts at 0.0°, still

What happened, in order:
 0.00 s  ball2_sphere starts touching ramp2_start_shelf
 0.00 s  domino1_box starts touching floor
 0.00 s  domino2_box starts touching floor
 0.00 s  flap1 starts at its 0° stop (the end where it sits higher)
 0.00 s  cart1 starts at its lower stop (0 m)
 0.00 s  lever1 starts at its 0° stop (the end where it sits higher)
 0.00 s  ball1_sphere first touches ramp1_surface
 0.00 s  lever1_bar first touches ball3_sphere
 0.01 s  lever1 is at its smallest, -0.0°
 0.02 s  ball1 starts moving
 0.89 s  ball1_sphere leaves ramp1_surface
 0.91 s  ball1_sphere first touches domino1_box
 0.91 s  domino1 starts moving
 0.91 s  ball1_sphere leaves domino1_box
 0.99 s  domino1_box first touches domino2_box
 0.99 s  domino2 starts moving
 0.99 s  ball1_sphere touches domino1_box again
 0.99 s  ball1 passes 0.12 m from domino2 (domino2_box) without touching it: nearest points (0.16, 0.00, 0.15) m and (0.28, 0.00, 0.15) m
 0.99 s  domino1_box leaves floor
 0.99 s  domino1_box leaves domino2_box
 1.00 s  ball1_sphere leaves domino1_box
 1.03 s  domino1_box touches floor again
 1.05 s  ball1_sphere touches domino1_box again
 1.05 s  ball1 passes 0.34 m from flap1 (flap1_panel) without touching it: nearest points (0.16, 0.00, 0.11) m and (0.50, 0.00, 0.11) m
 1.08 s  domino1_box touches domino2_box again
 1.08 s  domino1_box leaves domino2_box
 1.11 s  ball1_sphere leaves domino1_box
 1.13 s  domino1_box touches domino2_box again
 1.13 s  domino1_box leaves domino2_box
 1.14 s  ball1_sphere first touches floor
 1.17 s  domino2_box first touches flap1_panel
 1.17 s  domino1 passes 0.12 m from flap1 (flap1_panel) without touching it: nearest points (0.38, 0.00, 0.16) m and (0.50, 0.00, 0.16) m
 1.17 s  domino1_box touches domino2_box again
 1.18 s  domino2_box leaves flap1_panel
 1.25 s  domino2_box touches flap1_panel again
 1.43 s  flap1 passes 0.19 m from cart_rails (cart_rails_left) without touching it: nearest points (0.78, -0.07, 0.33) m and (0.90, -0.07, 0.48) m
 1.47 s  domino1 passes 0.41 m from cart1 (cart1_striker_extension) without touching it: nearest points (0.42, 0.00, 0.13) m and (0.83, 0.00, 0.15) m
 1.48 s  flap1_panel first touches cart1_striker_extension
 1.48 s  domino1 comes to rest at (0.29, 0.00, 0.10) m
 1.48 s  domino2 passes 0.26 m from cart1 (cart1_striker_extension) without touching it: nearest points (0.58, 0.00, 0.10) m and (0.83, 0.00, 0.15) m
 1.49 s  flap1_panel leaves cart1_striker_extension
 1.55 s  flap1_panel touches cart1_striker_extension again
 1.56 s  flap1_panel leaves cart1_striker_extension
 1.57 s  domino2 passes 0.47 m from cart_rails (cart_rails_left) without touching it: nearest points (0.55, -0.02, 0.17) m and (0.89, -0.07, 0.48) m
 1.63 s  flap1_panel touches cart1_striker_extension again
 1.63 s  flap1_panel leaves cart1_striker_extension
 1.64 s  flap1 reaches its 65° stop (the end where it sits lower) moving +125°/s
 1.65 s  flap1 is at its largest, 65.1°
 1.65 s  domino2 comes to rest at (0.46, 0.00, 0.08) m
 2.54 s  cart1 passes 0.01 m from ramp2 (ramp2_surface) without touching it: nearest points (1.49, 0.09, 0.50) m and (1.49, 0.09, 0.49) m
 2.58 s  cart1_box first touches ball2_sphere
 2.58 s  ball2 starts moving
 2.59 s  cart1_box leaves ball2_sphere
 2.61 s  ball1_sphere leaves floor
 2.61 s  ball1_sphere first touches catch_fence_left
 2.62 s  ball1_sphere leaves catch_fence_left
 2.65 s  ball1_sphere touches floor again
 2.65 s  ball1 comes to rest at (-0.98, 0.00, 0.05) m
 2.74 s  cart1_box touches ball2_sphere again
 2.74 s  cart1_box leaves ball2_sphere
 2.92 s  ball2_sphere leaves ramp2_start_shelf
 2.95 s  ball2_sphere first touches ramp2_surface
 3.63 s  ball2_sphere leaves ramp2_surface
 3.66 s  ball2_sphere first touches lever1_left_trigger
 3.66 s  ball3 starts moving
 3.67 s  ball2_sphere leaves lever1_left_trigger
 3.71 s  lever1_bar leaves ball3_sphere
 3.71 s  ball3_sphere first touches launch_guide_left
 3.71 s  ball3_sphere leaves launch_guide_left
 3.74 s  ball3_sphere first touches launch_guide_right
 3.75 s  lever1_bar touches ball3_sphere again
 3.75 s  ball3_sphere leaves launch_guide_right
 3.77 s  ball2_sphere first touches floor
 3.78 s  ball2_sphere leaves floor
 3.81 s  ball3_sphere touches launch_guide_left again
 3.81 s  ball3_sphere leaves launch_guide_left
 3.82 s  ball2_sphere touches floor again
 3.86 s  ball2_sphere touches lever1_left_trigger again
 3.86 s  ball2_sphere leaves lever1_left_trigger
 3.88 s  ball3_sphere touches launch_guide_right again
 3.90 s  ball2_sphere touches lever1_left_trigger again
 3.93 s  ball2_sphere leaves lever1_left_trigger
 4.06 s  ball3_sphere leaves launch_guide_right
 4.09 s  ball3_sphere touches launch_guide_right again
 4.15 s  ball3_sphere leaves launch_guide_right
 4.15 s  lever1_bar leaves ball3_sphere
 4.16 s  ball3 is at the top of its flight, at (3.14, 0.00, 1.04) m
 4.21 s  lever1 reaches its 45° stop (the end where it sits lower) moving +153°/s
 4.21 s  lever1 is at its largest, 45.0°
 4.29 s  ball3_sphere touches launch_guide_left again
 4.29 s  ball3_sphere leaves launch_guide_left
 4.32 s  ball3_sphere touches launch_guide_right again
 4.32 s  ball3_sphere leaves launch_guide_right
 4.34 s  ball3_sphere touches launch_guide_left again
 4.34 s  ball3_sphere leaves launch_guide_left
 4.49 s  cart1 reaches its upper stop (0.6 m) moving +0.05 m/s
 4.51 s  ball3 passes 0.01 m from ring1 (ring1_segment01) without touching it: nearest points (3.21, 0.01, 0.57) m and (3.22, 0.01, 0.57) m
 4.51 s  ball2 passes 0.46 m from ring1 (ring1_segment08) without touching it: nearest points (3.05, 0.00, 0.10) m and (3.05, 0.00, 0.56) m
 4.59 s  ball3_sphere first touches pendulum1_bob
 4.60 s  ball3_sphere leaves pendulum1_bob
 4.60 s  cart1 is at its largest, 0.6 m
 4.69 s  ball3 is at the top of its flight, at (3.22, 0.00, 0.36) m
 4.76 s  ball2 passes 0.09 m from pendulum1 (pendulum1_bob) without touching it: nearest points (3.14, 0.00, 0.10) m and (3.14, 0.00, 0.19) m
 4.88 s  lever1_left_trigger first touches pendulum1_bob
 4.90 s  pendulum1 is at its largest, 4.1°
 4.93 s  lever1_left_trigger leaves pendulum1_bob
 4.94 s  ball3_sphere first touches floor
 4.95 s  ball3_sphere leaves floor
 5.00 s  ball3_sphere touches floor again
 5.60 s  pendulum1 is at its smallest, -3.5°
 5.84 s  ball3_sphere first touches catch_fence_right
 5.85 s  ball3_sphere leaves catch_fence_right
 5.86 s  ball3 comes to rest at (3.68, 0.00, 0.05) m
 6.82 s  ball2 comes to rest at (3.54, 0.00, 0.05) m
12.00 s  ball2 passes 0.13 m from catch_fence (catch_fence_right) without touching it: nearest points (3.60, 0.00, 0.05) m and (3.73, 0.00, 0.05) m
12.00 s  ball2 passes 0.02 m from ball3 (ball3_sphere) without touching it: nearest points (3.60, 0.00, 0.05) m and (3.62, 0.00, 0.05) m

State every 0.25 s:
0.00 s: ball1 at (-0.88, 0.00, 0.52) m, at rest; touching nothing | domino1 at (0.14, 0.00, 0.12) m, at rest; touching floor | domino2 at (0.32, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | cart1 at 0.000 m, still; touching nothing | ball2 at (1.55, 0.00, 0.53) m, at rest; touching ramp2_start_shelf | lever1 at 0.0°, still; touching nothing | ball3 at (3.14, 0.00, 0.92) m, at rest; touching nothing | pendulum1 at 0.0°, still; touching nothing
0.25 s: ball1 at (-0.81, 0.00, 0.50) m, moving 0.60 m/s (vx +0.56, vy +0.00, vz -0.20); touching ramp1_surface | domino1 at (0.14, 0.00, 0.12) m, at rest; touching floor | domino2 at (0.32, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | cart1 at 0.000 m, still; touching nothing | ball2 at (1.55, 0.00, 0.52) m, at rest; touching ramp2_start_shelf | lever1 at -0.0°, still; touching ball3_sphere | ball3 at (3.14, 0.00, 0.92) m, at rest; touching lever1_bar | pendulum1 at 0.0°, still; touching nothing
0.50 s: ball1 at (-0.60, 0.00, 0.42) m, moving 1.20 m/s (vx +1.13, vy +0.00, vz -0.41); touching ramp1_surface | domino1 at (0.14, 0.00, 0.12) m, at rest; touching floor | domino2 at (0.32, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | cart1 at 0.000 m, still; touching nothing | ball2 at (1.55, 0.00, 0.52) m, at rest; touching ramp2_start_shelf | lever1 at -0.0°, still; touching ball3_sphere | ball3 at (3.14, 0.00, 0.92) m, at rest; touching lever1_bar | pendulum1 at 0.0°, still; touching nothing
0.75 s: ball1 at (-0.24, 0.00, 0.29) m, moving 1.80 m/s (vx +1.69, vy +0.00, vz -0.61); touching ramp1_surface | domino1 at (0.14, 0.00, 0.12) m, at rest; touching floor | domino2 at (0.32, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | cart1 at 0.000 m, still; touching nothing | ball2 at (1.55, 0.00, 0.52) m, at rest; touching ramp2_start_shelf | lever1 at -0.0°, still; touching ball3_sphere | ball3 at (3.14, 0.00, 0.92) m, at rest; touching lever1_bar | pendulum1 at 0.0°, still; touching nothing
1.00 s: ball1 at (0.11, 0.00, 0.15) m, moving 0.39 m/s (vx +0.07, vy -0.00, vz -0.38); touching nothing | domino1 at (0.20, 0.00, 0.13) m, moving 0.44 m/s (vx +0.43, vy -0.00, vz +0.10), turned 25° from how it started; touching nothing | domino2 at (0.33, 0.00, 0.12) m, moving 0.44 m/s (vx +0.43, vy -0.00, vz +0.12), turned 3° from how it started; touching floor | flap1 at 0.0°, still; touching nothing | cart1 at 0.000 m, still; touching nothing | ball2 at (1.55, 0.00, 0.52) m, at rest; touching ramp2_start_shelf | lever1 at -0.0°, still; touching ball3_sphere | ball3 at (3.14, 0.00, 0.92) m, at rest; touching lever1_bar | pendulum1 at 0.0°, still; touching nothing
1.25 s: ball1 at (0.00, 0.00, 0.05) m, moving 0.72 m/s (vx -0.72, vy -0.00, vz -0.00); touching floor | domino1 at (0.27, 0.00, 0.11) m, moving 0.16 m/s (vx +0.14, vy -0.00, vz -0.08), turned 51° from how it started; touching floor | domino2 at (0.41, 0.00, 0.12) m, moving 0.30 m/s (vx +0.27, vy -0.00, vz -0.12), turned 42° from how it started; touching floor | flap1 at 8.5°, turning +101°/s; touching nothing | cart1 at 0.000 m, still; touching nothing | ball2 at (1.55, 0.00, 0.52) m, at rest; touching ramp2_start_shelf | lever1 at -0.0°, still; touching ball3_sphere | ball3 at (3.14, 0.00, 0.92) m, at rest; touching lever1_bar | pendulum1 at 0.0°, still; touching nothing
1.50 s: ball1 at (-0.18, 0.00, 0.05) m, moving 0.72 m/s (vx -0.72, vy -0.00, vz +0.00); touching floor | domino1 at (0.29, 0.00, 0.10) m, at rest, turned 58° from how it started; touching floor | domino2 at (0.45, 0.00, 0.09) m, moving 0.05 m/s (vx +0.04, vy -0.00, vz -0.04), turned 65° from how it started; touching floor | flap1 at 49.0°, turning +48°/s; touching nothing | cart1 at 0.007 m, moving +0.32 m/s; touching nothing | ball2 at (1.55, 0.00, 0.52) m, at rest; touching ramp2_start_shelf | lever1 at -0.0°, still; touching ball3_sphere | ball3 at (3.14, 0.00, 0.92) m, at rest; touching lever1_bar | pendulum1 at 0.0°, still; touching nothing
1.75 s: ball1 at (-0.36, 0.00, 0.05) m, moving 0.72 m/s (vx -0.72, vy -0.00, vz +0.00); touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.114 m, moving +0.48 m/s; touching nothing | ball2 at (1.55, 0.00, 0.52) m, at rest; touching ramp2_start_shelf | lever1 at -0.0°, still; touching ball3_sphere | ball3 at (3.14, 0.00, 0.92) m, at rest; touching lever1_bar | pendulum1 at 0.0°, still; touching nothing
2.00 s: ball1 at (-0.54, 0.00, 0.05) m, moving 0.72 m/s (vx -0.72, vy -0.00, vz +0.00); touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.227 m, moving +0.43 m/s; touching nothing | ball2 at (1.55, 0.00, 0.52) m, at rest; touching ramp2_start_shelf | lever1 at -0.0°, still; touching ball3_sphere | ball3 at (3.14, 0.00, 0.92) m, at rest; touching lever1_bar | pendulum1 at 0.0°, still; touching nothing
2.25 s: ball1 at (-0.72, 0.00, 0.05) m, moving 0.72 m/s (vx -0.72, vy -0.00, vz +0.00); touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.329 m, moving +0.39 m/s; touching nothing | ball2 at (1.55, 0.00, 0.52) m, at rest; touching ramp2_start_shelf | lever1 at -0.0°, still; touching ball3_sphere | ball3 at (3.14, 0.00, 0.92) m, at rest; touching lever1_bar | pendulum1 at 0.0°, still; touching nothing
2.50 s: ball1 at (-0.90, 0.00, 0.05) m, moving 0.72 m/s (vx -0.72, vy -0.00, vz +0.00); touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.422 m, moving +0.35 m/s; touching nothing | ball2 at (1.55, 0.00, 0.52) m, at rest; touching ramp2_start_shelf | lever1 at -0.0°, still; touching ball3_sphere | ball3 at (3.14, 0.00, 0.92) m, at rest; touching lever1_bar | pendulum1 at 0.0°, still; touching nothing
2.75 s: ball1 at (-0.98, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.473 m, moving +0.10 m/s; touching nothing | ball2 at (1.57, 0.00, 0.52) m, moving 0.14 m/s (vx +0.14, vy +0.00, vz +0.01); touching ramp2_start_shelf | lever1 at -0.0°, still; touching ball3_sphere | ball3 at (3.14, 0.00, 0.92) m, at rest; touching lever1_bar | pendulum1 at 0.0°, still; touching nothing
3.00 s: ball1 at (-0.97, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.497 m, moving +0.09 m/s; touching nothing | ball2 at (1.65, 0.00, 0.49) m, moving 0.61 m/s (vx +0.58, vy +0.00, vz -0.21); touching ramp2_surface | lever1 at -0.0°, still; touching ball3_sphere | ball3 at (3.14, 0.00, 0.92) m, at rest; touching lever1_bar | pendulum1 at 0.0°, still; touching nothing
3.25 s: ball1 at (-0.97, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.517 m, moving +0.08 m/s; touching nothing | ball2 at (1.86, 0.00, 0.41) m, moving 1.18 m/s (vx +1.11, vy +0.00, vz -0.41); touching nothing | lever1 at -0.0°, still; touching ball3_sphere | ball3 at (3.14, 0.00, 0.92) m, at rest; touching lever1_bar | pendulum1 at 0.0°, still; touching nothing
3.50 s: ball1 at (-0.97, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.536 m, moving +0.07 m/s; touching nothing | ball2 at (2.20, 0.00, 0.29) m, moving 1.75 m/s (vx +1.65, vy +0.00, vz -0.59); touching ramp2_surface | lever1 at -0.0°, still; touching ball3_sphere | ball3 at (3.14, 0.00, 0.92) m, at rest; touching lever1_bar | pendulum1 at 0.0°, still; touching nothing
3.75 s: ball1 at (-0.97, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.553 m, moving +0.06 m/s; touching nothing | ball2 at (2.61, 0.00, 0.09) m, moving 1.97 m/s (vx +1.35, vy +0.00, vz -1.44); touching nothing | lever1 at 11.6°, turning +79°/s; touching ball3_sphere | ball3 at (3.14, 0.00, 0.98) m, moving 0.38 m/s (vx -0.13, vy +0.00, vz +0.35); touching launch_guide_right, lever1_bar | pendulum1 at 0.0°, still; touching nothing
4.00 s: ball1 at (-0.96, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.569 m, moving +0.06 m/s; touching nothing | ball2 at (2.84, 0.00, 0.05) m, moving 0.45 m/s (vx +0.45, vy +0.00, vz -0.01); touching nothing | lever1 at 25.3°, turning +41°/s; touching ball3_sphere | ball3 at (3.14, 0.00, 1.04) m, moving 0.12 m/s (vx -0.00, vy +0.00, vz +0.12); touching launch_guide_right, lever1_bar | pendulum1 at 0.0°, still; touching nothing
4.25 s: ball1 at (-0.96, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.583 m, moving +0.05 m/s; touching nothing | ball2 at (2.95, 0.00, 0.05) m, moving 0.41 m/s (vx +0.41, vy +0.00, vz +0.00); touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.14, 0.00, 1.00) m, moving 0.89 m/s (vx -0.03, vy +0.00, vz -0.89); touching nothing | pendulum1 at 0.0°, still; touching nothing
4.50 s: ball1 at (-0.96, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.595 m, moving +0.05 m/s; touching nothing | ball2 at (3.04, 0.00, 0.05) m, moving 0.38 m/s (vx +0.38, vy +0.00, vz +0.01); touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.16, 0.00, 0.60) m, moving 2.67 m/s (vx +0.15, vy +0.00, vz -2.67); touching nothing | pendulum1 at 0.0°, still; touching nothing
4.75 s: ball1 at (-0.96, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.600 m, still; touching nothing | ball2 at (3.13, 0.00, 0.05) m, moving 0.34 m/s (vx +0.34, vy +0.00, vz +0.01); touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.24, 0.00, 0.34) m, moving 0.75 m/s (vx +0.44, vy +0.00, vz -0.61); touching nothing | pendulum1 at 2.9°, turning +14°/s; touching nothing
5.00 s: ball1 at (-0.95, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.599 m, still; touching nothing | ball2 at (3.21, 0.00, 0.05) m, moving 0.31 m/s (vx +0.31, vy +0.00, vz -0.00); touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.35, 0.00, 0.05) m, moving 0.45 m/s (vx +0.45, vy +0.00, vz -0.06); touching floor | pendulum1 at 3.7°, turning -8°/s; touching nothing
5.25 s: ball1 at (-0.95, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.599 m, still; touching nothing | ball2 at (3.29, 0.00, 0.05) m, moving 0.27 m/s (vx +0.27, vy +0.00, vz -0.00); touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.46, 0.00, 0.05) m, moving 0.41 m/s (vx +0.41, vy +0.00, vz +0.00); touching floor | pendulum1 at 0.2°, turning -17°/s; touching nothing
5.50 s: ball1 at (-0.95, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.599 m, still; touching nothing | ball2 at (3.35, 0.00, 0.05) m, moving 0.24 m/s (vx +0.24, vy +0.00, vz -0.02); touching nothing | lever1 at 45.0°, still; touching nothing | ball3 at (3.56, 0.00, 0.05) m, moving 0.38 m/s (vx +0.38, vy +0.00, vz +0.01); touching floor | pendulum1 at -3.1°, turning -7°/s; touching nothing
5.75 s: ball1 at (-0.95, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.599 m, still; touching nothing | ball2 at (3.40, 0.00, 0.05) m, moving 0.20 m/s (vx +0.20, vy +0.00, vz +0.00); touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.65, 0.00, 0.05) m, moving 0.34 m/s (vx +0.34, vy +0.00, vz +0.00); touching floor | pendulum1 at -2.7°, turning +9°/s; touching nothing
6.00 s: ball1 at (-0.94, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.598 m, still; touching nothing | ball2 at (3.45, 0.00, 0.05) m, moving 0.16 m/s (vx +0.16, vy +0.00, vz -0.00); touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.68, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 0.5°, turning +14°/s; touching nothing
6.25 s: ball1 at (-0.94, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.598 m, still; touching nothing | ball2 at (3.49, 0.00, 0.05) m, moving 0.13 m/s (vx +0.13, vy +0.00, vz -0.02); touching nothing | lever1 at 45.0°, still; touching nothing | ball3 at (3.68, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 2.8°, turning +3°/s; touching nothing
6.50 s: ball1 at (-0.94, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.598 m, still; touching nothing | ball2 at (3.51, 0.00, 0.05) m, moving 0.09 m/s (vx +0.09, vy +0.00, vz -0.00); touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 1.9°, turning -9°/s; touching nothing
6.75 s: ball1 at (-0.94, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.598 m, still; touching nothing | ball2 at (3.53, 0.00, 0.05) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz -0.00); touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at -0.9°, turning -11°/s; touching nothing
7.00 s: ball1 at (-0.93, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.598 m, still; touching nothing | ball2 at (3.54, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at -2.5°, still; touching nothing
7.25 s: ball1 at (-0.93, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.598 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at -1.3°, turning +9°/s; touching nothing
7.50 s: ball1 at (-0.93, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.597 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 1.1°, turning +8°/s; touching nothing
7.75 s: ball1 at (-0.93, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.597 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 2.1°, turning -1°/s; touching nothing
8.00 s: ball1 at (-0.92, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.597 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 0.7°, turning -8°/s; touching nothing
8.25 s: ball1 at (-0.92, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.597 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at -1.2°, turning -6°/s; touching nothing
8.50 s: ball1 at (-0.92, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.597 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at -1.7°, turning +2°/s; touching nothing
8.75 s: ball1 at (-0.92, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.597 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at -0.3°, turning +7°/s; touching nothing
9.00 s: ball1 at (-0.91, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.597 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 1.2°, turning +4°/s; touching nothing
9.25 s: ball1 at (-0.91, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.597 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 1.3°, turning -3°/s; touching nothing
9.50 s: ball1 at (-0.91, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.597 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at -0.0°, turning -6°/s; touching nothing
9.75 s: ball1 at (-0.91, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.597 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at -1.1°, turning -2°/s; touching nothing
10.00 s: ball1 at (-0.90, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.597 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at -0.9°, turning +3°/s; touching nothing
10.25 s: ball1 at (-0.90, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.597 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 0.2°, turning +5°/s; touching nothing
10.50 s: ball1 at (-0.90, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.597 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 1.0°, still; touching nothing
10.75 s: ball1 at (-0.90, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.597 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 0.7°, turning -4°/s; touching nothing
11.00 s: ball1 at (-0.89, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.597 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at -0.4°, turning -4°/s; touching nothing
11.25 s: ball1 at (-0.89, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.597 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at -0.9°, still; touching nothing
11.50 s: ball1 at (-0.89, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.596 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at -0.4°, turning +3°/s; touching nothing
11.75 s: ball1 at (-0.89, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.596 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 0.4°, turning +3°/s; touching nothing
12.00 s: ball1 at (-0.88, 0.00, 0.05) m, at rest; touching floor | domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor | domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor | flap1 at 65.0°, still; touching domino2_box | cart1 at 0.596 m, still; touching nothing | ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor | lever1 at 45.0°, still; touching nothing | ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor | pendulum1 at 0.7°, still; touching nothing

At the end (12.00 s):
- ball1 at (-0.88, 0.00, 0.05) m, at rest; touching floor
- domino1 at (0.30, 0.00, 0.10) m, at rest, turned 58° from how it started; touching domino2_box, floor
- domino2 at (0.46, 0.00, 0.08) m, at rest, turned 71° from how it started; touching domino1_box, flap1_panel, floor
- flap1 at 65.0°, still; touching domino2_box
- cart1 at 0.596 m, still; touching nothing
- ball2 at (3.55, 0.00, 0.05) m, at rest; touching floor
- lever1 at 45.0°, still; touching nothing
- ball3 at (3.67, 0.00, 0.05) m, at rest; touching floor
- pendulum1 at 0.7°, still; touching nothing

Openings (fixed rings, open through the middle; height is the middle of the whole thing), and each loose thing that comes down through one's height:
launch_guide: an opening 0.14 m across, centre (3.14, 0.00, 1.27) m
- nothing loose comes down through launch_guide's height
ring1: an opening 0.20 m across, centre (3.14, 0.00, 0.57) m
- ball3 comes down through ring1's height at 4.51 s, 0.02 m from its centre: through it
catch_fence: an opening 0.47 m across, centre (1.35, 0.00, 0.10) m
- ball1 comes down through catch_fence's height at 1.07 s, 1.24 m from its centre: outside it, missing by 1.00 m
- domino1 comes down through catch_fence's height at 1.37 s, 1.07 m from its centre: outside it, missing by 0.83 m
- domino2 comes down through catch_fence's height at 1.40 s, 0.91 m from its centre: outside it, missing by 0.68 m
- ball2 comes down through catch_fence's height at 3.74 s, 1.25 m from its centre: outside it, missing by 1.01 m
- ball3 comes down through catch_fence's height at 4.92 s, 1.97 m from its centre: outside it, missing by 1.73 m
</history>
