Write {n} briefs for physics worlds that another AI will build in MuJoCo from the brief alone. You will not build
them. They will be judged by a hidden test that you also write.

Each brief is one or two plain sentences, like these from an earlier set:

- "a catapult throws a ball into a bucket whose centre is 3 m from where the ball starts"
- "three balls sit in a row on the floor; the first is rolled into the second, the second rolls into the third, and
  the third rolls into a cup"

Make these harder than those:

- 5 to 15 things in the world (balls, blocks, ramps, seesaws, hinged flaps, pendulums, cups, boxes, walls, hoops,
  springs, dominoes...), and a chain of at least three causes, each set going by the one before.
- Only rigid bodies, gravity, contact, hinges, slides and springs. Nothing soft, no liquids, no ropes, no motors
  that steer.
- Every number the test depends on is in the brief (a distance, a height, a mass), and nothing the test does not need.
- Vary them: no two with the same mechanism at their heart.

For each brief, name its things (lowercase, letters and digits only, such as `ball`, `ramp2`, `flap`), and say for each
whether it moves freely (`loose`), turns on a hinge (`hinged`), slides on a slide joint (`sliding`), or never moves
(`fixed`). Never name the floor; it is always there and named `floor`.

The hidden test is 3 to 6 lines, in the order they happen, each in one of these forms exactly:

```
<thing> touches <thing>
<thing> comes to rest in <thing>
<thing> drops through <thing>
<thing> reaches its lower stop
<thing> reaches its upper stop
```

Rules for the test:

- Each line is something that happens during the run: a touch that begins after the start, a thing coming to rest in
  a container it did not start in, a thing falling down through a ring or opening, a hinged thing swinging to the
  end of its range. Never a touch with `floor`.
- Every line must hold in any world that does what the brief says, and the lines together should fail any world that
  doesn't.
- `comes to rest in` means slower than 5 cm/s at the end of a {seconds} s run, inside the container's footprint and
  below its top. Make sure the brief leaves time for that.
- Use only the names you gave.

Reply with one ```json block holding a list of {n} objects:

{"id": "<short lowercase word>", "brief": "<the brief>", "things": [{"name": "<name>", "kind": "loose|hinged|sliding|fixed", "what": "<a few words>"}], "test": ["<line>", ...]}
