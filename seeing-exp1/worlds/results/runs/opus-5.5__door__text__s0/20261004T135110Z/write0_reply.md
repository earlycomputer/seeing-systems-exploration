The door is a 43 kg slab on a vertical hinge. A spring with a negative rest angle (`springref=-0.3`) keeps pushing it toward closed even after it reaches 0. A joint limit at 0 acts as the door stop, and viscous damping takes out the swing energy. So the door swings shut from about 86° open in roughly 1.5 s, hits the stop, and stays pinned shut by about 6 N·m of residual spring torque. The jamb and frame are for visuals only (no collisions), so the stop itself is the hinge limit.

```xml
<mujoco model="self_closing_door">
  <compiler angle="radian"/>
  <option timestep="0.002" gravity="0 0 -9.81"/>

  <worldbody>
    <light name="sun" pos="1 -2 4" dir="-0.2 0.4 -1" directional="true"/>
    <geom name="floor" type="plane" size="5 5 0.1" rgba="0.6 0.6 0.6 1"/>

    <!-- door frame: visual only, the door stop is the hinge joint limit at 0 -->
    <geom name="hinge_post" type="box" pos="-0.06 0 1.05" size="0.04 0.06 1.05" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <geom name="latch_post" type="box" pos="0.96 0 1.05" size="0.04 0.06 1.05" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <geom name="lintel" type="box" pos="0.45 0 2.12" size="0.55 0.06 0.04" contype="0" conaffinity="0" rgba="0.4 0.3 0.2 1"/>
    <geom name="stop_strip" type="box" pos="0.88 -0.035 1.05" size="0.04 0.015 1.0" contype="0" conaffinity="0" rgba="0.3 0.2 0.15 1"/>

    <body name="door" pos="0 0 0">
      <joint name="hinge" type="hinge" pos="0 0 0" axis="0 0 1" limited="true" range="0 1.7" stiffness="20" springref="-0.3" damping="15" armature="0.05" solreflimit="0.01 1" solimplimit="0.95 0.99 0.001"/>
      <geom name="door_panel" type="box" pos="0.45 0 1.01" size="0.45 0.02 1.0" density="600" rgba="0.7 0.5 0.3 1"/>
      <geom name="door_knob" type="sphere" pos="0.82 0.05 1.0" size="0.03" density="600" contype="0" conaffinity="0" rgba="0.8 0.7 0.2 1"/>
    </body>
  </worldbody>

  <keyframe>
    <key name="start" qpos="1.5" qvel="0"/>
  </keyframe>
</mujoco>
```

---
thinking (summarized):

I'm thinking through how to make the door swing shut and stay closed—using a hinge joint with a limited range so it can't swing past the frame, combined with a spring pulling it toward closed and damping to prevent oscillation, essentially letting it rest against a stop at the closed position.

I'm now sketching the door's dimensions and hinge placement—sizing it roughly 0.9m wide by 2m tall, positioning the vertical hinge axis at the edge, setting the joint range so it can swing open to about 86 degrees, and tuning the spring reference point so it naturally pulls toward fully closed.

I'm estimating the door's mass from wood density (around 43 kg) and computing its rotational inertia about the hinge, then picking a spring stiffness and damping that let it swing closed in a few seconds without excessive bouncing against the stop—working through the underdamped oscillation math to check the timing.

I don't think a latch is necessary, and I'll skip adding a real jamb stop since the joint limit already handles it—I'll just add a visual-only frame post for appearance, positioned clear of the door's swing path so it doesn't interfere physically.

Now I'm adding a hinge-side post near the pivot, setting up the floor as a large plane, adding a light source, and defining a keyframe with the door partially open plus a small armature value for stability.

