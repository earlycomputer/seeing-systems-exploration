The first ball rolls into the second at 0.07 s, and the second hits the third at 0.18 s. The third reaches the cup’s low entrance wall but stalls on it, then rolls backward and stops outside the cup. The collision chain works, but the final step does not.

This revision moves the cup closer, lowers its entrance lip, and reduces resistance inside it. It has not yet been checked by a run.

```world
world  three balls roll into a cup

floor
  size      4 m
  friction  0.6, spinning 0.005, rolling 0.003

ball1
  is a      sphere 6 cm radius, 200 g
  rolls
  bounce    lively
  friction  0.6, spinning 0.005, rolling 0.003
  colour    orange
  moves     freely
  sits      on floor, 0 cm along, 0 cm to the left
  launched  1.8 m/s along
  spins     30 rad/s about y

ball2
  is a      sphere 6 cm radius, 200 g
  rolls
  bounce    lively
  friction  0.6, spinning 0.005, rolling 0.003
  colour    white
  moves     freely
  sits      on floor, 24 cm beyond ball1, 0 cm to the left

ball3
  is a      sphere 6 cm radius, 200 g
  rolls
  bounce    lively
  friction  0.6, spinning 0.005, rolling 0.003
  colour    orange
  moves     freely
  sits      on floor, 24 cm beyond ball2, 0 cm to the left

cup
  is an            open box
  length           48 cm
  width            30 cm
  walls            18 cm
  wall thickness   1 cm
  base thickness   1 mm
  near wall height  1 mm
  bounce           dead
  friction         0.6, spinning 0.005, rolling 0.003
  colour           wood
  sits             on floor, 36 cm beyond ball3, 0 cm to the left

expect
  ball1 touches ball2
  ball2 touches ball3
  ball3 comes to rest in cup
```

```json
{
  "what_happens": "Ball1 rolls into ball2, which hits ball3; ball3 reaches the cup's entrance wall, stalls, rolls backward, and comes to rest outside the cup.",
  "works": false,
  "problem": "The third ball does not enter and come to rest in the cup."
}
```