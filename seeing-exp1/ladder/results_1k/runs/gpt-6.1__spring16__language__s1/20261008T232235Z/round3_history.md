Before the run, at the start:
- ball5 already touches seesaw1 at the start, so their touch is not something that happens in the run

MuJoCo ran your scene for 20 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 0.11 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (-4.98, 0.00, 0.56) m, at rest
- cart1: free body; its geoms: cart1; starts at (-5.64, 0.00, 0.56) m, at rest
- cart1 spring pusher: hinge joint cart1_spring_hinge about axis (0.00, 1.00, 0.00), range 0° to 22.9183° as MuJoCo applies it; its geoms: cart1 spring pusher; starts at 0.0°, still
- pendulum1: hinge joint pendulum1_hinge about axis (0.00, 1.00, 0.00), range -40° to 0° as MuJoCo applies it; its geoms: pendulum1, pendulum1 rod; starts at 0.0°, still
- door1: hinge joint door1_hinge about axis (0.00, 1.00, 0.00), range 0° to 70° as MuJoCo applies it; its geoms: door1; starts at 0.0°, still
- block1: free body; its geoms: block1; starts at (-3.19, 0.20, 0.06) m, at rest
- domino1: free body; its geoms: domino1; starts at (-2.79, 0.20, 0.12) m, at rest
- lever1: hinge joint lever1_hinge about axis (0.00, 1.00, 0.00), range -45° to 0° as MuJoCo applies it; its geoms: lever1, lever1 trigger crossbar, lever1 striker; starts at 0.0°, still
- ball2: free body; its geoms: ball2; starts at (-2.03, 0.00, 1.07) m, at rest
- cart2: free body; its geoms: cart2, cart2 receiver, cart2 front bumper; starts at (-2.05, 0.00, 0.35) m, at rest
- domino2: free body; its geoms: domino2; starts at (-1.50, 0.00, 0.47) m, at rest
- ball3: free body; its geoms: ball3; starts at (-1.32, 0.00, 0.56) m, at rest
- flap1: hinge joint flap1_hinge about axis (0.00, 1.00, 0.00), range 0° to 60.0001° as MuJoCo applies it; its geoms: flap1, flap1 striker; starts at 0.0°, still
- pendulum2: hinge joint pendulum2_hinge about axis (0.00, 1.00, 0.00), range -38° to 0° as MuJoCo applies it; its geoms: pendulum2, pendulum2 rod; starts at 0.0°, still
- ball4: free body; its geoms: ball4; starts at (0.12, 0.00, 0.90) m, at rest
- seesaw1: hinge joint seesaw1_hinge about axis (0.00, 1.00, 0.00), range -42° to 0° as MuJoCo applies it; its geoms: seesaw1; starts at 0.0°, still
- ball5: free body; its geoms: ball5; starts at (1.10, 0.00, 0.35) m, at rest

What happened, in order:
 0.00 s  seesaw1 starts touching ball5
 0.00 s  ball3 starts touching ramp2_deck
 0.00 s  cart1 starts touching cart1 right track
 0.00 s  domino2 starts touching domino2 pedestal
 0.00 s  ball3 starts touching ball3 starting ledge
 0.00 s  ball1 starts touching ramp1_deck
 0.00 s  cart2 starts touching cart2 track
 0.00 s  cart1 starts touching cart1 left track
 0.00 s  block1 starts touching floor
 0.00 s  ball1 starts touching ball1 starting ledge
 0.00 s  domino1 starts touching floor
 0.00 s  cart1 spring pusher starts at its 0° stop (the end where it sits higher)
 0.00 s  pendulum1 starts at its 0° stop (the end where it sits lower)
 0.00 s  pendulum1 is at its largest at the start, 0.0°
 0.00 s  door1 starts at its 0° stop (the end where it sits higher)
 0.00 s  door1 is at its largest at the start, 0.0°
 0.00 s  lever1 starts at its 0° stop (the end where it sits higher)
 0.00 s  flap1 starts at its 0° stop (the end where it sits higher)
 0.00 s  flap1 is at its largest at the start, 0.0°
 0.00 s  pendulum2 starts at its 0° stop (the end where it sits lower)
 0.00 s  seesaw1 starts at its 0° stop (neither end sits lower)
 0.00 s  cart1 spring pusher reaches its 0° stop (the end where it sits higher) again moving +169°/s
 0.00 s  cart1 spring pusher reaches its 0° stop (the end where it sits higher) again moving +169°/s
 0.00 s  cart1 spring pusher reaches its 0° stop (the end where it sits higher) again moving +169°/s
 0.00 s  cart1 spring pusher reaches its lower stop 85 more times
 0.00 s  lever1 is at its smallest, -0.0°
 0.00 s  cart2 comes to rest at (-2.05, 0.00, 0.35) m
 0.00 s  ball4 first touches shelf1
 0.00 s  lever1 first touches ball2
 0.01 s  cart1 first touches cart1 spring pusher
 0.01 s  cart1 starts moving
 0.02 s  ball3 leaves ramp2_deck
 0.02 s  ball1 leaves ramp1_deck
 0.06 s  seesaw1 is at its largest, 0.0°
 0.06 s  pendulum2 is at its largest, 0.0°
 0.08 s  lever1 is at its largest, 0.0°
 0.11 s  cart1 leaves cart1 left track
 0.11 s  cart1 leaves cart1 left track
 0.11 s  cart1 leaves cart1 left track
 0.11 s  cart1 leaves cart1 left track
 0.11 s  cart1 leaves cart1 spring pusher
 0.11 s  cart1 is still moving at the end, 0.72 m/s
 0.15 s  cart2 starts moving
 0.15 s  cart2 first touches cart2 left guide
 0.16 s  cart2 receiver first touches cart2 right guide
 0.16 s  cart2 first touches cart2 right guide
 0.18 s  cart1 touches cart1 left track again
 0.18 s  cart1 touches cart1 left track again
 0.18 s  cart1 touches cart1 left track again
 0.18 s  cart1 touches cart1 left track 85 more times between 0.18 s and 0.11 s
 0.20 s  ball1 passes 0.39 m from cart1 without touching it: nearest points (-5.03, 0.00, 0.56) m and (-5.41, 0.00, 0.56) m
 0.20 s  cart1 passes 0.38 m from ramp1 (ramp1_leg) without touching it: nearest points (-5.41, 0.03, 0.51) m and (-5.03, 0.03, 0.49) m
 0.20 s  cart1 passes 0.38 m from ball1 starting ledge without touching it: nearest points (-5.41, 0.05, 0.51) m and (-5.03, 0.05, 0.51) m
 0.20 s  cart2 touches cart2 right guide again
 0.20 s  cart2 touches cart2 right guide again
 0.20 s  cart2 touches cart2 right guide again
 0.20 s  cart2 touches cart2 right guide 85 more times between 0.20 s and 0.23 s, still touching at the end
 0.21 s  cart1 first touches cart1 left guide
 0.21 s  cart1 first touches cart1 right guide
 0.22 s  cart2 receiver first touches cart2 left guide
 0.23 s  cart1 spring pusher is at its largest, 16.8°
 0.23 s  flap1 is at its smallest, -0.0°

State every 0.25 s:
0.00 s: ball1 at (-4.98, 0.00, 0.56) m, at rest; touching ball1 starting ledge, ramp1_deck | cart1 at (-5.64, 0.00, 0.56) m, at rest; touching cart1 left track, cart1 right track | cart1 spring pusher at 0.0°, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at 0.0°, still; touching nothing | block1 at (-3.19, 0.20, 0.06) m, at rest; touching floor | domino1 at (-2.79, 0.20, 0.12) m, at rest; touching floor | lever1 at 0.0°, still; touching nothing | ball2 at (-2.03, 0.00, 1.07) m, at rest; touching nothing | cart2 at (-2.05, 0.00, 0.35) m, at rest; touching cart2 track | domino2 at (-1.50, 0.00, 0.47) m, at rest; touching domino2 pedestal | ball3 at (-1.32, 0.00, 0.56) m, at rest; touching ball3 starting ledge, ramp2_deck | flap1 at 0.0°, still; touching nothing | pendulum2 at 0.0°, still; touching nothing | ball4 at (0.12, 0.00, 0.90) m, at rest; touching nothing | seesaw1 at 0.0°, still; touching ball5 | ball5 at (1.10, 0.00, 0.35) m, at rest; touching seesaw1

At the end (0.11 s):
- ball1 at (-4.98, 0.00, 0.56) m, at rest; touching ball1 starting ledge
- cart1 at (-5.60, 0.00, 0.56) m, moving 0.72 m/s (vx +0.64, vy +0.00, vz +0.32), turned 4° from how it started; touching cart1 right track
- cart1 spring pusher at 4.4°, turning +72°/s; touching nothing
- pendulum1 at 0.0°, still; touching nothing
- door1 at 0.0°, still; touching nothing
- block1 at (-3.19, 0.20, 0.06) m, at rest; touching floor
- domino1 at (-2.79, 0.20, 0.12) m, at rest; touching floor
- lever1 at 0.0°, still; touching ball2
- ball2 at (-2.03, 0.00, 1.07) m, at rest; touching lever1
- cart2 at (-2.05, 0.00, 0.35) m, at rest; touching cart2 track
- domino2 at (-1.50, 0.00, 0.47) m, at rest; touching domino2 pedestal
- ball3 at (-1.32, 0.00, 0.56) m, at rest; touching ball3 starting ledge
- flap1 at -0.0°, still; touching nothing
- pendulum2 at 0.0°, still; touching nothing
- ball4 at (0.12, 0.00, 0.90) m, at rest; touching shelf1
- seesaw1 at 0.0°, still; touching ball5
- ball5 at (1.10, 0.00, 0.35) m, at rest; touching seesaw1

Openings (fixed rings, open through the middle; height is the middle of the whole thing), and each loose thing that comes down through one's height:
ring1: an opening 0.16 m across, centre (-2.10, 0.00, 0.75) m
- cart1 comes down through ring1's height at 0.23 s, 3.41 m from its centre: outside it, missing by 3.33 m (down through that height 88 times; this is the closest)
ring2: an opening 0.16 m across, centre (0.44, 0.00, 0.60) m
- cart1 comes down through ring2's height at 0.23 s, 5.95 m from its centre: outside it, missing by 5.87 m (down through that height 88 times; this is the closest)
</history>
