---
title: SVG
layout: page
exclude: true
---

You can **configure an attribute of an svg** using the `attr` function passing in a string representation of the property you want to configure and a closure or value that sets it. If a closure is used this takes an data bound to the element.
```js
d3
  .select("svg")
  .select("circle")
  .data(someData)
  .attr("cx", 5) // set a static value for attribute cx
  .attr("cy", d => d.field); // set a dynamic value based on data for cy
```