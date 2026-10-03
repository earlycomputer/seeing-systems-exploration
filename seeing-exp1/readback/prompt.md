You are checking a physics scene against the brief it was written from, by looking at a picture of it.

<brief>
{brief}
</brief>

{scene_section}

How the picture was made. A dot renderer drew the scene at t = 0, as written, before any simulation. Every
object's surface is covered in small dark dots on a white ground, shaded only by surface normal against
one light from above; dots on surfaces facing away from the camera are hidden. The camera is fixed: it
stands at ({eye}) m and looks at ({target}) m, with a {fovy} degree vertical field of view, so +x runs
left to right and slightly away from you, z is up, and you look down a little. The image below is
{res}x{res} pixels: a box-filtered grayscale downsample of the 512x512 rendering, so each of its pixels
averages {block}x{block} pixels of the original.
