The ramp's low end sits above the cup's low near wall. The ball rolls off the end, drops into the cup and runs into the tall far wall. Dead bounces and high rolling friction on the cup then settle it well inside 6 s.

```world
world  ball down a ramp into a cup

floor
  friction  0.8, spinning 0.005, rolling 0.002

ramp
  is a       ramp
  high end   20 cm along, 24 cm up
  low end    80 cm along, 12 cm up
  width      20 cm
  thickness  4 cm
  friction   0.8, spinning 0.005, rolling 0.002
  colour     wood

cup
  is an             open box
  length            40 cm
  width             30 cm
  walls             15 cm
  near wall height  6 cm
  friction          0.9, spinning 0.02, rolling 0.01
  bounce            dead
  colour            grey
  its base 1.02 m along

ball
  is a      sphere 3 cm radius, 100 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  on ramp, 8 cm from the top

expect
  ball touches ramp
  ball comes to rest in cup
```

---
thinking (summarized):

I need to design a ramp with a high end and low end, a ball rolling down into a cup at the base, making sure the ball settles in the cup within 6 seconds. I'm working through the geometry—placing the high and low ends of the plank, accounting for thickness, so the ball's path and timing work out correctly.

I'm weighing cup placement: the near wall needs to be low enough to let the ball in, but the far wall needs to be tall enough to catch it and dissipate speed rather than bounce out. Having the ramp's foot hang just above the cup so the ball drops directly in seems most reliable, so I'm calculating the rolling sphere's velocity at the bottom using energy conservation, factoring in rotational inertia, to check the drop height and resulting speed are reasonable for the cup to catch it.

I'm uncertain whether the plank's measurements refer to its centerline or top surface, which makes the handoff point ambiguous. Trying a hybrid setup instead: a short near wall (4 cm) and tall far wall (15 cm) on a long cup, so the ball drops in, bounces dead off the far wall, and rolls back — checking if the 4 cm near wall is low enough to let the 3 cm-radius ball clear it without getting trapped.

Since the wall's top is just below the ball's center height, I bump the near wall to 6 cm so a slow-rolling ball can't easily climb back out, then raise the ramp foot to 10 cm with the deck around 12 cm to stay clear of it. I'm also considering rolling friction in MuJoCo (around 0.004) and whether that's low enough that the ball keeps bouncing between walls for a while before settling.

I'm now sketching concrete coordinates for the ramp, placing the high end around 20cm along and 40cm up, sloping down to about 12cm height near 1m along, giving roughly a 19° incline so I can estimate the ball's exit speed from the drop height.

I keep adjusting the numbers since the speed feels too high—trying a shallower slope (24cm high end, 12cm foot, 60cm length, ~11° angle) with the ball placed 8cm from the top, yielding about 1.2 m/s accounting for rolling friction. Now I'm moving on to analyzing the flight path from the deck top down to the resting position at the base.

Ball lands around x≈0.97, well within the cup's 0.81–1.21 span, then rolls toward the far wall at about 1.2 m/s, hitting it at 1.21 with a 15 cm wall — that should stop it fine. Now I'm figuring out the syntax for positioning the cup itself, trying phrasing like "its base 1.02 m along" to place it by absolute offset rather than relative to another part.

Near walls 15 cm tall, 6 cm near-side height noted. For the ball, I'll place it using `on ramp, 8 cm from the top`, matching the documented syntax, assuming it centers on the deck by default. Since it starts at rest on an 11° slope, gravity alone should set it rolling, and placing it 8 cm from the top keeps it clear of the leg post below.

Checking clearances: the post runs from floor to the deck centerline, so its top sits under the deck surface and shouldn't interfere with the ball's path near x≈0.28, well clear of the post at x=0.2 given the ball's 3 cm radius. With deck width 20 cm, ramp friction 0.8, and rolling resistance 0.002, the ball should maintain speed down the slope — I'll set its mass to 100 g for a reasonable weight.

I'm estimating the ball's landing velocity into the cup base at around 1.55 m/s vertically, which should produce a clean, dead bounce. Now I'm checking whether the ball retains enough speed to cross to the far wall and bounce back toward the near wall given the cup's 0.01 rolling friction.

Working through the deceleration (~2.3 m/s²), the ball should land near x=0.97, travel toward the far wall inner face at 1.21, hit it around 1.1 m/s, bounce back weakly (~0.3 m/s), and settle within the 6-second window — the geometry with the near wall spanning 0.81–0.83 and the deck ending at 0.8 all checks out.

Even checking the plank interpretation (top surface at the 12 cm end), it still clears the 6 cm wall fine, so I'm confident in this setup and ready to write it up.

