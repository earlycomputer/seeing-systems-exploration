The seesaw can only tip one way from level. The light ball sits at rest on the near end, which is held at the 0° stop. The 1 kg weight falls about 1.5 m onto the far end and snaps the seesaw to its 30° stop, which flings the ball upward.

A rough angular-momentum estimate gives the ball about 4 m/s off the end. That would lift it roughly 70 cm, comfortably over the 50 cm the brief asks for. This is an estimate only; I haven't run the scene.

```world
world  seesaw throw

floor
  friction  0.8, spinning 0.005, rolling 0.002

pivot
  is a  point
  at    1 m along, 40 cm up

fulcrum top
  is a  point
  at    1 m along, 38.5 cm up

fulcrum
  is a     post 6 cm square, from floor to fulcrum top
  touches  nothing
  colour   grey

-- positive turn about y tips the far end down; the 0° stop holds the ball's end up
seesaw
  is a      box 120 by 20 by 3 cm, 500 g
  colour    wood
  friction  0.8, spinning 0.005, rolling 0.002
  at        1 m along, 40 cm up
  turns on  seesaw hinge, about y, at pivot
  swings    from 0° to 30°

ball
  is a      sphere 4 cm radius, 100 g
  colour    orange
  friction  0.8, spinning 0.01, rolling 0.004
  moves     freely
  rests     on seesaw, 55 cm behind seesaw

weight
  is a      sphere 6 cm radius, 1 kg
  colour    dark grey
  bounce    dead
  moves     freely
  at        50 cm ahead of seesaw, 2 m up

expect
  weight touches seesaw
  ball touches seesaw
```

---
thinking (summarized):

I'm working out the physical setup of a seesaw with a central hinge, where a weight dropped on one end causes a ball on the opposite end to launch upward at least 50 cm — starting with the ball resting low and the weight positioned high before release.

Since a freely balanced seesaw would tip under even the ball's slight weight, I need to constrain its rotation range with hinge limits so the ball end naturally rests at a fixed low angle. I also need to add a small lip or stop at the ball's end so it doesn't roll off before the weight lands, rather than relying solely on friction.

Actually, a one-sided hinge limit (0° to 30°) could work better: the seesaw rests level with the ball end unable to dip below, so the ball just sits there until the weight lands on the opposite end and flings it upward. I should estimate whether a 1 kg weight dropped onto a light 0.5 kg, 1.2 m plank at 0.5 m radius generates enough rotational energy to launch the ball past 50 cm.

Running the numbers: moment of inertia comes out around 0.09, combined with the ball's added mass at impact gives roughly 0.34, yielding an angular velocity that translates to a ball speed near 3.6 m/s for a 1 m weight drop—enough for about 0.66 m height. But the abrupt 30° stop and gravity's deceleration during rotation complicate the real trajectory, so this estimate is rough.

I also need to check the pivot geometry: at 0.6 m arm length, a 30° swing drops the end about 0.3 m, so the pivot needs to sit at least 35 cm high to clear this. And checking rotation direction—positive rotation about the hinge axis tips the far end (where the weight sits) downward, while the ball's end would want to rotate the opposite way but gets blocked by the stop at 0°, which is the correct constraint.

For the ball's launch: dropping the weight from about 1.5 m gives it roughly 5.4 m/s at impact, transferring to about 4.4 m/s on the ball, which should be enough to reach around 1 m height after accounting for losses—good margin even with some energy loss from the soft contact limits in MuJoCo.

I should set the weight to not bounce after impact, since a harsh stop could make it ricochet unpredictably. The ball itself should stay put at rest on the level seesaw before launch, and its trajectory after being flung (slightly backward at a shallow angle) doesn't matter much since the main requirement is just clearing at least 50 cm above its starting point.

Now I'm working out the geometry of the world: a seesaw plank roughly 120×20×3 cm at 500 g, mounted on a fulcrum post positioned so the pivot sits just below the plank's center, making sure the post doesn't collide with the rotating plank as it swings.

I'm setting the fulcrum top point position and defining the post as a square column from floor to that point. For the seesaw box itself, I'm working out how to position it relative to the pivot using along/up/level-with clauses rather than fully absolute coordinates.

For the hinge, I'm naming it "seesaw hinge" turning about the y-axis at the pivot, swinging from 0° to 30°, and checking that the lower corner clears the floor by about 8.7 cm at full tilt. Then I'm placing the ball as a small sphere resting freely on the seesaw surface, positioned about 45 cm along from the pivot.

For the weight, I'm making it a 1 kg sphere with 6 cm radius, positioned about 50 cm ahead of the seesaw and roughly 2 m above the seesaw's top surface so it drops freely onto the far end when released.

Once the weight lands, the seesaw tilts to its 30° limit and the weight rolls off the far end—fine as-is, no need for extra rolling behavior on the ball. I'm checking that drop time (~0.55s) comfortably fits within the 6 second simulation, and that the seesaw's limit stop and ball placement near the rising end will naturally launch the ball upward as the plank accelerates.

Recomputing the rotational dynamics, the seesaw snaps through its 30° arc quickly (~0.065s), so gravity's contribution during that rotation is negligible. With the ball's moment of inertia and lever arm reworked, I get a launch speed around 4.4 m/s, giving a vertical component of roughly 3.8 m/s and a peak height near 0.74m—plenty of margin even accounting for imperfect energy transfer from the weight's impact. I could bump the drop height to 2m for extra margin, but 1.5m already works well.

Settling on keeping the weight drop at 2 meters for safety margin. Now I need to set up the expected end states: the ball touching the seesaw and the weight touching the seesaw.

