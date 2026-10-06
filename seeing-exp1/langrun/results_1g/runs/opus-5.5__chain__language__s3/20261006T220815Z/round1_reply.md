**What happened:** Each collision passed on less than half the speed. Ball1 was launched at 2.4 m/s, ball2 left at about 1.0 m/s, and ball3 left at about 0.43 m/s. Floor rolling friction slowed ball3 further. It reached the cup's 1 cm front step at about 0.3 m/s and could not climb it. It bounced back and stopped just outside the cup at x = 1.86 m. Ball1 and ball2 also stopped on the floor behind it.

**Changes:**
- Lowered the step: the cup's base and front wall are now 3 mm high, which a ball can roll over easily.
- Launched ball1 faster, at 4 m/s, still with matching spin so it starts rolling.
- Put the balls a little closer together (25 cm apart instead of 30 cm), so less speed is lost on the floor between collisions.
- Lowered the rolling friction inside the cup, so ball3 rolls well inside before it stops instead of halting on the edge.

```json
{"what_happens": "ball1 rolls into ball2 and ball2 into ball3, but each collision passes on less than half the speed; ball3 reaches the cup's 1 cm front step at about 0.3 m/s, bounces back off it and stops just outside the cup at x = 1.86 m, with ball1 and ball2 stopped on the floor behind it.", "works": false, "problem": "Ball3 arrives too slowly to climb the cup's 1 cm front step, so it stops outside the cup."}
```

```world
world  three balls into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ball1
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    orange
  moves     freely
  rests     on floor, 1 m along
  launched  4 m/s along
  spins     100 rad/s about y

ball2
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    white
  moves     freely
  rests     on floor, 25 cm beyond ball1

ball3
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    black
  moves     freely
  rests     on floor, 25 cm beyond ball2

cup
  is an             open box
  length            50 cm
  width             30 cm
  walls             10 cm
  wall thickness    2 cm
  base thickness    3 mm
  near wall height  3 mm
  friction          0.8, spinning 0.02, rolling 0.008
  bounce            dead
  colour            wood
  its base 55 cm beyond ball3

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 touches cup
  ball3 comes to rest in cup
```

---
thinking (summarized):

The speeds collapsed too much between collisions—ball2 dropped to 1.03 m/s and ball3 to just 0.43 m/s, too weak to climb the 1cm step given the 0.8 sliding friction. I need much higher launch speed, tighter spacing, and lower friction losses to keep the chain reaction alive.

The transfer ratio seems to be around 0.43 per collision, so to get ball3 climbing the step at around 1 m/s, ball1 would need to launch near 6 m/s—risky since it might cause the ball to hop off the surface rather than roll. Instead of pushing speed that high, maybe I should rethink the cup design itself, perhaps removing the obstacle that requires climbing a step altogether.

Reducing the step height to about 2mm instead of 1cm would make it much easier to climb, so I could bump the launch speed to 4 m/s and shorten gaps between balls to 20cm to minimize floor losses. Working through the energy transfer, ball3 should arrive at roughly 0.65 m/s at the shallow step, which seems survivable, then decelerate inside the cup at about 3.5 m/s² and stop within about 6cm—right near the edge of the cup's footprint, which is a bit tight but might work.

Lowering the cup's rolling friction to 0.008 instead would give a decay of about 1.4 m/s², letting the ball travel roughly 15cm into the cup before stopping, which is much safer given the cup is 50cm long. I should also consider that trailing balls 2 and 1 might follow into the cup and bump ball3 further in, which is still fine since they'd remain within the cup boundary, and I'm checking whether ball1 at 4 m/s might briefly hop off the floor during collision but conclude it should be okay.

