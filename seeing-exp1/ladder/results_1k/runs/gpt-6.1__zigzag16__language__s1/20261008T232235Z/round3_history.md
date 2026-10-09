Before the run, at the start:
- pendulum booster already touches pendulum1 at the start, so their touch is not something that happens in the run
- seesaw booster already touches seesaw1 at the start, so their touch is not something that happens in the run
- ball3 already touches seesaw1 at the start, so their touch is not something that happens in the run

MuJoCo ran your scene for 20 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 20.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- lever1: hinge joint lever1_hinge about axis (0.00, 1.00, 0.00), range -45° to 0° as MuJoCo applies it; its geoms: lever1, lever1.lever paddle; starts at 0.0°, still
- lever booster: hinge joint lever_booster_hinge about axis (0.00, 1.00, 0.00), range -45° to 0° as MuJoCo applies it; its geoms: lever booster, lever booster coupling; starts at 0.0°, still
- ball1: free body; its geoms: ball1; starts at (-0.03, 0.00, 1.55) m, at rest
- cart1: free body; its geoms: cart1, cart1 striker; starts at (0.31, 0.00, 0.42) m, at rest
- domino1: free body; its geoms: domino1; starts at (0.88, 0.00, 0.49) m, at rest
- ball2: free body; its geoms: ball2; starts at (1.06, 0.00, 0.54) m, at rest
- door1: hinge joint door1_hinge about axis (0.00, 1.00, 0.00), range 0° to 70° as MuJoCo applies it; its geoms: door1; starts at 0.0°, still
- pendulum1: hinge joint pendulum1_hinge about axis (0.00, 1.00, 0.00), range -38° to 0° as MuJoCo applies it; its geoms: pendulum1; starts at 0.0°, still
- pendulum booster: hinge joint pendulum_booster_hinge about axis (0.00, 1.00, 0.00), range -38° to 0° as MuJoCo applies it; its geoms: pendulum booster, pendulum booster.pendulum front coupling, pendulum booster.pendulum back coupling; starts at 0.0°, still
- block1: free body; its geoms: block1; starts at (2.82, 0.00, 0.06) m, at rest
- cart2: free body; its geoms: cart2, cart2 striker; starts at (3.34, 0.00, 0.05) m, at rest
- seesaw1: hinge joint seesaw1_hinge about axis (0.00, 1.00, 0.00), range -42° to 0° as MuJoCo applies it; its geoms: seesaw1, seesaw1.seesaw left end fin; starts at 0.0°, still
- seesaw booster: hinge joint seesaw_booster_hinge about axis (0.00, 1.00, 0.00), range -42° to 0° as MuJoCo applies it; its geoms: seesaw booster, seesaw booster.seesaw lower coupling, seesaw booster.seesaw upper coupling; starts at 0.0°, still
- ball3: free body; its geoms: ball3; starts at (4.54, 0.07, 1.45) m, at rest
- domino2: free body; its geoms: domino2; starts at (4.52, 0.07, 0.72) m, at rest
- flap1: hinge joint flap1_hinge about axis (0.00, 1.00, 0.00), range 0° to 60.0001° as MuJoCo applies it; its geoms: flap1; starts at 0.0°, still
- ball4: free body; its geoms: ball4; starts at (5.09, 0.07, 0.82) m, at rest

What happened, in order:
 0.00 s  seesaw1 starts touching seesaw booster.seesaw lower coupling
 0.00 s  cart2 starts touching floor
 0.00 s  pendulum1 starts touching pendulum booster.pendulum front coupling
 0.00 s  domino1 starts touching first slide bed
 0.00 s  block1 starts touching floor
 0.00 s  seesaw1 starts touching ball3
 0.00 s  seesaw1 starts touching seesaw booster.seesaw upper coupling
 0.00 s  domino2 starts touching final platform
 0.00 s  ball2 starts touching ramp retaining lip
 0.00 s  cart1 starts touching first slide bed
 0.00 s  ball4 starts touching shelf1
 0.00 s  lever1 starts at its 0° stop (neither end sits lower)
 0.00 s  lever booster starts at its 0° stop (neither end sits lower)
 0.00 s  door1 starts at its 0° stop (the end where it sits higher)
 0.00 s  door1 is at its largest at the start, 0.0°
 0.00 s  pendulum1 starts at its 0° stop (the end where it sits higher)
 0.00 s  pendulum booster starts at its 0° stop (neither end sits lower)
 0.00 s  seesaw1 starts at its 0° stop (neither end sits lower)
 0.00 s  seesaw booster starts at its 0° stop (neither end sits lower)
 0.00 s  flap1 starts at its 0° stop (the end where it sits higher)
 0.00 s  flap1 is at its largest at the start, 0.0°
 0.00 s  lever1 first touches lever booster coupling
 0.00 s  ball2 first touches ramp1
 0.01 s  ball1 starts moving
 0.02 s  ball3 starts moving
 0.02 s  ball3 first touches ball3 far guide
 0.02 s  ball3 comes to rest at (4.54, 0.07, 1.45) m
 0.03 s  ball3 first touches ball3 left guide
 0.07 s  seesaw1 is at its largest, 0.0°
 0.08 s  seesaw booster is at its largest, 0.0°
 0.25 s  ball1 passes 0.02 m from ring1 (ring1_07) without touching it: nearest points (-0.08, 0.01, 1.25) m and (-0.10, 0.01, 1.25) m
 0.26 s  lever booster is at its largest, 0.0°
 0.33 s  lever1 is at its largest, 0.0°
 0.34 s  lever1 first touches ball1
 0.38 s  lever1 leaves ball1
 0.39 s  ball1 is at the top of its flight, at (-0.03, 0.00, 1.00) m
 0.43 s  lever1.lever paddle first touches cart1
 0.43 s  cart1 starts moving
 0.44 s  cart1 first touches first slide left roof
 0.44 s  cart1 first touches first slide right roof
 0.44 s  lever booster passes 0.04 m from first slide bed without touching it: nearest points (0.15, 0.04, 0.40) m and (0.18, 0.04, 0.37) m
 0.45 s  lever1.lever paddle leaves cart1
 0.45 s  lever booster passes 0.07 m from cart1 without touching it: nearest points (0.21, 0.02, 0.44) m and (0.27, 0.02, 0.45) m
 0.46 s  lever1 first touches lever right hard stop
 0.46 s  lever1 first touches lever left hard stop
 0.52 s  cart1 leaves first slide left roof
 0.52 s  cart1 leaves first slide right roof
 0.59 s  cart1 comes to rest at (0.53, 0.00, 0.42) m
 0.61 s  lever1 touches ball1 again
 0.70 s  lever booster passes 0.02 m from ball1 without touching it: nearest points (0.00, 0.00, 0.65) m and (0.01, 0.00, 0.67) m
 0.87 s  lever1 leaves ball1
 0.87 s  lever1.lever paddle first touches ball1
 0.88 s  ball1 passes 0.05 m from lever left hard stop without touching it: nearest points (0.25, 0.02, 0.56) m and (0.26, 0.03, 0.52) m
 0.88 s  ball1 passes 0.05 m from lever right hard stop without touching it: nearest points (0.25, -0.02, 0.56) m and (0.26, -0.03, 0.52) m
 0.91 s  lever1.lever paddle leaves ball1
 0.91 s  cart1 passes 0.38 m from ramp1 without touching it: nearest points (0.65, -0.02, 0.45) m and (1.03, -0.02, 0.45) m
 0.93 s  cart1 passes 0.20 m from first slide left bumper without touching it: nearest points (0.65, 0.05, 0.47) m and (0.85, 0.05, 0.47) m
 0.93 s  cart1 passes 0.20 m from first slide right bumper without touching it: nearest points (0.65, -0.08, 0.47) m and (0.85, -0.08, 0.47) m
 0.93 s  cart1 passes 0.43 m from ramp retaining lip without touching it: nearest points (0.65, -0.03, 0.49) m and (1.07, -0.03, 0.49) m
 0.95 s  cart1 passes 0.36 m from ball2 without touching it: nearest points (0.65, 0.00, 0.54) m and (1.01, 0.00, 0.54) m
 0.96 s  ball1 first touches ball1 screen
 0.96 s  ball1 passes 0.17 m from cart1 without touching it: nearest points (0.30, 0.00, 0.59) m and (0.43, 0.00, 0.47) m
 0.97 s  cart1 passes 0.19 m from domino1 without touching it: nearest points (0.65, -0.02, 0.59) m and (0.84, -0.02, 0.59) m
 0.98 s  ball1 leaves ball1 screen
 0.99 s  lever1.lever paddle touches ball1 again
 1.10 s  lever1.lever paddle leaves ball1
 1.11 s  lever1 touches ball1 again
 1.11 s  ball1 passes 0.08 m from first slide left roof without touching it: nearest points (0.23, 0.03, 0.56) m and (0.23, 0.07, 0.49) m
 1.11 s  ball1 passes 0.08 m from first slide right roof without touching it: nearest points (0.23, -0.03, 0.56) m and (0.23, -0.07, 0.49) m
 1.11 s  ball1 passes 0.10 m from first slide left rail without touching it: nearest points (0.23, 0.03, 0.56) m and (0.23, 0.09, 0.49) m
 1.11 s  ball1 passes 0.10 m from first slide right rail without touching it: nearest points (0.23, -0.03, 0.56) m and (0.23, -0.09, 0.49) m
 1.11 s  ball1 passes 0.18 m from first slide bed without touching it: nearest points (0.23, 0.00, 0.55) m and (0.23, 0.00, 0.37) m
 1.23 s  lever1.lever paddle touches ball1 again
 1.25 s  ball1 comes to rest at (0.23, 0.00, 0.60) m
 4.96 s  lever1 passes 0.04 m from ball1 screen without touching it: nearest points (0.28, 0.02, 0.58) m and (0.31, 0.02, 0.60) m
 8.76 s  pendulum booster is at its largest, 0.0°
15.36 s  lever booster passes 0.05 m from first slide left rail without touching it: nearest points (0.24, 0.04, 0.49) m and (0.24, 0.09, 0.49) m
15.36 s  lever booster passes 0.05 m from first slide right rail without touching it: nearest points (0.24, -0.04, 0.49) m and (0.24, -0.09, 0.49) m
15.36 s  lever booster passes 0.02 m from first slide left roof without touching it: nearest points (0.24, 0.04, 0.49) m and (0.24, 0.07, 0.49) m
15.36 s  lever booster passes 0.02 m from first slide right roof without touching it: nearest points (0.24, -0.04, 0.49) m and (0.24, -0.07, 0.49) m
15.70 s  pendulum1 is at its largest, 0.0°
16.47 s  lever1 is at its smallest, -51.7°
16.47 s  lever booster passes 0.01 m from lever left hard stop without touching it: nearest points (0.25, 0.03, 0.49) m and (0.26, 0.03, 0.50) m
16.47 s  lever booster passes 0.01 m from lever right hard stop without touching it: nearest points (0.25, -0.03, 0.49) m and (0.26, -0.03, 0.50) m
16.47 s  lever booster passes 0.12 m from ball1 screen without touching it: nearest points (0.25, 0.04, 0.49) m and (0.31, 0.04, 0.60) m
16.47 s  lever booster is at its smallest, -51.7°
18.79 s  lever1 passes 0.01 m from first slide left roof without touching it: nearest points (0.26, 0.05, 0.49) m and (0.26, 0.07, 0.49) m
18.79 s  lever1 passes 0.01 m from first slide right roof without touching it: nearest points (0.26, -0.05, 0.49) m and (0.26, -0.07, 0.49) m

State every 0.25 s:
0.00 s: lever1 at 0.0°, still; touching nothing | lever booster at 0.0°, still; touching nothing | ball1 at (-0.03, 0.00, 1.55) m, at rest; touching nothing | cart1 at (0.31, 0.00, 0.42) m, at rest; touching first slide bed | domino1 at (0.88, 0.00, 0.49) m, at rest; touching first slide bed | ball2 at (1.06, 0.00, 0.54) m, at rest; touching ramp retaining lip | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching pendulum booster.pendulum front coupling | pendulum booster at 0.0°, still; touching pendulum1 | block1 at (2.82, 0.00, 0.06) m, at rest; touching floor | cart2 at (3.34, 0.00, 0.05) m, at rest; touching floor | seesaw1 at 0.0°, still; touching ball3, seesaw booster.seesaw lower coupling, seesaw booster.seesaw upper coupling | seesaw booster at 0.0°, still; touching seesaw1 | ball3 at (4.54, 0.07, 1.45) m, at rest; touching seesaw1 | domino2 at (4.52, 0.07, 0.72) m, at rest; touching final platform | flap1 at 0.0°, still; touching nothing | ball4 at (5.09, 0.07, 0.82) m, at rest; touching shelf1
0.25 s: lever1 at 0.0°, still; touching lever booster coupling | lever booster at 0.0°, still; touching lever1 | ball1 at (-0.03, 0.00, 1.24) m, moving 2.45 m/s (vx +0.00, vy +0.00, vz -2.45); touching nothing | cart1 at (0.31, 0.00, 0.42) m, at rest; touching first slide bed | domino1 at (0.88, 0.00, 0.49) m, at rest; touching first slide bed | ball2 at (1.06, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1 | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching pendulum booster.pendulum front coupling | pendulum booster at 0.0°, still; touching pendulum1 | block1 at (2.82, 0.00, 0.06) m, at rest; touching floor | cart2 at (3.34, 0.00, 0.05) m, at rest; touching floor | seesaw1 at 0.0°, still; touching ball3, seesaw booster.seesaw lower coupling, seesaw booster.seesaw upper coupling | seesaw booster at 0.0°, still; touching seesaw1 | ball3 at (4.54, 0.07, 1.45) m, at rest; touching ball3 far guide, ball3 left guide, seesaw1 | domino2 at (4.52, 0.07, 0.72) m, at rest; touching final platform | flap1 at 0.0°, still; touching nothing | ball4 at (5.09, 0.07, 0.82) m, at rest; touching shelf1
0.50 s: lever1 at -50.9°, turning -4°/s; touching lever booster coupling, lever left hard stop, lever right hard stop | lever booster at -50.8°, turning -8°/s; touching lever1 | ball1 at (-0.04, 0.00, 0.94) m, moving 1.11 m/s (vx -0.04, vy +0.00, vz -1.11); touching nothing | cart1 at (0.50, 0.00, 0.42) m, moving 0.94 m/s (vx +0.93, vy -0.00, vz +0.14); touching first slide bed | domino1 at (0.88, 0.00, 0.49) m, at rest; touching first slide bed | ball2 at (1.06, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1 | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching pendulum booster.pendulum front coupling | pendulum booster at 0.0°, still; touching pendulum1 | block1 at (2.82, 0.00, 0.06) m, at rest; touching floor | cart2 at (3.34, 0.00, 0.05) m, at rest; touching floor | seesaw1 at 0.0°, still; touching ball3, seesaw booster.seesaw lower coupling, seesaw booster.seesaw upper coupling | seesaw booster at 0.0°, still; touching seesaw1 | ball3 at (4.54, 0.07, 1.45) m, at rest; touching ball3 far guide, ball3 left guide, seesaw1 | domino2 at (4.52, 0.07, 0.72) m, at rest; touching final platform | flap1 at 0.0°, still; touching nothing | ball4 at (5.09, 0.07, 0.82) m, at rest; touching shelf1
0.75 s: lever1 at -51.4°, turning -1°/s; touching ball1, lever booster coupling, lever left hard stop, lever right hard stop | lever booster at -51.4°, turning -1°/s; touching lever1 | ball1 at (0.08, 0.00, 0.69) m, moving 1.23 m/s (vx +1.08, vy +0.00, vz -0.59); touching lever1 | cart1 at (0.54, 0.00, 0.42) m, at rest; touching first slide bed | domino1 at (0.88, 0.00, 0.49) m, at rest; touching first slide bed | ball2 at (1.06, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1 | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching pendulum booster.pendulum front coupling | pendulum booster at 0.0°, still; touching pendulum1 | block1 at (2.82, 0.00, 0.06) m, at rest; touching floor | cart2 at (3.34, 0.00, 0.05) m, at rest; touching floor | seesaw1 at 0.0°, still; touching ball3, seesaw booster.seesaw lower coupling, seesaw booster.seesaw upper coupling | seesaw booster at 0.0°, still; touching seesaw1 | ball3 at (4.54, 0.07, 1.45) m, at rest; touching ball3 far guide, ball3 left guide, seesaw1 | domino2 at (4.52, 0.07, 0.72) m, at rest; touching final platform | flap1 at 0.0°, still; touching nothing | ball4 at (5.09, 0.07, 0.82) m, at rest; touching shelf1
1.00 s: lever1 at -51.6°, still; touching ball1, lever booster coupling, lever left hard stop, lever right hard stop | lever booster at -51.6°, still; touching lever1 | ball1 at (0.26, 0.00, 0.62) m, moving 0.13 m/s (vx -0.12, vy +0.00, vz -0.05); touching lever1.lever paddle | cart1 at (0.54, 0.00, 0.42) m, at rest; touching first slide bed | domino1 at (0.88, 0.00, 0.49) m, at rest; touching first slide bed | ball2 at (1.06, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1 | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching pendulum booster.pendulum front coupling | pendulum booster at 0.0°, still; touching pendulum1 | block1 at (2.82, 0.00, 0.06) m, at rest; touching floor | cart2 at (3.34, 0.00, 0.05) m, at rest; touching floor | seesaw1 at 0.0°, still; touching ball3, seesaw booster.seesaw lower coupling, seesaw booster.seesaw upper coupling | seesaw booster at 0.0°, still; touching seesaw1 | ball3 at (4.54, 0.07, 1.45) m, at rest; touching ball3 far guide, ball3 left guide, seesaw1 | domino2 at (4.52, 0.07, 0.72) m, at rest; touching final platform | flap1 at 0.0°, still; touching nothing | ball4 at (5.09, 0.07, 0.82) m, at rest; touching shelf1
1.25 s: lever1 at -51.7°, still; touching ball1, lever booster coupling, lever left hard stop, lever right hard stop | lever booster at -51.7°, still; touching lever1 | ball1 at (0.23, 0.00, 0.60) m, moving 0.06 m/s (vx -0.05, vy +0.00, vz -0.03); touching lever1.lever paddle | cart1 at (0.54, 0.00, 0.42) m, at rest; touching first slide bed | domino1 at (0.88, 0.00, 0.49) m, at rest; touching first slide bed | ball2 at (1.06, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1 | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching pendulum booster.pendulum front coupling | pendulum booster at 0.0°, still; touching pendulum1 | block1 at (2.82, 0.00, 0.06) m, at rest; touching floor | cart2 at (3.34, 0.00, 0.05) m, at rest; touching floor | seesaw1 at 0.0°, still; touching ball3, seesaw booster.seesaw lower coupling, seesaw booster.seesaw upper coupling | seesaw booster at 0.0°, still; touching seesaw1 | ball3 at (4.54, 0.07, 1.45) m, at rest; touching ball3 far guide, ball3 left guide, seesaw1 | domino2 at (4.52, 0.07, 0.72) m, at rest; touching final platform | flap1 at 0.0°, still; touching nothing | ball4 at (5.09, 0.07, 0.82) m, at rest; touching shelf1
1.50 s: lever1 at -51.7°, still; touching ball1, lever booster coupling, lever left hard stop, lever right hard stop | lever booster at -51.7°, still; touching lever1 | ball1 at (0.23, 0.00, 0.60) m, at rest; touching lever1, lever1.lever paddle | cart1 at (0.54, 0.00, 0.42) m, at rest; touching first slide bed | domino1 at (0.88, 0.00, 0.49) m, at rest; touching first slide bed | ball2 at (1.06, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1 | door1 at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching pendulum booster.pendulum front coupling | pendulum booster at 0.0°, still; touching pendulum1 | block1 at (2.82, 0.00, 0.06) m, at rest; touching floor | cart2 at (3.34, 0.00, 0.05) m, at rest; touching floor | seesaw1 at 0.0°, still; touching ball3, seesaw booster.seesaw lower coupling, seesaw booster.seesaw upper coupling | seesaw booster at 0.0°, still; touching seesaw1 | ball3 at (4.54, 0.07, 1.45) m, at rest; touching ball3 far guide, ball3 left guide, seesaw1 | domino2 at (4.52, 0.07, 0.72) m, at rest; touching final platform | flap1 at 0.0°, still; touching nothing | ball4 at (5.09, 0.07, 0.82) m, at rest; touching shelf1
(the same through 20.00 s)

At the end (20.00 s):
- lever1 at -51.7°, still; touching ball1, lever booster coupling, lever left hard stop, lever right hard stop
- lever booster at -51.7°, still; touching lever1
- ball1 at (0.23, 0.00, 0.60) m, at rest; touching lever1, lever1.lever paddle
- cart1 at (0.54, 0.00, 0.42) m, at rest; touching first slide bed
- domino1 at (0.88, 0.00, 0.49) m, at rest; touching first slide bed
- ball2 at (1.06, 0.00, 0.54) m, at rest; touching ramp retaining lip, ramp1
- door1 at 0.0°, still; touching nothing
- pendulum1 at 0.0°, still; touching pendulum booster.pendulum front coupling
- pendulum booster at 0.0°, still; touching pendulum1
- block1 at (2.82, 0.00, 0.06) m, at rest; touching floor
- cart2 at (3.34, 0.00, 0.05) m, at rest; touching floor
- seesaw1 at 0.0°, still; touching ball3, seesaw booster.seesaw lower coupling, seesaw booster.seesaw upper coupling
- seesaw booster at 0.0°, still; touching seesaw1
- ball3 at (4.54, 0.07, 1.45) m, at rest; touching ball3 far guide, ball3 left guide, seesaw1
- domino2 at (4.52, 0.07, 0.72) m, at rest; touching final platform
- flap1 at 0.0°, still; touching nothing
- ball4 at (5.09, 0.07, 0.82) m, at rest; touching shelf1

Openings (fixed rings, open through the middle; height is the middle of the whole thing), and each loose thing that comes down through one's height:
ring1: an opening 0.16 m across, centre (-0.03, 0.00, 1.25) m
- ball1 comes down through ring1's height at 0.25 s, 0.00 m from its centre: through it
ring2: an opening 0.16 m across, centre (4.54, 0.07, 1.13) m
- ball1 comes down through ring2's height at 0.29 s, 4.58 m from its centre: outside it, missing by 4.50 m
</history>
