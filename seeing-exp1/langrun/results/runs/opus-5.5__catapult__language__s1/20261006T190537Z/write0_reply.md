The arm starts flat at its lower stop. A spring pulls it up hard, and a stop at 40° halts it there, so the ball flies off at about 44° and 4.6 m/s. It should land near the middle of a 70 cm bucket whose centre is 3 m ahead of where the ball starts. I worked these numbers out by hand and have not run the scene, so the result is unconfirmed.

**Hand calculation**
- **Inertia:** the arm, scoop, ball and armature together come to about 0.075 kg·m² about the pivot.
- **Speed at the stop:** the arm needs 8.05 rad/s, which gives the ball 4.62 m/s at 0.573 m from the pivot.
- **Energy needed:** that speed is 2.43 J of kinetic energy, plus 0.88 J to lift the arm, scoop and ball.
- **Spring:** the spring pulls toward 90°. Supplying 3.30 J between 0° and 40° takes k ≈ 3.87 N·m/rad.
- **Trajectory:** the ball is released at 0.91 m high and 2.83 m short of the bucket centre. Its centre clears the near wall's top about 17 cm past the wall, and it reaches the bucket floor near the centre.

**Where it could go wrong**
- **Narrow tolerance:** a speed error of roughly ±3% would still land the ball in the bucket. Larger errors would miss.
- **Assumptions:**
  - The stop at 40° is reasonably stiff, so the ball leaves at about 40°.
  - The ball starts against the scoop back and stays there while the arm swings.

```world
world  catapult into a bucket

floor
  friction  0.8, spinning 0.005, rolling 0.002

catapult
  is a          catapult
  pivot height  50 cm
  arm length    60 cm
  arm mass      300 g
  swings        from 0° to 40°
  spring        3.87 N·m/rad toward 90°
  damping       0 N·m·s/rad
  armature      0.01 kg·m²
  stands        on floor

ball
  is a      sphere 3 cm radius, 60 g
  rolls
  bounce    dead
  friction  0.8, spinning 0.01, rolling 0.004
  colour    orange
  moves     freely
  sits      on catapult.scoop base, outside catapult.scoop back's far end

bucket
  is an   open box
  length  70 cm
  width   70 cm
  walls   25 cm
  colour  wood
  stands  on floor, its base 3 m beyond ball

expect
  ball comes to rest in bucket
```

---
thinking (summarized):

Since I can't simulate this physically, I need to reason through the catapult's geometry carefully: a stand box supporting a pivot, with an arm hinged at that point extending backward, and a scoop attached to launch the ball toward the bucket 3 meters away.

Working through the hinge rotation math, I find that rotating the arm positively about the y-axis lifts the near end up and swings it toward +x, so at a 45° angle the near end's velocity points equally upward and forward — ideal for a 45° launch angle, meaning I should place the bucket in the +x direction.

Now I'm thinking about the mechanism itself — starting the arm at a cocked angle with a spring pulling it toward release.

For ball placement, I need to decide whether "in catapult" positions the ball relative to the scoop base at rest, and whether that still works correctly if the arm starts turned. To keep things simple and predictable, I think it's safer to start the arm horizontal at 0° with a swing limit, let the spring pull it toward a larger angle, and have it stop at the limit (maybe 45°) where the ball releases.

When the arm hits the stop abruptly, the ball continues with the velocity it had at that instant, which is perpendicular to the arm — so at a 45° stop the launch angle is also roughly 45°, which works out nicely. I'm now checking whether the scoop's back wall would interfere with the ball's motion at release, but since the ball moves in the arm's local normal direction while the scoop back extends along a different local axis, it shouldn't obstruct the launch.

The release should happen right at the mechanical limit, since the spring keeps accelerating the arm until it's forcibly stopped. I'll set the limit angle at 45° with the spring's natural equilibrium well beyond that, maybe toward 90° or more, so the arm is still accelerating hard at the stop — and I should double check that the spring torque at the starting rest position (angle 0) is strong enough to overcome gravity's torque on the arm.

Next I need to work out the actual launch speed and resulting throw distance, starting from the bucket's position roughly 3 meters from the ball's starting point.

I'm figuring out the ball's exact starting position: it sits in the scoop near the arm's near end, with the scoop base centered about 8 cm in from that end, and its height stacked up from the pivot height plus the arm thickness, scoop base thickness, and ball radius.

Rather than trying to precisely simulate the spring-driven dynamics — which gets messy with damping and inertia — I'm thinking about just defining the physical setup (pivot height, arm length, scoop geometry) and computing the launch from energy/torque balance at the release point, since the brief really does require the catapult to physically throw the ball from rest.

Now I'm working through the energy balance: the spring's stored energy as the arm swings from vertical to 45°, accounting for both the spring torque integral and the rise in the arm's center of mass against gravity, to figure out the ball's launch speed and angle.

Using the parallel axis theorem I get the arm's moment of inertia around 0.12 m per unit mass, giving about 0.036 kg·m² for a 0.3 kg arm. Then I'm adding the scoop base and scoop back contributions, each with their own offset distances along and perpendicular to the arm, working out the back piece's position just outside the base's near end at 0.605 m.

Summing all contributions—arm, armature, scoop base, scoop back, and the ball's position plus its small self-rotation term—I get a total moment of inertia around 0.0715 kg·m². Then I'm figuring the ball's release speed from the arm's angular velocity times its radius of about 0.5234 m, noting the velocity direction is slightly offset from the arm's direction due to the ball sitting off-axis in the scoop.

For the launch angle, I'm rotating the ball's position vector by 45° using standard rotation formulas to get its coordinates at release, then computing velocity as angular velocity crossed with position—giving a velocity vector with both forward and vertical components that I'll use to find the actual launch angle.

Computing atan(0.3253/0.4101) gives 38.4°, not the 45° I'd assumed—so I could either accept this angle or adjust the rotation limit to around 50° to push the launch angle closer to 45° if needed. I'll just go with the 45° limit and 38.4° launch angle for simplicity in the simulation.

Now working out the release geometry: with pivot at (x_p, 0.50), the ball leaves from roughly (x_p−0.52, 0.56), and I need the bucket centered about 2.805 m horizontally from release, with the trajectory crossing the ~0.30 m rim height near the bucket's center.

Solving the projectile equation for z0=0.91, target z=0.30 at d=2.75 m, α=38.4°, I get v²≈21.64, so v≈4.65 m/s for the launch speed.

No air resistance to worry about, so angular velocity is just v divided by arm radius, giving ω≈8.89 rad/s. I need to think about whether the ball actually stays at the end of the scoop throughout the swing though — gravity pulls it toward the pivot while centrifugal force pushes it outward, and early in the motion when ω is small, the ball could potentially slide back toward the pivot instead of staying at the tip.

Checking the numbers: with angular acceleration around τ/I, I find ω²r grows faster than gθ as long as α exceeds roughly 9.4 rad/s², which it easily does, so the ball stays pinned against the outer end of the scoop the whole time — good, that confirms my energy calculation is valid. Kinetic energy at release comes out to about 2.824 J, and now I'm working out the gravitational work done as the arm swings up.

Totaling the rises for the arm mass, ball, and the two scoop component masses gives roughly 0.941 J of gravitational work resisting the motion. For damping, I'm leaning toward setting it to zero for predictability, though I'll need to double check whether zero damping is acceptable or if a small nonzero value is required, and I still need to think through what happens when the arm hits its travel limit.

Computing the required spring energy by summing the gravitational and kinetic terms gives 3.765 J, and using the integral of torque from 0 to θL (which simplifies to k times 3π²/32) I solve for k ≈ 4.07 N·m/rad. I still need to confirm whether "spring toward 90°" corresponds to setting the hinge's spring reference angle to 90° in radians within MuJoCo.

There's some uncertainty about whether the soft limit stop causes slight overshoot, shifting the release angle and launch angle a bit later/higher than ideal—likely within acceptable tolerance since the ball releases once the arm starts decelerating near the limit. I also want to check whether the ball stays centered on the scoop throughout the swing or shifts slightly outward.

Estimating the angular acceleration and swing dynamics, I find the radial displacement over the ~0.155s swing comes out around 0.14 m, which exceeds the 5cm gap, suggesting the ball likely reaches the scoop's back wall during the motion.

Maybe I should just position the ball manually from the start rather than relying on `in catapult` placement — placing it explicitly relative to the scoop back's far end, offset by the ball's radius, and resting on the scoop base. I'm uncertain about default behavior for unspecified directions like "across," so I'll need to account for how the catapult's position is defined along that axis.

Let me recompute with ball centre along at 0.57, giving p0 = (-0.57, 0.06), so r² comes out to 0.3285 and r ≈ 0.5731. Then the ball's moment of inertia term works out to about 0.0197, adding to the running total.

At the 45° release point, the velocity components give an exit angle around 39.0°, slightly off the ideal 45°, with speed proportional to ω·0.5731. I'm weighing whether a steeper trajectory into the bucket would be better for catching against walls versus the sensitivity of range to launch speed, and considering bumping the swing limit toward 50° to compensate for the small 6° geometric offset from the pivot-to-ball-centre angle.

Recomputing at 50° release, though, I realize the exit angle actually drops to around 34° rather than increasing — this reveals that the relationship is really angle = 90° − θ, meaning higher swing angles give flatter exit trajectories, the opposite of what I assumed.

Accounting for the perpendicular offset of the ball relative to the arm, the launch angle actually becomes 84° − θ. So for a 45° launch I need θ ≈ 39°, and picking a limit of θ=40° gives a 44° launch angle. I'm now computing the ball's release position at θ=40° using the arm geometry and offset.

The velocity direction comes out at about 44° from horizontal. I'm now working out the release point in world coordinates relative to the pivot x_p, and figuring where the bucket center sits so I can check the horizontal distance the ball must travel — then checking what height the ball is at when it crosses the bucket's near wall versus where it lands at the base.

I'm trying to make sure the ball's center clears the near wall (accounting for wall thickness) while still landing inside before the far wall, which feels tight with a 60cm bucket — so I'm considering enlarging the bucket to 80cm to give more margin.

Let's go with a 70 cm bucket with 2.5 cm walls instead, recomputing the near and far wall positions, and aiming the trajectory so the ball lands around the center of the bucket, erring slightly past center in case it rolls toward the far wall. Now I'm setting up the trajectory equation using the launch angle of 44 degrees and solving for the velocity that makes the ball's height hit zero (ground level) at the target distance.

Solving that equation gives a velocity around 4.6, and I'm using it to check the ball's height at an earlier distance to make sure it clears the near wall with enough margin, which comes out to roughly 2.66 meters.

Checking clearances: the near wall top gives about 17cm of margin and the far wall gives about 32cm, both acceptable. The sensitivity analysis shows the landing range changes roughly 1.2m per m/s of velocity, so a 3% speed tolerance translates to about 6% energy tolerance — tight but workable.

Computing angular velocity (~8.05 rad/s) and kinetic energy (~2.43 J), I'm now considering whether the ball's own spin should add rotational kinetic energy on top of the arm's motion if it's rotating rigidly without slipping.

Accounting for the ball's rotational inertia, that contribution turns out negligible. I'm then computing the gravitational potential energy change for each component — arm COM, ball, and scoop base/back — at the 40° launch angle, summing to about 0.876 J total rise in potential energy. Subtracting this from the required total gives a spring energy target of about 3.302 J, so now I need to work out the spring configuration that delivers this toward the θ0 = 90° reference angle.

Solving the spring work equation gives k ≈ 3.871 N·m/rad. I then double-check the scoop base geometry relative to the arm's near end and pivot, confirming the placement at -0.52 is consistent with the arm extending to -0.60. I'm also noting I'll explicitly set the arm's rotational inertia to 0.01 kg·m² rather than relying on the default.

Recomputing the arm's moment of inertia using the box dimensions (0.6 x 0.06 x 0.04, mass 0.3), I get the centroidal term plus the parallel-axis contribution, totaling 0.03604 kg·m². Now I'm checking whether the support stand might physically collide with the arm, working through the stand's height and alignment under the pivot point.

Confirming the arm clears the stand given the geometry, and double-checking the ball's starting position doesn't intersect anything else. Then I'm deciding how to specify the catapult's placement — whether to anchor it explicitly on the floor or just leave it at the origin, since parts without an explicit position default there anyway.

For positioning the bucket, I'm working out that it should sit 2.43 m along from the ball's start, matching its open-box dimensions (70 cm length/width, 25 cm walls) with its base resting on the floor, and considering whether offsets are measured from the part's own origin or relative to another placed piece.

I'm ordering the scene as floor, then catapult, then ball, then bucket, with the ball resting at half its default thickness above the floor. Given wall height is only 25 cm but the ball could arrive at over 4.6 m/s, I'm setting the ball's bounce to dead to avoid it jumping out.

For the arm, I'm leaving damping at zero and trusting the default joint limit to stop it near 40°, accepting a small overshoot as the soft constraint engages — the ball should separate from the arm right as deceleration starts, so launch angle stays effectively at 40°.

Now I'm checking whether the scoop's back wall could clip the ball mid-flight: since the ball leaves perpendicular to the radius vector (which is offset ~6° from the arm direction), its velocity has a small component directed back toward the pivot rather than straight along the arm-normal, so I need to verify the back wall's geometry doesn't intersect that trajectory.

Working through it, the velocity direction angles toward the pivot slightly, confirming no clipping of the back wall. I also confirm the ball initially rests against the back wall at angle zero, and there's no air resistance to account for, so the ball should simply come to rest in the bucket at the end.

Checking the initial torque balance: spring torque at zero position (3.87 × 1.5708 ≈ 6.08 N·m) comfortably exceeds the combined gravity torques from the arm, ball, and scoop (totaling roughly 1.38 N·m), confirming the spring can lift the arm from rest. I'm now double-checking the hinge sign convention to make sure a positive angle actually lifts the near end rather than driving it downward into the stand.

Working through the y-axis rotation math confirms positive rotation lifts the arm end upward as intended, and at 40° the arm clears the stand height fine. I'm also verifying the ball's placement relative to the scoop's back face to make sure its center lands correctly at -0.57 along the axis.

For the bucket, I'm placing its base 3 meters beyond the ball, giving a center x of 2.43, sitting on the floor — colors can stay optional.

