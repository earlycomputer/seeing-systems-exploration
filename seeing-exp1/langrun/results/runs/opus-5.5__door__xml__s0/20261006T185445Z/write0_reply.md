The door hangs on a vertical hinge with a door-closer spring. Its spring reference is set slightly past shut (−0.2 rad), so the closer pulls the door against a hard stop at 0 and keeps pressing it there. The joint limit at 0, together with a physical stop strip on the latch jamb, stops the door from swinging through. The keyframe starts the door open at about 80°. The damping is light enough that the door closes in about a second, hits the stop, and then rests at 0 for the remainder of the 6 s.

```xml
<mujoco model="self_closing_door">
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <visual>
    <headlight ambient="0.4 0.4 0.4" diffuse="0.6 0.6 0.6"/>
  </visual>

  <worldbody>
    <light name="sun" pos="0.5 -2 4" dir="0 0.4 -1" directional="true"/>
    <geom name="floor" type="plane" size="3 3 0.1" rgba="0.8 0.8 0.75 1"/>

    <!-- door frame (static) -->
    <geom name="hinge_jamb" type="box" pos="-0.075 0 1.05" size="0.045 0.07 1.05" rgba="0.45 0.3 0.2 1"/>
    <geom name="latch_jamb" type="box" pos="0.985 0 1.05" size="0.045 0.07 1.05" rgba="0.45 0.3 0.2 1"/>
    <geom name="lintel" type="box" pos="0.455 0 2.15" size="0.575 0.07 0.05" rgba="0.45 0.3 0.2 1"/>
    <geom name="door_stop" type="box" pos="0.87 -0.046 1.0" size="0.07 0.025 0.95" rgba="0.35 0.22 0.15 1"/>

    <!-- the door: shut at hinge = 0, opens toward +y for positive angles -->
    <body name="door" pos="0 0 0">
      <joint name="hinge" type="hinge" axis="0 0 1" pos="0 0 0" range="0 1.65" limited="true" stiffness="20" springref="-0.2" damping="8" solreflimit="0.01 1"/>
      <geom name="door_panel" type="box" pos="0.47 0 1.02" size="0.45 0.02 1.0" density="500" rgba="0.75 0.55 0.35 1"/>
      <geom name="door_knob" type="sphere" pos="0.82 0.05 1.0" size="0.03" density="500" contype="0" conaffinity="0" rgba="0.85 0.75 0.3 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="1.4" qvel="0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I need a hinge door that starts open and swings closed on its own — a spring pulling it toward 0 with damping to prevent slamming bounce, plus a joint limit (like 0 to 1.6 rad) so it doesn't swing past shut and stays there.

Working through the physics: a door panel roughly 0.45 x 0.02 x 1.0 half-sizes gives a mass around 36 kg and rotational inertia near 9.7 kg·m² about the hinge. I'm testing stiffness values like k=20 to get critical damping around c≈27.9, checking how long it takes to settle near 0 from a 1.3 rad starting angle — looks like it takes several seconds to fully close, so I'm considering whether a slightly underdamped response with a hard stop would look more natural and close faster.

With a joint limit at 0, a spring referenced to 0 would just rest lightly against the stop with no real preload, so instead I want to set the spring reference slightly negative (like -0.2 rad) to mimic a real door closer pressing the door shut against the stop, giving a steady torque to hold it closed. I'm now working out how much the joint limit would deflect under that torque given the default solver reference stiffness.

Beyond the hinge limit itself, I also want a physical stop geometry — a jamb post at the latch end of the frame — so the door physically contacts something when it closes at angle zero, rather than relying purely on the joint limit constraint.

I'm laying out the hinge-side and latch-side posts along x to clear the door's rotation sweep, sizing the panel from x=0.02 to 0.92 so the farthest swinging corner stays within bounds, and positioning the latch post and stop strip to avoid overlapping the door's swept arc.

I'm checking that during opening the door's -y face sweeps away from the stop rather than into it, confirming the stop geometry attaches to the post without collision, and setting up a keyframe with qpos near 80 degrees and zero velocity, tuning spring damping so the hinge settles smoothly against its limit.

I could add a soft limit reflection parameter, though friction loss isn't really needed since MJCF can compute inertia automatically from geometry. Now I'll write the full file, naming every body and geom, setting up the floor plane, and adding lighting.

