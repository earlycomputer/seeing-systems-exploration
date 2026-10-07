## What happened in the run

The release and the impact chain both work:

- **Release:** the pendulum fell from 60° and was swinging at about 3.1 m/s when it struck ball1 at 0.54 s.
- **Chain:** ball1 hit ball2 at 0.59 s, ball2 hit ball3 at 0.69 s, and ball3 hit ball4 at 0.96 s.

Each impact lost a lot of energy, so the motion faded down the row:

- ball1 left at about 3 m/s.
- ball2 left at about 1 m/s.
- ball3 left at about 0.4 m/s.
- ball4 left at only about 0.16 m/s.

ball4 rolled 5 cm and stopped on the rail at x = 0.56 m at 1.38 s. That was still about 8 cm short of the rail end and the box, and it stayed there to the end. The pendulum kept swinging gently, about ±11.5°.

## What I changed

**Less loss between impacts.** I lowered friction on the balls and rail, so the balls slide across the 10 cm gaps. Before, they converted to rolling, which wastes energy, and high rolling resistance slowed them further.

**More starting energy.** The bob is now 300 g, so ball1 leaves at roughly 1.5 times the bob's speed. The balls stay equal at 100 g each.

**Shorter run to the box.** The rail now ends 5 cm past ball4, with the box's low near wall right there. A slow ball4 still tips off the edge and falls into the box.

**Clearance at the rail start.** The rail now starts 1 cm later, because the bob grazed its near end. The box keeps its high friction and dead bounce, so ball4 settles inside it.

```json
{"what_happens": "The pendulum swings down and strikes ball1, and the impacts pass along ball1→ball2→ball3→ball4, but each impact and roll loses most of the energy: ball4 leaves at only ~0.16 m/s, rolls 5 cm and stops on the rail at x=0.56 m, about 8 cm short of the rail end and the box, staying there until 6 s.", "works": false, "problem": "Energy losses along the chain leave ball4 too slow to reach the box, so it rests on the rail instead of in the box."}
```

```world
world  pendulum chain into box

floor
  friction  0.8, spinning 0.005, rolling 0.002

pivot
  is a  point
  at    0 m along, 122.5 cm up

pendulum
  is a           sphere 2.5 cm radius, 300 g
  bounce         lively
  friction       0.1, spinning 0.001, rolling 0.0005
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
  is a      box 51 by 10 by 20 cm
  friction  0.05, spinning 0.001, rolling 0.0005
  colour    wood
  stands    on floor, 30.5 cm along

ball
  is a      sphere 2.5 cm radius, 100 g
  rolls
  bounce    lively
  friction  0.1, spinning 0.001, rolling 0.0005
  colour    white
  moves     freely
  repeated  4 times, 15 cm apart along
  rests     on rail, 6 cm along

box
  is an             open box
  length            70 cm
  width             30 cm
  walls             25 cm
  near wall height  10 cm
  bounce            dead
  friction          0.9, spinning 0.05, rolling 0.03
  colour            grey
  rests             on floor, 92 cm along

expect
  pendulum touches ball1
  ball1 touches ball2
  ball2 touches ball3
  ball3 touches ball4
  ball4 comes to rest in box
```

---
thinking (summarized):

The energy losses in the chain seem huge - ball4 only reached 0.16 m/s before stopping at 0.56, while the pendulum hit at roughly 3.14 m/s. The numbers aren't adding up cleanly across the collision sequence, with ball3 at 0.41 m/s and ball1's velocity after impact still unclear, plus the pendulum continuing to swing afterward.

Looking at the pendulum's post-collision amplitude of ~11.5°, it seems to have retained much of its energy - calculating the fraction gives about 4%, meaning the pendulum itself lost most of its energy while ball1 got launched and apparently left the rail around 0.54 s. Tracking ball1's velocity jump (~3 m/s), then ball2 (~1 m/s), ball3 (~0.4 m/s), and ball4 (0.16 m/s), each collision seems to lose roughly 60% of energy, which is more than expected from sliding-to-rolling friction conversion (5/7 factor) alone, so something else - maybe soft contact properties in MuJoCo or spin effects - must be contributing to this unusually low restitution.

Since I can't easily tune the contact solver beyond basic parameters, I'm thinking about compensating by shortening the required travel distance for ball4 - if I position the rail's end closer to ball4's starting point, it won't need much velocity to roll off the edge and still trigger the final fall into the box.

I'm also considering lowering friction coefficients on the rail and balls so they slide rather than roll, since MuJoCo takes the max of contact friction values -- keeping both the rail and ball friction low would reduce energy losses from spin, while the box surface friction stays high to catch the ball once it lands.

I'm unsure about the restitution coefficient for ball-ball collisions, so I'm considering making the pendulum bob heavier—say 300 g—so it transfers more speed to ball1, roughly 1.5× its own velocity. I'm also checking whether the bob swings clear of the rail afterward, since at the bottom its center aligns with the rail top but as it swings forward it rises above that level, avoiding contact.

I'm nudging the rail's starting position to 5 cm and keeping ball1's contact point at 6 cm to make sure the geometry stays clean near the rail edge, since ball4's speed just needs to be enough to clear the area near the wall regardless of exact value. Now I'm thinking through whether ball4, moving fast into a 70 cm box with friction 0.9 and rolling resistance 0.02, will still have enough speed left when it arrives.

I'm placing the box so its near wall sits right after the rail ends, spanning roughly 57 to 127 cm with its centre around 92 cm, while the rail itself runs about 51 cm long centred near 30.5 cm. Since friction is low, balls 1-3 will likely slide along and follow ball4 into the box too, which should be fine. For the pendulum, I'm keeping it at 300 g with a 2.5 cm radius sphere, dense enough that the rod clears everything, starting at a 60° angle, and I'm setting the ball friction to 0.1.

Now I'm tuning friction values across surfaces: spinning at 0.001, rolling at 0.0005 for the rail, higher friction of 0.1 for the pendulum, and much higher values (0.9 sliding, 0.05 spinning, 0.03 rolling) for the box so objects actually catch there. The floor's friction barely matters since balls shouldn't touch it. I'll keep the rolling flag active so rolling contact uses condim 6.

