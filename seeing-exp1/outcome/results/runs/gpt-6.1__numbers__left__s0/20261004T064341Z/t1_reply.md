The ball rises to about **4.11 m**, then descends past rim height near **(x, y, z) = (3.97, +0.36, 3.05) m**. The rim is centered at **(4, 0, 3.05) m**, with an inner radius of about **0.229 m**. The ball’s center is already outside that opening on the **+y side—left as the shooter sees it**.

It does **not** drop through. The leftward offset, about **0.36 m**, is much larger than the roughly **0.03 m** shortward offset. It continues beyond the hoop and lands near **(4.824, 1.091, 0.111) m**.

```json
{"description":"The ball rises to about 4.11 m, then descends through rim height near (3.97, +0.36, 3.05) m, left of the hoop opening. The leftward offset is much larger than the shortward offset. It lands near (4.824, 1.091, 0.111) m.","goes_in":false,"miss":"left","evidence":"both"}
```

---
thinking (summarized):

**Analyzing results**

I'm comparing a lateral miss of .36 to .03 short. I need to be careful with approximate interpolation after the collision, but it looks dense enough to show a clear left whole. At z, yes, the x ball plus .119 will straddle the left miss. There's evidence for both misses, so I think we have enough data here to make some conclusions. It feels like I've got a handle on this now!