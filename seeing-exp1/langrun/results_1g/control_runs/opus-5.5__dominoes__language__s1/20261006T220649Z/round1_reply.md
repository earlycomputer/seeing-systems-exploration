**What happened:** nothing fell. All ten dominoes stood still for the whole 6 s. `domino1` twitched about 1° at 0.16 s and settled back upright.

**Why:** the starting spin was far too weak.
- A domino spinning about its centre has to switch to pivoting on its front bottom edge as soon as that edge meets the floor. Angular momentum carries over, but the moment of inertia about the edge is about 4 times larger. So the spin drops to a quarter and the rotational energy to a quarter.
- At 4 rad/s that leaves about 3×10⁻⁵ J. Lifting the domino's centre past its balance point needs about 7.6×10⁻⁵ J, so it rocked and dropped back.
- At 15 rad/s the leftover is about 3.8×10⁻⁴ J, roughly five times what is needed. That should send it over firmly without throwing it off the floor.

```json
{"what_happens": "All ten dominoes stay standing for the full 6 s; domino1 only rocks about 1° at 0.16 s and settles back upright, so nothing is knocked down.", "works": false, "problem": "The 4 rad/s starting spin on domino1 is too weak: once its front edge meets the floor it keeps only a quarter of its energy, too little to tip it past balance."}
```

```world
world  domino row

floor
  size      4 m
  friction  0.8, spinning 0.005, rolling 0.002

domino
  is a             box 1 by 4 by 8 cm, 25 g
  colour           wood
  friction         0.6, spinning 0.005, rolling 0.002
  moves            freely
  repeated         10 times, 5 cm apart along
  first one spins  15 rad/s about y
  stands           on floor, 1 m along

expect
  domino1 touches domino2
  domino9 touches domino10
  domino10 touches floor
```

---
thinking (summarized):

I'm noticing domino1 barely rotated, only about 1° despite the 4 rad/s spin, since the floor contact absorbed most of it. I'm estimating the rotational kinetic energy about its center using the moment of inertia formula, getting roughly 1.1e-4 J.

Checking the energy needed to tip: raising the center of mass by about 0.31 mm requires mgΔ ≈ 7.6e-5 J. But the collision when the corner hits the floor is inelastic—angular momentum conservation shows the moment of inertia about the corner is 4× that about the center, so the post-impact kinetic energy drops to a quarter. That means I need ω² ≥ 45, so roughly 6.7 rad/s minimum, and testing 20 rad/s gives about 9× the required energy, suggesting that speed should work but might cause the domino to hop rather than cleanly tip.

Maybe instead of relying on rotating a copy, a separate pusher like a ball launched at the domino's upper section would be more reliable—I'm thinking through how its radius and resting height compare to the domino's center of mass to see where contact occurs and whether it pushes high enough to tip rather than just sliding the base.

Though a pendulum hitting the top could work too, it adds complexity. Simplest fix might just be cranking up the spin rate, though I need to check hop risk from the front corner catching the floor. Alternatively, I could launch a small sphere through the air at the right height and speed to strike the domino's back face directly.

Checking the drop over that short flight time, the ball lands at the right height with enough momentum from its mass and speed to tip the domino. I'm unsure whether I can reference "domino1" by name for relative positioning or need to stick with absolute coordinates like "90 cm along, 7 cm up."

Now I'm working through whether a 1 m/s ball striking 2 cm above the domino's center delivers enough angular impulse about the base edge to topple it — computing the required angular momentum against the moment of inertia at the corner to see if the needed impulse threshold is met.

Actually, maybe simplify further: just use a spin approach at 10 rad/s without introducing a separate ball, avoiding extra naming complexity. Checking the energy at that spin, it's about double what's needed, and the front corner impact creates only a tiny vertical velocity, while the bottom edge slides backward faster — friction there would actually help generate forward torque rather than hinder it.

