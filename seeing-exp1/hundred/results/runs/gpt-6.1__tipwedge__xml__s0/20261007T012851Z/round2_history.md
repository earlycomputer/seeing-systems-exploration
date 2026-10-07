MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- block: free body; its geoms: block_weight; starts at (0.20, 0.00, 0.94) m, at rest
- wedge: free body; its geoms: wedge_foot, wedge_lower, wedge_middle, wedge_upper, wedge_cap; starts at (0.00, 0.00, 0.00) m, at rest
- ball1: free body; its geoms: ball1_sphere; starts at (0.39, 0.00, 0.30) m, at rest
- flap: hinge joint flap_hinge about axis (0.00, -1.00, 0.00), range -75° to 0° as MuJoCo applies it; its geoms: flap_striker, flap_tray, flap_release_lip, flap_rear_lip, flap_left_guide, flap_right_guide; starts at 0.0°, still
- ball2: free body; its geoms: ball2_sphere; starts at (1.29, 0.00, 0.59) m, at rest

What happened, in order:
 0.00 s  wedge_foot starts touching floor
 0.00 s  flap starts at its upper stop (0°)
 0.00 s  flap is at its largest at the start, 0.0°
 0.01 s  block starts moving
 0.01 s  ball1 starts moving
 0.01 s  ball2 starts moving
 0.01 s  flap_tray first touches ball2_sphere
 0.01 s  ball1_sphere first touches ramp_terrace
 0.32 s  block_weight first touches wedge_cap
 0.32 s  wedge starts moving
 0.49 s  wedge_cap first touches ball1_sphere
 0.51 s  wedge_cap leaves ball1_sphere
 0.55 s  wedge_cap touches ball1_sphere again
 0.58 s  wedge_cap leaves ball1_sphere
 0.61 s  block_weight first touches ball1_sphere
 0.62 s  block_weight leaves ball1_sphere
 0.62 s  wedge_cap first touches ramp_terrace
 0.64 s  wedge comes to rest at (0.01, 0.00, 0.02) m
 0.71 s  block comes to rest at (0.37, 0.00, 0.35) m
 0.74 s  ball1_sphere leaves ramp_terrace
 0.74 s  ball1_sphere first touches ramp_slope
 0.88 s  ball1_sphere touches ramp_terrace again
 0.88 s  ball1_sphere leaves ramp_terrace
 1.65 s  ball1_sphere leaves ramp_slope
 1.65 s  ball1_sphere first touches flap_striker
 1.67 s  ball1 passes 0.33 m from ball2 (ball2_sphere) without touching it: nearest points (1.23, 0.00, 0.22) m and (1.28, 0.00, 0.55) m
 1.69 s  ball1_sphere leaves flap_striker
 1.70 s  ball1_sphere touches ramp_slope again
 1.78 s  flap_rear_lip first touches ball2_sphere
 1.81 s  flap_rear_lip leaves ball2_sphere
 1.83 s  ball1_sphere touches flap_striker again
 2.27 s  flap_tray leaves ball2_sphere
 2.32 s  ball1 comes to rest at (1.26, 0.00, 0.14) m
 2.37 s  ball1 passes 0.25 m from cup (cup_entrance_wall) without touching it: nearest points (1.32, 0.00, 0.14) m and (1.57, 0.00, 0.13) m
 2.38 s  flap reaches its lower stop (-75°) moving -300°/s
 2.38 s  flap is at its smallest, -75.6°
 2.38 s  flap passes 0.01 m from cup (cup_entrance_wall) without touching it: nearest points (1.57, 0.02, 0.14) m and (1.57, 0.02, 0.13) m
 2.38 s  flap reaches its lower stop (-75°) again moving +4°/s
 2.44 s  ball2_sphere first touches cup_bottom
 2.48 s  ball2_sphere leaves cup_bottom
 2.53 s  ball2_sphere touches cup_bottom again
 2.97 s  ball2_sphere first touches cup_far_wall
 3.00 s  ball2_sphere leaves cup_far_wall
 3.03 s  ball2 comes to rest at (2.21, 0.00, 0.07) m
 6.00 s  block passes 0.05 m from ramp (ramp_terrace) without touching it: nearest points (0.40, -0.04, 0.29) m and (0.40, -0.04, 0.24) m

State every 0.25 s:
0.00 s: block at (0.20, 0.00, 0.94) m, at rest; touching nothing | wedge at (0.00, 0.00, 0.00) m, at rest; touching floor | ball1 at (0.39, 0.00, 0.30) m, at rest; touching nothing | flap at 0.0°, still; touching nothing | ball2 at (1.29, 0.00, 0.59) m, at rest; touching nothing
0.25 s: block at (0.20, 0.00, 0.63) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | wedge at (0.00, 0.00, 0.00) m, at rest; touching floor | ball1 at (0.39, 0.00, 0.29) m, at rest; touching ramp_terrace | flap at 0.0°, still; touching ball2_sphere | ball2 at (1.29, 0.00, 0.59) m, at rest; touching flap_tray
0.50 s: block at (0.30, 0.00, 0.39) m, moving 0.56 m/s (vx +0.54, vy +0.00, vz -0.15), turned 14° from how it started; touching wedge_cap | wedge at (0.00, 0.00, 0.01) m, at rest, turned 14° from how it started; touching ball1_sphere, block_weight | ball1 at (0.39, 0.00, 0.29) m, moving 0.47 m/s (vx +0.46, vy +0.00, vz +0.10); touching ramp_terrace, wedge_cap | flap at 0.0°, still; touching ball2_sphere | ball2 at (1.29, 0.00, 0.59) m, at rest; touching flap_tray
0.75 s: block at (0.37, 0.00, 0.35) m, at rest, turned 20° from how it started; touching wedge_cap | wedge at (0.01, 0.00, 0.02) m, at rest, turned 20° from how it started; touching block_weight, floor, ramp_terrace | ball1 at (0.49, 0.00, 0.30) m, moving 0.37 m/s (vx +0.36, vy +0.00, vz +0.11); touching ramp_slope | flap at 0.0°, still; touching ball2_sphere | ball2 at (1.29, 0.00, 0.59) m, at rest; touching flap_tray
1.00 s: block at (0.37, 0.00, 0.35) m, at rest, turned 20° from how it started; touching wedge_cap | wedge at (0.01, 0.00, 0.02) m, at rest, turned 20° from how it started; touching block_weight, floor, ramp_terrace | ball1 at (0.60, 0.00, 0.28) m, moving 0.56 m/s (vx +0.55, vy +0.00, vz -0.10); touching ramp_slope | flap at 0.0°, still; touching ball2_sphere | ball2 at (1.29, 0.00, 0.59) m, at rest; touching flap_tray
1.25 s: block at (0.37, 0.00, 0.35) m, at rest, turned 20° from how it started; touching wedge_cap | wedge at (0.01, 0.00, 0.02) m, at rest, turned 20° from how it started; touching block_weight, floor, ramp_terrace | ball1 at (0.77, 0.00, 0.25) m, moving 0.88 m/s (vx +0.86, vy +0.00, vz -0.16); touching ramp_slope | flap at 0.0°, still; touching ball2_sphere | ball2 at (1.29, 0.00, 0.59) m, at rest; touching flap_tray
1.50 s: block at (0.37, 0.00, 0.35) m, at rest, turned 20° from how it started; touching wedge_cap | wedge at (0.01, 0.00, 0.02) m, at rest, turned 20° from how it started; touching block_weight, floor, ramp_terrace | ball1 at (1.03, 0.00, 0.20) m, moving 1.19 m/s (vx +1.17, vy +0.00, vz -0.22); touching ramp_slope | flap at 0.0°, still; touching ball2_sphere | ball2 at (1.29, 0.00, 0.59) m, at rest; touching flap_tray
1.75 s: block at (0.37, 0.00, 0.35) m, at rest, turned 20° from how it started; touching wedge_cap | wedge at (0.01, 0.00, 0.02) m, at rest, turned 20° from how it started; touching block_weight, floor, ramp_terrace | ball1 at (1.22, 0.00, 0.17) m, moving 0.05 m/s (vx +0.05, vy +0.00, vz -0.00); touching ramp_slope | flap at -3.9°, turning -39°/s; touching ball2_sphere | ball2 at (1.30, 0.00, 0.59) m, moving 0.12 m/s (vx +0.12, vy +0.00, vz +0.01); touching flap_tray
2.00 s: block at (0.37, 0.00, 0.35) m, at rest, turned 20° from how it started; touching wedge_cap | wedge at (0.01, 0.00, 0.02) m, at rest, turned 20° from how it started; touching block_weight, floor, ramp_terrace | ball1 at (1.24, 0.00, 0.16) m, moving 0.07 m/s (vx +0.07, vy +0.00, vz -0.03); touching flap_striker, ramp_slope | flap at -14.5°, turning -65°/s; touching ball1_sphere, ball2_sphere | ball2 at (1.40, 0.00, 0.58) m, moving 0.64 m/s (vx +0.62, vy -0.00, vz -0.14); touching flap_tray
2.25 s: block at (0.37, 0.00, 0.35) m, at rest, turned 20° from how it started; touching wedge_cap | wedge at (0.01, 0.00, 0.02) m, at rest, turned 20° from how it started; touching block_weight, floor, ramp_terrace | ball1 at (1.26, 0.00, 0.15) m, moving 0.11 m/s (vx +0.07, vy +0.00, vz -0.08); touching ramp_slope | flap at -43.9°, turning -190°/s; touching ball2_sphere | ball2 at (1.63, 0.00, 0.46) m, moving 1.69 m/s (vx +1.26, vy -0.00, vz -1.13); touching flap_tray
2.50 s: block at (0.37, 0.00, 0.35) m, at rest, turned 20° from how it started; touching wedge_cap | wedge at (0.01, 0.00, 0.02) m, at rest, turned 20° from how it started; touching block_weight, floor, ramp_terrace | ball1 at (1.26, 0.00, 0.14) m, at rest; touching flap_striker, ramp_slope | flap at -75.0°, still; touching ball1_sphere | ball2 at (1.92, 0.00, 0.08) m, moving 0.77 m/s (vx +0.77, vy +0.00, vz +0.04); touching nothing
2.75 s: block at (0.37, 0.00, 0.35) m, at rest, turned 20° from how it started; touching wedge_cap | wedge at (0.01, 0.00, 0.02) m, at rest, turned 20° from how it started; touching block_weight, floor, ramp_terrace | ball1 at (1.26, 0.00, 0.14) m, at rest; touching flap_striker, ramp_slope | flap at -75.0°, still; touching ball1_sphere | ball2 at (2.10, 0.00, 0.07) m, moving 0.59 m/s (vx +0.59, vy +0.00, vz -0.02); touching nothing
3.00 s: block at (0.37, 0.00, 0.35) m, at rest, turned 20° from how it started; touching wedge_cap | wedge at (0.01, 0.00, 0.02) m, at rest, turned 20° from how it started; touching block_weight, floor, ramp_terrace | ball1 at (1.26, 0.00, 0.14) m, at rest; touching flap_striker, ramp_slope | flap at -75.0°, still; touching ball1_sphere | ball2 at (2.21, 0.00, 0.07) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz -0.00); touching cup_bottom, cup_far_wall
3.25 s: block at (0.37, 0.00, 0.35) m, at rest, turned 20° from how it started; touching wedge_cap | wedge at (0.01, 0.00, 0.02) m, at rest, turned 20° from how it started; touching block_weight, floor, ramp_terrace | ball1 at (1.26, 0.00, 0.14) m, at rest; touching flap_striker, ramp_slope | flap at -75.0°, still; touching ball1_sphere | ball2 at (2.20, 0.00, 0.07) m, at rest; touching cup_bottom
(the same through 4.75 s)
5.00 s: block at (0.38, 0.00, 0.35) m, at rest, turned 20° from how it started; touching wedge_cap | wedge at (0.01, 0.00, 0.02) m, at rest, turned 20° from how it started; touching block_weight, floor, ramp_terrace | ball1 at (1.26, 0.00, 0.14) m, at rest; touching flap_striker, ramp_slope | flap at -75.0°, still; touching ball1_sphere | ball2 at (2.20, 0.00, 0.07) m, at rest; touching cup_bottom
(the same through 6.00 s)

At the end (6.00 s):
- block at (0.38, 0.00, 0.35) m, at rest, turned 20° from how it started; touching wedge_cap
- wedge at (0.01, 0.00, 0.02) m, at rest, turned 20° from how it started; touching block_weight, floor, ramp_terrace
- ball1 at (1.26, 0.00, 0.14) m, at rest; touching flap_striker, ramp_slope
- flap at -75.0°, still; touching ball1_sphere
- ball2 at (2.20, 0.00, 0.07) m, at rest; touching cup_bottom
</history>
