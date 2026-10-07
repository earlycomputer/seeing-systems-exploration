MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_arm, pendulum_bob; starts at 90.0°, still
- ball1: free body; its geoms: ball1_geom; starts at (0.00, 0.00, 0.24) m, at rest
- ball2: free body; its geoms: ball2_geom; starts at (0.15, 0.00, 0.24) m, at rest
- ball3: free body; its geoms: ball3_geom; starts at (0.30, 0.00, 0.24) m, at rest
- ball4: free body; its geoms: ball4_geom; starts at (0.45, 0.00, 0.24) m, at rest

What happened, in order:
 0.00 s  ball2_geom starts touching rail_base
 0.00 s  ball3_geom starts touching rail_base
 0.00 s  ball4_geom starts touching rail_base
 0.00 s  ball1_geom starts touching rail_base
 0.00 s  pendulum is at its largest at the start, 90.0°
 0.42 s  pendulum_bob first touches ball1_geom
 0.42 s  ball1 starts moving
 0.43 s  pendulum_bob leaves ball1_geom
 0.45 s  pendulum passes 0.12 m from ball2 (ball2_geom) without touching it: nearest points (-0.01, 0.00, 0.24) m and (0.11, 0.00, 0.24) m
 0.45 s  ball1_geom first touches ball2_geom
 0.45 s  ball2 starts moving
 0.47 s  ball1_geom leaves ball2_geom
 0.48 s  pendulum passes 0.27 m from ball3 (ball3_geom) without touching it: nearest points (-0.01, 0.00, 0.24) m and (0.26, 0.00, 0.24) m
 0.49 s  ball2_geom first touches ball3_geom
 0.49 s  ball3 starts moving
 0.49 s  pendulum passes 0.00 m from rail (rail_base) without touching it: nearest points (-0.04, 0.00, 0.20) m and (-0.04, 0.00, 0.20) m
 0.50 s  ball2_geom leaves ball3_geom
 0.52 s  ball3_geom first touches ball4_geom
 0.52 s  ball4 starts moving
 0.52 s  ball1 passes 0.27 m from ball4 (ball4_geom) without touching it: nearest points (0.14, 0.00, 0.24) m and (0.41, 0.00, 0.24) m
 0.52 s  pendulum passes 0.41 m from ball4 (ball4_geom) without touching it: nearest points (0.00, 0.00, 0.24) m and (0.41, 0.00, 0.24) m
 0.53 s  ball3_geom leaves ball4_geom
 0.55 s  ball4_geom leaves rail_base
 0.75 s  ball4_geom first touches box_floor
 0.75 s  ball4_geom leaves box_floor
 0.82 s  ball4_geom touches box_floor again
 0.83 s  ball4_geom leaves box_floor
 0.88 s  ball4_geom touches box_floor again
 0.88 s  ball4_geom leaves box_floor
 0.92 s  ball4_geom touches box_floor again
 0.94 s  ball4_geom leaves box_floor
 0.94 s  ball4_geom first touches box_wall_far
 0.95 s  ball4_geom leaves box_wall_far
 0.97 s  ball4_geom touches box_floor 1 more times between 0.97 s and 6.00 s, still touching at the end
 0.98 s  ball4 comes to rest at (1.23, 0.00, 0.05) m
 1.19 s  ball3_geom leaves rail_base
 1.29 s  ball3_geom first touches box_wall_near
 1.29 s  ball3_geom leaves box_wall_near
 1.33 s  ball1_geom touches ball2_geom again
 1.34 s  ball1_geom leaves ball2_geom
 1.37 s  ball3_geom first touches box_floor
 1.38 s  ball3_geom leaves box_floor
 1.42 s  ball3_geom touches box_floor again
 2.04 s  ball2_geom leaves rail_base
 2.11 s  pendulum is at its smallest, -6.8°
 2.15 s  ball2_geom first touches box_wall_near
 2.15 s  ball2_geom leaves box_wall_near
 2.22 s  ball2_geom touches ball3_geom again
 2.24 s  ball2_geom leaves ball3_geom
 2.25 s  ball2_geom first touches box_floor
 2.69 s  ball3 comes to rest at (0.87, 0.00, 0.05) m
 2.85 s  ball1_geom leaves rail_base
 2.95 s  ball1_geom first touches box_wall_near
 2.96 s  ball1_geom leaves box_wall_near
 2.98 s  ball1_geom touches ball2_geom again
 3.00 s  ball1_geom leaves ball2_geom
 3.10 s  ball1 is at the top of its flight, at (0.59, 0.00, 0.18) m
 3.20 s  ball1_geom touches ball2_geom again
 3.21 s  ball1_geom leaves ball2_geom
 3.27 s  ball1_geom touches box_wall_near again
 3.28 s  ball1_geom leaves box_wall_near
 3.39 s  ball2 comes to rest at (0.66, 0.00, 0.05) m
 3.40 s  ball1_geom first touches box_floor
 3.42 s  ball1 comes to rest at (0.58, 0.00, 0.05) m

State every 0.25 s:
0.00 s: pendulum at 90.0°, still; touching nothing | ball1 at (0.00, 0.00, 0.24) m, at rest; touching rail_base | ball2 at (0.15, 0.00, 0.24) m, at rest; touching rail_base | ball3 at (0.30, 0.00, 0.24) m, at rest; touching rail_base | ball4 at (0.45, 0.00, 0.24) m, at rest; touching rail_base
0.25 s: pendulum at 55.1°, turning -271°/s; touching nothing | ball1 at (0.00, 0.00, 0.24) m, at rest; touching rail_base | ball2 at (0.15, 0.00, 0.24) m, at rest; touching rail_base | ball3 at (0.30, 0.00, 0.24) m, at rest; touching rail_base | ball4 at (0.45, 0.00, 0.24) m, at rest; touching rail_base
0.50 s: pendulum at -4.5°, turning -23°/s; touching nothing | ball1 at (0.10, 0.00, 0.24) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz -0.00); touching rail_base | ball2 at (0.24, 0.00, 0.24) m, moving 0.15 m/s (vx +0.15, vy +0.00, vz -0.00); touching rail_base | ball3 at (0.32, 0.00, 0.24) m, moving 2.53 m/s (vx +2.53, vy -0.00, vz -0.00); touching rail_base | ball4 at (0.45, 0.00, 0.24) m, at rest; touching rail_base
0.75 s: pendulum at -6.6°, turning +7°/s; touching nothing | ball1 at (0.16, 0.00, 0.24) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz -0.00); touching rail_base | ball2 at (0.28, 0.00, 0.24) m, moving 0.15 m/s (vx +0.15, vy +0.00, vz +0.00); touching rail_base | ball3 at (0.43, 0.00, 0.24) m, moving 0.20 m/s (vx +0.20, vy -0.00, vz +0.00); touching rail_base | ball4 at (0.97, 0.00, 0.05) m, moving 1.51 m/s (vx +1.47, vy +0.00, vz +0.36); touching box_floor
1.00 s: pendulum at -1.5°, turning +29°/s; touching nothing | ball1 at (0.21, 0.00, 0.24) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz +0.00); touching rail_base | ball2 at (0.31, 0.00, 0.24) m, moving 0.15 m/s (vx +0.15, vy +0.00, vz +0.00); touching rail_base | ball3 at (0.48, 0.00, 0.24) m, moving 0.20 m/s (vx +0.20, vy -0.00, vz +0.00); touching rail_base | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
1.25 s: pendulum at 5.3°, turning +19°/s; touching nothing | ball1 at (0.27, 0.00, 0.24) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz -0.00); touching rail_base | ball2 at (0.35, 0.00, 0.24) m, moving 0.15 m/s (vx +0.15, vy +0.00, vz -0.00); touching rail_base | ball3 at (0.55, 0.00, 0.19) m, moving 1.01 m/s (vx +0.38, vy -0.00, vz -0.94); touching nothing | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
1.50 s: pendulum at 6.2°, turning -12°/s; touching nothing | ball1 at (0.31, 0.00, 0.24) m, moving 0.15 m/s (vx +0.15, vy -0.00, vz -0.00); touching rail_base | ball2 at (0.40, 0.00, 0.24) m, moving 0.22 m/s (vx +0.22, vy +0.00, vz +0.00); touching rail_base | ball3 at (0.66, 0.00, 0.05) m, moving 0.27 m/s (vx +0.27, vy +0.00, vz -0.04); touching nothing | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
1.75 s: pendulum at 0.3°, turning -30°/s; touching nothing | ball1 at (0.35, 0.00, 0.24) m, moving 0.15 m/s (vx +0.15, vy -0.00, vz +0.00); touching rail_base | ball2 at (0.45, 0.00, 0.24) m, moving 0.22 m/s (vx +0.22, vy -0.00, vz +0.00); touching rail_base | ball3 at (0.68, 0.00, 0.05) m, at rest; touching box_floor | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
2.00 s: pendulum at -6.0°, turning -15°/s; touching nothing | ball1 at (0.39, 0.00, 0.24) m, moving 0.15 m/s (vx +0.15, vy -0.00, vz -0.00); touching rail_base | ball2 at (0.51, 0.00, 0.24) m, moving 0.26 m/s (vx +0.25, vy -0.00, vz -0.07); touching rail_base | ball3 at (0.68, 0.00, 0.05) m, at rest; touching box_floor | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
2.25 s: pendulum at -5.6°, turning +17°/s; touching nothing | ball1 at (0.43, 0.00, 0.24) m, moving 0.15 m/s (vx +0.15, vy -0.00, vz -0.00); touching rail_base | ball2 at (0.60, 0.00, 0.05) m, moving 0.10 m/s (vx -0.07, vy -0.00, vz +0.08); touching box_floor | ball3 at (0.70, 0.00, 0.05) m, moving 0.75 m/s (vx +0.75, vy +0.00, vz -0.02); touching nothing | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
2.50 s: pendulum at 0.9°, turning +30°/s; touching nothing | ball1 at (0.46, 0.00, 0.24) m, moving 0.15 m/s (vx +0.15, vy -0.00, vz -0.00); touching rail_base | ball2 at (0.60, 0.00, 0.05) m, at rest; touching box_floor | ball3 at (0.83, 0.00, 0.05) m, moving 0.34 m/s (vx +0.34, vy +0.00, vz +0.01); touching nothing | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
2.75 s: pendulum at 6.4°, turning +10°/s; touching nothing | ball1 at (0.50, 0.00, 0.24) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz -0.01); touching rail_base | ball2 at (0.60, 0.00, 0.05) m, at rest; touching box_floor | ball3 at (0.87, 0.00, 0.05) m, at rest; touching box_floor | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
3.00 s: pendulum at 4.8°, turning -21°/s; touching nothing | ball1 at (0.59, 0.00, 0.13) m, moving 0.94 m/s (vx +0.08, vy +0.00, vz +0.93); touching nothing | ball2 at (0.61, 0.00, 0.05) m, moving 0.26 m/s (vx +0.25, vy -0.00, vz +0.02); touching nothing | ball3 at (0.87, 0.00, 0.05) m, at rest; touching box_floor | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
3.25 s: pendulum at -2.1°, turning -29°/s; touching nothing | ball1 at (0.58, 0.00, 0.14) m, moving 0.57 m/s (vx -0.54, vy +0.00, vz +0.20); touching nothing | ball2 at (0.64, 0.00, 0.05) m, moving 0.26 m/s (vx +0.26, vy -0.00, vz +0.02); touching box_floor | ball3 at (0.87, 0.00, 0.05) m, at rest; touching box_floor | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
3.50 s: pendulum at -6.7°, turning -5°/s; touching nothing | ball1 at (0.58, 0.00, 0.05) m, at rest; touching box_floor | ball2 at (0.66, 0.00, 0.05) m, at rest; touching box_floor | ball3 at (0.87, 0.00, 0.05) m, at rest; touching box_floor | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
3.75 s: pendulum at -3.9°, turning +24°/s; touching nothing | ball1 at (0.58, 0.00, 0.05) m, at rest; touching box_floor | ball2 at (0.66, 0.00, 0.05) m, at rest; touching box_floor | ball3 at (0.87, 0.00, 0.05) m, at rest; touching box_floor | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
4.00 s: pendulum at 3.2°, turning +27°/s; touching nothing | ball1 at (0.58, 0.00, 0.05) m, at rest; touching box_floor | ball2 at (0.66, 0.00, 0.05) m, at rest; touching box_floor | ball3 at (0.87, 0.00, 0.05) m, at rest; touching box_floor | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
4.25 s: pendulum at 6.8°, still; touching nothing | ball1 at (0.58, 0.00, 0.05) m, at rest; touching box_floor | ball2 at (0.66, 0.00, 0.05) m, at rest; touching box_floor | ball3 at (0.87, 0.00, 0.05) m, at rest; touching box_floor | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
4.50 s: pendulum at 2.9°, turning -27°/s; touching nothing | ball1 at (0.58, 0.00, 0.05) m, at rest; touching box_floor | ball2 at (0.66, 0.00, 0.05) m, at rest; touching box_floor | ball3 at (0.87, 0.00, 0.05) m, at rest; touching box_floor | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
4.75 s: pendulum at -4.2°, turning -24°/s; touching nothing | ball1 at (0.58, 0.00, 0.05) m, at rest; touching box_floor | ball2 at (0.66, 0.00, 0.05) m, at rest; touching box_floor | ball3 at (0.87, 0.00, 0.05) m, at rest; touching box_floor | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
5.00 s: pendulum at -6.7°, turning +6°/s; touching nothing | ball1 at (0.58, 0.00, 0.05) m, at rest; touching box_floor | ball2 at (0.66, 0.00, 0.05) m, at rest; touching box_floor | ball3 at (0.87, 0.00, 0.05) m, at rest; touching box_floor | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
5.25 s: pendulum at -1.8°, turning +29°/s; touching nothing | ball1 at (0.58, 0.00, 0.05) m, at rest; touching box_floor | ball2 at (0.66, 0.00, 0.05) m, at rest; touching box_floor | ball3 at (0.87, 0.00, 0.05) m, at rest; touching box_floor | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
5.50 s: pendulum at 5.1°, turning +20°/s; touching nothing | ball1 at (0.58, 0.00, 0.05) m, at rest; touching box_floor | ball2 at (0.66, 0.00, 0.05) m, at rest; touching box_floor | ball3 at (0.87, 0.00, 0.05) m, at rest; touching box_floor | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
5.75 s: pendulum at 6.3°, turning -11°/s; touching nothing | ball1 at (0.58, 0.00, 0.05) m, at rest; touching box_floor | ball2 at (0.66, 0.00, 0.05) m, at rest; touching box_floor | ball3 at (0.87, 0.00, 0.05) m, at rest; touching box_floor | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
6.00 s: pendulum at 0.6°, turning -30°/s; touching nothing | ball1 at (0.58, 0.00, 0.05) m, at rest; touching box_floor | ball2 at (0.66, 0.00, 0.05) m, at rest; touching box_floor | ball3 at (0.87, 0.00, 0.05) m, at rest; touching box_floor | ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor

At the end (6.00 s):
- pendulum at 0.6°, turning -30°/s; touching nothing
- ball1 at (0.58, 0.00, 0.05) m, at rest; touching box_floor
- ball2 at (0.66, 0.00, 0.05) m, at rest; touching box_floor
- ball3 at (0.87, 0.00, 0.05) m, at rest; touching box_floor
- ball4 at (1.23, 0.00, 0.05) m, at rest; touching box_floor
</history>
