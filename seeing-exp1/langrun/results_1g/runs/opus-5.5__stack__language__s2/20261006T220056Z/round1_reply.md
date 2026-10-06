**What happened:** The ball slid for a while before it started rolling, which cost it speed. It reached block1 at 1.30 s moving only about 0.75 m/s. The dead hit nudged the whole stack about 2–3 cm along the floor as one piece. All five blocks came to rest still stacked, tilted at most 1°, and block5 never touched the floor. The stack never toppled, so the world does not do what the brief says.

**What I changed:**
- **A harder, sustained push.** The ball is now heavier (3 kg), faster (3.5 m/s) and starts already rolling, so it keeps its speed. Lower rolling friction means it slows less on the way.
- **A stack that tips instead of sliding.** The blocks are now taller boxes (8 × 8 × 12 cm) and grip each other with friction 0.9. When the bottom block is shoved out, the four blocks above should be dragged at their base and tip over rather than slide off as a unit.
- **A longer standing time.** The ball starts further back, so the stack stands untouched for most of a second first.

```world
world  five block stack knocked from below

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

block
  is a      box 8 by 8 by 12 cm, 150 g
  friction  0.9, spinning 0.005
  colour    wood
  moves     freely
  stacked   5 high
  stands    on floor, 1.5 m along

pusher ball
  is a      sphere 5 cm radius, 3 kg
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.0005
  colour    orange
  moves     freely
  rests     on floor, 1 m behind block1
  launched  3.5 m/s along
  spins     70 rad/s about y

expect
  pusher ball touches block1
  block5 touches floor
```

```json
{"what_happens": "The ball slid before rolling and reached block1 at 1.30 s at only about 0.75 m/s. The dead hit pushed the whole stack about 2-3 cm along the floor as one piece, and every block came to rest still stacked, tilted at most 1 degree, with block5 never reaching the floor.", "works": false, "problem": "The push was too weak and too brief, so the stack slid a little as one unit instead of toppling."}
```

---
thinking (summarized):

I'm working through the ball's deceleration from sliding to rolling friction, then calculating its impact velocity on the block and how the stack slides together given the friction coefficients between the blocks and floor.

That only produced a 2 cm shift, so I need a much harder hit — a faster ball that's already spinning to match rolling (computing ω=v/r=100 rad/s about the y-axis to avoid sliding losses), with reduced rolling friction (0.0005) so it keeps speed. With the ball at 5 m/s striking the 0.2 kg bottom block, I'm estimating it'll shoot out from under the stack while the upper blocks drop and hopefully remain standing upright.

But I realize the ball may continue forward and collide with the falling stack mid-drop, knocking it sideways instead of leaving it standing — so maybe hitting the bottom block off-center to induce spin/tilt would produce a cleaner toppling motion instead.

Thinking about the tipping physics: if I give the base block a sudden impulsive acceleration, the upper stack's inertia tends to tip it backward around the contact edge, provided the required tipping acceleration (roughly g times half-width over height of the center of mass) is exceeded — and given how large an impact-driven acceleration would be, toppling should occur as long as inter-block friction transmits enough force.

But I also realize tipping needs friction above about 0.25, which 0.6 easily satisfies — the issue is the impulse needs to be sustained long enough to carry the rotation past the tipping point, not just a brief nudge. So instead of a quick strike, I should have a heavier ball continuously pushing block1 along the floor, since its momentum (roughly 6 kg·m/s at 3 m/s) should outlast the floor's frictional resistance on the lighter block and keep driving it forward.

Let me settle on parameters: ball at 3 kg, 4 m/s, spinning 80 rad/s, with 0.9 friction blocks made taller and lighter (8x8x12 cm, 150 g) to topple more easily in a 60 cm stack. I'll position the ball further back, around -1.5 m, so it travels a full 3 m before impact, giving the stack time to settle and stand before the collision.

