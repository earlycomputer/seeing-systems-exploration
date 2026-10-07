MuJoCo ran your scene for 6 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 6.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), no range limit; its geoms: pendulum, pendulum rod; starts at 66.4°, still
- cart: free body; its geoms: cart; starts at (0.30, 0.68, 1.40) m, at rest
- weight: free body; its geoms: weight; starts at (1.38, 0.68, 1.34) m, at rest
- seesaw: hinge joint seesaw_hinge about axis (1.00, 0.00, 0.00), range -18° to 15° as MuJoCo applies it; its geoms: seesaw, seesaw.launch tray, seesaw.launch back; starts at 15.0°, still
- ball: free body; its geoms: ball; starts at (1.70, -0.74, 0.48) m, at rest

What happened, in order:
 0.00 s  weight starts touching runway
 0.00 s  cart starts touching runway
 0.00 s  pendulum is at its largest at the start, 66.4°
 0.00 s  seesaw starts at its upper stop (15°)
 0.00 s  seesaw.launch tray first touches ball
 0.03 s  ball starts moving
 0.19 s  seesaw.launch tray leaves ball
 0.21 s  seesaw first touches ball
 0.24 s  seesaw.launch back first touches ball
 0.57 s  pendulum first touches cart
 0.57 s  cart starts moving
 0.60 s  pendulum leaves cart
 0.88 s  cart first touches weight
 0.88 s  weight starts moving
 0.92 s  cart leaves weight
 1.06 s  pendulum is at its smallest, -43.2°
 1.18 s  weight leaves runway
 1.31 s  cart leaves runway
 1.31 s  cart first touches right cart stop
 1.31 s  cart first touches left cart stop
 1.32 s  weight first touches weight drop wall
 1.33 s  cart passes 0.31 m from weight drop wall without touching it: nearest points (1.54, 0.58, 1.55) m and (1.85, 0.58, 1.55) m
 1.33 s  weight leaves weight drop wall
 1.34 s  cart leaves right cart stop
 1.34 s  cart leaves left cart stop
 1.34 s  cart touches runway again
 1.35 s  cart passes 0.19 m from cup (cup_left_wall) without touching it: nearest points (1.54, 0.54, 1.25) m and (1.54, 0.54, 1.06) m
 1.39 s  weight first touches seesaw
 1.40 s  cart comes to rest at (1.41, 0.68, 1.40) m
 1.45 s  weight passes 0.01 m from cup (cup_left_wall) without touching it: nearest points (1.69, 0.57, 0.84) m and (1.69, 0.56, 0.84) m
 1.45 s  weight leaves seesaw
 1.51 s  seesaw reaches its lower stop (-18°) moving -311°/s
 1.51 s  seesaw leaves ball
 1.52 s  seesaw.launch back leaves ball
 1.52 s  weight touches seesaw again
 1.54 s  seesaw is at its smallest, -21.6°
 1.61 s  weight leaves seesaw
 1.62 s  seesaw reaches its lower stop (-18°) again moving +36°/s
 1.65 s  weight touches seesaw again
 1.67 s  seesaw reaches its lower stop (-18°) again moving -15°/s
 1.67 s  weight leaves seesaw
 1.86 s  ball is at the top of its flight, at (1.70, -0.03, 1.51) m
 1.90 s  weight first touches floor
 1.97 s  weight leaves floor
 2.01 s  weight touches floor again
 2.10 s  ball passes 0.16 m from right guide without touching it: nearest points (1.66, 0.47, 1.23) m and (1.50, 0.50, 1.25) m
 2.11 s  cart passes 0.13 m from ball without touching it: nearest points (1.53, 0.53, 1.25) m and (1.66, 0.50, 1.21) m
 2.11 s  ball passes 0.09 m from right cart stop without touching it: nearest points (1.66, 0.50, 1.22) m and (1.58, 0.53, 1.25) m
 2.11 s  ball passes 0.16 m from runway without touching it: nearest points (1.66, 0.49, 1.20) m and (1.50, 0.51, 1.20) m
 2.15 s  ball first touches cup_left_wall
 2.16 s  ball passes 0.11 m from weight drop wall without touching it: nearest points (1.75, 0.58, 1.09) m and (1.85, 0.58, 1.09) m
 2.17 s  ball leaves cup_left_wall
 2.22 s  ball passes 0.21 m from left cart stop without touching it: nearest points (1.68, 0.69, 1.09) m and (1.58, 0.79, 1.25) m
 2.23 s  ball passes 0.28 m from left guide without touching it: nearest points (1.67, 0.71, 1.07) m and (1.50, 0.84, 1.25) m
 2.32 s  seesaw reaches its upper stop (15°) again moving +111°/s
 2.34 s  cart passes 0.41 m from seesaw without touching it: nearest points (1.53, 0.76, 1.25) m and (1.53, 0.76, 0.84) m
 2.34 s  seesaw is at its largest, 15.7°
 2.37 s  seesaw reaches its upper stop (15°) again moving -14°/s
 2.59 s  ball first touches floor
 2.60 s  weight passes 0.12 m from ball without touching it: nearest points (1.53, 1.22, 0.02) m and (1.66, 1.23, 0.02) m
 2.68 s  weight comes to rest at (1.41, 1.22, 0.09) m
 3.61 s  pendulum passes 0.04 m from left guide without touching it: nearest points (0.13, 0.80, 1.38) m and (0.13, 0.84, 1.37) m
 3.61 s  pendulum passes 0.04 m from right guide without touching it: nearest points (0.13, 0.56, 1.38) m and (0.13, 0.52, 1.37) m
 5.70 s  pendulum passes 0.04 m from runway without touching it: nearest points (0.13, 0.68, 1.29) m and (0.13, 0.68, 1.25) m
 6.00 s  ball is still moving at the end, 1.45 m/s

State every 0.25 s:
0.00 s: pendulum at 66.4°, still; touching nothing | cart at (0.30, 0.68, 1.40) m, at rest; touching runway | weight at (1.38, 0.68, 1.34) m, at rest; touching runway | seesaw at 15.0°, still; touching nothing | ball at (1.70, -0.74, 0.48) m, at rest; touching nothing
0.25 s: pendulum at 50.6°, turning -122°/s; touching nothing | cart at (0.30, 0.68, 1.40) m, at rest; touching runway | weight at (1.38, 0.68, 1.34) m, at rest; touching runway | seesaw at 15.0°, still; touching ball | ball at (1.70, -0.80, 0.45) m, moving 0.06 m/s (vx +0.00, vy +0.06, vz +0.03); touching seesaw.launch back
0.50 s: pendulum at 9.3°, turning -194°/s; touching nothing | cart at (0.30, 0.68, 1.40) m, at rest; touching runway | weight at (1.38, 0.68, 1.34) m, at rest; touching runway | seesaw at 15.0°, still; touching ball | ball at (1.70, -0.79, 0.45) m, at rest; touching seesaw, seesaw.launch back
0.75 s: pendulum at -26.0°, turning -105°/s; touching nothing | cart at (0.80, 0.68, 1.40) m, moving 2.74 m/s (vx +2.74, vy -0.00, vz -0.00); touching nothing | weight at (1.38, 0.68, 1.34) m, at rest; touching runway | seesaw at 15.0°, still; touching ball | ball at (1.70, -0.79, 0.45) m, at rest; touching seesaw, seesaw.launch back
1.00 s: pendulum at -42.6°, turning -23°/s; touching nothing | cart at (1.24, 0.68, 1.40) m, moving 0.60 m/s (vx +0.60, vy -0.00, vz +0.02); touching runway | weight at (1.47, 0.68, 1.34) m, moving 0.80 m/s (vx +0.80, vy +0.00, vz -0.00); touching runway | seesaw at 15.0°, still; touching ball | ball at (1.70, -0.79, 0.45) m, at rest; touching seesaw, seesaw.launch back
1.25 s: pendulum at -36.4°, turning +70°/s; touching nothing | cart at (1.38, 0.68, 1.40) m, moving 0.53 m/s (vx +0.53, vy -0.00, vz +0.01); touching runway | weight at (1.67, 0.68, 1.23) m, moving 1.65 m/s (vx +0.81, vy +0.00, vz -1.44), turned 40° from how it started; touching nothing | seesaw at 15.0°, still; touching ball | ball at (1.70, -0.79, 0.45) m, at rest; touching seesaw, seesaw.launch back
1.50 s: pendulum at -10.5°, turning +128°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.77, 0.69, 0.60) m, moving 3.51 m/s (vx +0.25, vy +0.08, vz -3.51), turned 109° from how it started; touching nothing | seesaw at -15.3°, turning -312°/s; touching ball | ball at (1.70, -0.76, 0.87) m, moving 4.42 m/s (vx -0.00, vy +1.48, vz +4.17); touching seesaw, seesaw.launch back
1.75 s: pendulum at 21.3°, turning +114°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.64, 0.92, 0.41) m, moving 1.75 m/s (vx -0.55, vy +1.09, vz -1.25), turned 78° from how it started; touching nothing | seesaw at -18.0°, turning +2°/s; touching nothing | ball at (1.70, -0.26, 1.45) m, moving 2.32 m/s (vx -0.00, vy +2.06, vz +1.07); touching nothing
2.00 s: pendulum at 41.2°, turning +39°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.46, 1.10, 0.13) m, moving 0.70 m/s (vx -0.65, vy +0.00, vz +0.27), turned 142° from how it started; touching nothing | seesaw at -11.4°, turning +50°/s; touching nothing | ball at (1.70, 0.26, 1.41) m, moving 2.48 m/s (vx -0.00, vy +2.06, vz -1.38); touching nothing
2.25 s: pendulum at 39.0°, turning -55°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.36, 1.14, 0.14) m, moving 0.60 m/s (vx -0.36, vy +0.40, vz -0.27), turned 124° from how it started; touching floor | seesaw at 7.3°, turning +99°/s; touching nothing | ball at (1.70, 0.71, 1.02) m, moving 1.94 m/s (vx -0.00, vy +1.49, vz -1.25); touching nothing
2.50 s: pendulum at 15.8°, turning -122°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.37, 1.19, 0.12) m, moving 0.33 m/s (vx +0.20, vy +0.25, vz -0.10), turned 109° from how it started; touching floor | seesaw at 15.0°, still; touching nothing | ball at (1.70, 1.09, 0.41) m, moving 3.99 m/s (vx -0.00, vy +1.49, vz -3.70); touching nothing
2.75 s: pendulum at -16.4°, turning -122°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.41, 1.22, 0.09) m, at rest, turned 98° from how it started; touching floor | seesaw at 15.0°, still; touching nothing | ball at (1.70, 1.45, 0.04) m, moving 1.45 m/s (vx -0.00, vy +1.45, vz +0.00); touching floor
3.00 s: pendulum at -39.3°, turning -54°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.41, 1.22, 0.09) m, at rest, turned 98° from how it started; touching floor | seesaw at 15.0°, still; touching nothing | ball at (1.70, 1.81, 0.04) m, moving 1.45 m/s (vx -0.00, vy +1.45, vz +0.00); touching floor
3.25 s: pendulum at -41.0°, turning +40°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.41, 1.22, 0.09) m, at rest, turned 98° from how it started; touching floor | seesaw at 15.0°, still; touching nothing | ball at (1.70, 2.18, 0.04) m, moving 1.45 m/s (vx +0.00, vy +1.45, vz +0.00); touching floor
3.50 s: pendulum at -20.8°, turning +115°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.41, 1.22, 0.09) m, at rest, turned 98° from how it started; touching floor | seesaw at 15.0°, still; touching nothing | ball at (1.70, 2.54, 0.04) m, moving 1.45 m/s (vx -0.00, vy +1.45, vz -0.00); touching floor
3.75 s: pendulum at 11.1°, turning +127°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.41, 1.22, 0.09) m, at rest, turned 98° from how it started; touching floor | seesaw at 15.0°, still; touching nothing | ball at (1.70, 2.90, 0.04) m, moving 1.45 m/s (vx -0.00, vy +1.45, vz -0.00); touching floor
4.00 s: pendulum at 36.7°, turning +69°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.41, 1.22, 0.09) m, at rest, turned 98° from how it started; touching floor | seesaw at 15.0°, still; touching nothing | ball at (1.70, 3.27, 0.04) m, moving 1.45 m/s (vx -0.00, vy +1.45, vz -0.00); touching floor
4.25 s: pendulum at 42.4°, turning -24°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.41, 1.22, 0.09) m, at rest, turned 98° from how it started; touching floor | seesaw at 15.0°, still; touching nothing | ball at (1.70, 3.63, 0.04) m, moving 1.45 m/s (vx -0.00, vy +1.45, vz +0.00); touching floor
4.50 s: pendulum at 25.4°, turning -105°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.41, 1.22, 0.09) m, at rest, turned 98° from how it started; touching floor | seesaw at 15.0°, still; touching nothing | ball at (1.70, 3.99, 0.04) m, moving 1.45 m/s (vx -0.00, vy +1.45, vz +0.00); touching floor
4.75 s: pendulum at -5.6°, turning -131°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.41, 1.22, 0.09) m, at rest, turned 98° from how it started; touching floor | seesaw at 15.0°, still; touching nothing | ball at (1.70, 4.36, 0.04) m, moving 1.45 m/s (vx -0.00, vy +1.45, vz -0.00); touching floor
5.00 s: pendulum at -33.5°, turning -82°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.41, 1.22, 0.09) m, at rest, turned 98° from how it started; touching floor | seesaw at 15.0°, still; touching nothing | ball at (1.70, 4.72, 0.04) m, moving 1.45 m/s (vx -0.00, vy +1.45, vz -0.00); touching floor
5.25 s: pendulum at -43.1°, turning +8°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.41, 1.22, 0.09) m, at rest, turned 98° from how it started; touching floor | seesaw at 15.0°, still; touching nothing | ball at (1.70, 5.09, 0.04) m, moving 1.45 m/s (vx -0.00, vy +1.45, vz -0.00); touching floor
5.50 s: pendulum at -29.6°, turning +94°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.41, 1.22, 0.09) m, at rest, turned 98° from how it started; touching floor | seesaw at 15.0°, still; touching nothing | ball at (1.70, 5.45, 0.04) m, moving 1.45 m/s (vx -0.00, vy +1.45, vz +0.00); touching floor
5.75 s: pendulum at 0.1°, turning +132°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.41, 1.22, 0.09) m, at rest, turned 98° from how it started; touching floor | seesaw at 15.0°, still; touching nothing | ball at (1.70, 5.81, 0.04) m, moving 1.45 m/s (vx -0.00, vy +1.45, vz +0.00); touching floor
6.00 s: pendulum at 29.8°, turning +94°/s; touching nothing | cart at (1.40, 0.68, 1.40) m, at rest; touching runway | weight at (1.41, 1.22, 0.09) m, at rest, turned 98° from how it started; touching floor | seesaw at 15.0°, still; touching nothing | ball at (1.70, 6.18, 0.04) m, moving 1.45 m/s (vx -0.00, vy +1.45, vz -0.00); touching floor

At the end (6.00 s):
- pendulum at 29.8°, turning +94°/s; touching nothing
- cart at (1.40, 0.68, 1.40) m, at rest; touching runway
- weight at (1.41, 1.22, 0.09) m, at rest, turned 98° from how it started; touching floor
- seesaw at 15.0°, still; touching nothing
- ball at (1.70, 6.18, 0.04) m, moving 1.45 m/s (vx -0.00, vy +1.45, vz -0.00); touching floor
</history>
