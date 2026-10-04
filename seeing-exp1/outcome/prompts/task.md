Does the shot drop through the hoop? If not, which way does it miss: short (it falls before reaching the
hoop), long (it goes past the hoop), or left or right (as the shooter sees it, facing the hoop along +x,
so left is +y)? If it misses in more than one way, name the larger.

First say what you {look_verb}: where the ball goes and where it ends up. Then end your reply with a
```json block holding one object:

{"description": "<what you {look_verb}>", "goes_in": <true or false>, "miss": <"none", "short", "long", "left" or "right">, "evidence": <{evidence}>}

`evidence` says where your answer came from.
