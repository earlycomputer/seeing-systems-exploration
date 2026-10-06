A part only takes the lines it needs and a position, so I removed the `colour` line from `bucket`. The catapult launch numbers are unchanged, and the run is still unchecked.

```world
world  catapult into a bucket

floor
  friction  0.8, spinning 0.005, rolling 0.002

catapult
  is a          catapult
  pivot height  50 cm
  arm length    60 cm
  arm mass      300 g
  swings        from 0° to 40°
  spring        3.87 N·m/rad toward 90°
  damping       0 N·m·s/rad
  armature      0.01 kg·m²
  stands        on floor

ball
  is a      sphere 3 cm radius, 60 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  sits      on catapult.scoop base, outside catapult.scoop back's far end

bucket
  is an   open box
  length  70 cm
  width   70 cm
  walls   25 cm
  stands  on floor, its base 3 m beyond ball

expect
  ball comes to rest in bucket
```

---
thinking (summarized):

I should remove the colour reference from the bucket, and double-check the catapult—confirming colour isn't used there either, so that's fine.

