**What happened.** The chain lost almost all its speed at the two impacts. Ball1 was launched at 2.5 m/s and spinning. When it hit ball2, the high grip between the balls let its spin climb it up and over: ball1 flew into the air, and ball2 got only 0.74 m/s. Ball2 then did the same against ball3, which got just 0.19 m/s. Ball3 crept to x = 1.28 m and stopped about 0.6 m short of the cup. It never touched the cup.

**The fix.**
- **Slippery balls.** MuJoCo uses the larger friction of two touching things, so ball-on-floor contact keeps the floor's 0.8. Ball-on-ball contact gets the balls' own 0.05, so they no longer climb each other.
- **Elastic collisions.** The balls bounce lively so each impact passes on more speed.
- **Faster launch.** Ball1 starts at 4 m/s.
- **A cup that holds the ball.** The cup is longer and has higher rolling resistance, so ball3 can't bounce back out over the sill.

```world
world  three balls in a row into a cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ball1
  is a      sphere 4 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.05, spinning 0.005, rolling 0.002
  colour    orange
  moves     freely
  sits      on floor, 50 cm along
  launched  4 m/s along
  spins     100 rad/s about y

ball2
  is a      sphere 4 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.05, spinning 0.005, rolling 0.002
  colour    white
  moves     freely
  sits      on floor, 30 cm beyond ball1

ball3
  is a      sphere 4 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.05, spinning 0.005, rolling 0.002
  colour    grey
  moves     freely
  sits      on floor, 30 cm beyond ball2

cup
  is an             open box
  length            60 cm
  width             30 cm
  walls             12 cm
  near wall height  1.5 cm
  base thickness    5 mm
  friction          0.8, spinning 0.02, rolling 0.01
  bounce            dead
  colour            wood
  on                floor, 2.2 m along

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

```json
{"what_happens": "Ball1 is launched at 2.5 m/s and hits ball2, but its spin and the high friction between the balls make it climb over ball2 and fly up. Ball2 gets only 0.74 m/s, and the same happens again when it hits ball3, which gets 0.19 m/s. Ball3 creeps to x = 1.28 m and stops about 0.6 m short of the cup without touching it; ball1 and ball2 stop behind it.", "works": false, "problem": "Too much energy is lost at the ball-to-ball impacts (high friction lets the spinning balls climb each other), so ball3 stops far short of the cup and never reaches it."}
```

---
thinking (summarized):

This attempt failed badly — too much energy got lost. Ball1 actually bounced upward off the collision instead of transferring momentum cleanly, so ball2 only picked up 0.74 m/s and ball3 just 0.19 m/s, and both decelerated way too fast from friction, suggesting the rolling friction coefficient is way too strong in this setup.

Since contact friction in MuJoCo takes the max of the two geoms' friction values, and I've set the floor to 0.8, any ball-to-ball contact also inherits that high friction, causing the spinning balls to "climb" each other instead of sliding smoothly. The fix is to lower the ball friction value (maybe down to 0.05) so ball-ball collisions behave more elastically, even though ball-floor contact will still use the floor's higher friction.

Alternatively, rather than relying on tuning chain efficiency, I could just launch harder — say 4 m/s initial speed — so even after losses through the chain (slide-to-roll transition cuts speed to 5/7, friction decel along the way), ball3 still arrives with enough speed (~1.7 m/s) to travel the 0.7 m to the cup. I also want to lower the floor's rolling friction coefficient to something like 0.001 to keep the balls lively, though I need to watch that ball3 doesn't bounce too hard off the cup's far wall and climb back out over the near wall's 1 cm lip — so I may need to raise the near wall step-out height to keep fast-rolling balls contained.

Thinking through it more, I could lengthen the cup to 60 cm and give it a higher rolling friction coefficient (0.01) so that after a ball bounces off the far wall and heads back toward the near wall, it decelerates fast enough to stop before climbing out — rough calculations suggest a return speed around 0.8 m/s would decay to zero well within the cup's length. I also want to keep spin on ball1 so it transitions from sliding to rolling within about 0.1 m, using a ball friction coefficient around 0.05.

Residual spin after ball-ball collisions could drag the colliding balls forward at a fraction of their original speed, causing them to chase each other into the cup, which might cause some clutter but seems acceptable. I'm settling on friction values: sliding friction 0.05, spinning friction 0.005, and rolling friction 0.002 for the balls, relying on MuJoCo's max-based friction combination with the floor.

For the launch setup, I'll use an initial speed of 4 m/s with 100 rad/s of spin, a cup roughly 60 cm away, and rolling friction around 0.01.

