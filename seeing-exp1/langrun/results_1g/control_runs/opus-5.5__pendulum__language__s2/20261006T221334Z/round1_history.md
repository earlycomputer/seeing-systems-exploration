MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pivot about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_bob, pendulum_rod; starts at 23.0°, still
- ball: free body; its geoms: ball; starts at (0.07, 0.00, 0.03) m, at rest

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 23.0°
 0.37 s  pendulum_bob first touches ball
 0.37 s  ball starts moving
 0.43 s  pendulum_bob leaves ball
 2.09 s  pendulum is at its smallest, -10.0°
 2.35 s  ball leaves floor
 2.35 s  ball first touches cup_near_wall
 2.42 s  ball first touches cup_base
 2.49 s  ball comes to rest at (0.95, 0.00, 0.03) m
 2.50 s  ball leaves cup_near_wall

State every 0.25 s:
0.00 s: pendulum at 23.0°, still; touching nothing | ball at (0.07, 0.00, 0.03) m, at rest; touching floor
0.25 s: pendulum at 10.4°, turning -90°/s; touching nothing | ball at (0.07, 0.00, 0.03) m, at rest; touching floor
0.50 s: pendulum at -7.4°, turning -30°/s; touching nothing | ball at (0.13, 0.00, 0.03) m, moving 0.44 m/s (vx +0.44, vy +0.00, vz -0.00); touching floor
0.75 s: pendulum at -9.4°, turning +16°/s; touching nothing | ball at (0.24, 0.00, 0.03) m, moving 0.44 m/s (vx +0.44, vy +0.00, vz -0.00); touching floor
1.00 s: pendulum at -1.0°, turning +44°/s; touching nothing | ball at (0.35, 0.00, 0.03) m, moving 0.43 m/s (vx +0.43, vy +0.00, vz -0.00); touching floor
1.25 s: pendulum at 8.5°, turning +24°/s; touching nothing | ball at (0.46, 0.00, 0.03) m, moving 0.43 m/s (vx +0.43, vy +0.00, vz -0.00); touching floor
1.50 s: pendulum at 8.6°, turning -23°/s; touching nothing | ball at (0.57, 0.00, 0.03) m, moving 0.43 m/s (vx +0.43, vy +0.00, vz -0.00); touching floor
1.75 s: pendulum at -0.8°, turning -44°/s; touching nothing | ball at (0.67, 0.00, 0.03) m, moving 0.42 m/s (vx +0.42, vy +0.00, vz -0.00); touching floor
2.00 s: pendulum at -9.3°, turning -17°/s; touching nothing | ball at (0.78, 0.00, 0.03) m, moving 0.42 m/s (vx +0.42, vy +0.00, vz -0.00); touching floor
2.25 s: pendulum at -7.5°, turning +29°/s; touching nothing | ball at (0.88, 0.00, 0.03) m, moving 0.42 m/s (vx +0.42, vy +0.00, vz -0.00); touching floor
2.50 s: pendulum at 2.6°, turning +43°/s; touching nothing | ball at (0.95, 0.00, 0.03) m, at rest; touching cup_base
2.75 s: pendulum at 9.9°, turning +9°/s; touching nothing | ball at (0.95, 0.00, 0.03) m, at rest; touching cup_base
3.00 s: pendulum at 6.2°, turning -35°/s; touching nothing | ball at (0.95, 0.00, 0.03) m, at rest; touching cup_base
3.25 s: pendulum at -4.3°, turning -40°/s; touching nothing | ball at (0.95, 0.00, 0.03) m, at rest; touching cup_base
3.50 s: pendulum at -10.0°, still; touching nothing | ball at (0.95, 0.00, 0.03) m, at rest; touching cup_base
3.75 s: pendulum at -4.6°, turning +39°/s; touching nothing | ball at (0.95, 0.00, 0.03) m, at rest; touching cup_base
4.00 s: pendulum at 5.9°, turning +36°/s; touching nothing | ball at (0.95, 0.00, 0.03) m, at rest; touching cup_base
4.25 s: pendulum at 9.9°, turning -7°/s; touching nothing | ball at (0.95, 0.00, 0.03) m, at rest; touching cup_base
4.50 s: pendulum at 2.9°, turning -43°/s; touching nothing | ball at (0.95, 0.00, 0.03) m, at rest; touching cup_base
4.75 s: pendulum at -7.3°, turning -31°/s; touching nothing | ball at (0.95, 0.00, 0.03) m, at rest; touching cup_base
5.00 s: pendulum at -9.4°, turning +15°/s; touching nothing | ball at (0.95, 0.00, 0.03) m, at rest; touching cup_base
5.25 s: pendulum at -1.1°, turning +44°/s; touching nothing | ball at (0.95, 0.00, 0.03) m, at rest; touching cup_base
5.50 s: pendulum at 8.4°, turning +24°/s; touching nothing | ball at (0.95, 0.00, 0.03) m, at rest; touching cup_base
5.75 s: pendulum at 8.7°, turning -22°/s; touching nothing | ball at (0.95, 0.00, 0.03) m, at rest; touching cup_base
6.00 s: pendulum at -0.7°, turning -44°/s; touching nothing | ball at (0.95, 0.00, 0.03) m, at rest; touching cup_base

At the end (6.00 s):
- pendulum at -0.7°, turning -44°/s; touching nothing
- ball at (0.95, 0.00, 0.03) m, at rest; touching cup_base
</history>
