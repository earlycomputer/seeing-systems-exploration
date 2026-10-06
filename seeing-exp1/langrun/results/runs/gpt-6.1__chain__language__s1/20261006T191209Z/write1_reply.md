```parts
part rolling cup
  needs  length
  needs  width
  needs  walls
  needs  wall thickness, else 1 cm
  needs  base thickness, else 2 mm
  needs  near wall height, else 2 mm

  base
    is a      box length by width by base thickness
    on        floor
    friction  0.9, spinning 0.01, rolling 0.004
    bounce    dead
    colour    grey
  near wall
    is a      box wall thickness by width by near wall height
    on        floor, centred on base's near end
    friction  0.8, spinning 0.001, rolling 0.0001
    bounce    dead
    colour    grey
  far wall
    is a      box wall thickness by width by walls
    on        floor, centred on base's far end
    friction  0.9, spinning 0.01, rolling 0.004
    bounce    dead
    colour    grey
  left wall
    is a      box length by wall thickness by walls
    on        floor, centred on base's left side
    friction  0.9, spinning 0.01, rolling 0.004
    bounce    dead
    colour    grey
  right wall
    is a      box length by wall thickness by walls
    on        floor, centred on base's right side
    friction  0.9, spinning 0.01, rolling 0.004
    bounce    dead
    colour    grey
```

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
  is a              rolling cup
  length            36 cm
  width             24 cm
  walls             12 cm
  wall thickness    1 cm
  base thickness    2 mm
  near wall height  2 mm
  sits              on floor, 40 cm beyond ball3, 0 m to the left

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

---
thinking (summarized):

**Designing a custom cup**

I’m thinking about creating a custom "low entry cup" with specific measurements for length and width, and wall height set to some defaults: 1 cm, 2 mm for near height, and 2 mm overall. It seems clear enough, and the user isn’t asking for changes, just for the custom property. I’ll ensure to define the part with its base friction while keeping the rest of the walls unchanged. The requirements don't include any disallowed keys.