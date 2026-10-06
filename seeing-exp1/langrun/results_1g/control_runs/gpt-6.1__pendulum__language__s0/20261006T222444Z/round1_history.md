MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball: free body; its geoms: ball; starts at (0.00, 0.00, 0.03) m, at rest
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum, pendulum rod; starts at 30.0°, still

What happened, in order:
 0.00 s  ball starts touching floor
 0.00 s  pendulum is at its largest at the start, 30.0°
 0.40 s  ball first touches pendulum
 0.40 s  ball starts moving
 0.42 s  ball leaves pendulum
 0.77 s  pendulum passes 0.49 m from cup approach without touching it: nearest points (0.16, 0.00, 0.07) m and (0.65, 0.00, 0.00) m
 0.77 s  pendulum is at its smallest, -18.6°
 1.13 s  ball leaves floor
 1.13 s  ball first touches cup approach
 1.46 s  ball leaves cup approach
 1.51 s  ball first touches cup_base
 1.99 s  ball comes to rest at (1.08, 0.00, 0.03) m

State every 0.25 s:
0.00 s: ball at (0.00, 0.00, 0.03) m, at rest; touching floor | pendulum at 30.0°, still; touching nothing
0.25 s: ball at (0.00, 0.00, 0.03) m, at rest; touching floor | pendulum at 16.2°, turning -101°/s; touching nothing
0.50 s: ball at (0.10, 0.00, 0.03) m, moving 0.87 m/s (vx +0.87, vy -0.00, vz +0.01); touching floor | pendulum at -8.3°, turning -68°/s; touching nothing
0.75 s: ball at (0.31, 0.00, 0.03) m, moving 0.86 m/s (vx +0.86, vy -0.00, vz -0.00); touching floor | pendulum at -18.5°, turning -7°/s; touching nothing
1.00 s: ball at (0.53, 0.00, 0.03) m, moving 0.85 m/s (vx +0.85, vy -0.00, vz -0.00); touching floor | pendulum at -11.3°, turning +59°/s; touching nothing
1.25 s: ball at (0.73, 0.00, 0.04) m, moving 0.76 m/s (vx +0.76, vy -0.00, vz +0.02); touching cup approach | pendulum at 6.4°, turning +70°/s; touching nothing
1.50 s: ball at (0.91, 0.00, 0.03) m, moving 0.79 m/s (vx +0.68, vy -0.00, vz -0.40); touching nothing | pendulum at 17.9°, turning +15°/s; touching nothing
1.75 s: ball at (1.03, 0.00, 0.03) m, moving 0.34 m/s (vx +0.34, vy -0.00, vz +0.00); touching nothing | pendulum at 12.5°, turning -53°/s; touching nothing
2.00 s: ball at (1.08, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -4.5°, turning -71°/s; touching nothing
2.25 s: ball at (1.08, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -17.1°, turning -21°/s; touching nothing
2.50 s: ball at (1.08, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -13.5°, turning +47°/s; touching nothing
2.75 s: ball at (1.08, 0.00, 0.03) m, at rest; touching cup_base | pendulum at 2.7°, turning +71°/s; touching nothing
3.00 s: ball at (1.08, 0.00, 0.03) m, at rest; touching cup_base | pendulum at 16.1°, turning +28°/s; touching nothing
3.25 s: ball at (1.08, 0.00, 0.03) m, at rest; touching cup_base | pendulum at 14.3°, turning -41°/s; touching nothing
3.50 s: ball at (1.08, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -1.0°, turning -70°/s; touching nothing
3.75 s: ball at (1.08, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -15.1°, turning -33°/s; touching nothing
4.00 s: ball at (1.08, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -14.9°, turning +34°/s; touching nothing
4.25 s: ball at (1.08, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -0.7°, turning +69°/s; touching nothing
4.50 s: ball at (1.08, 0.00, 0.03) m, at rest; touching cup_base | pendulum at 13.9°, turning +38°/s; touching nothing
4.75 s: ball at (1.08, 0.00, 0.03) m, at rest; touching cup_base | pendulum at 15.3°, turning -27°/s; touching nothing
5.00 s: ball at (1.08, 0.00, 0.03) m, at rest; touching cup_base | pendulum at 2.3°, turning -67°/s; touching nothing
5.25 s: ball at (1.08, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -12.7°, turning -43°/s; touching nothing
5.50 s: ball at (1.08, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -15.6°, turning +21°/s; touching nothing
5.75 s: ball at (1.08, 0.00, 0.03) m, at rest; touching cup_base | pendulum at -3.8°, turning +64°/s; touching nothing
6.00 s: ball at (1.08, 0.00, 0.03) m, at rest; touching cup_base | pendulum at 11.3°, turning +47°/s; touching nothing

At the end (6.00 s):
- ball at (1.08, 0.00, 0.03) m, at rest; touching cup_base
- pendulum at 11.3°, turning +47°/s; touching nothing
</history>
