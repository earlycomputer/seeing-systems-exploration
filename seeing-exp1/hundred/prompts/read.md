Here is a world, written for this brief:

<brief>
{brief}
</brief>

```{fmt}
{world}
```

{about}It will be simulated for {seconds} s exactly as written. Nothing else acts on it. Without running it, say for each
statement below whether it will hold in the run.

- "A touches B" holds when they come into contact some time after the start (already touching at the start and
  never parting does not count).
- "A comes to rest in B" holds when A moves slower than 5 cm/s at the end, inside B's footprint and below its top,
  and did not start there.
- "A drops through B" holds when A comes down through B's height within B's opening.
- "A reaches its lower (upper) stop" holds when A's hinge swings to the end of its range after leaving it.
- Each statement must also happen no earlier than the one above it.

<statements>
{statements}
</statements>

Reply with one ```json block holding a list of true or false, one per statement, in order. Nothing else is needed.
