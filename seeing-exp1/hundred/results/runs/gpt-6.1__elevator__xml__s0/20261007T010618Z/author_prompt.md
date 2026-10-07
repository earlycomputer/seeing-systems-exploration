Write a MuJoCo MJCF scene for this brief:

<brief>
weight falls 0.5 m onto lever, whose rising end crosses a gap to push lift upward; lever reaches its lower stop before lift crosses another gap and strikes ball across bridge into cup where it rests.
</brief>

MuJoCo will load the file, reset to the keyframe named `start` if there is one, and simulate it for
6 s. Nothing else acts on the scene: whatever moves must be set moving by the scene itself, for
example by a keyframe velocity, a spring, gravity, or a motor whose control the keyframe sets (controls keep
their keyframe values for the whole run).

A few conventions so the other tools can find things. They fix names and axes, not what you build:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- Name each thing's body exactly: `weight` (lever weight: a body with a `<freejoint/>`); `lever` (lifting lever: a body on a hinge joint); `lift` (vertical striker: a body on a slide joint); `ball` (target ball: a body with a `<freejoint/>`); `bridge` (ball bridge: fixed in place; all its geoms belong to one body); `cup` (catching cup: fixed in place; all its geoms belong to one body). Its geoms may be named with the body's name as a prefix (`weight_...`).
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures,
  `<default>` classes or `<include>`.
- Give every body and geom a name, and write each element's attributes on a single line.
- Set `<option timestep="0.002"/>`.

Reply with the complete file in one ```xml code block. A sentence or two before the block is fine.

A ball counts as at rest when it moves slower than 5 cm/s at the end.
