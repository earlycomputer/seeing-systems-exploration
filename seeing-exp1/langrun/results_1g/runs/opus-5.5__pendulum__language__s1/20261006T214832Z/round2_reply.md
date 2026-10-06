**What happens:** The pendulum is released from 40° and swings down. At 0.37 s the bob strikes the ball, which was resting on the floor at x = 0.10 m. The ball rolls along the floor at about 1.0 m/s and reaches the cup's low near lip at 1.16 s. It bumps the lip a few times, climbs over, and lands on the cup base at 1.33 s. The base's high rolling friction stops it at x = 1.03 m by 1.54 s, and it stays there until 6 s. The cup's centre is at x = 1.10 m, 1 m from where the ball started. The pendulum keeps swinging freely throughout.

**The fix worked:** The higher rolling friction on the cup now stops the ball inside the cup.

**One oddity:** the pendulum's rod is reported touching its own stand arm the whole run. It does not appear to slow the swing.

```json
{"what_happens": "The pendulum swings down from 40° and strikes the floor-resting ball at 0.37 s. The ball rolls about 1.0 m/s, climbs over the cup's low near lip at 1.16–1.33 s and stops on the cup base at x = 1.03 m by 1.54 s, staying at rest to the end. The cup's centre is 1 m from the ball's start at x = 0.10 m.", "works": true, "problem": ""}
```

---
thinking (summarized):

Checking the cup position one meter from the ball's start confirms the cup base centers correctly and the ball rests inside it at the right spot; the pendulum rod brushing the stand arm is a minor detail that doesn't affect the fixed setup, so this works.

