The catapult throws the ball, but at 0.97 s it strikes the outside of the bucket’s near wall. It rebounds backward and comes to rest on the floor, outside the bucket. **The world does not satisfy the brief.**

This correction lowers the bucket walls so the observed flight can clear the near rim. The bucket remains centred 3 m beyond the ball’s starting position.

```world
world  spring catapult into a bucket

floor
  size      8 m
  friction  0.8, spinning 0.01, rolling 0.005

catapult
  is a          catapult
  pivot height  60 cm
  arm length    1 m
  arm mass      250 g
  swings        0° to 45°
  spring        5.1 N·m/rad toward 90°
  damping       0.05 N·m·s/rad
  armature      0.01 kg·m²
  friction      0.8
  colour        wood
  on            floor

ball
  is a      sphere 4 cm radius, 150 g
  moves     freely
  rolls
  bounce    dead
  friction  0.8, spinning 0.02, rolling 0.01
  colour    orange
  on        catapult.scoop base, at catapult.scoop base's near end

bucket
  is an           open box
  length          90 cm
  width           70 cm
  walls           30 cm
  wall thickness  2 cm
  base thickness  2 cm
  bounce          dead
  friction        0.9, spinning 0.02, rolling 0.01
  colour          grey
  on              floor, 3 m beyond ball

expect
  ball touches bucket
  ball comes to rest in bucket
```

```json
{
  "what_happens": "The catapult launches the ball, which hits the outside of the bucket's near wall at 0.97 s, rebounds backward, and comes to rest on the floor outside the bucket.",
  "works": false,
  "problem": "The ball does not clear the near wall and therefore does not land in the bucket."
}
```