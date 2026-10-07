The pendulum is a 1 m hinged bob turned back 60°, so it starts 1 m × (1 − cos 60°) = 0.5 m above its lowest point. That point is level with the ball centres on the rail. It reaches about 3.1 m/s and strikes `ball1`, the first of four equal balls set 15 cm apart. The impacts pass down the row, and `ball4` rolls off the rail end over a low near wall into a dead, high-rolling-friction box. I haven't run this; two assumptions need checking in the 6 s run:

- **Hinge direction.** I assumed a positive hinge angle swings the bob back (toward −x). If the compiler's sign is the other way, the bob would start ahead, inside the balls.
- **Balls 1–3 drifting.** The balls left spinning may creep after `ball4` and also land in the box. The box is sized and given friction so they should all settle too.

```world
world  pendulum chain into box

floor
  friction  0.8, spinning 0.005, rolling 0.002

pivot
  is a  point
  at    0 m along, 122.5 cm up

pendulum
  is a           sphere 2.5 cm radius, 100 g
  bounce         lively
  friction       0.8, spinning 0.005, rolling 0.002
  colour         grey
  1 m below pivot
  turns on       pendulum hinge, about y, at pivot
  starts turned  60°

pendulum rod
  is a         rod 1 cm thick, from pivot to pendulum's top
  weighs       10 g
  touches nothing
  colour       dark grey
  attached to  pendulum

rail
  is a      box 60 by 10 by 20 cm
  friction  0.8, spinning 0.005, rolling 0.001
  colour    wood
  stands    on floor, 34 cm along

ball
  is a      sphere 2.5 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.005, rolling 0.002
  colour    white
  moves     freely
  repeated  4 times, 15 cm apart along
  rests     on rail, 6 cm along

box
  is an            open box
  length           70 cm
  width            30 cm
  walls            25 cm
  near wall height  10 cm
  bounce           dead
  friction         0.9, spinning 0.02, rolling 0.02
  colour           grey
  rests            on floor, 100 cm along

expect
  pendulum touches ball1
  ball1 touches ball2
  ball2 touches ball3
  ball3 touches ball4
  ball4 comes to rest in box
```

---
thinking (summarized):

I'm setting up a Newton's cradle scenario: a pendulum dropped from 0.5m swings down to hit a line of balls spaced along a rail, calculating the impact velocity (~3.13 m/s) and working out the spacing needed so the chain reaction carries the last ball into a box.

I need to figure out how the pendulum hinge mechanism should be structured—likely as a primitive sphere turning on a hinge rather than using a prebuilt part, to keep naming clean. I'm also sketching the rail geometry as a long flat box to support the balls.

For the pendulum bob, I want its mass and radius to match the balls so momentum transfers cleanly, and I'm working out the geometry: choosing a pendulum length of 1 m gives a clean 60° release angle for a 0.5 m drop height, with the pivot positioned 1 m above the ball's center height. Now I'm working through the rotation direction convention about the hinge's y-axis to make sure the swing direction matches the intended strike direction.

With bob and ball radii both 2.5 cm, I place ball1 centered 5.5 cm from the pivot x for a small gap. After impact the pendulum settles since collisions aren't perfectly elastic in MuJoCo—ball1 slides off around 3 m/s, then friction brings it to rolling at 5/7 of that speed before it travels the 10 cm gap to hit ball2.

Ball1 might keep some spin and creep forward to hit ball2 again later, which is fine. I'm now thinking through ball4's exit speed (roughly 1.5-2.5 m/s) and how it needs to roll off the rail onto the floor and into an open box—making the rail and box base both 2 cm thick so the transition is seamless, while considering how the box wall doesn't block entry.

Actually, raising the rail higher so ball4 flies off the end and drops into the box seems cleaner: with a drop height around 10 cm, the ball would travel roughly 0.28-0.42 m horizontally depending on speed, so I can size a 60 cm box with a tall far wall to catch it and let it settle.

For resting behavior, I'm estimating rolling friction decay: with μ_r around 0.002 the deceleration is only about 0.56 m/s², taking roughly 2 s to stop from 1 m/s, so bumping the box's rolling friction coefficient to something like 0.01 would speed up settling to about 2.8 m/s² deceleration—though I need to check this doesn't also slow the ball down while it's still rolling on the rail.

I'm also considering whether ball4 will have enough speed from the pendulum impact (around 3.13 m/s) to actually reach the box after sliding and rolling losses, and whether balls 1-3, despite being nearly stationary after an elastic collision, might creep forward from residual spin and accidentally follow ball4 into the box—which seems mostly harmless for the goal but worth tracking.

Probably fine, rail friction should stop them in the box eventually, so I won't overengineer that part. Now I'm working out the physical layout: placing the rail as an elevated box roughly 80 by 10 by 20 cm, positioning the four balls along it with ball1 near x=5.5 cm and ball4 near x=50.5 cm, and setting the pivot and bob positions relative to the rail's top surface at ball-center height.

I need to make sure the swinging bob doesn't clip into the rail itself — since the bob's bottom edge sits right at rail height, the rail needs to start a bit further along (say x=3 cm) so the bob's arc clears it near the pivot before reaching the first ball.

Shifting the rail's near end to x=4 cm and the first ball to x=6 cm gives a safer 1 cm clearance. With four balls spaced 45 cm apart, the last ball lands around x=51 cm, so I'll size the rail from x=4 to x=64 cm, making it a 60 cm long box.

Now I need to figure out the catch box dimensions: after leaving the rail at 64 cm with some exit speed, the ball falls about 18 cm into the box, landing within roughly 0.19-0.48 m of travel. I'll set the box's near wall lower than the rail top so the ball clears it, sizing the box around 70 cm long with 25 cm tall walls starting at x=65.

I'm also working out how to phrase the placement syntax for positioning the box part on the floor relative to the ball's landing point, since I'm unsure whether to reference the base, rim, or some other anchor point in the description.

Settling on positioning the box at 100 cm along the floor with its base spanning 65 to 135, then placing the near wall centered on the base's near end so it fits snugly against the rail's far end at 64 cm. I'm positioning the rail at 34 cm along the floor, then setting up four balls repeated at 15 cm spacing along the rail, each 6 cm along and centered across.

For the pendulum, I'm defining a pivot point above the base, then hanging a sphere bob 1 m below it on a rotating hinge starting at 60° from vertical, connected by a thin rod from pivot to bob that adds 20 g of mass — keeping the bob's drop height fixed at 0.5 m despite the rod's added weight.

I'll keep the rod light enough and make sure it doesn't collide with anything, skipping any extra support frame since the pivot can stay fixed in midair. I'm also setting rolling and spinning friction values on the ball so the collision with the pendulum feels lively but realistic, accounting for the possibility of multiple bounces between bob and ball.

Checking box/ball friction combos (MuJoCo uses the max of components), I want the box's higher rolling friction to dominate and slow the ball quickly once inside, while the rail's lower friction barely affects it. I'm verifying ball4 clears the near wall given its fall time and speed, and confirming it won't bounce back out of the box given the wall height and ball size.

The sequence should play out as a chain: pendulum hits ball1, which hits ball2, then ball3, then ball4, which finally settles in the box. I double-check the rotation sign convention so the bob starts behind the balls rather than ahead of them, and confirm its starting x/z coordinates. With that settled, I'm ready to write out the full world definition.

