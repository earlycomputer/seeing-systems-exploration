MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_rod, pendulum_bob; starts at 45.8°, still
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 45.8°
 0.39 s  pendulum_bob first touches ball
 0.39 s  ball starts moving
 0.41 s  pendulum_bob leaves ball
 0.76 s  pendulum is at its smallest, -27.8°
 1.00 s  ball leaves floor
 1.00 s  ball first touches cup_entry_08
 1.01 s  ball leaves cup_entry_08
 1.11 s  ball first touches cup_inner_floor
 1.11 s  ball first touches cup_base
 1.11 s  ball leaves cup_base
 1.11 s  ball leaves cup_inner_floor
 1.17 s  ball touches cup_inner_floor again
 1.17 s  ball leaves cup_inner_floor
 1.21 s  ball touches cup_inner_floor again
 1.22 s  ball leaves cup_inner_floor
 1.25 s  ball touches cup_inner_floor again
 1.45 s  ball comes to rest at (1.07, 0.00, 0.04) m

State every 0.25 s:
0.00 s: pendulum at 45.8°, still; touching nothing | ball at (0.00, 0.00, 0.04) m, at rest; touching floor
0.25 s: pendulum at 24.4°, turning -157°/s; touching nothing | ball at (0.00, 0.00, 0.04) m, at rest; touching floor
0.50 s: pendulum at -13.1°, turning -104°/s; touching nothing | ball at (0.16, 0.00, 0.04) m, moving 1.32 m/s (vx +1.32, vy +0.00, vz -0.03); touching nothing
0.75 s: pendulum at -27.8°, turning -5°/s; touching nothing | ball at (0.48, 0.00, 0.04) m, moving 1.29 m/s (vx +1.29, vy +0.00, vz +0.02); touching floor
1.00 s: pendulum at -15.0°, turning +97°/s; touching nothing | ball at (0.80, 0.00, 0.04) m, moving 1.13 m/s (vx +1.09, vy +0.00, vz +0.30); touching cup_entry_08, floor
1.25 s: pendulum at 12.3°, turning +101°/s; touching nothing | ball at (1.01, 0.00, 0.04) m, moving 0.56 m/s (vx +0.56, vy +0.00, vz +0.00); touching cup_inner_floor
1.50 s: pendulum at 26.8°, turning +5°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
1.75 s: pendulum at 14.6°, turning -93°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
2.00 s: pendulum at -11.7°, turning -98°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
2.25 s: pendulum at -25.8°, turning -6°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
2.50 s: pendulum at -14.2°, turning +89°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
2.75 s: pendulum at 11.2°, turning +94°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
3.00 s: pendulum at 24.9°, turning +6°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
3.25 s: pendulum at 13.7°, turning -86°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
3.50 s: pendulum at -10.8°, turning -91°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
3.75 s: pendulum at -24.0°, turning -6°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
4.00 s: pendulum at -13.2°, turning +83°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
4.25 s: pendulum at 10.5°, turning +88°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
4.50 s: pendulum at 23.1°, turning +5°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
4.75 s: pendulum at 12.6°, turning -80°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
5.00 s: pendulum at -10.2°, turning -84°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
5.25 s: pendulum at -22.3°, turning -4°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
5.50 s: pendulum at -12.1°, turning +78°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
5.75 s: pendulum at 9.9°, turning +81°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
6.00 s: pendulum at 21.5°, turning +4°/s; touching nothing | ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor

At the end (6.00 s):
- pendulum at 21.5°, turning +4°/s; touching nothing
- ball at (1.07, 0.00, 0.04) m, at rest; touching cup_inner_floor
</history>
