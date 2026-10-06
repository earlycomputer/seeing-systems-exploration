```world
world  three ball relay into a cup

floor
  size      4 m
  friction  0.6, spinning 0.005, rolling 0.001

ball1
  is a      sphere 5 cm radius, 200 g
  moves     freely
  rolls
  bounce    lively
  friction  0.6, spinning 0.005, rolling 0.008
  colour    orange
  sits      on floor, 0 m along, 0 m to the left
  launched  2 m/s along
  spins     40 rad/s about y

ball2
  is a      sphere 5 cm radius, 200 g
  moves     freely
  rolls
  bounce    lively
  friction  0.6, spinning 0.005, rolling 0.004
  colour    white
  sits      on floor, 30 cm beyond ball1, 0 m to the left

ball3
  is a      sphere 5 cm radius, 200 g
  moves     freely
  rolls
  bounce    lively
  friction  0.6, spinning 0.005, rolling 0.001
  colour    orange
  sits      on floor, 30 cm beyond ball2, 0 m to the left

cup
  is an             open box
  length            40 cm
  width             26 cm
  walls             14 cm
  wall thickness    1 cm
  base thickness    1 mm
  near wall height  1 mm
  friction          0.9, spinning 0.02, rolling 0.006
  bounce            dead
  colour            grey
  sits              on floor, 40 cm beyond ball3, 0 m to the left

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

---
thinking (summarized):

**Evaluating cup design**

I'm thinking about the physics involved in a cup that can roll and how its dimensions affect performance. The cup has to stop quickly, factoring in issues like rolling resistance and friction, which shouldn't be too high. I find that with a 1mm wall height, there's minimal clearance for the ball, and a low front lip might work. The design seems feasible, especially if I customize it to have a flush base and thin walls that keep it visually appealing.

**Designing a round cup**

I'm considering whether to use custom parts for a round cup. Its dimensions would be 30 by 24 cm, with 12 cm walls, a 2mm near wall height, and a 1mm base. The launch speed for the balls is important, starting at 1.4 for ball one and varying for the others. I realize that to ensure the third ball is fully inside, it needs to meet a threshold of being greater than 1.15 at the center. High friction will help slow the entry of the balls.

**Assessing ball dynamics**

I need to analyze the rolling of different spheres on a floor. For a sphere with a radius of 0.01, the first impact velocity is 1.4 after traveling 0.3 meters. The second ball's behavior follows with specific velocities and distances, ending with certain residuals. There's a calculation involving gaps and potential touches between balls, too. Overall, I’m considering factors like friction and transition time during these calculations to ensure accuracy across the movements of the balls.

**Analyzing ball interactions**

I'm adjusting the dynamics of ball1 after a roll, with a stopping distance of 0.56 meters and a final position of 0.876. I'm considering how ball1 might hit ball2, which has a residual after an impact with ball3, possibly around 0.9. If I raise the rolling friction to 0.002, it could decelerate ball1 by 0.28, reducing the distance to 0.27, ending at 0.59, while ball2 would stop at 0.8. I need to be careful with these calculations!

**Considering mass and momentum in collisions**

I'm thinking about using unequal masses for three balls: ball 1 at 0.4 kg, ball 2 at 0.2 kg, and ball 3 at 0.1 kg, all with a radius of 0.05 m. When they collide, I'll focus on momentum transfer and how energy loss occurs with a coefficient of restitution (e1.0). The balls exhibit varying rolling friction, so I may set specific values for each. I want to ensure the calculations accurately reflect the motion and energy transfer.

**Analyzing ball dynamics and collisions**

I'm evaluating the motion of several balls after collisions. Ball 1 decelerates to 0.84, with an initial launch from a gap. After contact, ball 2 rolls and slows down as well, with its velocity changing over time. Ball 3 also has a slower deceleration. I want to consider how these balls interact, including possible spins and the effect of friction as they come to a stop against walls. I need to think about using simpler, symmetrical masses to keep things manageable while ensuring reliable speeds.

**Setting up a sphere motion experiment**

I need to work with three spheres, each with a 5 cm radius and a weight of 200 g, arranged with 30 cm spacing between them. I’m aiming for a speed of 1.8 m/s with a spin of 36. The floor will have a rolling resistance of 0.001, and the balls will have the same resistance. I want to see how they interact, especially how ball 1 can push ball 2 into a cup near the wall within 6 seconds after they stop.

**Examining floor friction effects**

I'm considering the effects of floor friction on different types of movement. For instance, with spinning, I've noted a friction coefficient of 0.6, while rolling is at 0.005. I also mentioned specific values for three balls: one has a spin of 0.6 and a roll of 0.008; the second ball has a friction of 0.004, and the third has a value of 0.001. I'm curious about how these interactions affect overall performance.