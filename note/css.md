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
> Written with [StackEdit](https://stackedit.io/).
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ3MDI3NTU5OF19
-->