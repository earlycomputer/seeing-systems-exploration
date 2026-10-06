The ball starts 30 cm from the table's edge already rolling at 1.56 m/s, so it leaves the edge at full speed. It falls 73 cm in about 0.39 s and lands about 60 cm past the edge, at the bucket's centre. On the way down it passes the bucket's near wall with roughly 13 cm to spare.

```world
world  ball off the table into a bucket

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

-- a solid table block, 1 m long and 75 cm high; its far edge is 50 cm along
table
  is a      box 100 by 60 by 75 cm
  friction  0.8, spinning 0.001, rolling 0.0002
  colour    wood
  stands    on floor, 0 cm along

-- the bucket's centre is 110 cm beyond the table's centre, so 60 cm beyond its edge
bucket
  is an     open box
  length    40 cm
  width     40 cm
  walls     30 cm
  friction  0.8, spinning 0.01, rolling 0.01
  bounce    dead
  colour    grey
  on floor, 110 cm beyond table

-- the ball starts 30 cm before the edge, already rolling forward (spin = speed / radius)
ball
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.001, rolling 0.0002
  colour    orange
  moves     freely
  rests     on table, 20 cm along
  launched  1.56 m/s along
  spins     52 rad/s about y

expect
  ball touches table
  ball comes to rest in bucket
```

These figures are worked out by hand and have not been run yet:

- **Flight:** the ball loses only about 0.01 m/s rolling on the low-friction table. It is fast enough that it leaves the edge rather than tipping over it.
- **Landing:** inside the bucket, the higher rolling friction (0.01) and dead bounce should stop the ball well within the 6 s run.
- **Table:** I built it as a solid block rather than the library's legged `table` part, because I wasn't sure how that part's top is positioned. The bucket is placed relative to the table's centre, so its position holds wherever the table ends up along x.

---
thinking (summarized):

I'm working out the table dimensions syntax, figuring out how the "120 by 60 cm" surface size combines with a thickness value, similar to how the catapult's box dimensions were specified with height offsets.

Given the uncertainty around how part positions and "beyond" offsets work, I decide it's safer to build the table as a simple fixed box rather than a multi-part table-with-legs construct. For the bucket, I'm reasoning through using an open box placed relative to the table's far edge using a centre-offset "beyond" clause, computing where its centre should land based on the table's box position.

Now I'm working through the actual physics: with the table at 0.75 m height, ball radius 3 cm, the bucket's wall height and base thickness, and computing the inner opening of the bucket from its 40 cm length and 2 cm wall thickness, so the ball launched off the table edge has room to clear the near wall and land inside.

Calculating the drop: ball falls from 0.78 m to around 0.05 m near the bucket floor, giving fall time ~0.386 s, needing horizontal velocity ~1.55 m/s to cover 0.6 m. Checking the near wall clearance at 0.44 m horizontal distance, the ball's center is still well above the 0.25 m wall top, confirming it clears safely before landing inside the bucket.

I'll bump the wall height to 30 cm for safety margin since it still clears the ball comfortably. For the ball's initial motion, I'm setting it rolling at 1.55 m/s with matching angular velocity, and to minimize friction-induced slowdown before it reaches the bucket, I'll start it closer to the table edge, around 30 cm away.

Over that short distance the rolling friction loss is manageable if I set a low friction coefficient on the ball itself, though I need to balance this against ensuring the ball eventually settles inside the bucket rather than coasting too long — so I'm considering giving the bucket's floor a higher friction value to help it come to rest once inside.

With the bounce effectively dead on impact (no restitution), the ball's downward velocity gets absorbed, and its horizontal momentum combined with matching spin lets it transition into pure rolling almost immediately. It then rolls the short remaining distance to the far wall, where another dead-ish contact absorbs the impact rather than bouncing it back, after which it should settle into rolling or resting within the bucket.

I'm working out the positional offsets for table, ball, and bucket, settling on absolute "along" values and skipping ambiguous "to the left" clauses. For the bucket, I'm treating it as an open box needing length, width, and wall pieces, positioned on the floor beyond the table, with the ball launched at 1.56 m/s.

Checking the rolling condition, I confirm ω=v/r gives +52 rad/s about y for rolling in +x, verified by computing the contact point velocity using the cross product. I expect the ball to land in the bucket and come to rest there, with mass set to 100 g and colors still to assign.

