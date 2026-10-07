MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block: free body; its geoms: block_weight; starts at (0.12, 0.20, 1.12) m, at rest
- wedge: free body; its geoms: wedge_foot, wedge_stem, wedge_bottom, wedge_left_slope, wedge_right_slope, wedge_loading_post, wedge_loading_ledge, wedge_striker; starts at (0.00, 0.00, 0.03) m, at rest
- ball1: free body; its geoms: ball1_sphere; starts at (0.24, 0.00, 0.48) m, at rest
- flap: hinge joint flap_hinge about axis (0.00, -1.00, 0.00), range -114.592° to 0° as MuJoCo applies it; its geoms: flap_striker_panel, flap_release_shelf, flap_retaining_lip, flap_rear_retainer, flap_axle, flap_counterweight_support, flap_counterweight_arm, flap_counterweight; starts at 0.0°, still
- ball2: free body; its geoms: ball2_sphere; starts at (1.03, 0.00, 0.51) m, at rest

What happened, in order:
 0.00 s  wedge_foot starts touching floor
 0.00 s  flap_retaining_lip starts touching ball2_sphere
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
 1.44 s  ball1_sphere leaves ramp_slope
 1.44 s  ball1_sphere first touches flap_striker_panel
 1.44 s  ball2 starts moving
 1.44 s  flap_rear_retainer first touches ball2_sphere
 1.45 s  ball1_sphere leaves flap_striker_panel
 1.47 s  flap_rear_retainer leaves ball2_sphere
 1.48 s  ball1_sphere touches ramp_slope again
 1.50 s  flap_retaining_lip touches ball2_sphere again
 1.50 s  ball1_sphere touches flap_striker_panel again
 1.50 s  ball1_sphere leaves flap_striker_panel
 1.50 s  flap_retaining_lip leaves ball2_sphere
 1.54 s  flap_retaining_lip touches ball2_sphere again
 1.55 s  flap_retaining_lip leaves ball2_sphere
 1.55 s  ball1_sphere leaves ramp_slope
 1.55 s  ball1_sphere touches flap_striker_panel again
 1.59 s  flap_rear_retainer touches ball2_sphere again
 1.67 s  flap_rear_retainer leaves ball2_sphere
 1.70 s  ball1_sphere first touches flap_axle
 1.70 s  flap reaches its lower stop (-114.592°) moving -558°/s
 1.71 s  flap is at its smallest, -115.7°
 1.71 s  ball1_sphere leaves flap_axle
 1.72 s  ball2_sphere first touches cup_bottom
 1.72 s  flap reaches its lower stop (-114.592°) again moving +61°/s
 1.79 s  ball2 comes to rest at (1.33, 0.00, 0.06) m
 1.92 s  ball1_sphere leaves flap_striker_panel
 1.98 s  ball1_sphere first touches flap_rear_retainer
 2.07 s  ball1_sphere leaves flap_rear_retainer
 2.15 s  ball1 passes 0.01 m from ball2 (ball2_sphere) without touching it: nearest points (1.36, 0.00, 0.09) m and (1.35, 0.00, 0.08) m
 2.18 s  ball1_sphere first touches cup_bottom
 2.32 s  ball1_sphere leaves cup_bottom
 2.32 s  ball1_sphere first touches cup_right_wall
 2.35 s  ball1_sphere leaves cup_right_wall
 2.39 s  ball1_sphere touches cup_bottom again
 2.44 s  ball1 comes to rest at (1.60, -0.01, 0.08) m
 2.59 s  wedge_right_slope leaves ramp_start_shelf

State every 0.25 s:
0.00 s: block at (0.12, 0.20, 1.12) m, at rest; touching nothing | wedge at (0.00, 0.00, 0.03) m, at rest; touching floor | ball1 at (0.24, 0.00, 0.48) m, at rest; touching nothing | flap at 0.0°, still; touching ball2_sphere | ball2 at (1.03, 0.00, 0.51) m, at rest; touching flap_retaining_lip
0.25 s: block at (0.12, 0.20, 0.82) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | wedge at (0.00, 0.00, 0.03) m, at rest; touching floor | ball1 at (0.24, 0.00, 0.48) m, at rest; touching ramp_start_shelf | flap at 0.0°, still; touching ball2_sphere | ball2 at (1.03, 0.00, 0.51) m, at rest; touching flap_release_shelf
0.50 s: block at (0.23, 0.20, 0.60) m, moving 0.74 m/s (vx +0.70, vy -0.08, vz -0.23), turned 10° from how it started; touching wedge_loading_ledge | wedge at (0.00, 0.00, 0.04) m, at rest, turned 10° from how it started; touching block_weight, floor | ball1 at (0.27, 0.00, 0.48) m, moving 0.45 m/s (vx +0.45, vy -0.00, vz +0.05); touching ramp_start_shelf | flap at 0.0°, still; touching ball2_sphere | ball2 at (1.03, 0.00, 0.51) m, at rest; touching flap_release_shelf
0.75 s: block at (0.32, 0.20, 0.55) m, moving 0.92 m/s (vx +0.41, vy -0.01, vz -0.82), turned 140° from how it started; touching nothing | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left, ramp_start_shelf | ball1 at (0.37, 0.00, 0.48) m, moving 0.43 m/s (vx +0.42, vy -0.00, vz -0.09); touching ramp_start_shelf | flap at 0.0°, still; touching ball2_sphere | ball2 at (1.03, 0.00, 0.51) m, at rest; touching flap_release_shelf
1.00 s: block at (0.43, 0.20, 0.04) m, moving 0.93 m/s (vx +0.83, vy -0.00, vz -0.43), turned 47° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left, ramp_start_shelf | ball1 at (0.51, 0.00, 0.46) m, moving 0.69 m/s (vx +0.68, vy -0.00, vz -0.09); touching ramp_slope | flap at 0.0°, still; touching ball2_sphere | ball2 at (1.02, 0.00, 0.51) m, at rest; touching flap_release_shelf
1.25 s: block at (0.54, 0.20, 0.04) m, at rest, turned 169° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left, ramp_start_shelf | ball1 at (0.71, 0.00, 0.43) m, moving 0.91 m/s (vx +0.91, vy -0.00, vz -0.12); touching ramp_slope | flap at 0.0°, still; touching ball2_sphere | ball2 at (1.02, 0.00, 0.51) m, at rest; touching flap_release_shelf
1.50 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left, ramp_start_shelf | ball1 at (0.93, 0.00, 0.41) m, moving 0.46 m/s (vx +0.46, vy -0.00, vz -0.04); touching ramp_slope | flap at -21.9°, turning -399°/s; touching ball2_sphere | ball2 at (1.11, 0.00, 0.50) m, moving 1.42 m/s (vx +1.30, vy +0.00, vz -0.57); touching flap_retaining_lip
1.75 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left, ramp_start_shelf | ball1 at (1.02, 0.00, 0.36) m, moving 0.50 m/s (vx +0.45, vy -0.00, vz -0.21); touching flap_striker_panel | flap at -114.6°, turning +2°/s; touching ball1_sphere | ball2 at (1.33, 0.00, 0.05) m, moving 0.35 m/s (vx +0.01, vy +0.00, vz +0.35); touching cup_bottom
2.00 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left, ramp_start_shelf | ball1 at (1.21, -0.01, 0.25) m, moving 1.23 m/s (vx +1.12, vy -0.00, vz -0.49); touching flap_rear_retainer | flap at -114.6°, still; touching ball1_sphere | ball2 at (1.33, 0.00, 0.06) m, at rest; touching cup_bottom
2.25 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left, ramp_start_shelf | ball1 at (1.53, -0.01, 0.08) m, moving 1.24 m/s (vx +1.24, vy -0.00, vz +0.04); touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.33, 0.00, 0.06) m, at rest; touching cup_bottom
2.50 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left, ramp_start_shelf | ball1 at (1.60, -0.01, 0.08) m, at rest; touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.33, 0.00, 0.06) m, at rest; touching cup_bottom
2.75 s: block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor | wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left | ball1 at (1.60, -0.01, 0.08) m, at rest; touching cup_bottom | flap at -114.6°, still; touching nothing | ball2 at (1.33, 0.00, 0.06) m, at rest; touching cup_bottom
(the same through 6.00 s)

At the end (6.00 s):
- block at (0.53, 0.20, 0.04) m, at rest, turned 180° from how it started; touching floor
- wedge at (0.00, 0.00, 0.04) m, at rest, turned 11° from how it started; touching floor, ramp_start_rail_left
- ball1 at (1.60, -0.01, 0.08) m, at rest; touching cup_bottom
- flap at -114.6°, still; touching nothing
- ball2 at (1.33, 0.00, 0.06) m, at rest; touching cup_bottom
</history>
