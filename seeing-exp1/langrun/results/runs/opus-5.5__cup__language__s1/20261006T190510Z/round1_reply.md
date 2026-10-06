**What happened:** The ball sat on the ramp deck and crept down it at a steady 0.09 m/s. By 6 s it had covered only 0.5 m and was still on the ramp, short of the cup.

**Why:** The ball's rolling friction was set too high. In MuJoCo, rolling resistance on a ball acts roughly like an uphill slope of `rolling coefficient ÷ radius`. Here that is 0.01 ÷ 0.03 m ≈ 0.33, which is steeper than the ramp itself (15 cm drop over 60 cm, about 0.25). Gravity could not get the ball rolling, so it only crept.

**The fix:**
- Lower the ball's rolling friction to 0.002. That works out to about 0.07, well under the ramp's slope.
  - The ball should then leave the ramp's low end at about 1.2 m/s.
  - It should land roughly 20 cm past the ramp's end.
- Lengthen the cup and shift it slightly further along so it has room to catch the ball.
- On the cup's floor, the remaining rolling friction and dead bounces against the walls should still bring it to rest within the run.

```json
{"what_happens": "The ball sits on the ramp deck and creeps down it at a steady 0.09 m/s, reaching only x = 0.56 m by 6 s; it never leaves the ramp or reaches the cup.", "works": false, "problem": "The ball's rolling friction (0.01 on a 3 cm ball) resists more than the ramp's 14° slope can overcome, so the ball barely rolls and never reaches the cup."}
```

```world
world  ball down a ramp into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ramp
  is a       ramp
  high end   0 m along, 40 cm up
  low end    60 cm along, 25 cm up
  width      20 cm
  thickness  2 cm

-- the cup sits where the ball lands after leaving the low end
cup
  is an      open box
  length     50 cm
  width      30 cm
  walls      8 cm
  on         floor, 97 cm along

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.002, rolling 0.002
  colour    orange
  moves     freely
  rests     on ramp.deck, 5 cm from the top

expect
  ball touches ramp
  ball comes to rest in cup
```

---
thinking (summarized):

The ball crept along at a constant 0.09 m/s, which seems off—rolling friction of 0.01 is actually too high here. I'm realizing MuJoCo's rolling friction coefficient is a torque term with length units, resisting torque proportional to mu_r times normal force. Dividing mu_r by the ball's radius (0.01/0.03 ≈ 0.33) gives an effective resistance slope greater than tan(14°) ≈ 0.25, which explains why the ball keeps creeping instead of staying still.

MuJoCo takes the max of the two geoms' rolling frictions, so even if the floor is low at 0.002, the deck's unknown default could dominate. Settling on ball rolling friction of 0.0005 gives 0.0005/0.03 ≈ 0.017, comfortably below the slope threshold, which should stop the creep—but I'm now second-guessing whether the ball will actually settle in the cup or just oscillate between the dead walls for too long given the resulting low deceleration (~0.12 m/s²). Maybe 0.002 is the better compromise, since 0.002/0.03 ≈ 0.067 still keeps it rolling without excessive drift.

I'm now tracing through the physics: deceleration on the flat section (~0.47 m/s²), acceleration down the slope (~1.24 m/s²), exit speed off the ramp edge (~1.15 m/s at the 14° angle), and the resulting trajectory as the ball clears the wall and lands—working out the x-position where it crosses near the 0.70 m wall mark based on drop height and timing.

Adjusting the cup's position: moving it to 90-97 cm with a 50 cm length so the near wall sits around 0.72-0.75 m gives enough clearance for the ball's 0.76 m edge to clear it, and the landing calculation puts it around x ≈ 0.83 m, which lands safely on the base. I'm settling on a rolling friction coefficient of 0.002 since it keeps the landing speed variance comfortably within the 50 cm target zone.

