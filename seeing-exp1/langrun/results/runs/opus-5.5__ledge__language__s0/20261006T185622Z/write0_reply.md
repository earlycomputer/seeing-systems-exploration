The table top is 75 cm high and its far edge is at x = 60 cm. The bucket is centred at x = 120 cm, which is 60 cm beyond that edge. The ball starts 40 cm from the edge, already rolling: it is launched at 1.55 m/s with a matching spin of v/r ≈ 51.7 rad/s, so table friction shouldn't slow it.

**Predicted path, from free-fall estimates (not checked by running MuJoCo):**
- At 1.55 m/s the ball should leave the edge cleanly instead of tipping over it.
- Its centre should pass over the bucket's 25 cm near wall about 49 cm beyond the edge. The wall is 39–41 cm beyond the edge, so the ball should clear it.
- It should reach the bucket's base about 59 cm beyond the edge, close to the bucket's centre.
- A dead bounce should keep it in the bucket.

**Uncertainties:**
- I place the bucket with `on floor, 1.2 m along` and assume the open box is positioned by its base. That is how the library's raised bucket places it, but the language doesn't spell this out.
- I assume the table part's top is centred at x = 0, since it is given no position. If either assumption is wrong, the 60 cm spacing will be off.

```world
world  roll off the table into a bucket

floor
  friction  0.8, spinning 0.005, rolling 0.002

table
  is a     table
  surface  120 by 60 cm
  height   75 cm

bucket
  is an   open box
  length  40 cm
  width   40 cm
  walls   25 cm
  on      floor, 1.2 m along

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.005, rolling 0.0005
  colour    orange
  moves     freely
  rests     on table.top, 20 cm along, 0 cm to the left
  launched  1.55 m/s along
  spins     51.7 rad/s about y

expect
  ball touches table
  ball comes to rest in bucket
```

---
thinking (summarized):

I need to work out the physics of a ball rolling off a table edge and landing in a bucket positioned 60 cm beyond the edge, factoring in table height, launch speed, and the fall time needed to clear that horizontal distance.

Testing a table height of 75 cm with a bucket wall height of 25 cm, I calculate the required launch speed (around 1.53 m/s) by checking fall times to clear the bucket rim and land near its base, making sure the trajectory clears the near wall before dropping into the bucket. I also need to account for whether the ball is sliding or truly rolling off the edge, since a ball launched without spin behaves differently (ending at 5/7 of its initial speed) than one rolling naturally, where angular velocity relates directly to linear speed through the radius.

For a rolling ball at roughly 1.55 m/s with a 3 cm radius, I set the spin to about 51.7 rad/s so it matches true rolling motion, and checking v²/(gr) confirms the ball leaves the table edge immediately rather than pivoting around it. Now I'm working out the actual table and object placement coordinates.

I'm trying to figure out positioning syntax for the bucket relative to the table—whether to use a relative offset like "beyond table" or just place it with an absolute coordinate like "1.2 m along" since the reference point for such placement phrases is ambiguous. I'll go with the safer absolute positioning approach.

Ball should leave the table edge at x=0.6 and land roughly 0.59 beyond, placing it around x=1.19, right in the bucket. I'll place the ball resting on the table top 20 cm from the edge so it rolls the 40 cm before departing, with friction left at default so it settles naturally in the bucket once it lands.

