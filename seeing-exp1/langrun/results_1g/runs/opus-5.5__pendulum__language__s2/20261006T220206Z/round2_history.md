Your expectations, checked against the run (2 of 2 hold):

- holds: ball touches pendulum (first touch at 0.35 s)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pivot about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_bob, pendulum_rod; starts at 40.0°, still
- ball: free body; its geoms: ball; starts at (0.06, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 40.0°
 0.35 s  pendulum_bob first touches ball
 0.35 s  ball starts moving
 0.39 s  pendulum_bob leaves ball
 0.68 s  pendulum is at its smallest, -28.8°
 1.08 s  ball leaves floor
 1.08 s  ball first touches cup_near_wall
 1.11 s  ball leaves cup_near_wall
 1.21 s  ball first touches cup_base
 1.21 s  ball touches floor again
 1.23 s  ball leaves floor
 1.34 s  ball leaves cup_base
 1.34 s  ball first touches cup_far_wall
 1.39 s  ball leaves cup_far_wall
 1.40 s  ball touches cup_base again
 2.65 s  ball touches cup_near_wall again
 2.65 s  ball comes to rest at (1.00, 0.00, 0.04) m
 2.68 s  ball leaves cup_near_wall

State every 0.25 s:
0.00 s: pendulum at 40.0°, still; touching nothing | ball at (0.06, 0.00, 0.04) m, at rest; touching floor
0.25 s: pendulum at 16.7°, turning -166°/s; touching nothing | ball at (0.06, 0.00, 0.03) m, at rest; touching floor
0.50 s: pendulum at -19.6°, turning -98°/s; touching nothing | ball at (0.24, 0.00, 0.03) m, moving 1.18 m/s (vx +1.18, vy -0.00, vz +0.00); touching floor
0.75 s: pendulum at -27.2°, turning +43°/s; touching nothing | ball at (0.54, 0.00, 0.03) m, moving 1.18 m/s (vx +1.18, vy -0.00, vz -0.00); touching floor
1.00 s: pendulum at -2.4°, turning +133°/s; touching nothing | ball at (0.83, 0.00, 0.03) m, moving 1.17 m/s (vx +1.17, vy -0.00, vz -0.00); touching floor
1.25 s: pendulum at 25.3°, turning +63°/s; touching nothing | ball at (1.05, 0.00, 0.04) m, moving 0.75 m/s (vx +0.75, vy -0.00, vz +0.04); touching cup_base
1.50 s: pendulum at 22.8°, turning -81°/s; touching nothing | ball at (1.11, 0.00, 0.04) m, moving 0.10 m/s (vx -0.10, vy -0.00, vz +0.00); touching cup_base
1.75 s: pendulum at -7.0°, turning -130°/s; touching nothing | ball at (1.08, 0.00, 0.04) m, moving 0.10 m/s (vx -0.10, vy -0.00, vz +0.00); touching cup_base
2.00 s: pendulum at -28.4°, turning -23°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, moving 0.10 m/s (vx -0.10, vy -0.00, vz +0.00); touching cup_base
2.25 s: pendulum at -16.0°, turning +111°/s; touching nothing | ball at (1.03, 0.00, 0.04) m, moving 0.10 m/s (vx -0.10, vy -0.00, vz +0.00); touching cup_base
2.50 s: pendulum at 15.6°, turning +112°/s; touching nothing | ball at (1.01, 0.00, 0.04) m, moving 0.10 m/s (vx -0.10, vy -0.00, vz +0.00); touching cup_base
2.75 s: pendulum at 28.4°, turning -20°/s; touching nothing | ball at (1.00, 0.00, 0.04) m, at rest; touching cup_base
3.00 s: pendulum at 7.4°, turning -129°/s; touching nothing | ball at (1.01, 0.00, 0.04) m, at rest; touching cup_base
3.25 s: pendulum at -22.5°, turning -83°/s; touching nothing | ball at (1.02, 0.00, 0.04) m, at rest; touching cup_base
3.50 s: pendulum at -25.5°, turning +61°/s; touching nothing | ball at (1.03, 0.00, 0.04) m, at rest; touching cup_base
3.75 s: pendulum at 1.9°, turning +133°/s; touching nothing | ball at (1.03, 0.00, 0.04) m, at rest; touching cup_base
4.00 s: pendulum at 27.1°, turning +46°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, at rest; touching cup_base
4.25 s: pendulum at 19.9°, turning -95°/s; touching nothing | ball at (1.05, 0.00, 0.04) m, at rest; touching cup_base
4.50 s: pendulum at -11.1°, turning -123°/s; touching nothing | ball at (1.06, 0.00, 0.04) m, at rest; touching cup_base
4.75 s: pendulum at -28.8°, turning -3°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_base
5.00 s: pendulum at -12.2°, turning +121°/s; touching nothing | ball at (1.08, 0.00, 0.04) m, at rest; touching cup_base
5.25 s: pendulum at 19.0°, turning +100°/s; touching nothing | ball at (1.09, 0.00, 0.04) m, at rest; touching cup_base
5.50 s: pendulum at 27.5°, turning -39°/s; touching nothing | ball at (1.09, 0.00, 0.04) m, at rest; touching cup_base
5.75 s: pendulum at 3.2°, turning -133°/s; touching nothing | ball at (1.10, 0.00, 0.04) m, at rest; touching cup_base
6.00 s: pendulum at -24.9°, turning -67°/s; touching nothing | ball at (1.11, 0.00, 0.04) m, at rest; touching cup_base

At the end (6.00 s):
- pendulum at -24.9°, turning -67°/s; touching nothing
- ball at (1.11, 0.00, 0.04) m, at rest; touching cup_base
</history>
