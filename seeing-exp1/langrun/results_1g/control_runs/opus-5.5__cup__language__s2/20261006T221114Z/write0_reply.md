The ball starts near the top of a gentle ramp, rolls off its low end, drops over the cup's near wall, and lands inside. The cup has dead bounces and high rolling friction, so the ball settles well within 6 s.

```world
world  ball down a ramp into a cup

floor
  friction  0.8, spinning 0.005, rolling 0.002

ramp
  is a       ramp
  high end   0 m along, 40 cm up
  low end    1 m along, 20 cm up
  width      30 cm
  friction   0.8, spinning 0.001, rolling 0.0005
  colour     wood

cup
  is an                open box
  length               60 cm
  width                30 cm
  walls                14 cm
  friction             0.9, spinning 0.02, rolling 0.02
  bounce               dead
  colour               grey
  its base 1.32 m along

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.002, rolling 0.001
  colour    orange
  moves     freely
  on ramp, 10 cm from the top

expect
  ball touches ramp
  ball comes to rest in cup
```

---
thinking (summarized):

I'm working out the ramp's physical layout—a plank with a high end and low end, elevated at roughly 40 cm with a thickness of about 4 cm, leading down to a cup positioned to catch the ball so it comes to rest within the 6-second target.

Now I'm thinking through how the cup should be placed relative to the ramp's foot—it needs walls tall and the box long enough that the ball rolls off and lands inside without flying over the far wall or bouncing out. I'm sketching coordinates: ramp running from roughly 40 cm high down to about 15 cm, giving a drop of 25 cm over a meter length, which sets a shallow slope angle.

I'm estimating the ball's exit speed using energy for a rolling sphere, then working through the projectile fall into the cup—checking the time to drop into the cup's interior, the horizontal distance traveled, and whether the ball clears the near wall of the cup while still landing before the far wall.

Since fixed bodies in MuJoCo don't collide, I realize the ramp's foot could actually extend over or into the cup without causing physics issues, which might simplify placement. I'm now considering making the near wall shorter and sizing the cup at roughly 50 cm long, 30 cm wide, with 15 cm walls.

Working through the ball's trajectory after it bounces off the far wall, I estimate the rolling friction deceleration at around 0.9 m/s², and with energy lost at each dead bounce off the walls, the ball should eventually settle to rest within the cup.

I also need to check the dead bounce doesn't launch the ball over the far wall—landing velocity stays low enough given the 15 cm wall height. Then I'm working out geometry so the ball clears the near wall of the cup: with the ramp's low end at 20 cm and walls 14 cm tall, dropping 8 cm takes about 0.128 s, giving roughly 0.22 m horizontal travel, so I'm positioning the near wall accordingly.

Working through the drop timing: landing around x≈1.31–1.34 m, which fits within the cup's 1.0–1.6 m span, so the ramp heights of 40 cm high and 20 cm low (11.3° angle) seem workable. Now I'm figuring out how to position the cup piece relative to the floor in the scene setup.

For the ball, I'll place it "on ramp, 10 cm from the top," matching the pattern used for ramp placement. Ramp width matches cup width at 30 cm, the ball's friction is 0.8 so it stays symmetric and won't roll sideways, and colours are optional. The expected outcome is the ball touching the ramp and coming to rest in the cup.

