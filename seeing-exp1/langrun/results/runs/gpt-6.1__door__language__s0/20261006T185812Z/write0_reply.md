```world
world  self closing door

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

frame
  is a    box 8 by 8 by 214 cm
  stands  on floor, 12 cm to the right
  colour  grey

door
  is a           box 4 by 90 by 200 cm, 12 kg
  raised         2 cm
  8 cm outside frame's left side
  colour         wood
  turns on       hinge, about z, at its right side
  swings         from 0° to 100°
  spring         40 N·m/rad toward -5°
  damping        22 N·m·s/rad
  starts turned  75°

expect
  door reaches its lower stop
```

---
thinking (summarized):

**Designing door mechanics**

I'm focusing on building a sensible door that closes properly, with a hinge at the top. I want to use a spring that targets a slight negative angle of about -5°. The dimensions are specific, and I need to ensure the door closes in around 1.6 seconds when pressed. The spring setup should have a preload to hold the door closed, adjusted for small penetrations within a very slight threshold. Finally, I’m designing a simple frame for this door.

**Designing door mechanics**

I'm working on a primitive door setup that’s raised 2 cm and placed 8 cm outside the frame on the left side. It needs to generate a pivot gap without any collisions. The frame will be positioned at a specific range, and I want to ensure the door swings without hitting anything at a positive range, ideally less than or equal to 90 degrees. I also want to include a latch on the opposite side and incorporate a spring mechanism targeting a negative angle of about -5°.

**Defining door specifications**

I need to think about ensuring the door reaches its lower stop reliably. It's important to name the door clearly as a primitive design. I plan to use a post frame that matches the library style and to apply the correct door mass. The floor height is 6, with the door mass set at 12. For the door's mechanics, I have an inertia of 3.24, an angle of 80 degrees, a spring constant of 40, and a damping coefficient of 22.