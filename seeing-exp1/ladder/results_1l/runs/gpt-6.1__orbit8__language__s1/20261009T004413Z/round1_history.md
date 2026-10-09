Before the run, at the start:
- block1 already touches seesaw1 at the start, so their touch is not something that happens in the run

MuJoCo ran your scene for 12 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 12.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum1: hinge joint pendulum1_hinge about axis (0.00, 1.00, 0.00), range -79.9998° to 55° as MuJoCo applies it; its geoms: pendulum1; starts at 55.0°, still
- ball1: free body; its geoms: ball1; starts at (0.07, 0.00, 0.49) m, at rest
- cart1: slide joint cart1_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.4 m as MuJoCo applies it; its geoms: cart1; starts at 0.000 m, still
- domino1: free body; its geoms: domino1; starts at (1.68, 0.00, 0.12) m, at rest
- flap1: hinge joint flap1_hinge about axis (0.00, 1.00, 0.00), range 0° to 64.9998° as MuJoCo applies it; its geoms: flap1; starts at 0.0°, still
- ball2: free body; its geoms: ball2; starts at (2.10, 0.13, 0.49) m, at rest
- seesaw1: hinge joint seesaw1_hinge about axis (0.00, 1.00, 0.00), range -40° to 0° as MuJoCo applies it; its geoms: seesaw1, seesaw1.seesaw left bracket, seesaw1.seesaw right bracket, seesaw1.seesaw left perch, seesaw1.seesaw right perch; starts at 0.0°, still
- block1: free body; its geoms: block1; starts at (3.23, 0.17, 1.00) m, at rest
- door1: hinge joint door1_hinge about axis (1.00, 0.00, 0.00), range 0° to 79.9998° as MuJoCo applies it; its geoms: door1; starts at 0.0°, still

What happened, in order:
 0.00 s  ball2 starts touching ball2 release lip
 0.00 s  ball1 starts touching ball1 release lip
 0.00 s  seesaw1.seesaw left perch starts touching block1
 0.00 s  domino1 starts touching floor
 0.00 s  ball2 starts touching ramp2
 0.00 s  ball1 starts touching ramp1
 0.00 s  seesaw1.seesaw right perch starts touching block1
 0.00 s  pendulum1 starts at its 55° stop (the end where it sits lower)
 0.00 s  pendulum1 is at its largest at the start, 55.0°
 0.00 s  cart1 starts at its lower stop (0 m)
 0.00 s  cart1 is at its largest at the start, 0.0 m
 0.00 s  flap1 starts at its 0° stop (the end where it sits higher)
 0.00 s  flap1 is at its largest at the start, 0.0°
 0.00 s  seesaw1 starts at its 0° stop (neither end sits lower)
 0.00 s  door1 starts at its 0° stop (the end where it sits lower)
 0.00 s  door1 is at its largest at the start, 0.0°
 0.09 s  seesaw1 is at its largest, 0.0°
 0.35 s  ball1 leaves ramp1
 0.35 s  pendulum1 first touches ball1
 0.35 s  ball1 starts moving
 0.35 s  pendulum1 is at its smallest, -0.6°
 0.35 s  pendulum1 passes 0.08 m from ball1 release lip without touching it: nearest points (0.03, 0.02, 0.49) m and (0.09, 0.02, 0.44) m
 0.37 s  pendulum1 leaves ball1
 0.45 s  ball1 touches ramp1 again
 0.45 s  ball1 leaves ball1 release lip
 0.54 s  ball1 touches ball1 release lip again
 0.54 s  ball1 leaves ramp1
 0.61 s  ball1 leaves ball1 release lip
 0.61 s  ball1 touches ramp1 again
 0.66 s  ball1 touches ball1 release lip again
 0.66 s  ball1 leaves ramp1
 0.67 s  ball1 comes to rest at (0.07, 0.00, 0.49) m
 0.70 s  ball1 leaves ball1 release lip
 0.70 s  ball1 touches ramp1 again
 0.73 s  ball1 touches ball1 release lip again
 0.92 s  pendulum1 passes 0.03 m from ramp1 without touching it: nearest points (0.01, 0.02, 0.49) m and (0.01, 0.02, 0.46) m
 0.98 s  pendulum1 touches ball1 again
 1.01 s  pendulum1 leaves ball1
 1.61 s  pendulum1 touches ball1 again
 1.64 s  pendulum1 leaves ball1
 2.20 s  pendulum1 touches ball1 again
 2.22 s  pendulum1 leaves ball1
 2.49 s  pendulum1 touches ball1 1 more times between 2.49 s and 12.00 s, still touching at the end

State every 0.25 s:
0.00 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.07, 0.00, 0.49) m, at rest; touching ball1 release lip, ramp1 | cart1 at 0.000 m, still; touching nothing | domino1 at (1.68, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | ball2 at (2.10, 0.13, 0.49) m, at rest; touching ball2 release lip, ramp2 | seesaw1 at 0.0°, still; touching block1 | block1 at (3.23, 0.17, 1.00) m, at rest; touching seesaw1.seesaw left perch, seesaw1.seesaw right perch | door1 at 0.0°, still; touching nothing
0.25 s: pendulum1 at 21.8°, turning -226°/s; touching nothing | ball1 at (0.07, 0.00, 0.49) m, at rest; touching ball1 release lip, ramp1 | cart1 at 0.000 m, still; touching nothing | domino1 at (1.68, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | ball2 at (2.10, 0.13, 0.49) m, at rest; touching ball2 release lip, ramp2 | seesaw1 at 0.0°, still; touching block1 | block1 at (3.23, 0.17, 1.00) m, at rest; touching seesaw1.seesaw left perch, seesaw1.seesaw right perch | door1 at 0.0°, still; touching nothing
0.50 s: pendulum1 at 3.6°, turning +22°/s; touching nothing | ball1 at (0.07, 0.00, 0.49) m, at rest; touching ramp1 | cart1 at 0.000 m, still; touching nothing | domino1 at (1.68, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | ball2 at (2.10, 0.13, 0.49) m, at rest; touching ball2 release lip, ramp2 | seesaw1 at 0.0°, still; touching block1 | block1 at (3.23, 0.17, 1.00) m, at rest; touching seesaw1.seesaw left perch, seesaw1.seesaw right perch | door1 at 0.0°, still; touching nothing
0.75 s: pendulum1 at 4.8°, turning -12°/s; touching nothing | ball1 at (0.07, 0.00, 0.49) m, at rest; touching ball1 release lip | cart1 at 0.000 m, still; touching nothing | domino1 at (1.68, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | ball2 at (2.10, 0.13, 0.49) m, at rest; touching ball2 release lip, ramp2 | seesaw1 at 0.0°, still; touching block1 | block1 at (3.23, 0.17, 1.00) m, at rest; touching seesaw1.seesaw left perch, seesaw1.seesaw right perch | door1 at 0.0°, still; touching nothing
1.00 s: pendulum1 at -0.0°, turning +4°/s; touching ball1 | ball1 at (0.07, 0.00, 0.49) m, at rest; touching ball1 release lip, pendulum1 | cart1 at 0.000 m, still; touching nothing | domino1 at (1.68, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | ball2 at (2.10, 0.13, 0.49) m, at rest; touching ball2 release lip, ramp2 | seesaw1 at 0.0°, still; touching block1 | block1 at (3.23, 0.17, 1.00) m, at rest; touching seesaw1.seesaw left perch, seesaw1.seesaw right perch | door1 at 0.0°, still; touching nothing
1.25 s: pendulum1 at 0.7°, still; touching nothing | ball1 at (0.07, 0.00, 0.49) m, at rest; touching ball1 release lip, ramp1 | cart1 at 0.000 m, still; touching nothing | domino1 at (1.68, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | ball2 at (2.10, 0.13, 0.49) m, at rest; touching ball2 release lip, ramp2 | seesaw1 at 0.0°, still; touching block1 | block1 at (3.23, 0.17, 1.00) m, at rest; touching seesaw1.seesaw left perch, seesaw1.seesaw right perch | door1 at 0.0°, still; touching nothing
1.50 s: pendulum1 at 0.4°, turning -3°/s; touching nothing | ball1 at (0.07, 0.00, 0.49) m, at rest; touching ball1 release lip, ramp1 | cart1 at 0.000 m, still; touching nothing | domino1 at (1.68, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | ball2 at (2.10, 0.13, 0.49) m, at rest; touching ball2 release lip, ramp2 | seesaw1 at 0.0°, still; touching block1 | block1 at (3.23, 0.17, 1.00) m, at rest; touching seesaw1.seesaw left perch, seesaw1.seesaw right perch | door1 at 0.0°, still; touching nothing
1.75 s: pendulum1 at 0.1°, still; touching nothing | ball1 at (0.07, 0.00, 0.49) m, at rest; touching ball1 release lip, ramp1 | cart1 at 0.000 m, still; touching nothing | domino1 at (1.68, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | ball2 at (2.10, 0.13, 0.49) m, at rest; touching ball2 release lip, ramp2 | seesaw1 at 0.0°, still; touching block1 | block1 at (3.23, 0.17, 1.00) m, at rest; touching seesaw1.seesaw left perch, seesaw1.seesaw right perch | door1 at 0.0°, still; touching nothing
(the same through 2.00 s)
2.25 s: pendulum1 at 0.0°, still; touching nothing | ball1 at (0.07, 0.00, 0.49) m, at rest; touching ball1 release lip, ramp1 | cart1 at 0.000 m, still; touching nothing | domino1 at (1.68, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | ball2 at (2.10, 0.13, 0.49) m, at rest; touching ball2 release lip, ramp2 | seesaw1 at 0.0°, still; touching block1 | block1 at (3.23, 0.17, 1.00) m, at rest; touching seesaw1.seesaw left perch, seesaw1.seesaw right perch | door1 at 0.0°, still; touching nothing
2.50 s: pendulum1 at 0.0°, still; touching ball1 | ball1 at (0.07, 0.00, 0.49) m, at rest; touching ball1 release lip, pendulum1, ramp1 | cart1 at 0.000 m, still; touching nothing | domino1 at (1.68, 0.00, 0.12) m, at rest; touching floor | flap1 at 0.0°, still; touching nothing | ball2 at (2.10, 0.13, 0.49) m, at rest; touching ball2 release lip, ramp2 | seesaw1 at 0.0°, still; touching block1 | block1 at (3.23, 0.17, 1.00) m, at rest; touching seesaw1.seesaw left perch, seesaw1.seesaw right perch | door1 at 0.0°, still; touching nothing
(the same through 12.00 s)

At the end (12.00 s):
- pendulum1 at 0.0°, still; touching ball1
- ball1 at (0.07, 0.00, 0.49) m, at rest; touching ball1 release lip, pendulum1, ramp1
- cart1 at 0.000 m, still; touching nothing
- domino1 at (1.68, 0.00, 0.12) m, at rest; touching floor
- flap1 at 0.0°, still; touching nothing
- ball2 at (2.10, 0.13, 0.49) m, at rest; touching ball2 release lip, ramp2
- seesaw1 at 0.0°, still; touching block1
- block1 at (3.23, 0.17, 1.00) m, at rest; touching seesaw1.seesaw left perch, seesaw1.seesaw right perch
- door1 at 0.0°, still; touching nothing

Openings (fixed rings, open through the middle; height is the middle of the whole thing), and each loose thing that comes down through one's height:
ring1: an opening 0.19 m across, centre (3.23, 0.17, 0.70) m
- nothing loose comes down through ring1's height
</history>
