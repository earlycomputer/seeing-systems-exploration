**What happened:** The stack stood still for 1.31 s. Then the ball reached block1, but it had slowed from 2.5 to about 1.06 m/s on the way. Rolling friction (0.004) and the slide-to-roll transition took most of its speed. At that speed the push only nudged the whole stack about 2–3 cm along. The ball stopped dead, block5 wobbled by 2°, and all five blocks settled upright. Nothing toppled.

**What I changed:** The push needs to be much harder and arrive at full speed. The ball now:
- is launched at 4 m/s,
- already spins at the matching rolling rate (100 rad/s about y), so it loses no speed sliding,
- has much lower rolling friction, so it still reaches the stack after about half a second.

A 1 kg ball at nearly 4 m/s should drive the 200 g bottom block out from under the stack, and the four blocks above should fall.

```json
{"what_happens": "The stack stands for 1.31 s until the rolling ball, slowed to about 1 m/s, reaches block1; the gentle push slides the whole stack about 2-3 cm, the top block wobbles 2°, and all five blocks settle upright and stay standing to the end.", "works": false, "problem": "The ball arrives far too slowly, so the bottom block and the whole stack only shuffle a few centimetres and the stack never topples."}
```

```world
world  toppled stack

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.0005

-- five tall blocks, block1 at the bottom, block5 on top
block
  is a      box 6 by 6 by 10 cm, 200 g
  friction  0.6
  colour    wood
  moves     freely
  stacked   5 high
  stands    on floor, 2 m along

-- the pusher: a heavy ball already rolling hard along the floor at the bottom block
ball
  is a      sphere 4 cm radius, 1 kg
  rolls
  friction  0.8, spinning 0.001, rolling 0.0005
  colour    orange
  moves     freely
  rests     on floor, 0 m along
  launched  4 m/s along
  spins     100 rad/s about y

expect
  ball touches block1
```

---
thinking (summarized):

The ball barely moved the stack before stopping — decelerating oddly fast, almost as if it lost momentum unnaturally on impact rather than realistically transferring force to a much lighter block. That suggests the push needs to be far stronger, and something about the collision physics seems off.

I'm working through launching the ball faster and with proper spin so it rolls from the start rather than sliding first. Checking the math: with radius 0.04 m, a 5 m/s launch needs angular velocity around 125 rad/s about the y-axis for true rolling, and I need to verify the sign convention so the spin direction matches forward motion along x.

The deceleration I measured earlier actually matches what rolling friction in MuJoCo would produce given the slip-to-roll transition factor, so I should lower that rolling friction coefficient to let the ball carry more speed into the impact.

Now I'm also reconsidering why the collision transferred so little momentum — the stacked blocks were likely held together by floor and inter-block friction (using the max-combination rule), absorbing the ball's momentum instead of letting block1 shoot forward, so a heavier, faster strike with less friction underneath should finally separate it from the stack.

I'm also reworking the timing: putting the 1 kg ball at the start with low rolling friction so it decelerates gently (~0.09 m/s² over ~1.9 m), arriving at roughly 3.9 m/s and giving the stack enough time to stand upright before impact rather than only 0.1 s.

Now checking whether block1 shooting out at that speed actually topples the stack, or if the ball instead clips block2 as it's falling — need to confirm the ball's travel distance during block2's ~0.14 s fall clears or collides with the dropping block.

