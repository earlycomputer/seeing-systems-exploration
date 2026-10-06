Write a MuJoCo MJCF scene for this brief:

<brief>
three balls sit in a row on the floor; the first is rolled into the second, the second rolls into the third, and the third rolls into a cup
</brief>

MuJoCo will load the file, reset to the keyframe named `start` if there is one, and simulate it for
6 s. Nothing else acts on the scene: whatever moves must be set moving by the scene itself, for
example by a keyframe velocity, a spring, gravity, or a motor whose control the keyframe sets (controls keep
their keyframe values for the whole run).

A few conventions so the other tools can find things. They fix names and axes, not what you build:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- The balls are bodies named `ball1` (the one set rolling), `ball2` and `ball3`, each with a `<freejoint/>` and one sphere geom. The cup is a body named `cup`; all its geoms belong to it.
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures,
  `<default>` classes or `<include>`.
- Give every body and geom a name, and write each element's attributes on a single line.
- Set `<option timestep="0.002"/>`.

Reply with the complete file in one ```xml code block. A sentence or two before the block is fine.

After the file, also write what should happen as an ```expect block, one expectation per line, in these forms:

```expect
ball touches ramp
ball comes to rest in cup
ball drops through hoop
door reaches its lower stop
```

A name is a body or geom name from your file (`bucket` also covers geoms named `bucket_...`). After each run your
expectations are checked against it and you are told which hold. A ball counts as at rest when it moves slower than
5 cm/s at the end. If you send a corrected file, send its ```expect block again.
