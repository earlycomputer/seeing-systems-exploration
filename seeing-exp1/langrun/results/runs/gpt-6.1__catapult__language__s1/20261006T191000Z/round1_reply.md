The catapult launches the initially resting ball, but the throw falls short. The ball reaches a height of 1.20 m, then strikes the bucket’s near wall from outside. It falls onto the floor and rolls backward, stopping outside the bucket. **The world does not meet the brief.**

The corrected world below increases the spring stiffness to give the throw more range.

```world
world  spring catapult into a bucket

floor
  size      8 m
  friction  0.8, spinning 0.005, rolling 0.002

catapult
  is a          catapult
  pivot height  60 cm
  arm length    60 cm
  arm mass      120 g
  swings        from 0° to 45°
  spring        4.2 N·m/rad toward 75°
  damping       0.015 N·m·s/rad
  armature      0.01 kg·m²

ball
  is a      sphere 4 cm radius, 60 g
  moves     freely
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  sits      on catapult.scoop base, centred over catapult.scoop base

bucket
  is an           open box
  length          120 cm
  width           80 cm
  walls           40 cm
  wall thickness  2 cm
  base thickness  2 cm
  sits            on floor, 3 m beyond ball

expect
  ball touches catapult.scoop base
  ball comes to rest in bucket
```

```json
{
  "what_happens": "The catapult launches the ball, which reaches a height of 1.20 m, strikes the outside of the bucket's near wall, falls onto the floor, and rolls backward to rest outside the bucket.",
  "works": false,
  "problem": "The throw falls short, so the ball hits the bucket's near wall rather than landing inside."
}
```