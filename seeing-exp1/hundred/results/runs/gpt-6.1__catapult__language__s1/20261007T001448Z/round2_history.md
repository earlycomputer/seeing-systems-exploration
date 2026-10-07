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
 0.55 s  pendulum passes 0.14 m from seesaw (seesaw.cradle left wall) without touching it: nearest points (0.00, 0.04, 0.74) m and (0.00, 0.10, 0.61) m
 0.58 s  pendulum_bob leaves cart
 0.70 s  cart first touches weight
 0.70 s  weight starts moving
 0.74 s  cart leaves weight
 0.76 s  pendulum passes 0.30 m from weight without touching it: nearest points (0.61, 0.00, 0.96) m and (0.90, 0.00, 0.90) m
 0.81 s  weight leaves track
 0.85 s  weight first touches weight arrest wall
 0.85 s  cart first touches left cart stop
 0.85 s  cart first touches right cart stop
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
 1.12 s  seesaw.launch crosspiece leaves ball
 1.12 s  seesaw.cradle right wall first touches floor
 1.12 s  seesaw.cradle left wall first touches floor
 1.12 s  weight leaves seesaw.cradle near wall
 1.13 s  weight touches seesaw.weight cradle again
 1.13 s  seesaw is at its smallest, -16.7°
 1.14 s  weight passes 0.44 m from lever stand without touching it: nearest points (1.24, 0.07, 0.36) m and (1.68, 0.07, 0.36) m
 1.17 s  seesaw.cradle right wall leaves floor
 1.17 s  seesaw.cradle left wall leaves floor
 1.25 s  seesaw.cradle right wall touches floor again
 1.25 s  seesaw.cradle left wall touches floor again
 1.26 s  weight comes to rest at (1.13, 0.00, 0.43) m
 1.29 s  ball is at the top of its flight, at (2.25, 0.45, 0.88) m
 1.55 s  ball first touches cup_far_wall
 1.55 s  ball leaves cup_far_wall
 1.60 s  ball passes 0.45 m from lever stand without touching it: nearest points (2.09, 0.43, 0.44) m and (1.82, 0.07, 0.40) m
 1.74 s  ball first touches floor
 1.82 s  ball comes to rest at (2.17, 0.45, 0.03) m
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
1.00 s: pendulum at -48.0°, turning -32°/s; touching pendulum_stand_arm | cart at (0.88, 0.00, 0.85) m, moving 0.17 m/s (vx -0.17, vy -0.00, vz -0.00); touching track | weight at (1.14, 0.00, 0.62) m, moving 1.76 m/s (vx +0.12, vy +0.00, vz -1.76), turned 2° from how it started; touching nothing | seesaw at -1.7°, turning -37°/s; touching ball | ball at (2.40, 0.45, 0.57) m, moving 0.42 m/s (vx -0.06, vy +0.00, vz +0.42); touching seesaw.launch crosspiece
1.25 s: pendulum at -42.7°, turning +71°/s; touching pendulum_stand_arm | cart at (0.84, 0.00, 0.85) m, moving 0.13 m/s (vx -0.13, vy -0.00, vz -0.00); touching track | weight at (1.13, 0.00, 0.43) m, moving 0.16 m/s (vx +0.01, vy -0.00, vz -0.16), turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, turning -13°/s; touching floor, weight | ball at (2.28, 0.45, 0.87) m, moving 0.77 m/s (vx -0.64, vy +0.00, vz +0.43); touching nothing
1.50 s: pendulum at -15.0°, turning +140°/s; touching pendulum_stand_arm | cart at (0.82, 0.00, 0.85) m, moving 0.09 m/s (vx -0.09, vy -0.00, vz +0.00); touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.12, 0.45, 0.67) m, moving 2.12 m/s (vx -0.64, vy +0.00, vz -2.03); touching nothing
1.75 s: pendulum at 20.9°, turning +132°/s; touching pendulum_stand_arm | cart at (0.80, 0.00, 0.85) m, moving 0.06 m/s (vx -0.06, vy -0.00, vz +0.00); touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.17, 0.45, 0.02) m, moving 0.17 m/s (vx +0.17, vy -0.00, vz -0.00); touching floor
2.00 s: pendulum at 44.8°, turning +53°/s; touching pendulum_stand_arm | cart at (0.79, 0.00, 0.85) m, at rest; touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.17, 0.45, 0.03) m, at rest; touching floor
2.25 s: pendulum at 45.0°, turning -50°/s; touching pendulum_stand_arm | cart at (0.79, 0.00, 0.85) m, at rest; touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.17, 0.45, 0.03) m, at rest; touching floor
2.50 s: pendulum at 21.6°, turning -129°/s; touching pendulum_stand_arm | cart at (0.79, 0.00, 0.85) m, at rest; touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.17, 0.45, 0.03) m, at rest; touching floor
2.75 s: pendulum at -13.5°, turning -138°/s; touching pendulum_stand_arm | cart at (0.79, 0.00, 0.85) m, at rest; touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.17, 0.45, 0.03) m, at rest; touching floor
3.00 s: pendulum at -40.0°, turning -60°/s; touching pendulum_stand_arm | cart at (0.86, 0.00, 0.87) m, moving 0.88 m/s (vx +0.87, vy -0.01, vz +0.10), turned 13° from how it started; touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.17, 0.45, 0.03) m, at rest; touching floor
3.25 s: pendulum at -43.0°, turning +36°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.17, 0.45, 0.03) m, at rest; touching floor
3.50 s: pendulum at -23.3°, turning +115°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.17, 0.45, 0.03) m, at rest; touching floor
3.75 s: pendulum at 9.2°, turning +132°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.17, 0.45, 0.03) m, at rest; touching floor
4.00 s: pendulum at 36.2°, turning +75°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.17, 0.45, 0.03) m, at rest; touching floor
4.25 s: pendulum at 43.4°, turning -18°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.17, 0.45, 0.03) m, at rest; touching floor
4.50 s: pendulum at 27.6°, turning -102°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.17, 0.45, 0.03) m, at rest; touching floor
4.75 s: pendulum at -3.3°, turning -132°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.17, 0.45, 0.03) m, at rest; touching floor
5.00 s: pendulum at -32.0°, turning -87°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.17, 0.45, 0.03) m, at rest; touching floor
5.25 s: pendulum at -43.0°, turning +2°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.17, 0.45, 0.03) m, at rest; touching floor
5.50 s: pendulum at -31.1°, turning +89°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.17, 0.45, 0.03) m, at rest; touching floor
5.75 s: pendulum at -2.2°, turning +130°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.17, 0.45, 0.03) m, at rest; touching floor
6.00 s: pendulum at 27.6°, turning +97°/s; touching pendulum_stand_arm | cart at (0.89, 0.00, 0.85) m, at rest; touching track | weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle | seesaw at -15.9°, still; touching floor, weight | ball at (2.17, 0.45, 0.03) m, at rest; touching floor

At the end (6.00 s):
- pendulum at 27.6°, turning +97°/s; touching pendulum_stand_arm
- cart at (0.89, 0.00, 0.85) m, at rest; touching track
- weight at (1.13, 0.00, 0.43) m, at rest, turned 16° from how it started; touching seesaw.weight cradle
- seesaw at -15.9°, still; touching floor, weight
- ball at (2.17, 0.45, 0.03) m, at rest; touching floor
</history>
