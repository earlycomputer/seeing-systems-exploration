MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum, pendulum rod; starts at 60.0°, still
- ball1: free body; its geoms: ball1; starts at (0.06, 0.00, 0.23) m, at rest
- ball2: free body; its geoms: ball2; starts at (0.21, 0.00, 0.23) m, at rest
- ball3: free body; its geoms: ball3; starts at (0.36, 0.00, 0.23) m, at rest
- ball4: free body; its geoms: ball4; starts at (0.51, 0.00, 0.23) m, at rest

What happened, in order:
 0.00 s  ball4 starts touching rail
 0.00 s  ball1 starts touching rail
 0.00 s  ball2 starts touching rail
 0.00 s  ball3 starts touching rail
 0.00 s  pendulum is at its largest at the start, 60.0°
 0.54 s  ball1 leaves rail
 0.54 s  pendulum first touches ball1
 0.54 s  ball1 starts moving
 0.54 s  pendulum leaves ball1
 0.59 s  ball1 touches rail again
 0.59 s  ball2 leaves rail
 0.59 s  ball1 first touches ball2
 0.59 s  ball2 starts moving
 0.60 s  ball1 leaves ball2
 0.63 s  ball2 touches rail again
 0.69 s  ball2 leaves rail
 0.69 s  ball2 first touches ball3
 0.69 s  ball3 starts moving
 0.69 s  ball1 passes 0.12 m from ball3 without touching it: nearest points (0.22, 0.00, 0.22) m and (0.34, 0.00, 0.23) m
 0.69 s  ball2 leaves ball3
 0.73 s  ball2 touches rail again
 0.96 s  ball1 passes 0.22 m from ball4 without touching it: nearest points (0.27, 0.00, 0.22) m and (0.49, 0.00, 0.22) m
 0.96 s  ball2 passes 0.12 m from ball4 without touching it: nearest points (0.37, 0.00, 0.22) m and (0.49, 0.00, 0.22) m
 0.96 s  ball3 first touches ball4
 0.96 s  ball4 starts moving
 0.96 s  ball3 leaves ball4
 0.98 s  ball3 comes to rest at (0.46, 0.00, 0.22) m
 1.11 s  ball2 comes to rest at (0.35, 0.00, 0.22) m
 1.24 s  ball1 comes to rest at (0.27, 0.00, 0.22) m
 1.38 s  ball4 comes to rest at (0.55, 0.00, 0.22) m
 2.06 s  pendulum passes 0.11 m from ball2 without touching it: nearest points (0.23, 0.00, 0.24) m and (0.34, 0.00, 0.23) m
 2.06 s  pendulum passes 0.21 m from ball3 without touching it: nearest points (0.23, 0.00, 0.24) m and (0.44, 0.00, 0.23) m
 2.06 s  pendulum passes 0.31 m from ball4 without touching it: nearest points (0.23, 0.00, 0.24) m and (0.54, 0.00, 0.23) m
 2.06 s  pendulum passes 0.44 m from box (box_near_wall) without touching it: nearest points (0.23, 0.00, 0.24) m and (0.64, 0.00, 0.10) m
 2.50 s  pendulum passes 0.00 m from rail without touching it: nearest points (0.04, 0.00, 0.20) m and (0.04, 0.00, 0.20) m
 4.06 s  pendulum is at its smallest, -11.7°
 5.99 s  ball2 passes 0.28 m from box (box_near_wall) without touching it: nearest points (0.39, 0.00, 0.21) m and (0.64, 0.00, 0.10) m
 5.99 s  ball1 passes 0.36 m from box (box_near_wall) without touching it: nearest points (0.30, 0.00, 0.22) m and (0.64, 0.00, 0.10) m

State every 0.25 s:
0.00 s: pendulum at 60.0°, still; touching nothing | ball1 at (0.06, 0.00, 0.23) m, at rest; touching rail | ball2 at (0.21, 0.00, 0.23) m, at rest; touching rail | ball3 at (0.36, 0.00, 0.23) m, at rest; touching rail | ball4 at (0.51, 0.00, 0.23) m, at rest; touching rail
0.25 s: pendulum at 44.9°, turning -117°/s; touching nothing | ball1 at (0.06, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.21, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.51, 0.00, 0.22) m, at rest; touching rail
0.50 s: pendulum at 5.9°, turning -180°/s; touching nothing | ball1 at (0.06, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.21, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.51, 0.00, 0.22) m, at rest; touching rail
0.75 s: pendulum at 6.5°, turning +31°/s; touching nothing | ball1 at (0.21, 0.00, 0.22) m, moving 0.21 m/s (vx +0.21, vy +0.00, vz +0.00); touching rail | ball2 at (0.32, 0.00, 0.22) m, moving 0.16 m/s (vx +0.15, vy -0.00, vz +0.04); touching rail | ball3 at (0.39, 0.00, 0.22) m, moving 0.41 m/s (vx +0.41, vy +0.00, vz -0.01); touching rail | ball4 at (0.51, 0.00, 0.22) m, at rest; touching rail
1.00 s: pendulum at 11.5°, turning +7°/s; touching nothing | ball1 at (0.25, 0.00, 0.22) m, moving 0.11 m/s (vx +0.11, vy +0.00, vz -0.00); touching rail | ball2 at (0.35, 0.00, 0.22) m, moving 0.07 m/s (vx +0.07, vy -0.00, vz -0.00); touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.52, 0.00, 0.22) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz +0.00); touching rail
1.25 s: pendulum at 9.8°, turning -20°/s; touching nothing | ball1 at (0.27, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.55, 0.00, 0.22) m, moving 0.08 m/s (vx +0.08, vy +0.00, vz -0.00); touching rail
1.50 s: pendulum at 2.3°, turning -36°/s; touching nothing | ball1 at (0.27, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
1.75 s: pendulum at -6.5°, turning -31°/s; touching nothing | ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
2.00 s: pendulum at -11.5°, turning -7°/s; touching nothing | ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
2.25 s: pendulum at -9.7°, turning +21°/s; touching nothing | ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
2.50 s: pendulum at -2.2°, turning +36°/s; touching nothing | ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
2.75 s: pendulum at 6.6°, turning +31°/s; touching nothing | ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
3.00 s: pendulum at 11.5°, turning +7°/s; touching nothing | ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
3.25 s: pendulum at 9.7°, turning -21°/s; touching nothing | ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
3.50 s: pendulum at 2.1°, turning -36°/s; touching nothing | ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
3.75 s: pendulum at -6.7°, turning -30°/s; touching nothing | ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
4.00 s: pendulum at -11.5°, turning -7°/s; touching nothing | ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
4.25 s: pendulum at -9.6°, turning +21°/s; touching nothing | ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
4.50 s: pendulum at -2.0°, turning +36°/s; touching nothing | ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
4.75 s: pendulum at 6.8°, turning +30°/s; touching nothing | ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
5.00 s: pendulum at 11.6°, turning +6°/s; touching nothing | ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
5.25 s: pendulum at 9.6°, turning -21°/s; touching nothing | ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
5.50 s: pendulum at 1.9°, turning -36°/s; touching nothing | ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
5.75 s: pendulum at -6.8°, turning -30°/s; touching nothing | ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
6.00 s: pendulum at -11.6°, turning -6°/s; touching nothing | ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail

At the end (6.00 s):
- pendulum at -11.6°, turning -6°/s; touching nothing
- ball1 at (0.28, 0.00, 0.22) m, at rest; touching rail
- ball2 at (0.36, 0.00, 0.22) m, at rest; touching rail
- ball3 at (0.46, 0.00, 0.22) m, at rest; touching rail
- ball4 at (0.56, 0.00, 0.22) m, at rest; touching rail
</history>
