MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_sphere; starts at (-1.79, 0.00, 1.52) m, at rest
- balance: hinge joint balance_hinge about axis (0.00, 1.00, 0.00), range -20.0535° to 0° as MuJoCo applies it; its geoms: balance_left_arm, balance_right_arm, balance_recess_floor, balance_recess_back, balance_recess_front, balance_recess_near, balance_recess_far, balance_striker_tray, balance_tray_inner_lip, balance_tray_near_lip, balance_tray_far_lip, balance_bias_weight; starts at 0.0°, still
- block: free body; its geoms: block_striker; starts at (0.70, 0.00, 0.47) m, at rest
- ball2: free body; its geoms: ball2_sphere; starts at (0.98, 0.00, 0.95) m, at rest

What happened, in order:
 0.00 s  balance_striker_tray starts touching block_striker
 0.00 s  balance starts at its upper stop (0°)
 0.00 s  balance is at its largest, 0.0°
 0.00 s  ball1_sphere first touches ramp_deck
 0.01 s  ball2 starts moving
 0.03 s  ball1 starts moving
 0.04 s  ball2_sphere first touches ball2_support_near_left
 0.04 s  ball2_sphere first touches ball2_support_far_right
 0.04 s  ball2_sphere first touches ball2_support_far_left
 0.04 s  ball2_sphere first touches ball2_support_near_right
 1.00 s  ball1_sphere leaves ramp_deck
 1.15 s  ball1_sphere first touches balance_left_arm
 1.15 s  block starts moving
 1.15 s  ball1_sphere first touches balance_recess_floor
 1.19 s  ball1_sphere leaves balance_recess_floor
 1.19 s  ball1_sphere first touches balance_recess_front
 1.20 s  ball1_sphere leaves balance_left_arm
 1.20 s  ball1 passes 0.45 m from fulcrum (fulcrum_post) without touching it: nearest points (-0.50, 0.00, 1.02) m and (-0.06, 0.00, 0.96) m
 1.22 s  ball1_sphere leaves balance_recess_front
 1.27 s  balance reaches its lower stop (-20.0535°) moving -153°/s
 1.28 s  balance is at its smallest, -20.2°
 1.28 s  balance_striker_tray leaves block_striker
 1.28 s  balance passes 0.15 m from ball2 (ball2_sphere) without touching it: nearest points (0.95, -0.06, 0.75) m and (0.97, -0.02, 0.88) m
 1.28 s  balance passes 0.14 m from ball2_support (ball2_support_near_left) without touching it: nearest points (0.95, -0.06, 0.75) m and (0.98, -0.06, 0.88) m
 1.29 s  ball1_sphere touches balance_left_arm again
 1.30 s  ball1_sphere touches balance_recess_floor again
 1.33 s  ball1_sphere leaves balance_recess_floor
 1.35 s  ball2_sphere leaves ball2_support_near_left
 1.35 s  ball2_sphere leaves ball2_support_far_right
 1.35 s  ball2_sphere leaves ball2_support_far_left
 1.35 s  ball2_sphere leaves ball2_support_near_right
 1.35 s  block_striker first touches ball2_sphere
 1.38 s  block_striker leaves ball2_sphere
 1.40 s  ball2_sphere touches ball2_support_far_right again
 1.40 s  ball2_sphere touches ball2_support_near_right again
 1.42 s  block is at the top of its flight, at (0.89, 0.00, 0.90) m
 1.44 s  ball1_sphere leaves balance_left_arm
 1.47 s  ball1_sphere touches balance_recess_floor again
 1.49 s  block passes 0.01 m from ball2_support (ball2_support_near_left) without touching it: nearest points (0.92, -0.03, 0.91) m and (0.92, -0.05, 0.91) m
 1.50 s  ball1_sphere first touches balance_recess_back
 1.50 s  ball1_sphere leaves balance_recess_floor
 1.53 s  ball1_sphere leaves balance_recess_back
 1.57 s  ball1_sphere touches balance_recess_back again
 1.58 s  ball1_sphere leaves balance_recess_back
 1.59 s  balance_striker_tray touches block_striker again
 1.59 s  ball1_sphere touches balance_recess_floor again
 1.65 s  ball1_sphere touches balance_recess_back again
 1.65 s  ball1 comes to rest at (-0.80, 0.00, 0.82) m
 1.74 s  block comes to rest at (0.91, 0.00, 0.76) m
 1.95 s  ball2_sphere touches ball2_support_near_left again
 1.95 s  ball2_sphere touches ball2_support_far_left again
 1.96 s  ball2 comes to rest at (0.98, 0.00, 0.94) m
 1.96 s  ball2_sphere leaves ball2_support_far_right
 1.96 s  ball2_sphere leaves ball2_support_near_right
 2.00 s  ball2_sphere touches ball2_support_far_right again
 2.00 s  ball2_sphere touches ball2_support_near_right again

State every 0.25 s:
0.00 s: ball1 at (-1.79, 0.00, 1.52) m, at rest; touching nothing | balance at 0.0°, still; touching block_striker | block at (0.70, 0.00, 0.47) m, at rest; touching balance_striker_tray | ball2 at (0.98, 0.00, 0.95) m, at rest; touching nothing
0.25 s: ball1 at (-1.73, 0.00, 1.50) m, moving 0.45 m/s (vx +0.44, vy +0.00, vz -0.12); touching ramp_deck | balance at 0.0°, still; touching block_striker | block at (0.70, 0.00, 0.46) m, at rest; touching balance_striker_tray | ball2 at (0.98, 0.00, 0.94) m, at rest; touching ball2_support_far_left, ball2_support_far_right, ball2_support_near_left, ball2_support_near_right
0.50 s: ball1 at (-1.57, 0.00, 1.46) m, moving 0.90 m/s (vx +0.87, vy +0.00, vz -0.23); touching ramp_deck | balance at 0.0°, still; touching block_striker | block at (0.70, 0.00, 0.46) m, at rest; touching balance_striker_tray | ball2 at (0.98, 0.00, 0.94) m, at rest; touching ball2_support_far_left, ball2_support_far_right, ball2_support_near_left, ball2_support_near_right
0.75 s: ball1 at (-1.30, 0.00, 1.38) m, moving 1.35 m/s (vx +1.31, vy +0.00, vz -0.35); touching ramp_deck | balance at 0.0°, still; touching block_striker | block at (0.70, 0.00, 0.46) m, at rest; touching balance_striker_tray | ball2 at (0.98, 0.00, 0.94) m, at rest; touching ball2_support_far_left, ball2_support_far_right, ball2_support_near_left, ball2_support_near_right
1.00 s: ball1 at (-0.92, 0.00, 1.28) m, moving 1.80 m/s (vx +1.74, vy +0.00, vz -0.47); touching ramp_deck | balance at 0.0°, still; touching block_striker | block at (0.70, 0.00, 0.46) m, at rest; touching balance_striker_tray | ball2 at (0.98, 0.00, 0.94) m, at rest; touching ball2_support_far_left, ball2_support_far_right, ball2_support_near_left, ball2_support_near_right
1.25 s: ball1 at (-0.60, 0.00, 0.97) m, moving 1.70 m/s (vx -0.38, vy +0.00, vz -1.65); touching nothing | balance at -15.8°, turning -159°/s; touching block_striker | block at (0.82, 0.00, 0.67) m, moving 2.46 m/s (vx +0.92, vy +0.00, vz +2.28), turned 16° from how it started; touching balance_striker_tray | ball2 at (0.98, 0.00, 0.94) m, at rest; touching ball2_support_far_left, ball2_support_far_right, ball2_support_near_left, ball2_support_near_right
1.50 s: ball1 at (-0.79, 0.00, 0.82) m, moving 1.13 m/s (vx -1.08, vy +0.00, vz -0.35); touching balance_recess_floor | balance at -20.1°, still; touching ball1_sphere | block at (0.90, 0.00, 0.87) m, moving 0.75 m/s (vx +0.01, vy -0.00, vz -0.75), turned 30° from how it started; touching nothing | ball2 at (1.00, 0.00, 0.95) m, at rest; touching ball2_support_far_right, ball2_support_near_right
1.75 s: ball1 at (-0.80, 0.00, 0.82) m, at rest; touching balance_recess_back, balance_recess_floor | balance at -20.1°, still; touching ball1_sphere, block_striker | block at (0.91, 0.00, 0.76) m, at rest, turned 20° from how it started; touching balance_striker_tray | ball2 at (0.99, 0.00, 0.95) m, moving 0.06 m/s (vx -0.05, vy -0.00, vz -0.02); touching ball2_support_far_right, ball2_support_near_right
2.00 s: ball1 at (-0.80, 0.00, 0.82) m, at rest; touching balance_recess_back, balance_recess_floor | balance at -20.1°, still; touching ball1_sphere, block_striker | block at (0.91, 0.00, 0.76) m, at rest, turned 20° from how it started; touching balance_striker_tray | ball2 at (0.98, 0.00, 0.94) m, at rest; touching ball2_support_far_left, ball2_support_far_right, ball2_support_near_left, ball2_support_near_right
(the same through 6.00 s)

At the end (6.00 s):
- ball1 at (-0.80, 0.00, 0.82) m, at rest; touching balance_recess_back, balance_recess_floor
- balance at -20.1°, still; touching ball1_sphere, block_striker
- block at (0.91, 0.00, 0.76) m, at rest, turned 20° from how it started; touching balance_striker_tray
- ball2 at (0.98, 0.00, 0.94) m, at rest; touching ball2_support_far_left, ball2_support_far_right, ball2_support_near_left, ball2_support_near_right
</history>
