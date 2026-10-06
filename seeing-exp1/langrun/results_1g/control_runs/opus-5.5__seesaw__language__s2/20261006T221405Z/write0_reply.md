The seesaw is a 2 m board on a hinge 40 cm up. Its hinge range stops it level, so the 100 g `ball` rests still on the far end. The 1 kg `weight` falls about 2 m onto the near end and drives that end down. When the board hits its −20° stop, the far end stops and the ball flies on.

Rough estimate, taking the weight as sticking to the board and with the hinge 90 cm from each ball:
- **Weight at impact:** about 6.3 m/s.
- **Board after impact:** about 5.4 rad/s, so the far end moves at about 4.8 m/s.
- **Ball's rise:** about 1 m above its start, double the 50 cm the brief asks for. This is a hand estimate; I haven't run it.

Two things could change the result in the run:
- The ball leaves tilted about 20° back toward the pivot, so it may come down on the board or the weight. That doesn't affect the height it reaches.
- The stand stops 2 cm short of the board so it can't jam the hinge, which leaves the hinge alone to hold the board.

```world
world  seesaw throw

floor
  friction  0.8, spinning 0.005, rolling 0.002

pivot
  is a  point
  at    40 cm up, 1 m along

stand top
  is a  point
  at    36 cm up, 1 m along

stand
  is a    post 4 cm square, from floor to stand top
  colour  grey

seesaw
  is a      box 200 by 10 by 4 cm, 500 g
  colour    wood
  at        1 m along, level with pivot
  turns on  seesaw hinge, about y, at pivot
  swings    from −20° to 0°
  armature  0.001 kg·m²

ball
  is a      sphere 4 cm radius, 100 g
  colour    orange
  rolls
  friction  0.8, spinning 0.01, rolling 0.004
  moves     freely
  rests     on seesaw, 90 cm beyond pivot

weight
  is a      sphere 5 cm radius, 1 kg
  colour    dark grey
  bounce    dead
  moves     freely
  at        90 cm behind pivot, 2.5 m up

expect
  weight touches seesaw
  ball touches seesaw
```

---
thinking (summarized):

I'm sketching the physical setup for a seesaw mechanism: a pivoted plank with a weight dropped on one end to launch a ball off the other end, and I need to work out the dimensions and masses so the ball rises at least 50 cm.

Working through the angular momentum transfer: if I drop a 1 kg weight from roughly 2.5 m above the near end at ~7 m/s, the collision impulse against the board (with inertia from its own mass plus the ball) should swing the far tip at nearly 5 m/s, sending the ball up about 1.2 m — comfortably past the 50 cm requirement. I'm also noting that once the near side hits the floor, the board's rotation stops abruptly, but the ball keeps flying upward from the momentum it already gained.

A lighter board, maybe 0.5 kg, could simplify things. I'm now setting up the actual geometry: pivot at 30 cm height, board 2 m long split evenly across it, and a tilt angle of about 17.5° needed for the far end to touch the floor, giving a rotation range of roughly ±17°. Working out the sign convention for rotation about the y-axis, I determine that a positive angle corresponds to the near end rising and the far end dropping — so the board should start tilted at about 15° in that positive direction before swinging through the collision.

Checking the numbers, at 15° tilt the far end only drops to about 0.02 m above the floor, so it's actually the joint's range limit that halts the swing rather than contact with the ground — bumping the pivot height to 35 cm would give more margin. I also need to make sure the ball's starting position matches the board's initial tilt, since the ball is a separate free body that must be placed correctly on the already-rotated board surface rather than on the flat, untilted version.

Thinking about physics realism, a ball resting on a 15° slope would simply roll off, so I'd need some kind of lip or cup at the far end to keep it in place, or reconsider having the board start level instead. If it starts level with the ball's weight unopposed, the near end would dip down, which actually matches the natural resting position for an unbalanced seesaw — so starting at the far-end-down limit might be the physically correct equilibrium, provided I add something to keep the ball from sliding off the incline.

Actually the far end naturally rests against the upper limit at 0° since the ball makes that side heavier, holding it level until the weight hits the near end and rotates it down to the -20° stop. That means the ball sits on a level board the whole time, so I don't need to worry about tilt calculations for its resting position — simpler than I thought. When the board stops at -20°, the far tip's velocity will be perpendicular to the board at that angle, which determines the ball's launch direction.

I also need to check geometry so the near end doesn't clip the floor at the -20° stop: with a 1m arm and the pivot raised to 40cm, the near end drops about 0.342m, landing around 0.04m above the floor, which should be fine.

For the weight drop, I'm positioning it centered over the near end (around x=-0.9) with the ball on the far end (x=+0.9), dropping from roughly 2-2.5m height so it hits with around 5.6-6.3 m/s. Sizing the weight sphere at roughly 5cm radius and the ball at 4cm, 100g, then estimating the board's moment of inertia (I≈0.167 for a 0.5kg, 2m board) to work out the resulting angular momentum from the impact.

Adding the weight's moment contribution (1*0.81) and the ball's (0.081), giving total inertia ~1.058, angular momentum ~5.67, and angular velocity ~5.36 rad/s — translating to ball launch speed around 4.8 m/s, enough to send it over a meter high, well above the 0.5m target. I'm settling on a board mass of 0.5 kg to keep these numbers consistent.

I'm double-checking the seesaw setup in MuJoCo — making sure the ball stays still on the level board while the weight falls, considering joint damping and friction defaults, and working out where to place the pivot point relative to the 200x10x4 cm board.

Now I'm worried the fixed support post could collide with the hinged board at the pivot and jam the mechanism, so I'm lowering the post's top slightly below the pivot height to leave a small gap. Then I'm working out the geometry of the board's bottom surface near the pivot as it tilts, to make sure nothing clips the stand during rotation.

Next I'm defining the seesaw's placement: fixing the pivot point's height and horizontal offset, specifying the seesaw body as level with the pivot and positioned along the same axis, with the across-axis left at default zero, then setting up the hinge joint turning about the y-axis at the pivot location.

I'm working out the swing range (-20° to 0°) and placing the weight and ball relative to the pivot — the weight about 0.9 m behind and elevated, the ball positioned beyond the pivot and resting on top of the seesaw.

