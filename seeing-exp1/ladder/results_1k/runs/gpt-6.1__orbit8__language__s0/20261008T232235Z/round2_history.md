MuJoCo ran your scene for 12 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 12.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum1: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), range -60.0001° to 55° as MuJoCo applies it; its geoms: pendulum1; starts at 55.0°, still
- ball1: free body; its geoms: ball1; starts at (0.04, 0.00, 0.50) m, at rest
- cart1: free body; its geoms: cart1; starts at (1.13, 0.00, 0.15) m, at rest
- domino1: free body; its geoms: domino1; starts at (1.68, 0.00, 0.22) m, at rest
- flap1: hinge joint flap_hinge about axis (0.00, 1.00, 0.00), range 25° to 90.0002° as MuJoCo applies it; its geoms: flap1; starts at 90.0°, still
- ball2: free body; its geoms: ball2; starts at (2.33, 0.00, 0.50) m, at rest
- seesaw1: hinge joint seesaw_hinge about axis (0.00, 1.00, 0.00), range -85° to -45° as MuJoCo applies it; its geoms: seesaw1; starts at -45.0°, still
- block1: free body; its geoms: block1; starts at (3.73, 0.00, 0.73) m, at rest
- door1: hinge joint door_hinge about axis (0.00, 1.00, 0.00), range 0° to 10° as MuJoCo applies it; its geoms: door1; starts at 0.0°, still

What happened, in order:
 0.00 s  ball2 starts touching ramp2_deck
 0.00 s  ball1 starts touching ramp1_deck
 0.00 s  cart1 starts touching cart track
 0.00 s  pendulum1 starts at its 55° stop (the end where it sits lower)
 0.00 s  pendulum1 is at its largest at the start, 55.0°
 0.00 s  flap1 starts at its 90.0002° stop (the end where it sits lower)
 0.00 s  flap1 is at its largest at the start, 90.0°
 0.00 s  seesaw1 starts at its -45° stop (neither end sits lower)
 0.00 s  door1 starts at its 0° stop (the end where it sits higher)
 0.00 s  door1 is at its largest at the start, 0.0°
 0.00 s  domino1 first touches cart track
 0.00 s  seesaw1 first touches block1
 0.00 s  block1 first touches block left ledge
 0.00 s  block1 first touches block right ledge
 0.02 s  ball1 starts moving
 0.02 s  ball2 starts moving
 0.06 s  ball2 leaves ramp2_deck
 0.06 s  ball1 leaves ramp1_deck
 0.06 s  ball1 first touches ball1 retainer
 0.06 s  ball2 first touches ball2 retainer
 0.09 s  ball2 touches ramp2_deck again
 0.09 s  ball1 touches ramp1_deck again
 0.09 s  ball2 comes to rest at (2.33, 0.00, 0.50) m
 0.09 s  ball1 leaves ball1 retainer
 0.09 s  ball2 leaves ball2 retainer
 0.13 s  ball1 touches ball1 retainer again
 0.13 s  ball2 touches ball2 retainer again
 0.35 s  ball1 leaves ramp1_deck
 0.35 s  pendulum1 first touches ball1
 0.35 s  pendulum1 passes 0.04 m from ramp1 (ramp1_deck) without touching it: nearest points (0.00, 0.02, 0.50) m and (0.01, 0.02, 0.46) m
 0.35 s  pendulum1 passes 0.08 m from ball1 retainer without touching it: nearest points (0.00, -0.02, 0.50) m and (0.08, -0.02, 0.46) m
 0.35 s  pendulum1 is at its smallest, -0.6°
 0.38 s  ball1 touches ramp1_deck again
 0.38 s  ball1 leaves ball1 retainer
 0.38 s  pendulum1 leaves ball1
 0.38 s  ball1 comes to rest at (0.04, 0.00, 0.50) m
 0.43 s  ball1 touches ball1 retainer again
 0.44 s  seesaw1 is at its largest, -45.0°
 0.48 s  door1 is at its smallest, -0.0°
 0.53 s  flap1 is at its smallest, 90.0°
 0.98 s  pendulum1 touches ball1 again
 1.01 s  pendulum1 leaves ball1
 1.49 s  pendulum1 touches ball1 again
 1.53 s  pendulum1 leaves ball1
 1.60 s  pendulum1 touches ball1 again

State every 0.25 s:
0.00 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.04, 0.00, 0.50) m, at rest; touching ramp1_deck | cart1 at (1.13, 0.00, 0.15) m, at rest; touching cart track | domino1 at (1.68, 0.00, 0.22) m, at rest; touching nothing | flap1 at 90.0°, still; touching nothing | ball2 at (2.33, 0.00, 0.50) m, at rest; touching ramp2_deck | seesaw1 at -45.0°, still; touching nothing | block1 at (3.73, 0.00, 0.73) m, at rest; touching nothing | door1 at 0.0°, still; touching nothing
0.25 s: pendulum1 at 21.8°, turning -226°/s; touching nothing | ball1 at (0.05, 0.00, 0.50) m, at rest; touching ball1 retainer, ramp1_deck | cart1 at (1.13, 0.00, 0.15) m, at rest; touching cart track | domino1 at (1.68, 0.00, 0.22) m, at rest; touching cart track | flap1 at 90.0°, still; touching nothing | ball2 at (2.33, 0.00, 0.50) m, at rest; touching ball2 retainer, ramp2_deck | seesaw1 at -45.0°, still; touching block1 | block1 at (3.73, 0.00, 0.73) m, at rest; touching block left ledge, block right ledge, seesaw1 | door1 at -0.0°, still; touching nothing
0.50 s: pendulum1 at 3.1°, turning +20°/s; touching nothing | ball1 at (0.05, 0.00, 0.50) m, at rest; touching ball1 retainer, ramp1_deck | cart1 at (1.13, 0.00, 0.15) m, at rest; touching cart track | domino1 at (1.68, 0.00, 0.22) m, at rest; touching cart track | flap1 at 90.0°, still; touching nothing | ball2 at (2.33, 0.00, 0.50) m, at rest; touching ball2 retainer, ramp2_deck | seesaw1 at -45.0°, still; touching block1 | block1 at (3.73, 0.00, 0.73) m, at rest; touching block left ledge, block right ledge, seesaw1 | door1 at -0.0°, still; touching nothing
0.75 s: pendulum1 at 4.3°, turning -10°/s; touching nothing | ball1 at (0.05, 0.00, 0.50) m, at rest; touching ball1 retainer, ramp1_deck | cart1 at (1.13, 0.00, 0.15) m, at rest; touching cart track | domino1 at (1.68, 0.00, 0.22) m, at rest; touching cart track | flap1 at 90.0°, still; touching nothing | ball2 at (2.33, 0.00, 0.50) m, at rest; touching ball2 retainer, ramp2_deck | seesaw1 at -45.0°, still; touching block1 | block1 at (3.73, 0.00, 0.73) m, at rest; touching block left ledge, block right ledge, seesaw1 | door1 at -0.0°, still; touching nothing
1.00 s: pendulum1 at 0.2°, turning +3°/s; touching ball1 | ball1 at (0.05, 0.00, 0.50) m, at rest; touching ball1 retainer, pendulum1, ramp1_deck | cart1 at (1.13, 0.00, 0.15) m, at rest; touching cart track | domino1 at (1.68, 0.00, 0.22) m, at rest; touching cart track | flap1 at 90.0°, still; touching nothing | ball2 at (2.33, 0.00, 0.50) m, at rest; touching ball2 retainer, ramp2_deck | seesaw1 at -45.0°, still; touching block1 | block1 at (3.73, 0.00, 0.73) m, at rest; touching block left ledge, block right ledge, seesaw1 | door1 at -0.0°, still; touching nothing
1.25 s: pendulum1 at 0.5°, still; touching nothing | ball1 at (0.05, 0.00, 0.50) m, at rest; touching ball1 retainer, ramp1_deck | cart1 at (1.13, 0.00, 0.15) m, at rest; touching cart track | domino1 at (1.68, 0.00, 0.22) m, at rest; touching cart track | flap1 at 90.0°, still; touching nothing | ball2 at (2.33, 0.00, 0.50) m, at rest; touching ball2 retainer, ramp2_deck | seesaw1 at -45.0°, still; touching block1 | block1 at (3.73, 0.00, 0.73) m, at rest; touching block left ledge, block right ledge, seesaw1 | door1 at -0.0°, still; touching nothing
1.50 s: pendulum1 at 0.2°, still; touching ball1 | ball1 at (0.05, 0.00, 0.50) m, at rest; touching ball1 retainer, pendulum1, ramp1_deck | cart1 at (1.13, 0.00, 0.15) m, at rest; touching cart track | domino1 at (1.68, 0.00, 0.22) m, at rest; touching cart track | flap1 at 90.0°, still; touching nothing | ball2 at (2.33, 0.00, 0.50) m, at rest; touching ball2 retainer, ramp2_deck | seesaw1 at -45.0°, still; touching block1 | block1 at (3.73, 0.00, 0.73) m, at rest; touching block left ledge, block right ledge, seesaw1 | door1 at -0.0°, still; touching nothing
(the same through 12.00 s)

At the end (12.00 s):
- pendulum1 at 0.2°, still; touching ball1
- ball1 at (0.05, 0.00, 0.50) m, at rest; touching ball1 retainer, pendulum1, ramp1_deck
- cart1 at (1.13, 0.00, 0.15) m, at rest; touching cart track
- domino1 at (1.68, 0.00, 0.22) m, at rest; touching cart track
- flap1 at 90.0°, still; touching nothing
- ball2 at (2.33, 0.00, 0.50) m, at rest; touching ball2 retainer, ramp2_deck
- seesaw1 at -45.0°, still; touching block1
- block1 at (3.73, 0.00, 0.73) m, at rest; touching block left ledge, block right ledge, seesaw1
- door1 at -0.0°, still; touching nothing

Openings (fixed rings, open through the middle; height is the middle of the whole thing), and each loose thing that comes down through one's height:
ring1: an opening 0.21 m across, centre (3.73, 0.00, 0.43) m
- nothing loose comes down through ring1's height
</history>
