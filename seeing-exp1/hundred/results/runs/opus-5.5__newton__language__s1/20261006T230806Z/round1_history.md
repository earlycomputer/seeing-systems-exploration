MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum, pendulum rod; starts at 80.4°, still
- ball1: free body; its geoms: ball1; starts at (0.07, 0.00, 0.33) m, at rest
- ball2: free body; its geoms: ball2; starts at (0.21, 0.00, 0.33) m, at rest
- ball3: free body; its geoms: ball3; starts at (0.36, 0.00, 0.33) m, at rest
- ball4: free body; its geoms: ball4; starts at (0.52, 0.00, 0.33) m, at rest

What happened, in order:
 0.00 s  ball1 starts touching rail
 0.00 s  ball2 starts touching rail
 0.00 s  ball3 starts touching rail
 0.00 s  ball4 starts touching rail
 0.00 s  pendulum is at its largest at the start, 80.4°
 0.44 s  pendulum first touches ball1
 0.44 s  ball1 starts moving
 0.45 s  pendulum leaves ball1
 0.50 s  ball1 leaves rail
 0.50 s  ball2 leaves rail
 0.50 s  ball1 first touches ball2
 0.50 s  ball2 starts moving
 0.51 s  ball1 leaves ball2
 0.54 s  ball2 touches rail again
 0.57 s  ball1 touches rail again
 0.61 s  ball2 leaves rail
 0.61 s  ball2 first touches ball3
 0.61 s  ball3 starts moving
 0.61 s  ball2 leaves ball3
 0.65 s  ball2 touches rail again
 0.68 s  ball2 comes to rest at (0.31, 0.00, 0.33) m
 0.81 s  ball1 passes 0.29 m from ball4 without touching it: nearest points (0.20, 0.00, 0.33) m and (0.49, 0.00, 0.33) m
 0.82 s  ball3 first touches ball4
 0.82 s  ball4 starts moving
 0.82 s  ball3 leaves ball4
 0.84 s  ball3 comes to rest at (0.46, 0.00, 0.33) m
 1.42 s  pendulum passes 0.40 m from ball4 without touching it: nearest points (0.15, 0.00, 0.35) m and (0.56, 0.00, 0.33) m
 1.42 s  pendulum touches ball1 again
 1.42 s  pendulum leaves ball1
 1.46 s  ball4 comes to rest at (0.59, 0.00, 0.33) m
 1.88 s  ball1 comes to rest at (0.22, 0.00, 0.33) m
 2.52 s  pendulum passes 0.01 m from rail left lip without touching it: nearest points (0.00, 0.03, 0.32) m and (0.00, 0.03, 0.32) m
 2.52 s  pendulum passes 0.01 m from rail right lip without touching it: nearest points (0.00, -0.03, 0.32) m and (0.00, -0.03, 0.32) m
 2.52 s  pendulum passes 0.01 m from rail without touching it: nearest points (0.00, 0.00, 0.31) m and (0.00, 0.00, 0.30) m
 4.45 s  pendulum is at its smallest, -12.3°
 6.00 s  ball2 passes 0.37 m from box (box_near_wall) without touching it: nearest points (0.35, 0.00, 0.32) m and (0.71, 0.00, 0.25) m
 6.00 s  ball3 passes 0.22 m from box (box_near_wall) without touching it: nearest points (0.50, 0.00, 0.32) m and (0.71, 0.00, 0.25) m
 6.00 s  pendulum passes 0.13 m from ball2 without touching it: nearest points (0.16, 0.00, 0.35) m and (0.29, 0.00, 0.33) m
 6.00 s  pendulum passes 0.28 m from ball3 without touching it: nearest points (0.16, 0.00, 0.35) m and (0.44, 0.00, 0.33) m
 6.00 s  ball1 passes 0.45 m from box (box_near_wall) without touching it: nearest points (0.27, 0.00, 0.32) m and (0.71, 0.00, 0.25) m

State every 0.25 s:
0.00 s: pendulum at 80.4°, still; touching nothing | ball1 at (0.07, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.21, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.36, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.52, 0.00, 0.33) m, at rest; touching rail
0.25 s: pendulum at 51.6°, turning -222°/s; touching nothing | ball1 at (0.07, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.21, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.36, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.52, 0.00, 0.33) m, at rest; touching rail
0.50 s: pendulum at 2.9°, turning +70°/s; touching nothing | ball1 at (0.15, 0.00, 0.33) m, moving 1.38 m/s (vx +1.38, vy -0.00, vz +0.03); touching nothing | ball2 at (0.21, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.36, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.52, 0.00, 0.33) m, at rest; touching rail
0.75 s: pendulum at 16.1°, turning +27°/s; touching nothing | ball1 at (0.17, 0.00, 0.33) m, moving 0.05 m/s (vx +0.05, vy -0.00, vz -0.00); touching rail | ball2 at (0.31, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.43, 0.00, 0.33) m, moving 0.41 m/s (vx +0.40, vy -0.00, vz -0.01); touching nothing | ball4 at (0.52, 0.00, 0.33) m, at rest; touching rail
1.00 s: pendulum at 14.2°, turning -41°/s; touching nothing | ball1 at (0.17, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.31, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.46, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.55, 0.00, 0.33) m, moving 0.14 m/s (vx +0.14, vy +0.00, vz -0.00); touching rail
1.25 s: pendulum at -1.1°, turning -71°/s; touching nothing | ball1 at (0.18, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.58, 0.00, 0.33) m, moving 0.08 m/s (vx +0.08, vy +0.00, vz -0.00); touching rail
1.50 s: pendulum at -10.3°, turning +27°/s; touching nothing | ball1 at (0.19, 0.00, 0.33) m, moving 0.12 m/s (vx +0.12, vy -0.00, vz -0.00); touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.59, 0.00, 0.33) m, at rest; touching rail
1.75 s: pendulum at 0.2°, turning +50°/s; touching nothing | ball1 at (0.21, 0.00, 0.33) m, moving 0.07 m/s (vx +0.07, vy -0.00, vz -0.00); touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail
2.00 s: pendulum at 10.5°, turning +26°/s; touching nothing | ball1 at (0.23, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail
2.25 s: pendulum at 10.9°, turning -23°/s; touching nothing | ball1 at (0.23, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail
2.50 s: pendulum at 1.0°, turning -50°/s; touching nothing | ball1 at (0.24, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail
2.75 s: pendulum at -9.9°, turning -30°/s; touching nothing | ball1 at (0.24, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail
3.00 s: pendulum at -11.4°, turning +18°/s; touching nothing | ball1 at (0.24, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail
3.25 s: pendulum at -2.2°, turning +49°/s; touching nothing | ball1 at (0.24, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail
3.50 s: pendulum at 9.1°, turning +33°/s; touching nothing | ball1 at (0.24, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail
3.75 s: pendulum at 11.8°, turning -14°/s; touching nothing | ball1 at (0.24, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail
4.00 s: pendulum at 3.3°, turning -48°/s; touching nothing | ball1 at (0.24, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail
4.25 s: pendulum at -8.3°, turning -37°/s; touching nothing | ball1 at (0.24, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail
4.50 s: pendulum at -12.1°, turning +9°/s; touching nothing | ball1 at (0.24, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail
4.75 s: pendulum at -4.4°, turning +46°/s; touching nothing | ball1 at (0.24, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail
5.00 s: pendulum at 7.4°, turning +40°/s; touching nothing | ball1 at (0.24, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail
5.25 s: pendulum at 12.2°, turning -4°/s; touching nothing | ball1 at (0.24, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail
5.50 s: pendulum at 5.5°, turning -45°/s; touching nothing | ball1 at (0.24, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail
5.75 s: pendulum at -6.4°, turning -43°/s; touching nothing | ball1 at (0.24, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail
6.00 s: pendulum at -12.3°, still; touching nothing | ball1 at (0.24, 0.00, 0.33) m, at rest; touching rail | ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail | ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail | ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail

At the end (6.00 s):
- pendulum at -12.3°, still; touching nothing
- ball1 at (0.24, 0.00, 0.33) m, at rest; touching rail
- ball2 at (0.32, 0.00, 0.33) m, at rest; touching rail
- ball3 at (0.47, 0.00, 0.33) m, at rest; touching rail
- ball4 at (0.60, 0.00, 0.33) m, at rest; touching rail
</history>
