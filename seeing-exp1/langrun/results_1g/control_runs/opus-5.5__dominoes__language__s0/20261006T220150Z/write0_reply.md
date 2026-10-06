Ten wooden dominoes, 10 cm tall, stand 6 cm apart. The first starts with a spin of 10 rad/s about y, which tips its top forward toward the others.

A spin of about 3.6 rad/s would carry it past its balance point. Contact with the floor wastes some of that, so 10 rad/s leaves a wide margin.

With a 4.5 cm gap and 10 cm height, a domino leaning on the next one already tilts about 27°. Most should collapse further as the chain settles, and the last one should fall flat.

```world
world  ten dominoes

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

domino
  is a       box 1.5 by 5 by 10 cm, 50 g
  colour     wood
  friction   0.5
  moves      freely
  stands     on floor, 50 cm along
  repeated   10 times, 6 cm apart along
  first one spins  10 rad/s about y

expect
  domino1 touches domino2
  domino9 touches domino10
```

I have not run this. The tilt of every domino after 6 s needs checking in the simulation.

---
thinking (summarized):

I'm sizing dominoes at roughly 1 by 2.5 by 5 cm with about 3.5 cm spacing so each one reaches the next, weighing around 10 grams, and now thinking about how to trigger the first tile—maybe with a launched velocity or spin.

For spinning the first domino, applying a positive rotation about the y-axis tips the top edge toward +x while the bottom edge pushes down and back into the floor, which contact resolution should handle fine and still cause it to topple. I'll use `first one spins` with a magnitude large enough to carry it past its tipping point, roughly estimating around 6 rad/s as a starting guess.

Checking the energy needed: the critical tipping angle is about 11°, and raising the center of mass from 2.5 to 2.55 cm requires surprisingly little height gain, but computing the rotational kinetic energy from the moment of inertia shows that even a 3 rad/s spin falls short of the energy needed to lift the center that far — I'd need something closer to 6.7 rad/s or higher, though too much risks making the domino hop unrealistically. I'm also considering just scaling up the domino dimensions to more closely match real domino proportions, which would change these energy requirements.

That 8/3.6 ratio gives roughly 5x the needed energy, which seems fine, but I need to check whether friction at the bottom actually opposes the spin - working through the torque from the friction force and the normal force at the penetrating edge to see if they cancel the rotation or sustain it.

Given these losses, using 10 rad/s with a resulting top velocity around 0.5 m/s should work. Rather than relying on identical copies for each domino, I'm considering whether a separate striker object - like a ball launched at the top of the first domino, or even a small pendulum - would be a more robust way to kick off the chain reaction instead of trying to pre-tilt domino1.

I'll settle on spinning the first domino at 10 rad/s about the y-axis for simplicity and safety margin. For the toppling geometry, I'm calculating the lean angle between dominoes based on spacing and thickness - with 6 cm center-to-center spacing and 1.5 cm thickness, the gap works out to about 4.5 cm, giving a lean angle around 27 degrees, comfortably above the 15 degree threshold needed for the cascade to continue.

Setting up the scene: dominoes standing on the floor, spaced 50 cm apart along x, mass 50 g each, with floor friction at 0.8 and domino-to-domino friction at 0.5. I'll also add simple touch relations between adjacent dominoes just to be safe, even though I'm unsure if that phrasing is strictly necessary.

