Ball1 starts rolling (launch plus matching spin) and knocks the speed down the row. The cup is an open box with a low 8 mm front lip that the rolling ball3 can climb. Its heavier rolling resistance stops the ball inside before it can get back out.

```world
world  three balls and a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ball1
  is a      sphere 4 cm radius, 170 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    orange
  moves     freely
  rests     on floor
  launched  1.4 m/s along
  spins     35 rad/s about y

ball2
  is a      sphere 4 cm radius, 170 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    white
  moves     freely
  rests     on floor, 30 cm beyond ball1

ball3
  is a      sphere 4 cm radius, 170 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    grey
  moves     freely
  rests     on floor, 30 cm beyond ball2

-- an open box with a low front lip the rolling ball can climb;
-- high rolling resistance inside stops the ball before it reaches the far wall
cup
  is an             open box
  length            40 cm
  width             30 cm
  walls             10 cm
  base thickness    3 mm
  near wall height  8 mm
  friction          0.8, spinning 0.005, rolling 0.015
  bounce            dead
  colour            wood
  its base 1.06 m beyond ball1

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

---
thinking (summarized):

I'm planning a sequence of three balls where ball1 strikes ball2, transferring velocity via an elastic collision with equal masses, and ball2 then strikes ball3, accounting for rolling physics where the struck ball slides before settling into rolling at 5/7 its initial speed, so ball3 ends up rolling into and resting in the cup.

Now I'm thinking through how ball3 physically enters a cup sitting on the floor — since a rolling ball generally can't climb over a wall taller than a small fraction of its radius, I'm considering making the cup's near wall very low, roughly matching the thickness of the cup's base, so the step up is just a few millimeters and the ball can roll over it smoothly rather than being blocked.

Maybe a raised platform is overkill; perhaps a low-lipped cup is fine if I check the actual step-climbing physics. I'm working out whether a ball rolling at speed v can climb a step of height h using angular momentum conservation about the step edge, comparing rotational energy before and after impact to see if it clears the lip.

Thinking through the lip geometry: with a 5mm base thickness and 1.5cm cup height, the inner lip sits about 1cm above the ball's resting point, so a dead-bounce return probably can't clear it — promising but uncertain.

I'm also considering a more robust alternative design: an open box with a gentle ramp leading up to the rim, where ball3 rolls up and falls in. But the ramp's geometry is ambiguous since plank thickness and placement relative to the floor aren't well defined, so the exact height the ball needs to climb is unclear.

Trying a cleaner setup instead: a shallow box with a thin 2mm base, 1.5cm walls, and 8cm span, with a 4cm ball needing to climb that 1.5cm lip — working out that the ball's velocity after the climb would be reduced to about 73% of its original speed.

Using energy balance to find the minimum incoming speed, I get v ≥ roughly 0.63 m/s for the ball to crest the near wall and land inside the cup; past the far wall it just rebounds weakly. I also need to think through rolling versus sliding — if the ball is rolling without slipping, its spin rate about the axis perpendicular to its motion should equal v/r.

For the collision with the second ball, since this is an elastic head-on collision between equal masses, ball 1 stops translating but keeps spinning, so friction then accelerates it forward to 2/7 of its original speed. Meanwhile ball 2 shoots off at the original speed with no spin and starts sliding before rolling takes over.

But real contacts in MuJoCo aren't perfectly elastic unless I tune solref/solimp for bounciness, so I need to account for energy loss there — chained collisions through ball2 hitting ball3 will compound this, needing the initial velocity to be large enough (roughly 1.5-2 m/s) for ball3 to still move meaningfully after all the inelastic losses.

I'm worried about the lively-dead material mismatch when ball3 bounces inside the cup — unclear how MuJoCo mixes solref values between a lively ball and dead cup walls, so maybe I should avoid relying on bounce dynamics entirely. Instead I could tune the entry speed so ball3 just barely crests the lip with minimal residual speed, or lengthen the cup and rely on rolling friction to kill momentum before it reaches the far wall.

Rolling friction with condim 6 looks like the right lever: computing deceleration from μ_r*g/r, a value like 0.03-0.05 rolling coefficient on the cup geom gives decelerations in the 5-9 m/s² range, which should be enough to settle a ball entering around 0.6 m/s within the cup length, since contact friction combination takes the max across geoms and only the ball needs condim 6 set via "rolls".

Working through the lip height needed for the ball to climb over: with a 1.5 cm lip, I calculate the ball needs roughly 0.63 m/s at minimum, so I'll set a target speed near 1.0 m/s to clear it with margin, checking the energy balance after it crests the edge.

After cresting, the ball drops into the cup at around 0.6 m/s, then rolling friction decelerates it quickly—stopping within about 10 cm given a 40 cm cup length. I'm worried that after bouncing around, it won't retain enough speed to climb back out over the 1 cm inner lip, so I need to reconsider whether rolling friction during the climb itself (contact between ball and cup edge) makes this escape even less likely.

Checking whether MuJoCo's rolling friction actually opposes angular velocity relative to tangential contact—yes, it resists relative rotation, confirming my deceleration estimates. Then I'm computing floor friction effects: with rolling coefficient 0.002, deceleration comes out to about 0.35 m/s², which over a 1 m distance at roughly 1 m/s could cut velocity-squared by 0.7, a meaningful loss. This tells me I should keep travel distances short and tune both the ball's and floor's rolling friction values down, maybe to 0.001 each, to preserve enough momentum for the ball to complete its path.

Settling on friction 0.8, spinning 0.005, and rolling 0.0005 for both floor and balls gives a gentler floor deceleration around 0.09 m/s², which should be fine. For collision elasticity, I want lively bounces between balls (near elastic) but a deader bounce for ball-cup contact—MuJoCo averages solref/solimp via solmix when priorities match, so the mixed values should work out reasonably, though the soft contact model means energy transfer won't be perfectly elastic.

Working through spacing: balls at 4cm radius, positioned at x=0, 0.3, 0.6, with the cup near the wall around x≈1.0. After a hit, the sliding-to-rolling transition takes about 0.06s and covers roughly 0.09m, so by the time ball2 reaches ball3 it's already rolling at 5/7 speed. Launching ball1 at v0=2.0 m/s, I estimate ball2 ends up around 1.43 m/s and ball3 around 1.02 m/s after accounting for the (5/7)² scaling and some additional losses.

Now checking whether ball3's speed survives hitting the cup's lip, I'm computing the velocity after the lip collision and whether it has enough energy to climb the 0.01m rim—running the numbers for both the lower (0.83 m/s) and higher (1.02 m/s) speed cases to see if the ball makes it over or stays trapped inside the cup afterward.

I also need to trace balls 1 and 2 through their subsequent collisions: ball1 retains 2/7 of the initial speed after the first hit and catches up to ball2, transferring momentum again, while ball2's resulting speed after hitting ball3 falls below the 0.63 m/s threshold needed to clear the lip — meaning they'd likely bounce back rather than climb in.

Now I'm working out how to position the cup geometrically — it's 30 cm wide with 10 cm walls, centered on the ball's path, and I need to figure out how to anchor the open-box part (specifying its base or rim relative to the ball's position) so it sits correctly on the floor at the right distance.

I'm calculating that if the base sits at 1.07 m beyond ball1, with base length 44 cm, the near wall edge lands around 0.84-0.86 m, leaving about a 20 cm gap from ball3's front edge at 0.64 m, which works. I'm also confirming default wall thickness (2 cm) and checking the various part thicknesses — base, walls, height, length, width — to make sure everything fits together properly.

For ball placement, I'll set ball1 on the floor, then position ball2 and ball3 each 30 cm beyond the previous one, treating "beyond" as an along-axis offset. I'm also noting ball mass and spin — a 4 cm radius sphere weighing 170 g, with ball1 spinning at 50 rad/s about the y-axis.

Launching at 2 m/s along the track, I'm reconsidering whether the balls should roll to rest naturally given rolling friction, with ball1 touching ball2 and ball2 touching ball3, and ball3 settling in the cup within the expected time. But I'm now second-guessing my step-collision assumption: when the lively ball hits the step's lip, the contact normal points from the edge toward the ball's center at an angle, so an elastic bounce would reflect the ball backward rather than let it climb over — meaning my earlier assumption of a perfectly inelastic impact at that contact point may be wrong.

With a lively ball, that normal component reverses substantially, giving significant horizontal rebound — which breaks the climbing behavior I wanted. I'm weighing whether to drop the "lively" setting and rely on default MuJoCo contact parameters instead, since their default damping ratio of 1 might produce nearly inelastic collisions and avoid this rebound problem.

Actually, maybe I can sidestep the step-climbing problem entirely — with rolling friction around 0.02 in the cup, a ball entering at 0.8 m/s decelerates fast enough (~3.4 m/s²) to stop within about 9 cm, well before reaching the far wall, so it never needs to roll back out or climb anything. That makes the near-wall step height mostly irrelevant since the ball settles before any rebound matters.

Still, a cup without a front lip feels odd, so I'll settle on an 8mm lip with 3mm base thickness and 0.015 rolling friction. Checking the climbing physics: a ball with radius 4 climbing an 8mm step needs velocity around 0.39 m/s minimum, and since the expected incoming speed is about 0.8 m/s, there's comfortable margin even accounting for partial energy loss on rebound.

But now I realize the earlier balls following at 0.4-0.57 m/s could also climb the lip and enter the cup, which isn't ideal since the brief wants only the third ball inside. I need to rework the spacing or friction so trailing balls don't reach the cup threshold with enough speed to climb in.

Checking whether ball3 clears the 0.2 m gap to the cup with v²=0.28, which works out, then tracing ball1's path from launch through collision at x≈0.22 traveling to x≈0.44, and ball2's path after hitting ball3 traveling to x≈0.63 — trying to see if ball1 catches up to ball2 before it stops.

None of the balls actually reach the cup at 0.84. Now I'm setting friction values for the floor and balls (sliding, spinning, rolling coefficients) and the cup's rolling friction, confirming ball-ball and resting-ball collisions are fine, and calculating the spin rate of 35 rad/s from the 1.4 m/s launch speed over a 4 cm radius. I'm also checking the cup geometry — thin base and wall thicknesses — and figuring out where the cup's near wall sits relative to ball1's position to confirm placement is reasonable.

Checking ball3's position relative to the cup gives roughly a 21 cm gap, and I need to confirm it comes to rest within the cup's footprint, which should be fine. Time to write it all out.

