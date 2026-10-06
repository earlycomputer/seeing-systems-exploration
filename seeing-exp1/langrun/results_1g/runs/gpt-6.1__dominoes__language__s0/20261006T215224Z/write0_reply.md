```world
world  ten dominoes falling in a row

floor
  size      3 m
  friction  0.8, spinning 0.001, rolling 0.0001

domino
  is a             box 2 by 8 by 20 cm, 200 g
  stands           on floor
  moves            freely
  friction         0.8, spinning 0.001, rolling 0.0001
  bounce           dead
  colour           white
  repeated         10 times, 8 cm apart along
  first one spins  8 rad/s about y

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

**Evaluating geometric spacing**

I’m considering the dense spacing limit, noting that it can jam under 15 if there’s only a vertical lean. Using the formula arcsin(d/h)=17.5 suggests we might be on track with d6 h20 yielding arcsin .3=17.46. However, I’m wondering if the geometry might actually be lower due to thickness factors. It seems I need to carefully evaluate how thickness plays into this setting—there are a lot of intricate details to think about!