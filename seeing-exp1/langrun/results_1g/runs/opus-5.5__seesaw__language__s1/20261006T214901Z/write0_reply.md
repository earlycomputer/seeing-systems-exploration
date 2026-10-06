The seesaw rests with its ball end down against a stop, and a lip keeps the ball from rolling off. The 1 kg weight falls about 1.6 m onto the high end, so it hits at about 5.5 m/s. That swings the arm up to its other stop and throws the ball.

By momentum about the pivot, the ball end should leave at roughly 4 m/s or more. That is enough to clear 50 cm with a comfortable margin, but it is an estimate I haven't run.

```world
world  seesaw throw

floor
  friction  0.8, spinning 0.005, rolling 0.002

fulcrum
  is a    box 4 by 20 by 26 cm
  stands  on floor
  colour  grey

pivot
  is a  point
  at    30 cm up

seesaw
  is a           box 100 by 12 by 2 cm, 300 g
  at             0 m along, level with pivot
  turns on       seesaw pivot, about y, at pivot
  swings         from -20° to 10°
  starts turned  10°
  bounce         dead
  colour         wood

lip
  is a         box 2 by 12 by 4 cm, 10 g
  on           seesaw, at seesaw's far end
  attached to  seesaw
  colour       wood

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  moves     freely
  on seesaw, 45 cm ahead of seesaw
  colour    orange

weight
  is a      sphere 6 cm radius, 1 kg
  bounce    dead
  moves     freely
  45 cm behind seesaw, 2 m up
  colour    dark grey

expect
  weight touches seesaw
  ball touches seesaw
```

---
thinking (summarized):

I'm picturing a seesaw design: a 1-meter plank on a central pivot, with the ball end resting down and the weight end raised. Dropping the 1 kg weight from some height onto the raised end should pivot the plank and launch the 100 g ball upward, so I need to work out the mass ratio and drop height required to get the ball at least 50 cm into the air.

Working through the angular momentum: using a light plank (~300 g) with the weight impacting at the far end, I calculate the resulting angular velocity and the ball's launch speed — needing roughly 5.4 m/s, implying a drop height around 1.5 m, with the ball accelerating as the plank rotates until it hits its stop and releases the ball.

Now I'm setting the geometry: pivot height 20 cm, half-length 50 cm, swing range ±20°, ball at the far end (+x) and weight dropping on the near end (−x), starting tilted +20° so the weight's impact rotates the plank negative and flings the ball upward until the −20° stop.

But I realize if positions are set before the tilt is applied, the ball placed at the far end of the unturned seesaw will end up sitting on a 20°-sloped surface once the tilt kicks in — it would just roll off the edge. I need some kind of lip, cup, or small attached wall at the far end to actually hold the ball in place before launch.

Okay, so the seesaw rests at +10° (far end down) initially, ball rolls down to the lip, then the weight drop hits the near end and drives rotation to −20°, a 30° total swing. The ball rises about 0.26m during contact before launching, and when the plank hits the −20° stop, the ball's velocity is perpendicular to the arm — pointing up and slightly backward (−x direction), with vertical component roughly cos20° ≈ 0.94 of total speed.

I should check the ball doesn't clip the weight or the lip on its way out — the weight sits low near the pivot and the lip is beyond the ball along the plank, so the trajectory should clear both. Sizing the ball (~3cm radius, ~880 density for 100g) and the weight (~6cm radius, ~1105 density for 1kg) seems physically reasonable, and MuJoCo's hinge limit stops should handle the momentum transfer adequately even though they're somewhat soft.

Since the weight keeps accelerating under gravity throughout the rotation while the ball end decelerates, the net torque favors continued push — gravity torque from the weight (1kg × 9.81 × 0.5) dominates over the ball's resistance (0.1kg × 9.81 × 0.5), so the ball should exit at roughly 83% of the weight's contact velocity. To hit a target ball speed of 4 m/s, I need contact velocity around 4.8 m/s, meaning a drop height near 1.2-1.5m for the weight's center above the near end, factoring in the ball's own 0.26m rise during contact as part of the total 50cm displacement.

Now I'm placing the weight precisely on the plank given the 10° tilt — accounting for the horizontal offset from the pivot so it sits correctly behind the seesaw's center, roughly 40-45cm back, with an appropriate drop height like 1.6m, and no lateral offset. I'm also specifying the seesaw's own dimensions: a 100×12×2cm box weighing 300g.

I still need to define the fulcrum supporting the pivot — a fixed post or box on the floor under the plank's center, roughly 30cm tall. I'm checking clearances: when the plank rotates to 20°, its underside near the edges dips down toward the fulcrum top, and I need to narrow the fulcrum so the corners don't collide with it during rotation.

Then I'll verify the plank's far and near ends don't hit the floor at the extreme tilt angles (+10° and -20°), confirming both clear with margin. Finally I'm adding a small lip block (2x12x4 cm, 10g) positioned on the seesaw near its edge.

Now I'm working out the exact positioning syntax for the seesaw relative to the fulcrum, and naming its hinge as the pivot about which it turns.

For the ball: a 3cm, 100g sphere placed on the seesaw offset along the plank, initially resting at the level position before the seesaw tilts 10°, causing the plank surface to drop and the ball to roll down toward the lip, settling against it with possible small bounces as the counterweight falls 1.6m.

The impact radius comes out close to 0.45 rather than 0.5, so the angular effect is slightly reduced, consistent with the ball's position. With the weight dropping from 1.5 m to the near end (~0.39 m), that's roughly a 1.05 m fall giving ~4.5 m/s, translating to ball speed near 3.7 m/s — raising the drop height to 2 m instead bumps that up to about 5.5 m/s, which seems better for the effect I want. I'll set up the scene so the ball and weight both visibly touch the seesaw at their respective ends.

I'll keep the hinge simple — seesaw as a box pivoting on an arm with no extra damping — and just build the structure directly.

