MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_rod, pendulum_bob; starts at 90.0°, still
- ball1: free body; its geoms: ball1_geom; starts at (0.05, 0.00, 0.33) m, at rest
- ball2: free body; its geoms: ball2_geom; starts at (0.20, 0.00, 0.33) m, at rest
- ball3: free body; its geoms: ball3_geom; starts at (0.35, 0.00, 0.33) m, at rest
- ball4: free body; its geoms: ball4_geom; starts at (0.50, 0.00, 0.33) m, at rest

What happened, in order:
 0.00 s  pendulum is at its largest at the start, 90.0°
 0.00 s  ball1_geom first touches rail_beam
 0.00 s  ball4_geom first touches rail_beam
 0.00 s  ball2_geom first touches rail_beam
 0.00 s  ball3_geom first touches rail_beam
 0.42 s  pendulum_bob first touches ball1_geom
 0.42 s  ball1 starts moving
 0.43 s  pendulum_bob leaves ball1_geom
 0.46 s  ball1_geom leaves rail_beam
 0.47 s  ball1_geom first touches ball2_geom
 0.47 s  ball2 starts moving
 0.47 s  pendulum passes 0.12 m from ball2 (ball2_geom) without touching it: nearest points (0.06, 0.00, 0.33) m and (0.18, 0.00, 0.33) m
 0.48 s  ball1_geom leaves ball2_geom
 0.54 s  ball1_geom touches rail_beam again
 0.56 s  pendulum passes 0.24 m from ball3 (ball3_geom) without touching it: nearest points (0.09, 0.00, 0.33) m and (0.33, 0.00, 0.33) m
 0.56 s  ball2_geom leaves rail_beam
 0.56 s  ball2_geom first touches ball3_geom
 0.56 s  ball3 starts moving
 0.57 s  ball2_geom leaves ball3_geom
 0.61 s  ball2_geom touches rail_beam again
 0.73 s  ball3_geom first touches ball4_geom
 0.73 s  ball4 starts moving
 0.73 s  ball1 passes 0.25 m from ball4 (ball4_geom) without touching it: nearest points (0.23, 0.00, 0.32) m and (0.48, 0.00, 0.32) m
 0.73 s  pendulum passes 0.36 m from ball4 (ball4_geom) without touching it: nearest points (0.11, 0.00, 0.33) m and (0.48, 0.00, 0.33) m
 0.74 s  ball3_geom leaves ball4_geom
 0.74 s  pendulum is at its smallest, -10.4°
 1.08 s  ball4_geom leaves rail_beam
 1.20 s  ball4_geom first touches box_wall_near
 1.21 s  ball4_geom leaves box_wall_near
 1.33 s  ball4_geom first touches box_base
 1.34 s  ball4_geom first touches floor
 1.35 s  ball4_geom leaves floor
 1.37 s  ball4_geom leaves box_base
 1.45 s  ball4_geom touches box_base again
 1.47 s  ball2_geom touches ball3_geom again
 1.47 s  ball2_geom leaves ball3_geom
 1.66 s  ball1_geom touches ball2_geom again
 1.66 s  ball1 passes 0.06 m from ball3 (ball3_geom) without touching it: nearest points (0.41, 0.00, 0.32) m and (0.47, 0.00, 0.32) m
 1.66 s  ball1 comes to rest at (0.38, 0.00, 0.32) m
 1.66 s  ball1_geom leaves ball2_geom
 1.95 s  ball2_geom touches ball3_geom again
 1.95 s  ball2_geom leaves ball3_geom
 2.80 s  ball3_geom leaves rail_beam
 2.91 s  ball3_geom first touches box_wall_near
 2.94 s  ball3_geom leaves box_wall_near
 3.11 s  ball3_geom touches ball4_geom again
 3.12 s  ball3_geom leaves ball4_geom
 3.16 s  ball3_geom first touches box_base
 3.19 s  ball3_geom leaves box_base
 3.22 s  ball3_geom touches box_wall_near again
 3.24 s  ball4 comes to rest at (0.80, 0.00, 0.03) m
 3.25 s  ball3_geom leaves box_wall_near
 3.25 s  ball3_geom touches box_base again
 3.27 s  ball3 comes to rest at (0.67, 0.00, 0.03) m
 3.76 s  ball2_geom leaves rail_beam
 3.88 s  ball2_geom first touches box_wall_near
 3.91 s  ball2_geom leaves box_wall_near
 3.92 s  ball2 is at the top of its flight, at (0.66, 0.00, 0.22) m
 4.12 s  ball2_geom first touches box_base
 4.12 s  ball2_geom first touches floor
 4.13 s  ball2_geom leaves floor
 4.15 s  ball2_geom leaves box_base
 4.23 s  ball2_geom touches box_base again
 4.27 s  ball2 comes to rest at (0.73, 0.00, 0.03) m
 4.64 s  ball2 passes 0.03 m from ball4 (ball4_geom) without touching it: nearest points (0.75, 0.00, 0.03) m and (0.78, 0.00, 0.03) m
 4.71 s  pendulum passes 0.00 m from rail (rail_beam) without touching it: nearest points (0.03, 0.00, 0.30) m and (0.03, 0.00, 0.30) m
 6.00 s  ball1 passes 0.19 m from box (box_wall_near) without touching it: nearest points (0.48, 0.00, 0.31) m and (0.63, 0.00, 0.20) m

State every 0.25 s:
0.00 s: pendulum at 90.0°, still; touching nothing | ball1 at (0.05, 0.00, 0.33) m, at rest; touching nothing | ball2 at (0.20, 0.00, 0.33) m, at rest; touching nothing | ball3 at (0.35, 0.00, 0.33) m, at rest; touching nothing | ball4 at (0.50, 0.00, 0.33) m, at rest; touching nothing
0.25 s: pendulum at 54.8°, turning -273°/s; touching nothing | ball1 at (0.05, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.20, 0.00, 0.32) m, at rest; touching rail_beam | ball3 at (0.35, 0.00, 0.32) m, at rest; touching rail_beam | ball4 at (0.50, 0.00, 0.32) m, at rest; touching rail_beam
0.50 s: pendulum at -4.8°, turning -41°/s; touching nothing | ball1 at (0.16, 0.00, 0.33) m, moving 0.11 m/s (vx +0.09, vy +0.00, vz +0.06); touching nothing | ball2 at (0.24, 0.00, 0.32) m, moving 1.14 m/s (vx +1.14, vy -0.00, vz -0.01); touching rail_beam | ball3 at (0.35, 0.00, 0.32) m, at rest; touching rail_beam | ball4 at (0.50, 0.00, 0.32) m, at rest; touching rail_beam
0.75 s: pendulum at -10.4°, still; touching nothing | ball1 at (0.20, 0.00, 0.32) m, moving 0.19 m/s (vx +0.19, vy +0.00, vz -0.00); touching rail_beam | ball2 at (0.32, 0.00, 0.32) m, moving 0.14 m/s (vx +0.14, vy -0.00, vz +0.00); touching rail_beam | ball3 at (0.45, 0.00, 0.33) m, at rest; touching nothing | ball4 at (0.51, 0.00, 0.32) m, moving 0.34 m/s (vx +0.33, vy +0.00, vz -0.01); touching rail_beam
1.00 s: pendulum at -4.4°, turning +42°/s; touching nothing | ball1 at (0.25, 0.00, 0.32) m, moving 0.19 m/s (vx +0.19, vy +0.00, vz -0.00); touching rail_beam | ball2 at (0.36, 0.00, 0.32) m, moving 0.14 m/s (vx +0.14, vy -0.00, vz +0.00); touching rail_beam | ball3 at (0.46, 0.00, 0.32) m, at rest; touching rail_beam | ball4 at (0.59, 0.00, 0.32) m, moving 0.33 m/s (vx +0.33, vy +0.00, vz -0.00); touching rail_beam
1.25 s: pendulum at 6.5°, turning +36°/s; touching nothing | ball1 at (0.30, 0.00, 0.32) m, moving 0.19 m/s (vx +0.19, vy +0.00, vz +0.00); touching rail_beam | ball2 at (0.39, 0.00, 0.32) m, moving 0.14 m/s (vx +0.14, vy -0.00, vz -0.00); touching rail_beam | ball3 at (0.47, 0.00, 0.32) m, at rest; touching rail_beam | ball4 at (0.69, 0.00, 0.17) m, moving 1.42 m/s (vx +0.73, vy +0.00, vz -1.22); touching nothing
1.50 s: pendulum at 10.1°, turning -9°/s; touching nothing | ball1 at (0.35, 0.00, 0.32) m, moving 0.19 m/s (vx +0.19, vy +0.00, vz +0.00); touching rail_beam | ball2 at (0.42, 0.00, 0.32) m, at rest; touching rail_beam | ball3 at (0.48, 0.00, 0.32) m, moving 0.09 m/s (vx +0.09, vy +0.00, vz +0.00); touching rail_beam | ball4 at (0.77, 0.00, 0.03) m, at rest; touching box_base
1.75 s: pendulum at 2.6°, turning -45°/s; touching nothing | ball1 at (0.38, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.44, 0.00, 0.32) m, moving 0.13 m/s (vx +0.13, vy -0.00, vz -0.00); touching rail_beam | ball3 at (0.50, 0.00, 0.32) m, moving 0.09 m/s (vx +0.09, vy +0.00, vz +0.00); touching rail_beam | ball4 at (0.77, 0.00, 0.03) m, at rest; touching box_base
2.00 s: pendulum at -7.9°, turning -30°/s; touching nothing | ball1 at (0.39, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.47, 0.00, 0.32) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz -0.00); touching rail_beam | ball3 at (0.52, 0.00, 0.32) m, moving 0.11 m/s (vx +0.11, vy +0.00, vz +0.00); touching rail_beam | ball4 at (0.77, 0.00, 0.03) m, at rest; touching box_base
2.25 s: pendulum at -9.6°, turning +18°/s; touching nothing | ball1 at (0.39, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.49, 0.00, 0.32) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz -0.00); touching rail_beam | ball3 at (0.55, 0.00, 0.32) m, moving 0.11 m/s (vx +0.11, vy +0.00, vz +0.00); touching rail_beam | ball4 at (0.77, 0.00, 0.03) m, at rest; touching box_base
2.50 s: pendulum at -0.7°, turning +46°/s; touching nothing | ball1 at (0.40, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.51, 0.00, 0.32) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz +0.00); touching rail_beam | ball3 at (0.58, 0.00, 0.32) m, moving 0.11 m/s (vx +0.11, vy +0.00, vz -0.00); touching rail_beam | ball4 at (0.77, 0.00, 0.03) m, at rest; touching box_base
2.75 s: pendulum at 9.0°, turning +23°/s; touching nothing | ball1 at (0.40, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.53, 0.00, 0.32) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz +0.00); touching rail_beam | ball3 at (0.61, 0.00, 0.32) m, moving 0.19 m/s (vx +0.18, vy +0.00, vz -0.07); touching rail_beam | ball4 at (0.77, 0.00, 0.03) m, at rest; touching box_base
3.00 s: pendulum at 8.7°, turning -25°/s; touching nothing | ball1 at (0.40, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.55, 0.00, 0.32) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz +0.00); touching rail_beam | ball3 at (0.68, 0.00, 0.20) m, moving 0.75 m/s (vx +0.42, vy +0.00, vz -0.62); touching nothing | ball4 at (0.77, 0.00, 0.03) m, at rest; touching box_base
3.25 s: pendulum at -1.3°, turning -46°/s; touching nothing | ball1 at (0.41, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.57, 0.00, 0.32) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz +0.00); touching rail_beam | ball3 at (0.66, 0.00, 0.04) m, moving 0.21 m/s (vx +0.13, vy +0.00, vz -0.16); touching box_wall_near | ball4 at (0.80, 0.00, 0.03) m, at rest; touching box_base
3.50 s: pendulum at -9.8°, turning -16°/s; touching nothing | ball1 at (0.41, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.59, 0.00, 0.32) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz +0.00); touching rail_beam | ball3 at (0.67, 0.00, 0.03) m, at rest; touching box_base | ball4 at (0.80, 0.00, 0.03) m, at rest; touching box_base
3.75 s: pendulum at -7.5°, turning +32°/s; touching nothing | ball1 at (0.42, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.61, 0.00, 0.32) m, moving 0.28 m/s (vx +0.22, vy -0.00, vz -0.16); touching rail_beam | ball3 at (0.67, 0.00, 0.03) m, at rest; touching box_base | ball4 at (0.80, 0.00, 0.03) m, at rest; touching box_base
4.00 s: pendulum at 3.1°, turning +44°/s; touching nothing | ball1 at (0.42, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.68, 0.00, 0.19) m, moving 0.86 m/s (vx +0.33, vy -0.00, vz -0.79); touching nothing | ball3 at (0.67, 0.00, 0.03) m, at rest; touching box_base | ball4 at (0.80, 0.00, 0.03) m, at rest; touching box_base
4.25 s: pendulum at 10.3°, turning +7°/s; touching nothing | ball1 at (0.43, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.73, 0.00, 0.03) m, moving 0.08 m/s (vx +0.01, vy -0.00, vz +0.08); touching box_base | ball3 at (0.67, 0.00, 0.03) m, at rest; touching box_base | ball4 at (0.80, 0.00, 0.03) m, at rest; touching box_base
4.50 s: pendulum at 6.0°, turning -37°/s; touching nothing | ball1 at (0.43, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.73, 0.00, 0.03) m, at rest; touching box_base | ball3 at (0.67, 0.00, 0.03) m, at rest; touching box_base | ball4 at (0.80, 0.00, 0.03) m, at rest; touching box_base
4.75 s: pendulum at -4.9°, turning -41°/s; touching nothing | ball1 at (0.43, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.73, 0.00, 0.03) m, at rest; touching box_base | ball3 at (0.67, 0.00, 0.03) m, at rest; touching box_base | ball4 at (0.80, 0.00, 0.03) m, at rest; touching box_base
5.00 s: pendulum at -10.4°, turning +1°/s; touching nothing | ball1 at (0.44, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.73, 0.00, 0.03) m, at rest; touching box_base | ball3 at (0.67, 0.00, 0.03) m, at rest; touching box_base | ball4 at (0.80, 0.00, 0.03) m, at rest; touching box_base
5.25 s: pendulum at -4.3°, turning +42°/s; touching nothing | ball1 at (0.44, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.73, 0.00, 0.03) m, at rest; touching box_base | ball3 at (0.67, 0.00, 0.03) m, at rest; touching box_base | ball4 at (0.80, 0.00, 0.03) m, at rest; touching box_base
5.50 s: pendulum at 6.5°, turning +36°/s; touching nothing | ball1 at (0.45, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.73, 0.00, 0.03) m, at rest; touching box_base | ball3 at (0.67, 0.00, 0.03) m, at rest; touching box_base | ball4 at (0.80, 0.00, 0.03) m, at rest; touching box_base
5.75 s: pendulum at 10.1°, turning -10°/s; touching nothing | ball1 at (0.45, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.73, 0.00, 0.03) m, at rest; touching box_base | ball3 at (0.67, 0.00, 0.03) m, at rest; touching box_base | ball4 at (0.80, 0.00, 0.03) m, at rest; touching box_base
6.00 s: pendulum at 2.5°, turning -45°/s; touching nothing | ball1 at (0.46, 0.00, 0.32) m, at rest; touching rail_beam | ball2 at (0.73, 0.00, 0.03) m, at rest; touching box_base | ball3 at (0.67, 0.00, 0.03) m, at rest; touching box_base | ball4 at (0.80, 0.00, 0.03) m, at rest; touching box_base

At the end (6.00 s):
- pendulum at 2.5°, turning -45°/s; touching nothing
- ball1 at (0.46, 0.00, 0.32) m, at rest; touching rail_beam
- ball2 at (0.73, 0.00, 0.03) m, at rest; touching box_base
- ball3 at (0.67, 0.00, 0.03) m, at rest; touching box_base
- ball4 at (0.80, 0.00, 0.03) m, at rest; touching box_base
</history>
