In the run, nothing falls. domino1 rocks to about 7° and settles back upright by 0.66 s. The other nine never move, so no dominoes touch. A 5 rad/s spin about the domino's own centre doesn't reliably carry it past its tipping point. The fix is a small ball launched into domino1's upper half, which should tip it with plenty of margin. I've also added a check that the ball hits domino1.

```world
world  ten dominoes

floor
  size      4 m
  friction  0.7, spinning 0.005, rolling 0.002

domino
  is a              box 1 by 4 by 8 cm, 20 g
  colour            wood
  friction          0.5, spinning 0.005, rolling 0.002
  moves             freely
  repeated          10 times, 5 cm apart along
  first one spins   5 rad/s about y
  stands            on floor, 50 cm along

pusher
  is a      sphere 1 cm radius, 12 g
  colour    orange
  moves     freely
  at        44 cm along, 7.5 cm up
  launched  1.2 m/s along

expect
  pusher touches domino1
  domino1 touches domino2
  domino2 touches domino3
  domino3 touches domino4
  domino4 touches domino5
  domino5 touches domino6
  domino6 touches domino7
  domino7 touches domino8
  domino8 touches domino9
  domino9 touches domino10
```

```json
{"what_happens": "domino1 rocks to about 7 degrees from its starting spin, settles back upright by 0.66 s, and the other nine dominoes never move; no domino touches another.", "works": false, "problem": "The 5 rad/s spin about domino1's own centre is not enough to tip it past its balance point, so the chain never starts."}
```

---
thinking (summarized):

I'm checking if a 7° rock with 5 rad/s spin about the center gives enough energy to tip the domino back up, computing the moment of inertia and kinetic energy against the required height change.

Even though the energy seems theoretically sufficient, I'm worried about contact impulses and floor penetration eating that margin — spinning about the center drives the near bottom edge down into the floor, which bleeds energy and risks bouncing. I'm considering a more robust approach: boosting the spin to 15 rad/s, or instead using a separate launched ball as a pusher to knock domino1 over, sizing and positioning it (radius, mass, launch height and speed) while accounting for gravity drop during flight.

Working through the numbers, I'm iterating on the ball's mass, speed, and starting offset so it arrives at the right height on domino1 to generate enough angular impulse — balancing against the risk of the impact being too violent and causing the domino to jump off its base.

I'll place the ball 6 cm behind domino1, giving a 4.5 cm gap with its radius accounted for, and position it using absolute coordinates (44 cm along, 7.5 cm up) rather than a relative reference, since it's safer than assuming domino1 is referable. The domino spacing of 5 cm for 8 cm tall pieces should work fine with the given friction.

