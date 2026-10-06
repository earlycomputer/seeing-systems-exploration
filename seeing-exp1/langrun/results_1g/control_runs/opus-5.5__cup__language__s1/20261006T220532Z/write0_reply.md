The ramp tips the ball off its low end, and it drops into an open box set just past the foot. Dead bounces and high friction in the cup let it settle well within 6 s.

```world
world  ball down a ramp into a cup

floor
  friction  0.8, spinning 0.005, rolling 0.002

ramp
  is a       ramp
  high end   0 m along, 30 cm up
  low end    1 m along, 15 cm up
  width      20 cm
  thickness  4 cm
  friction   0.9, spinning 0.005, rolling 0.002
  colour     wood

cup
  is an      open box
  length     50 cm
  width      30 cm
  walls      10 cm
  friction   1.0, spinning 0.02, rolling 0.01
  bounce     dead
  colour     grey
  stands     on floor, 1.3 m along

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.9, spinning 0.01, rolling 0.005
  colour    orange
  moves     freely
  rests     on ramp.deck, 10 cm from the top

expect
  ball touches ramp
  ball comes to rest in cup
```

---
thinking (summarized):

I need to think through the ramp geometry more carefully — the high end and low end define positions, the leg is a post running from floor to the top point, and the plank spans from top to foot, but it's unclear whether that's measured along the surface line or the centerline, so I should treat it as ambiguous and pick a reasonable convention.

For the ball, I'll place it "on ramp.deck, 10 cm from the top" to be unambiguous about which piece it rests on. For the cup, I need to figure out how to position the whole open-box part using one of its pieces as reference — I'll go with something like "stands on floor, 1.5 m along" rather than referencing an internal piece directly.

Then I'm working out the actual numbers: if the ramp's high end sits at height 40 cm and the low end near floor level, I need to check whether the plank's thickness would drive the deck surface below the floor at the low end, which would require adjusting the low-end height to account for half the plank thickness.

Since static geoms don't collide with each other, I don't need to worry about the ramp clipping the floor, so I can set the low end at roughly 2 cm up. Now I'm positioning the cup so the ball rolling off the ramp actually lands inside it rather than overshooting — trying ramp heights like 50 cm to 15 cm with the cup placed around 1.2 m along, walls 10 cm tall, box 40 cm long, then calculating the ball's exit speed from energy conservation with rolling (using the 10/7 factor for a solid sphere) to see if it's slow enough not to jump the far wall, and adjusting the slope drop height downward since the first estimate came out too fast.

I'll place the cup centered at 1.3 m so its 50 cm span (1.05 to 1.55) catches the ball landing near 1.24 m, with the far wall absorbing the ~1.3 m/s impact via a dead bounce. With high cup friction and modest ball rolling friction, the ball should settle within a few seconds as it bounces between the walls.

For the ramp, I'm setting it at 20 cm wide with the ball starting 10 cm from the top, giving an 8.5° slope over 90 cm of travel and about 13.5 cm of height drop — positioning the high end at 0 m along, 30 cm up, and the low end at 1 m along, 15 cm up, with both cup and ball using dead bounces so everything settles cleanly.

