MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum, pendulum rod; starts at 80.0°, still
- ball: free body; its geoms: ball; starts at (0.07, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 80.0°
 0.40 s  pendulum first touches ball
 0.40 s  ball starts moving
 0.43 s  pendulum leaves ball
 0.70 s  pendulum is at its smallest, -12.1°
 1.26 s  ball leaves floor
 1.26 s  ball first touches cup_near_wall
 1.28 s  ball leaves cup_near_wall
 1.37 s  ball first touches cup_base
 1.66 s  ball comes to rest at (1.06, 0.00, 0.04) m

State every 0.25 s:
0.00 s: pendulum at 80.0°, still; touching nothing | ball at (0.07, 0.00, 0.04) m, at rest; touching floor
0.25 s: pendulum at 45.8°, turning -260°/s; touching nothing | ball at (0.07, 0.00, 0.04) m, at rest; touching floor
0.50 s: pendulum at -7.5°, turning -42°/s; touching nothing | ball at (0.18, 0.00, 0.04) m, moving 0.99 m/s (vx +0.99, vy +0.00, vz -0.00); touching floor
0.75 s: pendulum at -11.8°, turning +11°/s; touching nothing | ball at (0.42, 0.00, 0.04) m, moving 0.99 m/s (vx +0.99, vy +0.00, vz -0.00); touching floor
1.00 s: pendulum at -3.0°, turning +52°/s; touching nothing | ball at (0.67, 0.00, 0.04) m, moving 0.99 m/s (vx +0.99, vy +0.00, vz -0.00); touching floor
1.25 s: pendulum at 9.2°, turning +35°/s; touching nothing | ball at (0.92, 0.00, 0.04) m, moving 0.98 m/s (vx +0.98, vy +0.00, vz -0.00); touching floor
1.50 s: pendulum at 11.1°, turning -21°/s; touching nothing | ball at (1.03, 0.00, 0.04) m, moving 0.29 m/s (vx +0.29, vy +0.00, vz -0.02); touching nothing
1.75 s: pendulum at 0.7°, turning -53°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
2.00 s: pendulum at -10.5°, turning -27°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
2.25 s: pendulum at -10.0°, turning +30°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
2.50 s: pendulum at 1.5°, turning +53°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
2.75 s: pendulum at 11.4°, turning +18°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
3.00 s: pendulum at 8.6°, turning -37°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
3.25 s: pendulum at -3.7°, turning -51°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
3.50 s: pendulum at -11.9°, turning -8°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
3.75 s: pendulum at -6.9°, turning +44°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
4.00 s: pendulum at 5.8°, turning +47°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
4.25 s: pendulum at 12.0°, turning -2°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
4.50 s: pendulum at 4.9°, turning -49°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
4.75 s: pendulum at -7.7°, turning -41°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
5.00 s: pendulum at -11.7°, turning +12°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
5.25 s: pendulum at -2.8°, turning +52°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
5.50 s: pendulum at 9.3°, turning +34°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
5.75 s: pendulum at 11.0°, turning -21°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
6.00 s: pendulum at 0.5°, turning -54°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base

At the end (6.00 s):
- pendulum at 0.5°, turning -54°/s; touching nothing
- ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
</history>
