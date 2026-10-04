MuJoCo ran your scene for {seconds} s from its start. Here is a picture of what happened.

How the picture was made. A dot renderer drew the run: every surface is covered in small dark dots on a
white ground, shaded only by surface normal against one light from above; dots on surfaces facing away from
the viewer are hidden. Everything that moved is drawn as residue: a copy of it every {dt} s from the start
to {end} s, older copies lighter, the last darkest. Everything that did not move is drawn once.

{view}

The image is {res}x{res} pixels: a box-filtered grayscale downsample of the 512x512 rendering, so each of
its pixels averages {block}x{block} pixels of the original.
