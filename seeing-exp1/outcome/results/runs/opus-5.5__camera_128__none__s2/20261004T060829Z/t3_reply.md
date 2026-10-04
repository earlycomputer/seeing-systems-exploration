**What I see:** The ball rises in an arc from its rest spot. It peaks left of the hoop at about rim height plus half a metre. It never reaches the rim opening. Instead the copies come down well in front of the hoop and land on the floor at roughly x ≈ 3 m, short of the hoop at x = 4 m. No copy passes down through the rim. It may have clipped the front rim and dropped back, but at this resolution I can't tell.

**Why my first correction missed:** It aimed for x ≈ 4.0 m using a hand estimate of the drag, and the drag loss was clearly larger than that estimate. The two renders bracket the answer:

- The original launch, with a no-drag rim-height crossing at x ≈ 4.8 m, came in long.
- This launch, with a no-drag crossing at x ≈ 4.5 m, came in short.

So I'm placing the no-drag crossing between them, at about 4.65 m. I'm also raising vz a little so the ball enters more steeply, which leaves more clearance on both sides of the rim.

**New launch:** vz = 9.0 gives about 1.41 s to come back down to 3.05 m. vx = 3.3 then gives a no-drag crossing at x ≈ 4.66 m. If the drag loss is about 0.6 m, as the two renders suggest, the ball comes down near the rim centre. This is an interpolation from two renders, not a simulation, so it needs a third render to confirm.

```json
{"description": "The ball arcs up, peaks left of the hoop a little above rim height, and comes down in front of the hoop, landing on the floor around x of 3 m; it never drops through the rim (it may clip the front rim). The shot is short.", "goes_in": false, "miss": "short", "evidence": "picture"}
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
    <key name="shot" qvel="3.3 0 9.0 0 0 0"/>
  </keyframe>
  <!-- Changed shot qvel from (3.36, 0, 8.75) to (3.3, 0, 9.0). The renders bracket the answer:
       (3.21, 0, 9.3), with a no-drag rim-height crossing at x of about 4.8 m, came in long;
       (3.36, 0, 8.75), with a no-drag crossing at about 4.5 m, came in short, landing near x = 3 m.
       Drag therefore costs more than the ~0.15 m first estimated. The new launch puts the no-drag
       descending crossing of z = 3.05 m at x of about 4.66 m (t of about 1.41 s). With roughly 0.6 m
       of drag loss it comes down near the rim centre at x = 4 m. The extra vz also gives a steeper
       entry, with more clearance on both rims. vy stays 0, so there is no left/right error.
       This is an interpolation from two renders, not a simulation; confirm it in a render. -->
</mujoco>
```

---
thinking (summarized):

I'm tracing the trajectory of the falling copies in the image, and it looks like the arc peaks early and the ball descends well short of the hoop's position around x≈90, falling instead near x≈68-70 down to the floor.

This discrepancy makes me reconsider whether the ball actually struck the rim and bounced, but the descent column sits too far left of the rim pixel location for that to be likely. That pushes me toward thinking the drag force in the MuJoCo model is stronger than I'd estimated—comparing to an earlier shot with vx 3.21 that reached the backboard with a modest drag effect, this new trajectory suggests something is pulling the ball down much harder than before.

Maybe drag is actually stronger than I estimated, but that conflicts with picture 1 showing the arc reaching near the backboard top. I should calibrate properly using the camera position and orientation to project the hoop and trajectory points into pixel space, computing the forward and right vectors from the camera to the look-at point.

With pixel scale 175.8 for the 128x128 image, I'm projecting the hoop point at (4.8,8.5,-1.2) into camera space, getting depth 9.642 and screen coordinates around (88,38), which checks out. Now I'm computing the projection for another point at x=3,z=3.

Projecting (3.8,8.5,-1.25) gives roughly px=71, py=40, and projecting x=3,z=1 gives py≈75. The descending column in the image sits near px 68-70, implying a world x around 2.8-3, which is about a meter short of where the ball should land without drag — suggesting a surprisingly strong drag effect is at play, since there's nothing physical at x=3 to cause this deviation.

Checking the peak location too: projecting x=2,z=3.7 gives px≈53, py≈27, which roughly matches the pixel peak I estimated. But the horizontal distance has shrunk much more than the vertical rise, which is strange — if drag were simply slowing things down uniformly, I'd expect the apex height to drop too, not stay similar while only the horizontal range compresses. This asymmetry makes me wonder if something besides simple drag is at work, though spin seems unlikely here.

I think my reading of the pixel positions might just be imprecise rather than there being a real physical effect — the empirical horizontal range looks like about 73% of my predicted value. If I try to correct for that by scaling up the initial horizontal velocity, I need to account for the fact that drag grows with speed, so a bigger push won't scale range linearly; meanwhile the time of flight seems roughly unchanged.

Trying to fit a drag coefficient that explains the 27% horizontal shortfall leads to a value that would also strongly damp the vertical motion, which should pull the peak height down a lot — but that contradicts the apex height I measured. So either my peak reading is also off, or something else doesn't add up, and I can't fully resolve the inconsistency from the data I have.

Comparing the two shots more carefully, shot 1 with similar vx reached a much higher x than shot 2 did, which doesn't fit a uniform drag model — unless shot 2's trajectory actually bounced off the front rim and is falling back toward the shooter, which would explain why the later frames show the ball descending short of where it should land.

Comparing with drag included, shot 2 likely falls slightly short, hitting the front rim and bouncing back near x≈3.3-3.5, which matches the shorter landing distance. So I should correct by aiming a touch longer and higher — nudging vz up to around 9.0 with a slightly adjusted trajectory to clear the front rim.

That drag loss seems surprisingly large, which suggests my estimated drag coefficient is off by maybe 4x—MuJoCo's ellipsoid drag model uses blunt and slender components that are tricky to pin down for a sphere. I should try refitting with a larger k, around 0.045, and re-simulate shot 2 to see if it lands correctly at the contact point.

Continuing the step, apex comes out near x=2.2, z=3.19, but when I try to finish the fall with this drag coefficient the landing point drifts to around x=4.2, nowhere near the expected 2.9. That mismatch tells me k=0.045 is off and this coarse numerical approach isn't converging to something consistent.

Trying a cleaner alternative, I pick vx=3.5 and vz=9.0 for a fresh trajectory estimate. Without drag, this puts the descending x near 4.65-4.87 at rim height, which would actually strike the backboard rather than pass through cleanly, while a slightly slower shot lands around 4.49 and falls short -- so the real trajectory with drag must sit somewhere between these two bounds, and I'm trying to pin down how much speed loss from drag would reconcile both outcomes with what the picture shows.

