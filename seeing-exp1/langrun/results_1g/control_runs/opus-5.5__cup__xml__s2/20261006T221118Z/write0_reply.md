The ball starts at rest on a 20° board and gravity sets it rolling. It leaves the low end of the board at about 1.3 m/s and drops into an open-topped cup. Rolling resistance on the cup's geoms then brings it to a stop.

```xml
<mujoco model="ball_ramp_cup">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="0 0 3" dir="0 0 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.8 1"/>

    <!-- Ramp: 1 m board tilted 20 deg, low end at x~0.47, z~0.25 -->
    <geom name="ramp_board" type="box" pos="0 0 0.41" euler="0 20 0" size="0.5 0.1 0.01" rgba="0.6 0.4 0.2 1"/>
    <geom name="ramp_post_high" type="box" pos="-0.4 0 0.27" size="0.02 0.05 0.27" rgba="0.4 0.3 0.2 1"/>
    <geom name="ramp_post_low" type="box" pos="0.4 0 0.125" size="0.02 0.05 0.125" rgba="0.4 0.3 0.2 1"/>

    <!-- Cup: open box, inner span x in [0.52, 0.86], y in [-0.17, 0.17], walls up to z=0.11 -->
    <body name="cup" pos="0.69 0 0">
      <geom name="cup_bottom" type="box" pos="0 0 0.005" size="0.18 0.18 0.005" friction="1 0.01 0.005" rgba="0.2 0.4 0.8 1"/>
      <geom name="cup_wall_px" type="box" pos="0.175 0 0.06" size="0.005 0.18 0.05" friction="1 0.01 0.005" rgba="0.2 0.4 0.8 0.6"/>
      <geom name="cup_wall_nx" type="box" pos="-0.175 0 0.06" size="0.005 0.18 0.05" friction="1 0.01 0.005" rgba="0.2 0.4 0.8 0.6"/>
      <geom name="cup_wall_py" type="box" pos="0 0.175 0.06" size="0.17 0.005 0.05" friction="1 0.01 0.005" rgba="0.2 0.4 0.8 0.6"/>
      <geom name="cup_wall_ny" type="box" pos="0 -0.175 0.06" size="0.17 0.005 0.05" friction="1 0.01 0.005" rgba="0.2 0.4 0.8 0.6"/>
    </body>

    <!-- Ball: starts resting on the ramp, 0.35 m up-slope from the low edge -->
    <body name="ball" pos="0.1547 0 0.397">
      <freejoint/>
      <geom name="ball" type="sphere" size="0.03" condim="6" friction="1 0.005 0.0001" rgba="0.9 0.1 0.1 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0.1547 0 0.397 1 0 0 0" qvel="0 0 0 0 0 0"/>
  </keyframe>
</mujoco>
```

I haven't run this, so the numbers come from hand calculations rather than a simulation:

- **Rolling down:** the ball should leave the board at about 1.3 m/s.
- **Landing:** it should land near x ≈ 0.70, inside the cup, whose inner floor spans 0.52 to 0.86.
- **Stopping:** after landing it rolls at roughly 0.9 m/s. The cup's rolling friction slows it at about 1.2 m/s², so it should stop within about a second, after a bounce off the far wall or two.

That would leave it well under 5 cm/s by 6 s. These are estimates; MuJoCo's soft contacts could change the bounce and the rolling-friction effect somewhat.

---
thinking (summarized):

I'm thinking through how to design the scene with a tilted ramp, a ball rolling down, and a cup positioned to catch it, making sure the ball comes to rest by the 6-second mark—considering whether the cup needs a recessed base or low walls for the ball to settle into.

To damp the ball's motion once it lands in the cup, I'm weighing options like adding rolling friction via the contact's condim and friction parameters, since a freejoint doesn't support damping directly.

Now I'm working through the actual geometry: ball radius, mass, ramp dimensions, and tilt angle so the ball rolls off the lower end into the cup at the right height and speed, computing the rotation needed to orient the ramp correctly.

Setting zc=0.41 to get the surface positioned near z=0.25 at the lower edge, giving coordinates for both ends of the ramp's top surface. I'm placing the ball's starting position partway along the ramp near the top and computing its coordinates to figure out the travel distance to the lower edge.

Computing the rolling acceleration along the ramp gives v≈2.08 m/s at the edge, which seems too fast for the projectile motion I want, so I should reduce the angle or starting distance to get something closer to 1.2 m/s. I'm considering just letting the ball drop off the edge normally, with velocity components resolved along and perpendicular to the ramp direction at the point of departure.

Now I'm working out the ball's exit position once it rolls off the edge, accounting for the radius offset, and starting to design the cup geometry—rim height, wall thickness, and how far the ball needs to fall before clearing the rim and landing inside.

Recomputing the wall-clearance timing gives t=0.136s, landing x=0.636, so the near wall's inner face needs to sit below about 0.606 at that moment. I'm reconsidering the cup placement so the near wall's outer face is closer to the ramp's end, checking the ramp's lower edge height to make sure it clears the wall top at 0.1.

I'm sizing the cup opening (inner x 0.52 to 0.86, center 0.69) so the ball lands near the center, then estimating how the rolling friction converts sliding speed into rolling speed before the ball bounces off the far wall about 0.14m away.

I'm checking the wall height against the ball's resting center so the collision contact stays well below the rim, and estimating rolling deceleration (~0.5 m/s²) to see the ball would travel about 0.64m before stopping, meaning it'll bounce between walls multiple times within the 6s simulation. I should probably increase rolling friction to settle it faster.

On the ramp though, rolling friction would also cut into the gravity component driving it downhill — comparing the friction-equivalent force to g·sinθ shows it's still enough to roll but meaningfully resists it. Since MuJoCo combines friction by taking the max between contacting geoms, a safer approach might be to set high rolling friction only on the cup geoms while keeping the ball and ramp at default values.

Torsional friction at 0.01 is fine too, and sliding friction combines as max(1,1)=1. Checking the ball's trajectory off the ramp edge, it stays well above the near wall's top height as it crosses, so no collision there — and the ramp box's bottom corner clears the wall geometry fine.

Testing velocity sensitivity at the edge: slower speeds (~0.9 m/s) land around x≈0.64, faster speeds (~1.4 m/s) land around x≈0.72, both comfortably inside the cup's inner opening starting at 0.55. The edge transition just slightly rotates the ball without much downward launch change, which is fine. In y, the ball stays centered at 0, well within both the ramp's width and the cup's inner walls at ±0.17.

Now I'm working out the ball's initial placement distance along the ramp from the edge.

I'm computing the ball's starting center coordinates using the contact point geometry, accounting for the combined radius and thickness offset, then nudging z slightly to avoid penetration. Gravity alone sets it rolling, which satisfies the "self-starting" requirement — I'm considering whether to lengthen the ramp travel distance for a more visible roll.

Working through the physics: exit velocity off the ramp, landing position after the projectile arc, and what happens on impact — MuJoCo's soft contact should absorb most of the bounce given default solver parameters, then friction transitions it from sliding to rolling before it decelerates to a stop within roughly a second.

Now I'm laying out the cup geometry — positioning the base box and computing wall placements from the inner cavity dimensions, setting each wall's center and half-thickness so the four sides enclose the 0.18m square interior with walls rising from 0.01 to 0.11 in height.

I'm also positioning the ramp board with its tilt angle and figuring out support posts underneath, computing where the ramp's bottom surface meets the ground at the high end using the rotation geometry.

I'm calculating post heights and positions at both ends to physically prop up the tilted ramp, then adding a light, floor plane, and a keyframe defining the ball's starting position and orientation with zero velocity.

