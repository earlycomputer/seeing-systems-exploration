This scene is tuned by hand calculation only. I haven't run it in MuJoCo, so the ball's speed and whether it ends in the cup are estimates.

**How it works**
- **The swing:** A 1 kg pendulum bob on a 0.5 m arm is released from 42°. It reaches about 1.6 m/s at the bottom and hits the ball just as it passes the lowest point.
- **The roll:** The bob is heavy and its contact with the ball has no friction. The ball should leave the bob, slip briefly on the floor, then roll at roughly 1.4 m/s.
- **Into the cup:** A small amount of rolling friction slows the ball slightly. It then climbs a 14° ramp to the 5 cm rim of an eight-sided cup centred at x = 1 m and drops in.
- **Coming to rest:** The cup's inside diameter is 22 cm, so the ball should land well short of the far wall. Collisions in MuJoCo lose most of their energy, and rolling friction stops what is left, so the ball should settle in the cup.

**Margin:** By my estimates, the ball should still reach the rim and stay in the cup if its rolling speed is anywhere from about 0.95 to 1.9 m/s. The target is about 1.44 m/s.

**What I'd check first in a run:**
- The ball's speed as it reaches the ramp.
- That it clears the rim.
- That it finishes inside the cup moving slower than 5 cm/s.

If it falls short or overshoots, the release angle (the first `qpos` value) is the easiest number to change.

```xml
<mujoco model="pendulum_ball_cup">
  <option timestep="0.002"/>
  <worldbody>
    <light name="sun" pos="0.5 0 3" dir="0 0 -1" diffuse="0.8 0.8 0.8"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <geom name="frame_post_left" type="capsule" fromto="-0.06 0.15 0 -0.06 0.15 0.535" size="0.01" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <geom name="frame_post_right" type="capsule" fromto="-0.06 -0.15 0 -0.06 -0.15 0.535" size="0.01" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <geom name="frame_axle" type="capsule" fromto="-0.06 -0.15 0.535 -0.06 0.15 0.535" size="0.008" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>

    <body name="pendulum" pos="-0.06 0 0.535">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.47" size="0.006" mass="0.05" rgba="0.3 0.3 0.3 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.5" size="0.03" mass="1.0" condim="1" priority="1" rgba="0.7 0.1 0.1 1"/>
    </body>

    <body name="ball" pos="0 0 0.03">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" mass="0.05" condim="6" friction="1 0.005 0.0003" rgba="0.1 0.3 0.9 1"/>
    </body>

    <geom name="ramp" type="box" pos="0.78121 0 0.02015" euler="0 -14.036 0" size="0.10308 0.06 0.005" rgba="0.5 0.5 0.3 1"/>

    <body name="cup" pos="1 0 0">
      <geom name="cup_bottom" type="cylinder" pos="0 0 0.0025" size="0.12 0.0025" rgba="0.9 0.6 0.1 1"/>
      <geom name="cup_wall_0" type="box" pos="0.115 0 0.025" euler="0 0 0" size="0.005 0.05 0.025" rgba="0.9 0.6 0.1 1"/>
      <geom name="cup_wall_45" type="box" pos="0.08132 0.08132 0.025" euler="0 0 45" size="0.005 0.05 0.025" rgba="0.9 0.6 0.1 1"/>
      <geom name="cup_wall_90" type="box" pos="0 0.115 0.025" euler="0 0 90" size="0.005 0.05 0.025" rgba="0.9 0.6 0.1 1"/>
      <geom name="cup_wall_135" type="box" pos="-0.08132 0.08132 0.025" euler="0 0 135" size="0.005 0.05 0.025" rgba="0.9 0.6 0.1 1"/>
      <geom name="cup_wall_180" type="box" pos="-0.115 0 0.025" euler="0 0 180" size="0.005 0.05 0.025" rgba="0.9 0.6 0.1 1"/>
      <geom name="cup_wall_225" type="box" pos="-0.08132 -0.08132 0.025" euler="0 0 225" size="0.005 0.05 0.025" rgba="0.9 0.6 0.1 1"/>
      <geom name="cup_wall_270" type="box" pos="0 -0.115 0.025" euler="0 0 270" size="0.005 0.05 0.025" rgba="0.9 0.6 0.1 1"/>
      <geom name="cup_wall_315" type="box" pos="0.08132 -0.08132 0.025" euler="0 0 315" size="0.005 0.05 0.025" rgba="0.9 0.6 0.1 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.733 0 0 0.03 1 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm laying out the scene geometry: a ball near the origin, a cup a meter away along x, and a pendulum positioned to swing in the xz plane and strike the ball at the bottom of its arc, sending it rolling toward the cup. I'm thinking through how friction and rolling resistance need to be tuned so the ball travels the full distance and settles inside the cup rather than overshooting or stopping short.

I consider a cup lying on its side with the mouth facing the ball, but that leaves the floor awkward since the cup's curved wall would sit on the ground. I think an upright cup with low walls plus a small ramp leading up and over the lip is the most physically honest setup, even though tuning the trajectory to land inside will be tricky.

For the ramp approach I need the ball to launch off the ramp's end, drop inside, bounce with friction, and settle—but if the near wall is short enough for the ball to clear, the far wall needs to be tall enough to actually catch it rather than let the ball roll right over, so all the walls should share the same adequate height.

Maybe uniform tall walls with a ramp leading to the rim would work better. I'll try specific dimensions: ball radius 0.025, cup inner radius 0.06, wall height 0.04, with a ramp rising at roughly 17°, though I'm worried about a bump at the ramp's base causing unpredictable bounces. Since I can't actually simulate the physics, I need a design that's robust to this uncertainty, relying on MuJoCo's friction model to keep the ball rolling naturally rather than bouncing unpredictably.

The pendulum strike sets the ball rolling with some energy loss from slide-to-roll transition, so the final speed is uncertain. I'm thinking a robust approach is to make the far wall taller than the near wall — if the ball comes in too fast it bounces off the tall backstop and stays trapped, if too slow it just rolls back down the ramp and fails, so I want to bias toward slightly excess speed with margin. I'm now considering skipping the ramp approach entirely and finding an alternative.

Friction will eventually convert spin back into forward motion against the wall and settle the ball there, so adding rolling friction damping should ensure it stays put inside. Though I'm second-guessing whether a slotted wall really counts as a "cup" per the brief — maybe a simple ring or rim shape on the floor would be more faithful to that description.

I thought about a low ring wall shorter than the ball radius so the ball could climb over, but that's the classic step-climbing problem with energy loss that's hard to make robust. Better to stick with a ramp leading into a cup with a tall back wall, sized so the ball's landing point can't reach the far wall.

Now I'm estimating actual numbers: ball radius 0.03, mass around 0.05 kg, with MuJoCo's soft contact behaving close to inelastic (critically damped solref, restitution near zero). That means after the pendulum bob strikes the ball, they'd roughly share a common velocity rather than bouncing elastically, and the bob would keep decelerating as it swings upward against gravity.

With a much heavier bob, the ball's velocity approaches the bob's impact velocity, then transitions from sliding to rolling at 5/7 of that speed due to friction. Factoring roughly ±20% uncertainty, I check whether the ball retains enough rolling kinetic energy to climb a 0.04 m rise on the ramp, which requires v² > 0.56, so v needs to exceed about 0.75 m/s.

Accounting for energy loss at ramp entry, I pick v_roll ≈ 1.2 m/s, giving v_top ≈ 0.94 m/s after the climb. Computing fall time over the 0.04 m drop gives about 0.09 s, translating to roughly 0.085 m of horizontal travel, and I need to size the cup's inner diameter so the ball clears the rim edge and lands with margin — landing at about 0.085 m plus the ball's diameter suggests an inner diameter around 0.2 m works.

Checking the sensitivity across v_roll from 1.0–1.5 m/s, travel ranges 0.06–0.115 m, which stays safely within a 0.2 m diameter cup, though below about 0.75 m/s the ball won't make it up the ramp at all. I'm also accounting for the ramp's 15° slope (0.04 m rise over 0.15 m length) and the energy lost when the ball transitions onto the incline — roughly a 7% KE loss from the cosine component, plus some spin mismatch.

The tricky part is the far wall: with wall height 0.04 m and the ball's center at 0.03 m, the wall face sits above the ball's center, so contact pushes the ball back down rather than letting it climb over. I'm weighing whether to raise the rim to 0.05 m for safety, which would require incoming speed above roughly 0.84 m/s to climb (from the energy condition v² > (10/7)×9.81×0.05 ≈ 0.7). I'm also considering whether a small bounce from soft contact damping after the drop could help the ball clear that wall.

Given the near-zero restitution from the wall contacts, the ball will likely oscillate briefly then settle against the far wall, with spin-driven friction gradually dissipating momentum until it comes to rest well under 5 cm/s. I'm considering adding rolling friction to the ball's contact properties to help it settle faster, estimating the deceleration from rolling resistance torque relative to gravity and radius.

I should add a small rolling friction coefficient, around 0.0003, so residual rolling velocity decays to zero within a second rather than bouncing indefinitely between walls. I also need to set condim 6 on the ball geom with appropriate friction values, keeping torsional friction small since spin isn't really relevant here, and remember that contact friction combines as the max between the two geoms involved.

Thinking about the pendulum after it strikes the ball—since the ball leaves nearly at the bob's speed while the pendulum decelerates, the pendulum will keep swinging back and forth but the ball will be long gone by the time it swings through bottom again, so undamped motion is fine. I should make sure the pendulum's support structure, if I add one in the worldbody, uses side posts so it doesn't block the ball's path.

Now I'm working out the geometry: the bob's bottom must stay above the floor, so I'll place the pivot and set the bob radius so contact with the ball happens right as the bob passes the bottom of its swing, positioning the pivot horizontally offset by the sum of the bob and ball radii plus a small clearance.

Let me make the bob a sphere matching the ball's radius, with its lowest point about 5mm above the floor so the contact point is slightly offset, giving a gentle downward push on the ball. Now I need to work out the pendulum length and release angle so the bob's speed at the bottom matches a target velocity, accounting for the mass ratio and restitution in the collision with the ball.

MuJoCo's default contact parameters use critical damping, meaning the collision behaves almost perfectly inelastically (the separation velocity is essentially zero, so restitution e≈0) rather than bouncing elastically. Since the bob is heavy and swinging forward, after contact the ball and bob share a common velocity momentarily, then the bob decelerates on its rising arc due to gravity while the ball keeps moving at that shared speed — so the ball's final velocity depends roughly on the mass ratio between bob and ball.

With M_bob=1kg and m_ball=0.05kg, that ratio is nearly 1, so the ball inherits almost the full bob velocity. But I also need to account for the ball initially sliding on the floor with friction before transitioning to rolling at 5/7 of its initial speed — and whether the bob catches up to the ball while it's still decelerating during that slide phase.

Checking the numbers: the bob's tangential deceleration near the bottom of its arc is nearly zero, while the ball decelerates from sliding friction over about 0.05s, so the bob could actually catch up and keep pushing the ball forward rather than just handing off velocity once. That complicates the clean elastic-collision picture since the ball ends up being pushed along the ground while the bob is still in contact.

I think a cleaner fix is to make the bob-ball collision more elastic by tuning the contact solref for higher restitution, so the ball launches at roughly (1+e)*M/(M+m) times the bob's speed. With e somewhere around 0.6-0.9, the ball should exit faster than the bob and stay ahead even after sliding friction decelerates it to 5/7 of its initial speed — rough estimate suggests e needs to exceed about 0.47. The uncertainty in e is still a problem though.

A better idea might be striking the ball at its "sweet spot" height (2r/5 above center, or 7r/5 above the floor contact) so it begins rolling without slipping immediately, avoiding the sliding deceleration phase entirely. With near-zero restitution, the bob and ball reach a common velocity at impact, then the bob decelerates while the ball rolls off cleanly at constant speed — this seems like the cleanest solution.

Wait, there's a problem: for sphere-on-sphere contact, the normal impulse always passes through the ball's center regardless of impact height, so there's no way to create torque through the normal force alone — only friction can provide torque at the contact point, which complicates the "sweet spot" idea. I think I need to go back to accepting the sliding phase and reconsider the heavy-pendulum-bob approach instead.

Once rolling without slip kicks in, floor friction stops and the ball coasts at roughly bob speed while the bob decelerates going uphill. I'm working through the contact geometry at the bob-ball interface to figure out whether the spinning ball's back surface moves up or down relative to the bob, since that determines the direction of friction there.

Since contact friction takes the max of the two geoms' coefficients, I realize I need to use priority to control which surface's parameters actually get applied. I'm setting the bob to condim 1 with priority 1 so it stays frictionless at that contact, which should prevent the bob-ball friction from fighting the ball's spin-up, while leaving the ball-floor contact to take the ball's higher condim and friction values as before.

Then I work through the physics: the ball spins up due to friction force f=μN from the floor, giving angular acceleration f·r/I, and I derive the impulse needed for the ball to reach rolling speed, roughly 2mv/5, to estimate how much the bob's velocity gets reduced by this friction interaction.

Combining these effects, I estimate the ball ends up rolling at around 0.93 times the bob's impact velocity, after accounting for the momentum loss during spin-up and the small rise of the bob's center during the slip phase, which produces a modest additional deceleration.

Checking the geometry, the distance at the bottom works out to about 0.0602, just slightly more than 0.06, so there's only a 0.2mm gap and contact happens right after the bottom point—I'll just set the pivot at x_p=−0.06 for simplicity, with the ball starting at x=0 and the cup centered at x=1.0.

Now I'm working through the rolling friction physics for MuJoCo's condim 6 setting, thinking about how the constraint torque opposes rotation up to μr*N, and setting up the coupled equations for linear deceleration and angular deceleration of the rolling ball.

Estimating the deceleration gives about 0.070 m/s² using μr=0.0003 and r=0.03. For the target ramp velocity, I'm aiming for around 1.3 m/s to clear the climb (needing roughly 0.75 m/s minimum given the 0.04m height plus losses), while checking the upper bound doesn't send the ball flying too far past the landing zone—working out that at 1.6 m/s the ball would land around 0.12m beyond, which needs checking against the wall's inner face position.

Confirming the ball leaving the ramp edge launches horizontally as expected, and small seams between the ramp and wall tops are acceptable since they're smaller than the ball. Now I'm working out precise geometry: the cup center sits at x=1.0 with inner radius 0.1 and wall thickness 0.01, meaning the near wall spans roughly x=0.89 to 0.90, and I need to figure out where the ramp starts relative to that.

I'm calculating a ramp with horizontal length 0.16 and height 0.04, giving a slope angle of about 14 degrees, running from x=0.73 to x=0.89. For the cup shape, I'm deciding whether to approximate a round cup using multiple box segments around a circle, or just keep it simple as a square cup with four walls — and considering whether to add a thin bottom plate for realism, which would slightly reduce the drop height but make the landing more physically sensible.

Working through the octagon approach with 8 wall segments: I'm computing the apothem, segment thickness, and tangential half-length so the segments fit together with slight overlap, then positioning the near-facing wall segment so its inner face aligns with x=0.89, matching the ramp's end point and the wall height of 0.04.

For the ramp itself, I'm figuring out the tilted box geometry: the top surface needs to run from (0.73,0) to (0.89,0.04), giving a slope length of about 0.165, with box half-sizes roughly (0.0825, 0.05, 0.005), then working out the pitch rotation needed to align the box's top face with that sloped line.

I'll put the ramp in the worldbody as a separate static geom named "ramp" rather than attaching it to the cup, since static geoms won't collide with each other or with the static cup body, which avoids unwanted collision pairs. Now I'm checking the exact position of the ramp's low edge to make sure the top surface meets the floor cleanly at x=0.73.

I'm checking whether the ball will actually climb the far wall given its center height versus the wall's top edge — since there's no vertical lift at that contact point, it likely won't bounce out unless I add more speed. To be safe, I'll bump the rim height up to 0.05 and adjust the ramp length accordingly for a more reliable cup shape.

Checking the landing trajectory for both slow and fast roll speeds confirms the ball clears the inner edge and lands within the far wall before reaching 0.17m travel, so a 0.22m inner diameter gives enough margin. I'm also confirming the ball stays clear of the rim while airborne and that wall thickness doesn't interfere, then considering what happens when it finally hits the far wall and possibly rebounds slightly.

Working through the rolling friction losses between launch and the ramp, I get a target launch speed around 1.44 m/s with roughly ±30% margin on either side, which gives decent tolerance for variation. Now I'm shifting to sizing the pendulum length.

Using L=0.5 and v_bob=1.6, I compute 1-cosθ = v²/(2gL) ≈ 0.261, giving θ≈42.4°. To refine, I account for the pendulum as a physical system rather than a point mass — treating the bob as a sphere (1 kg, r=0.03) and adding a light rod (0.05 kg, ~0.47 m) to estimate the combined moment of inertia, since these corrections will shift the effective swing angle slightly.

Working out the rotation direction: applying R_y to the downward vector shows positive angle swings the bob toward −x, so setting the hinge qpos to 0.733 with axis (0,1,0) releases it there and it swings to +x as intended. The effective mass from inertia over L² comes out to about 1.016 kg, and the ball's density works out fine at roughly 442 for a 0.03 radius sphere.

Now I'm figuring out the rod's capsule geometry connecting pivot to bob, checking that the bob and rod overlap without colliding since they're the same body, and then checking whether the rod could clip into the ball at the bottom of the swing based on their respective radii and positions.

Next I'm working out the support frame—posts at the pivot's x position and crossbar at the pivot height—and reasoning through MuJoCo's default collision filtering rules between a body and its parent, since the pendulum rod is parented to the world and I need to make sure it won't erroneously collide with or ignore the support structure.

Actually simplifying, I decide to just disable collisions on the frame geoms entirely (contype/conaffinity 0) so the rod can start right at the pivot without worrying about overlap math. That resolves the crossbar clearance issue cleanly, and the posts at y=±0.15 won't interfere since the ball rolls along y=0. The pendulum swinging back after the strike with some energy loss is fine since the ball is gone by then.

I verify the ball's initial rest position has it sitting right at the floor with center z=0.03, so the soft contact penetration should be negligible. For the keyframe, I'm laying out qpos as the pendulum hinge angle followed by the ball's free joint position and orientation, with qvel set to zero across all seven degrees of freedom.

I'm computing the bob's position at the 42° swing angle, giving roughly x=−0.395, z=0.163, which keeps it clear of the floor throughout its swing. Checking friction coefficients, the floor, ball, ramp, and cup geoms all mix to compatible values via MuJoCo's default max-based combination, so nothing unusual there.

Now I'm working out the ramp and rim geometry for the cup segment—using an apothem radius around 0.11-0.115, a rim height of 0.05 with half-height walls at 0.025, and computing the ramp's length, slope angle (~14°), and surface normal to position it correctly between the inner and outer walls.

I'm switching to a cylinder primitive for the bottom plate since ball-cylinder collision is well supported, then working through the octagon's eight segment positions by rotating around the center at radius 0.115, computing each vertex's x/y coordinates at 45° intervals.

I'm defining the body cup at position (1,0,0) with geoms placed at relative offsets matching those octagon vertices, and double-checking the ball rests comfortably within the cup radius. I also want to confirm the ball settles into steady rolling before reaching the ramp, and that the bob's contact stays purely normal so it doesn't impart unwanted lateral push on the ball.

Checking the timing: I need to verify the bob passes near the ball at the bottom of its swing without excessive overlap, and the pendulum's quarter period (~0.36s) lines up reasonably with the ball's roll time across the 0.68m span at 1.4 m/s (~0.5s).

Now I'm settling on physical parameters -- bob mass 1.0, rod mass 0.05, ball mass 0.05, floor size 3x3x0.1 -- and starting to write the MJCF file with a timestep option and a worldbody containing a light.

Still writing XML structure...

Checking whether the pendulum rod could collide with the ball geometry as it swings, but the positions keep them clear since the rod bottom stays above the ball's location even when tilted.

Now I'm verifying the ball's physical properties and checking the ramp geometry's rotation math—confirming the euler angle correctly orients the ramp surface so its normal points upward and the incline direction is correct, matching the intended slope direction.

I'm setting up the cup geometry with angled walls and defining a starting keyframe for the ball's initial position. I'm also double-checking that rolling friction behaves sensibly during contact with the heavy bob and floor, and planning to be upfront that this is an estimated physical setup rather than a fully simulated one.

