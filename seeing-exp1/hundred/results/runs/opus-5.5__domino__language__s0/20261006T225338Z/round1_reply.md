## What happened in the run

- **Ramp and first two dominoes:** ball1 rolled down the ramp and reached the floor at about 1.1 m/s. It hit d1 at 1.89 s, d1 toppled d2, and d2 toppled d3 at 1.99 s.
- **d3 and ball2:** d3 reached ball2 at 2.05 s, when it was only about 27° over. It nudged ball2 just 2 cm along the shelf.
- **The jam:** d3 then stayed leaning on ball2. Its front face pressed down and forward on ball2's upper back, so ball2 was pinned against the shelf. ball2 never left the shelf or reached the cup.
- **Why:** my dead-bounce setting on ball2 soaked up the impact. The tight 6 cm domino spacing also let d2 settle onto d3, so d3 was moving slowly when it reached ball2.

## Changes in the corrected world

- **Domino spacing:** widened to 7 cm.
- **Shelf and ball2:** the shelf is raised to 6 cm and ball2 moved to about 8 cm ahead of d3's front edge. Now d3's top corner, not its face, should strike ball2 near its centre height, pushing almost horizontally, at about 36°, before d3 lands on the shelf edge at about 45°.
- **ball2:** no longer dead, lighter, and lower in friction.
- **Cup:** moved along to match, with its near wall the same height as the shelf.

I worked out the new geometry by hand and have not re-run it.

```world
world  ramp ball domino chain into cup

floor
  size      6 m
  friction  0.8, spinning 0.005, rolling 0.002

ramp top
  is a  point
  at    0 m along, 12 cm up

ramp foot
  is a  point
  at    1.2 m along, -2 cm up

ramp
  is a    plank from ramp top to ramp foot, 20 cm wide, 4 cm thick
  colour  wood
  friction  0.8, spinning 0.005, rolling 0.002

-- ball1 sits 1 m up the 1.21 m deck, measured from its low end
ball1
  is a      sphere 6 cm radius, 80 g
  rolls
  friction  0.8, spinning 0.005, rolling 0.002
  colour    orange
  moves     freely
  on ramp, 20.8 cm from the top

d1
  is a      box 1.5 by 6 by 10 cm, 50 g
  friction  0.4
  colour    white
  moves     freely
  stands    on floor, 1.45 m along

d2
  is a      box 1.5 by 6 by 10 cm, 50 g
  friction  0.4
  colour    white
  moves     freely
  stands    on floor, 1.52 m along

d3
  is a      box 1.5 by 6 by 10 cm, 50 g
  friction  0.4
  colour    white
  moves     freely
  stands    on floor, 1.59 m along

-- shelf whose near end is 6 cm ahead of d3's front face; d3's top corner strikes ball2 near its centre height
shelf
  is a      box 10 by 12 by 6 cm
  colour    grey
  friction  0.8, spinning 0.005, rolling 0.002
  on floor, 1.71 m along

ball2
  is a      sphere 2 cm radius, 15 g
  rolls
  friction  0.4, spinning 0.005, rolling 0.002
  colour    black
  moves     freely
  on shelf, 1.68 m along

-- cup's near wall is flush with the shelf's far end and as tall as the shelf
cup
  is an             open box
  length            14 cm
  width             12 cm
  walls             12 cm
  wall thickness    2 cm
  base thickness    5 mm
  near wall height  6 cm
  bounce            dead
  colour            wood
  its base 1.84 m along

expect
  ball1 touches d1
  d1 touches d2
  d2 touches d3
  d3 touches ball2
  ball2 comes to rest in cup
```

```json
{"what_happens": "ball1 rolls down the ramp and hits d1, d1 topples d2, and d2 topples d3. d3 reaches ball2 when it is only about 27 degrees over, nudges it 2 cm and then jams leaning on it. ball2 stays pinned on the shelf and never reaches the cup.", "works": false, "problem": "d3 met ball2 slowly with its face, and ball2's dead bounce plus the face pressing down on it left ball2 pinned on the shelf instead of knocked into the cup."}
```

---
thinking (summarized):

The chain mostly works but ball2 barely budges — d3 only pushes it 2 cm because the dominoes are spaced too close together, leaning on each other at shallow angles (66°, 60°, 40°) and losing most of their energy before the final impact.

I could lower friction between ball2 and the dominoes specifically to prevent the jam, while keeping floor friction high enough that dominoes don't slip — since MuJoCo uses the max of paired friction coefficients, I need to balance ball2, domino, and shelf/floor values carefully. The deeper issue is likely spacing: at 6 cm with 4.5 cm gaps the dominoes are toppling into each other at steep, awkward angles instead of clean strikes, so widening to something like 7 cm might give better contact geometry.

That confirms the jam from friction, possibly worsened by soft contact stickiness in MuJoCo. I should reconsider the geometry entirely—maybe position ball2 so the domino's face strikes it with a more horizontal normal earlier in the fall, or rethink hitting it near the floor where the top corner rather than the face makes contact.

Actually, the real culprit might be the restitution setting: with ball2's bounce marked dead, the collision absorbs momentum instead of transferring it cleanly, so d3 sticks rather than knocking ball2 away. Making ball2 more elastic could let it pop off properly instead of getting stuck.

I'm now considering heavier dominoes with wider spacing (7.5cm, gap of 6) so d3 builds more angular velocity before impact, hitting ball2 at a steeper angle. That would require repositioning the shelf lower, and maybe shrinking ball2's radius with less friction so it rolls freely once struck. I'm also weighing whether to scrap the shelf entirely and put ball2 directly on the floor ahead of d3, though that raises its own entry alignment problems.

I'm now running the geometry for a shelf height of 2 cm with ball2's radius at 2 cm, computing where d3 should contact the ball at roughly a 45° angle so the normal force direction works out, and checking that the domino still clears the shelf's corner (reaching it around 67°, leaving good margin after the ball strike).

I'm weighing whether a lower contact angle like 30° gives better horizontal push despite making the domino swing slower, and considering an alternative design where ball2 sits at a height so the domino's top corner strikes the ball right at its center for a more direct horizontal impulse.

Checking the geometry shows the face would already overlap before reaching that angle, so it's actually the corner that makes contact first, at roughly 36° with the normal angled slightly downward. That means the domino tips further until its falling face reaches the shelf's near corner, so I need to check where that contact angle falls relative to the shelf edge position.

After the corner hit, the domino likely comes to rest against the shelf around 45°, but the real question is the impact speed delivered to the ball — probably around 0.5 m/s in a typical chain reaction. Since the original setup had a dead bounce causing a jam, removing that and using a clean corner strike with a mostly horizontal normal should launch the ball at 0.3-0.5 m/s, letting it roll along the shelf and drop into the cup positioned near the wall with the ball settling inside above the cup's base.

I'm recalculating positions with the spacing increased to 7 cm — tracking domino front edges, ball center placement on the shelf, and working out where the shelf and cup walls land relative to the ball's landing point to make sure everything lines up for the ball to drop cleanly into the cup.

Setting ball2's friction to 0.4 with rolling resistance 0.002, checking that domino-ball and ball-shelf friction pairs stay reasonable, and confirming ball2 rolls 7.5 cm across the shelf and over the near wall edge at a safe speed to drop into the cup. I'm also double-checking that ball1 strikes d1 above its center of mass and that d3's height still clears the corner path.

Now verifying that d3 tips fast enough at 36° after the chain reaction, considering spacing d2 to d3 at 7 cm for more transferred energy, and settling on ball2's mass at 15 g rather than lightening it further. I still need to check the shelf corner contact point on d3 at 45° after it's struck by the ball, confirm ball2's starting position at 8 cm (6 cm shelf plus 2 cm offset), and make sure ball1's initial setup remains unaffected before writing out the world file.

