MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_rod, pendulum_bob; starts at 66.4°, still
- cart: slide joint cart_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.32 m as MuJoCo applies it; its geoms: cart_base, cart_mast, cart_ram; starts at 0.000 m, still
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range -29.7938° to 0° as MuJoCo applies it; its geoms: seesaw_beam, seesaw_weight_end_lip, seesaw_ball_right_lip, seesaw_ball_outer_lip, seesaw_ball_inner_lip; starts at 0.0°, still
- weight: free body; its geoms: weight_sphere; starts at (-0.99, -0.30, 1.11) m, at rest
- ball: free body; its geoms: ball_sphere; starts at (0.70, 0.30, 0.62) m, at rest

What happened, in order:
 0.00 s  weight_sphere starts touching weight_shelf_deck
 0.00 s  seesaw_beam starts touching ball_sphere
 0.00 s  pendulum is at its largest at the start, 66.4°
 0.00 s  cart starts at its lower stop (0 m)
 0.00 s  seesaw starts at its upper stop (0°)
 0.00 s  seesaw is at its largest, 0.0°
 0.11 s  seesaw_ball_right_lip first touches ball_sphere
 0.55 s  pendulum_bob first touches cart_ram
 0.57 s  cart_ram first touches weight_sphere
 0.57 s  weight starts moving
 0.58 s  pendulum_bob leaves cart_ram
 0.58 s  cart_ram leaves weight_sphere
 0.63 s  weight_sphere leaves weight_shelf_deck
 0.64 s  weight is at the top of its flight, at (-0.88, -0.30, 1.12) m
 0.81 s  weight_sphere first touches weight_chute_front
 0.83 s  cart reaches its upper stop (0.32 m) moving +0.79 m/s
 0.85 s  weight_sphere leaves weight_chute_front
 0.86 s  pendulum_bob touches cart_ram again
 0.86 s  cart is at its largest, 0.3 m
 0.86 s  pendulum is at its smallest, -18.7°
 0.87 s  cart passes 0.05 m from weight_chute (weight_chute_outer_side) without touching it: nearest points (-0.87, -0.37, 1.07) m and (-0.87, -0.42, 1.07) m
 0.87 s  cart passes 0.35 m from seesaw (seesaw_weight_end_lip) without touching it: nearest points (-0.80, -0.30, 1.05) m and (-0.80, -0.30, 0.70) m
 0.87 s  pendulum passes 0.23 m from weight_shelf (weight_shelf_deck) without touching it: nearest points (-1.37, -0.30, 1.13) m and (-1.17, -0.30, 1.03) m
 0.87 s  pendulum passes 0.45 m from weight_chute (weight_chute_outer_side) without touching it: nearest points (-1.36, -0.33, 1.18) m and (-0.92, -0.42, 1.12) m
 0.87 s  pendulum_bob leaves cart_ram
 0.97 s  seesaw_beam first touches weight_sphere
 0.97 s  ball starts moving
 1.00 s  seesaw_beam leaves weight_sphere
 1.07 s  seesaw_weight_end_lip first touches weight_sphere
 1.08 s  seesaw_beam leaves ball_sphere
 1.08 s  seesaw_ball_right_lip leaves ball_sphere
 1.08 s  seesaw_beam first touches seesaw_lower_stop_block
 1.08 s  seesaw is at its smallest, -28.9°
 1.09 s  seesaw_weight_end_lip leaves weight_sphere
 1.09 s  seesaw_beam touches weight_sphere again
 1.10 s  weight passes 0.07 m from seesaw_lower_stop (seesaw_lower_stop_block) without touching it: nearest points (-0.65, -0.30, 0.22) m and (-0.65, -0.30, 0.15) m
 1.41 s  ball is at the top of its flight, at (-0.15, 0.30, 1.48) m
 1.42 s  weight passes 0.37 m from seesaw_support (seesaw_support_column) without touching it: nearest points (-0.42, -0.27, 0.40) m and (-0.06, -0.16, 0.40) m
 1.69 s  ball passes 0.39 m from weight_chute (weight_chute_inner_side) without touching it: nearest points (-0.77, 0.24, 1.10) m and (-0.77, -0.15, 1.10) m
 1.71 s  cart passes 0.48 m from ball (ball_sphere) without touching it: nearest points (-0.82, -0.23, 1.06) m and (-0.82, 0.25, 1.05) m
 1.76 s  seesaw_beam leaves weight_sphere
 1.76 s  seesaw_weight_end_lip touches weight_sphere again
 1.77 s  ball_sphere first touches cup_bottom
 1.77 s  ball passes 0.35 m from weight_shelf (weight_shelf_inner_leg) without touching it: nearest points (-0.95, 0.24, 0.86) m and (-0.95, -0.10, 0.86) m
 1.79 s  ball_sphere leaves cup_bottom
 1.81 s  seesaw_weight_end_lip leaves weight_sphere
 1.81 s  seesaw_beam leaves seesaw_lower_stop_block
 1.84 s  seesaw_weight_end_lip touches weight_sphere again
 1.84 s  seesaw_beam touches seesaw_lower_stop_block again
 1.85 s  ball_sphere touches cup_bottom again
 1.85 s  seesaw_beam touches weight_sphere again
 1.85 s  seesaw_weight_end_lip leaves weight_sphere
 1.89 s  seesaw_weight_end_lip touches weight_sphere again
 1.89 s  weight comes to rest at (-0.66, -0.30, 0.31) m
 1.89 s  ball comes to rest at (-0.98, 0.30, 0.86) m
 2.34 s  pendulum passes 0.25 m from cup (cup_left_wall) without touching it: nearest points (-1.81, -0.18, 1.09) m and (-1.81, 0.04, 0.98) m
 2.71 s  pendulum_bob touches cart_ram again
 2.72 s  pendulum_bob leaves cart_ram
 2.77 s  cart reaches its upper stop (0.32 m) again moving +0.32 m/s
 2.79 s  cart passes 0.39 m from seesaw_lower_stop (seesaw_lower_stop_block) without touching it: nearest points (-1.16, -0.24, 0.09) m and (-0.77, -0.24, 0.09) m
 4.72 s  pendulum_bob touches cart_ram again
 4.73 s  pendulum_bob leaves cart_ram
 4.83 s  cart reaches its upper stop (0.32 m) again moving +0.20 m/s

State every 0.25 s:
0.00 s: pendulum at 66.4°, still; touching nothing | cart at 0.000 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.99, -0.30, 1.11) m, at rest; touching weight_shelf_deck | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_beam
0.25 s: pendulum at 50.6°, turning -122°/s; touching nothing | cart at 0.000 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.99, -0.30, 1.11) m, at rest; touching weight_shelf_deck | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_ball_right_lip, seesaw_beam
0.50 s: pendulum at 9.2°, turning -194°/s; touching nothing | cart at 0.000 m, still; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.99, -0.30, 1.11) m, at rest; touching weight_shelf_deck | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_ball_right_lip, seesaw_beam
0.75 s: pendulum at -13.9°, turning -52°/s; touching nothing | cart at 0.246 m, moving +0.91 m/s; touching nothing | seesaw at 0.0°, still; touching ball_sphere | weight at (-0.70, -0.30, 1.05) m, moving 1.97 m/s (vx +1.62, vy -0.00, vz -1.13); touching nothing | ball at (0.70, 0.30, 0.62) m, at rest; touching seesaw_ball_right_lip, seesaw_beam
1.00 s: pendulum at -16.1°, turning +31°/s; touching nothing | cart at 0.315 m, moving -0.04 m/s; touching nothing | seesaw at -6.8°, turning -274°/s; touching ball_sphere, weight_sphere | weight at (-0.65, -0.30, 0.58) m, moving 2.77 m/s (vx -0.42, vy -0.00, vz -2.74); touching seesaw_beam | ball at (0.69, 0.30, 0.70) m, moving 3.38 m/s (vx -0.73, vy +0.00, vz +3.30); touching seesaw_ball_right_lip, seesaw_beam
1.25 s: pendulum at -4.6°, turning +57°/s; touching nothing | cart at 0.307 m, moving -0.02 m/s; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.54, -0.30, 0.37) m, moving 0.59 m/s (vx +0.52, vy -0.00, vz +0.28); touching seesaw_beam | ball at (0.21, 0.30, 1.35) m, moving 2.73 m/s (vx -2.22, vy -0.00, vz +1.59); touching nothing
1.50 s: pendulum at 9.6°, turning +51°/s; touching nothing | cart at 0.302 m, moving -0.01 m/s; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.50, -0.30, 0.39) m, moving 0.25 m/s (vx -0.22, vy -0.00, vz -0.12); touching seesaw_beam | ball at (-0.35, 0.30, 1.45) m, moving 2.38 m/s (vx -2.22, vy +0.00, vz -0.86); touching nothing
1.75 s: pendulum at 18.2°, turning +15°/s; touching nothing | cart at 0.299 m, still; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.65, -0.30, 0.32) m, moving 1.09 m/s (vx -0.95, vy -0.00, vz -0.52); touching seesaw_beam | ball at (-0.90, 0.30, 0.93) m, moving 3.99 m/s (vx -2.22, vy +0.00, vz -3.32); touching nothing
2.00 s: pendulum at 16.4°, turning -29°/s; touching nothing | cart at 0.297 m, still; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.66, -0.30, 0.31) m, at rest; touching seesaw_beam, seesaw_weight_end_lip | ball at (-0.98, 0.30, 0.86) m, at rest; touching cup_bottom
2.25 s: pendulum at 5.1°, turning -56°/s; touching nothing | cart at 0.296 m, still; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.66, -0.30, 0.31) m, at rest; touching seesaw_beam, seesaw_weight_end_lip | ball at (-0.98, 0.30, 0.86) m, at rest; touching cup_bottom
2.50 s: pendulum at -9.1°, turning -51°/s; touching nothing | cart at 0.296 m, still; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.66, -0.30, 0.31) m, at rest; touching seesaw_beam, seesaw_weight_end_lip | ball at (-0.98, 0.30, 0.86) m, at rest; touching cup_bottom
2.75 s: pendulum at -17.7°, turning -9°/s; touching nothing | cart at 0.309 m, moving +0.33 m/s; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.66, -0.30, 0.31) m, at rest; touching seesaw_beam, seesaw_weight_end_lip | ball at (-0.98, 0.30, 0.86) m, at rest; touching cup_bottom
3.00 s: pendulum at -14.6°, turning +32°/s; touching nothing | cart at 0.311 m, moving -0.04 m/s; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.66, -0.30, 0.31) m, at rest; touching seesaw_beam, seesaw_weight_end_lip | ball at (-0.98, 0.30, 0.86) m, at rest; touching cup_bottom
3.25 s: pendulum at -3.1°, turning +55°/s; touching nothing | cart at 0.303 m, moving -0.02 m/s; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.66, -0.30, 0.31) m, at rest; touching seesaw_beam, seesaw_weight_end_lip | ball at (-0.98, 0.30, 0.86) m, at rest; touching cup_bottom
3.50 s: pendulum at 10.2°, turning +46°/s; touching nothing | cart at 0.299 m, moving -0.01 m/s; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.66, -0.30, 0.31) m, at rest; touching seesaw_beam, seesaw_weight_end_lip | ball at (-0.98, 0.30, 0.86) m, at rest; touching cup_bottom
3.75 s: pendulum at 17.6°, turning +10°/s; touching nothing | cart at 0.296 m, still; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.66, -0.30, 0.31) m, at rest; touching seesaw_beam, seesaw_weight_end_lip | ball at (-0.98, 0.30, 0.86) m, at rest; touching cup_bottom
4.00 s: pendulum at 14.8°, turning -31°/s; touching nothing | cart at 0.294 m, still; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.66, -0.30, 0.31) m, at rest; touching seesaw_beam, seesaw_weight_end_lip | ball at (-0.98, 0.30, 0.86) m, at rest; touching cup_bottom
4.25 s: pendulum at 3.6°, turning -54°/s; touching nothing | cart at 0.293 m, still; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.66, -0.30, 0.31) m, at rest; touching seesaw_beam, seesaw_weight_end_lip | ball at (-0.98, 0.30, 0.86) m, at rest; touching cup_bottom
4.50 s: pendulum at -9.7°, turning -47°/s; touching nothing | cart at 0.292 m, still; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.66, -0.30, 0.31) m, at rest; touching seesaw_beam, seesaw_weight_end_lip | ball at (-0.98, 0.30, 0.86) m, at rest; touching cup_bottom
4.75 s: pendulum at -17.2°, turning -6°/s; touching nothing | cart at 0.299 m, moving +0.23 m/s; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.66, -0.30, 0.31) m, at rest; touching seesaw_beam, seesaw_weight_end_lip | ball at (-0.98, 0.30, 0.86) m, at rest; touching cup_bottom
5.00 s: pendulum at -13.7°, turning +33°/s; touching nothing | cart at 0.317 m, moving -0.02 m/s; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.66, -0.30, 0.31) m, at rest; touching seesaw_beam, seesaw_weight_end_lip | ball at (-0.98, 0.30, 0.86) m, at rest; touching cup_bottom
5.25 s: pendulum at -2.3°, turning +54°/s; touching nothing | cart at 0.312 m, moving -0.01 m/s; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.66, -0.30, 0.31) m, at rest; touching seesaw_beam, seesaw_weight_end_lip | ball at (-0.98, 0.30, 0.86) m, at rest; touching cup_bottom
5.50 s: pendulum at 10.4°, turning +43°/s; touching nothing | cart at 0.310 m, still; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.66, -0.30, 0.31) m, at rest; touching seesaw_beam, seesaw_weight_end_lip | ball at (-0.98, 0.30, 0.86) m, at rest; touching cup_bottom
5.75 s: pendulum at 17.1°, turning +8°/s; touching nothing | cart at 0.308 m, still; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.66, -0.30, 0.31) m, at rest; touching seesaw_beam, seesaw_weight_end_lip | ball at (-0.98, 0.30, 0.86) m, at rest; touching cup_bottom
6.00 s: pendulum at 14.0°, turning -32°/s; touching nothing | cart at 0.307 m, still; touching nothing | seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere | weight at (-0.66, -0.30, 0.31) m, at rest; touching seesaw_beam, seesaw_weight_end_lip | ball at (-0.98, 0.30, 0.86) m, at rest; touching cup_bottom

At the end (6.00 s):
- pendulum at 14.0°, turning -32°/s; touching nothing
- cart at 0.307 m, still; touching nothing
- seesaw at -28.6°, still; touching seesaw_lower_stop_block, weight_sphere
- weight at (-0.66, -0.30, 0.31) m, at rest; touching seesaw_beam, seesaw_weight_end_lip
- ball at (-0.98, 0.30, 0.86) m, at rest; touching cup_bottom
</history>
