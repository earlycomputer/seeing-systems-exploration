Write a MuJoCo MJCF scene for this brief:

<brief>
Use gravity 9.81 m/s2, contact friction 0.72, restitution 0.04, hinge damping 0.04 N m s/rad, and slide damping 0.20 N s/m; start every body from rest. Balls are 0.10 m diameter and 0.20 kg, dominoes are 0.08 by 0.04 by 0.24 m and 0.25 kg, carts are 0.22 by 0.18 by 0.10 m and 0.50 kg, blocks are 0.12 m cubes and 0.35 kg, ramps are 1.00 m long and 0.30 m wide at 20 degrees, and horizontal rings have 0.16 m clear diameter. Ball1 starts 0.30 m above ring1 and drops vertically through it. Ball1 falls another 0.25 m and touches the left end of lever1, a 0.60 by 0.10 by 0.04 m, 0.50 kg center-hinged lever. Lever1 rotates clockwise through 45 degrees to its lower stop, and its rising right end knocks cart1 along a horizontal slide. Cart1 slides 0.42 m and touches domino1. Domino1 topples across a 0.18 m spacing and touches ball2 at the high end of ramp1. Ball2 rolls down ramp1, whose low end is 0.15 m above the floor, crosses a 0.10 m gap, and touches door1. Door1, a 0.42 by 0.32 by 0.04 m, 0.45 kg panel, swings clockwise through 70 degrees to its hard stop and strikes pendulum1. Pendulum1, a 0.50 m long, 0.35 kg rigid pendulum, swings clockwise through 38 degrees and touches block1. Block1 slides 0.35 m across the floor and touches cart2. Cart2 slides 0.42 m and touches the left end of seesaw1, a 0.65 by 0.10 by 0.04 m, 0.55 kg center-hinged beam carrying ball3 on its right end. Seesaw1 rotates clockwise through 42 degrees to its lower stop and launches ball3 vertically from its rising right end. Ball3 rises and then drops through ring2, centered 0.32 m below its initial center. Ball3 falls another 0.24 m and touches domino2. Domino2 topples across a 0.18 m gap and touches flap1, a 0.38 by 0.18 by 0.04 m, 0.28 kg hinged panel. Flap1 swings clockwise through 60 degrees to its hard stop and knocks ball4 from shelf1, a fixed 0.30 by 0.25 by 0.04 m shelf 0.55 m above cup1. Ball4 falls into cup1, whose inner footprint is 0.30 by 0.30 m with 0.20 m high and 0.02 m thick walls, and comes to rest there.
</brief>

MuJoCo will load the file, reset to the keyframe named `start` if there is one, and simulate it for
20 s. Nothing else acts on the scene: whatever moves must be set moving by the scene itself, for
example by a keyframe velocity, a spring, gravity, or a motor whose control the keyframe sets (controls keep
their keyframe values for the whole run).

A few conventions so the other tools can find things. They fix names and axes, not what you build:

- SI units. z is up. The floor's top surface is at z = 0, and the floor is a plane geom named `floor`.
- Name each thing's body exactly: `ball1` (starting falling ball: a body with a `<freejoint/>`); `ring1` (first horizontal ring: fixed in place; all its geoms belong to one body); `lever1` (cart striking lever: a body on a hinge joint); `cart1` (first slide cart: a body on a slide joint); `domino1` (first upright domino: a body with a `<freejoint/>`); `ball2` (ramp ball: a body with a `<freejoint/>`); `ramp1` (inclined ramp: fixed in place; all its geoms belong to one body); `door1` (pendulum striking door: a body on a hinge joint); `pendulum1` (block striking pendulum: a body on a hinge joint); `block1` (pendulum struck block: a body with a `<freejoint/>`); `cart2` (second slide cart: a body on a slide joint); `seesaw1` (ball launching seesaw: a body on a hinge joint); `ball3` (launched falling ball: a body with a `<freejoint/>`); `ring2` (second horizontal ring: fixed in place; all its geoms belong to one body); `domino2` (second upright domino: a body with a `<freejoint/>`); `flap1` (final striking flap: a body on a hinge joint); `ball4` (final catch ball: a body with a `<freejoint/>`); `shelf1` (ball support shelf: fixed in place; all its geoms belong to one body); `cup1` (final catch cup: fixed in place; all its geoms belong to one body). Its geoms may be named with the body's name as a prefix (`ball1_...`).
- Only primitive geom types: plane, sphere, capsule, cylinder, box, ellipsoid. No meshes, textures,
  `<default>` classes or `<include>`.
- Give every body and geom a name, and write each element's attributes on a single line.
- Set `<option timestep="0.002"/>`.

Reply with the complete file in one ```xml code block. A sentence or two before the block is fine.

A ball counts as at rest when it moves slower than 5 cm/s at the end.
