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
 0.57 s  pendulum passes 0.09 m from ball2 without touching it: nearest points (0.10, 0.00, 0.23) m and (0.19, 0.00, 0.23) m
 0.57 s  ball2 leaves rail
 0.57 s  ball1 first touches ball2
 0.57 s  ball2 starts moving
 0.57 s  ball1 leaves ball2
 0.60 s  pendulum passes 0.18 m from ball3 without touching it: nearest points (0.15, 0.00, 0.23) m and (0.34, 0.00, 0.23) m
 0.60 s  pendulum touches ball1 again
 0.60 s  ball3 leaves rail
 0.60 s  ball2 first touches ball3
 0.60 s  ball3 starts moving
 0.61 s  pendulum leaves ball1
 0.61 s  ball2 leaves ball3
 0.64 s  ball3 touches rail again
 0.64 s  ball2 passes 0.12 m from ball4 without touching it: nearest points (0.36, 0.00, 0.23) m and (0.49, 0.00, 0.23) m
 0.64 s  pendulum passes 0.28 m from ball4 without touching it: nearest points (0.20, 0.00, 0.24) m and (0.49, 0.00, 0.23) m
 0.64 s  ball3 first touches ball4
 0.64 s  ball4 starts moving
 0.65 s  ball3 leaves ball4
 0.65 s  ball2 touches rail again
 0.65 s  ball1 touches rail again
 0.66 s  ball4 leaves rail
 0.66 s  ball1 passes 0.20 m from ball4 without touching it: nearest points (0.32, 0.00, 0.22) m and (0.52, 0.00, 0.22) m
 0.67 s  ball1 leaves rail
 0.67 s  ball1 touches ball2 again
 0.67 s  ball4 is at the top of its flight, at (0.55, 0.00, 0.23) m
 0.67 s  ball2 leaves rail
 0.67 s  ball1 leaves ball2
 0.70 s  ball1 touches rail again
 0.71 s  ball2 touches rail again
 0.74 s  ball1 passes 0.12 m from ball3 without touching it: nearest points (0.38, 0.00, 0.22) m and (0.51, 0.00, 0.23) m
 0.74 s  ball2 touches ball3 again
 0.75 s  ball2 leaves ball3
 0.76 s  ball3 leaves rail
 0.77 s  ball3 is at the top of its flight, at (0.57, 0.00, 0.23) m
 0.84 s  ball2 leaves rail
 0.86 s  ball4 first touches box_base
 0.87 s  ball4 leaves box_base
 0.96 s  ball4 touches box_base again
 0.96 s  ball3 first touches box_base
 0.97 s  ball4 leaves box_base
 0.98 s  ball3 leaves box_base
 1.00 s  ball4 touches box_base again
 1.01 s  pendulum passes 0.19 m from box (box_left_wall) without touching it: nearest points (0.44, 0.02, 0.31) m and (0.57, 0.14, 0.25) m
 1.03 s  ball4 comes to rest at (1.00, 0.00, 0.04) m
 1.04 s  ball2 first touches box_base
 1.05 s  ball2 leaves box_base
 1.07 s  ball3 touches box_base again
 1.09 s  ball3 comes to rest at (0.88, 0.00, 0.04) m
 1.10 s  ball1 leaves rail
 1.12 s  ball2 touches box_base again
 1.29 s  ball1 touches ball2 again
 1.29 s  ball1 leaves ball2
 1.30 s  ball1 first touches box_base
 1.32 s  ball1 leaves box_base
 1.36 s  ball1 touches box_base again
 1.36 s  ball1 comes to rest at (0.65, 0.00, 0.04) m
 1.40 s  ball2 comes to rest at (0.74, 0.00, 0.04) m
 3.04 s  pendulum is at its smallest, -25.3°
 4.59 s  pendulum passes 0.00 m from rail without touching it: nearest points (0.05, 0.00, 0.20) m and (0.05, 0.00, 0.20) m

State every 0.25 s:
0.00 s: pendulum at 60.0°, still; touching nothing | ball1 at (0.06, 0.00, 0.23) m, at rest; touching rail | ball2 at (0.21, 0.00, 0.23) m, at rest; touching rail | ball3 at (0.36, 0.00, 0.23) m, at rest; touching rail | ball4 at (0.51, 0.00, 0.23) m, at rest; touching rail
0.25 s: pendulum at 45.0°, turning -115°/s; touching nothing | ball1 at (0.06, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.21, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.51, 0.00, 0.22) m, at rest; touching rail
0.50 s: pendulum at 6.4°, turning -179°/s; touching nothing | ball1 at (0.06, 0.00, 0.22) m, at rest; touching rail | ball2 at (0.21, 0.00, 0.22) m, at rest; touching rail | ball3 at (0.36, 0.00, 0.22) m, at rest; touching rail | ball4 at (0.51, 0.00, 0.22) m, at rest; touching rail
0.75 s: pendulum at -17.5°, turning -57°/s; touching nothing | ball1 at (0.36, 0.00, 0.23) m, moving 0.66 m/s (vx +0.66, vy +0.00, vz -0.00); touching nothing | ball2 at (0.49, 0.00, 0.22) m, moving 0.80 m/s (vx +0.80, vy -0.00, vz +0.03); touching rail | ball3 at (0.54, 0.00, 0.23) m, moving 1.49 m/s (vx +1.49, vy +0.00, vz -0.01); touching nothing | ball4 at (0.71, 0.00, 0.19) m, moving 2.09 m/s (vx +1.92, vy -0.00, vz -0.83); touching nothing
1.00 s: pendulum at -25.2°, turning -3°/s; touching nothing | ball1 at (0.51, 0.00, 0.23) m, moving 0.53 m/s (vx +0.53, vy +0.00, vz -0.01); touching nothing | ball2 at (0.67, 0.00, 0.11) m, moving 1.70 m/s (vx +0.71, vy -0.00, vz -1.54); touching nothing | ball3 at (0.86, 0.00, 0.05) m, moving 0.30 m/s (vx +0.22, vy +0.00, vz +0.21); touching nothing | ball4 at (1.00, 0.00, 0.05) m, moving 0.29 m/s (vx +0.26, vy -0.00, vz -0.13); touching nothing
1.25 s: pendulum at -18.6°, turning +53°/s; touching nothing | ball1 at (0.64, 0.00, 0.12) m, moving 1.53 m/s (vx +0.52, vy +0.00, vz -1.44); touching nothing | ball2 at (0.70, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
1.50 s: pendulum at -1.3°, turning +79°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
1.75 s: pendulum at 16.7°, turning +59°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
2.00 s: pendulum at 25.2°, turning +6°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
2.25 s: pendulum at 19.3°, turning -50°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
2.50 s: pendulum at 2.3°, turning -78°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
2.75 s: pendulum at -16.0°, turning -61°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
3.00 s: pendulum at -25.1°, turning -9°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
3.25 s: pendulum at -19.9°, turning +48°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
3.50 s: pendulum at -3.3°, turning +78°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
3.75 s: pendulum at 15.2°, turning +63°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
4.00 s: pendulum at 25.0°, turning +12°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
4.25 s: pendulum at 20.5°, turning -45°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
4.50 s: pendulum at 4.3°, turning -77°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
4.75 s: pendulum at -14.4°, turning -65°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
5.00 s: pendulum at -24.8°, turning -15°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
5.25 s: pendulum at -21.1°, turning +43°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
5.50 s: pendulum at -5.3°, turning +77°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
5.75 s: pendulum at 13.6°, turning +66°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
6.00 s: pendulum at 24.6°, turning +18°/s; touching nothing | ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base | ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base | ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base | ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base

At the end (6.00 s):
- pendulum at 24.6°, turning +18°/s; touching nothing
- ball1 at (0.65, 0.00, 0.04) m, at rest; touching box_base
- ball2 at (0.74, 0.00, 0.04) m, at rest; touching box_base
- ball3 at (0.88, 0.00, 0.04) m, at rest; touching box_base
- ball4 at (1.00, 0.00, 0.04) m, at rest; touching box_base
</history>
