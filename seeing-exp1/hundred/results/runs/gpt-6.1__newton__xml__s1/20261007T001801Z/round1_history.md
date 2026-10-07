MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_rod, pendulum_bob; starts at 60.0°, still
- ball1: free body; its geoms: ball1_sphere; starts at (0.08, 0.00, 0.14) m, at rest
- ball2: free body; its geoms: ball2_sphere; starts at (0.23, 0.00, 0.14) m, at rest
- ball3: free body; its geoms: ball3_sphere; starts at (0.38, 0.00, 0.14) m, at rest
- ball4: free body; its geoms: ball4_sphere; starts at (0.53, 0.00, 0.14) m, at rest

What happened, in order:
 0.00 s  pendulum is at its largest at the start, 60.0°
 0.00 s  ball3_sphere first touches rail_bed
 0.00 s  ball4_sphere first touches rail_bed
 0.00 s  ball1_sphere first touches rail_bed
 0.00 s  ball2_sphere first touches rail_bed
 0.54 s  pendulum_bob first touches ball1_sphere
 0.54 s  ball1 starts moving
 0.55 s  pendulum_bob leaves ball1_sphere
 0.56 s  pendulum passes 0.13 m from ball2 (ball2_sphere) without touching it: nearest points (0.06, 0.00, 0.14) m and (0.19, 0.00, 0.14) m
 0.57 s  ball1_sphere first touches ball2_sphere
 0.57 s  ball2 starts moving
 0.58 s  ball1_sphere leaves ball2_sphere
 0.59 s  pendulum passes 0.28 m from ball3 (ball3_sphere) without touching it: nearest points (0.06, 0.00, 0.14) m and (0.34, 0.00, 0.14) m
 0.60 s  ball2_sphere first touches ball3_sphere
 0.60 s  ball3 starts moving
 0.61 s  ball2_sphere leaves ball3_sphere
 0.62 s  pendulum passes 0.42 m from ball4 (ball4_sphere) without touching it: nearest points (0.07, 0.00, 0.14) m and (0.49, 0.00, 0.14) m
 0.63 s  ball3_sphere first touches ball4_sphere
 0.63 s  ball4 starts moving
 0.64 s  ball3_sphere leaves ball4_sphere
 0.73 s  ball4_sphere leaves rail_bed
 0.75 s  ball4_sphere first touches box_front_lip
 0.75 s  ball4_sphere leaves box_front_lip
 0.79 s  ball4 is at the top of its flight, at (0.90, 0.00, 0.15) m
 0.91 s  ball4_sphere first touches box_back_wall
 0.93 s  ball3 comes to rest at (0.49, 0.00, 0.14) m
 0.94 s  ball4_sphere leaves box_back_wall
 0.95 s  pendulum is at its smallest, -2.8°
 0.96 s  ball4_sphere first touches box_bottom
 0.96 s  ball4 comes to rest at (1.18, 0.00, 0.05) m
 0.98 s  ball1 comes to rest at (0.20, 0.00, 0.14) m
 1.16 s  ball2 comes to rest at (0.37, 0.00, 0.14) m
 1.45 s  pendulum passes 0.00 m from rail (rail_bed) without touching it: nearest points (0.00, 0.00, 0.10) m and (0.00, 0.00, 0.10) m
 6.00 s  ball3 passes 0.27 m from box (box_front_lip) without touching it: nearest points (0.53, 0.00, 0.13) m and (0.80, 0.00, 0.10) m
 6.00 s  ball2 passes 0.38 m from box (box_left_wall) without touching it: nearest points (0.41, 0.01, 0.14) m and (0.78, 0.12, 0.14) m

State every 0.25 s:
0.00 s: pendulum at 60.0°, still; touching nothing | ball1 at (0.08, 0.00, 0.14) m, at rest; touching nothing | ball2 at (0.23, 0.00, 0.14) m, at rest; touching nothing | ball3 at (0.38, 0.00, 0.14) m, at rest; touching nothing | ball4 at (0.53, 0.00, 0.14) m, at rest; touching nothing
0.25 s: pendulum at 45.1°, turning -115°/s; touching nothing | ball1 at (0.08, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.23, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (0.53, 0.00, 0.14) m, at rest; touching rail_bed
0.50 s: pendulum at 6.7°, turning -178°/s; touching nothing | ball1 at (0.08, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.23, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (0.53, 0.00, 0.14) m, at rest; touching rail_bed
0.75 s: pendulum at -2.3°, turning -5°/s; touching nothing | ball1 at (0.18, 0.00, 0.14) m, moving 0.09 m/s (vx +0.09, vy -0.00, vz -0.00); touching rail_bed | ball2 at (0.33, 0.00, 0.14) m, moving 0.12 m/s (vx +0.12, vy +0.00, vz -0.01); touching rail_bed | ball3 at (0.47, 0.00, 0.14) m, moving 0.08 m/s (vx +0.08, vy -0.00, vz -0.00); touching rail_bed | ball4 at (0.83, 0.00, 0.14) m, moving 2.18 m/s (vx +2.16, vy +0.00, vz +0.34); touching nothing
1.00 s: pendulum at -2.7°, turning +1°/s; touching nothing | ball1 at (0.20, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.36, 0.00, 0.14) m, moving 0.08 m/s (vx +0.08, vy +0.00, vz -0.00); touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
1.25 s: pendulum at -1.6°, turning +7°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.37, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
1.50 s: pendulum at 0.4°, turning +9°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
1.75 s: pendulum at 2.3°, turning +5°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
2.00 s: pendulum at 2.8°, turning -1°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
2.25 s: pendulum at 1.6°, turning -7°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
2.50 s: pendulum at -0.4°, turning -9°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
2.75 s: pendulum at -2.2°, turning -5°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
3.00 s: pendulum at -2.8°, turning +1°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
3.25 s: pendulum at -1.7°, turning +7°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
3.50 s: pendulum at 0.4°, turning +9°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
3.75 s: pendulum at 2.2°, turning +5°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
4.00 s: pendulum at 2.8°, turning -1°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
4.25 s: pendulum at 1.7°, turning -7°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
4.50 s: pendulum at -0.4°, turning -9°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
4.75 s: pendulum at -2.2°, turning -5°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
5.00 s: pendulum at -2.8°, turning +1°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
5.25 s: pendulum at -1.7°, turning +7°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
5.50 s: pendulum at 0.3°, turning +9°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
5.75 s: pendulum at 2.2°, turning +5°/s; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
6.00 s: pendulum at 2.8°, still; touching nothing | ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed | ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed | ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed | ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom

At the end (6.00 s):
- pendulum at 2.8°, still; touching nothing
- ball1 at (0.21, 0.00, 0.14) m, at rest; touching rail_bed
- ball2 at (0.38, 0.00, 0.14) m, at rest; touching rail_bed
- ball3 at (0.49, 0.00, 0.14) m, at rest; touching rail_bed
- ball4 at (1.17, 0.00, 0.05) m, at rest; touching box_bottom
</history>
