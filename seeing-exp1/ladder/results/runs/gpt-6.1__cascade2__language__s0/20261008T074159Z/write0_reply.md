The language has no numeric gravity or restitution setting: this requires the compiler’s gravity to be 9.81 m/s², and uses `dead` contacts rather than claiming exact restitution 0.05. No hinge or slide joints are used, and every moving body starts from rest.

```world
world  ramp ball and two dominoes

floor
  size      6 m
  friction  0.70, spinning 0, rolling 0

-- Endpoints describe the deck centreline.
-- With a 2 cm deck, its low upper edge is 0.15 m above the floor.
ramp high
  is a  point
  at    0 m along, 0 m to the left, 0.482623217 m up

ramp low
  is a  point
  at    0.939692621 m along, 0 m to the left, 0.140603074 m up

ramp1
  is a      plank from ramp high to ramp low, 0.30 m wide, 0.02 m thick
  friction  0.70, spinning 0, rolling 0
  bounce    dead
  colour    wood

ball1
  is a      sphere 0.10 m across, 0.20 kg
  rolls
  friction  0.70, spinning 0, rolling 0
  bounce    dead
  moves     freely
  rests     on ramp1, 0 m from the top
  colour    orange

-- The first domino's near face is 0.10 m beyond the ramp's low upper edge.
domino1
  is a      box 0.08 by 0.04 by 0.24 m, 0.25 kg
  friction  0.70, spinning 0, rolling 0
  bounce    dead
  moves     freely
  stands    on floor, 1.083112822 m along, 0 m to the left
  colour    white

domino2
  is a      box 0.08 by 0.04 by 0.24 m, 0.25 kg
  friction  0.70, spinning 0, rolling 0
  bounce    dead
  moves     freely
  stands    on floor, 0.18 m beyond domino1, 0 m to the left
  colour    white

expect
  ball1 touches ramp1
  ball1 touches domino1
  domino1 touches domino2
```

---
thinking (summarized):

**Evaluating ramp engineering**

I need to avoid complicating the comments about the original plank coordinates for ramp1. The library ramp creates a leg at the top that could collide with a ball if the starting distance is too high. There are concerns about the leg post being positioned 6cm from the floor, as it might penetrate the deck. I need to correct the dimensions, specifically the ramp surface and center ball contact with the leg edge. I’ll have to ensure everything aligns properly in terms of calculations.

**Analyzing Domino Mechanics**

I'm evaluating the physical configuration for travel; the exit gap needs to be defined at .10 near the edge. I'm checking if the top portion of the ball hits correctly at .19 to knock over the domino, which weighs .25kg with a thickness of .08 and reaches a velocity of 1.8. I need to ensure I account for the rotation and angles correctly. I also want to set default rolling resistance to zero to prevent energy loss, but there are challenges with damping and restitution calculations—I can’t set those numerically with defaults.

**Selecting Ramp Specifications**

I'm thinking we should go with a simple, primitive design for ramp1, ensuring that the start and end have the required center offset. The user has fixed the ramp's length at 1, with a width of .3 and an angle of 20 degrees. I need to confirm the endpoint coordinates at .939692621 and calculate the z delta of .342020143 to determine the length. The thickness is set at .02, but including it is optional.