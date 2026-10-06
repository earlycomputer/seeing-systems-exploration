A level seesaw rests its far end on a support post, with the light ball sitting on that end. The heavy cube falls 1.4 m onto the near end and flips the far end up hard enough to throw the ball.

**Rough check (hand estimate, not a run):**
- The cube hits at about 5.3 m/s.
- If the cube doesn't bounce (`bounce dead`), the far end starts up at about 4 m/s. The cube's weight keeps pressing on the near end after that.
- The far end rises about 30 cm before the near end hits the floor and stops the beam.
- The ball then leaves at roughly 4 m/s, about 30° back from vertical. That should carry it well over 50 cm above where it started.

**Why the far end can't tip down early:** the support post under the far end stops that end from dropping before the cube lands. So the beam stays level, and the ball doesn't roll off.

```world
world  seesaw throw

floor
  friction  0.8, spinning 0.005, rolling 0.002

pivot
  is a  point
  at    30 cm up

fulcrum
  is a    box 8 by 20 by 24 cm
  on      floor
  colour  grey

rest post
  is a    box 6 by 20 by 28 cm
  on      floor, 55 cm along
  colour  grey

seesaw
  is a      box 120 by 20 by 4 cm, 500 g
  centred over fulcrum, level with pivot
  turns on  seesaw hinge, about y, at pivot
  swings    from -35° to 35°
  friction  0.8
  colour    wood

ball
  is a      sphere 4 cm radius, 100 g
  rolls
  friction  0.8, spinning 0.01, rolling 0.004
  moves     freely
  colour    orange
  on seesaw, 50 cm along

weight
  is a      cube 10 cm, 1 kg
  bounce    dead
  friction  0.8
  moves     freely
  colour    dark grey
  at        50 cm behind pivot, 1.8 m up

expect
  weight touches seesaw
```

---
thinking (summarized):

I'm designing a seesaw mechanism: a beam pivoting on a fixed fulcrum, with a 1 kg weight dropped on one side to launch a 100 g ball at least 50 cm high from the other end, working out beam length, pivot height, and starting tilt.

I need to be careful about rotation direction conventions—a positive rotation about the y-axis lowers the far end of the beam, so I'll place the ball on that far end (starting down) and have the weight drop onto the near end (starting raised), ensuring the geometry matches the intended launch motion.

But placing a ball on a pre-tilted beam creates issues: if positioned relative to the level beam, it would float above the tilted surface rather than resting on it. A simpler approach is to start the beam level, let the weight's impact drive the rotation, and let the ball launch once the beam swings up to its limit—though I need to check that the ball doesn't destabilize the level start before the weight even lands.

I'm now reconsidering the balance problem: if the ball sits on one end, the beam might tip toward it before the weight drops, causing it to roll off or launch prematurely. A fix is to add a fixed post or stop under the far end so that side rests level despite the ball's weight, only lifting once the weight impacts the other end and shifts the torque.

For the hinge limits, I'm setting a swing range (roughly ±30°) with the post acting as one stop and the floor as the other, based on a pivot height around 0.3m and matching beam half-length.

Now working out the impact dynamics: a 1 kg weight dropping onto the near end transfers momentum into the beam-ball system, so I'm computing the combined moment of inertia (beam plus ball at the far end) and solving for the resulting angular velocity using conservation of angular momentum, treating the collision as inelastic.

With ω around 0.79v, I then factor in gravity continuing to accelerate the system and the fact that the far end needs to rise about 0.3 m during the 30° swing before the ball launches. Requiring a launch speed near 3 m/s to clear a 0.5 m rise, I back-calculate that the weight needs roughly 4 m/s at impact, meaning a drop height near 0.8 m — so I'm testing a 1.5 m drop, giving about 5.4 m/s impact speed and 4.3 m/s at the far end, which seems promising.

After separation the ball still rises another 0.9 m plus the 0.3 m it gained during the swing, giving a comfortable margin above the needed height. I also check the trajectory direction: since the far end's velocity at launch is perpendicular to the tilted beam, the ball flies up and slightly back toward the pivot — working out the vertical component (~3.7 m/s) confirms a 0.7 m rise, and checking the horizontal travel suggests the ball likely clears the weight sitting at the near end without collision.

Now I'm thinking through how to represent the dropped weight — making it a cube rather than a sphere since the ball itself is already a sphere, and working out where to position it relative to the pivot and seesaw using absolute offsets for the setup.

I also need to size the fulcrum post carefully so its top doesn't collide with the beam as it rotates — checking the geometry of the beam's bottom edge at an angle to make sure there's enough clearance below the pivot height.

For the seesaw itself, I'll keep it simple: a flat box roughly 120 by 20 by 4 cm, lightweight, positioned level with the pivot so it balances naturally at the fulcrum.

I'll set up a hinge joint named "seesaw hinge" rotating about the y-axis at the pivot point, with a swing range of roughly ±35° and minimal damping. For the resting support at the far end, I'll add a short post sized to match the beam's rise, placed so it sits under the beam around the 55 cm mark along the length, keeping the beam level when it's not tilted — making sure it stays clear once the beam rotates and the far end lifts.

Then I'm placing the weight ball as a 4 cm radius sphere, 100 g, positioned "on seesaw" at 52 cm along — reasoning through whether that phrase fixes vertical placement only or also anchors the along-position absolutely, similar to how "on floor" examples work.

I'm figuring out the weight's placement next: a 1 kg cube, 10 cm, set to bounce dead and move freely, positioned something like "50 cm behind pivot" to fix its along-offset, then a separate height like "1.8 m up" to fix vertical position, leaving the across-axis still undetermined.

Now I'm computing the drop: falling from 1.8 m centre height to the beam's top surface gives about 1.43 m of fall, so impact speed is roughly 5.3 m/s. Then I'm working out the angle at which the beam's near end would strike the floor, solving for where the bottom corner touches down, getting roughly 28°, with the beam's range limited to about ±35° before the floor stops it — and considering whether the sitting weight might slide or bounce sideways off the near end when that happens.

I'm also mapping out the object ordering: fulcrum box on the floor, then the pivot, the seesaw resting on it, and finally the ball and weight placed on top, keeping the setup straightforward with simple touch relationships like "weight touches seesaw" rather than anything more complex.

For the physics itself, I estimate the weight (1 kg at a 0.6 m radius) contributes enough torque during the swing to help lift the ball, so the margin should hold up fine.

