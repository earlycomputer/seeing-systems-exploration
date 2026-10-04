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

## What the full matrix showed (2026-10-04)

- **Text only was at the top.** Both models worked the flight out from the keyframe with drag. The left miss is
  a y velocity in the text, and edited qvels carry four decimals where the unedited scene keeps "3.21 0 9.3",
  so the text says whether the shot was changed (not which way). A next outcome test should edit the shot in a
  way the text cannot give away, or make the outcome depend on contacts.
- **Opus's quick estimate.** In 7 of its 9 wrong calls (all "long") Opus said the ball is "about 1 m above the
  rim" at the hoop's distance, a no-drag number, and described the picture as agreeing. Without drag that is
  roughly right; with drag the shot goes in. It integrated the drag carefully when it wrote the shot and when
  it had text only, but not when it had a picture to look at.
- **Pictures at 128 px were worse for Opus than at 64.** At 64 px it often said the picture was too coarse (or,
  for the left miss, that the camera looks along +y and cannot show it) and worked from the text. At 128 px it
  read the picture, and every run cited "both".
- **Opus's corrections from pictures land short.** All 12 failed first corrections fell 0.26 to 0.52 m short,
  and shown that short shot on turn 3 it said "goes in" 9 times. It over-corrects downward and then does not
  see the result.
- **GPT-6.1 Sol cites "both" almost always** (44 of 48 picture runs; "picture" alone 4 times). Its
  descriptions are short and pictorial ("descends beyond the hoop"), so the picture probably helps it agree
  with its own calculation, but this design cannot separate the two.
- **Another session added `viewer.py`** (every shot animated, every run's readback and words) while the
  matrix ran; merged, regenerated with all 144 runs. It changes no result.
