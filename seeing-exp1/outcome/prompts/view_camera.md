How the picture was made. MuJoCo simulated the shot, and a dot renderer drew the flight as residue: a
copy of the ball every {every} s from launch to its first landing, older copies lighter, the landing
darkest. Everything else is drawn once; it does not move. Every surface is covered in small dark dots on
a white ground, shaded only by surface normal against one light from above; dots on surfaces facing away
from the camera are hidden. The camera is fixed: it stands at ({eye}) m and looks at ({target}) m, with a
{fovy} degree vertical field of view, so +x runs left to right and slightly away from you, z is up, and you
look down a little. The image below is {res}x{res} pixels: a box-filtered grayscale downsample of the
512x512 rendering, so each of its pixels averages {block}x{block} pixels of the original.
