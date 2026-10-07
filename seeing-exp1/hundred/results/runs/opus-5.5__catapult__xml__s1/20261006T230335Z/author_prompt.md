Write a MuJoCo MJCF scene for this brief:

<brief>
pendulum released from 0.6 m above its lowest point strikes cart, which knocks weight onto one end of seesaw so seesaw reaches its lower stop and throws ball into cup where it rests.
</brief>

MuJoCo will load the file, reset to the keyframe named `start` if there is one, and simulate it for
6 s. Nothing else acts on the scene: whatever moves must be set moving by the scene itself, for
example by a keyframe velocity, a spring, gravity, or a motor whose control the keyframe sets (controls keep
their keyframe values for the whole run).

A few conventions so the other tools can find things. They fix names and axes, not what you build:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- Name each thing's body exactly: `pendulum` (swinging striker: a body on a hinge joint); `cart` (impact cart: a body on a slide joint); `weight` (falling seesaw weight: a body with a `<freejoint/>`); `seesaw` (launching lever: a body on a hinge joint); `ball` (launched ball: a body with a `<freejoint/>`); `cup` (catching cup: fixed in place; all its geoms belong to one body). Its geoms may be named with the body's name as a prefix (`pendulum_...`).
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures,
  `<default>` classes or `<include>`.
- Give every body and geom a name, and write each element's attributes on a single line.
- Set `<option timestep="0.002"/>`.

Reply with the complete file in one ```xml code block. A sentence or two before the block is fine.

A ball counts as at rest when it moves slower than 5 cm/s at the end.
