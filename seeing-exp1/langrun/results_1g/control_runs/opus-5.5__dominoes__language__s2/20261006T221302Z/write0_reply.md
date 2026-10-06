Each domino is 1.5 cm thick, 5 cm wide, 10 cm tall and stands 6 cm from the next. The first one starts with a forward spin of 6 rad/s, which tips it past its balance point; it needs only about 8.5° of tilt to go over. Each falling domino should hit the next one when it is roughly 37° from upright. The last one should end flat on the floor, with the others leaning on each other well past 15°. I haven't simulated this, so those angles are estimates.

```world
world  domino row

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

domino
  is a      box 1.5 by 5 by 10 cm, 50 g
  colour    wood
  friction  0.5, spinning 0.005, rolling 0.002
  moves     freely
  repeated  10 times, 6 cm apart along
  first one spins  6 rad/s about y
  stands    on floor, 1 m along

expect
  domino1 touches domino2
  domino9 touches domino10
```

---
thinking (summarized):

I'm working out domino dimensions for the box—thinking about thickness, width, and height ratios, settling around 1.5 by 5 by 10 cm with spacing less than the height so each piece reliably knocks over the next.

For the spin, I'm checking that positive rotation about y tips the top forward along +x using the right-hand rule, then computing the critical tipping angle from arctan(thickness/height), about 8.5°. I'm now calculating the velocity of the bottom front edge given angular velocity about the center, using the cross product of ω with the position vector to the edge, to figure out whether the initial spin is enough to pivot the domino over.

Let me settle on 6 rad/s giving reasonable top speed of 0.3 m/s without excessive skidding. Now figuring spacing: with centers 6 cm apart and 4.5 cm gaps, a domino tips about 37° before touching the next one in line. The last domino falls freely to the floor while the others lean against their neighbor at that contact angle.

I'm estimating mass from dimensions: roughly 75 cm³ of wood giving about 50 g per piece, with friction set to 0.5 between dominoes and 0.8 against the floor to prevent sliding. For positioning, I'll place each domino along a line a meter apart, naming them sequentially, and optionally note the first domino touching the second for a plausible contact relationship.

