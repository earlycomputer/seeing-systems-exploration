MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pivot about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum_bob, pendulum_rod; starts at 66.4°, still
- cart: free body; its geoms: cart; starts at (0.23, 0.00, 0.85) m, at rest
- weight: free body; its geoms: weight; starts at (0.90, 0.00, 0.81) m, at rest
- seesaw: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range -35° to 0° as MuJoCo applies it; its geoms: seesaw, seesaw.weight cradle, seesaw.cradle near wall, seesaw.cradle far wall, seesaw.cradle left wall, seesaw.cradle right wall, seesaw.launch crosspiece; starts at 0.0°, still
- ball: free body; its geoms: ball; starts at (2.40, 0.45, 0.55) m, at rest

What happened, in order:
 0.00 s  pendulum_rod starts touching pendulum_stand_arm
 0.00 s  pendulum is at its largest at the start, 66.4°
 0.00 s  seesaw starts at its upper stop (0°)
 0.00 s  weight first touches track
 0.00 s  seesaw.launch crosspiece first touches ball
 0.00 s  cart first touches track
 0.55 s  pendulum_bob first touches cart
 0.55 s  cart starts moving
 0.55 s  pendulum passes 0.15 m from pendulum_stand_post without touching it: nearest points (0.00, -0.12, 0.85) m and (0.00, -0.27, 0.85) m
 0.55 s  pendulum passes 0.12 m from cup (cup_right_wall) without touching it: nearest points (0.00, 0.09, 0.78) m and (0.00, 0.19, 0.70) m
 0.58 s  pendulum_bob leaves cart
 0.70 s  cart first touches weight
 0.70 s  weight starts moving
 0.74 s  cart leaves weight
 0.76 s  pendulum passes 0.30 m from weight without touching it: nearest points (0.61, 0.00, 0.96) m and (0.90, 0.00, 0.90) m
 0.81 s  weight leaves track
 0.85 s  weight first touches weight arrest wall
 0.85 s  cart first touches left cart stop
 0.85 s  cart first touches right cart stop
 0.86 s  cart passes 0.11 m from seesaw (seesaw.cradle near wall) without touching it: nearest points (1.02, 0.10, 0.72) m and (1.04, 0.10, 0.61) m
 0.86 s  pendulum passes 0.50 m from seesaw (seesaw.cradle near wall) without touching it: nearest points (0.72, 0.00, 0.99) m and (1.04, 0.00, 0.61) m
 0.89 s  cart leaves left cart stop
 0.89 s  cart leaves right cart stop
 0.90 s  weight leaves weight arrest wall
 0.96 s  seesaw is at its largest, 0.0°
 0.96 s  weight first touches seesaw.cradle near wall
 0.96 s  ball starts moving
 0.96 s  weight leaves seesaw.cradle near wall
 1.01 s  pendulum passes 0.26 m from left cart stop without touching it: nearest points (0.83, 0.03, 1.11) m and (1.02, 0.08, 0.94) m
 1.01 s  pendulum passes 0.26 m from right cart stop without touching it: nearest points (0.83, -0.03, 1.11) m and (1.02, -0.08, 0.94) m
 1.02 s  weight first touches seesaw.weight cradle
 1.07 s  pendulum passes 0.36 m from weight arrest wall without touching it: nearest points (0.88, 0.00, 1.19) m and (1.24, 0.00, 1.17) m
 1.07 s  pendulum is at its smallest, -49.1°
 1.08 s  weight leaves seesaw.weight cradle
 1.09 s  weight touches seesaw.cradle near wall again
 1.20 s  weight touches seesaw.weight cradle again
 1.22 s  seesaw reaches its lower stop (-35°) moving -209°/s
 1.22 s  seesaw.launch crosspiece leaves ball
 1.22 s  weight leaves seesaw.cradle near wall
 1.24 s  seesaw is at its smallest, -36.4°
 1.24 s  weight passes 0.37 m from lever stand without touching it: nearest points (1.31, 0.07, 0.19) m and (1.68, 0.07, 0.19) m
 1.28 s  seesaw reaches its lower stop (-35°) again moving +21°/s
 1.29 s  weight touches seesaw.cradle near wall again
 1.32 s  weight comes to rest at (1.18, 0.00, 0.22) m
 1.41 s  ball is at the top of its flight, at (1.96, 0.45, 1.10) m
 1.75 s  ball passes 0.37 m from weight arrest wall without touching it: nearest points (1.43, 0.42, 0.54) m and (1.26, 0.11, 0.62) m
 1.75 s  ball passes 0.50 m from left cart stop without touching it: nearest points (1.42, 0.43, 0.55) m and (1.06, 0.14, 0.72) m
 1.76 s  ball passes 0.44 m from lever stand without touching it: nearest points (1.44, 0.43, 0.50) m and (1.68, 0.07, 0.40) m
 1.84 s  weight passes 0.35 m from ball without touching it: nearest points (1.30, 0.07, 0.20) m and (1.31, 0.42, 0.20) m
 1.88 s  ball first touches cup_base
 1.91 s  ball leaves cup_base
 2.01 s  ball touches cup_base again
 2.02 s  ball comes to rest at (1.23, 0.45, 0.05) m
 2.92 s  pendulum_bob touches cart again
 2.95 s  pendulum_bob leaves cart
 3.03 s  cart touches left cart stop again
 3.03 s  cart touches right cart stop again
 3.03 s  cart passes 0.21 m from weight arrest wall without touching it: nearest points (1.03, 0.11, 0.97) m and (1.24, 0.11, 0.97) m
 3.05 s  cart leaves left cart stop
 3.05 s  cart leaves right cart stop
 3.14 s  cart comes to rest at (0.89, 0.00, 0.85) m
 3.67 s  pendulum passes 0.02 m from left guide without touching it: nearest points (0.03, 0.12, 0.84) m and (0.03, 0.14, 0.84) m
 3.67 s  pendulum passes 0.02 m from right guide without touching it: nearest points (0.03, -0.12, 0.84) m and (0.03, -0.14, 0.84) m
 5.76 s  pendulum passes 0.01 m from track without touching it: nearest points (0.02, 0.00, 0.73) m and (0.02, 0.00, 0.72) m

State every 0.25 s:
0.00 s: pendulum at 66.4°, still; touching pendulum_stand_arm | cart at (0.23, 0.00, 0.85) m, at rest; touching nothing | weight at (0.90, 0.00, 0.81) m, at rest; touching nothing | seesaw at 0.0°, still; touching nothing | ball at (2.40, 0.45, 0.55) m, at rest; touching nothing
0.25 s: pendulum at 50.7°, turning -122°/s; touching pendulum_stand_arm | cart at (0.23, 0.00, 0.85) m, at rest; touching track | weight at (0.90, 0.00, 0.81) m, at rest; touching track | seesaw at 0.0°, still; touching ball | ball at (2.40, 0.45, 0.55) m, at rest; touching seesaw.launch crosspiece
0.50 s: pendulum at 9.6°, turning -192°/s; touching pendulum_stand_arm | cart at (0.23, 0.00, 0.85) m, at rest; touching track | weight at (0.90, 0.00, 0.81) m, at rest; touching track | seesaw at 0.0°, still; touching ball | ball at (2.40, 0.45, 0.55) m, at rest; touching seesaw.launch crosspiece
0.75 s: pendulum at -28.1°, turning -122°/s; touching pendulum_stand_arm | cart at (0.76, 0.00, 0.85) m, moving 1.38 m/s (vx +1.37, vy -0.00, vz -0.08); touching track | weight at (0.97, 0.00, 0.81) m, moving 1.67 m/s (vx +1.67, vy +0.00, vz -0.04), turned 1° from how it started; touching track | seesaw at 0.0°, still; touching ball | ball at (2.40, 0.45, 0.55) m, at rest; touching seesaw.launch crosspiece
1.00 s: pendulum at -48.0°, turning -32°/s; touching pendulum_stand_arm | cart at (0.88, 0.00, 0.85) m, moving 0.17 m/s (vx -0.17, vy -0.00, vz -0.00); touching track | weight at (1.14, 0.00, 0.61) m, moving 1.77 m/s (vx +0.11, vy +0.00, vz -1.77), turned 2° from how it started; touching nothing | seesaw at -1.7°, turning -38°/s; touching ball | ball at (2.40, 0.45, 0.57) m, moving 0.43 m/s (vx -0.06, vy +0.00, vz +0.43); touching seesaw.launch crosspiece
1.25 s: pendulum at -42.7°, turning +71°/s; touching pendulum_stand_arm | cart at (0.84, 0.00, 0.85) m, moving 0.13 m/s (vx -0.13, vy -0.00, vz -0.00); touching track | weight at (1.18, 0.00, 0.21) m, moving 0.26 m/s (vx -0.12, vy -0.00, vz +0.23), turned 36° from how it started; touching seesaw.weight cradle | seesaw at -36.3°, turning +21°/s; touching weight | ball at (2.21, 0.45, 0.97) m, moving 2.21 m/s (vx -1.52, vy +0.00, vz +1.60); touching nothing
1.50 s: pendulum at -15.0°, turning +140°/s; touching pendulum_stand_arm | cart at (0.82, 0.00, 0.85) m, moving 0.09 m/s (vx -0.09, vy -0.00, vz +0.00); touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.83, 0.45, 1.06) m, moving 1.75 m/s (vx -1.52, vy +0.00, vz -0.86); touching nothing
1.75 s: pendulum at 20.9°, turning +132°/s; touching pendulum_stand_arm | cart at (0.80, 0.00, 0.85) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.45, 0.45, 0.54) m, moving 3.64 m/s (vx -1.52, vy +0.00, vz -3.31); touching nothing
2.00 s: pendulum at 44.8°, turning +53°/s; touching pendulum_stand_arm | cart at (0.79, 0.00, 0.85) m, at rest; touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.23, 0.45, 0.05) m, moving 0.40 m/s (vx -0.12, vy +0.00, vz -0.38); touching nothing
2.25 s: pendulum at 45.0°, turning -50°/s; touching pendulum_stand_arm | cart at (0.79, 0.00, 0.85) m, at rest; touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.23, 0.45, 0.05) m, at rest; touching cup_base
2.50 s: pendulum at 21.6°, turning -129°/s; touching pendulum_stand_arm | cart at (0.79, 0.00, 0.85) m, at rest; touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.23, 0.45, 0.05) m, at rest; touching cup_base
2.75 s: pendulum at -13.5°, turning -138°/s; touching pendulum_stand_arm | cart at (0.79, 0.00, 0.85) m, at rest; touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.23, 0.45, 0.05) m, at rest; touching cup_base
3.00 s: pendulum at -40.0°, turning -60°/s; touching pendulum_stand_arm | cart at (0.86, 0.00, 0.87) m, moving 0.88 m/s (vx +0.87, vy -0.01, vz +0.10), turned 13° from how it started; touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.23, 0.45, 0.05) m, at rest; touching cup_base
3.25 s: pendulum at -43.0°, turning +36°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.23, 0.45, 0.05) m, at rest; touching cup_base
3.50 s: pendulum at -23.3°, turning +115°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.23, 0.45, 0.05) m, at rest; touching cup_base
3.75 s: pendulum at 9.2°, turning +132°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.23, 0.45, 0.05) m, at rest; touching cup_base
4.00 s: pendulum at 36.2°, turning +75°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.23, 0.45, 0.05) m, at rest; touching cup_base
4.25 s: pendulum at 43.4°, turning -18°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.23, 0.45, 0.05) m, at rest; touching cup_base
4.50 s: pendulum at 27.6°, turning -102°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.23, 0.45, 0.05) m, at rest; touching cup_base
4.75 s: pendulum at -3.3°, turning -132°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.23, 0.45, 0.05) m, at rest; touching cup_base
5.00 s: pendulum at -32.0°, turning -87°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.23, 0.45, 0.05) m, at rest; touching cup_base
5.25 s: pendulum at -43.0°, turning +2°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.23, 0.45, 0.05) m, at rest; touching cup_base
5.50 s: pendulum at -31.1°, turning +89°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.23, 0.45, 0.05) m, at rest; touching cup_base
5.75 s: pendulum at -2.2°, turning +130°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.23, 0.45, 0.05) m, at rest; touching cup_base
6.00 s: pendulum at 27.6°, turning +97°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle | seesaw at -35.0°, still; touching weight | ball at (1.23, 0.45, 0.05) m, at rest; touching cup_base

At the end (6.00 s):
- pendulum at 27.6°, turning +97°/s; touching pendulum_stand_arm
- cart at (0.89, 0.00, 0.85) m, at rest; touching track
- weight at (1.18, 0.00, 0.23) m, at rest, turned 35° from how it started; touching seesaw.cradle near wall, seesaw.weight cradle
- seesaw at -35.0°, still; touching weight
- ball at (1.23, 0.45, 0.05) m, at rest; touching cup_base
</history>
