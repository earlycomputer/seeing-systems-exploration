How the picture was made. MuJoCo simulated the shot, and a dot renderer drew the flight as residue: a
copy of the ball every {every} s from launch to its first landing, older copies lighter, the landing
darkest. Everything else is drawn once; it does not move. Every surface is covered in small dark dots on
a white ground, shaded only by surface normal against one light from above; dots on surfaces facing away
from the viewer are hidden.

The picture is a drafting view: two orthographic views stacked, with no perspective, sharing one scale of
{scale} pixels per metre, so x lines up between them. A thin gray rule separates them.
- Top band, side elevation, looking along +y: x runs left to right from {x0} to {x1} m, z runs up from
  {z0} to {z1} m.
- Bottom band, plan, looking down: x runs left to right over the same range, y runs up the page from {y0}
  to {y1} m. +y is the shooter's left when facing the hoop.

The image below is {res}x{res} pixels: a box-filtered grayscale downsample of the 512x512 rendering, so
each of its pixels averages {block}x{block} pixels of the original.
