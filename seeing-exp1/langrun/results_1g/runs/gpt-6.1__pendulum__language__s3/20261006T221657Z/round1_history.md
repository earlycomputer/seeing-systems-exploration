Your expectations, checked against the run (2 of 2 hold):

- holds: ball touches pendulum (first touch at 0.39 s)
- holds: ball comes to rest in cup (ball at rest inside cup at the end)

MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.07, 0.00, 0.04) m, at rest
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), range -12° to 35° as MuJoCo applies it; its geoms: pendulum, pendulum rod; starts at 30.0°, still

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 30.0°
 0.39 s  ball first touches pendulum
 0.39 s  ball starts moving
 0.42 s  ball leaves pendulum
 0.77 s  pendulum is at its smallest, -7.5°
 2.27 s  ball leaves floor
 2.27 s  ball first touches cup_near_wall
 2.29 s  ball first touches cup_base
 2.29 s  ball leaves cup_near_wall
 2.90 s  ball comes to rest at (1.08, 0.00, 0.04) m

State every 0.25 s:
0.00 s: ball at (0.07, 0.00, 0.04) m, at rest; touching floor | pendulum at 30.0°, still; touching nothing
0.25 s: ball at (0.07, 0.00, 0.04) m, at rest; touching floor | pendulum at 16.2°, turning -100°/s; touching nothing
0.50 s: ball at (0.13, 0.00, 0.04) m, moving 0.48 m/s (vx +0.48, vy -0.00, vz +0.00); touching floor | pendulum at -3.4°, turning -27°/s; touching nothing
0.75 s: ball at (0.25, 0.00, 0.04) m, moving 0.48 m/s (vx +0.48, vy -0.00, vz -0.00); touching floor | pendulum at -7.5°, turning -3°/s; touching nothing
1.00 s: ball at (0.37, 0.00, 0.04) m, moving 0.47 m/s (vx +0.47, vy -0.00, vz -0.00); touching floor | pendulum at -4.4°, turning +24°/s; touching nothing
1.25 s: ball at (0.48, 0.00, 0.04) m, moving 0.46 m/s (vx +0.46, vy -0.00, vz -0.00); touching floor | pendulum at 2.7°, turning +28°/s; touching nothing
1.50 s: ball at (0.60, 0.00, 0.04) m, moving 0.46 m/s (vx +0.46, vy -0.00, vz -0.00); touching floor | pendulum at 7.2°, turning +5°/s; touching nothing
1.75 s: ball at (0.71, 0.00, 0.04) m, moving 0.45 m/s (vx +0.45, vy -0.00, vz -0.00); touching floor | pendulum at 4.8°, turning -22°/s; touching nothing
2.00 s: ball at (0.83, 0.00, 0.04) m, moving 0.45 m/s (vx +0.45, vy -0.00, vz -0.00); touching floor | pendulum at -2.0°, turning -28°/s; touching nothing
2.25 s: ball at (0.94, 0.00, 0.04) m, moving 0.44 m/s (vx +0.44, vy -0.00, vz -0.00); touching floor | pendulum at -6.9°, turning -8°/s; touching nothing
2.50 s: ball at (1.02, 0.00, 0.04) m, moving 0.26 m/s (vx +0.26, vy -0.00, vz -0.01); touching nothing | pendulum at -5.2°, turning +20°/s; touching nothing
2.75 s: ball at (1.07, 0.00, 0.04) m, moving 0.10 m/s (vx +0.10, vy -0.00, vz -0.00); touching cup_base | pendulum at 1.4°, turning +28°/s; touching nothing
3.00 s: ball at (1.08, 0.00, 0.04) m, at rest; touching cup_base | pendulum at 6.5°, turning +10°/s; touching nothing
3.25 s: ball at (1.09, 0.00, 0.04) m, at rest; touching cup_base | pendulum at 5.4°, turning -17°/s; touching nothing
3.50 s: ball at (1.09, 0.00, 0.04) m, at rest; touching cup_base | pendulum at -0.7°, turning -28°/s; touching nothing
3.75 s: ball at (1.09, 0.00, 0.04) m, at rest; touching cup_base | pendulum at -6.1°, turning -12°/s; touching nothing
4.00 s: ball at (1.09, 0.00, 0.04) m, at rest; touching cup_base | pendulum at -5.6°, turning +15°/s; touching nothing
4.25 s: ball at (1.09, 0.00, 0.04) m, at rest; touching cup_base | pendulum at 0.1°, turning +27°/s; touching nothing
4.50 s: ball at (1.09, 0.00, 0.04) m, at rest; touching cup_base | pendulum at 5.7°, turning +14°/s; touching nothing
4.75 s: ball at (1.09, 0.00, 0.04) m, at rest; touching cup_base | pendulum at 5.8°, turning -12°/s; touching nothing
5.00 s: ball at (1.09, 0.00, 0.04) m, at rest; touching cup_base | pendulum at 0.4°, turning -26°/s; touching nothing
5.25 s: ball at (1.09, 0.00, 0.04) m, at rest; touching cup_base | pendulum at -5.2°, turning -15°/s; touching nothing
5.50 s: ball at (1.09, 0.00, 0.04) m, at rest; touching cup_base | pendulum at -5.9°, turning +10°/s; touching nothing
5.75 s: ball at (1.09, 0.00, 0.04) m, at rest; touching cup_base | pendulum at -1.0°, turning +25°/s; touching nothing
6.00 s: ball at (1.09, 0.00, 0.04) m, at rest; touching cup_base | pendulum at 4.8°, turning +17°/s; touching nothing

At the end (6.00 s):
- ball at (1.09, 0.00, 0.04) m, at rest; touching cup_base
- pendulum at 4.8°, turning +17°/s; touching nothing
</history>
