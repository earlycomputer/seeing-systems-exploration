The pendulum is a 300 g bob on a 50 m-long... correction, a 50 cm hinge, started 40° back. It hits a 50 g rolling ball near its equator at the bottom of its swing. The ball rolls about 0.85 m on low rolling friction and climbs an 8 mm lip into a low-walled cup. The cup's walls are `dead`, and its base has strong rolling friction so the ball stops inside.

These numbers are back-of-envelope estimates, not a simulation result:
- **Bob speed:** about 1.5 m/s at the bottom of the swing.
- **Ball after the hit:** about 0.9–1.8 m/s once it settles into rolling.
- **Speed at the lip:** about 0.8–1.8 m/s.
- **Speed needed:** about 0.4 m/s to climb the lip.
- **Biggest uncertainty:** how elastic the bob–ball contact is in MuJoCo. That is why I aimed for a fairly wide speed range.

```world
world  pendulum strikes ball into cup

floor
  size      6 m
  friction  0.8, spinning 0.002, rolling 0.0005

pivot
  is a  point
  at    53.2 cm up

pendulum
  is a           sphere 3 cm radius, 300 g
  colour         grey
  50 cm below pivot
  turns on       pendulum hinge, about y, at pivot
  starts turned  40°

pendulum rod
  is a         rod 1 cm thick, from pivot to pendulum's top
  weighs       20 g
  colour       grey
  attached to  pendulum

stand arm
  is a    box 4 by 30 by 4 cm
  colour  wood
  touches nothing
  4 cm above pivot, its left side at pivot

stand post
  is a    post 6 cm square, from floor to stand arm's top
  colour  wood
  touches nothing
  centred on stand arm's right side

ball
  is a      sphere 3 cm radius, 50 g
  rolls
  friction  0.8, spinning 0.002, rolling 0.0005
  colour    orange
  moves     freely
  rests     on floor, 6.2 cm along

cup
  is an             open box
  length            24 cm
  width             20 cm
  walls             8 cm
  wall thickness    1 cm
  base thickness    3 mm
  near wall height  8 mm
  friction          0.8, spinning 0.01, rolling 0.01
  bounce            dead
  colour            white
  its base 1 m beyond ball

expect
  ball touches pendulum
  ball comes to rest in cup
```

---
thinking (summarized):

I'm working out the physics and geometry setup for a pendulum that strikes a ball, which then rolls one meter into a cup — figuring out pivot height, bob size, swing length, and how to name and hinge the pendulum part correctly.

For the rotation, I'm calculating that swinging about the y-axis with the bob starting at a positive angle will pull it back along -x before swinging forward along +x to strike the ball, which I'm placing on the floor ahead with its center aligned to the bob's lowest swing point.

I'm also checking whether a floor collision would interfere—since the pendulum body's parent is the worldbody, I need to verify whether MuJoCo's parent-child contact filtering actually excludes world-attached bodies from floor contact, since I recall the filter may not apply when the parent is specifically the world.

To avoid issues, I'll size the bob slightly smaller than or equal to the ball with a small clearance above the floor, so it strikes near the ball's center without touching ground. Now I'm thinking about the broader mechanics: for the ball to roll and stop precisely in a cup, equal masses would give a clean elastic transfer, but a cup with raised walls is problematic since a rolling ball can't climb over them—so I need another way to contain it, like sinking the cup or using a different stopping mechanism.

Maybe a low wall around 1 cm could work if the ball has enough speed to roll over the edge, though friction could make it bounce unpredictably, and I also need to account for the base thickness being an obstacle itself—so I should keep the base and wall height minimal, perhaps a few millimeters. Alternatively, I'm considering a ring-shaped cup lying flat on the floor, essentially a shallow hoop that the ball settles into without needing to climb anything.

I think the cleanest design is an open box with a short, ramp-like near wall and taller far/side walls, so the ball rolls over the low lip, loses energy hitting the far wall, and settles inside the base—success being measured by the ball coming to rest within the cup's footprint. The tricky part is figuring out the minimum speed needed for a 3 cm radius ball to clear a small step height without just bouncing back out.

I'm working through the physics of a rolling ball striking a low step edge: using angular momentum conservation about the edge to find the ball's rotation rate after impact, then checking whether its kinetic energy is enough to lift it over a step of a given height.

After confirming the ball needs just over 0.3 m/s to climb that step, I'm now considering what happens once it's inside the cup — rolling across the base, bouncing off the far wall, and returning to hit the near lip, where I need to account for the relative heights of the base and the near wall from the floor.

Maybe rolling friction is the better tool here—letting the ball lose speed naturally as it travels so it arrives at the cup slow enough to climb the near lip but not enough to escape over the far wall. I'm working out the deceleration from a rolling friction coefficient, estimating something like μ_r=0.002 gives a gentle enough slowdown over the rolling distance to tune the final approach speed.

Given the uncertainty in exact dynamics, I should just keep rolling friction modest and lean on the cup geometry to trap the ball across a range of arrival speeds. The tricky case is a fast arrival where the ball hops the lip and bounces off the far wall — with a dead bounce the normal velocity gets absorbed but forward spin keeps pressing the ball into the wall until friction kills the spin and it settles.

I'll make the far wall tall enough (taller than the ball's 6cm diameter) and the cup long enough that even a slight hop from hitting an 8mm lip at 1.5 m/s stays contained. Then I pick low rolling friction values on both ball and floor to minimize sensitivity to arrival speed, checking that the resulting deceleration over the travel distance keeps final velocities within a safe, cup-trappable range.

Also I need to account for the ball not spinning initially after impact—friction has to convert sliding into rolling, which reduces effective speed to 5/7 of the post-impact value, and the pendulum strikes slightly above the ball's center which is a minor effect. The bigger concern is that MuJoCo's default contact solref behaves as nearly inelastic, so "bounce lively" likely means tuning solref damping down to get a livelier, less damped collision response.

I'll make the bob significantly heavier than the ball—say 300 g vs 50 g—so the ball comes away with solid speed regardless of whether the collision leans elastic or inelastic, and this gives roughly a factor-of-two range in outcome velocity depending on restitution, which should still land ball rolling speed in a workable range.

Checking whether that speed survives friction losses before reaching the lip, I realize the lower end of the range might actually stall the ball out entirely since the velocity-squared loss term can exceed the starting kinetic term, so I need to bump up the bob's release velocity to around 1.4 m/s to keep a margin of safety across the whole range of friction and collision scenarios.

I could set cup rolling friction high, like 0.01, which applies across all cup geoms including near the wall. That gives strong deceleration inside the cup—roughly 2.3 m/s² over 15 cm, enough to kill velocity squared by 0.7, which really helps trap the ball. I'll keep floor rolling friction at 0.0005, ball rolling at 0.0005, cup rolling at 0.01, and set floor sliding friction around 0.8 with zero spinning friction.

For the pendulum, I'm working out the release angle to hit a bob speed near 1.4 m/s using energy conservation: with rod length 0.5 m, I need 1-cosθ ≈ 0.2, giving θ around 37°, but adjusting to 40° to account for rod mass and inertia effects gives v ≈ 1.52 m/s, which is close enough since the rod is light relative to the 300 g bob. Then I'm estimating the ball's rolling resistance deceleration at the start, factoring in the 5/7 rolling coefficient.

Now I'm checking the ball's arrival speed after friction losses, landing somewhere around 0.7–1.8 m/s depending on assumptions, and worrying whether the upper end might cause it to hop over the far wall given the 8 mm lip and 6 cm wall height — so I'm considering raising the walls to 8 cm to be safe. I'm also thinking through whether the dead-bounce contact model in MuJoCo will behave reasonably at these speeds, and whether I should instead dial back the bob's release speed to avoid edge cases.

With the default critically-damped contact settings, restitution should be close to zero, meaning the ball and bob likely stay in contact longer, with the ball picking up velocity close to the bob's speed as it decelerates through the swing.

I'm estimating the ball starts sliding around 1.3 m/s, then friction brings it to rolling speed near 0.93 m/s, factoring in the 5/7 rolling conversion. Running the numbers for the inelastic case gives roughly 0.81 m/s at arrival after accounting for height loss, while a more elastic contact scenario would push that closer to 1.85 m/s—so I need to decide how lively to make the ball versus the cup and bob to land in a believable range, keeping the cup itself non-bouncy.

Now I'm working out the strike geometry: positioning the bob directly below the pivot at the bottom of its swing and placing the ball just ahead of it, accounting for their radii and a small gap of a couple millimeters so contact happens near the ball's equator without the bob needing to be exactly at dead center.

I also need to add a physical stand (post and crossbar) to visually anchor the pivot without interfering with the swing, but I'm realizing the rod connecting to the bob might physically collide with the crossbar near the pivot point since they'd occupy the same space — need to check how the physics library handles that collision.

Making both touches nothing is safest. Rather than relying on a pendulum library, I'll build my own parts directly — naming the body "pendulum" so it satisfies the hinge requirement, placing the pivot point up and across with explicit coordinates, then defining the bob as a sphere attached via rod.

For positioning the bob, I'm reasoning through how "below pivot" sets vertical offset, keeping pivot coordinates at the origin so along/across defaults align regardless. I'm setting up the hinge rotation about the y-axis at the pivot, an initial 40° turn angle, grey coloring, then defining the connecting rod between pivot and bob.

For the stand arm, I'm working through its placement relative to the pendulum rod's top, trying to figure out how "on pendulum rod" and "its left side at pivot" translate into across/along offsets, considering whether a simpler absolute position phrasing might work better.

Switching to "4 cm above pivot, its left side at pivot" to avoid overlap, so the arm sits clear of the rod capsule. Then I'm positioning the stand post, 6 cm square, running from floor to the arm's top, centered on the arm's right side with no touches. Finally setting up the ball — 3 cm radius sphere, 50 g, rolling with friction 0.8 and some spin.

Now I'm placing the ball on the floor, 6.2 cm from the pendulum, accounting for bob radius plus ball radius plus a small gap, giving an absolute x position. I'm also checking the bob's starting coordinates given the 40° tilt to confirm it clears the floor, and verifying the rod doesn't collide with the ball once brought down.

Next I'm working out the cup's placement: an open box roughly 24×20×8 cm with 1 cm walls and a thin base, positioned about 1 m from the ball's start so its near wall and base sit correctly relative to the ball's trajectory.

I'm calculating the geometry of where the ball meets the near wall's lip — checking the height of the step the ball sees at the wall and the position at which the ball's circumference first contacts that edge.

Then I'm verifying the ball can climb over the small step at the wall: computing the required velocity using energy and rotational inertia terms, finding it needs roughly 0.41 m/s, and confirming the estimated arrival speed gives enough margin given the rolling friction at the wall edge.

Moving inside, I check the ball's deceleration across the base (2.3 m/s² over 22 cm) and confirm it still clears the far wall above 1 m/s before dead-bouncing, with escape back over the 5mm lip unlikely afterward. I also confirm the bob geometry — pivot height, arm length, and sphere radius — lines up so the bob sits just above the floor as intended.

The bob's density checks out fine for its mass and radius. After the strike, the pendulum swings through a full period and returns to the bottom well after the ball has already moved away, so no re-collision. The slight height mismatch between bob center and ball just pushes the ball gently into the floor, which is fine, and I'm naming colors for the cup, ball, pendulum, and stand, then noting the event label should read "ball touches pendulum" rather than ramp.

Now I'm working out the position syntax for the pendulum rod and cup — using bare position lines like "50 cm below pivot" to match the library's format, sizing the floor at 6 meters, and defining the rod from pivot to pendulum top. For the cup, I'm specifying it as an open box with given length, width, wall height, wall thickness, and base thickness, then positioning it near the wall.

I'm adding friction, bounce, and color properties for the cup, and placing its base 1 meter beyond the ball, keeping key/value lines separated by two spaces. I'm double-checking that the near wall and side walls fit properly around the base without causing overlap issues near the ball's position, then finalizing the setup.

