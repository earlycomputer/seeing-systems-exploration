Ball1 is launched rolling along x into ball2, which knocks ball2 into ball3. Ball3 rolls over a low lip into an open-box cup, and the cup's tall dead far wall stops it there.

```world
world  three ball chain into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ball1
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.6, spinning 0.005, rolling 0.002
  colour    orange
  moves     freely
  rests     on floor, 0 m along
  launched  1.5 m/s along
  spins     37.5 rad/s about y

ball2
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.6, spinning 0.005, rolling 0.002
  colour    white
  moves     freely
  rests     on floor, 50 cm along

ball3
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.6, spinning 0.005, rolling 0.002
  colour    grey
  moves     freely
  rests     on floor, 1 m along

cup
  is an             open box
  length            40 cm
  width             30 cm
  walls             12 cm
  wall thickness    2 cm
  base thickness    5 mm
  near wall height  5 mm
  bounce            dead
  friction          1.0, spinning 0.01, rolling 0.01
  colour            wood
  stands            on floor, 1.75 m along

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 touches cup
  ball3 comes to rest in cup
```

---
thinking (summarized):

I'm setting up a chain-reaction scene with three balls in a row that collide sequentially, with the last one rolling into a cup — thinking through how the cup should be shaped, perhaps with a short near wall, so a rolling ball can actually enter it rather than being blocked.

Making balls lively but the cup dead means a chain collision shares momentum ball to ball, with spin and rolling friction causing each ball to drift forward slightly after impact rather than stopping dead. I need to check ball3's radius against the cup's 30x30 cm footprint to make sure it actually settles inside the boundary rather than rolling out.

I should give ball1 proper topspin to roll rather than slide, with ω=v/r about the y-axis. Working through the collision chain, ball3 ends up with speed around 0.77 m/s after friction decay, and I need to check whether that's enough rolling energy to climb the 5mm step given its 4cm radius—there's a known threshold condition for a rolling ball clearing a step edge that I need to apply here.

I'm also considering whether ball3's final speed is enough to clear the far wall rather than just bounce dead against it, which depends on wall height versus ball diameter—maybe raising the walls to 12cm solves it. Separately, I'm figuring out how to phrase the cup's placement relative to the floor, settling on something like "stands on floor, 1.75 m along" to position it correctly using the part-placement syntax.

Now I'm checking the cup's length against the ball positions to confirm there's no overlap, and considering whether using identical names like ball1, ball2, ball3 for repeated spheres lets me selectively apply properties like spin to just one. I'm also working out whether balls can validly "touch" each other in a sequence, with the end result being ball3 coming to rest inside the cup.

With rolling friction set low at 0.002, the balls stay lively enough that ball1 might eventually catch up to ball2's position and possibly climb a step, but this shouldn't disrupt the main outcome. Given the six-second window, ball3 should reach the cup around the 1.5 second mark, leaving plenty of time for everything to settle.

