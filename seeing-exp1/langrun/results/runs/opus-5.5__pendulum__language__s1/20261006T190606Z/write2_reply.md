The duplicate joint seems to come from the rod `attached to` the hinged bob: the compiler appears to emit the hinge once for each thing in the group. To avoid this, the pendulum is now a single thing with nothing attached. It is a heavy 4 cm thick rod, 1.2 kg, hanging from the pivot. Its rounded lower end hangs 7.5 cm behind the ball's centre, at 6 cm height, which leaves a 5 mm gap.

It starts swung back 40°. That gives the tip about 1.85 m/s at the bottom of the swing, with an effective striking mass of about 0.4 kg. The ball should leave rolling at roughly 1–2 m/s, enough to hop the cup's 1.5 cm lip.

```parts
part low cup
  needs  length
  needs  width
  needs  walls
  needs  lip height
  needs  wall thickness, else 1 cm
  needs  base thickness, else 2 mm

  base
    is a  box length by width by base thickness
    on    floor
  near wall
    is a  box wall thickness by width by lip height
    on    floor, centred on base's near end
  far wall
    is a    box wall thickness by width by walls
    on      floor, centred on base's far end
    bounce  dead
  left wall
    is a    box length by wall thickness by walls
    on      floor, centred on base's left side
    bounce  dead
  right wall
    is a    box length by wall thickness by walls
    on      floor, centred on base's right side
    bounce  dead
```

```world
world  pendulum knocks a ball into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.001

ball
  is a      sphere 5 cm radius, 100 g
  rolls
  friction  0.8, spinning 0.005, rolling 0.001
  colour    orange
  moves     freely
  rests     on floor, 1 m along

pivot
  is a  point
  at    7.5 cm behind ball, 56 cm up

pendulum foot
  is a  point
  at    7.5 cm behind ball, 6 cm up

-- one heavy rod, pivoted at its top; its rounded lower end hangs 5 mm short of the ball
pendulum
  is a           rod 4 cm thick, from pivot to pendulum foot
  weighs         1.2 kg
  colour         grey
  turns on       swing, about y, at pivot
  starts turned  40°

stand beam
  is a    box 4 by 16 by 4 cm
  colour  wood
  at      7.5 cm behind ball, 12 cm to the left, level with pivot

stand post
  is a    box 4 by 4 by 58 cm
  colour  wood
  stands  on floor, 7.5 cm behind ball, 22 cm to the left

cup
  is a         low cup
  length       20 cm
  width        20 cm
  walls        10 cm
  lip height   1.5 cm
  its base 1 m beyond ball

expect
  ball touches pendulum
  ball comes to rest in cup
```

---
thinking (summarized):

I'm puzzling over why the joint seems duplicated regardless of naming — maybe the rod attached to the pendulum is inheriting the same joint declaration as the bob, so the compiler ends up emitting it twice for the same body.

To work around it, I consider simplifying: drop the separate bob entirely and make the pendulum a single rod/capsule with mass concentrated for a desired effective inertia. I'm running the physics — using rotational energy conservation to estimate tip speed at a 45° swing, getting around 2.07 m/s with an effective mass near 0.4 kg, and now thinking about adjusting the rod's mass and length to tune that result.

Pivot sits 56 cm up with rod extending down to 6 cm, giving a 50 cm rod length with the foot positioned 7.5 cm behind the ball. I'm checking whether the rod's capsule geometry at the pivot and the beam clearance still work out fine, then turning to the rod's mass spec of 1.2 kg.

Checking the elastic and inelastic collision numbers for the ball at 40° still line up reasonably well, so I'll keep that angle and stick with naming the hinge `swing`.

