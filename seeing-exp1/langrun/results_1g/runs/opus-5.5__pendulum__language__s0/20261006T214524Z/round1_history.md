Your expectations, checked against the run (2 of 2 hold):

- holds: ball touches pendulum (first touch at 0.37 s)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum, pendulum rod; starts at 40.0°, still
- ball: free body; its geoms: ball; starts at (0.06, 0.00, 0.03) m, at rest

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 40.0°
 0.37 s  pendulum first touches ball
 0.37 s  ball starts moving
 0.41 s  pendulum leaves ball
 0.69 s  pendulum is at its smallest, -18.0°
 1.19 s  ball leaves floor
 1.19 s  ball first touches cup_near_wall
 1.21 s  ball leaves cup_near_wall
 1.30 s  ball first touches cup_base
 1.51 s  ball comes to rest at (1.02, 0.00, 0.03) m

State every 0.25 s:
0.00 s: pendulum at 40.0°, still; touching nothing | ball at (0.06, 0.00, 0.03) m, at rest; touching floor
0.25 s: pendulum at 18.9°, turning -153°/s; touching nothing | ball at (0.06, 0.00, 0.03) m, at rest; touching floor
0.50 s: pendulum at -11.9°, turning -60°/s; touching nothing | ball at (0.20, 0.00, 0.03) m, moving 1.06 m/s (vx +1.06, vy +0.00, vz +0.00); touching floor
0.75 s: pendulum at -17.4°, turning +20°/s; touching nothing | ball at (0.47, 0.00, 0.03) m, moving 1.04 m/s (vx +1.04, vy +0.00, vz -0.00); touching floor
1.00 s: pendulum at -3.8°, turning +78°/s; touching nothing | ball at (0.72, 0.00, 0.03) m, moving 1.01 m/s (vx +1.01, vy +0.00, vz -0.00); touching floor
1.25 s: pendulum at 14.1°, turning +50°/s; touching nothing | ball at (0.95, 0.00, 0.04) m, moving 0.50 m/s (vx +0.50, vy +0.00, vz +0.02); touching nothing
1.50 s: pendulum at 16.4°, turning -33°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, moving 0.06 m/s (vx +0.06, vy +0.00, vz +0.00); touching cup_base
1.75 s: pendulum at 0.6°, turning -80°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base
2.00 s: pendulum at -15.8°, turning -38°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base
2.25 s: pendulum at -14.8°, turning +45°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base
2.50 s: pendulum at 2.6°, turning +79°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base
2.75 s: pendulum at 17.1°, turning +25°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base
3.00 s: pendulum at 12.8°, turning -56°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base
3.25 s: pendulum at -5.7°, turning -76°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base
3.50 s: pendulum at -17.8°, turning -12°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base
3.75 s: pendulum at -10.3°, turning +65°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base
4.00 s: pendulum at 8.6°, turning +70°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base
4.25 s: pendulum at 18.0°, turning -2°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base
4.50 s: pendulum at 7.6°, turning -72°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base
4.75 s: pendulum at -11.2°, turning -63°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base
5.00 s: pendulum at -17.6°, turning +16°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base
5.25 s: pendulum at -4.6°, turning +77°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base
5.50 s: pendulum at 13.5°, turning +53°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base
5.75 s: pendulum at 16.7°, turning -29°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base
6.00 s: pendulum at 1.5°, turning -80°/s; touching nothing | ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base

At the end (6.00 s):
- pendulum at 1.5°, turning -80°/s; touching nothing
- ball at (1.02, 0.00, 0.03) m, at rest; touching cup_base
</history>
