```world
world  basketball shot from the floor

floor
  size      10 m
  friction  0.8, spinning 0.005, rolling 0.002

ball
  is a      sphere 12 cm radius, 624 g
  is        hollow, lively
  colour    orange
  rolls
  friction  0.8, spinning 0.005, rolling 0.002
  moves     freely
  rests     on floor, 0 m along
  launched  3.076923 m/s along, 8.630346 m/s up

hoop
  is a        hoop
  rim height  3.05 m
  rim size    45.72 cm
  tube        16 mm
  its rim 4 m beyond ball

expect
  ball drops through hoop
```

---
thinking (summarized):

**Considering basketball specifications**

I'm analyzing a basketball's dimensions and weight. A standard ball is 24 cm across, with a circumference of about 75.4 cm and a mass of 625 grams, which fits within NBA regulations. The hoop should be 45.72 cm in diameter, with an optional tube size. The rim's thickness isn't strictly necessary, but I’m considering what fits best. I'll confirm that the default configurations are suitable for my calculations.