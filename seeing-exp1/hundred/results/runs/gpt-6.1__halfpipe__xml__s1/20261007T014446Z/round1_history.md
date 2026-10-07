MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_sphere; starts at (-1.66, 0.00, 1.36) m, at rest
- block: free body; its geoms: block_striker; starts at (1.12, 0.00, 0.67) m, at rest
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), range -75° to 8° as MuJoCo applies it; its geoms: pendulum_rod, pendulum_bob; starts at 0.0°, still
- ball2: free body; its geoms: ball2_sphere; starts at (1.78, 0.00, 0.75) m, at rest

What happened, in order:
 0.00 s  ball2_sphere starts touching ball2_stand_top
 0.00 s  block_striker starts touching block_support_deck
 0.00 s  ball1_sphere first touches ramp_surface
 0.01 s  ball1 starts moving
 0.64 s  ball1_sphere leaves ramp_surface
 0.64 s  ball1_sphere first touches halfpipe_01
 0.68 s  ball1_sphere leaves halfpipe_01
 0.68 s  ball1_sphere first touches halfpipe_02
 0.71 s  ball1_sphere leaves halfpipe_02
 0.72 s  ball1_sphere first touches halfpipe_03
 0.75 s  ball1_sphere leaves halfpipe_03
 0.75 s  ball1_sphere first touches halfpipe_04
 0.78 s  ball1_sphere leaves halfpipe_04
 0.78 s  ball1_sphere first touches halfpipe_05
 0.81 s  ball1_sphere leaves halfpipe_05
 0.81 s  ball1_sphere first touches halfpipe_06
 0.84 s  ball1_sphere leaves halfpipe_06
 0.84 s  ball1_sphere first touches halfpipe_07
 0.86 s  ball1_sphere leaves halfpipe_07
 0.86 s  ball1_sphere first touches halfpipe_08
 0.89 s  ball1_sphere leaves halfpipe_08
 0.89 s  ball1_sphere first touches halfpipe_09
 0.91 s  ball1_sphere leaves halfpipe_09
 0.91 s  ball1_sphere first touches halfpipe_10
 0.93 s  ball1_sphere leaves halfpipe_10
 0.93 s  ball1_sphere first touches halfpipe_11
 0.96 s  ball1_sphere leaves halfpipe_11
 0.96 s  ball1_sphere first touches halfpipe_12
 0.98 s  ball1_sphere leaves halfpipe_12
 0.98 s  ball1_sphere first touches halfpipe_13
 1.00 s  ball1_sphere leaves halfpipe_13
 1.00 s  ball1_sphere first touches halfpipe_14
 1.03 s  ball1_sphere leaves halfpipe_14
 1.03 s  ball1_sphere first touches halfpipe_15
 1.06 s  ball1_sphere leaves halfpipe_15
 1.06 s  ball1_sphere first touches halfpipe_16
 1.09 s  ball1_sphere leaves halfpipe_16
 1.09 s  ball1_sphere first touches halfpipe_17
 1.12 s  ball1_sphere leaves halfpipe_17
 1.12 s  ball1_sphere first touches halfpipe_18
 1.15 s  ball1_sphere leaves halfpipe_18
 1.16 s  ball1_sphere first touches halfpipe_19
 1.19 s  ball1_sphere leaves halfpipe_19
 1.19 s  ball1_sphere first touches halfpipe_20
 1.23 s  ball1_sphere leaves halfpipe_20
 1.23 s  ball1_sphere first touches block_support_deck
 1.23 s  ball1_sphere leaves block_support_deck
 1.27 s  ball1_sphere first touches block_striker
 1.27 s  block starts moving
 1.27 s  ball1_sphere leaves block_striker
 1.41 s  block_striker leaves block_support_deck
 1.41 s  block_striker first touches pendulum_bob
 1.41 s  block_striker leaves pendulum_bob
 1.44 s  block_striker touches block_support_deck again
 1.47 s  block_striker touches pendulum_bob again
 1.47 s  block_striker leaves pendulum_bob
 1.48 s  ball1 is at the top of its flight, at (1.24, 0.00, 0.94) m
 1.63 s  ball1 passes 0.34 m from pendulum_support (pendulum_support_left) without touching it: nearest points (1.42, -0.07, 0.82) m and (1.42, -0.41, 0.82) m
 1.64 s  ball1_sphere touches block_striker again
 1.64 s  block passes 0.26 m from ball2_stand (ball2_stand_top) without touching it: nearest points (1.46, -0.12, 0.71) m and (1.72, -0.12, 0.70) m
 1.64 s  block passes 0.45 m from cup (cup_wall_09) without touching it: nearest points (1.46, -0.12, 0.60) m and (1.82, -0.12, 0.33) m
 1.64 s  ball1_sphere leaves block_striker
 1.65 s  block passes 0.49 m from hoop (hoop_08) without touching it: nearest points (1.46, 0.00, 0.60) m and (1.92, 0.00, 0.45) m
 1.74 s  ball1 passes -0.08 m from pendulum (pendulum_rod) without touching it: nearest points (1.64, 0.00, 0.91) m and (1.57, 0.00, 0.89) m
 1.78 s  ball1 is at the top of its flight, at (1.63, 0.00, 0.90) m
 1.86 s  ball1_sphere first touches ball2_sphere
 1.86 s  ball2 starts moving
 1.87 s  pendulum is at its smallest, -16.8°
 1.87 s  pendulum passes 0.00 m from ball2_stand (ball2_stand_top) without touching it: nearest points (1.72, 0.00, 0.70) m and (1.72, 0.00, 0.70) m
 1.87 s  pendulum passes 0.32 m from hoop (hoop_08) without touching it: nearest points (1.70, 0.00, 0.68) m and (1.93, 0.00, 0.45) m
 1.87 s  pendulum passes 0.36 m from cup (cup_wall_09) without touching it: nearest points (1.68, 0.00, 0.66) m and (1.82, 0.00, 0.33) m
 1.88 s  ball1_sphere leaves ball2_sphere
 1.89 s  pendulum_bob first touches ball2_sphere
 1.89 s  pendulum_bob leaves ball2_sphere
 1.90 s  ball1 is at the top of its flight, at (1.81, 0.00, 0.87) m
 1.99 s  ball1 passes 0.09 m from ball2_stand (ball2_stand_top) without touching it: nearest points (1.89, 0.00, 0.78) m and (1.84, 0.00, 0.70) m
 2.14 s  block_striker touches pendulum_bob again
 2.14 s  block_striker leaves pendulum_bob
 2.16 s  ball1 passes 0.15 m from hoop (hoop_08) without touching it: nearest points (2.10, 0.01, 0.52) m and (1.96, 0.04, 0.45) m
 2.30 s  ball1_sphere first touches cup_bottom
 2.31 s  ball1_sphere leaves cup_bottom
 2.37 s  ball1_sphere touches cup_bottom again
 2.44 s  block_striker touches pendulum_bob again
 2.45 s  ball2_sphere leaves ball2_stand_top
 2.45 s  block_striker leaves pendulum_bob
 2.59 s  block passes 0.23 m from ball2 (ball2_sphere) without touching it: nearest points (1.35, 0.00, 0.60) m and (1.58, 0.00, 0.57) m
 2.61 s  ball2_sphere first touches block_support_deck
 2.61 s  ball2_sphere leaves block_support_deck
 2.63 s  block_striker touches pendulum_bob 6 more times between 2.63 s and 2.94 s
 2.78 s  ball2_sphere first touches floor
 2.84 s  block comes to rest at (1.26, 0.00, 0.67) m
 2.85 s  ball2 comes to rest at (1.65, 0.00, 0.05) m
 2.94 s  ball1_sphere leaves cup_bottom
 2.94 s  ball1_sphere first touches cup_wall_01
 2.94 s  pendulum is at its largest, 1.5°
 2.95 s  ball1_sphere leaves cup_wall_01
 2.98 s  ball1_sphere touches cup_bottom again
 3.00 s  ball1 comes to rest at (3.06, 0.00, 0.12) m
 4.47 s  ball2_sphere first touches ball2_stand_column
 4.48 s  ball2 passes 0.05 m from cup (cup_bottom) without touching it: nearest points (1.75, 0.00, 0.05) m and (1.80, 0.00, 0.05) m
 4.52 s  ball2_sphere leaves ball2_stand_column

State every 0.25 s:
0.00 s: ball1 at (-1.66, 0.00, 1.36) m, at rest; touching nothing | block at (1.12, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at 0.0°, still; touching nothing | ball2 at (1.78, 0.00, 0.75) m, at rest; touching ball2_stand_top
0.25 s: ball1 at (-1.55, 0.00, 1.25) m, moving 1.24 m/s (vx +0.88, vy -0.00, vz -0.88); touching ramp_surface | block at (1.12, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at 0.0°, still; touching nothing | ball2 at (1.78, 0.00, 0.75) m, at rest; touching ball2_stand_top
0.50 s: ball1 at (-1.22, 0.00, 0.92) m, moving 2.48 m/s (vx +1.75, vy +0.00, vz -1.75); touching ramp_surface | block at (1.12, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at 0.0°, still; touching nothing | ball2 at (1.78, 0.00, 0.75) m, at rest; touching ball2_stand_top
0.75 s: ball1 at (-0.66, 0.00, 0.40) m, moving 3.65 m/s (vx +3.03, vy -0.00, vz -2.03); touching halfpipe_04 | block at (1.12, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at 0.0°, still; touching nothing | ball2 at (1.78, 0.00, 0.75) m, at rest; touching ball2_stand_top
1.00 s: ball1 at (0.27, 0.00, 0.21) m, moving 3.89 m/s (vx +3.77, vy +0.00, vz +0.96); touching halfpipe_13 | block at (1.12, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at 0.0°, still; touching nothing | ball2 at (1.78, 0.00, 0.75) m, at rest; touching ball2_stand_top
1.25 s: ball1 at (0.97, 0.00, 0.68) m, moving 2.71 m/s (vx +1.56, vy +0.00, vz +2.21); touching nothing | block at (1.12, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at 0.0°, still; touching nothing | ball2 at (1.78, 0.00, 0.75) m, at rest; touching ball2_stand_top
1.50 s: ball1 at (1.26, 0.00, 0.93) m, moving 1.19 m/s (vx +1.17, vy +0.00, vz -0.22); touching nothing | block at (1.33, 0.00, 0.67) m, moving 0.52 m/s (vx +0.52, vy -0.00, vz +0.02); touching block_support_deck | pendulum at -4.3°, turning -58°/s; touching nothing | ball2 at (1.78, 0.00, 0.75) m, at rest; touching ball2_stand_top
1.75 s: ball1 at (1.59, 0.00, 0.89) m, moving 1.49 m/s (vx +1.46, vy +0.00, vz +0.31); touching nothing | block at (1.39, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at -15.4°, turning -24°/s; touching nothing | ball2 at (1.78, 0.00, 0.75) m, at rest; touching ball2_stand_top
2.00 s: ball1 at (1.94, 0.00, 0.83) m, moving 1.66 m/s (vx +1.36, vy +0.00, vz -0.95); touching nothing | block at (1.39, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at -14.2°, turning +33°/s; touching nothing | ball2 at (1.76, 0.00, 0.75) m, moving 0.14 m/s (vx -0.14, vy -0.00, vz +0.00); touching ball2_stand_top
2.25 s: ball1 at (2.28, 0.00, 0.29) m, moving 3.67 m/s (vx +1.36, vy +0.00, vz -3.40); touching nothing | block at (1.36, 0.00, 0.67) m, moving 0.27 m/s (vx -0.27, vy +0.00, vz +0.00); touching block_support_deck | pendulum at -7.1°, turning +15°/s; touching nothing | ball2 at (1.72, 0.00, 0.75) m, moving 0.14 m/s (vx -0.14, vy -0.00, vz +0.00); touching ball2_stand_top
2.50 s: ball1 at (2.61, 0.00, 0.12) m, moving 1.24 m/s (vx +1.24, vy +0.00, vz -0.05); touching nothing | block at (1.31, 0.00, 0.67) m, moving 0.22 m/s (vx -0.22, vy +0.00, vz -0.01); touching block_support_deck | pendulum at -2.1°, turning +13°/s; touching nothing | ball2 at (1.66, 0.00, 0.69) m, moving 1.04 m/s (vx -0.38, vy -0.00, vz -0.97); touching nothing
2.75 s: ball1 at (2.89, 0.00, 0.12) m, moving 1.00 m/s (vx +1.00, vy +0.00, vz +0.01); touching cup_bottom | block at (1.27, 0.00, 0.67) m, moving 0.10 m/s (vx -0.09, vy +0.00, vz -0.01); touching block_support_deck | pendulum at 0.9°, turning +7°/s; touching nothing | ball2 at (1.64, 0.00, 0.15) m, moving 3.39 m/s (vx +0.18, vy -0.00, vz -3.38); touching nothing
3.00 s: ball1 at (3.05, 0.00, 0.12) m, at rest; touching cup_bottom | block at (1.26, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at 1.5°, turning -1°/s; touching nothing | ball2 at (1.66, 0.00, 0.05) m, at rest; touching floor
3.25 s: ball1 at (3.05, 0.00, 0.12) m, at rest; touching cup_bottom | block at (1.26, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at 0.6°, turning -5°/s; touching nothing | ball2 at (1.67, 0.00, 0.05) m, at rest; touching floor
3.50 s: ball1 at (3.05, 0.00, 0.12) m, at rest; touching cup_bottom | block at (1.26, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at -0.7°, turning -5°/s; touching nothing | ball2 at (1.67, 0.00, 0.05) m, at rest; touching floor
3.75 s: ball1 at (3.05, 0.00, 0.12) m, at rest; touching cup_bottom | block at (1.26, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at -1.5°, turning -1°/s; touching nothing | ball2 at (1.68, 0.00, 0.05) m, at rest; touching floor
4.00 s: ball1 at (3.05, 0.00, 0.12) m, at rest; touching cup_bottom | block at (1.26, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at -1.1°, turning +3°/s; touching nothing | ball2 at (1.69, 0.00, 0.05) m, at rest; touching floor
4.25 s: ball1 at (3.05, 0.00, 0.12) m, at rest; touching cup_bottom | block at (1.26, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at 0.0°, turning +5°/s; touching nothing | ball2 at (1.69, 0.00, 0.05) m, at rest; touching floor
4.50 s: ball1 at (3.05, 0.00, 0.12) m, at rest; touching cup_bottom | block at (1.26, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at 1.2°, turning +3°/s; touching nothing | ball2 at (1.70, 0.00, 0.05) m, at rest; touching ball2_stand_column, floor
4.75 s: ball1 at (3.05, 0.00, 0.12) m, at rest; touching cup_bottom | block at (1.26, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at 1.4°, turning -1°/s; touching nothing | ball2 at (1.69, 0.00, 0.05) m, at rest; touching floor
5.00 s: ball1 at (3.05, 0.00, 0.12) m, at rest; touching cup_bottom | block at (1.26, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at 0.6°, turning -5°/s; touching nothing | ball2 at (1.69, 0.00, 0.05) m, at rest; touching floor
5.25 s: ball1 at (3.05, 0.00, 0.12) m, at rest; touching cup_bottom | block at (1.26, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at -0.7°, turning -5°/s; touching nothing | ball2 at (1.69, 0.00, 0.05) m, at rest; touching floor
5.50 s: ball1 at (3.05, 0.00, 0.12) m, at rest; touching cup_bottom | block at (1.26, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at -1.4°, turning -1°/s; touching nothing | ball2 at (1.69, 0.00, 0.05) m, at rest; touching floor
5.75 s: ball1 at (3.05, 0.00, 0.12) m, at rest; touching cup_bottom | block at (1.26, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at -1.1°, turning +3°/s; touching nothing | ball2 at (1.69, 0.00, 0.05) m, at rest; touching floor
6.00 s: ball1 at (3.05, 0.00, 0.12) m, at rest; touching cup_bottom | block at (1.26, 0.00, 0.67) m, at rest; touching block_support_deck | pendulum at -0.0°, turning +5°/s; touching nothing | ball2 at (1.69, 0.00, 0.05) m, at rest; touching floor

At the end (6.00 s):
- ball1 at (3.05, 0.00, 0.12) m, at rest; touching cup_bottom
- block at (1.26, 0.00, 0.67) m, at rest; touching block_support_deck
- pendulum at -0.0°, turning +5°/s; touching nothing
- ball2 at (1.69, 0.00, 0.05) m, at rest; touching floor
</history>
