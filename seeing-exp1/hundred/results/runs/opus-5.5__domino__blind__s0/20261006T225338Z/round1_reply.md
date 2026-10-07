When the scene runs:

- **Ramp:** ball1 rolls down the 15° ramp from 1 m along it and reaches the floor at about 1.5 m/s.
- **Domino chain:** ball1 strikes d1 at 6 cm, above d1's centre of mass, so d1 tips into d2 and d2 tips into d3. Ball1 loses most of its momentum and stalls behind the fallen dominoes.
- **Contact with ball2:** d3's face meets ball2, which sits on the step, at about 26° of fall.

That contact is where the scene fails. Every pair involved has friction 1, because MuJoCo uses the larger value of the two geoms. Ball2 is pinched between d3's face, which pushes it forward and down, and the step top. The line between the two contact points lies about 32° off each contact normal. That is inside both 45° friction cones, so the ball can wedge. d3 would then stall, still holding ball2 on the step, and ball2 never reaches the cup.

Fix: lower the friction on d3, the step and ball2 to 0.3, which gives a 16.7° cone, so no wedge is possible. Rolling and tipping still work because the floor contacts keep μ = 1. With that change, ball2 is shoved off the step, drops over the low near wall into the cup, and rolling friction brings it to rest against the walls well before 6 s.

```xml
<mujoco model="ramp_domino_cup">
  <option timestep="0.002"/>
  <worldbody>
    <light name="main_light" pos="0 0 2" dir="0 0 -1"/>
    <geom name="floor" type="plane" pos="0 0 0" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="ramp" pos="-0.6813 0 0.1619" euler="0 15 0">
      <geom name="ramp_plank" type="box" size="0.7 0.15 0.02" rgba="0.6 0.4 0.2 1"/>
    </body>

    <body name="ball1" pos="-0.9504 0 0.3170">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.06" density="150" condim="6" friction="0.8 0.005 0.005" rgba="0.9 0.1 0.1 1"/>
    </body>

    <body name="d1" pos="0.25 0 0.05">
      <freejoint name="d1_free"/>
      <geom name="d1_geom" type="box" size="0.01 0.04 0.05" density="600" rgba="0.1 0.3 0.9 1"/>
    </body>

    <body name="d2" pos="0.32 0 0.05">
      <freejoint name="d2_free"/>
      <geom name="d2_geom" type="box" size="0.01 0.04 0.05" density="600" rgba="0.1 0.5 0.9 1"/>
    </body>

    <body name="d3" pos="0.39 0 0.05">
      <freejoint name="d3_free"/>
      <geom name="d3_geom" type="box" size="0.01 0.04 0.05" density="600" friction="0.3 0.005 0.0001" rgba="0.1 0.7 0.9 1"/>
    </body>

    <body name="step" pos="0.46 0 0.02">
      <geom name="step_block" type="box" size="0.015 0.07 0.02" friction="0.3 0.005 0.0001" rgba="0.5 0.5 0.5 1"/>
    </body>

    <body name="ball2" pos="0.46 0 0.0651">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.025" density="300" condim="6" friction="0.3 0.005 0.002" rgba="0.1 0.8 0.1 1"/>
    </body>

    <body name="cup" pos="0 0 0">
      <geom name="cup_base" type="box" pos="0.605 0 0.002" size="0.12 0.07 0.002" rgba="0.9 0.8 0.2 1"/>
      <geom name="cup_near_wall" type="box" pos="0.48 0 0.01" size="0.005 0.08 0.01" rgba="0.9 0.8 0.2 1"/>
      <geom name="cup_far_wall" type="box" pos="0.73 0 0.035" size="0.005 0.08 0.035" rgba="0.9 0.8 0.2 1"/>
      <geom name="cup_left_wall" type="box" pos="0.605 0.075 0.035" size="0.12 0.005 0.035" rgba="0.9 0.8 0.2 1"/>
      <geom name="cup_right_wall" type="box" pos="0.605 -0.075 0.035" size="0.12 0.005 0.035" rgba="0.9 0.8 0.2 1"/>
    </body>
  </worldbody>
</mujoco>
```

```json
{"what_happens": "ball1 rolls down the ramp, hits d1 above its centre of mass, and d1 topples d2, which topples d3. d3's face then presses ball2 forward and down against the step top. With friction 1 at both contacts, the ball can wedge there, so d3 stalls and ball2 may never leave the step for the cup.", "works": false, "problem": "With friction 1 everywhere, ball2 can jam between d3's falling face and the step top (the contact line is about 32° off each normal, inside the 45° friction cones), so d3 may stall without knocking ball2 into the cup."}
```

---
thinking (summarized):

Double-checking the setup: ball1's starting position is close enough to the expected value, and it should roll down and hit domino d1 with sufficient speed to tip it. I'm now verifying ball2's position relative to the step it's resting on.

Working through the geometry of d3, the cup, and the walls, I confirm the gaps are all consistent and clearances check out. I'm then tracing whether ball1, after bouncing off d1, could have enough momentum to reach and strike ball2 directly—working through the x-coordinates, it looks like the step face blocks ball1 before it can reach ball2's position, so that contact shouldn't happen.

The domino chain propagation speed is roughly 1 m/s, taking about 0.15–0.3 s to cover the gap, while ball1 moves slower and likely stays blocked by d1. I'm now considering whether ball2's situation creates a bigger concern than this timing issue.

If ball2 bounces back toward the near wall, it's too low to clear it and would just roll back into the cup, so that seems safe. I should also check whether d3 leaning against the step corner stays stable there.

Reconsidering, the face actually hits the near corner first at 48°, giving the top of d3 a position that doesn't intrude into the cup — that's consistent with the earlier ball-contact angle of 26°. But I need to double check whether ball2 could get pinned between d3 and the step before escaping, since it still needs to shift its center past 0.475 to actually fall.

I'm checking whether the ball could jam between the two contact points — domino face above and step surface below both having high friction could create conflicting rolling constraints. I'm working through the rolling-without-slip condition, figuring out the angular velocity direction needed for forward motion and whether that's consistent with both contact points simultaneously.

So the domino's friction on the ball creates a torque opposing its spin and pulls it down, while the normal force still pushes it forward-down. Working through the force balance with μ=1 friction, the horizontal components still net forward, so the ball doesn't jam there—it seems like it could instead slide forward against the step without fully rolling, depending on the friction available at that contact.

Computing the torque from the domino friction at the contact point, it comes out negative, opposing forward rolling. I'm now setting up the equations of motion combining the step friction force and torque to check whether the ball can actually roll forward without slipping at both contacts simultaneously.

With the domino force treated as dominant, I find the required step friction and resulting torque are inconsistent with pure rolling, so the ball would tend to spin backward rather than roll cleanly. This points to a different scenario: the ball sticks (no slip) at the domino face but slips against the step instead, which could cause it to get dragged downward and jam.

I'm checking whether the ball could get wedged in static equilibrium between the domino and step by analyzing the friction cone geometry at both contact points. I'm testing the classic wedging condition: whether the line connecting the two contact points falls within both friction cones, which would mean the ball jams rather than slips free.

The calculation shows both angles (around 32°) fall within the 45° friction cone limit, confirming jamming is a real risk with the current friction settings. To fix this, I'm considering lowering the friction coefficient on the step geometry and ball surfaces so the contact can't sustain the wedge force.

Rethinking the friction values: better to set d3 at 0.3, step at 0.2, and ball2 at 0.3 so the ball2-d3 and ball2-step contacts both land at μ=0.3, keeping the jam angle well below the 32° domino angle. I also check ball1-d1 contact (friction resolves to 1, fine for near-normal impact) and confirm ball2 sits stable on the flat step at μ=0.3.

Checking d2-d3 contact friction, it resolves to 1 since only d3's value changes and d2 stays default — no issue there. So the original file has a jam risk and needs correcting with these friction tweaks.

