MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), range -79.9998° to 60.0001° as MuJoCo applies it; its geoms: pendulum, pendulum rod; starts at 60.0°, still
- ball1: free body; its geoms: ball1; starts at (0.08, 0.00, 0.14) m, at rest
- ball2: free body; its geoms: ball2; starts at (0.23, 0.00, 0.14) m, at rest
- ball3: free body; its geoms: ball3; starts at (0.38, 0.00, 0.14) m, at rest
- ball4: free body; its geoms: ball4; starts at (0.53, 0.00, 0.14) m, at rest

What happened, in order:
 0.00 s  pendulum starts at its upper stop (60.0001°)
 0.00 s  pendulum is at its largest at the start, 60.0°
 0.00 s  ball4 first touches rail
 0.00 s  ball1 first touches rail
 0.00 s  ball2 first touches rail
 0.00 s  ball3 first touches rail
 0.43 s  pendulum passes 0.02 m from left guide without touching it: nearest points (-0.32, 0.04, 0.19) m and (-0.32, 0.06, 0.19) m
 0.43 s  pendulum passes 0.02 m from right guide without touching it: nearest points (-0.32, -0.04, 0.19) m and (-0.32, -0.06, 0.19) m
 0.54 s  pendulum first touches ball1
 0.54 s  ball1 starts moving
 0.54 s  pendulum leaves ball1
 0.57 s  ball1 first touches ball2
 0.57 s  ball2 starts moving
 0.58 s  ball1 leaves ball2
 0.62 s  ball2 first touches ball3
 0.62 s  ball3 starts moving
 0.62 s  ball2 leaves ball3
 0.68 s  ball3 first touches ball4
 0.68 s  ball4 starts moving
 0.68 s  ball3 leaves ball4
 0.68 s  pendulum passes 0.33 m from ball4 without touching it: nearest points (0.16, 0.00, 0.15) m and (0.49, 0.00, 0.14) m
 0.83 s  pendulum passes 0.10 m from ball2 without touching it: nearest points (0.26, 0.00, 0.16) m and (0.35, 0.00, 0.15) m
 0.83 s  ball1 touches ball2 again
 0.84 s  ball1 leaves ball2
 0.91 s  pendulum passes 0.20 m from ball3 without touching it: nearest points (0.29, 0.00, 0.17) m and (0.49, 0.00, 0.14) m
 0.94 s  ball2 touches ball3 again
 0.94 s  ball2 leaves ball3
 1.15 s  ball4 leaves rail
 1.17 s  ball1 touches ball2 again
 1.18 s  ball1 leaves ball2
 1.28 s  ball4 first touches box_base
 1.30 s  ball4 leaves box_base
 1.36 s  ball4 touches box_base again
 1.80 s  ball3 leaves rail
 1.89 s  ball3 touches ball4 again
 1.89 s  ball3 leaves ball4
 1.90 s  ball3 first touches box_base
 2.18 s  ball2 leaves rail
 2.19 s  ball2 touches ball3 again
 2.19 s  ball2 leaves ball3
 2.26 s  ball2 touches ball3 again
 2.26 s  ball1 passes 0.07 m from ball3 without touching it: nearest points (0.93, 0.00, 0.12) m and (0.99, 0.00, 0.08) m
 2.26 s  ball2 touches rail again
 2.27 s  ball1 touches ball2 again
 2.27 s  ball2 leaves rail
 2.27 s  ball1 leaves ball2
 2.27 s  ball1 passes 0.16 m from ball4 without touching it: nearest points (0.94, 0.00, 0.13) m and (1.09, 0.00, 0.07) m
 2.27 s  ball1 passes 0.09 m from box (box_near_wall) without touching it: nearest points (0.91, 0.00, 0.10) m and (0.94, 0.00, 0.02) m
 2.33 s  ball2 touches rail again
 2.39 s  ball3 touches ball4 again
 2.39 s  ball3 leaves ball4
 2.39 s  ball2 passes 0.07 m from ball4 without touching it: nearest points (1.02, 0.00, 0.10) m and (1.09, 0.00, 0.07) m
 2.43 s  ball3 touches ball4 again
 2.54 s  ball3 leaves ball4
 2.55 s  ball2 leaves ball3
 2.55 s  pendulum passes 0.00 m from rail without touching it: nearest points (0.00, 0.00, 0.10) m and (0.00, 0.00, 0.10) m
 2.57 s  ball2 leaves rail
 2.58 s  ball2 first touches box_base
 2.58 s  ball3 comes to rest at (1.07, 0.00, 0.06) m
 2.58 s  ball4 comes to rest at (1.15, 0.00, 0.06) m
 2.60 s  ball2 leaves box_base
 2.63 s  ball2 touches box_base again
 2.63 s  ball2 comes to rest at (0.99, 0.00, 0.06) m
 5.07 s  pendulum is at its smallest, -15.8°
 5.13 s  ball1 comes to rest at (0.70, 0.00, 0.14) m

State every 0.25 s:
0.00 s: pendulum at 60.0°, still; touching nothing | ball1 at (0.08, 0.00, 0.14) m, at rest; touching nothing | ball2 at (0.23, 0.00, 0.14) m, at rest; touching nothing | ball3 at (0.38, 0.00, 0.14) m, at rest; touching nothing | ball4 at (0.53, 0.00, 0.14) m, at rest; touching nothing
0.25 s: pendulum at 45.1°, turning -115°/s; touching nothing | ball1 at (0.08, 0.00, 0.14) m, at rest; touching rail | ball2 at (0.23, 0.00, 0.14) m, at rest; touching rail | ball3 at (0.38, 0.00, 0.14) m, at rest; touching rail | ball4 at (0.53, 0.00, 0.14) m, at rest; touching rail
0.50 s: pendulum at 6.7°, turning -178°/s; touching nothing | ball1 at (0.08, 0.00, 0.14) m, at rest; touching rail | ball2 at (0.23, 0.00, 0.14) m, at rest; touching rail | ball3 at (0.38, 0.00, 0.14) m, at rest; touching rail | ball4 at (0.53, 0.00, 0.14) m, at rest; touching rail
0.75 s: pendulum at -9.9°, turning -39°/s; touching nothing | ball1 at (0.26, 0.00, 0.14) m, moving 0.62 m/s (vx +0.62, vy +0.00, vz +0.00); touching rail | ball2 at (0.36, 0.00, 0.14) m, moving 0.43 m/s (vx +0.43, vy +0.00, vz +0.00); touching rail | ball3 at (0.48, 0.00, 0.14) m, moving 0.32 m/s (vx +0.32, vy -0.00, vz +0.00); touching rail | ball4 at (0.59, 0.00, 0.14) m, moving 0.89 m/s (vx +0.89, vy -0.00, vz +0.00); touching rail
1.00 s: pendulum at -15.7°, turning -6°/s; touching nothing | ball1 at (0.39, 0.00, 0.14) m, moving 0.45 m/s (vx +0.45, vy +0.00, vz +0.00); touching rail | ball2 at (0.48, 0.00, 0.14) m, moving 0.39 m/s (vx +0.39, vy +0.00, vz +0.00); touching rail | ball3 at (0.57, 0.00, 0.14) m, moving 0.51 m/s (vx +0.51, vy -0.00, vz +0.00); touching rail | ball4 at (0.82, 0.00, 0.14) m, moving 0.88 m/s (vx +0.88, vy -0.00, vz -0.00); touching rail
1.25 s: pendulum at -12.5°, turning +30°/s; touching nothing | ball1 at (0.50, 0.00, 0.14) m, moving 0.41 m/s (vx +0.41, vy +0.00, vz +0.00); touching rail | ball2 at (0.58, 0.00, 0.14) m, moving 0.43 m/s (vx +0.43, vy -0.00, vz +0.00); touching rail | ball3 at (0.69, 0.00, 0.14) m, moving 0.51 m/s (vx +0.51, vy -0.00, vz -0.01); touching rail | ball4 at (1.04, 0.00, 0.09) m, moving 1.30 m/s (vx +0.88, vy -0.00, vz -0.96); touching nothing
1.50 s: pendulum at -2.0°, turning +49°/s; touching nothing | ball1 at (0.60, 0.00, 0.14) m, moving 0.40 m/s (vx +0.40, vy +0.00, vz +0.00); touching rail | ball2 at (0.69, 0.00, 0.14) m, moving 0.42 m/s (vx +0.42, vy -0.00, vz -0.01); touching rail | ball3 at (0.82, 0.00, 0.14) m, moving 0.50 m/s (vx +0.50, vy -0.00, vz +0.00); touching rail | ball4 at (1.10, 0.00, 0.06) m, at rest; touching box_base
1.75 s: pendulum at 9.6°, turning +39°/s; touching nothing | ball1 at (0.70, 0.00, 0.14) m, moving 0.40 m/s (vx +0.40, vy +0.00, vz +0.00); touching rail | ball2 at (0.79, 0.00, 0.14) m, moving 0.42 m/s (vx +0.42, vy -0.00, vz +0.00); touching rail | ball3 at (0.95, 0.00, 0.14) m, moving 0.50 m/s (vx +0.50, vy -0.00, vz +0.00); touching rail | ball4 at (1.10, 0.00, 0.06) m, at rest; touching box_base
2.00 s: pendulum at 15.7°, turning +7°/s; touching nothing | ball1 at (0.80, 0.00, 0.14) m, moving 0.39 m/s (vx +0.39, vy +0.00, vz +0.00); touching rail | ball2 at (0.90, 0.00, 0.14) m, moving 0.41 m/s (vx +0.41, vy -0.00, vz +0.00); touching rail | ball3 at (1.02, 0.00, 0.06) m, at rest; touching box_base | ball4 at (1.12, 0.00, 0.06) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz -0.01); touching nothing
2.25 s: pendulum at 12.7°, turning -29°/s; touching nothing | ball1 at (0.90, 0.00, 0.14) m, moving 0.39 m/s (vx +0.39, vy +0.00, vz -0.00); touching rail | ball2 at (0.98, 0.00, 0.13) m, moving 0.30 m/s (vx +0.04, vy +0.00, vz -0.30); touching nothing | ball3 at (1.03, 0.00, 0.06) m, at rest; touching nothing | ball4 at (1.13, 0.00, 0.06) m, at rest; touching box_base
2.50 s: pendulum at 2.4°, turning -49°/s; touching nothing | ball1 at (0.88, 0.00, 0.14) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz +0.00); touching rail | ball2 at (0.99, 0.00, 0.10) m, moving 0.25 m/s (vx +0.01, vy +0.00, vz -0.25); touching rail | ball3 at (1.06, 0.00, 0.06) m, moving 0.14 m/s (vx +0.14, vy -0.00, vz -0.02); touching nothing | ball4 at (1.14, 0.00, 0.06) m, moving 0.16 m/s (vx +0.16, vy +0.00, vz +0.02); touching box_base
2.75 s: pendulum at -9.3°, turning -40°/s; touching nothing | ball1 at (0.86, 0.00, 0.14) m, moving 0.09 m/s (vx -0.09, vy +0.00, vz +0.00); touching rail | ball2 at (0.99, 0.00, 0.06) m, at rest; touching box_base | ball3 at (1.07, 0.00, 0.06) m, at rest; touching box_base | ball4 at (1.15, 0.00, 0.06) m, at rest; touching box_base
3.00 s: pendulum at -15.6°, turning -8°/s; touching nothing | ball1 at (0.84, 0.00, 0.14) m, moving 0.08 m/s (vx -0.08, vy +0.00, vz -0.01); touching rail | ball2 at (0.99, 0.00, 0.06) m, at rest; touching box_base | ball3 at (1.07, 0.00, 0.06) m, at rest; touching box_base | ball4 at (1.15, 0.00, 0.06) m, at rest; touching box_base
3.25 s: pendulum at -13.0°, turning +28°/s; touching nothing | ball1 at (0.82, 0.00, 0.14) m, moving 0.08 m/s (vx -0.08, vy +0.00, vz +0.00); touching rail | ball2 at (0.99, 0.00, 0.06) m, at rest; touching box_base | ball3 at (1.07, 0.00, 0.06) m, at rest; touching box_base | ball4 at (1.15, 0.00, 0.06) m, at rest; touching box_base
3.50 s: pendulum at -2.8°, turning +49°/s; touching nothing | ball1 at (0.80, 0.00, 0.14) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz +0.00); touching rail | ball2 at (0.99, 0.00, 0.06) m, at rest; touching box_base | ball3 at (1.07, 0.00, 0.06) m, at rest; touching box_base | ball4 at (1.15, 0.00, 0.06) m, at rest; touching box_base
3.75 s: pendulum at 9.0°, turning +41°/s; touching nothing | ball1 at (0.78, 0.00, 0.14) m, moving 0.07 m/s (vx -0.07, vy +0.00, vz +0.00); touching rail | ball2 at (0.99, 0.00, 0.06) m, at rest; touching box_base | ball3 at (1.07, 0.00, 0.06) m, at rest; touching box_base | ball4 at (1.15, 0.00, 0.06) m, at rest; touching box_base
4.00 s: pendulum at 15.6°, turning +10°/s; touching nothing | ball1 at (0.76, 0.00, 0.14) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching rail | ball2 at (0.99, 0.00, 0.06) m, at rest; touching box_base | ball3 at (1.07, 0.00, 0.06) m, at rest; touching box_base | ball4 at (1.15, 0.00, 0.06) m, at rest; touching box_base
4.25 s: pendulum at 13.2°, turning -27°/s; touching nothing | ball1 at (0.75, 0.00, 0.14) m, moving 0.06 m/s (vx -0.06, vy +0.00, vz +0.00); touching rail | ball2 at (0.99, 0.00, 0.06) m, at rest; touching box_base | ball3 at (1.07, 0.00, 0.06) m, at rest; touching box_base | ball4 at (1.15, 0.00, 0.06) m, at rest; touching box_base
4.50 s: pendulum at 3.2°, turning -48°/s; touching nothing | ball1 at (0.73, 0.00, 0.14) m, moving 0.05 m/s (vx -0.05, vy +0.00, vz +0.00); touching rail | ball2 at (0.99, 0.00, 0.06) m, at rest; touching box_base | ball3 at (1.07, 0.00, 0.06) m, at rest; touching box_base | ball4 at (1.15, 0.00, 0.06) m, at rest; touching box_base
4.75 s: pendulum at -8.6°, turning -42°/s; touching nothing | ball1 at (0.72, 0.00, 0.14) m, at rest; touching rail | ball2 at (0.99, 0.00, 0.06) m, at rest; touching box_base | ball3 at (1.07, 0.00, 0.06) m, at rest; touching box_base | ball4 at (1.15, 0.00, 0.06) m, at rest; touching box_base
5.00 s: pendulum at -15.5°, turning -11°/s; touching nothing | ball1 at (0.71, 0.00, 0.14) m, at rest; touching rail | ball2 at (0.99, 0.00, 0.06) m, at rest; touching box_base | ball3 at (1.07, 0.00, 0.06) m, at rest; touching box_base | ball4 at (1.15, 0.00, 0.06) m, at rest; touching box_base
5.25 s: pendulum at -13.4°, turning +26°/s; touching nothing | ball1 at (0.70, 0.00, 0.14) m, at rest; touching rail | ball2 at (0.99, 0.00, 0.06) m, at rest; touching box_base | ball3 at (1.07, 0.00, 0.06) m, at rest; touching box_base | ball4 at (1.15, 0.00, 0.06) m, at rest; touching box_base
5.50 s: pendulum at -3.6°, turning +48°/s; touching nothing | ball1 at (0.69, 0.00, 0.14) m, at rest; touching rail | ball2 at (0.99, 0.00, 0.06) m, at rest; touching box_base | ball3 at (1.07, 0.00, 0.06) m, at rest; touching box_base | ball4 at (1.15, 0.00, 0.06) m, at rest; touching box_base
5.75 s: pendulum at 8.3°, turning +42°/s; touching nothing | ball1 at (0.67, 0.00, 0.14) m, at rest; touching rail | ball2 at (0.99, 0.00, 0.06) m, at rest; touching box_base | ball3 at (1.07, 0.00, 0.06) m, at rest; touching box_base | ball4 at (1.15, 0.00, 0.06) m, at rest; touching box_base
6.00 s: pendulum at 15.4°, turning +12°/s; touching nothing | ball1 at (0.66, 0.00, 0.14) m, at rest; touching rail | ball2 at (0.99, 0.00, 0.06) m, at rest; touching box_base | ball3 at (1.07, 0.00, 0.06) m, at rest; touching box_base | ball4 at (1.15, 0.00, 0.06) m, at rest; touching box_base

At the end (6.00 s):
- pendulum at 15.4°, turning +12°/s; touching nothing
- ball1 at (0.66, 0.00, 0.14) m, at rest; touching rail
- ball2 at (0.99, 0.00, 0.06) m, at rest; touching box_base
- ball3 at (1.07, 0.00, 0.06) m, at rest; touching box_base
- ball4 at (1.15, 0.00, 0.06) m, at rest; touching box_base
</history>
