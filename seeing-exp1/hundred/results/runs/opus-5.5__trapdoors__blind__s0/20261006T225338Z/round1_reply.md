**What should happen when it runs**

1. ball1 falls about 0.97 m through hoop1 and strikes flap1's pocket at roughly 4.3 m/s.
2. The impact spins flap1 at about 7 rad/s toward its 35° lower stop.
3. The tip drops faster than gravity, so block separates and falls almost straight down into flap2's pocket at about 2.6 m/s.
4. That impact swings flap2 to its lower stop.
5. ball2 is left behind at flap2's tip and falls vertically through hoop2 into cup, where it settles.

**The weak point is the contact softness at these impact speeds.** The default contact solref is 0.02 s. At these speeds that allows roughly 2–3 cm of penetration. The flap plates are only 1 cm thick. That penetration would put ball1's centre within about 5 mm of flap1's mid-plane, and block's centre within a few mm of flap2's mid-plane. At that point the contact normal can flip and the object can tunnel through the flap. So I can't count on the chain working as written.

**Corrections in the file below**

- Contacts on the impacting geoms and the flap plates are stiffened to `solref="0.005 1"`, which should cut penetration to under 1 cm.
- The joint limits use the same value (`solreflimit`), which reduces overshoot at the stops.
- The flap plates are thickened to 3 cm, extending downward so their top surfaces stay at the same height.
- hoop2 is lowered to z = 0.14 to keep clearance under the thicker flap2 tip.

```json
{"what_happens": "ball1 falls through hoop1 into flap1's pocket; the impact tips flap1 to its lower stop, block falls off its tip into flap2's pocket, flap2 tips to its lower stop, and ball2 drops straight through hoop2 into the cup and settles. With default soft contacts, though, the ~4 m/s and ~2.6 m/s impacts penetrate 2-3 cm into 1 cm-thick flap plates, risking ball1 or block sinking through a flap.", "works": false, "problem": "Default soft contacts (solref 0.02) allow about 2-3 cm of penetration at the impact speeds, which is too deep for the 1 cm-thick flap plates, so ball1 or block may tunnel through a flap and break the chain."}
```

```xml
<mujoco model="trapdoor_chain">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.3 -1 3" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <body name="hoop1" pos="0.12 0 1.0">
      <geom name="hoop1_s0" type="capsule" size="0.006" fromto="0.0702 0.0291 0 0.0291 0.0702 0" rgba="0.9 0.5 0.1 1"/>
      <geom name="hoop1_s1" type="capsule" size="0.006" fromto="0.0291 0.0702 0 -0.0291 0.0702 0" rgba="0.9 0.5 0.1 1"/>
      <geom name="hoop1_s2" type="capsule" size="0.006" fromto="-0.0291 0.0702 0 -0.0702 0.0291 0" rgba="0.9 0.5 0.1 1"/>
      <geom name="hoop1_s3" type="capsule" size="0.006" fromto="-0.0702 0.0291 0 -0.0702 -0.0291 0" rgba="0.9 0.5 0.1 1"/>
      <geom name="hoop1_s4" type="capsule" size="0.006" fromto="-0.0702 -0.0291 0 -0.0291 -0.0702 0" rgba="0.9 0.5 0.1 1"/>
      <geom name="hoop1_s5" type="capsule" size="0.006" fromto="-0.0291 -0.0702 0 0.0291 -0.0702 0" rgba="0.9 0.5 0.1 1"/>
      <geom name="hoop1_s6" type="capsule" size="0.006" fromto="0.0291 -0.0702 0 0.0702 -0.0291 0" rgba="0.9 0.5 0.1 1"/>
      <geom name="hoop1_s7" type="capsule" size="0.006" fromto="0.0702 -0.0291 0 0.0702 0.0291 0" rgba="0.9 0.5 0.1 1"/>
    </body>

    <body name="ball1" pos="0.12 0 1.8">
      <freejoint name="ball1_free"/>
      <geom name="ball1_geom" type="sphere" size="0.03" mass="0.3" solref="0.005 1" rgba="0.2 0.3 0.9 1"/>
    </body>

    <body name="flap1" pos="0 0 0.8">
      <joint name="flap1_hinge" type="hinge" axis="0 1 0" limited="true" range="0 35" solreflimit="0.005 1"/>
      <geom name="flap1_plate" type="box" size="0.24 0.05 0.015" pos="0.12 0 -0.01" mass="0.1" solref="0.005 1" rgba="0.5 0.35 0.2 1"/>
      <geom name="flap1_counter" type="box" size="0.03 0.04 0.02" pos="-0.1 0 0" mass="1.3" rgba="0.3 0.3 0.3 1"/>
      <geom name="flap1_lip_in" type="box" size="0.005 0.05 0.02" pos="0.08 0 0.025" mass="0.01" solref="0.005 1" rgba="0.5 0.35 0.2 1"/>
      <geom name="flap1_lip_out" type="box" size="0.005 0.05 0.02" pos="0.16 0 0.025" mass="0.01" solref="0.005 1" rgba="0.5 0.35 0.2 1"/>
    </body>

    <body name="block" pos="0.34 0 0.825">
      <freejoint name="block_free"/>
      <geom name="block_geom" type="box" size="0.02 0.02 0.02" mass="0.3" solref="0.005 1" rgba="0.8 0.1 0.1 1"/>
    </body>

    <body name="flap2" pos="0.22 0 0.45">
      <joint name="flap2_hinge" type="hinge" axis="0 1 0" limited="true" range="0 35" solreflimit="0.005 1"/>
      <geom name="flap2_plate" type="box" size="0.24 0.05 0.015" pos="0.12 0 -0.01" mass="0.1" solref="0.005 1" rgba="0.5 0.35 0.2 1"/>
      <geom name="flap2_counter" type="box" size="0.03 0.04 0.02" pos="-0.1 0 0" mass="0.7" rgba="0.3 0.3 0.3 1"/>
      <geom name="flap2_lip_in" type="box" size="0.005 0.05 0.015" pos="0.08 0 0.02" mass="0.01" solref="0.005 1" rgba="0.5 0.35 0.2 1"/>
      <geom name="flap2_lip_out" type="box" size="0.005 0.05 0.015" pos="0.16 0 0.02" mass="0.01" solref="0.005 1" rgba="0.5 0.35 0.2 1"/>
      <geom name="flap2_lip_ball" type="box" size="0.005 0.05 0.008" pos="0.30 0 0.013" mass="0.01" rgba="0.5 0.35 0.2 1"/>
    </body>

    <body name="ball2" pos="0.56 0 0.485">
      <freejoint name="ball2_free"/>
      <geom name="ball2_geom" type="sphere" size="0.03" mass="0.1" condim="6" friction="1 0.005 0.001" solref="0.005 1" rgba="0.1 0.7 0.2 1"/>
    </body>

    <body name="hoop2" pos="0.56 0 0.14">
      <geom name="hoop2_s0" type="capsule" size="0.006" fromto="0.0702 0.0291 0 0.0291 0.0702 0" rgba="0.9 0.5 0.1 1"/>
      <geom name="hoop2_s1" type="capsule" size="0.006" fromto="0.0291 0.0702 0 -0.0291 0.0702 0" rgba="0.9 0.5 0.1 1"/>
      <geom name="hoop2_s2" type="capsule" size="0.006" fromto="-0.0291 0.0702 0 -0.0702 0.0291 0" rgba="0.9 0.5 0.1 1"/>
      <geom name="hoop2_s3" type="capsule" size="0.006" fromto="-0.0702 0.0291 0 -0.0702 -0.0291 0" rgba="0.9 0.5 0.1 1"/>
      <geom name="hoop2_s4" type="capsule" size="0.006" fromto="-0.0702 -0.0291 0 -0.0291 -0.0702 0" rgba="0.9 0.5 0.1 1"/>
      <geom name="hoop2_s5" type="capsule" size="0.006" fromto="-0.0291 -0.0702 0 0.0291 -0.0702 0" rgba="0.9 0.5 0.1 1"/>
      <geom name="hoop2_s6" type="capsule" size="0.006" fromto="0.0291 -0.0702 0 0.0702 -0.0291 0" rgba="0.9 0.5 0.1 1"/>
      <geom name="hoop2_s7" type="capsule" size="0.006" fromto="0.0702 -0.0291 0 0.0702 0.0291 0" rgba="0.9 0.5 0.1 1"/>
    </body>

    <body name="cup" pos="0.56 0 0">
      <geom name="cup_base" type="cylinder" size="0.08 0.005" pos="0 0 0.005" solref="0.005 1" rgba="0.6 0.6 0.9 1"/>
      <geom name="cup_w0" type="box" size="0.005 0.033 0.04" pos="0.075 0 0.05" euler="0 0 0" rgba="0.6 0.6 0.9 1"/>
      <geom name="cup_w1" type="box" size="0.005 0.033 0.04" pos="0.053 0.053 0.05" euler="0 0 45" rgba="0.6 0.6 0.9 1"/>
      <geom name="cup_w2" type="box" size="0.005 0.033 0.04" pos="0 0.075 0.05" euler="0 0 90" rgba="0.6 0.6 0.9 1"/>
      <geom name="cup_w3" type="box" size="0.005 0.033 0.04" pos="-0.053 0.053 0.05" euler="0 0 135" rgba="0.6 0.6 0.9 1"/>
      <geom name="cup_w4" type="box" size="0.005 0.033 0.04" pos="-0.075 0 0.05" euler="0 0 180" rgba="0.6 0.6 0.9 1"/>
      <geom name="cup_w5" type="box" size="0.005 0.033 0.04" pos="-0.053 -0.053 0.05" euler="0 0 225" rgba="0.6 0.6 0.9 1"/>
      <geom name="cup_w6" type="box" size="0.005 0.033 0.04" pos="0 -0.075 0.05" euler="0 0 270" rgba="0.6 0.6 0.9 1"/>
      <geom name="cup_w7" type="box" size="0.005 0.033 0.04" pos="0.053 -0.053 0.05" euler="0 0 315" rgba="0.6 0.6 0.9 1"/>
    </body>
  </worldbody>
</mujoco>
```

---
thinking (summarized):

I'm double-checking the joint limit setup: with range 0-35 and qpos0=0, a positive angle rotation about the y-axis tips the point downward, so the limit constraint is already active right at qpos=0, which makes sense.

Ball1 falls from 1.8 down to around 0.965-0.835 on contact, passing through hoop1's inner radius without issue. For the flap tipping, I'm checking whether the block separates from flap1 during impact — with friction 1 and a 35° tilt (tan35≈0.7), the block wouldn't normally slide off a static incline, but the sudden angular acceleration during impact should be enough to launch it clear before the flap settles against its stop, so it should fall freely rather than ride down with the plate.

With outward drift of about 8mm over the 0.27s fall, that's well within the 15mm pocket clearance, so the block should land fine. Now I'm estimating impact dynamics: the ball at 4.35 m/s hitting the flap gives an effective mass around 1.15 kg at the contact radius, and with the default contact softness time constant of 0.02s, the impact duration should be roughly that same order.

Working through the angular response, the flap's angular acceleration during impact comes out to around 250 rad/s², giving tip acceleration above g, so separation does occur as expected. I'm now double-checking whether the soft contact model's penetration depth at this impact velocity could be large enough to matter, looking at how the solver's reference acceleration and damping terms scale with penetration velocity.

I'm worried the plate's 1cm thickness could let the ball tunnel through if penetration gets that deep, since the sphere-box contact normal depends on the ball center staying above the plate's centerline. Still, my intuition from typical MuJoCo setups is that a ball dropped onto a thin box at small timesteps usually doesn't pass through, so this risk is probably manageable in practice.

Given the relative masses, the penetration estimate still lands around the centimeter scale once I account for the solimp ramp-up near zero penetration. This matches what I recall about MuJoCo's default soft-contact behavior—fast-moving bodies with the standard solref do show noticeable sinking before the spring response catches up, so a centimeter-scale penetration at this speed seems physically plausible rather than a bug.

Now checking flap2: block hits at 2.6 m/s with about 1.8 cm penetration against a 1 cm thick plate, which risks exceeding the plate's full thickness and causing the box-box collision solver to pick a strange contact normal — I need to check whether the overlap axis along z stays sane once the block sinks past the plate bottom.

A safer fix is to thicken the plates (maybe to 1.5 cm half-thickness) and tighten the solref timeconst for impact contacts, keeping it at least twice the timestep so collisions don't go unstable.

Checking the rest of the sequence: flap2 holding ball2 statically near its tip looks fine, the lip at the hinge side keeps the block in place at 35°, and the angular acceleration for flap2's release (~210 rad/s²) gives tip acceleration exceeding gravity, so the ball should separate properly as expected.

Ball2 then drops into the cup, reaching about 2.95 m/s before contact, penetrating roughly 2 cm into the base — still above the base's own center, and the floor plane catches it anyway so nothing clips through. There's no lateral velocity so it should settle cleanly, hoop2's clearance relative to flap2's tip looks fine, and flap1 should simply rest against its lower stop once it overshoots, since the torque stays positive there.

I'm also checking the block's fall onto flap2 — timing works out since flap1's tip is clear by then, and the rolling contact for ball2 on flap2 seems stable given the friction settings. The penetration into the 1 cm plate is the real worry though: using the relative-coordinate spring-damper math, I get about 3 cm of penetration against only a 0.5 cm margin above centerline, which is tight. But since the contact impedance isn't perfectly rigid, the force gets regularized rather than following the pure critical-damping reference acceleration exactly, so actual penetration should be somewhat less than my estimate.

The fix is to make contact stiffer by setting a tighter solref on the ball, block, and flap geoms, since right now the combined solref gets averaged with defaults via solmix weighting, which softens things. I should apply solref="0.005 1" consistently across the balls, block, flap plates, and cup base so penetration stays within the available margin.

Thickening the plates means I need to shift objects up slightly to preserve the same geometry — putting the plate center at a small negative z so the top surface stays at the original height while adding bulk below, avoiding disrupting the resting positions of balls and blocks on top.

Checking clearance at flap2's tip when swung to 40°, it lands about 1.4cm above hoop2's top, which is tight — I'll lower hoop2 to around 0.14 to give more room, confirming the ball still falls through the center fine and the cup/hoop dimensions stay consistent. Now checking flap1's tip position at its stop angle of 35° to make sure it clears similarly.

Checking overshoot at the limit stop: with flap angular velocity around 7 rad/s, overshoot comes out to roughly 2.8°, which is acceptable, though tightening solreflimit could help further. My real concern is that the default soft contact penetration depth (~3cm) against 1cm-thick flap plates risks the balls or block sinking through at high speed, so I'll flag this as a real issue and provide a corrected file.

