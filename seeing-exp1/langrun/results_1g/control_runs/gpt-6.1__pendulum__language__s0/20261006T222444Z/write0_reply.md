```world
world  pendulum rolls a ball into a cup

floor
  size      6 m
  friction  0.6, spinning 0.001, rolling 0.0002

ball
  is a      sphere 3 cm radius, 60 g
  moves     freely
  rolls
  bounce    dead
  friction  0.6, spinning 0.001, rolling 0.0002
  colour    orange
  rests     on floor, 0 m along

pivot
  is a  point
  at    7 cm behind ball, 64.2 cm up

pendulum
  is a           sphere 4 cm radius, 250 g
  60 cm below pivot, 7 cm behind ball
  turns on       pendulum hinge, about y, at pivot
  starts turned  30°
  damping        0.005 N·m·s/rad
  bounce         dead
  friction       0.2, spinning 0.001, rolling 0.0002
  colour         grey

pendulum rod
  is a         rod 8 mm thick, from pivot to pendulum's top
  weighs       30 g
  attached to  pendulum
  colour       grey

cup
  is an            open box
  length           26 cm
  width            20 cm
  walls            10 cm
  wall thickness   1 cm
  base thickness   2 mm
  near wall height  1 cm
  bounce           dead
  friction         0.9, spinning 0.005, rolling 0.006
  colour           wood
  sits             on floor, 1 m beyond ball

approach foot
  is a  point
  at    35 cm behind cup, 1 mm up

approach crest
  is a  point
  at    12 cm behind cup, 11 mm up

cup approach
  is a      plank from approach foot to approach crest, 18 cm wide, 2 mm thick
  bounce    dead
  friction  0.6, spinning 0.001, rolling 0.0002
  colour    wood

expect
  ball touches pendulum
  ball comes to rest in cup
```

---
thinking (summarized):

**Designing a physics tool**

I'm thinking about how to design a physics demonstration tool without available tools. I need a pendulum setup where a ball rolls into a cup. The cup needs to have a specific geometry; it must be accessible and positioned correctly. 

The cup's dimensions and structure, including wall thickness and shape, will affect how the ball behaves. I want to ensure the design allows the ball to roll in effectively. I’m aiming for a balance between functionality and accessibility.

**Analyzing pendulum design**

I’m considering the design of a cup as a base and how its center relates to the pendulum setup. The pendulum mechanics, particularly the pivot point and how the bob moves, are crucial. I need to ensure the dimensions—like the bob's radius and height—are precise for collision.

The placement of the ball and its relation to the pendulum's motion is also important. I’m wondering if the naming conventions in the library work correctly for the pendulum’s mechanics. Overall, clarity in positioning will help ensure a successful interaction.

**Calculating pendulum outcomes**

I'm working on understanding the physics of my pendulum system. The peak velocity formula involves parameters like gravitational acceleration and the length of the pendulum. For a 0.6 m length at 20 degrees, I get a velocity of about 0.843 m/s.

The masses of the bob and ball impact their interactions too, with coefficients of restitution affecting how they handle impacts. I need to ensure the ball doesn't bounce out of the cup after rolling and that the wall and floor interactions are taken into account for stability.

**Calculating cup dimensions**

I'm figuring out the dimensions for a cup near the wall. The wall thickness is .01, and the external start and end measurements are .875 and .885, respectively. The ramp top is at .883, and I need to account for an added z measurement of .01 plus the wall thickness. There's a bit of complexity here, but it's all about ensuring I get the measurements right! I just need to keep track of those specifics.

**Calculating pendulum position**

I need to determine a position that's "7 cm behind the ball," but it's important that the ball is positioned before the pivot. The ball should be resting on the floor at 0 m, while the pivot itself needs to be "7 cm behind the ball" and "64 cm up" from that position. Additionally, I need to place the pendulum at "60 cm below the pivot" and still "7 cm behind the ball" at the hinge pivot.

**Analyzing ball dynamics**

I'm looking at the physics of a ball rolling towards a cup, considering factors like inertia, speed, and friction. The ball's initial speed is around 1.254, and its speed when entering the cup could range from about .73 to 1.0. There's a lot of friction involved, with different coefficients for the ramp and cup affecting the motion. I'm also pondering if a slight ramp height and wall positioning might influence whether the ball rolls into the cup or bounces. My main expectation is that the ball eventually comes to rest inside the cup.