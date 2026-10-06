The pendulum hangs just behind the ball and starts swung back 45°. The cup is a custom part with a low 1.5 cm lip that the rolling ball can climb, and tall dead walls on its other three sides that it can't. The cup is centred 1 m beyond the ball's start.

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

ball
  is a      sphere 5 cm radius, 100 g
  rolls
  friction  0.8, spinning 0.005, rolling 0.001
  colour    orange
  moves     freely
  rests     on floor, 1 m along

pivot
  is a  point
  at    9.5 cm behind ball, 56 cm up

-- the bob: hangs 50 cm below the pivot, centre 6 cm up, 5.5 mm short of the ball
pendulum
  is a           sphere 4 cm radius, 400 g
  colour         grey
  50 cm below pivot, 9.5 cm behind ball
  turns on       pendulum hinge, about y, at pivot
  starts turned  45°

pendulum rod
  is a         rod 1 cm thick, from pivot to pendulum's top
  weighs       20 g
  colour       dark grey
  attached to  pendulum

stand beam
  is a    box 4 by 16 by 4 cm
  colour  wood
  at      9.5 cm behind ball, 12 cm to the left, level with pivot

stand post
  is a    box 4 by 4 by 58 cm
  colour  wood
  stands  on floor, 9.5 cm behind ball, 22 cm to the left

cup
  is a         low cup
  length       20 cm
  width        20 cm
  walls        10 cm
  lip height   1.5 cm
  its base 1 m beyond ball

expect
  ball touches pendulum
  ball comes to rest in cup
```

**How it is meant to work**

- **The swing.** A positive turn about y swings the bob back along −x. Released from 45° on a 50 cm arm, the bob reaches about 1.7 m/s at the bottom of its swing.
- **The strike.** The bob is four times the ball's mass and hits slightly above the ball's centre.
- **The roll.** The ball should come out rolling at roughly 1–2 m/s. Rolling friction is low, so it should still be well above the speed needed to hop the lip, about 0.6 m/s, when it reaches the cup.
- **Staying in.** Inside the cup, the dead far wall soaks up the ball's speed. The 10 cm walls are far too tall to roll over.

**What I haven't checked**

- I haven't run this, so the exact speeds are estimates.
- The biggest uncertainty is how elastic MuJoCo's default contact makes the strike.
- If the ball comes up short of the lip, increase `starts turned`.
- If the ball bounces back out over the lip, lower the angle.

---
thinking (summarized):

I'm working out the pendulum structure—placing the pivot and bob, and figuring out how the hinge joint should be named and configured so the part labeled "pendulum" swings correctly.

Now I'm figuring out the starting position of the pendulum relative to the ball and cup: the bob should hang displaced backward at rest so it swings forward to strike the ball, so I'm computing the rotation of the rod vector about the hinge axis to get the initial angle.

The trickier problem is the cup itself—since the ball rolls along the floor, it can't climb a wall into a raised cup, so I need to think about whether the cup's near wall should be very low or whether some other mechanism gets the ball to stop inside it.

The ball still risks bouncing back out over the near wall with no friction to settle it. I'm reconsidering a cup shape — maybe a ramp or raised platform — but the floor-resting constraint rules out a sunken design, so I'm weighing a flat ring-based cup as an alternative.

I'm working through the physics of a ball climbing a low step or wall, using angular momentum conservation about the step's edge to figure out the minimum speed needed to clear a given height, factoring in the ball's rotational inertia.

So the ball barely clears the far wall at 0.64 m/s, which makes me reconsider the geometry — maybe the near wall should stay short while the far and side walls are taller at 5 cm, so the ball can't escape that way and will bounce back weakened. I also need to account for the base thickness of the box, maybe around 2mm, which affects how the 1.5cm near-wall step is measured relative to the floor.

I'm also estimating rolling friction effects in MuJoCo: with a rolling friction coefficient around 0.002 and standard combination rules, the deceleration on the ball works out to roughly 0.28 m/s², which factors into how much speed it loses crossing the floor.

Accounting for the slide-then-roll transition (where rolling velocity ends up at 5/7 of the initial strike velocity), I need to strike the ball faster than its final rolling speed. I'm leaning toward lowering the rolling friction coefficients on both the floor and ball to around 0.001 for more predictable, gentler deceleration.

Now I'm sizing the cup: a 20x20 cm open box with 5 cm walls, 1.5 cm wall height, 1 cm wall thickness, and a 2 mm base. I'm working out how to position it relative to the ball — placing its base 1 m beyond the ball along the direction of travel, keeping it centered across with no vertical offset since it rests on the floor.

For the ball, I'm thinking through a 5 cm radius sphere and estimating the pendulum collision physics: given bob mass, pendulum length, and release angle, I can compute impact speed at the bottom, then consider how an elastic versus MuJoCo's typically inelastic contact model would transfer momentum to the ball.

Checking the rolling condition against the rotational factor gives a required speed of roughly 2.9 m/s, which seems achievable. Then I'm working through what happens when the ball hits the far wall — since the ball's center sits slightly above the wall's top edge, the contact normal points a bit upward, meaning the bounce would nudge the ball up rather than send it straight back.

Actually, that means the ball could potentially climb right over the wall instead of bouncing off it, since the wall height is less than the ball's radius. I'm checking whether a taller wall (8 cm) would prevent that climbing scenario entirely, while also thinking about how to make the ball's bounce lively but the cup's material feel dead on impact.

Since MuJoCo applies default near-critically-damped contact parameters, the collision between ball and bob is essentially inelastic rather than bouncy—so after impact they'd move together at a shared velocity of about 0.75v, with the bob swinging up under gravity while the ball continues sliding and decelerating due to floor friction.

If I instead tried to make the ball lively/bouncy for a more definite impact, that would also make it bounce unpredictably off the floor and far wall, which could send it back toward the near wall—not what I want.

Maybe instead make the back wall of the cup "dead" so it absorbs the impact entirely, stopping the ball from bouncing back out over the lip, while leaving the ball itself default. With a dead wall, spin from rolling could still drive the ball forward again via friction with the base, but without that reverse momentum it shouldn't have enough speed to clear the 1.3 cm lip.

Now I'm sketching the physical dimensions: a 5 cm radius, 100 g ball, and a bob sphere of radius 4 cm, 400 g, placed with its center 6 cm up so it doesn't scrape the floor and strikes the ball slightly above center for a bit of topspin. The offset between centers works out to be mostly horizontal with a small downward component, which should be fine.

For the pendulum setup, I'm giving the bob a 0.5 m rod length, swinging from about 50°, which works out to roughly 1.87 m/s at impact — with a thin, light 20 g rod so it doesn't add much extra mass to the system.

Working through the collision: with a 400g to 100g mass ratio, inelastic impact drops velocity to around 1.5 m/s sliding, settling to about 1.07 m/s once it starts rolling (or closer to 2.1 m/s rolling if the collision is more elastic). Accounting for rolling friction over roughly a meter of travel, the ball should arrive at the lip with speed still in the 1-2 m/s range, enough to climb but hit the far wall at low enough speed that contact restitution in MuJoCo shouldn't cause it to bounce back out.

Trying a steeper 45° release angle instead gives a cleaner result: the swing produces about 1.69 m/s, which after an inelastic strike and transition to rolling settles around 0.97 m/s -- comfortably above the ~0.58 m/s threshold the ball needs to stay in the cup. I also want to check whether the pendulum bob, after releasing the ball, could swing back and strike it again, but since the ball has already left the area this shouldn't be an issue.

I work out the hinge geometry by confirming that a positive rotation about the y-axis moves the bob toward negative x, meaning a 45° starting angle places the bob properly behind the ball. Then I define the pendulum rod itself, about a centimeter thick running from the pivot to the top, weighing roughly 20 grams.

Now I'm thinking through how to support the pivot visually — adding a square post from the floor up to pivot height, offset to the side, plus a connecting beam box — while worrying whether that fixed support geometry might overlap or collide with the rod's capsule near the pivot point.

I'm second-guessing whether a support post is even necessary—a hinge anchored in the world could work physically without one, but it'd look odd visually. I'll try defining the post as a simple box resting on the floor, positioning it using absolute coordinates to align with the pivot height, and default the ball's position to rest on the floor at zero along.

Setting the ball explicitly at 1 m along, with the pivot placed 9.5 cm behind it and 56 cm up—then the pendulum bob hanging 50 cm below the pivot, relying on the "below" direction to only fix the vertical offset while along defaults to zero.

Checking the geometry: ball center sits 5 cm up since it rests on the floor, bob center lands at 6 cm, and the gap between surfaces works out to about 5.5 mm, which seems reasonable. I'm also sketching the rod running from the pivot down to the pendulum's top, with a 5 mm radius capsule extending slightly above the pivot.

For the stand, I'm placing a crossbeam box offset 9.5 cm behind the ball and 12 cm to the left, level with the pivot, plus a vertical post positioned further back and to the left so its top aligns with the beam. I'm checking for collisions — the beam sits high enough (54-58 cm) that it shouldn't intersect either the ball or the bob when the pendulum swings near the pivot.

Now I'm sketching out a "cup" part definition with needs for length, width, wall height, lip height, wall thickness, and base thickness, then renaming the "lip" need to "lip height" to avoid clashing with a piece of the same name. I'm laying out the base and four walls (near, far, left, right) with bounce applied to the far/left/right walls, positioning each wall centered on the appropriate edge of the base similar to an open box design.

I'm checking the ball's trajectory climbing over the near wall and settling onto the base, verifying it stays within the cup's interior bounds against the far wall, and considering renaming the part "low cup" to avoid naming collision with the "cup" object itself.

Pendulum period gives a quarter swing around 0.36 s, while the ball travels roughly a meter in about a second, so the whole sequence resolves within a couple seconds and settles comfortably inside my 6-second window.

Now I'm setting friction values for the ball and floor, keeping both low with small rolling and spinning coefficients. I'm sizing the ball at 100 g versus the 400 g bob, and thinking through how to phrase contact events like "ball touches pendulum" or the ball coming to rest in the cup, while also working out that after an inelastic strike the bob continues forward around 1.35 m/s and swings up roughly 9 cm.

I'm computing the swing angle from energy conservation, getting about 36 degrees and 0.29 m forward displacement, then comparing speeds — realizing that since the collision is inelastic, the bob and ball briefly share velocity before the ball's friction slows it to a rolling 0.97 m/s while the bob, decelerating more slowly, may catch up and strike the ball again.

Given the uncertainty in exact speeds, I'll just note the approximation and move forward with writing up the answer.

