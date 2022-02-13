---
title: Color
layout: page
exclude: true
---

You can **pass in an RGB representation of a color field** by using the built in `rgb` function of d3.
```js
d3
  .select("body")
  .style("background-color", d3.rgb(255, 0, 255)); // pink background color
```