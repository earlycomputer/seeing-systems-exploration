```world
world  spring catapult into a bucket

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

catapult
  is a          catapult
  pivot height  65 cm
  arm length    70 cm
  arm mass      200 g
  swings        from 0° to 55°
  spring        4 N·m/rad toward 70°
  damping       0.025 N·m·s/rad
  armature      0.01 kg·m²

ball
  is a      sphere 2.5 cm radius, 40 g
  moves     freely
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.005
  colour    orange
  rests     on catapult.scoop base, centred over catapult.scoop base

bucket
  is an           open box
  length          1 m
  width           80 cm
  walls           50 cm
  wall thickness  2 cm
  base thickness  2 cm
  bounce          dead
  friction        0.8, spinning 0.01, rolling 0.005
  sits            on floor, 3 m beyond ball

expect
  ball comes to rest in bucket
```

---
thinking (summarized):

**Evaluating design parameters**

I think it's safer to stick with standard library top-level friction and avoid new parts. I'm considering a bucket with height 0.5, length 1.2, and width 0.8, and perhaps capturing a clear range. I’ll manage the spring constant at 4 N·m with rest angle of 70°, allowing swings from 0 to 55°. I’m also checking the mass and radius of the ball to ensure it fits well. Overall, I want to prioritize physical robustness without making an impractical design.

**Clarifying simulation expectations**

I’m analyzing the simulation where a ball is involved. It seems like there's an expectation for the ball to bounce, but it appears it might not bounce as expected. I'm considering how it interacts with a catapult and whether it can touch it. There's also a thought about the ball coming to rest in a bucket. It looks like the expectation of the ball touching the catapult is optional, but I need to clarify how it all fits together.