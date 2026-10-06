Parts don't take `colour`, so I removed it from the bucket. I also put `at` in front of the bucket's position line, since bare position lines might not parse there.

```world
world  catapult into a bucket

floor
  friction  0.8, spinning 0.005, rolling 0.002

catapult
  is a          catapult
  pivot height  50 cm
  arm length    50 cm
  arm mass      300 g
  swings        from 0° to 40°
  spring        5.5 N·m/rad toward 90°
  damping       0.01 N·m·s/rad
  armature      0.01 kg·m²

ball
  is a      sphere 3 cm radius, 100 g
  colour    orange
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  moves     freely
  rests     in catapult

bucket
  is an   open box
  length  80 cm
  width   80 cm
  walls   30 cm
  at      its base 3 m beyond ball

expect
  ball comes to rest in bucket
```

---
thinking (summarized):

I should remove the colour line from the bucket and reconsider whether position can be written bare, like "its base 3 m beyond ball" — need to check if that parses without an explicit "at" keyword, or if it's safer to prefix it with "at" so the clause structure stays consistent with the other position examples like "its rim 4 m beyond ball".

