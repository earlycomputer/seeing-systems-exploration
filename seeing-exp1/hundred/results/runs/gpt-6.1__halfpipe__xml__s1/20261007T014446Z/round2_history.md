MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1_sphere; starts at (-1.66, 0.00, 1.36) m, at rest
- block: free body; its geoms: block_striker; starts at (1.12, 0.00, 0.71) m, at rest
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), range -75° to 8° as MuJoCo applies it; its geoms: pendulum_rod, pendulum_bob; starts at 0.0°, still
- ball2: free body; its geoms: ball2_sphere; starts at (1.66, 0.00, 0.71) m, at rest

What happened, in order:
 0.00 s  block_striker starts touching block_support_deck
 0.00 s  ball2_sphere starts touching ball2_stand_top
 0.00 s  pendulum is at its largest at the start, 0.0°
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
 1.39 s  block_striker first touches pendulum_bob
 1.39 s  block_striker leaves pendulum_bob
 1.42 s  ball1_sphere first touches ball1_backstop_wall
 1.42 s  ball1 passes 0.44 m from ball2 (ball2_sphere) without touching it: nearest points (1.22, 0.00, 0.90) m and (1.62, 0.00, 0.73) m
 1.43 s  ball1_sphere leaves ball1_backstop_wall
 1.49 s  ball2_sphere leaves ball2_stand_top
 1.49 s  pendulum_bob first touches ball2_sphere
 1.49 s  pendulum_bob leaves ball2_sphere
 1.49 s  ball2 starts moving
 1.49 s  block passes 0.19 m from ball2 (ball2_sphere) without touching it: nearest points (1.44, 0.00, 0.71) m and (1.63, 0.00, 0.71) m
 1.51 s  ball2 is at the top of its flight, at (1.69, 0.00, 0.71) m
 1.55 s  ball1 is at the top of its flight, at (1.15, 0.00, 1.00) m
 1.55 s  pendulum_bob first touches ball2_stand_top
 1.57 s  block passes 0.14 m from ball2_stand (ball2_stand_top) without touching it: nearest points (1.50, -0.10, 0.67) m and (1.65, -0.10, 0.67) m
 1.57 s  block passes 0.33 m from cup (cup_wall_10) without touching it: nearest points (1.50, -0.12, 0.60) m and (1.58, -0.12, 0.28) m
 1.57 s  block passes 0.28 m from hoop (hoop_09) without touching it: nearest points (1.50, 0.00, 0.60) m and (1.69, 0.00, 0.39) m
 1.57 s  block_striker touches pendulum_bob again
 1.57 s  pendulum is at its smallest, -12.2°
 1.58 s  block_striker leaves pendulum_bob
 1.59 s  pendulum_bob leaves ball2_stand_top
 1.79 s  block_striker touches pendulum_bob again
 1.79 s  block_striker leaves pendulum_bob
 1.81 s  ball1_sphere touches block_support_deck again
 1.86 s  ball2_sphere first touches cup_bottom
 1.88 s  ball2_sphere leaves cup_bottom
 1.88 s  block_striker touches pendulum_bob again
 1.88 s  block_striker leaves pendulum_bob
 1.96 s  ball2_sphere touches cup_bottom again
 1.99 s  block_striker touches pendulum_bob 10 more times between 1.99 s and 6.00 s, still touching at the end
 2.08 s  ball1_sphere touches block_striker again
 2.08 s  ball1_sphere leaves block_striker
 2.33 s  pendulum_bob touches ball2_stand_top again
 2.34 s  pendulum_bob leaves ball2_stand_top
 2.36 s  ball2 comes to rest at (2.40, 0.00, 0.09) m
 2.61 s  ball1_sphere touches block_striker again
 2.61 s  ball1 passes 0.12 m from pendulum (pendulum_bob) without touching it: nearest points (1.29, 0.00, 0.68) m and (1.42, 0.00, 0.69) m
 2.61 s  ball1 passes 0.38 m from pendulum_support (pendulum_support_right) without touching it: nearest points (1.25, 0.06, 0.67) m and (1.41, 0.41, 0.67) m
 2.61 s  ball1 passes 0.35 m from ball2_stand (ball2_stand_top) without touching it: nearest points (1.29, 0.00, 0.67) m and (1.65, 0.00, 0.67) m
 2.61 s  ball1 passes 0.46 m from cup (cup_wall_09) without touching it: nearest points (1.27, 0.00, 0.62) m and (1.58, 0.00, 0.28) m
 2.61 s  ball1 passes 0.47 m from hoop (hoop_08) without touching it: nearest points (1.28, 0.00, 0.63) m and (1.69, 0.00, 0.39) m
 2.62 s  ball1_sphere leaves block_striker
 2.77 s  pendulum_bob touches ball2_stand_top again
 2.79 s  pendulum_bob leaves ball2_stand_top
 2.96 s  pendulum_bob touches ball2_stand_top again
 2.97 s  pendulum_bob leaves ball2_stand_top
 3.27 s  block comes to rest at (1.41, 0.00, 0.71) m
 6.00 s  ball1 is still moving at the end, 0.05 m/s

State every 0.25 s:
0.00 s: ball1 at (-1.66, 0.00, 1.36) m, at rest; touching nothing | block at (1.12, 0.00, 0.71) m, at rest; touching block_support_deck | pendulum at 0.0°, still; touching nothing | ball2 at (1.66, 0.00, 0.71) m, at rest; touching ball2_stand_top
0.25 s: ball1 at (-1.55, 0.00, 1.25) m, moving 1.24 m/s (vx +0.88, vy -0.00, vz -0.88); touching ramp_surface | block at (1.12, 0.00, 0.71) m, at rest; touching block_support_deck | pendulum at 0.0°, still; touching nothing | ball2 at (1.66, 0.00, 0.71) m, at rest; touching ball2_stand_top
0.50 s: ball1 at (-1.22, 0.00, 0.92) m, moving 2.48 m/s (vx +1.75, vy +0.00, vz -1.75); touching ramp_surface | block at (1.12, 0.00, 0.71) m, at rest; touching block_support_deck | pendulum at 0.0°, still; touching nothing | ball2 at (1.66, 0.00, 0.71) m, at rest; touching ball2_stand_top
0.75 s: ball1 at (-0.66, 0.00, 0.40) m, moving 3.65 m/s (vx +3.03, vy -0.00, vz -2.03); touching halfpipe_04 | block at (1.12, 0.00, 0.71) m, at rest; touching block_support_deck | pendulum at 0.0°, still; touching nothing | ball2 at (1.66, 0.00, 0.71) m, at rest; touching ball2_stand_top
1.00 s: ball1 at (0.27, 0.00, 0.21) m, moving 3.89 m/s (vx +3.77, vy +0.00, vz +0.96); touching halfpipe_13 | block at (1.12, 0.00, 0.71) m, at rest; touching block_support_deck | pendulum at 0.0°, still; touching nothing | ball2 at (1.66, 0.00, 0.71) m, at rest; touching ball2_stand_top
1.25 s: ball1 at (0.97, 0.00, 0.68) m, moving 2.71 m/s (vx +1.56, vy +0.00, vz +2.21); touching nothing | block at (1.12, 0.00, 0.71) m, at rest; touching block_support_deck | pendulum at 0.0°, still; touching nothing | ball2 at (1.66, 0.00, 0.71) m, at rest; touching ball2_stand_top
1.50 s: ball1 at (1.15, 0.00, 0.99) m, moving 0.45 m/s (vx -0.09, vy -0.00, vz +0.44); touching nothing | block at (1.38, 0.00, 0.71) m, moving 0.87 m/s (vx +0.87, vy -0.00, vz +0.03); touching nothing | pendulum at -9.7°, turning -56°/s; touching nothing | ball2 at (1.68, 0.00, 0.71) m, moving 1.41 m/s (vx +1.41, vy -0.00, vz +0.06); touching nothing
1.75 s: ball1 at (1.13, 0.00, 0.80) m, moving 2.01 m/s (vx -0.09, vy -0.00, vz -2.01); touching nothing | block at (1.39, 0.00, 0.71) m, moving 0.28 m/s (vx -0.28, vy +0.00, vz +0.00); touching block_support_deck | pendulum at -8.3°, turning +33°/s; touching nothing | ball2 at (2.03, 0.00, 0.42) m, moving 2.78 m/s (vx +1.41, vy -0.00, vz -2.40); touching nothing
2.00 s: ball1 at (1.15, 0.00, 0.67) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz +0.00); touching block_support_deck | block at (1.32, 0.00, 0.71) m, moving 0.23 m/s (vx -0.23, vy +0.00, vz -0.01); touching nothing | pendulum at -2.8°, turning +16°/s; touching nothing | ball2 at (2.28, 0.00, 0.09) m, moving 0.65 m/s (vx +0.63, vy -0.00, vz -0.14); touching nothing
2.25 s: ball1 at (1.19, 0.00, 0.67) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz +0.00); touching block_support_deck | block at (1.34, 0.00, 0.71) m, moving 0.15 m/s (vx +0.15, vy -0.00, vz +0.01); touching block_support_deck | pendulum at -9.7°, turning -39°/s; touching nothing | ball2 at (2.39, 0.00, 0.09) m, moving 0.22 m/s (vx +0.21, vy -0.00, vz -0.02); touching nothing
2.50 s: ball1 at (1.21, 0.00, 0.67) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz -0.00); touching block_support_deck | block at (1.35, 0.00, 0.71) m, at rest; touching block_support_deck | pendulum at -9.2°, turning +28°/s; touching nothing | ball2 at (2.40, 0.00, 0.09) m, at rest; touching cup_bottom
2.75 s: ball1 at (1.21, 0.00, 0.67) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz +0.00); touching block_support_deck | block at (1.39, 0.00, 0.71) m, moving 0.25 m/s (vx +0.25, vy +0.00, vz +0.00); touching block_support_deck | pendulum at -11.5°, turning -36°/s; touching nothing | ball2 at (2.40, 0.00, 0.09) m, at rest; touching cup_bottom
3.00 s: ball1 at (1.20, 0.00, 0.67) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz -0.00); touching block_support_deck | block at (1.42, 0.00, 0.71) m, at rest; touching block_support_deck | pendulum at -11.9°, turning +8°/s; touching nothing | ball2 at (2.40, 0.00, 0.09) m, at rest; touching cup_bottom
3.25 s: ball1 at (1.19, 0.00, 0.67) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz -0.00); touching block_support_deck | block at (1.41, 0.00, 0.71) m, at rest; touching block_support_deck | pendulum at -9.9°, turning +5°/s; touching nothing | ball2 at (2.40, 0.00, 0.09) m, at rest; touching cup_bottom
3.50 s: ball1 at (1.17, 0.00, 0.67) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz +0.00); touching block_support_deck | block at (1.41, 0.00, 0.71) m, at rest; touching block_support_deck | pendulum at -9.5°, turning +1°/s; touching nothing | ball2 at (2.40, 0.00, 0.09) m, at rest; touching cup_bottom
3.75 s: ball1 at (1.16, 0.00, 0.67) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz +0.00); touching block_support_deck | block at (1.41, 0.00, 0.71) m, at rest; touching block_support_deck | pendulum at -9.5°, still; touching nothing | ball2 at (2.40, 0.00, 0.09) m, at rest; touching cup_bottom
4.00 s: ball1 at (1.15, 0.00, 0.67) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz +0.00); touching block_support_deck | block at (1.41, 0.00, 0.71) m, at rest; touching block_support_deck, pendulum_bob | pendulum at -9.5°, still; touching block_striker | ball2 at (2.40, 0.00, 0.09) m, at rest; touching cup_bottom
4.25 s: ball1 at (1.13, 0.00, 0.67) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz -0.00); touching block_support_deck | block at (1.41, 0.00, 0.71) m, at rest; touching block_support_deck, pendulum_bob | pendulum at -9.5°, still; touching block_striker | ball2 at (2.40, 0.00, 0.09) m, at rest; touching cup_bottom
4.50 s: ball1 at (1.12, 0.00, 0.67) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz -0.00); touching block_support_deck | block at (1.41, 0.00, 0.71) m, at rest; touching block_support_deck, pendulum_bob | pendulum at -9.5°, still; touching block_striker | ball2 at (2.40, 0.00, 0.09) m, at rest; touching cup_bottom
4.75 s: ball1 at (1.11, 0.00, 0.67) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz -0.00); touching block_support_deck | block at (1.41, 0.00, 0.71) m, at rest; touching block_support_deck, pendulum_bob | pendulum at -9.4°, still; touching block_striker | ball2 at (2.40, 0.00, 0.09) m, at rest; touching cup_bottom
5.00 s: ball1 at (1.10, 0.00, 0.67) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz -0.00); touching block_support_deck | block at (1.41, 0.00, 0.71) m, at rest; touching block_support_deck | pendulum at -9.4°, still; touching nothing | ball2 at (2.40, 0.00, 0.09) m, at rest; touching cup_bottom
5.25 s: ball1 at (1.08, 0.00, 0.67) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz -0.00); touching block_support_deck | block at (1.41, 0.00, 0.71) m, at rest; touching block_support_deck | pendulum at -9.4°, still; touching nothing | ball2 at (2.40, 0.00, 0.09) m, at rest; touching cup_bottom
5.50 s: ball1 at (1.07, 0.00, 0.67) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz -0.00); touching block_support_deck | block at (1.41, 0.00, 0.71) m, at rest; touching block_support_deck | pendulum at -9.4°, still; touching nothing | ball2 at (2.40, 0.00, 0.09) m, at rest; touching cup_bottom
5.75 s: ball1 at (1.06, 0.00, 0.67) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz +0.00); touching block_support_deck | block at (1.41, 0.00, 0.71) m, at rest; touching block_support_deck | pendulum at -9.4°, still; touching nothing | ball2 at (2.40, 0.00, 0.09) m, at rest; touching cup_bottom
6.00 s: ball1 at (1.04, 0.00, 0.67) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz -0.00); touching block_support_deck | block at (1.41, 0.00, 0.71) m, at rest; touching block_support_deck, pendulum_bob | pendulum at -9.4°, still; touching block_striker | ball2 at (2.40, 0.00, 0.09) m, at rest; touching cup_bottom

At the end (6.00 s):
- ball1 at (1.04, 0.00, 0.67) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz -0.00); touching block_support_deck
- block at (1.41, 0.00, 0.71) m, at rest; touching block_support_deck, pendulum_bob
- pendulum at -9.4°, still; touching block_striker
- ball2 at (2.40, 0.00, 0.09) m, at rest; touching cup_bottom
</history>
