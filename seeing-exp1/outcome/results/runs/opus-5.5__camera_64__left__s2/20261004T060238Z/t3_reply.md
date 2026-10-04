**What I see.** The trail rises from the ball's spot at the left, arcs over, and comes down toward the hoop. Its last copies sit at about rim height, just left of the hoop: around pixel (39–40, 18–20). By my projection of the camera, the rim centre lands near pixel (44, 19) and the floor directly beneath it near (43, 45). A ball that dropped through would leave a column of copies falling from the rim to that floor spot, ending in the darkest landing copy. I don't see that column. The trail appears to stop in front of the rim, roughly 0.4 m short of its centre in x.

**Caveats.** At 64×64 one pixel is about 0.1 m at the hoop's distance, so this reading is uncertain. The picture also looks much like the first readback, so the resolution may not be separating the cases well. My best reading is that the ball now falls short and strikes the front of the rim. That would mean the air drag is stronger than I estimated.

**Fix.** Raise the forward speed so the ball crosses the rim plane about 0.3 m farther along x, at the rim centre. Keep vy = 0 and vz = 9.3.

```json
{"description": "The ball arcs from its resting spot toward the hoop. The trail ends at about rim height just in front of (left of, in the image) the rim centre, with no column of copies falling below the hoop to the floor. It appears to hit the front of the rim, short by roughly 0.3-0.4 m. The image is low resolution and this reading is uncertain.", "goes_in": false, "miss": "short", "evidence": "picture"}
```

```xml
<mujoco model="basketball_hoop">
  <option timestep="0.002" density="1.2"/>

  <visual>
    <headlight ambient="0.15 0.15 0.15" diffuse="0.3 0.3 0.3" specular="0 0 0"/>
  </visual>

  <worldbody>
    <!-- Lighting: main overhead directional light plus a softer fill spot above the hoop -->
    <light name="overhead_sun" directional="true" pos="2 0 10" dir="0 0 -1" diffuse="0.8 0.8 0.8" specular="0.2 0.2 0.2" castshadow="true"/>
    <light name="overhead_fill" pos="4 0 8" dir="0 0 -1" diffuse="0.3 0.3 0.3" specular="0 0 0" castshadow="false"/>

    <!-- Floor: top surface at z = 0 -->
    <geom name="floor" type="plane" pos="0 0 0" size="10 10 0.1" rgba="0.72 0.52 0.32 1" friction="0.8 0.005 0.0001"/>

    <!-- Regulation size-7 basketball: circumference 0.75 m -> radius 0.1194 m, mass ~0.62 kg (hollow shell inertia 2/3 m r^2) -->
    <body name="ball" pos="0 0 0.1194">
      <freejoint name="ball_free"/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.005893 0.005893 0.005893"/>
      <geom name="ball" type="sphere" size="0.1194" rgba="0.85 0.40 0.10 1" friction="0.9 0.01 0.001" solref="0.01 0.2" fluidshape="ellipsoid" fluidcoef="0.25 0.25 1.5 1.0 1.0"/>
    </body>

    <!-- Hoop: origin at rim center, 4 m along +x, rim at 3.05 m. Fixed to the world (no joint). -->
    <body name="hoop" pos="4 0 3.05">
      <!-- Rim: 16 capsule segments, inner diameter 0.4572 m (18 in), tube radius 0.008 m, tube-center radius 0.2366 m -->
      <geom name="rim_00" type="capsule" size="0.008" fromto="0.2366 0 0 0.2186 0.0905 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_01" type="capsule" size="0.008" fromto="0.2186 0.0905 0 0.1673 0.1673 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_02" type="capsule" size="0.008" fromto="0.1673 0.1673 0 0.0905 0.2186 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_03" type="capsule" size="0.008" fromto="0.0905 0.2186 0 0 0.2366 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_04" type="capsule" size="0.008" fromto="0 0.2366 0 -0.0905 0.2186 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_05" type="capsule" size="0.008" fromto="-0.0905 0.2186 0 -0.1673 0.1673 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_06" type="capsule" size="0.008" fromto="-0.1673 0.1673 0 -0.2186 0.0905 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_07" type="capsule" size="0.008" fromto="-0.2186 0.0905 0 -0.2366 0 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_08" type="capsule" size="0.008" fromto="-0.2366 0 0 -0.2186 -0.0905 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_09" type="capsule" size="0.008" fromto="-0.2186 -0.0905 0 -0.1673 -0.1673 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_10" type="capsule" size="0.008" fromto="-0.1673 -0.1673 0 -0.0905 -0.2186 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_11" type="capsule" size="0.008" fromto="-0.0905 -0.2186 0 0 -0.2366 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_12" type="capsule" size="0.008" fromto="0 -0.2366 0 0.0905 -0.2186 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_13" type="capsule" size="0.008" fromto="0.0905 -0.2186 0 0.1673 -0.1673 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_14" type="capsule" size="0.008" fromto="0.1673 -0.1673 0 0.2186 -0.0905 0" rgba="0.9 0.3 0.05 1"/>
      <geom name="rim_15" type="capsule" size="0.008" fromto="0.2186 -0.0905 0 0.2366 0 0" rgba="0.9 0.3 0.05 1"/>

      <!-- Bracket joining the back of the rim to the backboard face -->
      <geom name="hoop_bracket" type="box" pos="0.3105 0 -0.01" size="0.0705 0.05 0.012" rgba="0.9 0.3 0.05 1"/>

      <!-- Backboard: 1.80 x 1.05 m, 0.03 m thick; front face 0.15 m behind the rim's inner edge (x = 0.381); bottom edge 0.15 m below rim -->
      <geom name="backboard" type="box" pos="0.396 0 0.375" size="0.015 0.9 0.525" rgba="0.92 0.95 0.98 0.85"/>
      <!-- Target square painted on the backboard front (thin, visual only) -->
      <geom name="backboard_square" type="box" pos="0.3805 0 0.145" size="0.0005 0.295 0.225" rgba="0.1 0.1 0.1 1" contype="0" conaffinity="0"/>
    </body>

    <!-- Support: floor plate, vertical pole behind the backboard, and horizontal arm to the backboard's back face (x = 4.411) -->
    <body name="hoop_support" pos="5.2 0 0">
      <geom name="support_base" type="box" pos="0 0 0.025" size="0.4 0.4 0.025" rgba="0.2 0.2 0.25 1"/>
      <geom name="support_pole" type="box" pos="0 0 1.7" size="0.1 0.1 1.7" rgba="0.25 0.25 0.3 1"/>
      <geom name="support_arm" type="box" pos="-0.4445 0 3.3" size="0.3445 0.06 0.06" rgba="0.25 0.25 0.3 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="shot" qvel="3.48 0 9.3 0 0 0"/>
    <!-- Changed qvel from "3.26 0 9.3 0 0 0" to "3.48 0 9.3 0 0 0" (vy stays 0, vz stays 9.3).
         Why: in the readback of the previous version, the ball fell short. Its trail ended at rim height
         in front of the rim, apparently on the front rim, with the ball's centre near x = 3.6-3.7 m.
         It needs to cross the rim plane about 0.3 m farther along x, at the rim centre (x = 4.0).
         The flight takes about 1.35 s to reach the rim, and drag eats a little of any added speed, so
         this needs about 0.22 m/s more forward speed. Keeping vz unchanged keeps the arc's height and
         its steep entry angle.
         Caveat: the readback image is 64x64, so the size of the miss is read only roughly. -->
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm trying to trace the ball's arc in the image to see where it lands relative to the hoop, but it's hard to tell from the trajectory alone whether it actually went through.

I'm trying to pin down exactly where the hoop projects in the camera frame by working through the actual camera transform math—computing the forward, right, and up vectors from the camera position and target, then projecting the hoop's 3D coordinates to figure out where the trail should end up on screen if the shot were on target.

If the shot went in, the trail should continue descending toward the floor near (43,45), but what I actually perceive in the image is the arc ending higher up, around x~40, y~20, just left of the hoop. That makes me wonder if the ball actually missed—hitting the rim short—rather than completing a full trajectory to the floor, since the darkest (most recent) copy should mark the true landing point and it doesn't appear to extend that far down.

The two images look nearly identical at this resolution, so I can't visually confirm whether the ball dropped through versus hit the rim and bounced. Physics suggests it should likely go in, but the picture itself is too ambiguous to be certain, so I'll have to make a judgment call rather than rely purely on the visual trail.

I'm estimating the correction needed to vx — maybe a 0.3-0.4 increase to shift the crossing point forward by the right amount, but wary of overcorrecting. If the contact was at the front rim, I can back-calculate the ball's position at that moment from the frame spacing to pin down the shortfall more precisely.

Landing on a crossing adjustment of roughly 0.23, I settle on nudging vx up to about 3.48.

