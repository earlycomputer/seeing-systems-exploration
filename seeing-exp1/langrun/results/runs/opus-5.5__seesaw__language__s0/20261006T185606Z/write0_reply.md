The seesaw rests level on its upper hinge stop, so the 100 g ball sits still on the far end. The 1 kg weight falls about 1.7 m onto the near end, which swings down 20° to the lower stop and throws the ball.

**Hand estimate (not a run):**
- The weight lands at about 5.8 m/s.
- Treating the hit as dead (no bounce) and keeping angular momentum, the far end takes off at about 4.6 m/s.
- That rough figure would carry the ball well over 50 cm.
- I have not simulated this. The stated `expect` lines only check that the weight hits the seesaw and the seesaw reaches its lower stop. They do not measure the ball's height.

```world
world  seesaw throw

floor
  friction  0.8, spinning 0.005, rolling 0.002

pivot
  is a  point
  at    1 m along, 30 cm up

stand top
  is a  point
  at    1 m along, 24 cm up

stand
  is a    post 6 cm square, from floor to stand top
  colour  grey

seesaw
  is a      box 120 by 10 by 3 cm, 300 g
  at        1 m along, level with pivot
  turns on  seesaw hinge, about y, at pivot
  swings    from −20° to 0°
  colour    wood

ball
  is a      sphere 4 cm radius, 100 g
  friction  0.8, spinning 0.01, rolling 0.004
  moves     freely
  colour    orange
  rests     on seesaw, 50 cm beyond pivot

weight
  is a      sphere 6 cm radius, 1 kg
  bounce    dead
  moves     freely
  colour    dark grey
  at        50 cm behind pivot, 2 m up

expect
  weight touches seesaw
  seesaw reaches its lower stop
```

---
thinking (summarized):

I'm working out the seesaw physics: a plank pivoting at center, with a 1 kg weight dropped on one end to launch a 100g ball off the other end at least 50cm high, which requires launch speed around 3.13 m/s with some safety margin, so I'm calculating the drop height and arm lengths needed to achieve that transfer.

Calculating moments of inertia, I find a drop height around 2m gives the ball enough speed through the collision, though I'm considering that the seesaw stopping abruptly when the weight end hits the floor is actually what launches the ball. I'm also considering starting the seesaw pre-tilted with the weight end raised and the ball end resting on the floor, so dropping the weight directly rotates the plank and flings the ball upward.

Working out the geometry now: pivot height roughly 20cm, half-length 0.6m giving a tilt angle near 19.5 degrees, and setting joint limits so the plank stops abruptly at that angle to release the ball. I'm sizing the plank itself at 120cm long, 10cm wide, 3cm thick, around 300g, with the pivot positioned accordingly.

I'm figuring out rotation direction around the y-axis — a positive angle about y moves the +x end downward, so starting the seesaw turned 15 degrees should tilt it in the direction I want.

Actually, simpler to keep the seesaw level initially, placing the ball on the far end and the weight on the near end, then letting rotation happen naturally: near end down corresponds to a negative angle, so I'll set the range to -20° to 20°, start flat at 0°, and make sure the pivot height (30 cm) is tall enough that the ends don't hit the floor before reaching the rotation limit.

Now I'm thinking about whether to add a support post beneath the pivot, but realize the post geometry needs to clear the plank as it rotates, so I need to work out the right height and clearance for the post so it doesn't collide with the plank's underside at the pivot point.

I also realize the physics works out naturally without needing a preset tilt: since the ball sits on one end with nothing counterbalancing it yet, that end will simply sink under its own weight to the rotation limit before the falling weight even arrives, which actually sets up the seesaw correctly for the weight to land on the raised end.

Actually, simpler: constrain the hinge range to -20° to 0°, so the seesaw rests level with the ball sitting still on the far end, blocked at its upper limit. Then the dropped weight pushes the near end down, swinging the far end up to -20° and launching the ball — no lip needed since the ball never has to roll while the plank is tilted.

Now I'm sizing the weight sphere and working out its fall speed: dropping from 2 m to about 0.3 m gives roughly 5.8 m/s on impact. Then I recompute the seesaw's moment of inertia with plank, ball, and weight all included, getting about 0.311, which gives an angular velocity near 9.3 rad/s and a resulting ball launch speed around 4 m/s.

Checking the ball's motion on the plank as it rotates 20°, the normal force keeps it sliding outward along the plank rather than staying fixed, since the ball tends to travel straight while the plank rotates beneath it. At the point of release the ball exits around 4.5 m/s, angled about 20° from vertical, moving up and inward toward the pivot side given the rotation direction.

The vertical rise from that exit speed comes out to roughly 0.9 m, which gives plenty of margin even accounting for energy losses, so I'll set the weight's bounce to be dead/inelastic to avoid a seesaw rebound, while leaving the ball's bounce at default. I'll also check that the hinge limit at -20° stops the plank abruptly and that MuJoCo's default limit stiffness is sufficient here.

For the scene setup, I'm placing the stand post under the stand-top point to support the seesaw's pivot, with the plank mass defined via its box spec, and keeping the floor plain. I'll define the final expected contact events simply, like "weight touches seesaw," matching the style of prior examples.

Now I'm working out positions precisely: the pivot sits 1 m along and 30 cm up, the seesaw plank is 3 cm thick so its top surface is at 31.5 cm, and the ball (4 cm radius, 100 g) rests on the seesaw 50 cm beyond the pivot while the weight sits 50 cm behind the pivot at an absolute height of 2 m. Since the plank is level, I don't think the ball needs a rolling behavior added.

