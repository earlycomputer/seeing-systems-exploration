**What happens in the run**

The pendulum swings down correctly and reaches the ball at about 0.31 s. The strike transfers almost nothing: the ball leaves at only 0.39 m/s, and the pendulum, which carried about 0.7 J, is left swinging just ±6°.

The ball rolls slowly forward and reaches the cup's 1.5 cm lip at 2.82 s, travelling 0.27 m/s. That is too slow to climb the lip, so the ball bounces back off it. It is still drifting backward, away from the cup, at the end.

**Why the strike failed**

Momentum went missing in the strike, so most of it must have gone into the floor. The likely cause is friction where the pendulum meets the ball.

1. As the ball starts to roll, its back surface slides upward against the pendulum.
2. Friction there (about μ 1) drives the ball down into the floor.
3. Floor friction then rises sharply and resists the ball's forward motion.

**Fix**

- Give both the ball and the pendulum low sliding friction. The floor keeps μ 0.8, so the ball still rolls properly; this assumes contacts take the larger of the two friction values.
- Lower the striking tip to the ball's centre height, so the push is horizontal.
- Raise the cup's back and side walls to 15 cm, so a faster ball that hops the lip can't clear them.

```parts
part low cup
  needs  length
  needs  width
  needs  walls
  needs  lip height
  needs  wall thickness, else 1 cm
  needs  base thickness, else 2 mm

  base
    is a  box length by width by base thickness
    on    floor
  near wall
    is a  box wall thickness by width by lip height
    on    floor, centred on base's near end
  far wall
    is a    box wall thickness by width by walls
    on      floor, centred on base's far end
    bounce  dead
  left wall
    is a    box length by wall thickness by walls
    on      floor, centred on base's left side
    bounce  dead
  right wall
    is a    box length by wall thickness by walls
    on      floor, centred on base's right side
    bounce  dead
```

```world
world  pendulum knocks a ball into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.001

-- low sliding friction on the ball, so the pendulum can't drag it into the floor;
-- the floor's 0.8 still governs ball-floor contact, so it rolls
ball
  is a      sphere 5 cm radius, 100 g
  rolls
  friction  0.05, spinning 0.005, rolling 0.001
  colour    orange
  moves     freely
  rests     on floor, 1 m along

pivot
  is a  point
  at    7.5 cm behind ball, 55 cm up

pendulum foot
  is a  point
  at    7.5 cm behind ball, 5 cm up

-- one heavy rod, pivoted at its top; its rounded lower end is level with the ball's centre, 5 mm short of it
pendulum
  is a           rod 4 cm thick, from pivot to pendulum foot
  weighs         1.2 kg
  friction       0.05, spinning 0.001, rolling 0.0001
  colour         grey
  turns on       swing, about y, at pivot
  starts turned  40°

stand beam
  is a    box 4 by 16 by 4 cm
  colour  wood
  at      7.5 cm behind ball, 12 cm to the left, level with pivot

stand post
  is a    box 4 by 4 by 57 cm
  colour  wood
  stands  on floor, 7.5 cm behind ball, 22 cm to the left

cup
  is a         low cup
  length       20 cm
  width        20 cm
  walls        15 cm
  lip height   1.5 cm
  its base 1 m beyond ball

expect
  ball touches pendulum
  ball comes to rest in cup
```

```json
{"what_happens": "The pendulum swings down and strikes the ball at 0.31 s, but nearly all its energy is lost in the strike: the ball leaves at only 0.39 m/s while the pendulum is left swinging ±6°. The ball rolls slowly to the cup, reaches the 1.5 cm lip at 2.82 s at 0.27 m/s, bounces back off it, and is still drifting backward away from the cup at 6 s.", "works": false, "problem": "The strike transfers too little speed, apparently because friction between pendulum and ball drives the ball into the floor, so the ball arrives too slowly to climb the cup's lip and never gets in."}
```

---
thinking (summarized):

This time the ball only reached 0.39 m/s, far too slow, and it rolled toward the wall near the 1.9 m mark, hitting the lip at just 0.27 m/s before bouncing back — a failure. I'm wondering why the pendulum transfer is losing so much energy.

Checking the amplitude ratio after impact, the pendulum retains only about 2.6% of its initial energy, which implies a massive loss during the strike — far more than the ball gained as kinetic energy. I suspect the geometry of the contact is the culprit: the rod's endpoint sphere may be striking the ball at an angle that pushes it downward into the floor rather than straight forward, causing the ball to get squeezed and losing energy to friction instead of being cleanly launched.

The ball only reached 0.4 m/s instead of the expected inelastic momentum-sharing speed of roughly 1.48 m/s, so a lot of energy vanished — maybe the floor is absorbing it if the ball gets pinned against the ground during contact, or the condim/rolling friction settings are bleeding off velocity.

I'm also checking whether the pendulum's angular velocity trajectory (dropping from 40° to 10.7° with ω around -201°/s) matches the free-pendulum energy equation ω² = 3g(cosθ − cos40°)/L, to see if the rod itself is behaving as expected before and after the collision.

Since the physics checks out for the pendulum alone, the energy loss must be happening at the contact point. I'm now considering that even with low rolling friction, the geometry of the contact—the ball's sphere center position relative to the floor—could create a downward force component that's draining energy from the system.

Actually contact happens just past bottom dead center, around −0.7°, nearly horizontal. But the momentum numbers don't add up — the pendulum tip carries much more momentum than the ball ends up with, so something besides the pendulum-ball collision must be absorbing energy, maybe the floor contact through the ball itself.

I'm wondering if condim 6 rolling/torsional friction defaults are sapping energy, or if sliding friction at the pendulum tip against the ball is draining momentum since the tip contacts at a slight angle. I don't have a clean diagnosis yet — practically, the strike just loses too much energy, so I should think about this differently rather than keep chasing the exact friction term.

Momentum isn't conserved without an external impulse, so the hinge must be supplying one to the pendulum. Computing the pendulum's angular momentum loss about the pivot and converting that to an impulse at the tip, I get about 0.62 N·s transferred, which seems too large for the ball's resulting momentum gain—suggesting something's off in how the contact impulse is being applied.

Maybe the capsule caps extend beyond the given endpoints, putting the rod's bottom lower than I assumed, around 4 cm, with the ball's top at 10 cm. Then I should consider how floor friction interacts with the ball being struck above its center, causing it to both slide and spin as friction resists the horizontal push.

Maybe I should step back from the exact strike physics and instead make the design robust by lowering the entry lip significantly, say to 3mm, so even a slow 0.27 m/s ball can clear it—though the math comes out marginal, and I still need to worry about the ball bouncing back out off the far wall.

I'm also considering repositioning the pendulum's strike point so the bob contacts the ball closer to its center height, making the impact force more purely horizontal rather than imparting unwanted vertical components.

I should also look at friction at the contact point—with μ near 1, the tangential force could end up acting vertically rather than horizontally if the pendulum tip slides against the ball's surface in that direction, which might explain the unexpected bounce-back behavior.

That's the feedback loop killing momentum. Since MuJoCo combines friction by taking the max, I should lower the ball's own friction and the pendulum's friction to something small like 0.05, letting the floor's 0.8 friction dominate for rolling while keeping ball-pendulum contact closer to frictionless sliding.

For placement, I need the pivot roughly 7.5 cm behind the ball so the strike happens near horizontal, with only a tiny angular offset causing negligible vertical rise at contact — keeping the collision effectively a clean horizontal strike. I'm estimating the resulting ball speed should land around 1.48 m/s for an inelastic-style strike, then transitioning from sliding to rolling.

I'm checking whether the ball retains enough speed to climb the cup's lip (needs roughly 0.53-0.58 m/s depending on step height), and whether a bounce off the dead far wall would send it back with near-zero rebound, with spin helping nudge it forward afterward. I'm also confirming friction interactions at the lip use the higher coefficient between ball and wall, and noting the pendulum won't interfere again once the ball has moved on.

If the collision is elastic instead, the ball could still be moving around 2 m/s when it reaches the lip, which raises the possibility it hops over the edge entirely rather than settling — so I'm working out the launch angle and height from climbing a 1.5 cm edge at that speed to see if it clears the 10 cm far wall.

