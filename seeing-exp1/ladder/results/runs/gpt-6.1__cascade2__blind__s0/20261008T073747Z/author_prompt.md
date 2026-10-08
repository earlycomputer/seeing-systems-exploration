Write a MuJoCo MJCF scene for this brief:

<brief>
Use gravity 9.81 m/s2, contact friction 0.70, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, loose blocks are 0.12 m cubes and 0.35 kg, fixed ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Ball1 starts at the high end of ramp1, whose low end is 0.15 m above the floor, and rolls down to touch domino1 after a 0.10 m exit gap. Domino1 then topples across a 0.18 m center spacing and touches domino2.
</brief>

MuJoCo will load the file, reset to the keyframe named `start` if there is one, and simulate it for
6 s. Nothing else acts on the scene: whatever moves must be set moving by the scene itself, for
example by a keyframe velocity, a spring, gravity, or a motor whose control the keyframe sets (controls keep
their keyframe values for the whole run).

A few conventions so the other tools can find things. They fix names and axes, not what you build:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- Name each thing's body exactly: `ball1` (starting ramp ball: a body with a `<freejoint/>`); `ramp1` (first inclined ramp: fixed in place; all its geoms belong to one body); `domino1` (first upright domino: a body with a `<freejoint/>`); `domino2` (second upright domino: a body with a `<freejoint/>`). Its geoms may be named with the body's name as a prefix (`ball1_...`).
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures,
  `<default>` classes or `<include>`.
- Give every body and geom a name, and write each element's attributes on a single line.
- Set `<option timestep="0.002"/>`.

Reply with the complete file in one ```xml code block. A sentence or two before the block is fine.

A ball counts as at rest when it moves slower than 5 cm/s at the end.
