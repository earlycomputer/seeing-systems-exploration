MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), range -60° to 60° as MuJoCo applies it; its geoms: pendulum_rod, pendulum_bob; starts at 31.5°, still
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 31.5°
 0.38 s  pendulum_bob first touches ball
 0.38 s  ball starts moving
 0.40 s  pendulum_bob leaves ball
 0.79 s  pendulum is at its smallest, -23.3°
 1.28 s  ball leaves floor
 1.28 s  ball first touches cup_base
 1.29 s  ball leaves cup_base
 1.36 s  ball touches cup_base again
 1.67 s  ball comes to rest at (0.95, 0.00, 0.04) m

State every 0.25 s:
0.00 s: pendulum at 31.5°, still; touching nothing | ball at (0.00, 0.00, 0.04) m, at rest; touching floor
0.25 s: pendulum at 17.1°, turning -105°/s; touching nothing | ball at (0.00, 0.00, 0.04) m, at rest; touching floor
0.50 s: pendulum at -9.4°, turning -87°/s; touching nothing | ball at (0.12, 0.00, 0.04) m, moving 0.88 m/s (vx +0.88, vy +0.00, vz -0.00); touching floor
0.75 s: pendulum at -23.1°, turning -14°/s; touching nothing | ball at (0.34, 0.00, 0.04) m, moving 0.87 m/s (vx +0.87, vy +0.00, vz -0.00); touching floor
1.00 s: pendulum at -15.3°, turning +71°/s; touching nothing | ball at (0.56, 0.00, 0.04) m, moving 0.87 m/s (vx +0.87, vy +0.00, vz -0.00); touching floor
1.25 s: pendulum at 6.6°, turning +89°/s; touching nothing | ball at (0.78, 0.00, 0.04) m, moving 0.86 m/s (vx +0.86, vy +0.00, vz -0.00); touching floor
1.50 s: pendulum at 22.0°, turning +24°/s; touching nothing | ball at (0.92, 0.00, 0.04) m, moving 0.34 m/s (vx +0.34, vy +0.00, vz -0.01); touching nothing
1.75 s: pendulum at 16.8°, turning -62°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
2.00 s: pendulum at -3.9°, turning -90°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
2.25 s: pendulum at -20.7°, turning -34°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
2.50 s: pendulum at -18.0°, turning +52°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
2.75 s: pendulum at 1.3°, turning +89°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
3.00 s: pendulum at 19.2°, turning +42°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
3.25 s: pendulum at 18.9°, turning -43°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
3.50 s: pendulum at 1.1°, turning -87°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
3.75 s: pendulum at -17.5°, turning -49°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
4.00 s: pendulum at -19.6°, turning +33°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
4.25 s: pendulum at -3.5°, turning +84°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
4.50 s: pendulum at 15.7°, turning +56°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
4.75 s: pendulum at 19.9°, turning -24°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
5.00 s: pendulum at 5.6°, turning -80°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
5.25 s: pendulum at -13.7°, turning -61°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
5.50 s: pendulum at -20.0°, turning +15°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
5.75 s: pendulum at -7.6°, turning +76°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
6.00 s: pendulum at 11.7°, turning +65°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base

At the end (6.00 s):
- pendulum at 11.7°, turning +65°/s; touching nothing
- ball at (0.95, 0.00, 0.04) m, at rest; touching cup_base
</history>
