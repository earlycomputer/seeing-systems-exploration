**What I see.** In the side view the pendulum leaves a fan of copies on the left as it swings down. After the strike the ball leaves only a few widely spaced copies along the floor. They end around x ≈ 0.5–0.6 m, which is where the ramp starts. In the plan view the cup square on the right is empty: no ball copy appears inside it at any time. The ball was set rolling but did not carry enough speed to climb the 5 cm entry ramp, so it never got into the cup.

**What I changed.**
- **Pendulum:** the arm is now 0.35 m with a 2 kg bob, so the strike speed rises from about 2 m/s to about 2.6 m/s.
- **Entry rim:** lowered from 5 cm to 4 cm. The ball now needs about 0.75 m/s to get over, and should arrive with well over that.
- **Other walls:** the far and side walls are now 15 cm tall, so a faster ball still can't escape.

The ramp geometry is recomputed for the new rim height. This fix comes from the picture and the geometry; I have not run it.

```json
{"what_happens": "The pendulum swings down and strikes the ball, which rolls toward the cup but only reaches about x = 0.5-0.6 m near the foot of the entry ramp; it never enters the cup, which stays empty.", "works": false, "problem": "The ball leaves the strike too slowly to climb the 5 cm entry ramp, so it never gets into the cup."}
```

```xml
<mujoco model="pendulum_ball_cup">
  <compiler angle="degree"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="0.5 -1 3" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- visual-only pivot marker -->
    <geom name="pivot_marker" type="cylinder" pos="-0.061 0 0.38" euler="90 0 0" size="0.012 0.03" contype="0" conaffinity="0" rgba="0.3 0.3 0.3 1"/>

    <!-- pendulum: pivot 0.35 m above the bob's lowest point; bob at bottom touches ball at centre height -->
    <body name="pendulum" pos="-0.061 0 0.38">
      <joint name="pendulum_hinge" type="hinge" axis="0 1 0" pos="0 0 0"/>
      <geom name="pendulum_rod" type="capsule" fromto="0 0 0 0 0 -0.325" size="0.008" mass="0.05" rgba="0.4 0.4 0.5 1"/>
      <geom name="pendulum_bob" type="sphere" pos="0 0 -0.35" size="0.025" mass="2.0" rgba="0.8 0.2 0.2 1"/>
    </body>

    <!-- ball resting on the floor at the origin -->
    <body name="ball" pos="0 0 0.03">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.03" mass="0.1" rgba="0.2 0.4 0.9 1"/>
    </body>

    <!-- cup centred 1 m from the ball's start; ramp leads up to a 4 cm entry rim -->
    <body name="cup" pos="1 0 0">
      <geom name="cup_ramp" type="box" pos="-0.31868 0 0.01009" euler="0 -7.595 0" size="0.15133 0.1 0.01" rgba="0.6 0.5 0.3 1"/>
      <geom name="cup_wall_near" type="box" pos="-0.16 0 0.02" size="0.01 0.17 0.02" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_far" type="box" pos="0.16 0 0.075" size="0.01 0.17 0.075" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_left" type="box" pos="0 0.16 0.075" size="0.17 0.01 0.075" rgba="0.9 0.7 0.2 1"/>
      <geom name="cup_wall_right" type="box" pos="0 -0.16 0.075" size="0.17 0.01 0.075" rgba="0.9 0.7 0.2 1"/>
    </body>
  </worldbody>

  <keyframe>
    <!-- pendulum held horizontal (bob at x = -0.411), ball at rest -->
    <key name="start" qpos="1.5708 0 0 0.03 1 0 0 0" qvel="0 0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm examining the side and plan views to pinpoint pixel positions of the pendulum, ball copies, and cup, then converting those pixel locations to actual x-coordinates using the image scale factor.

I'm working out the pixel-to-meter scale to locate the pendulum and ball copies: pivot around pixel 30, bob at rest near pixel 16, and successive ball copies appearing around pixels 52, 63, 72, corresponding to roughly x=0.27, 0.43, 0.56 m, sampled every 0.26 seconds.

Computing the ball's speed from those spaced copies gives about 0.57 m/s, which seems too slow for it to climb the 5 cm ramp — it likely rolled partway up and came back down rather than landing in the cup. I'm trying to figure out why it's moving slower than expected, possibly due to the pendulum bob's clearance or an initial contact issue affecting the ball's launch.

I should try lengthening the pendulum to 0.35 m and increasing the bob mass to boost energy, while lowering the rim height requirement. But I need to check that the resulting launch speed doesn't send the ball flying over the far wall given the ramp angle and launch height.

Checking the far wall collision at 3.5 m/s: with spin-driven rise of about 0.05 m, the ball's top could reach 0.11 m, just under a 0.12 wall, so bumping walls to 0.15 m gives more margin. I'm also second-guessing whether the bob strikes the ball off-center due to hinge or rod inertia effects that could explain the slower-than-expected speeds.

Maybe it's rolling friction or the soft contact absorbing energy — with the 1kg vs 0.1kg mass mismatch and solref timeconst of 0.02s, the force should still transfer close to full velocity, but sliding-to-rolling conversion (5/7 factor) brings 1.98 down to 1.41, and the observed value seems even lower, possibly because the ball partially climbed the ramp. I'll just add more safety margin: lengthening the arm to 0.35 with a 2kg bob and a 0.04 rim, then recompute the pivot position at z=0.38, x=-0.061.

Checking the rod and bob placement against the keyframe: bob swings from x=-0.411 to x=0.29 at horizontal, staying clear of the ramp which starts further out at x=0.53, and clearance from the floor looks fine at the current bob radius. Now working out the rim and ramp slope geometry — rim at x=-0.16 with a thin wall, and ramp rising 0.04 over a run from 0.53 to 0.83, giving a slope length around 0.303 and half-length 0.151.

I'm computing the ramp's incline angle near 7.6°, the normal vector, and the adjusted top-center position accounting for wall thickness, then checking the side wall placements at 0.15 height. I'm also considering whether the pendulum could swing back and strike the ball again after the initial hit, but that seems fine either way.

