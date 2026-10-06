```world
world  catapult into a bucket

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

catapult
  is a          catapult
  pivot height  70 cm
  arm length    1 m
  arm mass      250 g
  swings        from 0° to 45°
  spring        3.6 N·m/rad toward 100°
  damping       0.05 N·m·s/rad
  armature      0.01 kg·m²
  friction      0.3
  bounce        dead
  colour        wood

ball
  is a      sphere 5 cm radius, 100 g
  moves     freely
  rolls
  bounce    dead
  friction  0.3, spinning 0.01, rolling 0.004
  colour    orange
  rests     on catapult.scoop base, centred over catapult.scoop base

bucket
  is an           open box
  length          80 cm
  width           60 cm
  walls           45 cm
  wall thickness  2 cm
  base thickness  2 cm
  friction        0.9, spinning 0.02, rolling 0.01
  bounce          dead
  colour          grey
  on              floor, 3 m beyond ball

expect
  ball comes to rest in bucket
```

---
thinking (summarized):

**Calculating spring dynamics**

I’m looking into how the spring behaves beyond its rest position. Gravity and drag might affect the angle, maybe limiting it to around 45 degrees. I want to choose a resting angle between 100-120° for the spring. Considering the arm's moments and the forces at play, especially at θ45, it seems the spring could still push if it’s tuned properly. I’m also targeting a throw speed of about 5 m/s at a 45° angle for optimal range.

**Calculating potential energy**

I'm considering the calculation of potential energy here, starting with a mass of 1 kg and some components. I've got a scoop and various factors like the arm and ball coming into play. After estimating some values, I reach a total of approximately 0.211. Then I break down the gravitational potential energy formulas related to θ and the components involved. Ultimately, I calculate ΔPE, which turns out to be around 1.698 joules. It's quite detailed!

**Clarifying catapult parameters**

I'm working on naming the catapult library, including specific terms like hinge and bucket. I want to ensure the ball comes to rest in the bucket, which the library expects. I should check if I need to mention that no simulation is performed since the user likely only cares about the world model. 

I'm using particular values for the catapult, like mass and spring properties. Also, I need to clarify the positioning details and confirm alignment with documentation examples about centering.

**Positioning parts for runtime**

I'm considering the runtime for the ball's positioning while it rests on the arm, starting from the default position of zero. It seems I don't need to include a turned start since that's not necessary for this part. 

The hinge will swing from 0 to 45 degrees. I think I have a clear understanding here, and this should set everything up well for the intended functionality.