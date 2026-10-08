MuJoCo ran your scene for 8 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 8.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- pendulum1: hinge joint pendulum_hinge about axis (0.00, 1.00, 0.00), range -70° to 55° as MuJoCo applies it; its geoms: pendulum1; starts at 55.0°, still
- ball1: free body; its geoms: ball1; starts at (0.08, 0.00, 0.51) m, at rest
- cart1: hinge joint cart_guide_approximation about axis (0.00, 0.00, 1.00), range 0° to 0.0229183° as MuJoCo applies it; its geoms: cart1; starts at 0.0°, still
- domino1: free body; its geoms: domino1; starts at (1.68, 0.00, 0.24) m, at rest
- flap1: hinge joint flap_hinge about axis (0.00, 1.00, 0.00), range -90.0002° to -25° as MuJoCo applies it; its geoms: flap1; starts at -90.0°, still
- ball2: free body; its geoms: ball2; starts at (2.25, 0.00, 0.39) m, at rest

What happened, in order:
 0.00 s  ball2 starts touching ball2 keeper
 0.00 s  domino1 starts touching domino support
 0.00 s  ball1 starts touching ball1 keeper
 0.00 s  ball1 starts touching ramp1_deck
 0.00 s  pendulum1 starts at its 55° stop (the end where it sits lower)
 0.00 s  pendulum1 is at its largest at the start, 55.0°
 0.00 s  cart1 starts at its 0° stop (neither end sits lower)
 0.00 s  cart1 starts at its 0.0229183° stop (neither end sits lower)
 0.00 s  cart1 is at its largest at the start, 0.0°
 0.00 s  flap1 starts at its -90.0002° stop (the end where it sits higher)
 0.00 s  flap1 is at its largest at the start, -90.0°
 0.00 s  ball2 first touches ramp2_deck
 0.35 s  ball1 leaves ramp1_deck
 0.35 s  pendulum1 first touches ball1
 0.35 s  ball1 starts moving
 0.35 s  flap1 is at its smallest, -90.0°
 0.35 s  pendulum1 passes 0.08 m from ball1 keeper without touching it: nearest points (0.04, 0.00, 0.50) m and (0.10, 0.00, 0.46) m
 0.35 s  pendulum1 is at its smallest, -0.8°
 0.38 s  pendulum1 leaves ball1
 0.40 s  ball1 leaves ball1 keeper
 0.40 s  ball1 touches ramp1_deck again
 0.44 s  pendulum1 passes 0.02 m from ramp1 (ramp1_deck) without touching it: nearest points (0.01, 0.00, 0.50) m and (0.01, 0.00, 0.48) m
 0.47 s  ball1 touches ball1 keeper again
 0.47 s  ball1 comes to rest at (0.08, 0.00, 0.51) m
 1.00 s  pendulum1 touches ball1 again
 1.03 s  pendulum1 leaves ball1
 1.64 s  pendulum1 touches ball1 again
 1.67 s  pendulum1 leaves ball1
 2.28 s  pendulum1 touches ball1 again
 2.32 s  pendulum1 leaves ball1
 2.88 s  pendulum1 touches ball1 17 more times between 2.88 s and 8.00 s, still touching at the end

State every 0.25 s:
0.00 s: pendulum1 at 55.0°, still; touching nothing | ball1 at (0.08, 0.00, 0.51) m, at rest; touching ball1 keeper, ramp1_deck | cart1 at 0.0°, still; touching nothing | domino1 at (1.68, 0.00, 0.24) m, at rest; touching domino support | flap1 at -90.0°, still; touching nothing | ball2 at (2.25, 0.00, 0.39) m, at rest; touching ball2 keeper
0.25 s: pendulum1 at 21.7°, turning -227°/s; touching nothing | ball1 at (0.08, 0.00, 0.51) m, at rest; touching ball1 keeper, ramp1_deck | cart1 at 0.0°, still; touching nothing | domino1 at (1.68, 0.00, 0.24) m, at rest; touching domino support | flap1 at -90.0°, still; touching nothing | ball2 at (2.25, 0.00, 0.39) m, at rest; touching ball2 keeper, ramp2_deck
0.50 s: pendulum1 at 2.5°, turning +18°/s; touching nothing | ball1 at (0.08, 0.00, 0.51) m, at rest; touching ball1 keeper, ramp1_deck | cart1 at 0.0°, still; touching nothing | domino1 at (1.68, 0.00, 0.24) m, at rest; touching domino support | flap1 at -90.0°, still; touching nothing | ball2 at (2.25, 0.00, 0.39) m, at rest; touching ball2 keeper, ramp2_deck
0.75 s: pendulum1 at 3.8°, turning -8°/s; touching nothing | ball1 at (0.08, 0.00, 0.51) m, at rest; touching ball1 keeper, ramp1_deck | cart1 at 0.0°, still; touching nothing | domino1 at (1.68, 0.00, 0.24) m, at rest; touching domino support | flap1 at -90.0°, still; touching nothing | ball2 at (2.25, 0.00, 0.39) m, at rest; touching ball2 keeper, ramp2_deck
1.00 s: pendulum1 at -0.1°, turning -6°/s; touching ball1 | ball1 at (0.08, 0.00, 0.51) m, at rest; touching ball1 keeper, pendulum1, ramp1_deck | cart1 at 0.0°, still; touching nothing | domino1 at (1.68, 0.00, 0.24) m, at rest; touching domino support | flap1 at -90.0°, still; touching nothing | ball2 at (2.25, 0.00, 0.39) m, at rest; touching ball2 keeper, ramp2_deck
1.25 s: pendulum1 at 0.6°, turning +1°/s; touching nothing | ball1 at (0.08, 0.00, 0.51) m, at rest; touching ball1 keeper, ramp1_deck | cart1 at 0.0°, still; touching nothing | domino1 at (1.68, 0.00, 0.24) m, at rest; touching domino support | flap1 at -90.0°, still; touching nothing | ball2 at (2.25, 0.00, 0.39) m, at rest; touching ball2 keeper, ramp2_deck
1.50 s: pendulum1 at 0.4°, turning -3°/s; touching nothing | ball1 at (0.08, 0.00, 0.51) m, at rest; touching ball1 keeper, ramp1_deck | cart1 at 0.0°, still; touching nothing | domino1 at (1.68, 0.00, 0.24) m, at rest; touching domino support | flap1 at -90.0°, still; touching nothing | ball2 at (2.25, 0.00, 0.39) m, at rest; touching ball2 keeper, ramp2_deck
1.75 s: pendulum1 at 0.0°, still; touching nothing | ball1 at (0.08, 0.00, 0.51) m, at rest; touching ball1 keeper, ramp1_deck | cart1 at 0.0°, still; touching nothing | domino1 at (1.68, 0.00, 0.24) m, at rest; touching domino support | flap1 at -90.0°, still; touching nothing | ball2 at (2.25, 0.00, 0.39) m, at rest; touching ball2 keeper, ramp2_deck
(the same through 3.00 s)
3.25 s: pendulum1 at 0.0°, still; touching ball1 | ball1 at (0.08, 0.00, 0.51) m, at rest; touching ball1 keeper, pendulum1, ramp1_deck | cart1 at 0.0°, still; touching nothing | domino1 at (1.68, 0.00, 0.24) m, at rest; touching domino support | flap1 at -90.0°, still; touching nothing | ball2 at (2.25, 0.00, 0.39) m, at rest; touching ball2 keeper, ramp2_deck
3.50 s: pendulum1 at 0.0°, still; touching nothing | ball1 at (0.08, 0.00, 0.51) m, at rest; touching ball1 keeper, ramp1_deck | cart1 at 0.0°, still; touching nothing | domino1 at (1.68, 0.00, 0.24) m, at rest; touching domino support | flap1 at -90.0°, still; touching nothing | ball2 at (2.25, 0.00, 0.39) m, at rest; touching ball2 keeper, ramp2_deck
(the same through 4.50 s)
4.75 s: pendulum1 at 0.0°, still; touching ball1 | ball1 at (0.08, 0.00, 0.51) m, at rest; touching ball1 keeper, pendulum1, ramp1_deck | cart1 at 0.0°, still; touching nothing | domino1 at (1.68, 0.00, 0.24) m, at rest; touching domino support | flap1 at -90.0°, still; touching nothing | ball2 at (2.25, 0.00, 0.39) m, at rest; touching ball2 keeper, ramp2_deck
5.00 s: pendulum1 at 0.0°, still; touching nothing | ball1 at (0.08, 0.00, 0.51) m, at rest; touching ball1 keeper, ramp1_deck | cart1 at 0.0°, still; touching nothing | domino1 at (1.68, 0.00, 0.24) m, at rest; touching domino support | flap1 at -90.0°, still; touching nothing | ball2 at (2.25, 0.00, 0.39) m, at rest; touching ball2 keeper, ramp2_deck
5.25 s: pendulum1 at 0.0°, still; touching ball1 | ball1 at (0.08, 0.00, 0.51) m, at rest; touching ball1 keeper, pendulum1, ramp1_deck | cart1 at 0.0°, still; touching nothing | domino1 at (1.68, 0.00, 0.24) m, at rest; touching domino support | flap1 at -90.0°, still; touching nothing | ball2 at (2.25, 0.00, 0.39) m, at rest; touching ball2 keeper, ramp2_deck
(the same through 8.00 s)

At the end (8.00 s):
- pendulum1 at 0.0°, still; touching ball1
- ball1 at (0.08, 0.00, 0.51) m, at rest; touching ball1 keeper, pendulum1, ramp1_deck
- cart1 at 0.0°, still; touching nothing
- domino1 at (1.68, 0.00, 0.24) m, at rest; touching domino support
- flap1 at -90.0°, still; touching nothing
- ball2 at (2.25, 0.00, 0.39) m, at rest; touching ball2 keeper, ramp2_deck
</history>
