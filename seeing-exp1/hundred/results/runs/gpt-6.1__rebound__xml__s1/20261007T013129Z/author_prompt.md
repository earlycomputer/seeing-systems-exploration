Write a MuJoCo MJCF scene for this brief:

<brief>
block falls 0.5 m onto spring-loaded plunger, whose rebound makes it strike ball up ramp so ball descends through hoop into cup and rests.
</brief>

MuJoCo will load the file, reset to the keyframe named `start` if there is one, and simulate it for
6 s. Nothing else acts on the scene: whatever moves must be set moving by the scene itself, for
example by a keyframe velocity, a spring, gravity, or a motor whose control the keyframe sets (controls keep
their keyframe values for the whole run).

A few conventions so the other tools can find things. They fix names and axes, not what you build:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- Name each thing's body exactly: `block` (falling compressor: a body with a `<freejoint/>`); `plunger` (spring-loaded striker: a body on a slide joint); `ball` (launched ball: a body with a `<freejoint/>`); `ramp` (launch ramp: fixed in place; all its geoms belong to one body); `hoop` (flight hoop: fixed in place; all its geoms belong to one body); `cup` (catching cup: fixed in place; all its geoms belong to one body). Its geoms may be named with the body's name as a prefix (`block_...`).
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures,
  `<default>` classes or `<include>`.
- Give every body and geom a name, and write each element's attributes on a single line.
- Set `<option timestep="0.002"/>`.

Reply with the complete file in one ```xml code block. A sentence or two before the block is fine.

A ball counts as at rest when it moves slower than 5 cm/s at the end.
