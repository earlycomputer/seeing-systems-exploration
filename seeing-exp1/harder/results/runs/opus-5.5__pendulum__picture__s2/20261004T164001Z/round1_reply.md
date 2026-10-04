## What the picture shows

The pendulum swings and leaves a fan of copies around its hinge. Its first, lightest copy is high on the left, where it starts.

The ball ends as a dark dot at about x ≈ 0.56 m, just short of the foot of the ramp. There are no ball copies inside the cup.

## Why it failed

The ball never got up the ramp. It reached the ramp too slowly to climb the 6 cm, or it climbed part way and rolled back. I can't tell which from the picture, or whether the pendulum hit it again on the way back.

My speed margin was too thin: about 1.2 m/s expected against about 0.95 m/s needed.

## Changes

- **Faster ball.** The pendulum now starts at 1.10 rad instead of 0.86 rad. That should give the ball a rolling speed of about 1.5–2.2 m/s.
- **Taller cup.** The cup walls are now 0.12 m, so a fast ball can't fly over the far side.
- **Spout notch.** A notch of 0.06 m walls faces the ramp, and the ramp top still meets the notch rim. The ball enters through the notch and drops in. Once inside, the inner face of the notch (0.06 m) is taller than the ball (0.06 m across) and twice its radius, so it can't climb back out.
- **Wider speed window.** This should now be roughly 0.95–2.5 m/s, comfortably around the expected range.

```json
{"what_happens": "The pendulum swings down and strikes the ball, but the ball ends the run on the floor at about x = 0.56 m, just short of the ramp foot, never entering the cup at x = 1.", "works": false, "problem": "The ball arrives at the ramp too slowly (or rolls back down it) and never climbs into the cup, because the strike speed left almost no margin over what the 6 cm ramp requires."}
```

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="0.5 -1 3" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.75 1"/>

    <!-- visual-only support frame for the pendulum -->
    <geom name="frame_post_left" type="cylinder" fromto="-0.056 0.15 0 -0.056 0.15 0.56" size="0.01" contype="0" conaffinity="0" rgba="0.3 0.3 0.35 1"/>
    <geom name="frame_post_right" type="cylinder" fromto="-0.056 -0.15 0 -0.056 -0.15 0.56" size="0.01" contype="0" conaffinity="0" rgba="0.3 0.3 0.35 1"/>
    <geom name="frame_axle" type="cylinder" fromto="-0.056 -0.15 0.53 -0.056 0.15 0.53" size="0.008" contype="0" conaffinity="0" rgba="0.3 0.3 0.35 1"/>

    <!-- pendulum: hinge at 0.53 m, bob centre 0.5 m below hinge (z = 0.03 at bottom, level with ball centre) -->
    <body name="pendulum" pos="-0.056 0 0.53">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.475" size="0.006" mass="0.05" rgba="0.6 0.6 0.65 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.025" mass="1.0" rgba="0.75 0.2 0.2 1"/>
    </body>

    <!-- ball resting on the floor at x = 0 -->
    <body name="ball" pos="0 0 0.03">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" mass="0.1" rgba="0.95 0.95 0.95 1"/>
    </body>

    <!-- entry ramp: top surface rises from (0.62, 0) to (0.87, 0.06), meeting the cup's spout notch -->
    <geom name="ramp" type="box" pos="0.74733 0 0.02028" euler="0 -13.496 0" size="0.12855 0.05 0.01" rgba="0.55 0.45 0.3 1"/>

    <!-- cup centred 1 m from the ball's start: base disc plus 16 wall slats, inner radius 0.12, walls 0.12 high with a 0.06 high spout notch facing the ramp -->
    <body name="cup" pos="1 0 0">
      <geom name="cup_base" type="cylinder" pos="0 0 0.002" size="0.13 0.002" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_00" type="box" pos="0.125 0 0.06" euler="0 0 0" size="0.005 0.026 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_01" type="box" pos="0.11548 0.04784 0.06" euler="0 0 22.5" size="0.005 0.026 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_02" type="box" pos="0.08839 0.08839 0.06" euler="0 0 45" size="0.005 0.026 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_03" type="box" pos="0.04784 0.11548 0.06" euler="0 0 67.5" size="0.005 0.026 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_04" type="box" pos="0 0.125 0.06" euler="0 0 90" size="0.005 0.026 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_05" type="box" pos="-0.04784 0.11548 0.06" euler="0 0 112.5" size="0.005 0.026 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_06" type="box" pos="-0.08839 0.08839 0.06" euler="0 0 135" size="0.005 0.026 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_07" type="box" pos="-0.11548 0.04784 0.03" euler="0 0 157.5" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_08" type="box" pos="-0.125 0 0.03" euler="0 0 180" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_09" type="box" pos="-0.11548 -0.04784 0.03" euler="0 0 202.5" size="0.005 0.026 0.03" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_10" type="box" pos="-0.08839 -0.08839 0.06" euler="0 0 225" size="0.005 0.026 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_11" type="box" pos="-0.04784 -0.11548 0.06" euler="0 0 247.5" size="0.005 0.026 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_12" type="box" pos="0 -0.125 0.06" euler="0 0 270" size="0.005 0.026 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_13" type="box" pos="0.04784 -0.11548 0.06" euler="0 0 292.5" size="0.005 0.026 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_14" type="box" pos="0.08839 -0.08839 0.06" euler="0 0 315" size="0.005 0.026 0.06" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_15" type="box" pos="0.11548 -0.04784 0.06" euler="0 0 337.5" size="0.005 0.026 0.06" rgba="0.2 0.4 0.8 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="1.10  0 0 0.03  1 0 0 0" qvel="0  0 0 0  0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm trying to parse the image layout, looking at where the ball and pendulum residue marks fall relative to the cup position across the pixel coordinates.

Good, so the scale factor actually applies to the 128px image directly, confirming cup, hinge, and fan positions align. Now I'm checking that leftover mark near px 15-20 in the top view — mapping its coordinates suggests it's the pendulum bob at its starting angle rather than a separate object.

Near the cup I'm tracking another dot around px 78 along with a ramp line leading toward the cup circle at px 100-110, trying to figure out if that dot marks the ball's position before the ramp.

I'm puzzled because if the ball ended at x≈0.56 before the ramp, that implies it climbed the ramp, failed to clear it, and rolled back—but without friction it shouldn't settle there; it should keep rolling back toward the pendulum indefinitely, so something about this stopping point doesn't add up physically.

Actually checking the pendulum swing fan, the arc looks roughly symmetric before and after impact, suggesting it retained most of its energy rather than transferring much to the ball. With mass ratio 1:0.1, the pendulum should keep about 90% of its speed, meaning the ball ought to come away with around 1.8 m/s — so maybe the ball wasn't actually struck cleanly, and that small gap near the bob's resting position is throwing off my read of where contact happened.

Rechecking against the cup position, the ramp spans roughly x=0.62 to 0.87, and the ball's dot in the plan view actually lines up near x≈0.56, right at the base of the ramp. That means the ball never made it up — it likely rolled partway up and came back down, sitting near the ramp's foot at t=6s rather than reaching the cup.

Could the bob have struck the ball off-center, or hit it late during the swing rather than at the bottom? The pendulum's hinge position and swing angle suggest the bob passes through the bottom moving fast enough, so a soft-contact timing issue in the physics engine seems more plausible than a slow hit.

Ruling out static objects (floor, frame, ramp, cup) since none sit at that pixel location, I'm confident the dot at px 78 must be the ball, likely resting near the ramp's base. That points to a scenario where the ball climbed partway up the ramp, didn't have enough speed to crest it, and rolled back down to settle near where it started.

Checking the arithmetic though, if the ball returned by around 1 second, it would have drifted much farther by 6 seconds than what's shown, so that scenario doesn't fit. This pushes me toward thinking the ball's overall motion was very slow, averaging roughly 0.1 m/s, or alternatively that it was repeatedly struck by the swinging pendulum, which has a period of about 1.42 seconds and leaves motion-blur copies at fixed intervals across its arc that I'm now trying to map against the visible pixel range.

Estimating the pendulum's energy loss from amplitude change — starting around 49° and settling near 30° — gives roughly a 60% drop in energy, which seems too large to be explained by the ball alone at a modest mass and speed, so something else must be absorbing that energy.

I'm checking whether the bob or rod could be clipping the floor given the clearances, but the geometry seems fine with enough gap, so that's probably not the cause.

I'm reconsidering whether the ball actually got struck hard enough to explain its motion, but the masses and keyframe values don't obviously support a big impulse, so maybe the discrepancy isn't from a direct collision at all. Rather than keep guessing, I should look more carefully at whether the frame's components (like the axle, which has collisions disabled) could be involved in whatever's causing this energy discrepancy.

Actually maybe the ball doesn't reach the ramp top and rolls back, potentially re-colliding with the swinging pendulum bob near the bottom of its arc since the bob alternates direction every 0.7s. That could kick the ball back toward the ramp again, creating a repeated bounce cycle between the pendulum and ramp before settling at a final position.

Looking at the plan view, I notice a faint horizontal residue line and a cross shape near the pendulum location—likely the axle frame crossed with the swing arc—which supports this back-and-forth interpretation. The real puzzle is why the ball fails to make it up the ramp into the cup; it could be that my rolling-speed estimate is too generous, or the kink at the ramp's foot absorbs more energy than I assumed.

I should also consider friction effects at the bob-ball contact point—if the bob keeps rising after impact, a second contact from above could impart backspin that saps forward momentum. Checking whether MuJoCo properly handles rolling behavior for a sphere on a plane with condim 3 contacts, and whether soft-contact restitution in sphere-sphere collisions could be sapping energy unexpectedly.

Now I'm double-checking the ramp's rotation sign via the euler angle convention, verifying how a rotation about the y-axis by angle β maps the x-axis under MuJoCo's intrinsic xyz sequence.

I'm also ruling out other failure points: checking whether the ball clears the cup walls and ramp top, whether the bob's initial position or floor contact could be causing issues, and confirming the swing direction matches the image (bob starting at the left side). None of these seem to be the actual problem, so I'm still searching for what's really going wrong.

I'm now reconsidering whether the final dot position really represents a resting ball, since without rolling friction a sphere on a plane should keep rolling rather than stop — though MuJoCo's soft contacts might introduce some damping. This suggests a more chaotic scenario: the ball rolling up the ramp, failing to clear it, rolling back, and possibly getting struck again by the pendulum in a repeating cycle.

The core issue seems to be insufficient speed to climb the ramp, so I'm weighing fixes like giving much more speed margin, avoiding the ramp design entirely, or redesigning the cup so it reliably catches the ball regardless of incoming speed. A shorter cup wall feels too marginal given the ball's size, so I'm thinking about alternatives like uneven wall heights or simply increasing the ball's rolling speed substantially while keeping the walls tall enough to contain it.

Now I'm running the numbers for a taller cup (walls at 0.12m matching the ramp height) with a higher rolling speed around 2.5-3 m/s, checking whether the minimum speed to climb the ramp and the trajectory after leaving the rim still lands the ball safely against the back wall rather than overshooting.

This feels too fragile for high speeds, so I'm considering adding a dedicated backstop — a tall backboard positioned right behind the cup's back wall. The idea is that any ball flying over the rim at speed would strike this backboard and get redirected back down into the cup instead of escaping, making the catch robust even if timing calculations are slightly off.

I'm also reconsidering my speed estimate — maybe the ball's actual rolling speed is higher than assumed, or there's backspin from the pendulum follow-through. I'm recalculating trajectories at higher velocities (around 2.0 m/s at the ramp top) to check whether the ball would clear or hit the inner rim, factoring in horizontal and vertical velocity components at the point it reaches the cup's far edge.

I realize keeping all walls equal height is causing the ball to overshoot, so I'm considering an uneven design — a cup with a notch or spout at the front where the ramp meets it, with shorter walls there and taller walls (0.12) everywhere else, including the back, to catch the ball before it escapes.

Checking the back wall at 0.12 height: with velocities around 2.4-2.5, the ball's center stays just below the wall top, so it strikes the face rather than clearing it — meaning the valid speed window is roughly 0.95 to 2.5, with 1.6 as a good target. To get the pendulum to deliver that speed after the roll, I'm working out the required release angle, landing around θ≈1.18 radians.

I'm also second-guessing whether a weaker-than-expected strike could stem from something else — maybe the second contact between the bob and ball changes the dynamic, since the bob continues following at a similar speed to the ball post-roll.

Checking the geometry near the ramp's lower edge, I'm trying to confirm where the sloped top meets the floor and whether the ball might be clipping that kink, which could cause a small energy loss. I'm also re-examining my pixel-to-coordinate mapping for the top-view image, since the row-to-height conversion might be off and throwing my z-estimate for the ball's position.

For now, I'll leave the ramp kink loss as-is and instead increase overall energy and add a tall-walled spout notch. I also want to verify the pendulum's starting geometry — hinge position, arm length, and initial angle — which seems consistent with the bob's computed starting coordinates.

After the strike, the pendulum swings to the positive x side with roughly 55° amplitude, landing well short of where the ramp begins, so no collision there. I don't think I need added rolling friction for the ball to settle into the cup, and the notch-and-tall-slat wall configuration (with tall slats at 0.06 half-height and notch slats at 0.03) should let the ball pass through the gap cleanly while being contained by the taller neighboring slats.

