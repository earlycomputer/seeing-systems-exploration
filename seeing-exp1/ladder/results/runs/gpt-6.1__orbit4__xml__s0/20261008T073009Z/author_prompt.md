Write a MuJoCo MJCF scene for this brief:

<brief>
Use gravity 9.81 m/s2, contact friction 0.68, restitution 0.05, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, blocks are 0.12 m cubes and 0.35 kg, ramps are 0.95 m long and 0.30 m wide at 19 degrees, and horizontal rings have 0.16 m clear diameter. Pendulum1 is a 0.55 m long, 0.40 kg rigid pendulum released 55 degrees left of vertical, and it swings clockwise to touch ball1 at the high end of ramp1. Ball1 rolls down ramp1, whose low end is 0.15 m above the floor, crosses a 0.12 m gap, and touches cart1. Cart1 slides 0.40 m along its horizontal slide and touches domino1. Domino1 topples 0.18 m into flap1, a 0.40 by 0.20 by 0.04 m, 0.30 kg panel, making flap1 swing clockwise through 65 degrees to its hard stop and knock ball2 at the high end of ramp2.
</brief>

MuJoCo will load the file, reset to the keyframe named `start` if there is one, and simulate it for
8 s. Nothing else acts on the scene: whatever moves must be set moving by the scene itself, for
example by a keyframe velocity, a spring, gravity, or a motor whose control the keyframe sets (controls keep
their keyframe values for the whole run).

A few conventions so the other tools can find things. They fix names and axes, not what you build:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- Name each thing's body exactly: `pendulum1` (starting pendulum: a body on a hinge joint); `ball1` (first ramp ball: a body with a `<freejoint/>`); `ramp1` (first inclined ramp: fixed in place; all its geoms belong to one body); `cart1` (first slide cart: a body on a slide joint); `domino1` (first upright domino: a body with a `<freejoint/>`); `flap1` (first striking flap: a body on a hinge joint); `ball2` (second ramp ball: a body with a `<freejoint/>`); `ramp2` (second inclined ramp: fixed in place; all its geoms belong to one body). Its geoms may be named with the body's name as a prefix (`pendulum1_...`).
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures,
  `<default>` classes or `<include>`.
- Give every body and geom a name, and write each element's attributes on a single line.
- Set `<option timestep="0.002"/>`.

Reply with the complete file in one ```xml code block. A sentence or two before the block is fine.

A ball counts as at rest when it moves slower than 5 cm/s at the end.
