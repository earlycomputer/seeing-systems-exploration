**What happened:** Ball1 hit ball2 at 0.06 s, and the contact blew up. Both balls were thrown out at about 30 m/s, ball1 backwards and ball2 forwards, over ball3, the ramp and the cup. They landed tens of metres away and were still moving fast at 6 s. Ball3 was never touched and stayed at its start position.

**Cause:** The ball contact setting `solref="0.005 0.1"` is too stiff for the 2 ms timestep and has almost no damping. The collision therefore added energy instead of passing it on.

**Changes in the corrected file:**
- **Ball contacts:** softened to `solref="0.02 0.3"`, which is stable at this timestep and still somewhat springy.
- **Ramp and step height:** lowered from 5 cm to 4 cm, which needs only about 0.75 m/s to climb. A 4 cm step is still higher than the centre of a ball sitting in the cup, so the ball cannot roll back out.
- **Starting speed:** ball1 now starts at 4.5 m/s, rolling, to leave margin for the less elastic hits.

```json
{"what_happens": "ball1 rolls into ball2 at 0.06 s and the contact blows up: both balls are flung at ~30 m/s, ball1 backwards and ball2 forwards over ball3, the ramp and the cup, ending tens of metres away still moving fast; ball3 is never touched and stays at its start.", "works": false, "problem": "The ball contact solref (0.005, 0.1) is too stiff and undamped for the 2 ms timestep, so the first collision becomes unstable and launches the balls instead of transferring momentum along the row."}
```

```xml
<mujoco model="three_ball_chain_into_cup">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.8 -1 2" dir="0 0.4 -1" directional="true"/>
    <geom name="floor" type="plane" pos="0 0 0" size="3 1 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="ball1" pos="0 0 0.03">
      <freejoint/>
      <geom name="ball1_geom" type="sphere" size="0.03" solref="0.02 0.3" rgba="0.9 0.2 0.2 1"/>
    </body>
    <body name="ball2" pos="0.3 0 0.03">
      <freejoint/>
      <geom name="ball2_geom" type="sphere" size="0.03" solref="0.02 0.3" rgba="0.2 0.8 0.2 1"/>
    </body>
    <body name="ball3" pos="0.6 0 0.03">
      <freejoint/>
      <geom name="ball3_geom" type="sphere" size="0.03" solref="0.02 0.3" rgba="0.2 0.3 0.9 1"/>
    </body>

    <geom name="ramp" type="box" pos="1.2005 0 0.015025" euler="0 -5.711 0" size="0.201 0.1 0.005" rgba="0.6 0.4 0.2 1"/>
    <geom name="platform" type="box" pos="1.45 0 0.02" size="0.05 0.1 0.02" rgba="0.6 0.4 0.2 1"/>

    <body name="cup" pos="1.5 0 0">
      <geom name="cup_base" type="box" pos="0.175 0 0.0025" size="0.175 0.1 0.0025" condim="6" friction="1 0.01 0.01" rgba="0.9 0.7 0.1 1"/>
      <geom name="cup_near" type="box" pos="0.005 0 0.02" size="0.005 0.1 0.02" condim="6" friction="1 0.01 0.01" rgba="0.9 0.7 0.1 1"/>
      <geom name="cup_far" type="box" pos="0.345 0 0.075" size="0.005 0.1 0.075" condim="6" friction="1 0.01 0.01" rgba="0.9 0.7 0.1 1"/>
      <geom name="cup_left" type="box" pos="0.175 0.105 0.075" size="0.175 0.005 0.075" condim="6" friction="1 0.01 0.01" rgba="0.9 0.7 0.1 0.5"/>
      <geom name="cup_right" type="box" pos="0.175 -0.105 0.075" size="0.175 0.005 0.075" condim="6" friction="1 0.01 0.01" rgba="0.9 0.7 0.1 0.5"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 0 0.03 1 0 0 0 0.3 0 0.03 1 0 0 0 0.6 0 0.03 1 0 0 0" qvel="4.5 0 0 0 150 0 0 0 0 0 0 0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
ball1 touches ball2
ball2 touches ball3
ball3 touches ramp
ball3 comes to rest in cup
```

---
thinking (summarized):

The ball-ball collision is exploding into ~30 m/s velocities because the contact solref (0.005 timeconst with low damping) is too stiff relative to the 0.002s timestep, giving an unstable ratio of 2.5. At 4 m/s closing speed, penetration of 8mm per step triggers a huge spring force that injects energy rather than dissipating it.

I should switch to default solref or something softer like "0.02 0.5" and accept a less bouncy, more inelastic collision — this keeps the chain reaction working since momentum still transfers through the balls, just with lower restitution (maybe ~0.16 based on the dampratio). I'm estimating ball3 would end up around 1.3 m/s linear speed after the chain, which is marginal for clearing the 0.05m ramp requiring ~0.84 m/s — I might need to bump v0 up to 5 m/s or reconsider the ramp geometry relative to the ball radius and step height to make sure the ball actually gets trapped where intended.

I'm also checking whether a faster ball at the ramp kink could launch off the platform edge — running the projectile math, a ball leaving at 3 m/s from 0.04m height would land well within the cup's far wall, so that's fine. I'm now leaning toward picking a moderate solref like "0.02 0.3" for the ball contacts, balancing stability (timeconst equivalent to 10 timesteps) against getting enough restitution for the chain reaction to work.

I'm working through the collision chain with e≈0.37 and v0=4.5: tracking how linear and rolling velocities transfer from ball1 to ball2 to ball3 as each collision adds spin and slows the leading ball, trying to see if ball3 gets enough speed to make it over the ramp.

Checking that the cup's rolling friction and condim settings won't cause instability, confirming ball-cup solref mixing matches my earlier (0.02, 0.65) values, then recalculating the ramp geometry with rise 0.04 over run 0.4 to get the incline angle and slope components.

