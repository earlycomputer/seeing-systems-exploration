Your expectations, checked against the run (1 of 2 hold):

- holds: ball touches pendulum (first touch at 0.34 s)
- DOES NOT HOLD: ball comes to rest in cup (ball is still moving at the end (0.06 m/s), outside cup)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pivot about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_bob, pendulum_rod; starts at 30.0°, still
- ball: free body; its geoms: ball; starts at (0.06, 0.00, 0.03) m, at rest

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 30.0°
 0.34 s  pendulum_bob first touches ball
 0.34 s  ball starts moving
 0.48 s  pendulum_bob leaves ball
 4.54 s  pendulum is at its smallest, -6.1°
 6.00 s  ball is still moving at the end, 0.06 m/s
 6.00 s  ball passes 0.50 m from cup (cup_near_wall) without touching it: nearest points (0.45, 0.00, 0.03) m and (0.95, 0.00, 0.01) m

State every 0.25 s:
0.00 s: pendulum at 30.0°, still; touching nothing | ball at (0.06, 0.00, 0.03) m, at rest; touching floor
0.25 s: pendulum at 12.0°, turning -127°/s; touching nothing | ball at (0.06, 0.00, 0.03) m, at rest; touching floor
0.50 s: pendulum at -6.0°, turning -4°/s; touching nothing | ball at (0.11, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching floor
0.75 s: pendulum at -3.1°, turning +25°/s; touching nothing | ball at (0.12, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching floor
1.00 s: pendulum at 3.6°, turning +23°/s; touching nothing | ball at (0.14, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching floor
1.25 s: pendulum at 5.9°, turning -7°/s; touching nothing | ball at (0.15, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor
1.50 s: pendulum at 0.9°, turning -28°/s; touching nothing | ball at (0.16, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor
1.75 s: pendulum at -5.2°, turning -15°/s; touching nothing | ball at (0.18, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor
2.00 s: pendulum at -4.9°, turning +17°/s; touching nothing | ball at (0.19, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor
2.25 s: pendulum at 1.4°, turning +28°/s; touching nothing | ball at (0.21, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching floor
2.50 s: pendulum at 6.0°, turning +5°/s; touching nothing | ball at (0.22, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching floor
2.75 s: pendulum at 3.2°, turning -24°/s; touching nothing | ball at (0.24, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching floor
3.00 s: pendulum at -3.5°, turning -24°/s; touching nothing | ball at (0.25, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching floor
3.25 s: pendulum at -6.0°, turning +6°/s; touching nothing | ball at (0.27, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching floor
3.50 s: pendulum at -1.1°, turning +28°/s; touching nothing | ball at (0.28, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching floor
3.75 s: pendulum at 5.1°, turning +16°/s; touching nothing | ball at (0.29, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching floor
4.00 s: pendulum at 5.0°, turning -16°/s; touching nothing | ball at (0.31, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor
4.25 s: pendulum at -1.3°, turning -28°/s; touching nothing | ball at (0.32, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor
4.50 s: pendulum at -6.0°, turning -5°/s; touching nothing | ball at (0.34, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor
4.75 s: pendulum at -3.4°, turning +24°/s; touching nothing | ball at (0.35, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor
5.00 s: pendulum at 3.4°, turning +24°/s; touching nothing | ball at (0.37, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor
5.25 s: pendulum at 6.0°, turning -5°/s; touching nothing | ball at (0.38, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching floor
5.50 s: pendulum at 1.2°, turning -28°/s; touching nothing | ball at (0.39, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching floor
5.75 s: pendulum at -5.1°, turning -16°/s; touching nothing | ball at (0.41, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz +0.00); touching floor
6.00 s: pendulum at -5.1°, turning +16°/s; touching nothing | ball at (0.42, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching floor

At the end (6.00 s):
- pendulum at -5.1°, turning +16°/s; touching nothing
- ball at (0.42, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching floor
</history>
