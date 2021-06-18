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

You can **space HTML elements using white space** by adding the `pre` tag to the `white-space` property. By default **white space is collapsed by HTML displays** so you cannot easily space elements using a white space.
```css
p {
  white-space: pre;
}
```

## before / after

You can **add text content to a `before` / `after` relative tags** by enclosing the `content` inside `""` quote marks. If you don't include the content inside quote marks it will not be parsed as valid css.
```css
p::before {
  content: "some text"
}
```

## checkbox

You can **alter the styling of an element based on the state of a checkbox that is associated with it** by adding the `:checked` property to the `input[type="checkbox"]` followed by a `~` tilde character and then the element you want to style.
```css

```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMzg0NDI0NzM4LDcxMDA0MzQ2OSwyMDIwOD
E3Nzg4LC0xODUxMTAzNzcwLC00NzAyNzU1OThdfQ==
-->