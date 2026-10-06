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

pendulum
  is a           sphere 4 cm radius, 400 g
  at             5 cm behind ball, 4.2 cm up
  turns on       pendulum hinge, about y, at pivot
  starts turned  22°
  damping        0.015 N·m·s/rad
  bounce         dead
  colour         dark grey

pendulum rod
  is a         rod 1 cm thick, from pivot to pendulum's top
  weighs       30 g
  attached to  pendulum
  colour       grey

cup
  is a      low entry cup
  sits      on floor, 1 m beyond ball

expect
  ball touches pendulum
  ball comes to rest in cup
```

---
thinking (summarized):

**Exploring pendulum design**

I'm thinking we need to design a robust system where a pendulum strikes a ball to roll it into a cup placed at the center, one meter away. However, there are no tools available to test this right now, and I can’t make any claims until I have results. 

I wonder if using an open box with a low wall could work or if I should opt for a custom cup that’s flush with the floor. The ball needs to roll over a small step and must have enough energy to do so.

**Analyzing pendulum collisions**

I’m thinking about the pendulum design with a primitive sphere hinge. So, the ball has a radius of 3 cm, and the pendulum bob has the same radius, resting at a center height of 3.5 cm. The pivot height is 63.5 cm, and the pendulum length is 60 cm. 

I need to ensure that the collision between the bob and the ball happens before they reach equilibrium to maintain good velocity. I’m estimating the release angle, the momentum, and the energy loss during rolling on the floor, which all play crucial roles in this setup!

**Considering collision effects**

I’m thinking about how a lively collision could impact the system. If the collision is strong enough, with a speed over 1 m/s, it seems like the ball might roll into the cup within 2 seconds. However, the cup would then stop because of the friction from the high-friction base and the far wall. 

It's interesting to analyze how these factors interplay—collision strength, speed, and friction—all need careful consideration to get the expected results!

**Evaluating MuJoCo friction settings**

I'm analyzing MuJoCo's friction settings for rolling surfaces and how they affect movement. I’m considering rolling friction values for the floor and the ball to ensure smooth travel. It seems like dead contacts can allow for a bit of rebound, even when designated as "dead." I wonder if specifying different friction values on the cup could help optimize performance. Defining a new cup part with specific entry and friction properties could be key to achieving better results.

**Analyzing cup trap dynamics**

I'm assessing how to design a cup trap for a ball in a MuJoCo simulation. The dimensions of the cup are crucial, and I’m considering a base size of 24 by 20 by 0.2 cm with low height. I'll use an open box feature near the wall to accommodate the ball but need to ensure the cup can handle the dynamics of the incoming ball. The impact details are important, especially regarding how floor friction affects speed. I want to ensure that the design allows for optimal ball travel and stops without unwanted bounces.

**Assessing ball dynamics in a cup**

I'm looking into the dynamics of a ball approaching a cup with a radius of 0.04 and discussing its behavior when near the rim at 0.88 and the far wall at 1.12. I expect the ball to come to rest after hitting the far wall, as the restitution is low there, causing it to stop completely. There might be angular spin affecting its movement post-rebound, especially since there's high friction involved. I’ll consider creating a custom cup base with a high rolling friction to refine this design further.

**Evaluating support structure**

I'm considering if I can omit support entirely since the pivot point represents a fixed joint and rod. It seems I can have the scene unanchored, which allows for a logical hinge in a physical sense. I think if we place a support post at y + 0.15, and the arm doesn’t touch anything visually, it might not be necessary. It’s interesting to explore how support requirements could change in this setup!