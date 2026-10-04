# Notes

## Parking lot

Ideas that came up while building experiment 1b. Not in code; each needs a human before it becomes work.

- **A right miss.** The design has short, long and left only. A model that answers "right" for a left miss
  is caught, but there is no right miss to test the reverse.
- **Shots from a player's height.** The ball launches from the floor, as the design says ("from where it
  rests"). A real shot leaves the hands at about 2 m, which flattens the arc and changes how the misses look.
- **A stage with scale marks.** The drafting view gives exact positions in the prompt; the camera does not.
  Ground marks every metre (journal, open questions) would test whether a picture can carry its own scale.

## Building it

- MuJoCo's default air is twice as draggy as a real basketball's; see the README. The ellipsoid model's
  default blunt drag is the same. Both were measured on the authored scene before choosing.
- From the floor, a shot below about 57° reaches rim height near its apex and cannot come down into the
  hoop at all. Between 57° and 62°, a long miss banks in off the backboard even at +12%. Opus chose 71°,
  where +12% clears the board. A survey of launch angles 50° to 70°, with and without backspin, is in the
  build log, not in results.
- Clean makes are narrow: about 2% to 4% of launch speed at 62° to 70°. A real free throw's margin is
  similar, so ±8% is never close.
- Opus wrote the shot by integrating the drag equations by hand in its reasoning (RK2, about 16 steps) and
  predicted the ball would clear the front and back rim by about 7 cm. MuJoCo put it 1.4 cm from the center.
  That is a strong first data point for "text only": for a ballistic shot, thinking it through may be enough.

- **A harness bug the first batch found.** The check that a correction changed nothing but the keyframe
  counted an XML comment as a change. The correction prompt asks for a comment "after the key", and Opus
  put it just after `</keyframe>`, so a correction MuJoCo made (7 mm from the rim's center) was scored as
  a miss. Fixed by ignoring comments; `outcome/rescore.py` re-judged the saved files.

## What the pictures show, before any model has looked

From contact sheets of the base and each miss at 512, 128 and 64 px, made during the build (not committed):

- The camera barely shows a left miss: it moves along the camera's line of sight. The drafting plan view
  shows it clearly, as a path that kinks off the rim's left side.
- In the drafting side view the rim is edge-on, a short line about 2 px thick at 128 px and faint at 64.
  In the plan view it is a small circle.
- The short miss comes down through rim height 0.86 m in front of the rim and lands under the backboard,
  touching nothing. The long miss goes over the board and lands behind the pole.
