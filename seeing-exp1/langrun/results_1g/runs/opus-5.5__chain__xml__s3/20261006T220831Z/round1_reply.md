In the run, ball1 struck ball2 at 0.13 s, but much of its energy was lost. Ball2 left at only 0.58 m/s, while ball1 rode up over it on its spin and flew briefly before landing. Ball2 then hit ball3 at about 0.53 m/s, and ball3 left at only 0.15 m/s. Rolling friction stopped ball3 at x ≈ 0.89 m, about 3 cm short of the cup's lip. It never reached the cup.

The cause is the ball-to-ball contacts. They are soft and damped, and their friction is high, so the spinning balls grind and climb over each other and lose most of their momentum. In the fix below:

- The default contacts between balls are excluded.
- Each ball pair gets an explicit contact that is frictionless (`condim="1"`), stiff and lightly damped, so the collisions are close to elastic. Ball2 should then roll off at about 1.3 m/s and ball3 at about 0.85 m/s.
- Rolling friction is a little higher, so the balls settle sooner.

```xml
<mujoco model="ball_chain_into_cup">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.5 0 2" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="ball1" pos="0 0 0.025">
      <freejoint/>
      <geom name="ball1_geom" type="sphere" size="0.025" condim="6" friction="0.6 0.005 0.002" rgba="0.9 0.2 0.2 1"/>
    </body>
    <body name="ball2" pos="0.3 0 0.025">
      <freejoint/>
      <geom name="ball2_geom" type="sphere" size="0.025" condim="6" friction="0.6 0.005 0.002" rgba="0.2 0.8 0.2 1"/>
    </body>
    <body name="ball3" pos="0.6 0 0.025">
      <freejoint/>
      <geom name="ball3_geom" type="sphere" size="0.025" condim="6" friction="0.6 0.005 0.002" rgba="0.2 0.3 0.9 1"/>
    </body>

    <body name="cup" pos="1 0 0">
      <geom name="cup_back" type="box" pos="0.065 0 0.03" size="0.005 0.045 0.03" rgba="0.6 0.4 0.2 1"/>
      <geom name="cup_left" type="box" pos="0 0.04 0.03" size="0.065 0.005 0.03" rgba="0.6 0.4 0.2 1"/>
      <geom name="cup_right" type="box" pos="0 -0.04 0.03" size="0.065 0.005 0.03" rgba="0.6 0.4 0.2 1"/>
      <geom name="cup_lip" type="box" pos="-0.06 0 0.0025" size="0.003 0.035 0.0025" rgba="0.6 0.4 0.2 1"/>
    </body>
  </worldbody>

  <contact>
    <exclude name="ex12" body1="ball1" body2="ball2"/>
    <exclude name="ex13" body1="ball1" body2="ball3"/>
    <exclude name="ex23" body1="ball2" body2="ball3"/>
    <pair name="pair12" geom1="ball1_geom" geom2="ball2_geom" condim="1" solref="0.01 0.1" solimp="0.99 0.99 0.001"/>
    <pair name="pair13" geom1="ball1_geom" geom2="ball3_geom" condim="1" solref="0.01 0.1" solimp="0.99 0.99 0.001"/>
    <pair name="pair23" geom1="ball2_geom" geom2="ball3_geom" condim="1" solref="0.01 0.1" solimp="0.99 0.99 0.001"/>
  </contact>

  <keyframe>
    <key name="start" qpos="0 0 0.025 1 0 0 0  0.3 0 0.025 1 0 0 0  0.6 0 0.025 1 0 0 0" qvel="2 0 0 0 80 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
ball1 touches ball2
ball2 touches ball3
ball3 touches cup
ball3 comes to rest in cup
```

```json
{"what_happens": "Ball1 hits ball2 at 0.13 s but loses most of its momentum and hops over ball2 on its spin. Ball2 crawls into ball3 at 0.58 s, and ball3 leaves at only 0.15 m/s. Rolling friction stops ball3 at x = 0.89 m, about 3 cm short of the cup's lip, and it never touches the cup.", "works": false, "problem": "The ball-to-ball contacts are damped and frictional, so the spinning balls climb and grind against each other and pass on too little momentum for ball3 to reach the cup."}
```

---
thinking (summarized):

Ball1 launches at 2 m/s with 80 rad/s spin and hops off the floor at 0.13s as its spin carries it over ball2, but ball2 only picks up 0.58 m/s from the collision. The transfer chain is quite lossy: ball2 hits ball3 at 0.53 m/s but ball3 only gets 0.15 m/s, and rolling friction then drags ball3 down from 0.15 to 0.05 m/s.

I'm realizing the real culprit is spinning surfaces at the ball-ball contact dissipating energy through torsional and rolling friction, compounded by soft/critically-damped contacts. The fix likely needs explicit contact pair overrides between balls—reducing friction to near-frictionless (condim 1) and tuning solref toward a more elastic, spring-like response for better restitution.

The observed decelerations aren't quite matching my earlier estimates, but they're small enough not to matter much. Working through the elastic frictionless collision chain, ball2 should end up rolling around 1.3 m/s and ball3 around 0.85 m/s after the cascading hits, enough to cover the 0.33m to the lip—though I need to check whether ball3 clears the lip or bounces back into the wall.

Given the cup only fits two balls in that 0.117m space, ball1 trailing behind at a slower 0.57 m/s likely gets stuck outside or collides again, so I'm now tracing whether the ball2-ball3 collision against the back wall sends ball3 bouncing back out instead of settling.

I'm considering bumping rolling friction up to around 0.002 so velocities decay properly and balls actually settle by 6 seconds rather than drifting indefinitely.

Ball3 at roughly 0.8 m/s clears the 5mm lip fine, and the back wall's soft collision gives a small rebound while spin keeps it moving forward—this all checks out. Time to write the file.

