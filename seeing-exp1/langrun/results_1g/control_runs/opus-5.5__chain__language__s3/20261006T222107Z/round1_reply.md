**What happens in the run**

Ball1 leaves at 2 m/s and strikes ball2 at 0.06 s. Ball2 strikes ball3 at 0.15 s. Ball3 rolls off at about 0.5 m/s, but every ball slows at roughly 0.5 m/s².

That deceleration comes from the rolling friction on the balls and the floor. MuJoCo applies the larger of the two coefficients to each contact. A coefficient of 0.003 on a 4 cm ball brakes it hard.

Ball3 stops at x = 1.74 m, 2 cm short of the cup's near wall, and never enters the cup. The chain of collisions works; only the last step fails.

**What I changed**

- **Rolling friction:** cut to 0.0005 on the floor and on the balls. The cup keeps 0.01, so a ball that gets inside still stops quickly.
- **Launch speed:** raised to 3 m/s.
- **Cup position:** moved 10 cm closer.
- **Lip height:** lowered from 8 mm to 6 mm so ball3 can climb in with margin.

```json
{"what_happens": "ball1 hits ball2, which hits ball3, but heavy rolling friction slows every ball at about 0.5 m/s² and ball3 stops on the floor 2 cm short of the cup's near wall, never entering the cup.", "works": false, "problem": "Rolling friction of 0.002–0.003 on 4 cm balls brakes ball3 to a stop before it reaches the cup."}
```

```world
world  three balls into a cup

floor
  size      6 m
  friction  0.8, spinning 0.002, rolling 0.0005

ball1
  is a      sphere 4 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.002, rolling 0.0005
  colour    orange
  moves     freely
  on floor, 1 m along
  launched  3 m/s along
  spins     75 rad/s about y

ball2
  is a      sphere 4 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.002, rolling 0.0005
  colour    white
  moves     freely
  on floor, 20 cm beyond ball1

ball3
  is a      sphere 4 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.002, rolling 0.0005
  colour    black
  moves     freely
  on floor, 20 cm beyond ball2

cup
  is an             open box
  length            30 cm
  width             20 cm
  walls             10 cm
  base thickness    3 mm
  near wall height  6 mm
  bounce            dead
  friction          1.0, spinning 0.01, rolling 0.01
  colour            wood
  on floor, its base 45 cm beyond ball3

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

---
thinking (summarized):

Ball1 barely moved before stopping, going from 1.00 to about 1.12 where it made contact with ball2 (positioned at 1.20, with radii of 4 each meeting at that point). That gap of 0.12 m covered in 0.06 s gives a collision speed of 2 m/s, matching the initial launch velocity.

I'm tracing through the subsequent collisions: ball2 hitting ball3 around 0.15s, then the deceleration pattern on ball3 (0.50→0.38→0.25→0.14) revealing a decay of roughly 0.5 m/s². This matches the physics of rolling friction with MuJoCo's default coefficient around 0.003, where the deceleration formula comes out to about 0.53 m/s² — consistent with what I'm seeing. Since MuJoCo takes the max of the two geoms' rolling friction values, both the ball and floor coefficients are contributing, so I should lower both to something like 0.0002 to get a much gentler decay of about 0.035 m/s². I also suspect ball1's quick stop despite its spin and the small bounce at 0.05s are related to this same friction issue.

With rolling friction reduced, ball3 should keep moving around 0.7 m/s when it reaches the cup area, landing close enough (within a couple centimeters) given the gap and distances I calculated. But the cup itself needs higher rolling friction (around 0.01) so that once a ball lands inside it, the contact pair friction (taking the max) forces a fast deceleration of about 1.75 m/s² to bring it to rest quickly, satisfying the requirement that it settles under 5 cm/s by 6 seconds.

I should bump the threshold to 0.4, so increasing launch speed to 3 m/s and shrinking the lip to 6mm should help, while also moving the cup closer (45cm beyond ball3, ~26cm gap) with a lower near wall and thinner base. At 3 m/s launch, ball3's velocity scales up to roughly 0.85, which clears things nicely — I'll leave ball1's spin alone since it's harmless.

