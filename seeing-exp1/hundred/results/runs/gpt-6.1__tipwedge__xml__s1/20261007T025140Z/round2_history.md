MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block: free body; its geoms: block_weight; starts at (0.12, 0.20, 1.12) m, at rest
- wedge: free body; its geoms: wedge_foot, wedge_stem, wedge_bottom, wedge_left_slope, wedge_right_slope, wedge_loading_post, wedge_loading_ledge, wedge_striker; starts at (0.00, 0.00, 0.03) m, at rest
- ball1: free body; its geoms: ball1_sphere; starts at (0.24, 0.00, 0.48) m, at rest
- flap: hinge joint flap_hinge about axis (0.00, -1.00, 0.00), range -114.592° to 0° as MuJoCo applies it; its geoms: flap_striker_panel, flap_release_shelf, flap_retaining_lip, flap_axle, flap_counterweight_support, flap_counterweight_arm, flap_counterweight; starts at 0.0°, still
- ball2: free body; its geoms: ball2_sphere; starts at (1.03, 0.00, 0.51) m, at rest

What happened, in order:
 0.00 s  flap_retaining_lip starts touching ball2_sphere
 0.00 s  wedge_foot starts touching floor
 0.00 s  flap starts at its upper stop (0°)
 0.00 s  flap_retaining_lip leaves ball2_sphere
 0.00 s  ball1_sphere first touches ramp_start_shelf
 0.00 s  flap_release_shelf first touches ball2_sphere
 0.01 s  block starts moving
 0.32 s  block_weight first touches wedge_loading_ledge
 0.32 s  wedge starts moving
 0.34 s  block_weight leaves wedge_loading_ledge
 0.42 s  block_weight touches wedge_loading_ledge again
 0.45 s  wedge_striker first touches ball1_sphere
 0.45 s  ball1 starts moving
 0.47 s  wedge_striker leaves ball1_sphere
 0.52 s  wedge_striker touches ball1_sphere again
 0.52 s  wedge_loading_ledge first touches ramp_start_rail_left
 0.52 s  wedge_striker leaves ball1_sphere
 0.54 s  wedge_right_slope first touches ramp_start_shelf
 0.55 s  wedge comes to rest at (0.00, 0.00, 0.04) m
 0.72 s  block_weight leaves wedge_loading_ledge
 0.79 s  ball1_sphere leaves ramp_start_shelf
 0.79 s  ball1_sphere first touches ramp_slope
 0.82 s  block passes 0.11 m from ball1 (ball1_sphere) without touching it: nearest points (0.40, 0.16, 0.48) m and (0.40, 0.06, 0.48) m
 0.85 s  block passes 0.01 m from ramp (ramp_slope_rail_left) without touching it: nearest points (0.41, 0.16, 0.40) m and (0.41, 0.15, 0.40) m
 1.00 s  block_weight first touches floor
 1.02 s  block_weight leaves floor
 1.05 s  block_weight touches floor again
 1.26 s  block passes 0.35 m from flap (flap_counterweight) without touching it: nearest points (0.58, 0.18, 0.08) m and (0.87, 0.18, 0.27) m
 1.26 s  block passes 0.40 m from cup (cup_back_wall) without touching it: nearest points (0.58, 0.22, 0.08) m and (0.98, 0.22, 0.08) m
 1.40 s  block comes to rest at (0.53, 0.20, 0.04) m
 1.44 s  flap is at its largest, 0.0°
 1.44 s  flap_release_shelf leaves ball2_sphere
 1.44 s  ball1_sphere first touches flap_striker_panel
 1.44 s  ball2 starts moving
 1.45 s  ball1_sphere leaves flap_striker_panel
 1.45 s  ball2 is at the top of its flight, at (1.02, 0.00, 0.51) m
 1.50 s  ball1_sphere leaves ramp_slope
 1.50 s  ball1_sphere touches flap_striker_panel again
 1.55 s  ball1_sphere first touches ball2_sphere
 1.63 s  flap is at its smallest, -115.9°
 1.65 s  flap reaches its lower stop (-114.592°) moving +61°/s
 1.67 s  ball1_sphere leaves ball2_sphere
 1.79 s  ball1_sphere leaves flap_striker_panel
 1.85 s  ball2_sphere first touches cup_bottom
 1.95 s  ball1_sphere touches ball2_sphere again
 1.97 s  ball1_sphere first touches cup_bottom
 1.97 s  ball1_sphere leaves ball2_sphere
 2.33 s  ball2_sphere first touches cup_right_wall
 2.33 s  ball2_sphere leaves cup_bottom
 2.35 s  ball1_sphere first touches cup_front_wall
 2.37 s  ball2_sphere leaves cup_right_wall
 2.37 s  ball2_sphere touches cup_bottom again
 2.38 s  ball1_sphere leaves cup_front_wall
 2.55 s  ball1_sphere first touches flap_retaining_lip
 2.55 s  ball1 comes to rest at (1.20, -0.13, 0.08) m
 2.57 s  ball1_sphere leaves flap_retaining_lip
 2.59 s  wedge_right_slope leaves ramp_start_shelf
 4.53 s  ball1_sphere touches cup_front_wall again
 4.54 s  ball1_sphere leaves cup_front_wall
 4.55 s  ball2_sphere first touches cup_back_wall
 4.59 s  ball2_sphere leaves cup_back_wall
 6.00 s  ball2 is still moving at the end, 0.08 m/s

State every 0.25 s:
0.00 s: block at (0.12, 0.20, 1.12) m, at rest; touching nothing | wedge at (0.00, 0.00, 0.03) m, at rest; touching floor | ball1 at (0.24, 0.00, 0.48) m, at rest; touching nothing | flap at 0.0°, still; touching ball2_sphere | ball2 at (1.03, 0.00, 0.51) m, at rest; touching flap_retaining_lip
0.25 s: block at (0.12, 0.20, 0.82) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | wedge at (0.00, 0.00, 0.03) m, at rest; touching floor | ball1 at (0.24, 0.00, 0.48) m, at rest; touching ramp_start_shelf | flap at 0.0°, still; touching ball2_sphere | ball2 at (1.03, 0.00, 0.51) m, at rest; touching flap_release_shelf
0.50 s: block at (0.23, 0.20, 0.60) m, moving 0.74 m/s (vx +0.70, vy -0.08, vz -0.23), turned 10° from how it started; touching wedge_loading_ledge | wedge at (0.00, 0.00, 0.04) m, at rest, turned 10° from how it started; touching block_weight, floor | ball1 at (0.27, 0.00, 0.48) m, moving 0.45 m/s (vx +0.45, vy -0.00, vz +0.05); touching ramp_start_shelf | flap at 0.0°, still; touching ball2_sphere | ball2 at (1.03, 0.00, 0.51) m, at rest; touching flap_release_shelf
0.75 s: block at (0.32, 0.20, 0.55) m, moving 0.92 m/s (vx +0.41, vy -0.01, vz -0.82), turned 140° from how it started; touching nothing | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left, ramp_start_shelf | ball1 at (0.37, 0.00, 0.48) m, moving 0.43 m/s (vx +0.42, vy -0.00, vz -0.09); touching ramp_start_shelf | flap at 0.0°, still; touching ball2_sphere | ball2 at (1.03, 0.00, 0.51) m, at rest; touching flap_release_shelf
1.00 s: block at (0.43, 0.20, 0.04) m, moving 0.93 m/s (vx +0.83, vy -0.00, vz -0.43), turned 47° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left, ramp_start_shelf | ball1 at (0.51, 0.00, 0.46) m, moving 0.69 m/s (vx +0.68, vy -0.00, vz -0.09); touching ramp_slope | flap at 0.0°, still; touching ball2_sphere | ball2 at (1.02, 0.00, 0.51) m, at rest; touching flap_release_shelf
1.25 s: block at (0.54, 0.20, 0.04) m, at rest, turned 169° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left, ramp_start_shelf | ball1 at (0.71, 0.00, 0.43) m, moving 0.91 m/s (vx +0.91, vy -0.00, vz -0.12); touching ramp_slope | flap at 0.0°, still; touching ball2_sphere | ball2 at (1.02, 0.00, 0.51) m, at rest; touching flap_release_shelf
1.50 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left, ramp_start_shelf | ball1 at (0.94, 0.00, 0.40) m, moving 0.75 m/s (vx +0.75, vy -0.00, vz -0.09); touching ramp_slope | flap at -31.0°, turning -397°/s; touching nothing | ball2 at (1.03, 0.00, 0.50) m, moving 0.47 m/s (vx +0.09, vy +0.00, vz -0.47); touching nothing
1.75 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left, ramp_start_shelf | ball1 at (1.10, 0.00, 0.32) m, moving 0.97 m/s (vx +0.89, vy -0.00, vz -0.41); touching flap_striker_panel | flap at -114.6°, still; touching ball1_sphere | ball2 at (1.21, 0.01, 0.29) m, moving 2.00 m/s (vx +1.02, vy +0.05, vz -1.72); touching nothing
2.00 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left, ramp_start_shelf | ball1 at (1.30, -0.02, 0.08) m, moving 0.40 m/s (vx -0.19, vy -0.34, vz +0.05); touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.41, 0.02, 0.06) m, moving 0.69 m/s (vx +0.69, vy +0.07, vz +0.07); touching cup_bottom
2.25 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left, ramp_start_shelf | ball1 at (1.25, -0.11, 0.08) m, moving 0.39 m/s (vx -0.19, vy -0.35, vz +0.00); touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.58, 0.04, 0.06) m, moving 0.70 m/s (vx +0.69, vy +0.07, vz +0.00); touching cup_bottom
2.50 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left, ramp_start_shelf | ball1 at (1.21, -0.13, 0.08) m, moving 0.16 m/s (vx -0.15, vy +0.06, vz +0.00); touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.62, 0.05, 0.06) m, moving 0.11 m/s (vx -0.09, vy +0.06, vz +0.00); touching cup_bottom
2.75 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left | ball1 at (1.21, -0.13, 0.08) m, at rest; touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.60, 0.07, 0.06) m, moving 0.11 m/s (vx -0.09, vy +0.06, vz +0.00); touching cup_bottom
3.00 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left | ball1 at (1.22, -0.13, 0.08) m, at rest; touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.58, 0.08, 0.06) m, moving 0.11 m/s (vx -0.09, vy +0.06, vz -0.00); touching cup_bottom
3.25 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left | ball1 at (1.23, -0.13, 0.08) m, at rest; touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.55, 0.09, 0.06) m, moving 0.11 m/s (vx -0.09, vy +0.06, vz -0.00); touching cup_bottom
3.50 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left | ball1 at (1.24, -0.14, 0.08) m, at rest; touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.53, 0.11, 0.06) m, moving 0.11 m/s (vx -0.09, vy +0.06, vz -0.00); touching cup_bottom
3.75 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left | ball1 at (1.25, -0.14, 0.08) m, at rest; touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.51, 0.12, 0.06) m, moving 0.11 m/s (vx -0.09, vy +0.06, vz -0.00); touching cup_bottom
4.00 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left | ball1 at (1.26, -0.14, 0.08) m, at rest; touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.48, 0.13, 0.06) m, moving 0.11 m/s (vx -0.09, vy +0.06, vz -0.00); touching cup_bottom
4.25 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left | ball1 at (1.27, -0.14, 0.08) m, at rest; touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.46, 0.15, 0.06) m, moving 0.11 m/s (vx -0.09, vy +0.06, vz -0.00); touching cup_bottom
4.50 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left | ball1 at (1.28, -0.14, 0.08) m, at rest; touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.44, 0.16, 0.06) m, moving 0.11 m/s (vx -0.09, vy +0.06, vz -0.00); touching cup_bottom
4.75 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left | ball1 at (1.28, -0.14, 0.08) m, at rest; touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.42, 0.16, 0.06) m, moving 0.08 m/s (vx -0.08, vy -0.01, vz +0.00); touching cup_bottom
5.00 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left | ball1 at (1.29, -0.14, 0.08) m, at rest; touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.40, 0.16, 0.06) m, moving 0.08 m/s (vx -0.08, vy -0.01, vz -0.00); touching cup_bottom
5.25 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left | ball1 at (1.30, -0.14, 0.08) m, at rest; touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.38, 0.16, 0.06) m, moving 0.08 m/s (vx -0.08, vy -0.01, vz -0.00); touching cup_bottom
5.50 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left | ball1 at (1.30, -0.14, 0.08) m, at rest; touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.36, 0.15, 0.06) m, moving 0.08 m/s (vx -0.08, vy -0.01, vz -0.00); touching cup_bottom
5.75 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left | ball1 at (1.31, -0.14, 0.08) m, at rest; touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.33, 0.15, 0.06) m, moving 0.08 m/s (vx -0.08, vy -0.01, vz -0.00); touching cup_bottom
6.00 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left | ball1 at (1.32, -0.13, 0.08) m, at rest; touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.31, 0.14, 0.06) m, moving 0.08 m/s (vx -0.08, vy -0.01, vz -0.00); touching cup_bottom

At the end (6.00 s):
- block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor
- wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left
- ball1 at (1.32, -0.13, 0.08) m, at rest; touching cup_bottom
- flap at -114.6°, still; touching nothing
- ball2 at (1.31, 0.14, 0.06) m, moving 0.08 m/s (vx -0.08, vy -0.01, vz -0.00); touching cup_bottom
</history>
