MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum, pendulum rod; starts at 48.0°, still
- ball: free body; its geoms: ball; starts at (0.10, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 48.0°
 0.37 s  pendulum first touches ball
 0.37 s  ball starts moving
 0.55 s  pendulum leaves ball
 2.02 s  pendulum is at its smallest, -21.4°
 4.80 s  ball first touches cup_near_wall
 4.80 s  ball comes to rest at (0.86, 0.00, 0.04) m
 5.68 s  ball leaves cup_near_wall

State every 0.25 s:
0.00 s: pendulum at 48.0°, still; touching nothing | ball at (0.10, 0.00, 0.04) m, at rest; touching floor
0.25 s: pendulum at 21.9°, turning -189°/s; touching nothing | ball at (0.10, 0.00, 0.04) m, at rest; touching floor
0.50 s: pendulum at -17.0°, turning -62°/s; touching ball | ball at (0.22, 0.00, 0.04) m, moving 0.46 m/s (vx +0.46, vy -0.00, vz +0.00); touching floor, pendulum
0.75 s: pendulum at -18.9°, turning +45°/s; touching nothing | ball at (0.29, 0.00, 0.04) m, moving 0.24 m/s (vx +0.24, vy -0.00, vz -0.00); touching floor
1.00 s: pendulum at 1.1°, turning +98°/s; touching nothing | ball at (0.35, 0.00, 0.04) m, moving 0.23 m/s (vx +0.23, vy -0.00, vz -0.00); touching floor
1.25 s: pendulum at 19.9°, turning +36°/s; touching nothing | ball at (0.40, 0.00, 0.04) m, moving 0.21 m/s (vx +0.21, vy -0.00, vz -0.00); touching floor
1.50 s: pendulum at 15.6°, turning -66°/s; touching nothing | ball at (0.45, 0.00, 0.04) m, moving 0.20 m/s (vx +0.20, vy -0.00, vz -0.00); touching floor
1.75 s: pendulum at -6.8°, turning -93°/s; touching nothing | ball at (0.50, 0.00, 0.04) m, moving 0.19 m/s (vx +0.19, vy -0.00, vz -0.00); touching floor
2.00 s: pendulum at -21.3°, turning -11°/s; touching nothing | ball at (0.55, 0.00, 0.04) m, moving 0.17 m/s (vx +0.17, vy -0.00, vz -0.00); touching floor
2.25 s: pendulum at -11.1°, turning +83°/s; touching nothing | ball at (0.59, 0.00, 0.04) m, moving 0.16 m/s (vx +0.16, vy -0.00, vz -0.00); touching floor
2.50 s: pendulum at 12.0°, turning +81°/s; touching nothing | ball at (0.63, 0.00, 0.04) m, moving 0.15 m/s (vx +0.15, vy -0.00, vz -0.00); touching floor
2.75 s: pendulum at 21.1°, turning -15°/s; touching nothing | ball at (0.66, 0.00, 0.04) m, moving 0.14 m/s (vx +0.14, vy -0.00, vz -0.00); touching floor
3.00 s: pendulum at 5.7°, turning -94°/s; touching nothing | ball at (0.69, 0.00, 0.04) m, moving 0.13 m/s (vx +0.13, vy -0.00, vz -0.00); touching floor
3.25 s: pendulum at -16.4°, turning -63°/s; touching nothing | ball at (0.72, 0.00, 0.04) m, moving 0.12 m/s (vx +0.12, vy -0.00, vz -0.00); touching floor
3.50 s: pendulum at -19.4°, turning +41°/s; touching nothing | ball at (0.75, 0.00, 0.04) m, moving 0.11 m/s (vx +0.11, vy -0.00, vz -0.00); touching floor
3.75 s: pendulum at 0.1°, turning +98°/s; touching nothing | ball at (0.78, 0.00, 0.04) m, moving 0.10 m/s (vx +0.10, vy +0.00, vz -0.00); touching floor
4.00 s: pendulum at 19.5°, turning +41°/s; touching nothing | ball at (0.80, 0.00, 0.04) m, moving 0.09 m/s (vx +0.09, vy +0.00, vz -0.00); touching floor
4.25 s: pendulum at 16.3°, turning -63°/s; touching nothing | ball at (0.82, 0.00, 0.04) m, moving 0.08 m/s (vx +0.08, vy +0.00, vz -0.00); touching floor
4.50 s: pendulum at -5.8°, turning -94°/s; touching nothing | ball at (0.84, 0.00, 0.04) m, moving 0.07 m/s (vx +0.07, vy +0.00, vz -0.00); touching floor
4.75 s: pendulum at -21.1°, turning -16°/s; touching nothing | ball at (0.86, 0.00, 0.04) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz -0.00); touching floor
5.00 s: pendulum at -11.9°, turning +81°/s; touching nothing | ball at (0.86, 0.00, 0.04) m, at rest; touching cup_near_wall, floor
5.25 s: pendulum at 11.2°, turning +83°/s; touching nothing | ball at (0.86, 0.00, 0.04) m, at rest; touching cup_near_wall, floor
5.50 s: pendulum at 21.3°, turning -11°/s; touching nothing | ball at (0.86, 0.00, 0.04) m, at rest; touching cup_near_wall, floor
5.75 s: pendulum at 6.7°, turning -93°/s; touching nothing | ball at (0.86, 0.00, 0.04) m, at rest; touching floor
6.00 s: pendulum at -15.7°, turning -67°/s; touching nothing | ball at (0.86, 0.00, 0.04) m, at rest; touching floor

At the end (6.00 s):
- pendulum at -15.7°, turning -67°/s; touching nothing
- ball at (0.86, 0.00, 0.04) m, at rest; touching floor
</history>
