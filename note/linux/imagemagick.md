---
layout: page
exclude: true
title: Imagemagick
---

You can **convert an image sequence into a gif** by using the `convert` command on `imagemagick`. The `convert` command takes all files in the current folder with the `.png` extension and converts them into a single gif with a specified name.  The `delay` between frames is given in milliseconds. The `convert` command shown below is the direct command in the CLI and does not need to be pre-pended by the program name.

```
convert -delay <DELAY_AMOUNT> -loop 0 *.png <GIF_NAME>.gif
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDkzMDA0MjQ2XX0=
-->