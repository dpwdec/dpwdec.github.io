---
title: Transitions
layout: page
exclude: true
---

You can **animate the properties of elements** using the `transition` function.
```js
d3
  .select("body")
  .transition()
  .style("background-color", "green");
```

You can **control the duration of a transition** using the `duration` function in milliseconds.
```js
d3
  .select("body")
  .transition()
  .duration(3000)
  .style("background-color", "green");
```

You can **control the easing of a transition** using the `ease` function. [D3 comes equipped with a range of easing curves that can be used to control the animation easing](https://github.com/d3/d3-ease).
```js
d3
  .select("body")
  .transition()
  .ease(d3.easeCubicOut)
  .style("background-color", "green");
```

