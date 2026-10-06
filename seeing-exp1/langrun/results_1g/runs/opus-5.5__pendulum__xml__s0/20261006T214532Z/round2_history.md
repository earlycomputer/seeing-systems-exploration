Your expectations, checked against the run (4 of 4 hold):

- holds: pendulum touches ball (first touch at 0.33 s)
- holds: ball touches ramp (first touch at 0.69 s)
- holds: ball touches cup_base (first touch at 1.15 s)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_arm, pendulum_bob; starts at 50.4°, still
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.03) m, at rest

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 50.4°
 0.33 s  pendulum_bob first touches ball
 0.33 s  ball starts moving
 0.34 s  ball leaves floor
 0.37 s  ball touches floor again
 0.41 s  pendulum_bob leaves ball
 0.65 s  pendulum is at its smallest, -43.1°
 0.69 s  ball first touches ramp
 0.70 s  ball leaves floor
 1.02 s  ball leaves ramp
 1.04 s  ball is at the top of its flight, at (0.94, 0.00, 0.09) m
 1.14 s  ball first touches cup_back
 1.15 s  ball first touches cup_base
 1.23 s  ball leaves cup_back
 1.25 s  ball comes to rest at (1.04, 0.00, 0.03) m
 4.57 s  pendulum passes 0.30 m from ramp without touching it: nearest points (0.25, 0.00, 0.12) m and (0.52, 0.00, 0.00) m

State every 0.25 s:
0.00 s: pendulum at 50.4°, still; touching nothing | ball at (0.00, 0.00, 0.03) m, at rest; touching floor
0.25 s: pendulum at 18.9°, turning -224°/s; touching nothing | ball at (0.00, 0.00, 0.02) m, at rest; touching floor
0.50 s: pendulum at -31.9°, turning -140°/s; touching nothing | ball at (0.24, 0.00, 0.02) m, moving 1.44 m/s (vx +1.44, vy -0.00, vz +0.00); touching floor
0.75 s: pendulum at -38.7°, turning +90°/s; touching nothing | ball at (0.59, 0.00, 0.04) m, moving 1.36 m/s (vx +1.34, vy -0.00, vz +0.24); touching ramp
1.00 s: pendulum at 4.1°, turning +209°/s; touching nothing | ball at (0.90, 0.00, 0.09) m, moving 1.08 m/s (vx +1.07, vy -0.00, vz +0.17); touching ramp
1.25 s: pendulum at 41.5°, turning +56°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, moving 0.05 m/s (vx -0.05, vy -0.00, vz +0.01); touching cup_base
1.50 s: pendulum at 25.9°, turning -166°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
1.75 s: pendulum at -23.2°, turning -176°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
2.00 s: pendulum at -42.3°, turning +39°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
2.25 s: pendulum at -7.4°, turning +207°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
2.50 s: pendulum at 37.1°, turning +106°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
2.75 s: pendulum at 34.1°, turning -126°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
3.00 s: pendulum at -12.8°, turning -200°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
3.25 s: pendulum at -43.0°, turning -15°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
3.50 s: pendulum at -18.4°, turning +189°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
3.75 s: pendulum at 30.1°, turning +149°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
4.00 s: pendulum at 39.8°, turning -78°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
4.25 s: pendulum at -1.5°, turning -210°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
4.50 s: pendulum at -40.8°, turning -68°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
4.75 s: pendulum at -28.0°, turning +157°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
5.00 s: pendulum at 21.0°, turning +183°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
5.25 s: pendulum at 42.7°, turning -26°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
5.50 s: pendulum at 10.0°, turning -204°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
5.75 s: pendulum at -35.7°, turning -116°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
6.00 s: pendulum at -35.6°, turning +116°/s; touching nothing | ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base

At the end (6.00 s):
- pendulum at -35.6°, turning +116°/s; touching nothing
- ball at (1.04, 0.00, 0.03) m, at rest; touching cup_base
</history>
