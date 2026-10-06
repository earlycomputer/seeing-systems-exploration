The ball leaves the floor at about 9.4 m/s, 72° above horizontal. It peaks near 4.2 m and drops through a 0.457 m rim, centered at 3.05 m height and 4 m away, about 1.4 s after launch. It enters at roughly 59° below horizontal, with about 6 cm of clearance from the rim on each side along its path. The bounce is damped and the floor has rolling friction, so the ball should settle well before the 6 s run ends. I worked this out by hand and haven't run the file in MuJoCo, so the clearance and the final resting speed still need confirming in a simulation.

```xml
<mujoco model="basketball_shot">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="2 -3 8" dir="0 0.3 -1" directional="true"/>
    <geom name="floor" type="plane" size="20 20 0.1" rgba="0.75 0.6 0.4 1" friction="0.8 0.005 0.03" solref="0.01 0.25"/>

    <body name="ball" pos="0 0 0.121">
      <freejoint name="ball_free"/>
      <geom name="ball" type="sphere" size="0.12" mass="0.62" rgba="0.9 0.45 0.1 1" condim="6" friction="0.8 0.005 0.03" solref="0.01 0.25"/>
    </body>

    <body name="hoop" pos="4 0 3.05">
      <geom name="rim00" type="capsule" size="0.01" fromto="0.2286 0 0 0.2112 0.0875 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim01" type="capsule" size="0.01" fromto="0.2112 0.0875 0 0.1616 0.1616 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim02" type="capsule" size="0.01" fromto="0.1616 0.1616 0 0.0875 0.2112 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim03" type="capsule" size="0.01" fromto="0.0875 0.2112 0 0 0.2286 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim04" type="capsule" size="0.01" fromto="0 0.2286 0 -0.0875 0.2112 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim05" type="capsule" size="0.01" fromto="-0.0875 0.2112 0 -0.1616 0.1616 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim06" type="capsule" size="0.01" fromto="-0.1616 0.1616 0 -0.2112 0.0875 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim07" type="capsule" size="0.01" fromto="-0.2112 0.0875 0 -0.2286 0 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim08" type="capsule" size="0.01" fromto="-0.2286 0 0 -0.2112 -0.0875 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim09" type="capsule" size="0.01" fromto="-0.2112 -0.0875 0 -0.1616 -0.1616 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim10" type="capsule" size="0.01" fromto="-0.1616 -0.1616 0 -0.0875 -0.2112 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim11" type="capsule" size="0.01" fromto="-0.0875 -0.2112 0 0 -0.2286 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim12" type="capsule" size="0.01" fromto="0 -0.2286 0 0.0875 -0.2112 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim13" type="capsule" size="0.01" fromto="0.0875 -0.2112 0 0.1616 -0.1616 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim14" type="capsule" size="0.01" fromto="0.1616 -0.1616 0 0.2112 -0.0875 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim15" type="capsule" size="0.01" fromto="0.2112 -0.0875 0 0.2286 0 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="neck" type="box" size="0.07 0.04 0.01" pos="0.31 0 0" rgba="0.9 0.2 0.05 1"/>
    </body>

    <body name="support" pos="0 0 0">
      <geom name="backboard" type="box" size="0.015 0.915 0.525" pos="4.395 0 3.425" rgba="0.95 0.95 0.95 0.6"/>
      <geom name="arm" type="capsule" size="0.04" fromto="4.42 0 3.6 5.0 1.5 3.6" rgba="0.3 0.3 0.35 1"/>
      <geom name="pole" type="cylinder" size="0.08" fromto="5.0 1.5 0 5.0 1.5 3.6" rgba="0.3 0.3 0.35 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 0 0.121 1 0 0 0" qvel="2.865 0 8.947 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out the physical setup for a basketball shot: ball radius and mass, rim height at 3.05m, horizontal distance of 4m, and the rim's inner diameter so the ball can pass cleanly through while dropping downward.

Calculating a trajectory with an apex around 4.2m, I derive the launch velocity components and time of flight, finding the ball enters the rim at a steep angle (~59° from horizontal) with a descending vertical velocity—good for a clean swish. Then I'm checking whether the ball's radius leaves enough clearance against the rim's inner radius and tube thickness at that entry angle, accounting for how the effective opening shrinks as the ball crosses it at a slant.

I'll build the rim as a ring of small capsule segments rather than a torus primitive, checking that the chord approximation stays within tolerance for ball clearance. I'm also planning a static hoop body attached to the world with a backboard positioned slightly behind the rim.

Checking the ball's trajectory after it passes through the rim, it clears the backboard's bottom edge with room to spare, so I'll place the support pole further back at x=5.2 to avoid any collision with the ball's path.

Computing the landing point: solving the vertical drop equation gives t≈0.428s, landing at x≈5.226, which is uncomfortably close to a pole at 5.2. I should reconsider placement to avoid interference, or simplify by omitting the backboard/pole structure entirely.

For getting the ball to rest within the time limit, I need damped bounces plus rolling friction. Estimating with a coefficient of restitution around 0.75-0.8 and an impact velocity of about 8.95 m/s, the total bounce decay time comes out to roughly 5.47 seconds, which is cutting it close to the 6s window once I add rolling time after the bounces settle.

I'm lowering the restitution closer to 0.5 to shrink the bounce decay to about 1.82 seconds, then working out the horizontal rolling transition—accounting for the ball's hollow-shell moment of inertia, the post-friction rolling speed comes to around 1.72 m/s, after which I need enough rolling friction to bring it to a stop within the remaining few seconds.

No need to worry about shellinertia; solid default works fine, and with it I get a reasonable μ_r≈0.03 giving distance around 1.19 m over roughly 1.16 s, which seems fine. I also need to check whether skidding during bounces settles into rolling naturally and whether the ball starts in contact with the floor at its initial height.

Using regulation size-7 ball dimensions, r=0.12 m and mass 0.62 kg, starting at z=0.12 gives enough clearance from the rim (0.134 needed vs 0.1957 available), so that's fine. Air drag is off by default since density is zero. For restitution, I'm working out the damping ratio needed in MuJoCo's solref to achieve a coefficient of restitution around e≈0.5, solving the exponential relation between e and ζ.

Checking timing: with timeconst 0.01 and timestep 0.002, that satisfies the ≥2*timestep constraint, so it should work. I'm roughly estimating bounce duration — around 2.74s for the bouncing phase ending near 4.56s, then about a second of rolling — which feels workable though a bit tight, so I'm considering raising ζ to around 0.3 for a cleaner bounce behavior.

Trying ζ=0.3 gives e≈0.37 and bounce duration near 1.07s, settling around 2.9s, which seems reasonable even if less bouncy than a real basketball. ζ=0.25 gives e≈0.44 with bounce duration around 1.46s — I'll go with 0.25 since the geometric decay combined with contact softness naturally settles the motion anyway.

For rolling behavior, I'm accounting for horizontal speed changes from sliding friction during impacts, settling to roughly 2 m/s rolling speed, with rolling friction around 0.03 bringing it to rest in about 1.2s, plus torsional friction of 0.005 and condim=6 on the ball geom for full contact dimensionality.

I'm setting floor friction values and placing them on the ball, checking that rolling friction won't interfere with the flight phase. Estimating the ball's final resting position by adding up the initial distance, bounce travel (~3.3m over 1.46s), and rolling distance (~1.2m), landing around x≈9.7 — since the floor plane is infinite for collision purposes, I just need to position the support pole and backboard off to the side so they don't interfere, placing the backboard at x=4.38 spanning the appropriate height range.

I'm confirming the ball clears the backboard bottom with about 0.2m margin, then positioning the support pole off-axis at x=5.0, y=1.5 with a horizontal arm connecting to the backboard, since the ball rolls straight along y=0 with no lateral deviation given its symmetric initial conditions.

Still placing arm and pole geometry...

I'm structuring the hoop as its own body with rim and neck geoms, and a separate support body for the backboard and pole, positioning everything relative to the hoop's origin. Now I'm computing the 16 rim capsule segment coordinates around the circle using the rim radius and tube thickness, working through the angles in 22.5° increments...

Still computing rim angles...

Now I'm verifying the ball's initial velocity components so the trajectory reaches the right apex height and timing.

I'm setting up the keyframe with the ball's position and velocity vectors in the freejoint. I'm also noting a small concern about the ball starting exactly at floor contact distance zero, which might cause an instant spurious launch—bumping the initial height slightly would avoid that, though the effect is negligible either way.

Checking the solref defaults and mass/inertia settings for the ball look fine without extra shell inertia terms, and the rolling friction with condim 6 should let it settle to rest reasonably despite soft-constraint creep. Moving on to lighting and visuals before writing out the file.

