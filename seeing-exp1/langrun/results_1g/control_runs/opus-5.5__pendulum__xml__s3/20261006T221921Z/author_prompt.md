Write a MuJoCo MJCF scene for this brief:

<brief>
a pendulum swings down and strikes a ball resting on the floor, which rolls into a cup whose centre is 1 m from where the ball starts
</brief>

MuJoCo will load the file, reset to the keyframe named `start` if there is one, and simulate it for
6 s. Nothing else acts on the scene: whatever moves must be set moving by the scene itself, for
example by a keyframe velocity, a spring, gravity, or a motor whose control the keyframe sets (controls keep
their keyframe values for the whole run).

A few conventions so the other tools can find things. They fix names and axes, not what you build:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- The pendulum is a body named `pendulum` on a hinge joint; every geom of the pendulum is named with the prefix `pendulum`. The ball is a body named `ball` with a `<freejoint/>` and one sphere geom named `ball`. The cup is a body named `cup`; all its geoms belong to it.
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures,
  `<default>` classes or `<include>`.
- Give every body and geom a name, and write each element's attributes on a single line.
- Set `<option timestep="0.002"/>`.

Reply with the complete file in one ```xml code block. A sentence or two before the block is fine.

A ball counts as at rest when it moves slower than 5 cm/s at the end.
