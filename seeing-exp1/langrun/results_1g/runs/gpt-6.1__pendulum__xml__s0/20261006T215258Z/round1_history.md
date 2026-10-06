Your expectations, checked against the run (3 of 3 hold):

- holds: ball touches pendulum (first touch at 0.42 s)
- holds: ball touches cup_entry_ramp (first touch at 1.27 s)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_arm, pendulum_bob; starts at 25.2°, still
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.04) m, at rest

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 25.2°
 0.42 s  ball leaves floor
 0.42 s  pendulum_bob first touches ball
 0.42 s  ball starts moving
 0.43 s  pendulum_bob leaves ball
 0.48 s  ball touches floor again
 0.48 s  ball leaves floor
 0.53 s  ball touches floor again
 0.53 s  ball leaves floor
 0.56 s  ball touches floor again
 0.81 s  pendulum is at its smallest, -20.3°
 1.27 s  ball leaves floor
 1.27 s  ball first touches cup_entry_ramp
 1.45 s  ball first touches cup_lip_180
 1.45 s  ball leaves cup_lip_180
 1.49 s  ball leaves cup_entry_ramp
 1.51 s  ball touches cup_lip_180 again
 1.51 s  ball leaves cup_lip_180
 1.54 s  ball first touches cup_bottom
 2.05 s  ball comes to rest at (1.04, 0.00, 0.04) m

State every 0.25 s:
0.00 s: pendulum at 25.2°, still; touching nothing | ball at (0.00, 0.00, 0.04) m, at rest; touching floor
0.25 s: pendulum at 14.3°, turning -80°/s; touching nothing | ball at (0.00, 0.00, 0.03) m, at rest; touching floor
0.50 s: pendulum at -7.5°, turning -74°/s; touching nothing | ball at (0.09, 0.00, 0.04) m, moving 1.07 m/s (vx +1.07, vy -0.00, vz +0.02); touching nothing
0.75 s: pendulum at -19.8°, turning -18°/s; touching nothing | ball at (0.30, 0.00, 0.03) m, moving 0.78 m/s (vx +0.78, vy -0.00, vz +0.00); touching floor
1.00 s: pendulum at -14.9°, turning +53°/s; touching nothing | ball at (0.50, 0.00, 0.04) m, moving 0.77 m/s (vx +0.77, vy -0.00, vz -0.02); touching nothing
1.25 s: pendulum at 2.9°, turning +78°/s; touching nothing | ball at (0.69, 0.00, 0.03) m, moving 0.77 m/s (vx +0.77, vy -0.00, vz +0.00); touching floor
1.50 s: pendulum at 18.1°, turning +34°/s; touching nothing | ball at (0.86, 0.00, 0.05) m, moving 0.59 m/s (vx +0.59, vy -0.00, vz -0.08); touching nothing
1.75 s: pendulum at 17.5°, turning -38°/s; touching nothing | ball at (0.98, 0.00, 0.04) m, moving 0.36 m/s (vx +0.36, vy -0.00, vz -0.05); touching nothing
2.00 s: pendulum at 1.8°, turning -78°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, moving 0.11 m/s (vx +0.10, vy -0.00, vz -0.03); touching nothing
2.25 s: pendulum at -15.4°, turning -49°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, at rest; touching cup_bottom
2.50 s: pendulum at -19.1°, turning +21°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, at rest; touching cup_bottom
2.75 s: pendulum at -6.2°, turning +73°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, at rest; touching cup_bottom
3.00 s: pendulum at 12.0°, turning +61°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, at rest; touching cup_bottom
3.25 s: pendulum at 19.7°, turning -4°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, at rest; touching cup_bottom
3.50 s: pendulum at 10.3°, turning -65°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, at rest; touching cup_bottom
3.75 s: pendulum at -8.0°, turning -70°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, at rest; touching cup_bottom
4.00 s: pendulum at -19.3°, turning -14°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, at rest; touching cup_bottom
4.25 s: pendulum at -13.8°, turning +54°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, at rest; touching cup_bottom
4.50 s: pendulum at 3.7°, turning +74°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, at rest; touching cup_bottom
4.75 s: pendulum at 17.8°, turning +30°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, at rest; touching cup_bottom
5.00 s: pendulum at 16.4°, turning -40°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, at rest; touching cup_bottom
5.25 s: pendulum at 0.8°, turning -75°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, at rest; touching cup_bottom
5.50 s: pendulum at -15.4°, turning -45°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, at rest; touching cup_bottom
5.75 s: pendulum at -18.2°, turning +24°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, at rest; touching cup_bottom
6.00 s: pendulum at -5.1°, turning +72°/s; touching nothing | ball at (1.04, 0.00, 0.04) m, at rest; touching cup_bottom

At the end (6.00 s):
- pendulum at -5.1°, turning +72°/s; touching nothing
- ball at (1.04, 0.00, 0.04) m, at rest; touching cup_bottom
</history>
