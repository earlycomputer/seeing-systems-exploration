Three 4 cm balls sit 30 cm apart. The first is launched already rolling, at 2.4 m/s with matching spin. The cup is a low-fronted open box with a dead bounce. Its front edge is only a 1 cm step. High rolling friction inside the cup brings the third ball to rest before it can come back out. I haven't run this yet. If anything misses, the likeliest problem is the third ball losing too much speed at the step or bouncing back out of the cup.

```world
world  three balls into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ball1
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    orange
  moves     freely
  rests     on floor, 1 m along
  launched  2.4 m/s along
  spins     60 rad/s about y

ball2
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    white
  moves     freely
  rests     on floor, 30 cm beyond ball1

ball3
  is a      sphere 4 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    black
  moves     freely
  rests     on floor, 30 cm beyond ball2

cup
  is an             open box
  length            50 cm
  width             30 cm
  walls             10 cm
  wall thickness    2 cm
  base thickness    1 cm
  near wall height  1 cm
  friction          0.8, spinning 0.02, rolling 0.02
  bounce            dead
  colour            wood
  its base 55 cm beyond ball3

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 touches cup
  ball3 comes to rest in cup
```

---
thinking (summarized):

I'm planning a three-ball chain reaction where each ball knocks into the next, with the final ball needing to land in a cup. I'm figuring out how to make the cup work with a flat floor, since a walled cup would just block a rolling ball rather than catch it, so I'm considering options like a ramp leading into a lowered or angled catch area.

Actually the ramp-to-cup idea feels risky given unclear plank joint geometry. Let me reconsider: a simple low-walled box cup where the ball climbs a small step and loses enough energy that rolling friction brings it to rest inside, rather than bouncing back out — I could bump up the cup's rolling friction coefficient so the deceleration from friction torque is strong enough to stop the ball before it exits.

I'll go with an open box shape: 40 cm long, 30 cm wide, 10 cm high walls, 1 cm thick base, with the near-side wall shrunk down to about 1 cm so the ball can roll in easily over it.

So a 2 cm x 30 cm x 1 cm near wall creates basically a small 1 cm step — with a 4 cm ball, climbing that should be fine since the contact angle mostly pushes upward and the ball's speed (~1.5 m/s) is more than enough. I'm now wondering whether the step is even necessary, since the base itself is just a flat box sitting on the floor anyway.

I'll give the cup's interior a rolling friction of about 0.02 and add a dead bounce at the far wall (10 cm tall) to absorb energy, since the ball (4 cm radius) should have no trouble clearing it physically. Ball3 might hit the far wall around 1 m/s, but with rolling friction over the 40 cm cup length it'll have slowed some before then. For collisions between equal-mass rolling balls, I'm tracking how sliding friction transitions each ball to rolling afterward — the struck ball initially slides at close to the incoming speed before settling into rolling at 5/7 of that speed, so momentum and speed degrade through the chain in a predictable way.

I'll set ball1's launch speed so ball3 ends up rolling toward the cup around 1.2 m/s, meaning v0 should be roughly 2.4 m/s. That leaves ball2 trailing behind at about 0.5 m/s after its own collision, which should still be slow enough with rolling friction that it doesn't crash into ball3 inside the cup, though I'm aware ball1 and ball2 might also eventually drift in.

Computing the rolling transition time for ball1 over the sliding friction, I estimate it reaches pure rolling after about 0.3 m, so I'll give it an initial spin of roughly 60 rad/s about the y-axis to start it rolling immediately. For ball3, factoring in rolling friction over the remaining 40 cm plus the step climb, it should arrive at the cup around 1.2 m/s.

Inside the cup, with rolling friction around 0.02, deceleration should bring it to rest within about 14 cm, so I'll size the cup around 50 cm for margin. Now I need to work out the positions: ball1 on the floor at 1 m, ball2 30 cm beyond ball1, ball3 30 cm beyond ball2, and then figure out how to place the cup relative to ball3 using its component pieces like the base or rim.

I'll place the base's center 55 cm beyond ball3, giving about a 26 cm gap from the ball's surface since the base is 50 cm long, with the across-axis defaulting to zero to align with the balls. The near wall of the cup should be centered on the base's near end with a slight protrusion of about 1 cm, and the wall itself is 2 cm thick. For the balls, I'm setting radius to 4 cm, mass 100 g, friction 0.8, spinning friction 0.005, and rolling friction 0.002, matching the floor's rolling friction so the balls roll consistently and eventually collide in sequence before the last one settles in the cup.

