I expect the door to start 1.2 radians (about 69°) open and swing shut under the hinge spring’s torque. The damping should dissipate its motion, while the joint’s lower limit restricts travel past the shut position. It should settle effectively at `hinge = 0` well before 6 seconds and remain shut.

This is a prediction from the scene’s parameters, not an observed simulation.

```json
{
  "what_happens": "The initially open door swings shut under spring torque, settles with damping near hinge = 0, and stays shut.",
  "works": true,
  "problem": ""
}
```