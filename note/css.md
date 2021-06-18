---
title: CSS
layout: page
exclude: true
---

## Alignment

You can **put two `div`s on the same line** using the `float` css indicator. In the example below, `div`s with the `id="same-line"` will float next to each other rather than being separated by a line break.
```css
#same-line {
  float: left;
}
```

You can **form a `div` onto a new line** using the `clear` indicator. `Div`s with the `id="new-line"` from the example below will be pushed down onto a new line away from any `float`ing counterparts.
```css
#new-line {
  clear: left
}
```

You can **horizontally centre a div** by setting `margin` to `auto`.
```css
div {
  margin: auto
}
```

By default **white space is stripped by HTML displays** meaning that trying to add element spacing 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4NTExMDM3NzAsLTQ3MDI3NTU5OF19
-->