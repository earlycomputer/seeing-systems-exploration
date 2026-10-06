The seesaw starts flat, held level by a rest block under the end that carries `ball`. `weight` falls about 1.28 m onto the other arm, 40 cm from the pivot. That end drives down to the hinge stop at −15° and flicks `ball` upward.

**Rough estimate.** This assumes a dead, plastic hit and ignores the rest of the travel.
- `weight` lands at about 5.0 m/s.
- The seesaw's inertia about the pivot is about 0.21 kg·m². That gives it about 9.5 rad/s, so `ball` leaves at about 4.3–4.8 m/s.
- `ball` should rise about 1 m above its starting height of 19.5 cm, well above the 50 cm needed.

**Caveat.** I haven't run this in MuJoCo, so the figures are a hand estimate.
- One assumption is that the positive hinge angle lowers the far end. If MuJoCo's sign convention is the reverse, the range should be flipped to `from −10° to 15°`.
- The `on seesaw` placement for `ball` is also untested.

```world
world  seesaw throw

floor
  friction  0.8, spinning 0.005, rolling 0.002

pivot
  is a  point
  at    1 m along, 15 cm up

fulcrum
  is a    box 6 by 20 by 12 cm
  stands  on floor, 1 m along
  colour  grey

rest block
  is a    box 10 by 20 by 13.5 cm
  stands  on floor, 1.45 m along
  colour  dark grey

seesaw
  is a      box 100 by 20 by 3 cm, 300 g
  1 m along, level with pivot
  turns on  seesaw hinge, about y, at pivot
  swings    from −15° to 10°
  damping   0.01 N·m·s/rad
  friction  0.8
  colour    wood

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  rests     on seesaw, 45 cm beyond pivot

weight
  is a      sphere 5 cm radius, 1 kg
  bounce    dead
  friction  0.8
  colour    black
  moves     freely
  40 cm behind pivot, 1.5 m up

expect
  weight touches seesaw
```

---
thinking (summarized):

I'm sketching out the physical design of a seesaw: a hinged plank with a pivot height, where a 1 kg weight drops on one end to launch a 100 g ball at least 50 cm into the air off the other end, and working through plausible dimensions and mass for the board.

Now I'm reasoning through the rotation mechanics—naming the hinge, setting a starting tilt angle with the ball's end down and weight's end up, and carefully tracking the sign convention for rotation about the y-axis so the lowered end matches where the ball should sit. I'm also catching a subtlety: if object positions are defined relative to the board's unturned geometry, starting the seesaw "turned" could cause the ball to clip through or float above the surface, so I need to adjust where the ball is placed to account for the initial tilt.

Then I'm estimating the physics of the launch: a weight dropped onto the near end from some height, colliding with the board (treated as a plastic collision using angular momentum about the pivot, factoring in the board's and ball's moments of inertia), causing the far end to swing up and launch the ball. I'm working out the resulting angular velocity and torque balance (gravity helping on the weight side, opposing on the ball side) to estimate the ball's launch speed once the board hits its rotational limit.

With L=0.5m, a 1 m, 0.3 kg board, and a 1 kg weight, I calculate the board's angular velocity from the collision, then the ball's launch speed as roughly 0.833 times the weight's impact velocity. To get the ball to rise about 0.5 m, I need a launch speed near 4 m/s (with some margin), which means the impact velocity needs to be about 4.8 m/s, implying a drop height around 1.17 m — then I start factoring in the extra boost from gravity acting on the weight during the board's swing.

Trying a drop height of 1.5 m instead gives an impact velocity of 5.42 m/s, producing a ball speed near 4.5 m/s and a rise of about 1.03 m, which gives comfortable margin. I need to be careful about what "above where it started" means for the ball, and about how the ball's velocity direction tilts slightly toward the pivot as the board rotates up to angle θ. I also need to check that the hinge's range of motion actually permits the far end to swing upward as required.

I'm checking clearance limits: with pivot height 15 cm and arm length 0.5 m, the near end would hit the floor around a 15.6° swing, so I'll cap the hinge range at ±15° and verify the board's thickness still clears the floor at that angle, which comes out to about 0.6 cm of clearance.

But I realize a problem—nothing holds the far end flat initially, so a ball sitting there would tip the board before the dropped weight even arrives. I'm thinking the fix is to add a small support block under the far end so the board starts resting flat; once the weight lands on the near end, the far end lifts off the support naturally, and I can pair this with a hinge limit so it only swings between -15° and 0°.

Moving the arm to 0.4m reduces leverage slightly but still gives good momentum: total inertia ~0.21, angular speed ~1.9×v0, ball exit speed ~0.95×v0. Dropping from 1.5m gives v0≈5.4, ball speed ~5 m/s, rotating 15° in about 26ms before hitting the hinge stop — plenty of margin for the ball to clear the board. I need to double check the weight's behavior on impact to avoid an unrealistic dead bounce.

Now I'm working out the ball's starting height and trajectory: center begins at 19.5cm and needs to rise past 69.5cm, which checks out fine. I'm figuring out the board's dimensions and mass (a 100×20×3cm box at 300g) and how to position it centered over the pivot in the seesaw setup.

For the pivot itself, I'm defining it as a point 1 meter along and 15cm up, then positioning the board level with that pivot. I'm also adding a small fixed box as the fulcrum stand under the pivot — 6×20×12cm on the floor — checking that the gap leaves enough clearance for the board to tilt without the fulcrum interfering.

Now I'm placing a rest block under the far end of the board (10×20×13.5cm, 1.45m along) with its top matching the board's resting height, and loosening the hinge rotation range to -15° to 10° so the block can catch it. Then I'm adding the weight — a 5cm radius sphere, 1kg, positioned about 40cm behind the pivot and 1.5m up — working out the drop height and resulting impact velocity to make sure the motion looks right.

Finally, I'm adding a small ball (3cm radius, 100g, rolling, resting on the seesaw) 45cm beyond the pivot on the opposite side, letting it sit at the seesaw's default height. I'm noting the weight may bounce after impact and should have friction against the seesaw surface, then writing everything up.

