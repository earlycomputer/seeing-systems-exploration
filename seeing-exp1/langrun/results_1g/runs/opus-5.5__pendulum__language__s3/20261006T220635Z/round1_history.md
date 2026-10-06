Your expectations, checked against the run (2 of 2 hold):

- holds: ball touches pendulum (first touch at 0.37 s)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum, pendulum rod; starts at 35.0°, still
- ball: free body; its geoms: ball; starts at (0.08, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 35.0°
 0.37 s  pendulum first touches ball
 0.37 s  ball starts moving
 0.43 s  pendulum leaves ball
 0.70 s  pendulum is at its smallest, -20.9°
 1.40 s  ball leaves floor
 1.40 s  ball first touches cup_near_wall
 1.42 s  ball leaves cup_near_wall
 1.46 s  ball first touches cup_base
 1.77 s  ball first touches cup_far_wall
 1.82 s  ball leaves cup_far_wall
 1.84 s  ball comes to rest at (1.15, 0.00, 0.04) m

State every 0.25 s:
0.00 s: pendulum at 35.0°, still; touching nothing | ball at (0.08, 0.00, 0.04) m, at rest; touching floor
0.25 s: pendulum at 16.3°, turning -135°/s; touching nothing | ball at (0.08, 0.00, 0.04) m, at rest; touching floor
0.50 s: pendulum at -13.4°, turning -71°/s; touching nothing | ball at (0.21, 0.00, 0.04) m, moving 0.82 m/s (vx +0.82, vy +0.00, vz +0.00); touching floor
0.75 s: pendulum at -20.4°, turning +20°/s; touching nothing | ball at (0.41, 0.00, 0.04) m, moving 0.81 m/s (vx +0.81, vy +0.00, vz -0.00); touching floor
1.00 s: pendulum at -5.1°, turning +89°/s; touching nothing | ball at (0.61, 0.00, 0.04) m, moving 0.81 m/s (vx +0.81, vy +0.00, vz -0.00); touching floor
1.25 s: pendulum at 15.8°, turning +60°/s; touching nothing | ball at (0.82, 0.00, 0.04) m, moving 0.81 m/s (vx +0.81, vy +0.00, vz -0.00); touching floor
1.50 s: pendulum at 19.4°, turning -34°/s; touching nothing | ball at (1.00, 0.00, 0.04) m, moving 0.65 m/s (vx +0.65, vy +0.00, vz +0.03); touching cup_base
1.75 s: pendulum at 1.7°, turning -92°/s; touching nothing | ball at (1.14, 0.00, 0.04) m, moving 0.45 m/s (vx +0.45, vy -0.00, vz -0.00); touching cup_base
2.00 s: pendulum at -17.8°, turning -48°/s; touching nothing | ball at (1.15, 0.00, 0.04) m, at rest; touching cup_base
2.25 s: pendulum at -17.8°, turning +48°/s; touching nothing | ball at (1.15, 0.00, 0.04) m, at rest; touching cup_base
2.50 s: pendulum at 1.7°, turning +92°/s; touching nothing | ball at (1.15, 0.00, 0.04) m, at rest; touching cup_base
2.75 s: pendulum at 19.4°, turning +35°/s; touching nothing | ball at (1.15, 0.00, 0.04) m, at rest; touching cup_base
3.00 s: pendulum at 15.8°, turning -60°/s; touching nothing | ball at (1.15, 0.00, 0.04) m, at rest; touching cup_base
3.25 s: pendulum at -5.1°, turning -90°/s; touching nothing | ball at (1.15, 0.00, 0.04) m, at rest; touching cup_base
3.50 s: pendulum at -20.4°, turning -21°/s; touching nothing | ball at (1.15, 0.00, 0.04) m, at rest; touching cup_base
3.75 s: pendulum at -13.4°, turning +71°/s; touching nothing | ball at (1.15, 0.00, 0.04) m, at rest; touching cup_base
4.00 s: pendulum at 8.3°, turning +85°/s; touching nothing | ball at (1.15, 0.00, 0.04) m, at rest; touching cup_base
4.25 s: pendulum at 20.9°, turning +6°/s; touching nothing | ball at (1.15, 0.00, 0.04) m, at rest; touching cup_base
4.50 s: pendulum at 10.6°, turning -79°/s; touching nothing | ball at (1.15, 0.00, 0.04) m, at rest; touching cup_base
4.75 s: pendulum at -11.3°, turning -78°/s; touching nothing | ball at (1.15, 0.00, 0.04) m, at rest; touching cup_base
5.00 s: pendulum at -20.8°, turning +9°/s; touching nothing | ball at (1.15, 0.00, 0.04) m, at rest; touching cup_base
5.25 s: pendulum at -7.5°, turning +86°/s; touching nothing | ball at (1.15, 0.00, 0.04) m, at rest; touching cup_base
5.50 s: pendulum at 14.0°, turning +69°/s; touching nothing | ball at (1.15, 0.00, 0.04) m, at rest; touching cup_base
5.75 s: pendulum at 20.2°, turning -24°/s; touching nothing | ball at (1.15, 0.00, 0.04) m, at rest; touching cup_base
6.00 s: pendulum at 4.3°, turning -90°/s; touching nothing | ball at (1.15, 0.00, 0.04) m, at rest; touching cup_base

At the end (6.00 s):
- pendulum at 4.3°, turning -90°/s; touching nothing
- ball at (1.15, 0.00, 0.04) m, at rest; touching cup_base
</history>
