Write a MuJoCo MJCF scene for this brief:

<brief>
{brief}
</brief>

MuJoCo will load and simulate the file, and a separate renderer will draw it from body and geom state
alone. A person should be able to read the file and see what is where.

A few conventions so the other tools can find things. They fix names and axes, not what you build:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- The ball is a body named `ball` with a `<freejoint/>` and exactly one sphere geom, also named `ball`.
  At t = 0 it rests on the floor with its center at x = 0, y = 0.
- The hoop is a body named `hoop` whose origin is the center of the rim. Every rim geom is named with the
  prefix `rim`. The backboard is a geom of the `hoop` body, so it moves with the hoop. The rim center lies
  on the +x axis from the ball (y = 0).
- Any support for the hoop is a separate body with a descriptive name.
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures, or
  `<default>` classes, and no `<include>`.
- Give every body and geom a name, and write each element's attributes on a single line.
- Set `<option timestep="0.002"/>`.

Reply with the complete file in one ```xml code block. A sentence or two before the block is fine.
