```world
world  spring catapult into a bucket

floor
  size      8 m
  friction  0.8, spinning 0.01, rolling 0.005

catapult
  is a          catapult
  pivot height  70 cm
  arm length    1 m
  arm mass      300 g
  swings        0° to 45°
  spring        5 N·m/rad toward 100°
  damping       0.08 N·m·s/rad
  armature      0.01 kg·m²
  friction      0.6, spinning 0.005, rolling 0.002
  colour        wood
  on            floor

ball
  is a      sphere 4 cm radius, 150 g
  moves     freely
  rolls
  bounce    dead
  friction  0.8, spinning 0.02, rolling 0.01
  colour    orange
  rests     on catapult.scoop base, centred over catapult.scoop base

bucket
  is an           open box
  length          1.2 m
  width           80 cm
  walls           60 cm
  wall thickness  2 cm
  base thickness  2 cm
  bounce          dead
  friction        0.8, spinning 0.02, rolling 0.01
  colour          grey
  on              floor, 3 m beyond ball

expect
  ball touches catapult
  ball comes to rest in bucket
```

---
thinking (summarized):

**Designing a spring catapult**

I need to design a spring catapult that will launch a ball from rest at a specific range. I don't have any tools for simulation, so I'd like to ensure it's physically plausible, using a generous bucket with reasonable wall size. The dynamics should allow the catapult to work effectively. I’ll set the arm's position, ensuring it can swing upwards properly, and determine the launch angles and velocities for the best results. The launch angle must be optimized.

**Calculating catapult dynamics**

I’m figuring out the position of the catapult ball relative to the pivot, using some trigonometry. The scoop’s design needs to ensure the ball is well-positioned, making sure the arm’s length is accurate. I've set up the necessary offsets for height to ensure proper launch angles. Now, I need to calculate the launch velocities and distances needed for the ball to reach a specific point after dropping. I’ll fine-tune the angles for optimal performance.