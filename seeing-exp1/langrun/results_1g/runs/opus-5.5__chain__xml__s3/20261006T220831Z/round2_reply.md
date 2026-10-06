All four expectations hold, but the run does not match the brief.

**What happens in the run**
- **The first collision adds energy.** Ball1 hits ball2 at 2.0 m/s. Ball1 bounces back at 1.66 m/s and rolls away to x = −2.1 m. Ball2 is launched at 3.5 m/s, mostly upward, and flies about 0.6 m high.
- **Ball2 never rolls into ball3.** It clips ball3 while airborne at 0.20 s, sails over the cup, and comes to rest at x = 5.5 m.
- **Ball3 does do its part.** It hops the lip, hits the back wall and settles in the cup at x = 0.96 m.

**Cause and fix**

The near-elastic ball-pair contacts are too stiff and too lightly damped for the 2 ms timestep, so they overshoot and inject energy. I've made them softer and better damped, which gives a moderate bounce instead. To make up for the lower restitution, ball1 starts faster and the balls are spaced so ball3 has less distance to cover. The lip is also slightly lower and rolling friction a bit weaker, so ball3 still has the speed to get over the lip.

```xml
<mujoco model="ball_chain_into_cup">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.5 0 2" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="ball1" pos="0 0 0.025">
      <freejoint/>
      <geom name="ball1_geom" type="sphere" size="0.025" condim="6" friction="0.6 0.005 0.001" rgba="0.9 0.2 0.2 1"/>
    </body>
    <body name="ball2" pos="0.35 0 0.025">
      <freejoint/>
      <geom name="ball2_geom" type="sphere" size="0.025" condim="6" friction="0.6 0.005 0.001" rgba="0.2 0.8 0.2 1"/>
    </body>
    <body name="ball3" pos="0.75 0 0.025">
      <freejoint/>
      <geom name="ball3_geom" type="sphere" size="0.025" condim="6" friction="0.6 0.005 0.001" rgba="0.2 0.3 0.9 1"/>
    </body>

    <body name="cup" pos="1 0 0">
      <geom name="cup_back" type="box" pos="0.065 0 0.03" size="0.005 0.045 0.03" rgba="0.6 0.4 0.2 1"/>
      <geom name="cup_left" type="box" pos="0 0.04 0.03" size="0.065 0.005 0.03" rgba="0.6 0.4 0.2 1"/>
      <geom name="cup_right" type="box" pos="0 -0.04 0.03" size="0.065 0.005 0.03" rgba="0.6 0.4 0.2 1"/>
      <geom name="cup_lip" type="box" pos="-0.06 0 0.0015" size="0.003 0.035 0.0015" rgba="0.6 0.4 0.2 1"/>
    </body>
  </worldbody>

  <contact>
    <exclude name="ex12" body1="ball1" body2="ball2"/>
    <exclude name="ex13" body1="ball1" body2="ball3"/>
    <exclude name="ex23" body1="ball2" body2="ball3"/>
    <pair name="pair12" geom1="ball1_geom" geom2="ball2_geom" condim="1" solref="0.02 0.3" solimp="0.95 0.99 0.001"/>
    <pair name="pair13" geom1="ball1_geom" geom2="ball3_geom" condim="1" solref="0.02 0.3" solimp="0.95 0.99 0.001"/>
    <pair name="pair23" geom1="ball2_geom" geom2="ball3_geom" condim="1" solref="0.02 0.3" solimp="0.95 0.99 0.001"/>
  </contact>

  <keyframe>
    <key name="start" qpos="0 0 0.025 1 0 0 0  0.35 0 0.025 1 0 0 0  0.75 0 0.025 1 0 0 0" qvel="2.5 0 0 0 100 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
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
{"what_happens": "Ball1 hits ball2 at 0.13 s and the collision adds energy: ball1 bounces back at 1.66 m/s and rolls to x=-2.1 m, while ball2 is launched about 0.6 m into the air. Ball2 clips ball3 in flight at 0.20 s, flies over the cup and lands near x=5.5 m. Ball3 hops the lip, hits the back wall and comes to rest inside the cup at x=0.96 m.", "works": false, "problem": "The ball-ball contacts are too stiff and underdamped for the timestep, so the first collision injects energy and launches ball2 through the air instead of letting it roll into ball3."}
```

---
thinking (summarized):

Something's off here physically — ball1 rebounds backward at 1.66 m/s while ball2 launches at 3.49 m/s up to 0.64 m height, which means energy isn't being conserved. This looks like the contact is overshooting due to timestep or solimp stiffness issues, causing ball2 to jump over ball3 and the cup instead of rolling.

The narrow timeconst combined with low damping ratio is likely causing numerical energy gain under semi-implicit Euler integration. I should try dampratio closer to 0.5 with a larger timeconst like 0.02, and reconsider using a more moderate restitution so the collision chain stays physically plausible rather than relying on fragile elastic parameters.

Actually the z=0.025 start seems fine, so the vz spike probably comes from the floor contact itself—ball2 getting shoved hard horizontally with condim 6 friction could trigger a known MuJoCo pyramidal-cone artifact where strong tangential impulses couple into spurious normal forces, making the ball pop upward.

I think the real culprit is the pair solref being too stiff relative to timestep, causing ball1's rebound to overshoot. I'll keep the option block limited to just the timestep attribute to avoid risk, and adjust the pair's solref/solimp values to soften the contact and tune the effective restitution down.

With v0=2.5 m/s and e≈0.4, I'm tracing through the chain: ball2 gets 1.75 sliding→1.25 rolling, ball3 gets 0.875 sliding→0.63 rolling. Working through the rolling friction decel over the 0.33m gap, the remaining energy at the lip looks marginal — I should lower rolling friction to 0.001 and reduce the lip height to around 0.003 to make sure it still clears.

I'm placing ball1 at 0, ball2 at 0.35, ball3 at 0.75, with the cup lip at 0.937, checking that ball2's slide-to-roll transition (~0.13m) still leaves it with enough speed (~0.6 m/s) to follow into the cup and tap ball3, while ball1 keeps trailing behind too.

Watching for a weird vertical pop at floor contact — earlier runs showed a ball briefly leaving the floor during friction climb or pair-contact impacts, likely from an overshooting horizontal impulse creating spurious vertical force through the floor's pyramidal friction model. Spreading that impulse over more timesteps with a softer contact constant should flatten the peak force and fix it — I'll go with that. I also need to check how ball3 rebounds off the back wall after entering around 0.9m.

