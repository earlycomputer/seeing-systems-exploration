```world
world  three balls roll into a cup

floor
  size      4 m
  friction  0.8, spinning 0.001, rolling 0.0001

ball1
  is a      sphere 4 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.001, rolling 0.0001
  moves     freely
  sits      on floor, 0 m along, 0 m to the left
  launched  1.8 m/s along
  spins     45 rad/s about y
  colour    orange

ball2
  is a      sphere 4 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.001, rolling 0.0001
  moves     freely
  sits      on floor, 30 cm beyond ball1, 0 m to the left
  colour    white

ball3
  is a      sphere 4 cm radius, 150 g
  rolls
  bounce    lively
  friction  0.8, spinning 0.001, rolling 0.0001
  moves     freely
  sits      on floor, 30 cm beyond ball2, 0 m to the left
  colour    orange

-- A low entrance lip lets the third ball roll into the cup.
cup
  is an             open box
  length            36 cm
  width             24 cm
  walls             12 cm
  wall thickness    1 cm
  base thickness    2 mm
  near wall height  2 mm
  friction          0.9, spinning 0.01, rolling 0.004
  bounce            dead
  sits              on floor, 40 cm beyond ball3, 0 m to the left
  colour            grey

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

---
thinking (summarized):

**Designing a reliable capture cup**

I need to create a physically reliable capture cup, considering no tools are available. I want to reason about the energy involved in rolling and collisions. Maybe I'll design a custom cup as an open box with a side entry ramp, positioned close to the wall at a low height. I'm thinking of placing three balls in a row with specific mass and spacing to ensure they engage properly. Let’s ensure the design allows for smooth ball entry and containment.

**Designing a custom capture cup**

I'm thinking about building a custom cup with a low entry as an open box, instead of using a traditional cup shape. It seems like it should be upright with potentially a horizontal orientation. I can design the walls to be 12cm high, but with a low entry of 1cm. I want to ensure the design captures a bouncing ball effectively, so I need to add a ramp and think carefully about the base measurements to make it reliable for capturing.

**Designing a broad catch cup**

I'm considering how a broad catch cup could work with a ramp that helps dissipate energy against a dead wall. With a high floor friction and lively interactions, I need to think about how the bounce might function. I want to specify certain dimensions for the "catch cup," ensuring it has a 1cm entrance slope to help with ball entry. Overall, I’ll design an open box cup with specific dimensions and high friction to improve its effectiveness.

**Evaluating rolling friction**

I'm looking into the rolling friction coefficient for a surface, which is surprisingly low at `0.002`. This results in a constant deceleration of about `0.35 m/s²` for a radius of `0.04`. If the floor friction is `0.8`, it can create a deceleration of `0.035 m/s²`. When considering the ball and cup dynamics, the cup has a rolling coefficient causing a stoppage distance of about `0.04`, ensuring it doesn't exit or hit the far wall. I need to combine these friction coefficients to finalize calculations.

**Refining ramp design**

I’m working on a ramp design to ensure effective ball entry into the cup. The ramp should eliminate any lip while maintaining a height of 1 cm at the entrance. I need to find a way to make the ramp connect well to the cup base, ensuring that it’s centered and positioned accurately. It might be easier to use absolute positions for clarity, and I’ll consider the thickness of materials involved too. Let's keep this simple and functional!

**Designing a cup with ramp**

I'm considering a cup with a low entrance and shallow lip—no ramp needed if the ball rolls at least 0.2 m/s. The cup could be an open box design with one lowered side, making it adaptable. I could create a ramp that launches the ball into the cup or incorporate a bridge over the wall. The idea is to allow balls to roll in easily, with a speed of up to 2 m/s. It sounds like a fun challenge!

**Exploring cup design options**

I’m considering a cup design with a shallow depth of 3 cm and walls 3 cm high, which may work better with a ball radius of 4 cm. However, achieving higher speeds, like 3 m/s, would require careful management of ground friction losses. A custom ramp could help retain the ball, but I’m also thinking about an alternative. What if I designed a hollow, horizontal cup resembling a tipped cup? It could add an interesting dynamic!

**Evaluating ramp design**

I'm thinking about designing a very small entrance ramp that ensures a smooth entry. I should create a ramp starting from a height of 2 mm, with certain measurements related to the cup and wall thickness. I want the ramp to be thin, at 2 mm high at the edge, allowing the ball to climb easily. However, it seems like a straightforward design might actually be the best approach. Let’s simplify!