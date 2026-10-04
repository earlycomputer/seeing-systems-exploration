The ball starts just above the floor at x = 0. Its keyframe velocity is (3.193, 0, 8.495) m/s, a launch at about 69° and 9.1 m/s. That puts the apex at about 3.8 m. The ball reaches the rim centre (4, 0, 3.05) after about 1.25 s, falling at roughly 50° below horizontal.

At 50° the 0.457 m rim opening looks about 0.35 m wide to the ball. The ball is 0.239 m across, so it should clear the rim by about 5 cm on each side. The 8.495 m/s vertical speed is about 1 cm/s above the ideal-parabola value. That is meant to offset the ~1 cm low drift from MuJoCo's semi-implicit Euler stepping.

These clearance numbers are hand calculations. I have not run the scene, so whether the ball actually passes through the rim is unconfirmed until you simulate it.

```xml
<mujoco model="basketball_shot">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <global offwidth="1280" offheight="720"/>
  </visual>

  <worldbody>
    <light name="sun" pos="2 -3 8" dir="0 0.3 -1" directional="true"/>
    <camera name="side" pos="2.5 -8 2.2" xyaxes="1 0 0 0 0.25 1"/>

    <geom name="floor" type="plane" size="12 12 0.1" rgba="0.75 0.6 0.4 1" solref="0.01 0.3"/>

    <!-- Basketball: size 7, radius 0.1193 m, mass 0.62 kg, thin-shell inertia (2/3 m r^2) -->
    <body name="ball" pos="0 0 0.12">
      <freejoint name="ball_free"/>
      <inertial pos="0 0 0" mass="0.62" diaginertia="0.005883 0.005883 0.005883"/>
      <geom name="ball" type="sphere" size="0.1193" rgba="0.9 0.45 0.1 1" friction="0.8 0.005 0.0001" solref="0.01 0.3"/>
    </body>

    <!-- Hoop: origin at rim center, 3.05 m high, 4 m from launch point. Inner diameter 0.4572 m, tube radius 0.008 m -->
    <body name="hoop" pos="4 0 3.05">
      <geom name="rim_00" type="capsule" size="0.008" fromto="0.2366 0 0 0.21859 0.09054 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim_01" type="capsule" size="0.008" fromto="0.21859 0.09054 0 0.16730 0.16730 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim_02" type="capsule" size="0.008" fromto="0.16730 0.16730 0 0.09054 0.21859 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim_03" type="capsule" size="0.008" fromto="0.09054 0.21859 0 0 0.2366 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim_04" type="capsule" size="0.008" fromto="0 0.2366 0 -0.09054 0.21859 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim_05" type="capsule" size="0.008" fromto="-0.09054 0.21859 0 -0.16730 0.16730 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim_06" type="capsule" size="0.008" fromto="-0.16730 0.16730 0 -0.21859 0.09054 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim_07" type="capsule" size="0.008" fromto="-0.21859 0.09054 0 -0.2366 0 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim_08" type="capsule" size="0.008" fromto="-0.2366 0 0 -0.21859 -0.09054 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim_09" type="capsule" size="0.008" fromto="-0.21859 -0.09054 0 -0.16730 -0.16730 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim_10" type="capsule" size="0.008" fromto="-0.16730 -0.16730 0 -0.09054 -0.21859 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim_11" type="capsule" size="0.008" fromto="-0.09054 -0.21859 0 0 -0.2366 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim_12" type="capsule" size="0.008" fromto="0 -0.2366 0 0.09054 -0.21859 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim_13" type="capsule" size="0.008" fromto="0.09054 -0.21859 0 0.16730 -0.16730 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim_14" type="capsule" size="0.008" fromto="0.16730 -0.16730 0 0.21859 -0.09054 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="rim_15" type="capsule" size="0.008" fromto="0.21859 -0.09054 0 0.2366 0 0" rgba="0.9 0.2 0.05 1"/>
      <geom name="bracket" type="box" size="0.07 0.04 0.01" pos="0.311 0 -0.01" rgba="0.9 0.2 0.05 1"/>
    </body>

    <!-- Backboard: face 0.381 m behind rim center (15 in), bottom edge ~6 in below rim -->
    <body name="backboard" pos="4.406 0 3.432">
      <geom name="board" type="box" size="0.025 0.915 0.5335" rgba="0.95 0.95 0.97 0.6"/>
    </body>

    <!-- Support stanchion well behind the basket -->
    <body name="support" pos="0 0 0">
      <geom name="arm" type="box" size="1.25 0.06 0.06" pos="5.68 0 3.40" rgba="0.3 0.3 0.35 1"/>
      <geom name="pole" type="cylinder" size="0.1 1.75" pos="7.0 0 1.75" rgba="0.3 0.3 0.35 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="0 0 0.12 1 0 0 0" qvel="3.193 0 8.495 0 0 0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm working out the physical specs needed—regulation basketball size, mass, and rim dimensions—to set up a projectile launched from the floor that must arc through the hoop at 3.05 m height and 4 m horizontal distance.

For the rim, I'm modeling it as a ring of small capsules approximating a torus, then calculating the minimum descent angle (around 31°) needed for the ball to clear the rim opening given its diameter, so I'm targeting a steeper ~50° entry angle for a safe margin. I'm now solving the kinematic equations for vertical and horizontal launch velocity components that satisfy both the horizontal travel distance and the required descending entry angle at the hoop.

Working through the numbers, I get T≈1.25s, vx≈3.19 m/s, vz0≈8.49 m/s, giving a launch speed around 9.06 m/s at roughly 69° — this seems like a reasonable, physically plausible shot arc. I'm also considering whether a backboard is needed, but since the trajectory passes cleanly through the hoop center it likely won't interact with one anyway.

Checking the rim geometry more carefully, the rim's inner edge sits 6 inches from the backboard, putting the rim center about 0.381 m out. I need to verify the ball's path through the rim's depth properly — since it's moving forward in x while descending, I have to confirm it doesn't clip the far side of the rim as it passes through the circular opening at x=4.

Working out the clearance condition: the perpendicular distance from the trajectory line to the rim's front and back points needs to exceed the ball radius plus tube radius (0.1273 m). With the entry angle at 50° below horizontal, I compute the trajectory direction vector and check the perpendicular distance to the front rim point first.

The numerical integration error from the timestep is small enough to ignore, and I'll skip air drag since MuJoCo defaults to none. I should start the ball slightly above the floor (z=0.12 instead of touching) to avoid any initial contact impulse messing with the launch velocity, adjusting the height difference slightly to account for that offset.

I'm deciding to skip adding a net since the geoms would likely interfere with the ball's physics, but I'm considering whether to add a backboard and pole for visual realism, checking the standard dimensions (42-inch board, rim 6 inches above the board's bottom edge) to position it correctly relative to the rim at 10 feet.

Working through the trajectory, I calculate that after passing the rim the ball clears the backboard's bottom edge with room to spare, so placing a pole further back around x=5.2 should avoid collisions. I'm solving the quadratic for when the ball reaches the floor, finding it lands around t≈0.477s after the rim crossing.

Checking the arm position against the ball's trajectory confirms the ball stays well below the support arm height when near the pole, so no collision issue there. For the bounce physics, I'll just keep the default contact solver settings rather than overengineering the restitution parameters.

For the ball's inertia, I'm computing the hollow-sphere moment of inertia explicitly (2/3 m r²) and specifying it directly via an inertial element rather than relying on the geom's automatic solid-sphere inertia calculation, since that gives a more physically accurate basketball.

Now I'm working out the hoop rim geometry, placing the hoop body and computing the 16 segment endpoints around the rim circle using trigonometry at 22.5° increments, scaled by the rim radius, to build capsule segments approximating a torus.

I'm checking the clearance distance against the rim radius and confirming it's sufficient. I also need to add a bracket body connecting the rim to the backboard, and treat the hoop as a static body with the backboard as a separate attached element.

Now I'm positioning the backboard relative to the rim, computing its center height and half-dimensions, then adding the support arm and pole geometry. I'm also estimating the ball's landing point and timing after it bounces off the rim, accounting for restitution and friction effects on its velocity.

I'm working out the keyframe values for the free joint's position and velocity, verifying the trajectory equations give consistent height, horizontal distance, and landing angle at the target time using projectile motion with gravity.

I also account for MuJoCo's semi-implicit Euler integration, which shifts the actual z slightly lower than the analytic prediction—roughly 1.2cm at the crossing point—so I nudge the initial vertical velocity up slightly to 8.495 to compensate and preserve the clearance margin.

Now I'm fleshing out the model details: setting up the floor as a 10x10 plane, adding a light, making the ball orange, and configuring contact parameters. I'm considering solref values for the ball geom to give it a realistic bounce, since MuJoCo averages solref/solmix between contacting geoms, so I want to pick ball-side values that combine with the floor's defaults to produce believable basketball-like bounciness.

