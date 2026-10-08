MuJoCo ran your scene for 12 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 12.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.02, 0.00, 1.11) m, at rest
- pendulum1: hinge joint pendulum1_hinge about axis (0.00, 1.00, 0.00), range -79.9998° to 55° as MuJoCo applies it; its geoms: pendulum1, pendulum1 rod; starts at 55.0°, still
- cart1: hinge joint cart1_guide_approximation about axis (0.00, 0.00, 1.00), range 0° to 0.229184° as MuJoCo applies it; its geoms: cart1; starts at 0.0°, still
- domino1: free body; its geoms: domino1; starts at (0.00, 0.00, 0.82) m, at rest
- flap1: hinge joint flap1_hinge about axis (0.00, 1.00, 0.00), range 90.0002° to 155° as MuJoCo applies it; its geoms: flap1; starts at 90.0°, still
- ball2: free body; its geoms: ball2; starts at (2.01, 0.00, 1.11) m, at rest
- seesaw1: hinge joint seesaw1_hinge about axis (0.00, 1.00, 0.00), range -40° to 0° as MuJoCo applies it; its geoms: seesaw1, seesaw1.seesaw catch lip; starts at 0.0°, still
- block1: free body; its geoms: block1; starts at (3.57, 0.00, 0.78) m, at rest
- door1: hinge joint door1_hinge about axis (0.00, 1.00, 0.00), range 0° to 15° as MuJoCo applies it; its geoms: door1; starts at 0.0°, still

What happened, in order:
 0.00 s  pendulum1 starts at its 55° stop (the end where it sits lower)
 0.00 s  pendulum1 is at its largest at the start, 55.0°
 0.00 s  cart1 starts at its 0° stop (neither end sits lower)
 0.00 s  cart1 starts at its 0.229184° stop (neither end sits lower)
 0.00 s  cart1 is at its largest at the start, 0.0°
 0.00 s  flap1 starts at its 90.0002° stop (the end where it sits higher)
 0.00 s  seesaw1 starts at its 0° stop (neither end sits lower)
 0.00 s  door1 starts at its 0° stop (the end where it sits higher)
 0.00 s  seesaw1 first touches block1
 0.00 s  ball1 first touches ramp1
 0.00 s  ball2 first touches ramp2
 0.01 s  domino1 starts moving
 0.01 s  seesaw1 is at its smallest, -0.0°
 0.02 s  ball1 starts moving
 0.02 s  ball2 starts moving
 0.05 s  seesaw1 is at its largest, 0.0°
 0.11 s  ball1 leaves ramp1
 0.11 s  ball2 leaves ramp2
 0.11 s  ball1 first touches ramp1 release lip
 0.11 s  ball2 first touches ramp2 release lip
 0.12 s  door1 reaches its 15° stop (the end where it sits lower) moving +221°/s
 0.14 s  door1 is at its largest, 16.5°
 0.19 s  door1 reaches its 15° stop (the end where it sits lower) again moving -16°/s
 0.24 s  ball1 touches ramp1 again
 0.24 s  ball2 touches ramp2 again
 0.24 s  ball1 leaves ramp1 release lip
 0.24 s  ball2 leaves ramp2 release lip
 0.36 s  ball1 leaves ramp1
 0.36 s  ball2 leaves ramp2
 0.36 s  ball1 touches ramp1 release lip again
 0.36 s  ball2 touches ramp2 release lip again
 0.38 s  domino1 first touches floor
 0.41 s  ball1 first touches pendulum1
 0.42 s  pendulum1 is at its smallest, -2.2°
 0.42 s  pendulum1 passes 0.03 m from ramp1 without touching it: nearest points (-0.02, 0.00, 1.08) m and (0.00, 0.00, 1.06) m
 0.42 s  pendulum1 passes 0.07 m from ramp1 release lip without touching it: nearest points (-0.02, 0.00, 1.09) m and (0.05, 0.00, 1.06) m
 0.43 s  ball2 touches ramp2 again
 0.43 s  ball2 leaves ramp2 release lip
 0.44 s  ball1 leaves pendulum1
 0.46 s  domino1 comes to rest at (0.00, 0.00, 0.12) m
 0.49 s  ball2 leaves ramp2
 0.49 s  ball2 touches ramp2 release lip again
 0.53 s  ball2 touches ramp2 again
 0.57 s  ball1 leaves ramp1 release lip
 0.57 s  ball1 touches ramp1 again
 0.72 s  ball1 leaves ramp1
 0.72 s  ball1 touches ramp1 release lip again
 0.80 s  ball1 touches ramp1 again
 0.80 s  ball1 leaves ramp1 release lip
 0.89 s  ball1 leaves ramp1
 0.89 s  ball1 touches ramp1 release lip again
 0.93 s  ball1 touches ramp1 2 more times between 0.93 s and 12.00 s, still touching at the end
 0.93 s  ball1 leaves ramp1 release lip
 0.98 s  ball1 touches ramp1 release lip 1 more times between 0.98 s and 12.00 s, still touching at the end
 0.98 s  ball1 comes to rest at (0.03, 0.00, 1.10) m
 1.39 s  ball1 touches pendulum1 again
 1.43 s  ball1 leaves pendulum1
 2.37 s  ball2 leaves ramp2
 2.37 s  flap1 first touches ball2
 2.38 s  flap1 is at its largest, 105.0°
 2.38 s  ball2 comes to rest at (2.03, 0.00, 1.10) m
 3.29 s  ball2 touches ramp2 1 more times between 3.29 s and 12.00 s, still touching at the end

State every 0.25 s:
0.00 s: ball1 at (0.02, 0.00, 1.11) m, at rest; touching nothing | pendulum1 at 55.0°, still; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.82) m, at rest; touching nothing | flap1 at 90.0°, still; touching nothing | ball2 at (2.01, 0.00, 1.11) m, at rest; touching nothing | seesaw1 at 0.0°, still; touching nothing | block1 at (3.57, 0.00, 0.78) m, at rest; touching nothing | door1 at 0.0°, still; touching nothing
0.25 s: ball1 at (0.03, 0.00, 1.10) m, moving 0.11 m/s (vx -0.10, vy -0.00, vz +0.05); touching ramp1 | pendulum1 at 30.4°, turning -179°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.52) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | flap1 at 90.0°, still; touching nothing | ball2 at (2.02, 0.00, 1.10) m, moving 0.11 m/s (vx -0.10, vy -0.00, vz +0.05); touching ramp2 | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.1°, turning -2°/s; touching nothing
0.50 s: ball1 at (0.04, 0.00, 1.11) m, at rest; touching ramp1 release lip | pendulum1 at -1.0°, turning +16°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 90.0°, still; touching nothing | ball2 at (2.03, 0.00, 1.10) m, at rest; touching ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
0.75 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1 release lip | pendulum1 at 2.7°, turning +10°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 90.0°, still; touching nothing | ball2 at (2.02, 0.00, 1.10) m, at rest; touching ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
1.00 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 3.4°, turning -5°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 90.0°, still; touching nothing | ball2 at (2.02, 0.00, 1.10) m, at rest; touching ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
1.25 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.7°, turning -14°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 90.1°, still; touching nothing | ball2 at (2.02, 0.00, 1.10) m, at rest; touching ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
1.50 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -1.0°, turning +5°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 90.2°, turning +1°/s; touching nothing | ball2 at (2.02, 0.00, 1.10) m, at rest; touching ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
1.75 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.5°, turning +6°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 90.7°, turning +3°/s; touching nothing | ball2 at (2.02, 0.00, 1.10) m, at rest; touching ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
2.00 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 1.3°, still; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 92.4°, turning +12°/s; touching nothing | ball2 at (2.02, 0.00, 1.10) m, at rest; touching ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
2.25 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.8°, turning -4°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 98.4°, turning +41°/s; touching nothing | ball2 at (2.02, 0.00, 1.10) m, at rest; touching ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
2.50 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -0.5°, turning -5°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.9°, still; touching ball2 | ball2 at (2.03, 0.00, 1.10) m, at rest; touching flap1, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
2.75 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -1.2°, still; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.9°, still; touching ball2 | ball2 at (2.03, 0.00, 1.10) m, at rest; touching flap1, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
3.00 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -0.7°, turning +4°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.8°, still; touching ball2 | ball2 at (2.03, 0.00, 1.10) m, at rest; touching flap1, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
3.25 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.5°, turning +4°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
3.50 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 1.0°, still; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
3.75 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.5°, turning -4°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
4.00 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -0.4°, turning -3°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
4.25 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -0.9°, still; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
4.50 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -0.4°, turning +3°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
4.75 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.4°, turning +3°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
5.00 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.8°, still; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
5.25 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.3°, turning -3°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
5.50 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -0.4°, turning -2°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
5.75 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -0.7°, still; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
6.00 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -0.3°, turning +3°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
6.25 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.4°, turning +2°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
6.50 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.6°, still; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
6.75 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.2°, turning -2°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
7.00 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -0.4°, turning -2°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
7.25 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -0.5°, still; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
7.50 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -0.1°, turning +2°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
7.75 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.3°, turning +1°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
8.00 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.4°, still; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
8.25 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.1°, turning -2°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
8.50 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -0.3°, turning -1°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
8.75 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -0.4°, still; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
9.00 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -0.1°, turning +2°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
9.25 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.3°, still; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
(the same through 9.50 s)
9.75 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.0°, turning -1°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
10.00 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -0.3°, still; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
(the same through 10.25 s)
10.50 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -0.0°, turning +1°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
10.75 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.2°, still; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
(the same through 11.00 s)
11.25 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.0°, turning -1°/s; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
11.50 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at -0.2°, still; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing
(the same through 11.75 s)
12.00 s: ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip | pendulum1 at 0.0°, still; touching nothing | cart1 at 0.0°, still; touching nothing | domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor | flap1 at 104.7°, still; touching ball2 | ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip | seesaw1 at 0.0°, still; touching block1 | block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1 | door1 at 15.0°, still; touching nothing

At the end (12.00 s):
- ball1 at (0.03, 0.00, 1.10) m, at rest; touching ramp1, ramp1 release lip
- pendulum1 at 0.0°, still; touching nothing
- cart1 at 0.0°, still; touching nothing
- domino1 at (0.00, 0.00, 0.12) m, at rest; touching floor
- flap1 at 104.7°, still; touching ball2
- ball2 at (2.02, 0.00, 1.10) m, at rest; touching flap1, ramp2, ramp2 release lip
- seesaw1 at 0.0°, still; touching block1
- block1 at (3.57, 0.00, 0.78) m, at rest; touching seesaw1
- door1 at 15.0°, still; touching nothing

Openings (fixed rings, open through the middle; height is the middle of the whole thing), and each loose thing that comes down through one's height:
ring1: an opening 0.24 m across, centre (3.57, 0.00, 0.48) m
- domino1 comes down through ring1's height at 0.26 s, 3.57 m from its centre: outside it, missing by 3.46 m
</history>
