Ten wooden dominoes, each 10 cm tall, stand 6 cm apart. That spacing is under the height, so each one reaches the next as it falls. The first starts with a forward spin about y, which tips its top along +x into domino2. The chain should end with each domino leaning on the next at about 35–40° and the last one lying flat. All of these clear the 15° minimum, but I haven't run the scene.

```world
world  domino chain

floor
  size      4 m
  friction  0.8, spinning 0.005, rolling 0.002

domino
  is a              box 1.5 by 5 by 10 cm, 50 g
  colour            wood
  friction          0.5, spinning 0.005, rolling 0.002
  moves             freely
  repeated          10 times, 6 cm apart along
  first one spins   5 rad/s about y
  stands            on floor, 0 m along

expect
  domino1 touches domino2
  domino9 touches domino10
```

---
thinking (summarized):

I'm sizing the dominoes at roughly 0.8 by 2.4 by 4.8 cm with spacing around 3 cm, and working out how an initial 4 rad/s spin about the y-axis would tip the first domino forward.

Since pivoting about its bottom edge means the center moves rather than staying fixed, I'm computing the resulting linear velocity from the cross product of angular velocity and the pivot-to-center vector, giving roughly 0.096 m/s forward and 0.016 m/s upward at 4 rad/s — checking whether this matches what "first one spins" implies versus a launched velocity.

Deciding that just spinning the first domino about its center at a few rad/s is enough, since friction will naturally cause it to pivot on the floor and topple into the next one, and verifying the tipping energy is small for a thin domino. I'm also working out spacing so the end-of-chain dominoes lean at a steep enough angle (using asin of spacing over height), and settling on slightly larger domino dimensions, mass, and friction values for stability in the simulator, placing the first domino at the origin and the rest spaced along the x-axis, with timing comfortably under the 6-second limit.

