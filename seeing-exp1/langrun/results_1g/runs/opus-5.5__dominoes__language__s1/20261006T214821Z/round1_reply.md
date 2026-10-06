**What happened:** Nothing moved. All ten dominoes stood upright at their starting places for the full 6 s, and domino1 was at rest from the start. The `first one spins` line never set domino1 turning, so no domino ever touched another.

**Fix:** Drop the spin. Add a small launched ball that hits domino1 near its top and tips it toward the row.

**Check of the ball's path:** It starts 15 cm behind domino1 at 8 cm up, moving 1.5 m/s along and 0.5 m/s up. It crosses the 12.5 cm gap in about 0.08 s and arrives at roughly 9 cm up, close to domino1's top. That should push domino1 over.

```world
world  domino row

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

domino
  is a              box 1 by 5 by 10 cm, 30 g
  friction          0.5, spinning 0.005, rolling 0.002
  colour            wood
  moves             freely
  repeated          10 times, 6 cm apart along
  stands            on floor, 1 m along

pusher
  is a      sphere 2 cm radius, 30 g
  colour    orange
  moves     freely
  at        85 cm along, 8 cm up
  launched  1.5 m/s along, 0.5 m/s up

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
{"what_happens": "All ten dominoes stand upright and motionless for the whole 6 s; domino1 never received any spin, so it never tipped and no domino touched another.", "works": false, "problem": "The 'first one spins' line did not give domino1 any starting motion, so nothing set the row falling."}
```

---
thinking (summarized):

It's odd that domino1 shows zero velocity at the start despite the spin instruction — maybe that spin value never got applied, possibly due to parsing or ordering issues with the key.

Instead of fighting the spin mechanism, I'm considering adding a separate launched ball as a "pusher" to strike domino1 directly. I'm calculating a trajectory for a small sphere launched from behind and slightly below domino1's top, accounting for gravity drop, so it arrives with enough momentum near the top of the domino to tip it over — then working out how to position that ball relative to domino1 in the setup.

