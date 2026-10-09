Before the run, at the start:
- lever1 already touches lever1 follower at the start, so their touch is not something that happens in the run
- ball5 already touches seesaw1 at the start, so their touch is not something that happens in the run

MuJoCo ran your scene for 20 s from its start. Here is what happened, written out from MuJoCo's state by a
program that watched the run. It reports what MuJoCo did, using the names in the file; it does not know the brief.
Angles and ranges are in degrees, read back from MuJoCo as it applied them.

<history>
The run lasted 20.00 s. Positions are of each body's origin in metres; z is up and the floor's top is z = 0.

Things that can move:
- ball1: free body; its geoms: ball1; starts at (0.02, 0.00, 0.56) m, at rest
- cart1: slide joint cart1_axial_slide about axis (0.00, 0.00, 1.00), range -0.62 m to 0.2 m as MuJoCo applies it; its geoms: cart1, cart1 pushing face; starts at 0.200 m, still
- pendulum1: hinge joint pendulum1_pendulum_hinge about axis (0.00, 1.00, 0.00), range -40° to 0° as MuJoCo applies it; its geoms: pendulum1_bob, pendulum1_rod; starts at 0.0°, still
- door1: hinge joint door1_hinge about axis (0.00, 1.00, 0.00), range -90.0002° to -20° as MuJoCo applies it; its geoms: door1; starts at -90.0°, still
- block1: free body; its geoms: block1; starts at (1.84, 0.00, 0.06) m, at rest
- domino1: free body; its geoms: domino1; starts at (2.26, 0.00, 0.12) m, at rest
- lever1: hinge joint lever1_hinge about axis (0.00, 1.00, 0.00), range -73° to -28° as MuJoCo applies it; its geoms: lever1; starts at -28.0°, still
- lever1 follower: slide joint lever1_follower_slide about axis (0.00, 0.00, 1.00), range -0.01 m to 0.3 m as MuJoCo applies it; its geoms: lever1 follower, lever1 follower stem, lever1 follower.lever1 ball seat; starts at 0.000 m, still
- ball2: free body; its geoms: ball2; starts at (2.97, 0.00, 1.21) m, at rest
- cart2: slide joint cart2_slide about axis (1.00, 0.00, 0.00), range 0 m to 0.44 m as MuJoCo applies it; its geoms: cart2; starts at 0.000 m, still
- domino2: free body; its geoms: domino2; starts at (3.66, 0.00, 0.62) m, at rest
- ball3: free body; its geoms: ball3; starts at (3.84, 0.00, 0.56) m, at rest
- flap1: hinge joint flap1_hinge about axis (0.00, 1.00, 0.00), range 30° to 90.0002° as MuJoCo applies it; its geoms: flap1, flap1 striker; starts at 90.0°, still
- pendulum2: hinge joint pendulum2_pendulum_hinge about axis (0.00, 1.00, 0.00), range -188° to -150° as MuJoCo applies it; its geoms: pendulum2_bob, pendulum2_rod; starts at -150.0°, still
- ball4: free body; its geoms: ball4; starts at (4.91, 0.14, 0.90) m, at rest
- seesaw1: hinge joint seesaw1_hinge about axis (0.00, 1.00, 0.00), range -42° to 0° as MuJoCo applies it; its geoms: seesaw1, seesaw1 ball seat, seesaw1 scoop back, seesaw1 scoop far lip; starts at 0.0°, still
- ball5: free body; its geoms: ball5; starts at (5.50, 0.14, 0.36) m, at rest

What happened, in order:
 0.00 s  domino1 starts touching floor
 0.00 s  block1 starts touching floor
 0.00 s  seesaw1 ball seat starts touching ball5
 0.00 s  lever1 starts touching lever1 follower
 0.00 s  seesaw1 scoop back starts touching ball5
 0.00 s  cart1 starts at its upper stop (0.2 m)
 0.00 s  cart1 is at its largest at the start, 0.2 m
 0.00 s  pendulum1 starts at its 0° stop (the end where it sits lower)
 0.00 s  pendulum1 is at its largest at the start, 0.0°
 0.00 s  door1 starts at its -90.0002° stop (the end where it sits higher)
 0.00 s  door1 is at its largest at the start, -90.0°
 0.00 s  lever1 starts at its -28° stop (neither end sits lower)
 0.00 s  cart2 starts at its lower stop (0 m)
 0.00 s  cart2 is at its largest at the start, 0.0 m
 0.00 s  flap1 starts at its 90.0002° stop (the end where it sits lower)
 0.00 s  flap1 is at its largest at the start, 90.0°
 0.00 s  pendulum2 starts at its -150° stop (the end where it sits lower)
 0.00 s  seesaw1 starts at its 0° stop (neither end sits lower)
 0.00 s  seesaw1 scoop back leaves ball5
 0.00 s  domino2 first touches domino2 platform
 0.00 s  ball1 first touches ball1 launch pad
 0.00 s  ball3 first touches ball3 launch pad
 0.00 s  ball4 first touches shelf1
 0.00 s  lever1 follower.lever1 ball seat first touches ball2
 0.01 s  ball2 starts moving
 0.02 s  ball2 comes to rest at (2.97, 0.00, 1.21) m
 0.03 s  lever1 follower is at its largest, 0.0 m
 0.05 s  seesaw1 is at its largest, 0.0°
 0.05 s  pendulum2 is at its largest, -150.0°
 0.09 s  lever1 is at its largest, -28.0°
 0.27 s  cart1 pushing face first touches ball1 launch pad
 0.27 s  door1 is at its smallest, -90.0°
 0.27 s  ball1 passes 0.00 m from cart1 (cart1 pushing face) without touching it: nearest points (-0.03, 0.00, 0.57) m and (-0.03, 0.00, 0.57) m
 0.27 s  cart1 passes 0.05 m from ramp1 without touching it: nearest points (-0.04, 0.09, 0.50) m and (0.01, 0.09, 0.49) m
 0.27 s  cart1 is at its smallest, -0.3 m
 0.29 s  cart1 pushing face leaves ball1 launch pad
 0.52 s  flap1 is at its smallest, 90.0°
 0.79 s  cart1 pushing face touches ball1 launch pad again
 0.81 s  cart1 pushing face leaves ball1 launch pad
 1.18 s  cart1 pushing face touches ball1 launch pad again
 1.21 s  cart1 pushing face leaves ball1 launch pad
 1.29 s  cart1 pushing face touches ball1 launch pad again
 1.54 s  seesaw1 scoop far lip first touches ball5
 1.56 s  seesaw1 scoop far lip leaves ball5
 2.20 s  seesaw1 scoop far lip touches ball5 again
 2.22 s  seesaw1 scoop far lip leaves ball5
 2.36 s  seesaw1 scoop far lip touches ball5 again

State every 0.25 s:
0.00 s: ball1 at (0.02, 0.00, 0.56) m, at rest; touching nothing | cart1 at 0.200 m, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at -90.0°, still; touching nothing | block1 at (1.84, 0.00, 0.06) m, at rest; touching floor | domino1 at (2.26, 0.00, 0.12) m, at rest; touching floor | lever1 at -28.0°, still; touching lever1 follower | lever1 follower at 0.000 m, still; touching lever1 | ball2 at (2.97, 0.00, 1.21) m, at rest; touching nothing | cart2 at 0.000 m, still; touching nothing | domino2 at (3.66, 0.00, 0.62) m, at rest; touching nothing | ball3 at (3.84, 0.00, 0.56) m, at rest; touching nothing | flap1 at 90.0°, still; touching nothing | pendulum2 at -150.0°, still; touching nothing | ball4 at (4.91, 0.14, 0.90) m, at rest; touching nothing | seesaw1 at 0.0°, still; touching ball5 | ball5 at (5.50, 0.14, 0.36) m, at rest; touching seesaw1 ball seat, seesaw1 scoop back
0.25 s: ball1 at (0.02, 0.00, 0.56) m, at rest; touching ball1 launch pad | cart1 at -0.228 m, moving -2.69 m/s; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at -90.0°, still; touching nothing | block1 at (1.84, 0.00, 0.06) m, at rest; touching floor | domino1 at (2.26, 0.00, 0.12) m, at rest; touching floor | lever1 at -28.0°, still; touching lever1 follower | lever1 follower at 0.001 m, still; touching ball2, lever1 | ball2 at (2.97, 0.00, 1.21) m, at rest; touching lever1 follower.lever1 ball seat | cart2 at 0.000 m, still; touching nothing | domino2 at (3.66, 0.00, 0.62) m, at rest; touching domino2 platform | ball3 at (3.84, 0.00, 0.56) m, at rest; touching ball3 launch pad | flap1 at 90.0°, still; touching nothing | pendulum2 at -150.0°, still; touching nothing | ball4 at (4.91, 0.14, 0.90) m, at rest; touching shelf1 | seesaw1 at 0.0°, still; touching ball5 | ball5 at (5.50, 0.14, 0.36) m, at rest; touching seesaw1 ball seat
0.50 s: ball1 at (0.02, 0.00, 0.56) m, at rest; touching ball1 launch pad | cart1 at -0.194 m, moving +0.10 m/s; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at -90.0°, still; touching nothing | block1 at (1.84, 0.00, 0.06) m, at rest; touching floor | domino1 at (2.26, 0.00, 0.12) m, at rest; touching floor | lever1 at -28.0°, still; touching lever1 follower | lever1 follower at 0.001 m, still; touching ball2, lever1 | ball2 at (2.97, 0.00, 1.21) m, at rest; touching lever1 follower.lever1 ball seat | cart2 at 0.000 m, still; touching nothing | domino2 at (3.66, 0.00, 0.62) m, at rest; touching domino2 platform | ball3 at (3.84, 0.00, 0.56) m, at rest; touching ball3 launch pad | flap1 at 90.0°, still; touching nothing | pendulum2 at -150.0°, still; touching nothing | ball4 at (4.91, 0.14, 0.90) m, at rest; touching shelf1 | seesaw1 at 0.0°, still; touching ball5 | ball5 at (5.50, 0.14, 0.36) m, at rest; touching seesaw1 ball seat
0.75 s: ball1 at (0.02, 0.00, 0.56) m, at rest; touching ball1 launch pad | cart1 at -0.250 m, moving -0.45 m/s; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at -90.0°, still; touching nothing | block1 at (1.84, 0.00, 0.06) m, at rest; touching floor | domino1 at (2.26, 0.00, 0.12) m, at rest; touching floor | lever1 at -28.0°, still; touching lever1 follower | lever1 follower at 0.001 m, still; touching ball2, lever1 | ball2 at (2.97, 0.00, 1.21) m, at rest; touching lever1 follower.lever1 ball seat | cart2 at 0.000 m, still; touching nothing | domino2 at (3.66, 0.00, 0.62) m, at rest; touching domino2 platform | ball3 at (3.84, 0.00, 0.56) m, at rest; touching ball3 launch pad | flap1 at 90.0°, still; touching nothing | pendulum2 at -150.0°, still; touching nothing | ball4 at (4.91, 0.14, 0.90) m, at rest; touching shelf1 | seesaw1 at 0.0°, still; touching ball5 | ball5 at (5.51, 0.14, 0.36) m, at rest; touching seesaw1 ball seat
1.00 s: ball1 at (0.02, 0.00, 0.56) m, at rest; touching ball1 launch pad | cart1 at -0.261 m, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at -90.0°, still; touching nothing | block1 at (1.84, 0.00, 0.06) m, at rest; touching floor | domino1 at (2.26, 0.00, 0.12) m, at rest; touching floor | lever1 at -28.0°, still; touching lever1 follower | lever1 follower at 0.001 m, still; touching ball2, lever1 | ball2 at (2.97, 0.00, 1.21) m, at rest; touching lever1 follower.lever1 ball seat | cart2 at 0.000 m, still; touching nothing | domino2 at (3.66, 0.00, 0.62) m, at rest; touching domino2 platform | ball3 at (3.84, 0.00, 0.56) m, at rest; touching ball3 launch pad | flap1 at 90.0°, still; touching nothing | pendulum2 at -150.0°, still; touching nothing | ball4 at (4.91, 0.14, 0.90) m, at rest; touching shelf1 | seesaw1 at 0.0°, still; touching ball5 | ball5 at (5.51, 0.14, 0.36) m, at rest; touching seesaw1 ball seat
1.25 s: ball1 at (0.02, 0.00, 0.56) m, at rest; touching ball1 launch pad | cart1 at -0.268 m, still; touching nothing | pendulum1 at 0.0°, still; touching nothing | door1 at -90.0°, still; touching nothing | block1 at (1.84, 0.00, 0.06) m, at rest; touching floor | domino1 at (2.26, 0.00, 0.12) m, at rest; touching floor | lever1 at -28.0°, still; touching lever1 follower | lever1 follower at 0.001 m, still; touching ball2, lever1 | ball2 at (2.97, 0.00, 1.21) m, at rest; touching lever1 follower.lever1 ball seat | cart2 at 0.000 m, still; touching nothing | domino2 at (3.66, 0.00, 0.62) m, at rest; touching domino2 platform | ball3 at (3.84, 0.00, 0.56) m, at rest; touching ball3 launch pad | flap1 at 90.0°, still; touching nothing | pendulum2 at -150.0°, still; touching nothing | ball4 at (4.91, 0.14, 0.90) m, at rest; touching shelf1 | seesaw1 at 0.0°, still; touching ball5 | ball5 at (5.51, 0.14, 0.36) m, at rest; touching seesaw1 ball seat
1.50 s: ball1 at (0.02, 0.00, 0.56) m, at rest; touching ball1 launch pad | cart1 at -0.268 m, still; touching ball1 launch pad | pendulum1 at 0.0°, still; touching nothing | door1 at -90.0°, still; touching nothing | block1 at (1.84, 0.00, 0.06) m, at rest; touching floor | domino1 at (2.26, 0.00, 0.12) m, at rest; touching floor | lever1 at -28.0°, still; touching lever1 follower | lever1 follower at 0.001 m, still; touching ball2, lever1 | ball2 at (2.97, 0.00, 1.21) m, at rest; touching lever1 follower.lever1 ball seat | cart2 at 0.000 m, still; touching nothing | domino2 at (3.66, 0.00, 0.62) m, at rest; touching domino2 platform | ball3 at (3.84, 0.00, 0.56) m, at rest; touching ball3 launch pad | flap1 at 90.0°, still; touching nothing | pendulum2 at -150.0°, still; touching nothing | ball4 at (4.91, 0.14, 0.90) m, at rest; touching shelf1 | seesaw1 at 0.0°, still; touching ball5 | ball5 at (5.51, 0.14, 0.36) m, at rest; touching seesaw1 ball seat
(the same through 2.25 s)
2.50 s: ball1 at (0.02, 0.00, 0.56) m, at rest; touching ball1 launch pad | cart1 at -0.268 m, still; touching ball1 launch pad | pendulum1 at 0.0°, still; touching nothing | door1 at -90.0°, still; touching nothing | block1 at (1.84, 0.00, 0.06) m, at rest; touching floor | domino1 at (2.26, 0.00, 0.12) m, at rest; touching floor | lever1 at -28.0°, still; touching lever1 follower | lever1 follower at 0.001 m, still; touching ball2, lever1 | ball2 at (2.97, 0.00, 1.21) m, at rest; touching lever1 follower.lever1 ball seat | cart2 at 0.000 m, still; touching nothing | domino2 at (3.66, 0.00, 0.62) m, at rest; touching domino2 platform | ball3 at (3.84, 0.00, 0.56) m, at rest; touching ball3 launch pad | flap1 at 90.0°, still; touching nothing | pendulum2 at -150.0°, still; touching nothing | ball4 at (4.91, 0.14, 0.90) m, at rest; touching shelf1 | seesaw1 at 0.0°, still; touching ball5 | ball5 at (5.51, 0.14, 0.36) m, at rest; touching seesaw1 ball seat, seesaw1 scoop far lip
(the same through 20.00 s)

At the end (20.00 s):
- ball1 at (0.02, 0.00, 0.56) m, at rest; touching ball1 launch pad
- cart1 at -0.268 m, still; touching ball1 launch pad
- pendulum1 at 0.0°, still; touching nothing
- door1 at -90.0°, still; touching nothing
- block1 at (1.84, 0.00, 0.06) m, at rest; touching floor
- domino1 at (2.26, 0.00, 0.12) m, at rest; touching floor
- lever1 at -28.0°, still; touching lever1 follower
- lever1 follower at 0.001 m, still; touching ball2, lever1
- ball2 at (2.97, 0.00, 1.21) m, at rest; touching lever1 follower.lever1 ball seat
- cart2 at 0.000 m, still; touching nothing
- domino2 at (3.66, 0.00, 0.62) m, at rest; touching domino2 platform
- ball3 at (3.84, 0.00, 0.56) m, at rest; touching ball3 launch pad
- flap1 at 90.0°, still; touching nothing
- pendulum2 at -150.0°, still; touching nothing
- ball4 at (4.91, 0.14, 0.90) m, at rest; touching shelf1
- seesaw1 at 0.0°, still; touching ball5
- ball5 at (5.51, 0.14, 0.36) m, at rest; touching seesaw1 ball seat, seesaw1 scoop far lip

Openings (fixed rings, open through the middle; height is the middle of the whole thing), and each loose thing that comes down through one's height:
ring1: an opening 0.21 m across, centre (2.97, 0.00, 0.89) m
- nothing loose comes down through ring1's height
ring2: an opening 0.21 m across, centre (4.88, 0.14, 0.60) m
- nothing loose comes down through ring2's height
</history>
