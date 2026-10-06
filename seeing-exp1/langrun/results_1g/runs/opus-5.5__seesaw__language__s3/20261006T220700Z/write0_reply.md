The seesaw is a light board pivoting at its centre. Its hinge only lets it tip so the ball's end rises, and it rests level at the start. The 1 kg weight falls about 1.4 m onto the near end. The board swings 25° to its stop, and the 100 g ball on the far end flies on.

**Rough check, assuming the weight sticks rather than bounces:**
- The weight lands at about 5.3 m/s.
- Angular momentum about the pivot gives the board about 10 rad/s.
- At 44 cm from the pivot, that is about 4.4 m/s at the ball.
- The upward part of that is about 4 m/s, enough for roughly 0.8 m of climb.
- The ball's end has already risen about 20 cm by the time the board stops.
- Together that is well over the 50 cm the brief asks for.

**What the `expect` block can and cannot check:**
- It checks that the weight hits the seesaw and the seesaw reaches its stop.
- It checks that the ball touches the floor, which only says the ball came off the board.
- None of the language's expectation forms can state the 50 cm height. That has to be read off the ball's track in the run.

```world
world  seesaw throw

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

pivot
  is a  point
  at    1 m along, 35 cm up

stand top
  is a  point
  at    1 m along, 30 cm up

stand
  is a  post 6 cm square, from floor to stand top
  colour  grey

seesaw
  is a      box 100 by 20 by 4 cm, 300 g
  colour    wood
  friction  0.8
  1 m along, level with pivot
  turns on  seesaw hinge, about y, at pivot
  swings    from -25° to 0°
  damping   0.02 N·m·s/rad

ball
  is a      sphere 4 cm radius, 100 g
  colour    orange
  friction  0.8, spinning 0.01, rolling 0.004
  rolls
  moves     freely
  on seesaw, 44 cm beyond seesaw

weight
  is a      sphere 6 cm radius, 1 kg
  colour    dark grey
  bounce    dead
  moves     freely
  44 cm behind seesaw, 1.5 m above seesaw

expect
  weight touches seesaw
  seesaw reaches its lower stop
  ball touches floor
```

---
thinking (summarized):

I'm designing a seesaw mechanism: a pivoted plank with a weight dropped on one end to launch a lighter ball on the other end at least 50 cm high, which means calculating the required launch velocity (~3-4 m/s with margin) based on energy transfer between the 1 kg weight and 100 g ball.

I work through the collision physics using angular momentum about the pivot—accounting for the board's moment of inertia, both masses, and the lever arm—to find that a drop height of about 1.3 m gives enough speed. I'm also setting up a rotation limit (roughly ±15°) so the board stops abruptly and flings the ball free once it reaches that angle.

I'm figuring out the hinge geometry: pivot height, how far each end dips below the resting position at 15°, and the sign convention for rotation about the y-axis so I know which direction corresponds to the ball launching upward.

A sphere resting on a tilted board would just roll off, so I need a lip or small stop block at the far (low) end to hold the ball in place before launch. When the board rotates, that end swings upward, flinging the ball off at an angle—though I'm also considering just starting the board level to simplify things.

Starting level at 0° avoids needing a lip, since the ball sits stably without rolling. The weight drops onto the near end, driving the rotation negative until it hits a stop at -25°, flinging the ball off the far end while it was resting steadily at 0° until impact.

I'm sketching rough dimensions: pivot height near 35 cm, board around 1 m long, 4 cm thick, 20 cm wide, with a roughly 1 kg weight (treating it as a dense sphere, maybe steel, radius ~5 cm).

I'm lightening the board to about 300 g and checking that the pivot limit at 0° still works with the ball resting near the far end. For the drop mechanism, I'm estimating the falling weight hits around 5.4 m/s from a 1.5 m drop, then computing the board's moment of inertia and the weight's contribution at its attachment radius to see how the impact transfers angular momentum into the launch.

Working through the numbers, I get an angular velocity near 9.8 rad/s, giving the ball a launch speed around 4.4 m/s — enough to reach roughly 1 m of height, which gives decent margin. I'm now double-checking whether the contact is stiff enough for the ball to actually reach that full transferred speed before the board rotates too far.

Then I move on to positioning: the board is a 100×20×4 cm, 300 g seesaw pivoting about its center, and I'm working out how to specify its location relative to the pivot point using "level with" and "along" placement so it sits correctly on the hinge.

For the support, I need a fixed post under the pivot, but it must avoid colliding with the rotating board's underside as it tilts, so I'm figuring out a point slightly below the pivot height to anchor the post's top without intersecting the board's swept geometry near center.

For the ball, I'm placing a 4 cm radius sphere weighing 100 g resting on the seesaw's board, positioned 45 cm forward from the seesaw's center, keeping the lateral offset at default so it sits near the board's edge.

For the weight, I'm using a 6 cm radius sphere weighing 1 kg that falls freely, positioned 44 cm behind the seesaw and 1.5 m above the board center — working out it ends up dropping about 1.42 m before impact, giving an impact speed around 5.3 m/s, which seems like a reasonable bounce. I'm leaving damping minimal or optional since it's not a strict requirement.

Tracking the ball's launch: with the board tipping at roughly -25°, the end velocity gives the ball a lateral component back toward the pivot of about -1.9 m/s and a vertical kick near 4 m/s, sending it up to roughly 1 m before arcing back over the weight's position without a collision. I'm trying to match the event vocabulary available — things like "touches," "comes to rest," "drops through," "reaches" — to describe outcomes like the ball landing back on the board or settling somewhere, since a precise "rises by 50 cm" phrasing isn't really expressible in this format.

I'm considering "seesaw reaches its lower stop" to describe the board hitting -25°, and noting the ball will also touch the floor eventually. Friction on the ball should be fine with default settings, and the floor spans 6 meters.

