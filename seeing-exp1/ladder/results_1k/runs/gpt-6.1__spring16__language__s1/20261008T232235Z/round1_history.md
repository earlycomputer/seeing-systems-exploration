Before the run, at the start:
- ball5 already touches seesaw1 at the start, so their touch is not something that happens in the run

MuJoCo ran your scene for 20 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 0.01 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (-4.98, 0.00, 0.56) m, at rest
- cart1: free body; its geoms: cart1; starts at (-5.64, 0.00, 0.56) m, at rest
- cart1 spring pusher: hinge joint cart1_spring_hinge about axis (0.00, 1.00, 0.00), range 0° to 22.9183° as MuJoCo applies it; its geoms: cart1 spring pusher; starts at 0.0°, still
- pendulum1: hinge joint pendulum1_hinge about axis (0.00, 1.00, 0.00), range -40° to 0° as MuJoCo applies it; its geoms: pendulum1, pendulum1 rod; starts at 0.0°, still
- door1: hinge joint door1_hinge about axis (0.00, 1.00, 0.00), range -90.0002° to -20° as MuJoCo applies it; its geoms: door1; starts at -90.0°, still
- block1: free body; its geoms: block1; starts at (-3.20, 0.00, 0.06) m, at rest
- domino1: free body; its geoms: domino1; starts at (-2.78, 0.00, 0.12) m, at rest
- lever1: hinge joint lever1_hinge about axis (0.00, 1.00, 0.00), range -45° to 0° as MuJoCo applies it; its geoms: lever1, lever1 striker; starts at 0.0°, still
- ball2: free body; its geoms: ball2; starts at (-2.03, 0.00, 1.07) m, at rest
- cart2: free body; its geoms: cart2; starts at (-1.75, 0.50, 0.40) m, at rest
- domino2: free body; its geoms: domino2; starts at (-1.20, 0.50, 0.47) m, at rest
- ball3: free body; its geoms: ball3; starts at (-0.99, 0.50, 0.56) m, at rest
- flap1: hinge joint flap1_hinge about axis (0.00, 1.00, 0.00), range -90.0002° to -30° as MuJoCo applies it; its geoms: flap1, flap1 striker; starts at -90.0°, still
- pendulum2: hinge joint pendulum2_hinge about axis (0.00, 1.00, 0.00), range -82.9998° to -45° as MuJoCo applies it; its geoms: pendulum2, pendulum2 rod; starts at -45.0°, still
- ball4: free body; its geoms: ball4; starts at (0.47, 0.50, 0.90) m, at rest
- seesaw1: hinge joint seesaw1_hinge about axis (0.00, 1.00, 0.00), range -42° to 0° as MuJoCo applies it; its geoms: seesaw1; starts at 0.0°, still
- ball5: free body; its geoms: ball5; starts at (1.50, 0.50, 0.35) m, at rest

What happened, in order:
 0.00 s  seesaw1 starts touching ball5
 0.00 s  cart2 starts touching cart2 left guide
 0.00 s  ball3 starts touching ramp2_deck
 0.00 s  cart2 starts touching cart2 right guide
 0.00 s  cart1 starts touching cart1 right track
 0.00 s  cart2 starts touching cart2 track
 0.00 s  ball3 starts touching ball3 starting ledge
 0.00 s  ball1 starts touching ramp1_deck
 0.00 s  domino1 starts touching floor
 0.00 s  cart1 starts touching cart1 left track
 0.00 s  domino2 starts touching domino2 pedestal
 0.00 s  domino2 starts touching cart2 track
 0.00 s  block1 starts touching floor
 0.00 s  ball1 starts touching ball1 starting ledge
 0.00 s  cart1 spring pusher starts at its 0° stop (the end where it sits higher)
 0.00 s  pendulum1 starts at its 0° stop (the end where it sits lower)
 0.00 s  pendulum1 is at its largest at the start, 0.0°
 0.00 s  door1 starts at its -90.0002° stop (the end where it sits higher)
 0.00 s  lever1 starts at its 0° stop (neither end sits lower)
 0.00 s  flap1 starts at its -90.0002° stop (the end where it sits higher)
 0.00 s  pendulum2 starts at its -45° stop (the end where it sits lower)
 0.00 s  seesaw1 starts at its 0° stop (neither end sits lower)
 0.00 s  block1 leaves floor
 0.00 s  flap1 first touches floor
 0.00 s  flap1 leaves floor
 0.00 s  door1 first touches block1
 0.00 s  door1 first touches floor
 0.00 s  door1 leaves floor
 0.00 s  cart1 spring pusher reaches its 0° stop (the end where it sits higher) again moving +197°/s
 0.00 s  cart1 spring pusher reaches its 0° stop (the end where it sits higher) again moving +197°/s
 0.00 s  cart1 spring pusher reaches its 0° stop (the end where it sits higher) again moving +197°/s
 0.00 s  cart1 spring pusher reaches its lower stop 354 more times
 0.00 s  door1 is at its largest, -0.2°
 0.00 s  block1 starts moving
 0.00 s  lever1 is at its smallest, -0.0°
 0.00 s  cart2 comes to rest at (-1.75, 0.50, 0.40) m
 0.00 s  flap1 is at its largest, -0.3°
 0.00 s  pendulum2 is at its largest, -0.4°
 0.00 s  pendulum2 passes 0.19 m from ramp2 (ramp2_deck) without touching it: nearest points (-0.17, 0.50, 0.41) m and (-0.23, 0.50, 0.23) m
 0.00 s  flap1 passes 0.33 m from ring2 (ring2_07) without touching it: nearest points (0.43, 0.50, 0.47) m and (0.74, 0.50, 0.60) m
 0.00 s  flap1 passes 0.45 m from seesaw1 without touching it: nearest points (0.43, 0.50, 0.26) m and (0.88, 0.50, 0.26) m
 0.00 s  cart1 first touches cart1 spring pusher
 0.00 s  ball4 first touches shelf1
 0.00 s  lever1 first touches ball2
 0.01 s  cart2 leaves cart2 left guide
 0.01 s  cart1 first touches cart1 left guide
 0.01 s  cart1 first touches cart1 right guide
 0.01 s  cart1 starts moving
 0.01 s  cart1 is still moving at the end, 0.06 m/s
 0.01 s  block1 is still moving at the end, 3.06 m/s
 0.01 s  door1 passes 0.29 m from domino1 without touching it: nearest points (-3.11, 0.00, 0.02) m and (-2.82, 0.00, 0.02) m
 0.02 s  cart2 starts moving
 0.02 s  cart2 first touches transfer chute
 0.03 s  cart1 spring pusher is at its smallest, -3.6°
 0.03 s  lever1 passes 0.40 m from cart2 without touching it: nearest points (-2.00, 0.05, 0.98) m and (-1.76, 0.11, 0.67) m
 0.03 s  flap1 passes 0.29 m from shelf1 without touching it: nearest points (0.30, 0.50, 0.55) m and (0.44, 0.50, 0.81) m
 0.03 s  flap1 passes 0.33 m from ball4 without touching it: nearest points (0.30, 0.50, 0.55) m and (0.44, 0.50, 0.85) m
 0.03 s  cart2 passes 0.26 m from ring1 (ring1_15) without touching it: nearest points (-1.75, 0.02, 0.66) m and (-2.00, 0.00, 0.75) m
 0.03 s  ball2 passes 0.43 m from cart2 without touching it: nearest points (-1.98, 0.00, 1.04) m and (-1.63, -0.02, 0.80) m
 0.04 s  lever1 is at its largest, 0.0°
 0.05 s  seesaw1 is at its largest, 0.0°
 0.05 s  flap1 striker first touches pendulum2
 0.06 s  cart1 spring pusher is at its largest, 2.8°
 0.06 s  door1 is at its smallest, -90.0°
 0.06 s  flap1 is at its smallest, -90.0°

State every 0.25 s:
0.00 s: ball1 at (-4.98, 0.00, 0.56) m, at rest; touching ball1 starting ledge, ramp1_deck | cart1 at (-5.64, 0.00, 0.56) m, at rest; touching cart1 left track, cart1 right track | cart1 spring pusher at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at -90.0°, still; touching nothing | block1 at (-3.20, 0.00, 0.06) m, at rest; touching floor | domino1 at (-2.78, 0.00, 0.12) m, at rest; touching floor | lever1 at 0.0°, still; touching nothing | ball2 at (-2.03, 0.00, 1.07) m, at rest; touching nothing | cart2 at (-1.75, 0.50, 0.40) m, at rest; touching cart2 left guide, cart2 right guide, cart2 track | domino2 at (-1.20, 0.50, 0.47) m, at rest; touching cart2 track, domino2 pedestal | ball3 at (-0.99, 0.50, 0.56) m, at rest; touching ball3 starting ledge, ramp2_deck | flap1 at -90.0°, still; touching nothing | pendulum2 at -45.0°, still; touching nothing | ball4 at (0.47, 0.50, 0.90) m, at rest; touching nothing | seesaw1 at 0.0°, still; touching ball5 | ball5 at (1.50, 0.50, 0.35) m, at rest; touching seesaw1

At the end (0.01 s):
- ball1 at (-4.98, 0.00, 0.56) m, at rest; touching ball1 starting ledge, ramp1_deck
- cart1 at (-5.64, 0.00, 0.56) m, moving 0.06 m/s (vx +0.06, vy -0.00, vz -0.01); touching cart1 left guide, cart1 left track, cart1 right guide, cart1 right track, cart1 spring pusher
- cart1 spring pusher at 0.5°, turning +17°/s; touching cart1
- pendulum1 at 0.0°, still; touching nothing
- door1 at -1.4°, turning -261°/s; touching block1
- block1 at (-3.20, 0.00, 0.07) m, moving 3.06 m/s (vx -0.23, vy -0.00, vz +3.06); touching door1
- domino1 at (-2.78, 0.00, 0.12) m, at rest; touching floor
- lever1 at 0.0°, turning +2°/s; touching ball2
- ball2 at (-2.03, 0.00, 1.07) m, at rest; touching lever1
- cart2 at (-1.75, 0.50, 0.40) m, at rest; touching cart2 right guide, cart2 track
- domino2 at (-1.20, 0.50, 0.47) m, at rest; touching cart2 track, domino2 pedestal
- ball3 at (-0.99, 0.50, 0.56) m, at rest; touching ball3 starting ledge, ramp2_deck
- flap1 at -2.4°, turning -428°/s; touching nothing
- pendulum2 at -3.6°, turning -646°/s; touching nothing
- ball4 at (0.47, 0.50, 0.90) m, at rest; touching shelf1
- seesaw1 at 0.0°, turning +2°/s; touching ball5
- ball5 at (1.50, 0.50, 0.35) m, at rest; touching seesaw1

Openings (fixed rings, open through the middle; height is the middle of the whole thing), and each loose thing that comes down through one's height:
ring1: an opening 0.21 m across, centre (-2.10, 0.00, 0.75) m
- cart2 comes down through ring1's height at 0.06 s, 1.04 m from its centre: outside it, missing by 0.93 m (down through that height 357 times; this is the closest)
ring2: an opening 0.21 m across, centre (0.84, 0.50, 0.60) m
- cart2 comes down through ring2's height at 0.06 s, 2.30 m from its centre: outside it, missing by 2.20 m (down through that height 357 times; this is the closest)
</history>
