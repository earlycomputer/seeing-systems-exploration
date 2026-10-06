```parts
part low entry cup
  base
    is a      box 24 by 24 by 0.2 cm
    on        floor
    friction  0.9, spinning 0.02, rolling 0.006
    bounce    dead
    colour    grey
  near wall
    is a      box 0.5 by 24 by 0.2 cm
    on        floor, centred on base's near end
    bounce    dead
  far wall
    is a      box 0.5 by 24 by 12 cm
    on        floor, centred on base's far end
    bounce    dead
  left wall
    is a      box 24 by 0.5 by 12 cm
    on        floor, centred on base's left side
    bounce    dead
  right wall
    is a      box 24 by 0.5 by 12 cm
    on        floor, centred on base's right side
    bounce    dead
```

```world
world  pendulum rolls a ball into a cup

floor
  size      4 m
  friction  0.6, spinning 0.001, rolling 0.0001

ball
  is a      sphere 4 cm radius, 100 g
  rolls
  moves     freely
  bounce    dead
  friction  0.6, spinning 0.001, rolling 0.0001
  colour    orange
  rests     on floor, 0 m along, 0 m to the left

pivot
  is a      point
  at        5 cm behind ball, 64.2 cm up

pendulum tip
  is a      point
  at        5 cm behind ball, 4.2 cm up

pendulum
  is a           rod 8 cm thick, from pivot to pendulum tip
  weighs         800 g
  turns on       swing, about y, at pivot
  starts turned  22°
  damping        0.015 N·m·s/rad
  bounce         dead
  colour         dark grey

cup
  is a      low entry cup
  sits     on floor, 1 m beyond ball

expect
  ball touches pendulum
  ball comes to rest in cup
```

---
thinking (summarized):

**Analyzing hinge conflicts**

I need to fix the repeated hinge issue. It seems that the compiler is mistakenly turning on duplicates due to the naming conflict with the `pendulum_hinge`. The rod and the joint are likely causing this error. To resolve it, I should use the built-in pendulum library, avoiding the name conflict by using the top-level name "pendulum_pivot." Removing the rod attachment altogether might also help to prevent this automatic conflict, focusing solely on using the known pendulum components.

**Refining pendulum design**

I’m working on a pendulum that has a spherical bob and a hinge at the pivot without a visible rod. It seems that I can simply remove the pendulum rod and rename the hinges to "swing pivot." To create a recognizable pendulum, I should define it as an elongated box at the pivot with specific dimensions and weight. This design allows the pendulum to swing and make contact with the ball at a certain height. I’m ensuring the mechanics work well, even without a visible bob, while still maintaining functionality and physics.

**Correcting pendulum design**

I need to create a simplified version of the pendulum by removing the rod and focusing on the pendulum sphere and hinge. This adjustment should make the design cleaner and more effective. It's important that the corrected world maintains the functionality of the pendulum while streamlining its components. By concentrating on just the sphere and hinge, I can achieve an honest representation of how the pendulum operates without unnecessary complexity.

**Analyzing pendulum mechanics**

I'm considering how the pendulum operates midair without the hinge fully rendered. The setup responds to gravity as it swings down and strikes a ball, but the world should ideally include a rod attachment. I suspect a bug with duplicate names in the compiler related to the pendulum hinge. The solution could involve adjusting the naming or opting for a single joint without rod attachment. I might use a capsule primitive instead. This setup needs to be robust within my token budget.

**Exploring pendulum design**

I'm examining a single pendulum shape with a rod thickness of 8 cm from the pivot to the massless bob. The hinge at the pivot supports an 800g rod, and I’m noting the curvature of the capsule around it. The gravitational center influences the angular acceleration and effective mass. I'm considering whether to simplify to a sphere pendulum, which looks easier and less risky. It might be worth using a library for precise bob size and ensuring everything's centered without excess geometry. Ultimately, I'll remove the rod and rename the hinge while incorporating a primitive pendulum design.