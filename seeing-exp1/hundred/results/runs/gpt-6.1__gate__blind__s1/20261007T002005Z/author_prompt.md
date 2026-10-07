Write a MuJoCo MJCF scene for this brief:

<brief>
ball starts 1 m up ramp and rolls into paddle, which swings into slider; slider knocks block off ledge so block drops through hoop into box and rests.
</brief>

MuJoCo will load the file, reset to the keyframe named `start` if there is one, and simulate it for
6 s. Nothing else acts on the scene: whatever moves must be set moving by the scene itself, for
example by a keyframe velocity, a spring, gravity, or a motor whose control the keyframe sets (controls keep
their keyframe values for the whole run).

A few conventions so the other tools can find things. They fix names and axes, not what you build:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- Name each thing's body exactly: `ball` (trigger ball: a body with a `<freejoint/>`); `ramp` (ball ramp: fixed in place; all its geoms belong to one body); `paddle` (swinging gate: a body on a hinge joint); `slider` (horizontal striker: a body on a slide joint); `block` (falling payload: a body with a `<freejoint/>`); `ledge` (payload ledge: fixed in place; all its geoms belong to one body); `hoop` (drop hoop: fixed in place; all its geoms belong to one body); `box` (catching box: fixed in place; all its geoms belong to one body). Its geoms may be named with the body's name as a prefix (`ball_...`).
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures,
  `<default>` classes or `<include>`.
- Give every body and geom a name, and write each element's attributes on a single line.
- Set `<option timestep="0.002"/>`.

Reply with the complete file in one ```xml code block. A sentence or two before the block is fine.

A ball counts as at rest when it moves slower than 5 cm/s at the end.
