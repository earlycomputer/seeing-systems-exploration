MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_rod, pendulum_bob; starts at 39.2°, still
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.03) m, at rest

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 39.2°
 0.36 s  pendulum_bob first touches ball
 0.36 s  ball starts moving
 0.41 s  pendulum_bob leaves ball
 1.05 s  ball first touches ramp
 1.06 s  ball leaves floor
 1.52 s  ball first touches cup_wall_near
 1.56 s  ball leaves ramp
 1.66 s  ball leaves cup_wall_near
 1.72 s  ball first touches cup_base
 1.73 s  ball touches floor again
 1.75 s  ball leaves floor
 2.27 s  ball comes to rest at (1.03, 0.00, 0.03) m
 3.50 s  pendulum is at its smallest, -13.0°

State every 0.25 s:
0.00 s: pendulum at 39.2°, still; touching nothing | ball at (0.00, 0.00, 0.03) m, at rest; touching floor
0.25 s: pendulum at 18.3°, turning -151°/s; touching nothing | ball at (0.00, 0.00, 0.02) m, at rest; touching floor
0.50 s: pendulum at -8.9°, turning -42°/s; touching nothing | ball at (0.13, 0.00, 0.02) m, moving 0.90 m/s (vx +0.90, vy -0.00, vz +0.00); touching floor
0.75 s: pendulum at -12.4°, turning +17°/s; touching nothing | ball at (0.35, 0.00, 0.02) m, moving 0.90 m/s (vx +0.90, vy -0.00, vz +0.00); touching floor
1.00 s: pendulum at -2.0°, turning +57°/s; touching nothing | ball at (0.58, 0.00, 0.02) m, moving 0.90 m/s (vx +0.90, vy -0.00, vz +0.00); touching floor
1.25 s: pendulum at 10.7°, turning +33°/s; touching nothing | ball at (0.77, 0.00, 0.05) m, moving 0.65 m/s (vx +0.64, vy -0.00, vz +0.11); touching ramp
1.50 s: pendulum at 11.4°, turning -28°/s; touching nothing | ball at (0.89, 0.00, 0.07) m, moving 0.34 m/s (vx +0.34, vy -0.00, vz +0.06); touching ramp
1.75 s: pendulum at -0.6°, turning -58°/s; touching nothing | ball at (0.96, 0.00, 0.02) m, moving 0.26 m/s (vx +0.24, vy -0.00, vz +0.11); touching cup_base, floor
2.00 s: pendulum at -11.9°, turning -23°/s; touching nothing | ball at (1.01, 0.00, 0.03) m, moving 0.12 m/s (vx +0.12, vy -0.00, vz -0.00); touching cup_base
2.25 s: pendulum at -9.9°, turning +37°/s; touching nothing | ball at (1.03, 0.00, 0.03) m, moving 0.05 m/s (vx +0.05, vy -0.00, vz -0.00); touching cup_base
2.50 s: pendulum at 3.2°, turning +56°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
2.75 s: pendulum at 12.7°, turning +12°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
3.00 s: pendulum at 8.0°, turning -46°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
3.25 s: pendulum at -5.7°, turning -52°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
3.50 s: pendulum at -13.0°, still; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
3.75 s: pendulum at -5.7°, turning +52°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
4.00 s: pendulum at 8.0°, turning +46°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
4.25 s: pendulum at 12.7°, turning -11°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
4.50 s: pendulum at 3.3°, turning -56°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
4.75 s: pendulum at -9.9°, turning -38°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
5.00 s: pendulum at -12.0°, turning +23°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
5.25 s: pendulum at -0.7°, turning +58°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
5.50 s: pendulum at 11.4°, turning +28°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
5.75 s: pendulum at 10.7°, turning -33°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
6.00 s: pendulum at -2.0°, turning -57°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base

At the end (6.00 s):
- pendulum at -2.0°, turning -57°/s; touching nothing
- ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
</history>
