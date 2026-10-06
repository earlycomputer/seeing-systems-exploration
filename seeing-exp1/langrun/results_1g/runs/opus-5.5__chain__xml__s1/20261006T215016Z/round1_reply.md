**What happened:** The run did not do what the brief says. At 0.11 s `ball1` reached `ball2`, and the ball-to-ball contact blew up. The two balls shot apart at about 30 m/s, `ball1` backwards and `ball2` forwards. `ball2` flew over `ball3` and over the cup. `ball3` was never touched and stayed where it started.

**Why:** My "bouncy" contact setting (`solref="0.005 0.05"`) made the contact spring far too stiff for the 2 ms timestep, and it was very lightly damped. The simulation became unstable and added energy instead of passing momentum along.

**The fix:** Ball-to-ball contacts are now stiff but fully damped (`solref="0.005 1"`), so the collisions are stable and nearly inelastic.
- `ball1` starts at 2.5 m/s, rolling with matching spin.
- When it hits `ball2`, they share momentum. `ball1`'s leftover spin keeps pushing `ball2` forward until `ball2` hits `ball3`.
- From then on the three roll together as a train at roughly 0.8 m/s. That is well above the roughly 0.5 m/s needed to clear the cup's lip.
- The cup is now longer, so `ball3` and a following ball both fit inside.

The 0.8 m/s and 0.5 m/s figures are hand estimates. This corrected file has not been run.

```xml
<mujoco model="three_ball_chain">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.4 0 2" dir="0 0 -1"/>
    <geom name="floor" type="plane" size="3 3 0.1" friction="0.5 0.005 0.0001" rgba="0.8 0.8 0.8 1"/>

    <body name="ball1" pos="0 0 0.02">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.02" friction="0.5 0.005 0.0001" rgba="0.9 0.2 0.2 1"/>
    </body>
    <body name="ball2" pos="0.25 0 0.02">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.02" friction="0.5 0.005 0.0001" rgba="0.2 0.8 0.2 1"/>
    </body>
    <body name="ball3" pos="0.5 0 0.02">
      <freejoint name="ball3_free"/>
      <geom name="ball3_geom" type="sphere" size="0.02" friction="0.5 0.005 0.0001" rgba="0.2 0.3 0.9 1"/>
    </body>

    <body name="cup" pos="0.85 0 0">
      <geom name="cup_ramp" type="box" size="0.03 0.07 0.005" pos="-0.0742 0 -0.0009" euler="0 -9.09 0" friction="0.5 0.005 0.0001" rgba="0.7 0.5 0.3 1"/>
      <geom name="cup_floor" type="box" size="0.082 0.07 0.001" pos="0.038 0 0.001" friction="0.5 0.005 0.0001" rgba="0.6 0.4 0.2 1"/>
      <geom name="cup_back" type="box" size="0.005 0.08 0.03" pos="0.125 0 0.03" friction="0.5 0.005 0.0001" rgba="0.6 0.4 0.2 1"/>
      <geom name="cup_side_left" type="box" size="0.1175 0.005 0.03" pos="0.0125 0.075 0.03" friction="0.5 0.005 0.0001" rgba="0.6 0.4 0.2 1"/>
      <geom name="cup_side_right" type="box" size="0.1175 0.005 0.03" pos="0.0125 -0.075 0.03" friction="0.5 0.005 0.0001" rgba="0.6 0.4 0.2 1"/>
    </body>
  </worldbody>

  <contact>
    <pair name="pair_b1_b2" geom1="ball1_geom" geom2="ball2_geom" condim="3" friction="0.2 0.2 0.005 0.0001 0.0001" solref="0.005 1"/>
    <pair name="pair_b2_b3" geom1="ball2_geom" geom2="ball3_geom" condim="3" friction="0.2 0.2 0.005 0.0001 0.0001" solref="0.005 1"/>
    <pair name="pair_b1_b3" geom1="ball1_geom" geom2="ball3_geom" condim="3" friction="0.2 0.2 0.005 0.0001 0.0001" solref="0.005 1"/>
  </contact>

  <keyframe>
    <key name="start" qpos="0 0 0.02 1 0 0 0  0.25 0 0.02 1 0 0 0  0.5 0 0.02 1 0 0 0" qvel="2.5 0 0 0 125 0  0 0 0 0 0 0  0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

```expect
ball1 touches ball2
ball2 touches ball3
ball3 touches cup_ramp
ball3 touches cup_back
ball3 comes to rest in cup
```

```json
{"what_happens": "ball1 rolls into ball2 at 0.11 s, but the ball-ball contact goes numerically unstable and launches ball1 backwards and ball2 forwards at about 30 m/s; ball2 flies over ball3 and the cup, and ball3 is never touched, staying at rest at its start position.", "works": false, "problem": "The ball-ball contact solref (0.005 s, damping ratio 0.05) was far too stiff and too lightly damped for the 2 ms timestep, so the first collision went unstable and added energy."}
```

---
thinking (summarized):

The ball-ball collision exploded apart at high speed, likely due to the solref values being too stiff relative to the timestep, causing numerical instability. I need to adjust the contact parameters to be less bouncy and more stable.

I'm reconsidering the solref values—trying timeconst 0.02 with damping 0.15 for a more physically reasonable restitution around 0.6, then working through how momentum transfers from ball1 to ball2 to ball3 in the collision chain, accounting for rolling versus sliding velocities.

Checking the margins: with v1 raised to 2.5 m/s, ball3 ends up with enough speed to clear the lip with some buffer, and I'm tracing how the trailing balls (ball1 and ball2) settle into slower rolling speeds afterward so they don't catch up and cause unwanted secondary collisions.

I'm also second-guessing whether the contact timeconst of 0.02 makes the fast ball-ball collisions too soft — estimating penetration depth versus ball radius to see if it's physically reasonable, and considering whether MuJoCo's impedance settings adequately limit that overlap.

Doing the math on the solref stiffness and damping parameters, I find the effective natural frequency comes out close to the integration timestep's stability limit, which explains why the 0.005/0.05 combination blew up — the resulting frequency was way too high for that timestep to handle.

Maybe the solver's semi-implicit nature keeps things stable even at higher ω, though it's risky territory. I'm considering avoiding bounce entirely by using inelastic default contacts instead, letting spin do the work: ball1 hits ball2, momentum splits evenly, then friction from the floor acts on each ball's spin to gradually bring them toward a common rolling speed, since the ball-ball collision force passes through centers and shouldn't impart torque about the contact point.

Tracking total angular momentum about the floor line (conserved since internal and floor friction forces produce no net torque there), I find the two balls settle to a common rolling speed of 1.25, then when that pair hits the third ball, the system redistributes again to a final common speed of about 0.83 — meaning all three balls end up rolling together into the cup.

Checking the geometry: ball3 clears the lip (needs only 0.49) and fits with ball2 inside the cup's interior length behind it, with ball1 possibly trailing on the ramp. The chain contact isn't perfectly clean — balls stay touching as a train rather than separating cleanly — but it's roughly consistent with the "first hits second, second hits third" picture. I'm now considering whether after inelastic contact the balls actually separate again, since ball2 without spin would decelerate from friction while ball1 behind it keeps accelerating.

I'm tuning contact stiffness parameters to avoid excessive penetration — testing solref/timeconst/dampratio combos (various natural frequencies and damping ratios giving restitution values around 0.37–0.44), but even the "stable" settings produce unrealistic penetration depths (over a centimeter) relative to the 2cm ball radius, which looks physically wrong and could cause the spheres to interact strangely rather than bounce cleanly.

That matches the critically damped max displacement formula. I'm thinking about lowering the approach speed to reduce penetration—with v1=1.5 m/s the inelastic collision gives a final train speed around 0.5 m/s, right near the lip threshold of 0.49, so I'm considering reducing the lip height instead, maybe to 4mm, which drops the escape threshold to about 0.33 m/s while trailing balls still push the lead ball against the wall.

Now I'm reconsidering the solver parameters for ball-pair contacts—testing solref "0.005 1" instead of the unstable low-damping setting, checking that critical damping with ω=200 keeps penetration around 4.6mm which seems acceptable, and recalling that the earlier explosion came from an extremely stiff spring constant at low damping ratio.

But I realize there's a subtler problem: with ball1 spinning forward and pressed against ball2, friction at the contact point acts upward on ball1 and downward on ball2, which could cause ball1 to climb up and over ball2 instead of staying in line.

Since normal force from pushing is bounded by floor friction, the upward lift stays small enough that climbing shouldn't happen, so I'll set a low ball-to-ball friction coefficient as a safety margin. Now I'm working through the three-ball train hitting the cup: ball3 leads, enters first and hits the back wall, with ball2 following close behind, and I'm checking the geometry of where each ball's center lands relative to the cup's lip and back wall.

The positions are tight — ball1 trailing the train might partially overlap the lip edge rather than clearing it fully, so I think extending the cup's length is a cleaner fix. I'm recalculating the cup dimensions with a longer floor and back wall position, adjusting the side wall span and half-widths to match, then re-verifying that ball3 actually comes to rest inside the cup and checking the spacing between balls in the train after their collisions.

I'm also checking the keyframe velocities — ball1's first collision happens at mid-height with no vertical component, which is fine, and the rotational velocity for the spin keyframe looks right. The "ball1 leaves the floor" moment around 0.11s is expected from the impact dynamics, so that's acceptable. Time to write the file.

