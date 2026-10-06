```world
world  three rolling balls into a cup

floor
  size      4 m
  friction  0.6, spinning 0.001, rolling 0.0003

ball1
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.6, spinning 0.001, rolling 0.0003
  colour    orange
  moves     freely
  sits      on floor, -60 cm along, 0 cm to the left
  launched  1.4 m/s along
  spins     35 rad/s about y

ball2
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.6, spinning 0.001, rolling 0.0003
  colour    white
  moves     freely
  sits      on floor, 25 cm beyond ball1, 0 cm to the left

ball3
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.6, spinning 0.001, rolling 0.0003
  colour    orange
  moves     freely
  sits      on floor, 25 cm beyond ball2, 0 cm to the left

cup
  is an             open box
  length            32 cm
  width             20 cm
  walls             12 cm
  wall thickness    2 mm
  base thickness    1 mm
  near wall height  1 mm
  friction          0.8, spinning 0.01, rolling 0.01
  bounce            dead
  colour            wood
  sits              on floor, 32 cm beyond ball3, 0 cm to the left

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

---
thinking (summarized):

**Designing a rolling ball cup**

I’m considering the design of a cup that allows balls to roll into it. Since I can’t use simulations, I want to ensure the spheres are lively and can roll smoothly on the floor with minimal friction. The cup should have low walls and a base thickness that allows balls to enter easily, while also preventing them from going out. I need to think about the positions of the balls carefully so they don’t end up pushing each other in unintended ways.

**Evaluating ball collisions**

I’m thinking about the mechanics of collision between equal spheres. When ball1 collides, it resumes at about 2/7 of its speed, while ball2 retains its original spin. Upon colliding with ball3, I estimate the third speed to be around 0.6 of the initial velocity. I have set the launch speed at 1.2 m/s with a spin of 40 rad/s. I’m also noting the distances for each ball related to the cup's entrance for precise positioning. This should help me fine-tune the setup for accurate results!

**Analyzing cup dynamics**

I'm analyzing the effects of friction on a cup's floor. With a friction coefficient of 0.006, I calculate the deceleration, which is about 1.4 m/s². This slows the ball down significantly within a short distance. If I lower the friction to 0.0001, it results in minimal deceleration, not enough to stop the balls. The cup's design allows for effective stopping, but the 1mm lip only slows the balls without stopping them completely. I'm considering how balls might coast and follow each other into the cup.

**Evaluating contact parameters**

I'm considering how in MuJoCo, contact priority and merge settings should adjust solref with smaller time constants. It seems that while high friction can stop motion, it doesn't fully eliminate the elastic collision of spheres. I’m also thinking about how a box wall impacts a lively ball's bounce. Should I combine lively and dead states? Simplifying cup friction and ball interactions while maintaining clarity on the output floor is my goal here. Let's keep it straightforward!

**Defining a cup's usage**

I’m thinking about what a cup should look like. Maybe it should have an upward opening instead of being low near a wall? I wonder if an open box could work as a cup, with a low lip for entry. This might help balls roll in more easily. I’m not sure if a standard cup needs a ramp to the rim, but it seems that a low entry is what the user is looking for.

**Calculating cup dimensions and ball dynamics**

I need to specify the dimensions for the cup: 32x20 cm, with walls of 10 mm and a base of 1 mm. The first ball's position is -60, the second -35, and the third -10 with adjustments on the entrance and interior dimensions. I think about friction and how the balls roll, estimating their speed and impacts. The cup seems to have enough capacity, measuring 31.8 cm inside, and I'm trying to analyze whether the balls will rehit each other during their movements.

**Analyzing cup and ball dynamics**

I'm trying to figure out the best masses for cups in a Newton's cradle. It seems that having different masses could affect how velocity transfers and reduces the spin of the first ball. Instead of spinning, I wonder if launching with a slide might work better. I also think about the cup's dimensions and how the balls need to be positioned relative to each other. I need to ensure the cup is placed correctly, so everything interacts smoothly.