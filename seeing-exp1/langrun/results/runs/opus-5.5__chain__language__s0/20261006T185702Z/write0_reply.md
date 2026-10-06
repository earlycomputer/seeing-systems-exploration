Each collision hands most of the momentum down the row. The cup has a low 1 cm lip that `ball3` can roll over, and a grippy, dead base and walls so the ball stays inside once it is in.

```parts
part low lipped cup
  needs  length
  needs  width
  needs  walls
  needs  lip, else 1 cm
  needs  wall thickness, else 1 cm
  needs  base thickness, else 1 cm

  base
    is a      box length by width by base thickness
    on        floor
    friction  0.9, spinning 0.02, rolling 0.01
    bounce    dead
  near wall
    is a      box wall thickness by width by lip
    on        floor, centred on base's near end
    bounce    dead
  far wall
    is a      box wall thickness by width by walls
    on        floor, centred on base's far end
    bounce    dead
  left wall
    is a      box length by wall thickness by walls
    on        floor, centred on base's left side
    bounce    dead
  right wall
    is a      box length by wall thickness by walls
    on        floor, centred on base's right side
    bounce    dead
```

```world
world  three balls into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ball1
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    orange
  moves     freely
  rests     on floor, 50 cm along
  launched  3 m/s along

ball2
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    white
  moves     freely
  rests     on floor, 30 cm beyond ball1

ball3
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    grey
  moves     freely
  rests     on floor, 30 cm beyond ball2

cup
  is a    low lipped cup
  length  20 cm
  width   14 cm
  walls   8 cm
  lip     1 cm
  its base 55 cm beyond ball3

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

---
thinking (summarized):

I'm thinking through a chain reaction setup: three balls in a row where the first hits the second, which hits the third, which needs to roll into a cup. The tricky part is the cup's walls—a rolling ball can't easily enter unless the wall is low enough to roll over, so I'm considering whether a small step height relative to the ball's radius would let it climb in.

So the step onto the base is about 1cm, which a 3cm-radius ball at ~1 m/s should climb fine. Inside, it'll hit the far wall and likely stay put with a dead bounce, but I need enough rolling friction on the base so it doesn't roll back toward the entrance — I'm estimating the deceleration from rolling friction torque to make sure it settles rather than escaping back down the step.

8 cm tall walls with a 1 cm lip works fine as "cup" terminology. For the collision chain with equal masses and elastic collisions, I'm thinking through how momentum transfers like a Newton's cradle: ball1 keeps its spin and rolls forward slightly, ball2 starts sliding without spin until friction brings it to rolling at 5/7 of its initial speed, and this degradation repeats down the chain. I'll pick an initial launch speed of 3 m/s for the first ball.

Following through the numbers: ball1 settles into rolling at 2.14 m/s and strikes ball2, which ends up rolling at about 1.53 m/s after its own friction settles, then ball3 rolls off at roughly 1.09 m/s—enough to clear the 1 cm step. Meanwhile ball1's retained spin pushes it forward again at about 0.6 m/s to catch up and hit ball2 a second time, and similarly ball2 chases ball3 afterward at around 0.44 m/s—which is right at the edge of whether it has enough energy to climb the step into the cup.

Working out floor friction effects, with deceleration around 0.47 m/s², ball2 at 0.44 m/s only coasts about 0.2 m before stopping, while ball3 at 1.09 m/s can travel over a meter. So placing the cup around 40-50 cm past ball3's resting point makes sense—checking, ball3 would still be moving near 0.85 m/s there, plenty to climb the step, while ball2's momentum dies out well before reaching that far, and ball1's second chase doesn't catch ball2 in time since ball2 is already moving faster again.

I'm also considering collision restitution settings—default MuJoCo contacts are fairly inelastic, so adding a "bounce lively" setting on the balls could help energy transfer. For spacing, I'm thinking roughly 15 cm gaps with 3 cm ball radius, and calculating the sliding-to-rolling transition distance for ball1 (about 0.28 m)—a shorter gap means ball1 hits ball2 while still sliding, which could actually give cleaner momentum transfer without residual spin. I'm laying out positions along the track at roughly 0.5 m, 0.8 m, and 1.1 m intervals for the three balls.

Now I'm working out the cup placement—positioning it on the floor using its base relative to ball3, roughly 55 cm beyond, so the base center lands around 1.65 m along the track with the near wall close enough that ball3 travels about 0.41 m before hitting the lip. I'm defaulting the across-position to zero and writing the placement reference accordingly.

I'm considering whether a library open box part could work instead of a custom one, but since I need friction control on the base, I'll stick with defining a custom "cup" part.

I'm naming the part "low lipped cup" to avoid conflicts, with a base having high rolling friction and dead bounce, and walls also with dead bounce, keeping width at 14 cm with 1 cm wall thickness since the balls stay aligned.

I'm also checking whether ball3 might bounce back out after hitting the far wall — with dead bounce and rolling friction, the rebound speed is small enough that it decelerates and stops well within the cup's length, though I still need to account for spin effects.

The ball keeps spinning forward against the wall after impact, which is fine, and the base's top sits at 1 cm with the ball center at 3 cm, so everything lines up properly. The expected outcome is that ball1 touches ball2, ball2 touches ball3, and ball3 settles to rest inside the cup — time to write it out.

