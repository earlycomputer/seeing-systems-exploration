Design {n} families of physics chain reactions that another AI will build in MuJoCo from a brief alone. You will not
build them. Each is judged by a hidden test that you also write.

Each family is one chain of 16 causal steps, each step set going by the one before. Then write it four times: as the
first 2 steps, the first 4, the first 8, and all 16. The shorter briefs are the same chain cut short: the same things
doing the same things in the same way, just fewer of them. That is the point of the experiment: only the length varies.

Steps are built only from these mechanisms (use at least five different ones in each family, and vary the families):

- a ball rolls down a ramp and hits something
- a ball, block or cart hits something and sets it moving
- a domino topples into the next thing
- a pendulum swings down and strikes something
- a hinged flap, door or lever is pushed and swings to a stop, releasing or knocking something
- a seesaw or lever is pushed down at one end and its other end lifts or launches something
- a cart slides along a slide joint and hits something
- a thing falls down through a hoop or ring
- a thing comes to rest in a cup, box or bin

Only rigid bodies, gravity, contact, hinges, slides and springs. Nothing soft, no liquids, no ropes, no motors that
steer. Every number the build depends on (a starting height, a distance, a mass) is in the brief.

For each version, name its things (lowercase, letters and digits only, such as `ball3`, `ramp1`, `flap2`; never a name
that starts with another thing's name followed by an underscore) and say for each whether it moves freely (`loose`),
turns on a hinge (`hinged`), slides on a slide joint (`sliding`) or never moves (`fixed`). Never name the floor; it is
always there, named `floor`. A shorter version names only the things its steps use, with the same names as the
16-step version.

The hidden test has exactly one line per step, in the order they happen, each in one of these forms exactly:

```
<thing> touches <thing>
<thing> comes to rest in <thing>
<thing> drops through <thing>
<thing> swings to a stop
```

- Each line is something that happens during the run: a touch that begins after the start, a thing coming to rest in
  a container it did not start in, a thing falling down through a ring or opening, a hinged thing swinging to an end
  of its range (say in the brief which way it swings, and test it by what it then does). Never a touch with `floor`.
- Lines closer than 0.1 s count as in order, so don't rely on the order of near-simultaneous events.
- `comes to rest in` means slower than 5 cm/s at the end of the run, inside the container's footprint and below its
  top. A version can only end with it as its last line.
- The test of each shorter version is exactly the first lines of the 16-step test, except that a `comes to rest in`
  line may only be the last line of the version it is in.
- Runs last {seconds_2} s for 2 steps, {seconds_4} s for 4, {seconds_8} s for 8 and {seconds_16} s for 16. Make the
  chain fit.

Each brief is plain sentences, one per step or two, short enough to read in one go.

Reply with one ```json block holding a list of {n} families:

{"family": "<short lowercase word>", "versions": {"2": {"brief": "...", "things": [{"name": "...", "kind": "loose|hinged|sliding|fixed", "what": "<a few words>"}], "test": ["..."]}, "4": {...}, "8": {...}, "16": {...}}}
