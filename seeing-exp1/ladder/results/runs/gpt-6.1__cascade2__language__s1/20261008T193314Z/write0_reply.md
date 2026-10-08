MuJoCo’s default gravity is 9.81 m/s². The language cannot specify exact numeric restitution or global damping defaults; this world uses `dead` contacts, no joints, and no initial velocities.

```world
world  gravity driven domino pair

floor
  size      6 m
  friction  0.70, spinning 0, rolling 0

ramp1
  is a       ramp
  high end   0 m along, 0.492020143 m up
  low end    0.939692621 m along, 0.15 m up
  width      0.30 m
  thickness  0.02 m
  friction   0.70, spinning 0, rolling 0
  bounce     dead
  colour     wood

ball1
  is a      sphere 0.10 m across, 0.20 kg
  moves     freely
  rolls
  friction  0.70, spinning 0, rolling 0
  bounce    dead
  colour    orange
  on ramp1.deck, 0 m from the top

-- The first domino's near face is 0.10 m beyond the ramp's exit.
domino1
  is a      box 0.08 by 0.04 by 0.24 m, 0.25 kg
  moves     freely
  friction  0.70, spinning 0, rolling 0
  bounce    dead
  colour    white
  stands    on floor, 0.14 m beyond ramp1.foot

domino2
  is a      box 0.08 by 0.04 by 0.24 m, 0.25 kg
  moves     freely
  friction  0.70, spinning 0, rolling 0
  bounce    dead
  colour    white
  stands    on floor, 0.18 m beyond domino1

expect
  ball1 touches domino1
  domino1 touches domino2
```

---
thinking (summarized):

**Analyzing angles and torque**

I'm looking into the next gap, where rotating an angle gives me about 25 degrees beyond equilibrium. I see that domino1 might slide due to a coefficient of .7, but the torque is dominant since it strikes above .15. I think this setup should pass through nicely. I'll need to ensure the rest of the system starts without any launch complications. It's a bit technical, but I feel I'm on the right track!

**Evaluating logical checks**

I'm considering using `ball1 touches ramp1.deck` but I wonder if the requirement checker is necessary for the expansion target. I really need the exact names of known compounds for ramp1 parsed correctly. My best options seem to be using `ball1 touches domino1` and `domino1 touches domino2`, as those should suffice for goal checks. It feels like that might be enough to wrap this up!