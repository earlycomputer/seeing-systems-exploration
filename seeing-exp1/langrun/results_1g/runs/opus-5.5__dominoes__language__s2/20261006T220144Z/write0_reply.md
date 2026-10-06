Ten wooden dominoes, each 1 cm thick, 4 cm wide and 8 cm tall, stand 5 cm apart. The first one starts with a forward spin about y so its top tips toward the rest.

- **Why each domino reaches the next:** the faces are 4 cm apart. A falling domino's top strikes the next one at about 30° of tilt.
- **Why every domino should end past 15°:** the dominoes left leaning on their neighbours should settle at 30° or more, and the last one should lie flat.

```world
world  ten dominoes

floor
  size      4 m
  friction  0.7, spinning 0.005, rolling 0.002

domino
  is a              box 1 by 4 by 8 cm, 20 g
  colour            wood
  friction          0.5, spinning 0.005, rolling 0.002
  moves             freely
  repeated          10 times, 5 cm apart along
  first one spins   5 rad/s about y
  stands            on floor, 50 cm along

expect
  domino1 touches domino2
  domino2 touches domino3
  domino3 touches domino4
  domino4 touches domino5
  domino5 touches domino6
  domino6 touches domino7
  domino7 touches domino8
  domino8 touches domino9
  domino9 touches domino10
```

---
thinking (summarized):

I'm sketching the domino dimensions and spacing—roughly 1cm thick, 4cm wide, 8cm tall blocks set about 5cm apart—and planning for the first domino to start with a spin around the y-axis to kick off the chain reaction.

Now I'm working through the geometry of how each falling domino leans against the next: with a 4cm gap between faces and 8cm height, the tilt angle where one domino's top edge contacts the next works out to about 30 degrees, and I'm checking that the final domino should end up flat against the floor while earlier ones rest leaning at shallower angles.

For physical parameters, I'm using wood density to get roughly 20g per domino, setting floor friction around 0.6 so the bases don't slide, and giving the first domino a spin of about 5 rad/s about the y-axis since the energy needed to tip it over its corner is tiny compared to that. I'm laying out the dominoes 5cm apart starting 50cm along, with ten repeated instances.

For expectations, I'll describe the chain reaction as each domino touching the next in sequence, down through domino9 touching domino10, plus the last one touching the floor. Then I'll color the dominoes wood-toned and finish up.

