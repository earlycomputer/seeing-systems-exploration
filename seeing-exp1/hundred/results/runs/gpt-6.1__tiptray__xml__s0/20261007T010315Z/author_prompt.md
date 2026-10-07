Write a MuJoCo MJCF scene for this brief:

<brief>
weight drops 0.6 m into tray, tipping tray to its lower stop so ball1 rolls out into ball2; ball2 knocks block through hoop and into bin where it rests.
</brief>

MuJoCo will load the file, reset to the keyframe named `start` if there is one, and simulate it for
6 s. Nothing else acts on the scene: whatever moves must be set moving by the scene itself, for
example by a keyframe velocity, a spring, gravity, or a motor whose control the keyframe sets (controls keep
their keyframe values for the whole run).

A few conventions so the other tools can find things. They fix names and axes, not what you build:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- Name each thing's body exactly: `weight` (tray tipping weight: a body with a `<freejoint/>`); `tray` (tipping tray: a body on a hinge joint); `ball1` (spilled ball: a body with a `<freejoint/>`); `ball2` (transfer ball: a body with a `<freejoint/>`); `block` (final payload: a body with a `<freejoint/>`); `hoop` (drop hoop: fixed in place; all its geoms belong to one body); `bin` (catching bin: fixed in place; all its geoms belong to one body). Its geoms may be named with the body's name as a prefix (`weight_...`).
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures,
  `<default>` classes or `<include>`.
- Give every body and geom a name, and write each element's attributes on a single line.
- Set `<option timestep="0.002"/>`.

Reply with the complete file in one ```xml code block. A sentence or two before the block is fine.

A ball counts as at rest when it moves slower than 5 cm/s at the end.
