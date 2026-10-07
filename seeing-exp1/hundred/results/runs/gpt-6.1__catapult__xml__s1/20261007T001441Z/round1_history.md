MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_rod, pendulum_bob; starts at 66.4°, still
- cart: slide joint cart_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.32 m as MuJoCo applies it; its geoms: cart_base, cart_mast, cart_ram; starts at 0.000 m, still
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range -29.7938° to 0° as MuJoCo applies it; its geoms: seesaw_beam, seesaw_ball_left_lip, seesaw_ball_right_lip, seesaw_ball_outer_lip, seesaw_ball_inner_lip; starts at 0.0°, still
- weight: free body; its geoms: weight_block; starts at (-0.99, -0.30, 1.11) m, at rest
- ball: free body; its geoms: ball_sphere; starts at (0.70, 0.30, 0.62) m, at rest

What happened, in order:
 0.00 s  weight_block starts touching weight_shelf_deck
 0.00 s  seesaw_beam starts touching ball_sphere
 0.00 s  pendulum is at its largest at the start, 66.4°
 0.00 s  cart starts at its lower stop (0 m)
 0.00 s  seesaw starts at its upper stop (0°)
 0.55 s  pendulum_bob first touches cart_ram
 0.57 s  weight_block leaves weight_shelf_deck
 0.57 s  cart_ram first touches weight_block
 0.57 s  weight starts moving
 0.58 s  pendulum_bob leaves cart_ram
 0.58 s  cart_ram leaves weight_block
 0.63 s  weight is at the top of its flight, at (-0.88, -0.30, 1.13) m
 0.77 s  weight_block first touches weight_chute_front
 0.77 s  cart reaches its upper stop (0.32 m) moving +1.13 m/s
 0.77 s  cart is at its largest, 0.3 m
 0.78 s  weight_block leaves weight_chute_front
 0.79 s  cart passes 0.05 m from weight_chute (weight_chute_outer_side) without touching it: nearest points (-0.87, -0.37, 1.07) m and (-0.87, -0.42, 1.07) m
 0.86 s  pendulum_bob touches cart_ram again
 0.87 s  pendulum_bob leaves cart_ram
 0.88 s  cart reaches its upper stop (0.32 m) again moving +0.44 m/s
 0.91 s  pendulum_bob touches cart_ram again
 0.92 s  pendulum passes 0.23 m from weight_shelf (weight_shelf_deck) without touching it: nearest points (-1.37, -0.30, 1.13) m and (-1.17, -0.30, 1.03) m
 0.92 s  cart passes 0.39 m from seesaw_lower_stop (seesaw_lower_stop_block) without touching it: nearest points (-1.16, -0.24, 0.09) m and (-0.77, -0.24, 0.09) m
 0.92 s  pendulum passes 0.45 m from weight_chute (weight_chute_outer_side) without touching it: nearest points (-1.36, -0.33, 1.18) m and (-0.93, -0.42, 1.12) m
 0.92 s  pendulum is at its smallest, -18.7°
 0.93 s  pendulum_bob leaves cart_ram
 1.05 s  seesaw_beam first touches weight_block
 1.05 s  ball starts moving
 1.07 s  seesaw_ball_right_lip first touches ball_sphere
 1.09 s  seesaw_beam leaves weight_block
 1.10 s  seesaw_beam leaves ball_sphere
 1.12 s  cart passes 0.42 m from seesaw (seesaw_beam) without touching it: nearest points (-1.16, -0.25, 0.17) m and (-0.76, -0.25, 0.31) m
 1.16 s  seesaw_beam touches ball_sphere again
 1.17 s  seesaw_beam touches weight_block again
 1.18 s  seesaw is at its smallest, -28.9°
 1.18 s  seesaw_beam leaves ball_sphere
 1.18 s  seesaw_beam first touches seesaw_lower_stop_block
 1.18 s  weight_block first touches seesaw_lower_stop_block
 1.18 s  seesaw_beam leaves weight_block
 1.18 s  seesaw_ball_left_lip first touches ball_sphere
 1.19 s  weight_block leaves seesaw_lower_stop_block
 1.19 s  seesaw_ball_left_lip leaves ball_sphere
 1.20 s  seesaw_ball_right_lip leaves ball_sphere
 1.21 s  seesaw_beam leaves seesaw_lower_stop_block
 1.22 s  weight is at the top of its flight, at (-0.78, -0.30, 0.26) m
 1.23 s  seesaw_ball_left_lip touches ball_sphere again
 1.23 s  ball passes 0.10 m from cup (cup_right_wall) without touching it: nearest points (0.50, 0.30, 0.98) m and (0.41, 0.30, 0.98) m
 1.31 s  seesaw_ball_left_lip leaves ball_sphere
 1.34 s  seesaw_ball_left_lip touches ball_sphere again
 1.34 s  seesaw_ball_left_lip leaves ball_sphere
 1.39 s  seesaw_beam touches ball_sphere again
 1.40 s  seesaw_ball_left_lip touches ball_sphere again
 1.41 s  weight_block first touches floor
 1.46 s  weight comes to rest at (-0.91, -0.30, 0.08) m
 1.53 s  seesaw_ball_left_lip leaves ball_sphere
 1.66 s  seesaw reaches its upper stop (0°) again moving +132°/s
 1.67 s  seesaw is at its largest, 0.1°
 1.68 s  ball comes to rest at (0.70, 0.30, 0.62) m
 2.89 s  pendulum_bob touches cart_ram again
 2.90 s  pendulum_bob leaves cart_ram
 2.90 s  cart reaches its upper stop (0.32 m) again moving +0.13 m/s
 3.43 s  pendulum passes 0.22 m from cup (cup_left_wall) without touching it: nearest points (-1.81, -0.17, 1.12) m and (-1.81, 0.04, 1.08) m

State every 0.25 s:
0.00 s: pendulum at 66.4°, still; touching nothing | cart at 0.000 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.99, -0.30, 1.11) m, at rest; touching weight_shelf_deck | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
0.25 s: pendulum at 50.6°, turning -122°/s; touching nothing | cart at 0.000 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.99, -0.30, 1.11) m, at rest; touching weight_shelf_deck | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
0.50 s: pendulum at 9.2°, turning -194°/s; touching nothing | cart at 0.000 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-1.00, -0.30, 1.11) m, at rest; touching weight_shelf_deck | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
0.75 s: pendulum at -13.4°, turning -49°/s; touching nothing | cart at 0.297 m, moving +1.16 m/s; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.64, -0.30, 1.06) m, moving 2.29 m/s (vx +1.94, vy +0.00, vz -1.20); touching nothing | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
1.00 s: pendulum at -18.1°, turning +14°/s; touching nothing | cart at 0.319 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.69, -0.30, 0.77) m, moving 2.32 m/s (vx -0.36, vy +0.00, vz -2.29); touching nothing | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
1.25 s: pendulum at -9.7°, turning +49°/s; touching nothing | cart at 0.317 m, still; touching nothing | seesaw at -28.5°, turning +5°/s; touching ball_sphere | weight at (-0.80, -0.30, 0.26) m, moving 0.74 m/s (vx -0.68, vy +0.00, vz -0.29), turned 49° from how it started; touching nothing | ball at (0.56, 0.30, 0.98) m, moving 0.13 m/s (vx +0.08, vy +0.00, vz -0.10); touching seesaw_ball_left_lip
1.50 s: pendulum at 4.3°, turning +57°/s; touching nothing | cart at 0.316 m, still; touching nothing | seesaw at -18.1°, turning +82°/s; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.64, 0.30, 0.84) m, moving 1.00 m/s (vx +0.41, vy +0.00, vz -0.92); touching seesaw_beam
1.75 s: pendulum at 15.8°, turning +31°/s; touching nothing | cart at 0.316 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
2.00 s: pendulum at 18.2°, turning -12°/s; touching nothing | cart at 0.315 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
2.25 s: pendulum at 10.2°, turning -48°/s; touching nothing | cart at 0.315 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
2.50 s: pendulum at -3.7°, turning -57°/s; touching nothing | cart at 0.315 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
2.75 s: pendulum at -15.4°, turning -32°/s; touching nothing | cart at 0.315 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
3.00 s: pendulum at -17.9°, turning +13°/s; touching nothing | cart at 0.320 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
3.25 s: pendulum at -9.8°, turning +49°/s; touching nothing | cart at 0.319 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
3.50 s: pendulum at 4.0°, turning +56°/s; touching nothing | cart at 0.318 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
3.75 s: pendulum at 15.5°, turning +31°/s; touching nothing | cart at 0.318 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
4.00 s: pendulum at 18.0°, turning -11°/s; touching nothing | cart at 0.318 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
4.25 s: pendulum at 10.3°, turning -47°/s; touching nothing | cart at 0.317 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
4.50 s: pendulum at -3.4°, turning -56°/s; touching nothing | cart at 0.317 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
4.75 s: pendulum at -15.1°, turning -33°/s; touching nothing | cart at 0.317 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
5.00 s: pendulum at -18.1°, turning +10°/s; touching nothing | cart at 0.317 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
5.25 s: pendulum at -10.7°, turning +46°/s; touching nothing | cart at 0.317 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
5.50 s: pendulum at 2.8°, turning +56°/s; touching nothing | cart at 0.317 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
5.75 s: pendulum at 14.7°, turning +34°/s; touching nothing | cart at 0.317 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
6.00 s: pendulum at 18.1°, turning -8°/s; touching nothing | cart at 0.317 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam

At the end (6.00 s):
- pendulum at 18.1°, turning -8°/s; touching nothing
- cart at 0.317 m, still; touching nothing
- seesaw at 0.0°, still; touching ball_sphere
- weight at (-0.91, -0.30, 0.08) m, at rest, turned 90° from how it started; touching floor
- ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
</history>
