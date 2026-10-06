The dropped weight drives the seesaw using gravity alone. Touching the overhead height marker requires the small ball to rise at least 66 cm above its starting position.

```world
world  gravity seesaw launch

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

support
  is a      box 8 by 32 by 58 cm
  on        floor
  colour    dark grey

pivot
  is a      point
  at        65 cm up

seesaw
  is a      box 200 by 24 by 4 cm, 250 g
  at        65 cm up
  turns on  seesaw hinge, about y, at pivot
  swings    from 0° to 30°
  damping   0.005 N·m·s/rad
  armature  0.001 kg·m²
  friction  0.5, spinning 0.005, rolling 0.002
  bounce    dead
  colour    wood

ball
  is a      sphere 4 cm radius, 100 g
  moves     freely
  rolls
  on        seesaw, 80 cm behind seesaw
  friction  0.5, spinning 0.005, rolling 0.002
  bounce    dead
  colour    orange

weight
  is a      sphere 7 cm radius, 1 kg
  moves     freely
  rolls
  at        80 cm beyond seesaw, 3.7 m up
  friction  0.5, spinning 0.005, rolling 0.002
  bounce    dead
  colour    black

height marker
  is a      box 140 by 60 by 2 cm
  at        80 cm behind pivot, 1.42 m up
  bounce    dead
  colour    grey

expect
  weight touches seesaw
  ball touches seesaw
  ball touches height marker
```

---
thinking (summarized):

**Analyzing seesaw physics**

I'm setting up a seesaw with specific measurements: 80 cm behind the pivot, a sphere with a 4 cm radius weighs 0.2 kg, and the beam itself has a mass and dimensions. I need to determine the angular movement and various positions as it swings from 0 to 35 degrees. The focus is on the first 0.03 seconds when the ball makes contact in an inelastic impact. I'm curious about the velocities once the ball contacts the beam; I need to figure those out!

**Evaluating hoop height and design**

I’m thinking about setting the hoop at a height of 1.5 and how to align it slightly centered at x=-0.8. I might not need to measure everything explicitly, but I need to check if the ball can touch the required height. If I use a fixed "witness" rod at the center, that could confirm the ball's initial position, ensuring it’s above the necessary height. I wonder about overhead markers being aesthetically pleasing or necessary, or maybe just a ring at the threshold should do.

**Assessing hoop design and functionality**

I'm considering a diameter of about 1.6m for the broad ring, with the light end at z=1.3. The ball needs to cross upward and downward, likely landing nearby but potentially getting caught. I might not need a marker if there's no expected height form. I'll rely on the ball touching a height marker and a seesaw for checks. This should allow me to verify the criteria through collisions at the right height. I wonder, should that roof be something that the ball can touch?

**Examining ball trajectory and setup**

I’m looking into the ball's sliding trajectories at the moment of collision. The speed taken via dead MuJoCo contact seems to cause soft contact with the surface, resulting in a slight horizontal velocity. I'm estimating about 100g of upward velocity in 0.14 seconds, while the board turns and stops in 0.065 seconds, but the ball remains airborne.

The dimensions of the setup with the marker and height marker box also need to be considered for accuracy. I’m thinking through how all these elements come together!

**Reviewing height marker calculations**

I’m checking how the overhead target’s underside is positioned 70 cm above the ball’s initial height. It seems if the ball touches it, this verifies a rise greater than 50 cm. The difference between the initial height and the underside is 66 cm. The center rise appears to be 66 cm based on the contact point of 1.37 m.

I want to ensure that the fixed height marker accurately reflects these measurements and that it verifies a minimum rise of 60 cm when the ball makes contact. I’m considering how to set everything correctly!

**Considering parsing options**

I’m examining whether parsing negative information is supported. Starting with the phrase "80 cm behind the pivot" seems good. I think separating out "at level with the pivot" could be optional, but I want to make sure it references the position correctly.

Using "at 65 cm up" in combination with the pivot is also worth considering. I’ll need to clarify how these phrases fit together to ensure everything is presented clearly and accurately!

**Finalizing description**

I shouldn't overcomplicate things—we need just one clear sentence that describes the target and the world. It’s important to weigh the balls precisely, with the black balls being heavy and the orange ones standing out clearly. The color marker should definitely be orange. And I want to keep the world number minimal. Once I have everything aligned, I think it’ll all come together nicely!