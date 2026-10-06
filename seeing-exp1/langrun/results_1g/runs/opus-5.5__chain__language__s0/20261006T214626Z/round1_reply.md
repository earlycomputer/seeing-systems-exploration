**What happened:** Ball1 hit ball2 at 0.29 s, and ball2 hit ball3 at 0.92 s. Each knock lost about half the speed, though. Rolling friction also braked the balls hard: a 0.002 rolling coefficient on a 4 cm ball slows it about 0.3 m/s². Ball3 started at only 0.26 m/s and stopped at x = 1.22 m. That is 28 cm short of the cup's lip.

**Changes:**
- Cut rolling friction on the floor and balls tenfold.
- Raised the launch to 3.5 m/s, with matching spin.
- Moved the balls and cup closer together, so ball3 reaches and climbs the 5 mm lip.

```world
world  three ball chain into a cup

floor
  size      6 m
  friction  0.8, spinning 0.002, rolling 0.0002

ball1
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.6, spinning 0.002, rolling 0.0002
  colour    orange
  moves     freely
  rests     on floor, 0 m along
  launched  3.5 m/s along
  spins     87.5 rad/s about y

ball2
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.6, spinning 0.002, rolling 0.0002
  colour    white
  moves     freely
  rests     on floor, 35 cm along

ball3
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.6, spinning 0.002, rolling 0.0002
  colour    grey
  moves     freely
  rests     on floor, 70 cm along

cup
  is an             open box
  length            40 cm
  width             30 cm
  walls             12 cm
  wall thickness    2 cm
  base thickness    5 mm
  near wall height  5 mm
  bounce            dead
  friction          1.0, spinning 0.02, rolling 0.01
  colour            wood
  stands            on floor, 1.3 m along

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 touches cup
  ball3 comes to rest in cup
```

```json
{"what_happens": "ball1 rolls into ball2 at 0.29 s and ball2 into ball3 at 0.92 s, but each knock loses about half the speed and strong rolling friction brakes the balls, so ball3 starts at only 0.26 m/s and stops on the floor at x = 1.22 m, 28 cm short of the cup, which it never touches.", "works": false, "problem": "Too little speed survives the chain and the high rolling friction, so ball3 stops short of the cup."}
```

---
thinking (summarized):

The energy loss across collisions is substantial: ball1 at 1.5 drops to 0.69 for ball2, then down to 0.26 for ball3, so these aren't elastic collisions and rolling friction on the floor is clearly significant. Ball2's speed decaying from 0.69 to 0.08 over just 0.4 m suggests heavy deceleration, likely from sliding friction before it settles into rolling motion at the 5/7 ratio.

Working through the physics, I estimate the rolling friction deceleration at roughly 0.35 m/s² given MuJoCo's friction combination rules (which take the max by default), so I should lower the rolling friction coefficient on both balls and floor to something like 0.0002 to reduce this drag. I'm also reconsidering whether the collisions themselves need more restitution — ball1 only retains about 0.16 of its velocity after hitting ball2, which feels too inelastic for a "lively" bounce. Combining a higher launch speed (around 4 m/s) with lower rolling friction should get ball3 moving at a reasonable fraction of the initial velocity after accounting for the pass-through losses at each collision.

With that deceleration, ball3 should reach the cup fine, and I want to check it doesn't just blow past the far wall instead. I'll place ball2 around 35 cm, ball3 at 70 cm, and the cup near 1.3 m with its near end at 1.1, giving the cup base extra rolling friction so it actually captures the ball rather than letting it escape.

