MuJoCo ran a world for {seconds} s, written for this brief:

<brief>
{brief}
</brief>

{evidence}

Answer from what is above. Things are named as in the world; `floor` is the ground.

<questions>
{questions}
</questions>

Reply with one ```json block holding a list of answers, one per question, in order: `true` or `false` where a question
asks yes or no, a thing's name or `"none"` where it asks which thing, and a number of seconds or `"never"` where it
asks when.
